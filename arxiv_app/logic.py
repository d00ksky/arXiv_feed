
# n
from operator import attrgetter

def filter_papers_after_year(papers, year):
    papers_after = []
    for paper in papers:
        if paper["year"] > year:
            papers_after.append(paper)
    return papers_after



def extract_titles(papers):
    titles = []
    for paper in papers:
        titles.append(paper["title"])
    return titles



def get_titles_after_year(papers, year):
    papers_after = filter_papers_after_year(papers, year)
    titles_after = extract_titles(papers_after)
    return titles_after
    


def limit_results(items, limit):
    limited_result = []
    for i in range(limit):
        if i < len(items):
            limited_result.append(items[i])
    return limited_result



def get_limited_titles_after_year(papers, year, limit):
    titles_after = get_titles_after_year(papers, year)
    limited = limit_results(titles_after, limit)
    return limited



def format_authors(authors):
    authors = []
    formatted_authors = ""
    for i in range(len(authors)):
        if i > 0:
            formatted_authors = formatted_authors + ", "
        formatted_authors = formatted_authors + authors[i]
    return formatted_authors


 
def filter_papers_by_author(papers, author_query):
    filtered = []
    for paper in papers:
        for author in paper["authors"]:
            if author_query.lower() in author.lower():
                filtered.append(paper)
                break
                
    return filtered




def titles_by_year(papers: list[dict]) -> dict[int, list[str]]:
    filtered = {}
    for paper in papers:
        year = paper["year"]
        title = paper["title"]
        if year not in filtered:
            filtered[year] = []
        filtered[year].append(title)
    return filtered
            
            



class Paper:
    def __init__(self, title: str, year: int, citations: int, authors: str):
        self.title = title
        self.year = year
        self.citations = citations
        self.authors = authors
        
papers1 = [
    Paper("A", 2023, 15, "authorA"),
    Paper("B", 2022, 40, "authorB"),
    Paper("C", 2023, 5, "authorC"),
    ]
        

papers = [
    {"title": "Deep Learning for Vision", "authors": ["Y. LeCun", "A. Smith"]},
    {"title": "Quantum Computing Basics", "authors": ["John Doe"]},
    {"title": "Neural Networks in Medicine", "authors": ["A. Smith", "K. Patel"]},
] 

def has_author(papers: list[dict], author: str) -> bool:
    author_lower = author.lower()      
    return any(
        any(author_lower in author_name.lower() for author_name in paper["authors"])
        for paper in papers
        )
        
def count_papers_by_author(papers: list[Paper], author: str) -> int:
    return len(papers_by_author(papers, author))

def top_author_papers(papers: list[Paper], author: str, n: int) -> list[Paper]:
    top_authors = sorted(papers_by_author(papers, author), key=lambda paper: paper.citations, reverse=True)
    return top_authors[:n]
  
        
def papers_by_author(papers: list[Paper], author: str) -> list[Paper]:
    return [paper for paper in papers if any(author.lower() in a.lower() for a in paper.authors)]
       
        
def top_papers_by_year(papers: list[Paper], year: int) -> list[str]:
    papers_from_year = [paper for paper in papers if paper.year == year]
    sorted_papers = sorted(
        papers_from_year, 
        key=lambda paper: paper.citations, 
        reverse=True
        )
    return [paper.title for paper in sorted_papers]


def top_n_papers(papers: list[Paper], n: int) -> list[Paper]:
    sorted_papers = sorted(papers, key=attrgetter("citations"), reverse=True)
    return sorted_papers[:n]


def top_papers_from_year(papers: list[Paper], year: int, n: int) -> list[Paper]:
    papers_from_year = [paper for paper in papers if paper.year == year]
    top_papers = sorted(papers_from_year, key=lambda paper: paper.citations, reverse=True)
    return top_papers[:n]
    
def search_papers_by_keyword(papers: list[Paper], keyword: str) -> list[Paper]:
    papers_with_keyword = [paper for paper in papers if keyword.lower() in paper.title.lower()]
    return papers_with_keyword

def search_and_rank(
    papers: list[Paper],
    keyword: str,
    n: int
) -> list[Paper]:
    sorted_with_keyword = sorted(search_papers_by_keyword(papers, keyword), key=lambda paper: paper.citations, reverse=True)
    return sorted_with_keyword[:n]
    ...

class Book:
    def __init__(self, title: str, pages: int, rating: float):
        self.title = title
        self.pages = pages
        self.rating = rating
        
        
        
books = [
    Book("Clean Code", 464, 4.5),
    Book("The Pragmatic Programmer", 352, 4.7),
    Book("Fluent Python", 790, 4.8),
    Book("The Mythical Man-Month", 322, 4.2),
]


def top_books_by_rating(books: list[Book]) -> list[str]:
    sorted_books = sorted(books, key=lambda book: book.rating, reverse=True )
    sorted_titles = [book.title for book in sorted_books]
    return sorted_titles
    
result = top_books_by_rating(books)
print(result)