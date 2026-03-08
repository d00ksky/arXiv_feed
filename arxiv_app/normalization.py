from models import Paper


def normalize_paper(raw_paper: dict) -> Paper:
    """
    raw_paper ma klucze: id, title, authors, published
    zwraca: id, title, authors, year (int)
    """
    
    return Paper(
        title = str(raw_paper["title"]),
        year = int(raw_paper["year"]),
        citations = int(raw_paper["citations"]),
        authors = list[str](raw_paper["authors"])
    )


def normalize_papers(raw_papers: list[dict]) -> list[Paper]:
    normalized_papers = []

    for raw_paper in raw_papers:
        normalized_papers.append(normalize_paper(raw_paper))
        
    return normalized_papers

