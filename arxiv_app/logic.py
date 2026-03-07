
# n
from operator import attrgetter
from dataclasses import dataclass


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
            
            

                                                                 
@dataclass
class Paper:
    title: str
    year: int
    citations: int
    authors: list[str]
    
    
    
    
    
# papers2 = [
#     Paper("A", 2023, 15, "authorA"),
#     Paper("B", 2022, 40, "authorB"),
#     Paper("C", 2023, 5, "authorC"),
#     ]
        

papers1 = [
    {"title": "Deep Learning for Vision", "authors": ["Y. LeCun", "A. Smith"]},
    {"title": "Quantum Computing Basics", "authors": ["John Doe"]},
    {"title": "Neural Networks in Medicine", "authors": ["A. Smith", "K. Patel"]},
] 


papers = [
    Paper("Deep Learning for Vision", 2021, 12000, ["Y. LeCun", "A. Smith"]),
    Paper("Neural Networks in Medicine", 2023, 450, ["A. Smith", "K. Patel"]),
    Paper("Transformers in NLP", 2020, 25000, ["A. Vaswani", "Y. LeCun"]),
    Paper("Quantum Computing Basics", 2019, 300, ["John Doe"]),
    Paper("Large Language Models", 2024, 800, ["A. Smith", "John Doe"]),
    Paper("AI in Healthcare", 2022, 600, ["K. Patel", "A. Smith"]),
]


def most_cited_papers(papers: list[Paper], n: int = 5) -> list[Paper]:
    sorted_papers = sorted(papers, key=lambda paper: paper.citations, reverse=True)
    return sorted_papers[:n]
        
    ...


def authors_count(papers: list[Paper], n: int = 5) -> list[tuple[str, int]]:
    authors_count = {}
    for paper in papers:
        for author in paper.authors:
            if author not in authors_count:
                authors_count[author] = 0
            authors_count[author] += 1
    authors_sorted = sorted(authors_count.items(), key=lambda author: author[1], reverse=True)
    return authors_sorted[:n]
                
        
    ...

def group_papers_by_year(papers: list[Paper]) -> dict[int, list[Paper]]:
    groups = {}
    for paper in papers:
        if paper.year not in groups:
            groups[paper.year] = []
        groups[paper.year].append(paper)
    return groups


def unique_authors(papers: list[dict]) -> set[str]:
    authors = set()
    for paper in papers:
        for author in paper["authors"]:
            authors.add(author)
    return authors


def count_papers_by_year(papers: list[dict]) -> dict[int, int]:
    counts = {}
    
    for paper in papers:
        year = paper["year"]
        if year not in counts:
            counts[year] = 0
        counts[year] += 1
    return counts


def newest_paper(papers: list[dict]) -> dict | None:
    return max(
        papers, 
        key=lambda x: x["year"],
        default=None
        )

def papers_by_author_sorted(papers: list[dict], author: str) -> list[dict]:
    author_lower = author.lower()
    return sorted(
        (paper for paper in papers 
         if any(author_lower in author_name.lower() for author_name in paper["authors"]))
         , key=lambda x: x["year"], 
        reverse=True
        )


def filter_by_author(papers: list[dict], author: str) -> list[dict]:
    author_lower = author.lower()
    return [
        paper for paper in papers 
        if any(author_lower in author_name.lower() for author_name in paper['authors'])
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
    authors_count = sorted(papers_by_author(papers, author), key=lambda paper: paper.citations, reverse=True)
    return authors_count[:n]
  
        
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
    
def search_papers_by_keyword2(papers: list[Paper], keyword: str) -> list[Paper]:
    papers_with_keyword = [paper for paper in papers if keyword.lower() in paper.title.lower()]
    return papers_with_keyword
    
    ...
    
    
result = search_papers_by_keyword2(papers, 'AI')
print(result)