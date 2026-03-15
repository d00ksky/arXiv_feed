
# n
from models import Paper
#Old dict functions
#____________________________________________________________________________

def filter_papers_after_year(papers: list[Paper], year: int) -> list[Paper]:
    papers_after = []
    for paper in papers:
        if paper.year > year:
            papers_after.append(paper)
    return papers_after



# def extract_titles(papers: list[Paper]) -> list[str]:
#     titles = []
#     for paper in papers:
#         titles.append(paper.title)
#     return titles

def extract_titles(papers: list[Paper]) -> list[str]:
    """Return titles extracted from a list of papers."""
    return [paper.title for paper in papers]


def get_titles_after_year(papers: list[Paper], year: int) -> list[str]:
    """Returns papers published after a given year."""
    papers_after = filter_papers_after_year(papers, year)
    titles_after = extract_titles(papers_after)
    return titles_after
    


def limit_results(items: list, limit: int) -> list:
    return items[:limit]



def get_limited_titles_after_year(papers: list[Paper], year: int, limit: int) -> list[str]:
    titles_after = get_titles_after_year(papers, year)
    limited = limit_results(titles_after, limit)
    return limited


 
def filter_papers_by_author(papers: list[Paper], author_query: str) -> list[Paper]:
    filtered = []
    for paper in papers:
        for author in paper.authors:
            if author_query.lower() in author.lower():
                filtered.append(paper)
                break
                
    return filtered




def titles_by_year(papers: list[Paper]) -> dict[int, list[str]]:
    filtered = {}
    for paper in papers:
        year = paper.year
        title = paper.title
        if year not in filtered:
            filtered[year] = []
        filtered[year].append(title)
    return filtered
            

#____________________________________________________________________________

# TODO: little refactor to continue / maybe divide functions into smaller modules than one big logic.py

            
def format_authors(authors):
    return ", ".join(authors)
                                                                 



def most_cited_papers(papers: list[Paper], n: int = 5) -> list[Paper]:
    sorted_papers = sorted(papers, key=lambda paper: paper.citations, reverse=True)
    return sorted_papers[:n]
        


def top_authors(papers: list[Paper], n: int = 5) -> list[tuple[str, int]]:
    authors_counts = {}
    for paper in papers:
        for author in paper.authors:
            if author not in authors_counts:
                authors_counts[author] = 0
            authors_counts[author] += 1
    authors_sorted = sorted(authors_counts.items(), key=lambda author: author[1], reverse=True)
    return authors_sorted[:n]
                
        
    

def group_papers_by_year(papers: list[Paper]) -> dict[int, list[Paper]]:
    """Returns dictionary of papers grouped by year of publication"""
    groups = {}
    for paper in papers:
        if paper.year not in groups:
            groups[paper.year] = []
        groups[paper.year].append(paper)
    return groups


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


def newest_paper(papers: list[Paper]) -> Paper | None:
    """Returns paper with newest date from papers"""
    return max(
        papers, 
        key=lambda x: x.year,
        default=None
        )

def papers_by_author(papers: list[Paper], author: str) -> list[Paper]:
    """Returns list of papers published by given author"""
    return [paper for paper in papers if any(author.lower() in a.lower() for a in paper.authors)]

#This one for future if we need for reference old version of papers_by_author_sorted
#
# def papers_by_author_sorted(papers: list[Paper], author: str) -> list[Paper]:
#     author_lower = author.lower()
#     return sorted(
#         (paper for paper in papers 
#          if any(author_lower in author_name.lower() for author_name in paper.authors))
#          , key=lambda x: x.year, 
#         reverse=True
#         )

def papers_by_author_sorted(papers: list[Paper], author: str) -> list[Paper]:
    """Returns list of papers for a given author sorted by year"""
    author_lower = author.lower()
    return sorted(
        papers_by_author(papers, author), 
        key=lambda paper: paper.year, 
        reverse=True
        )


def has_author(papers: list[Paper], author: str) -> bool:
    author_lower = author.lower()      
    return any(
        any(author_lower in author_name.lower() for author_name in paper.authors)
        for paper in papers
        )
        
def count_papers_by_author(papers: list[Paper], author: str) -> int:
    return len(papers_by_author(papers, author))

def top_author_papers(papers: list[Paper], author: str, n: int) -> list[Paper]:
    top_author_papers = sorted(papers_by_author(papers, author), key=lambda paper: paper.citations, reverse=True)
    return top_author_papers[:n]
       
        
def top_papers_by_year(papers: list[Paper], year: int) -> list[str]:
    papers_from_year = [paper for paper in papers if paper.year == year]
    sorted_papers = sorted(
        papers_from_year, 
        key=lambda paper: paper.citations, 
        reverse=True
        )
    return [paper.title for paper in sorted_papers]


def top_papers_from_year(papers: list[Paper], year: int, n: int) -> list[Paper]:
    papers_from_year = [paper for paper in papers if paper.year == year]
    top_papers = sorted(papers_from_year, key=lambda paper: paper.citations, reverse=True)
    return top_papers[:n]
    
def search_papers_by_keyword(papers: list[Paper], keyword: str) -> list[Paper]:
    """Returns paper searched by keyword"""
    return [paper for paper in papers if keyword.lower() in paper.title.lower()]

def search_and_rank(
    papers: list[Paper],
    keyword: str,
    n: int
) -> list[Paper]:
    """Returns papers for given keyword and sort them by citations"""
    sorted_with_keyword = sorted(search_papers_by_keyword(papers, keyword), key=lambda paper: paper.citations, reverse=True)
    return sorted_with_keyword[:n]
    


def recent_papers(papers: list[Paper], n: int = 5) -> list[Paper]:
    """
    Returns n most recent papers sorted by year and by citations for papers in that same year
    """
    return sorted(papers, key=lambda paper: (paper.year, paper.citations), reverse=True)[:n]
    
    ...
    
