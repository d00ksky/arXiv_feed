# Just notepad for testing and trying quick ideas 
from arxiv_app.models import Paper
import collections
from collections import (
    defaultdict,
    Counter,
)
from arxiv_app.logic import recent_papers



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


groups = group_papers_by_year(papers)

paper_in_year = {year:len(paper) for year, paper in groups.items()}

result = most_common_author(papers)

print(result)


