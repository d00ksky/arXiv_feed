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
    Paper(
    "AI Safety for Large Language Models",
    2024,
    920,
    ["R. Turner", "L. Smith"],
    "paper-8",
    "This paper studies AI safety challenges in large language models, including robustness, misalignment, and unsafe model behavior."
),
Paper(
    "Reasoning Abilities in Language Models",
    2024,
    780,
    ["M. Chen", "A. Gupta"],
    "paper-9",
    "We analyze reasoning abilities in language models and evaluate how well modern models solve multi-step reasoning tasks."
),
Paper(
    "Agentic Coding with LLM Systems",
    2025,
    410,
    ["D. Park", "J. Miller"],
    "paper-10",
    "This paper explores agentic coding systems where language models autonomously write, revise, and debug code in iterative loops."
),
Paper(
    "Retrieval-Augmented Generation in Practice",
    2024,
    650,
    ["S. Rao", "E. Brown"],
    "paper-11",
    "We study retrieval-augmented generation systems and show how external knowledge retrieval improves factual accuracy and grounding."
),
Paper(
    "Alignment and Control in AI Agents",
    2025,
    530,
    ["K. Patel", "N. Evans"],
    "paper-12",
    "This work focuses on alignment and control problems in AI agents, with an emphasis on safety, monitoring, and reliable behavior."
),
Paper(
    "Tool Use and Planning in Reasoning Models",
    2025,
    470,
    ["Y. Nakamura", "P. Silva"],
    "paper-13",
    "We examine reasoning models that combine tool use, explicit planning, and structured intermediate steps for harder tasks."
),
Paper(
    "Secure Deployment of Agentic AI Systems",
    2024,
    355,
    ["T. Ivanov"],
    "paper-14",
    "This paper discusses the secure deployment of agentic AI systems, including oversight, safety constraints, and failure prevention."
),
Paper(
    "Evaluation of OpenAI-style Reasoning Systems",
    2025,
    290,
    ["C. Weber", "F. Rossi"],
    "paper-15",
    "We evaluate OpenAI-style reasoning systems on benchmarks requiring chain-of-thought, planning, and robust problem solving."
),
]

test_queries = [
    "ai safety",
    "reasoning models",
    "agentic coding",
]


sorted_years = sorted(papers_by_year.items(), key=lambda count: count[1], reverse=True)

only_years = [item[0] for item in sorted_years]

titles = [paper.title for paper in papers]

author = "John Doe"

interests = ["openai", "superpartia", "    ", "Roberto"]


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
        

def safe_snippet_by_id(papers: list[Paper], paper_id: str, limit: int) -> str | None:
    for paper in papers:
        if paper.id == paper_id:
            if len(paper.summary) <= limit:
                return paper.summary
            return paper.summary[:limit] + "..."
    return None
    
# for query in test_queries:
#     selected_papers = select_discovery_papers(papers, query, 5)
#     print(f'\nQUERY: {query}')
#     for paper in selected_papers:
#         print('-', paper.title)
        
papers = [
    {"title": "A", "year": 2024},
    {"title": "B", "year": 2024},
    {"title": "C", "year": 2023},
]

def group_titles_by_year(papers: list[dict]) -> dict[int, list[str]]:
    years_grouped = {}
    for paper in papers:
        #print(paper['year'])
        if paper['year'] not in years_grouped:
            years_grouped[paper['year']] = []
        years_grouped[paper["year"]].append(paper["title"])
    return years_grouped
            


result = group_titles_by_year(papers)


print(result)
