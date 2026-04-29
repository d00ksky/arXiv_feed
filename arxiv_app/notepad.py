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



def safe_paper_field_by_id(papers: list[Paper], paper_id: str, field: str) -> str | int | list[str] | None:
    for paper in papers:
        if paper.id == paper_id:
            if field == 'title':
                return paper.title
            elif field == 'summary':
                return paper.summary
            elif field == 'year':
                return paper.year
            elif field == 'citations':
                return paper.citations
            elif field == 'authors':
                return paper.authors
            else:
                return None
    return None
        
    
result = safe_paper_field_by_id(papers, "paper-2", "citations")


print(result)
