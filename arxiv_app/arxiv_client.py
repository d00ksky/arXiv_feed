import urllib.request
import xml.etree.cElementTree as ET
import json
import sys

# n


def fetch_papers(query: str, max_results: int =10) -> list[dict]:
    URL = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"

    with urllib.request.urlopen(URL) as response:
        xml_bytes = response.read()

    xml_text = xml_bytes.decode("utf-8")

    ns = {"a": "http://www.w3.org/2005/Atom"}

    root = ET.fromstring(xml_text)

    entries = root.findall("a:entry", ns)
    
    papers = []
    
    

    for entry in entries: 
        pub_elem = entry.find("a:published", ns)
        if pub_elem is None or pub_elem.text is None:
            continue
        pub = pub_elem.text.strip()
        title_elem = entry.find("a:title", ns)
        if title_elem is None or title_elem.text is None:
            continue
        title = title_elem.text.strip()
        title_elem_id = entry.find("a:id", ns)
        if title_elem_id is None or title_elem_id.text is None:
            continue
        title_id = title_elem_id.text.strip()
        authors = []
        for author in entry.findall("a:author", ns):
            name_elem = author.find("a:name", ns)
            if name_elem is None or name_elem.text is None:
                continue
            name = name_elem.text.strip()
            authors.append(name)
        paper = {
            "id": title_id, 
            "title": title, 
            "authors": authors,
            "published": pub
            }
        papers.append(paper)
        
    return papers
 
 

        
