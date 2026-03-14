# Just notepad for testing and trying quick ideas 
from models import Paper
from collections import defaultdict
from logic import recent_papers


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
    Paper("Large Language Models", 2024, 800, ["A. Smith", "John Doe"]),
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

groups = group_papers_by_year(papers)

paper_in_year = {year:len(paper) for year, paper in groups.items()}

result = recent_papers(papers, 5)

print(result)


