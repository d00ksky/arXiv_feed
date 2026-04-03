from arxiv_app.models import Paper


def normalize_paper(raw_paper: dict) -> Paper:
    """
    raw_paper ma klucze: id, title, authors, published
    zwraca: id, title, authors, year (int)
    """
    
    return Paper(
        title = str(raw_paper["title"]),
        year = int(raw_paper["published"][:4]),
        citations = 0,
        authors = list(raw_paper["authors"]),
        id = str(raw_paper["id"]),
        summary = str(raw_paper["summary"])
    )


def normalize_papers(raw_papers: list[dict]) -> list[Paper]:
    normalized_papers = []

    for raw_paper in raw_papers:
        normalized_papers.append(normalize_paper(raw_paper))
        
    return normalized_papers

