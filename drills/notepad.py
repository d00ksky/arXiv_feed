papers = [
    {"title": "Attention Is All You Need", "year": 2017, "score": 9},
    {"title": "Retrieval-Augmented Generation", "year": 2020, "score": 8},
    {"title": "Old Neural Network Paper", "year": 1998, "score": 6},
    {"title": "Modern LLM Evaluation", "year": 2024, "score": 7},
]


def titles_after_year(papers: list[dict], year: int) -> list[str]:
    return [paper["title"] for paper in papers if paper["year"] > year]


# print(titles_after_year(papers, 2019))


def top_titles_by_score(papers: list[dict], limit: int) -> list[str]:
    return [
        paper["title"]
        for paper in sorted(papers, key=lambda paper: paper["score"], reverse=True)
    ][:limit]


print(top_titles_by_score(papers, 3))
