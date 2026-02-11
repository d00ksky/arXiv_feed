from arxiv_client import fetch_papers

def normalize_paper(raw_paper: dict) -> dict:
    """
    raw_paper ma klucze: id, title, authors, published
    zwraca: id, title, authors, year (int)
    """
