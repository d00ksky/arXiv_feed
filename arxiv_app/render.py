from logic import (
    extract_titles,
    format_authors
)

def render_paper_line(index: int, paper: dict) -> str:
    """
    Returns: '1. (2025) Title — Author1, Author2'
    """
    title = paper["title"]
    authors = paper["authors"]
    result = str(title) + str(authors)
    return result
