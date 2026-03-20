from models import Paper

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