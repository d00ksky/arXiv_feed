
def normalize_paper(raw_paper: dict) -> dict:
    """
    raw_paper ma klucze: id, title, authors, published
    zwraca: id, title, authors, year (int)
    """
    normalized_result = {}    
    normalized_result["id"] = str(raw_paper["id"])
    normalized_result["title"] = str(raw_paper["title"])
    normalized_result["authors"] = list(raw_paper["authors"])
    normalized_result["year"] = int(raw_paper["published"][:4])
    
    return normalized_result


def normalize_papers(raw_papers: list[dict]) -> list[dict]:
    normalized_papers = []

    for raw_paper in raw_papers:
        normalized_papers.append(normalize_paper(raw_paper))
        
    return normalized_papers

