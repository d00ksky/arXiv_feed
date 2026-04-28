# Just notepad for testing and trying quick ideas 
from arxiv_app.models import Paper
import collections
from collections import (
    defaultdict,
    Counter,
)
from arxiv_app.logic import recent_papers
import os
from arxiv_app.interests import (
    DEFAULT_INTERESTS,
)
from arxiv_app.render import render_discovery_view
from arxiv_app.ranking import select_discovery_papers


papers_by_year = {
    2019: 1,
    2020: 3,
    2021: 4,
    2022: 2
}

papers = [
    Paper(
        "Deep Learning for Vision",
        2021,
        12000,
        ["Y. LeCun", "A. Smith"],
        "paper-1",
        "A paper about deep learning methods used in computer vision tasks."
    ),
    Paper(
        "Neural Networks in Medicine",
        2023,
        450,
        ["A. Smith", "K. Patel"],
        "paper-2",
        "A study of neural network applications in medical diagnosis and treatment support."
    ),
    Paper(
        "Transformers in NLP",
        2020,
        25000,
        ["A. Vaswani", "Y. LeCun"],
        "paper-3",
        "An overview of transformer-based methods for natural language processing."
    ),
    Paper(
        "Quantum Computing Basics",
        2019,
        300,
        ["John Doe"],
        "paper-4",
        "A beginner-friendly introduction to the main concepts of quantum computing."
    ),
    Paper(
        "Large Language Models",
        2024,
        800,
        ["A. Smith", "John Doe"],
        "paper-5",
        "A paper discussing the capabilities and limitations of large language models."
    ),
    Paper(
        "AI in Healthcare",
        2022,
        600,
        ["K. Patel", "A. Smith"],
        "paper-6",
        "An analysis of how artificial intelligence can improve healthcare systems."
    ),
    Paper(
        "Self-Supervised Learning",
        2021,
        1500,
        ["A. Smith"],
        "paper-7",
        "A paper about self-supervised learning techniques for representation learning."
    ),
]


sorted_years = sorted(papers_by_year.items(), key=lambda count: count[1], reverse=True)

only_years = [item[0] for item in sorted_years]

titles = [paper.title for paper in papers]

author = "John Doe"

interests = ["openai", "superpartia", "    ", "Roberto"]

def non_empty_interests(interests: list[str]) -> list[str]:
    non_empty = []
    for interest in interests:
        if interest.strip() != "":
            non_empty.append(interest)
    return non_empty



def summaries_longer_than(papers: list[Paper], length: int) -> list[str]:
    return [paper.summary for paper in papers if len(paper.summary) > length]
    

def paper_count_with_keyword_in_summary(papers: list[Paper], keyword: str) -> int:
    return len([paper for paper in papers if keyword.lower() in paper.summary.lower()])
    

def titles_for_papers_with_long_summary(papers: list[Paper], min_length: int) -> list[str]:
    return [paper.title for paper in papers if len(paper.summary) >= min_length]


def ids_for_papers_with_long_summary(papers: list[Paper], min_length: int) -> list[str]:
    return [paper.id for paper in papers if len(paper.summary) >= min_length]

    
def paper_years_with_long_summary(papers: list[Paper], min_length: int) -> list[int]:
    return [paper.year for paper in papers if len(paper.summary) >= min_length]


def summaries_with_keyword(papers: list[Paper], keyword: str) -> list[str]:
    return [paper.summary for paper in papers if keyword.lower() in paper.summary.lower()]

def paper_titles_with_keyword_in_title(papers: list[Paper], keyword: str) -> list[str]:
    return [paper.title for paper in papers if keyword.lower() in paper.title.lower()]

def safe_first_paper(papers: list[Paper]) -> Paper | None:
    if not papers:
        return None
    return papers[0]


def safe_last_paper(papers: list[Paper]) -> Paper | None:
    if not papers:
        return None
    return papers[-1]

def papers_by_author_count(papers: list[Paper]) -> dict[int, list[Paper]]:
    groups = {}
    for paper in papers:
        author_count = len(paper.authors)
        if author_count not in groups:
            groups[author_count] = []
        groups[author_count].append(paper)
    return groups


def titles_by_author_count(papers: list[Paper]) -> dict[int, list[str]]:
    groups = {}
    for paper in papers:
        authors_count = len(paper.authors)
        if authors_count not in groups:
            groups[authors_count] = []
        groups[authors_count].append(paper.title)
    return groups


def ids_by_author_count(papers: list[Paper]) -> dict[int, list[str]]:
    groups = {}
    for paper in papers:
        authors_count = len(paper.authors)
        if authors_count not in groups:
            groups[authors_count] = []
        groups[authors_count].append(paper.id)
    return groups
            

def summaries_by_author_count(papers: list[Paper]) -> dict[int, list[str]]:
    groups = {}
    for paper in papers:
        author_count = len(paper.authors)
        if author_count not in groups:
            groups[author_count] = []
        groups[author_count].append(paper.summary)
    return groups


def counts_by_author_count(papers: list[Paper]) -> dict[int, int]:
    count = {}
    for paper in papers:
        author_count = len(paper.authors)
        if author_count not in count:
            count[author_count] = 0
        count[author_count] += 1
    return count


def counts_by_year(papers: list[Paper]) -> dict[int, int]:
    groups = {}
    for paper in papers:
        groups[paper.year] = groups.get(paper.year, 0) + 1
    return groups


def papers_with_summary_keyword_count_at_least(
    papers: list[Paper],
    keyword: str,
    min_count: int,
) -> list[Paper]:
    papers_with_keyword = []
    for paper in papers:
        summary_lower = paper.summary.lower()
        keyword_lower = keyword.lower()
        if summary_lower.count(keyword_lower) >= min_count:
            papers_with_keyword.append(paper)
    return papers_with_keyword
        

def paper_titles_with_summary_count_at_least(
    papers: list[Paper],
    keyword: str,
    min_count: int,
) -> list[str]:
    return [paper.title for paper in papers if paper.summary.lower().count(keyword.lower()) >= min_count]


def paper_ids_with_summary_count_at_least(
    papers: list[Paper],
    keyword: str,
    min_count: int,
) -> list[str]:
    return [paper.id for paper in papers if paper.summary.lower().count(keyword.lower()) >= min_count]
    
    
def paper_years_with_summary_count_at_least(
    papers: list[Paper],
    keyword: str,
    min_count: int,
) -> list[int]:
    
    return [paper.year for paper in papers if paper.summary.lower().count(keyword.lower()) >= min_count]


def paper_summaries_with_keyword_in_title(papers: list[Paper], keyword: str) -> list[str]:
    return [paper.summary for paper in papers if keyword.lower() in paper.title.lower()]
    

def paper_ids_with_keyword_in_title_and_summary(papers: list[Paper], keyword: str) -> list[str]:
    return [paper.id for paper in papers if keyword.lower() in paper.title.lower() or keyword.lower() in paper.summary.lower()]

def paper_titles_with_keyword_in_title_and_summary(papers: list[Paper], keyword: str) -> list[str]:
    keyword_lower = keyword.lower()
    return [paper.title for paper in papers if keyword_lower in paper.title.lower() or keyword_lower in paper.summary.lower()]

def paper_count_with_keyword_in_title_and_summary(papers: list[Paper], keyword: str) -> int:
    keyword_lower = keyword.lower()
    return len([paper for paper in papers if keyword_lower in paper.title.lower() or keyword_lower in paper.summary.lower()])
    
def papers_with_keyword_in_title_and_summary(papers: list[Paper], keyword: str) -> list[Paper]:
    keyword_lower = keyword.lower()
    return [paper for paper in papers if keyword_lower in paper.title.lower() or keyword_lower in paper.summary.lower()]
    
def safe_paper_by_index(papers: list[Paper], index: int) -> Paper | None:
    if index >= len(papers) or index < 0:
        return None
    return papers[index]

def safe_summary_snippet_by_index(
    papers: list[Paper],
    index: int,
    limit: int,
) -> str | None:
    if index < 0 or index >= len(papers):
        return None

    summary = papers[index].summary
    
    if len(summary) <= limit:
        return summary
    
    return summary[:limit] + "..."

def safe_title_by_id(papers: list[Paper], paper_id: str) -> str | None:
    for paper in papers:
        if paper.id == paper_id:
            return paper.title
    return None
            
def safe_summary_by_id(papers: list[Paper], paper_id: str) -> str | None:
    for paper in papers:
        if paper.id == paper_id:
            return paper.summary
    return None
    

def safe_year_by_id(papers: list[Paper], paper_id: str) -> int | None:
    for paper in papers:
        if paper.id == paper_id:
            return paper.year
    return None
    
def safe_authors_by_id(papers: list[Paper], paper_id: str) -> list[str] | None:
    for paper in papers:
        if paper.id == paper_id:
            return paper.authors
    return None


def safe_summary_by_year(papers: list[Paper], year: int) -> str | None:
    for paper in papers:
        if paper.year == year:
            return paper.summary
    return None

def safe_titles_by_year(papers: list[Paper], year: int) -> list:
    safed_titles = []    
    for paper in papers:
        if paper.year == year:
            safed_titles.append(paper.title)
    return safed_titles

def safe_titles_by_ids(papers: list[Paper], paper_id: str) -> list:
    saved_titles = []
    for paper in papers:
        if paper.id == paper_id:
            saved_titles.append(paper.title)
    return saved_titles
        

result = safe_titles_by_ids(papers, "paper-2")


print(result)
