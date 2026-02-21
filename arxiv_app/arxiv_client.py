import urllib.request
import urllib.error
import xml.etree.cElementTree as ET
import time
import os
from urllib.parse import quote_plus


def _is_cache_fresh(path: str, ttl_seconds: int) -> bool:
    if not os.path.exists(path):
        return False
    
    modified_time = os.path.getmtime(path)
    age = time.time() - modified_time 
    return age < ttl_seconds



def _cache_path(query: str, max_results: int) -> str:
    os.makedirs("cache", exist_ok=True)
    safe_query = query.replace(" ", "_")
    filename = f"{safe_query}_{max_results}.xml"
    return os.path.join("cache", filename)

# n

def _parse_xml(xml_bytes: bytes) -> list[dict]:
    xml_text = xml_bytes.decode("utf-8")
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries = root.findall("a:entry", ns)


    papers = []
    for entry in entries:
        pub_elem = entry.find("a:published", ns)
        title_elem = entry.find("a:title", ns)
        id_elem = entry.find("a:id", ns)
        if (
            pub_elem is None or pub_elem.text is None or
            title_elem is None or title_elem.text is None or
            id_elem is None or id_elem.text is None
        ):
            continue

        authors = []
        for author in entry.findall("a:author", ns):
            name_elem = author.find("a:name", ns)
            if name_elem is not None and name_elem.text is not None:
                authors.append(name_elem.text.strip())

        papers.append({
            "id": id_elem.text.strip(),
            "title": title_elem.text.strip(),
            "authors": authors,
            "published": pub_elem.text.strip(),
        })

    return papers



def fetch_papers(query: str, max_results: int =10, cache_ttl: int = 600) -> list[dict]:
    encoded_query = quote_plus(query)
    url = (
        f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={max_results}"
    )
    headers = {
        "User-Agent": "arxiv-app/0.1 (contact: debski.jakub@gmail.com)",
        "From": "debski.jakub@gmail.com",
    }
    
    cache_path = _cache_path(query, max_results)
    TTL = cache_ttl
    
    # retry/backoff
    max_attempts = 6
    delay = 1.0  # start 1s

    xml_bytes = None
    last_err = None

    if _is_cache_fresh(cache_path, TTL):
        with open(cache_path, 'rb') as f:
            xml_bytes = f.read()

    else:  
        for attempt in range(1, max_attempts + 1):
            req = urllib.request.Request(url, headers=headers, method="GET")
            try:
                with urllib.request.urlopen(req, timeout=20) as response:
                    xml_bytes = response.read()
                with open(cache_path, 'wb') as f:
                    f.write(xml_bytes)
                last_err = None
                break
            except urllib.error.HTTPError as e:
                last_err = e
                if e.code in (429, 503):
                    retry_after = e.headers.get("Retry-After")
                    if retry_after is not None:
                        try:
                            wait_s = float(retry_after)
                        except ValueError:
                            wait_s = delay
                    else:
                        wait_s = delay

                    time.sleep(wait_s)
                    delay = min(delay * 2, 30.0)  # cap 30s
                    continue
                raise  # inne kody: nie udajemy, że wiemy lepiej
            except Exception as e:
                last_err = e
                time.sleep(delay)
                delay = min(delay * 2, 30.0)

  
        if xml_bytes is None:
            raise last_err if last_err is not None else RuntimeError("fetch_papers failed")



    return _parse_xml(xml_bytes)
 

        
