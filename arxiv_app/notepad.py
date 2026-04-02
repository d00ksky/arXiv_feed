# Just notepad for testing and trying quick ideas 
from arxiv_app.models import Paper
import collections
from collections import (
    defaultdict,
    Counter,
)
from arxiv_app.logic import recent_papers
import os


papers_by_year = {
    2019: 1,
    2020: 3,
    2021: 4,
    2022: 2
}

papers = [
    Paper("Deep Learning for Vision", 2021, 12000, ["Y. LeCun", "A. Smith"]),
    Paper("Neural Networks in Medicine", 2023, 450, ["A. Smith", "K. Patel"]),
    Paper("Transformers in NLP", 2020, 25000, ["A. Vaswani", "Y. LeCun"]),
    Paper("Quantum Computing Basics", 2019, 300, ["John Doe"]),
    Paper("Large Language arxiv_app.arxiv_app.models", 2024, 800, ["A. Smith", "John Doe"]),
    Paper("AI in Healthcare", 2022, 600, ["K. Patel", "A. Smith"]),
    Paper("Self-Supervised Learning", 2021, 1500, ["A. Smith"]),
]


sorted_years = sorted(papers_by_year.items(), key=lambda count: count[1], reverse=True)

only_years = [item[0] for item in sorted_years]

def group_papers_by_year(papers: list[Paper]) -> dict[int, list[Paper]]:
    groups = defaultdict(list)
    for paper in papers:
        groups[paper.year].append(paper)
    return groups


def authors_with_keyword(papers: list[Paper], keyword: str) -> list[str]:
    title_with_keyword = [paper for paper in papers if keyword.lower() in paper.title.lower()]
    return sorted(set(author for paper in title_with_keyword for author in paper.authors))


# def most_common_author(papers: list[Paper]) -> str|None:
#     authors_count = {}
#     for paper in papers:
#         for author in paper.authors:
#             authors_count[author] = authors_count.get(author, 0) + 1
            
#     if not authors_count:
#         return None
    
#     return max(authors_count, key=lambda author: authors_count[author])
            

def most_common_author(papers: list[Paper]) -> str | None:
    '''Returns most common author using collections like counter and most_common'''
    authors_count = Counter(
        author for paper in papers for author in paper.authors
        )
            
    if not authors_count:
        return None
    
    return authors_count.most_common(1)[0][0]

def newest_titles(papers: list[Paper], limit: int) -> list[str]:
    '''just for training and fun!'''
    return [paper.title for paper in sorted(papers, key=lambda paper: paper.year, reverse=True)][:limit]



def papers_with_author_keyword(papers: list[Paper], keyword: str) -> list[Paper]:
    return [paper for paper in papers if any(keyword.lower() in author.lower() for author in paper.authors)]



def count_papers_per_author(papers: list[Paper]) -> dict[str, int]:
    # counter = {}
    # for paper in papers:
    #     for author in paper.authors:
    #         if author not in counter:
    #             counter[author] = 0
    #         counter[author] += 1
    # return counter
    return Counter(author for paper in papers for author in paper.authors)
    


def top_n_authors(papers: list[Paper], n: int) -> list[tuple[str, int]]:
    return Counter(author for paper in papers for author in paper.authors).most_common(n)


def has_multiple_authors(papers: list[Paper]) -> list[Paper]:
    return [paper for paper in papers if len(paper.authors) > 1]


def papers_with_all_authors_matching(papers: list[Paper], keyword: str) -> list[Paper]:
    return [paper for paper in papers if all(keyword.lower() in author.lower() for author in paper.authors )]

def papers_from_last_n_years(papers: list[Paper], years: int) -> list[Paper]:
    if not papers:
        return []
    
    else:
        max_year = max(paper.year for paper in papers)
        threshold = max_year - years + 1
        
        return [paper for paper in papers if paper.year >= threshold]
    
    
def papers_with_single_author(papers: list[Paper]) -> list[Paper]:
    return  [paper for paper in papers if len(paper.authors) == 1]





def render_discovery_view(papers: list[Paper]) -> str:
    # 2024
    # 1. Title A
    # 2. Title B
    
    # 2023
    # 3. Title C    
    view = []
    index = 1
    papers_by_year = {}
    
    for paper in papers:
        if paper.year not in papers_by_year:
            papers_by_year[paper.year] = []
        papers_by_year[paper.year].append(paper.title)
    
        
    for year in sorted(papers_by_year, reverse=True):
        if view:
            view.append("")
        view.append(f"[{year}]")
        for title in papers_by_year[year]:
            view.append(f"{index}. {title}")
            index += 1
             
    return "\n".join(view)



def titles_from_year(papers: list[Paper], year: int) -> list[str]:
    return [paper.title for paper in papers if paper.year == year]
    

def count_titles_from_year(papers: list[Paper], year: int) -> int:
    return sum(1 for paper in papers if paper.year == year)


def has_cache(path: str) -> bool:
    return os.path.exists(path)

def extract_years(papers: list[Paper]) -> list[int]:
    return [paper.year for paper in papers]
    

def unique_years_desc(papers: list[Paper]) -> list[int]:
    return sorted({paper.year for paper in papers}, reverse=True)


def title_match_score(title: str, query: str) -> int:
    score = 0
    query_lower = query.lower()
    title_lower = title.lower()
    if query_lower in title_lower:
        score += 3
    for word in query_lower.split():
        if word and word in title_lower:
            score += 1
    return score


def author_line(authors: list[str]) -> str:
    if not authors:
        return "N/A"
    return f"Authors: {", ".join(authors)}"



groups = group_papers_by_year(papers)

paper_in_year = {year:len(paper) for year, paper in groups.items()}

authors = ["Y. LeCun", "A. Smith"]

result = author_line(authors)

print(result)


