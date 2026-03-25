from arxiv_app.models import Paper
from collections import Counter

def unique_authors(papers: list[Paper]) -> set[str]:
    """Returns a set of all unique authors."""
    authors = set()
    for paper in papers:
        for author in paper.authors:
            authors.add(author)
    return authors


def count_papers_by_year(papers: list[Paper]) -> dict[int, int]:
    """Returns count of papers for each year from papers"""
    counts = {}
    
    for paper in papers:
        year = paper.year
        counts[year] = counts.get(year, 0) + 1
    return counts 

def most_common_author(papers: list[Paper]) -> str | None:
    authors_count = Counter(
        author for paper in papers for author in paper.authors
        )
            
    if not authors_count:
        return None
    
    return authors_count.most_common(1)[0][0]


def top_n_authors(papers: list[Paper], n: int) -> list[tuple[str, int]]:
    return Counter(author for paper in papers for author in paper.authors).most_common(n)