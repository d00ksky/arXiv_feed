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
    ...


result = paper_years_with_long_summary(papers, 10)

print(result)

