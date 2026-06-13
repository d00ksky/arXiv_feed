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


def count_by_year1(papers: list[dict]) -> dict[int, int]:
    paper_count = {}
    for paper in papers:
        if paper["year"] not in paper_count:
            paper_count[paper["year"]] = 0
        paper_count[paper["year"]] += 1
    return paper_count


papers = [
    {
        "title": "Paper A",
        "authors": ["Yann LeCun", "Geoffrey Hinton"],
    },
    {
        "title": "Paper B",
        "authors": ["Ilya Sutskever", "Alex Krizhevsky"],
    },
]


def has_author1(papers: list[dict], author_query: str) -> bool:
    author_query = author_query.lower()
    return any(
        any(author_query in author.lower() for author in paper["authors"])
        for paper in papers
    )


def normalize_keywords(text: str) -> list[str]:
    return [keyword.strip().lower() for keyword in text.split(",") if keyword.strip()]


# print(normalize_keywords("AI, Machine Learning,  RAG"))
# ["ai", "machine learning", "rag"]


# print(has_author(papers, "karpathy"))

papers = [
    {"title": "A", "year": 2024, "score": 9},
    {"title": "B", "year": 2024, "score": 7},
    {"title": "C", "year": 2020, "score": 8},
]


def count_by_year2(papers: list[dict]) -> dict[int, int]:
    paper_year_count = {}
    for paper in papers:
        year = paper["year"]
        if year not in paper_year_count:
            paper_year_count[year] = 0
        paper_year_count[year] += 1
    return paper_year_count


# print(count_by_year(papers))

# assert count_by_year(papers) == {2024: 2, 2020: 1}
# assert count_by_year([]) == {}

# print("All tests passed")


papers = [
    {
        "title": "Attention Is All You Need",
        "year": 2017,
        "authors": ["Ashish Vaswani", "Noam Shazeer"],
    },
    {
        "title": "Retrieval-Augmented Generation",
        "year": 2020,
        "authors": ["Patrick Lewis", "Ethan Perez"],
    },
    {
        "title": "Modern LLM Evaluation",
        "year": 2024,
        "authors": ["Anna Kowalska", "Jan Nowak"],
    },
]


def has_author(papers: list[dict], author_query: str) -> bool:
    author_query = author_query.lower()

    if not author_query.strip():
        return False

    return any(
        any(author_query in author.lower() for author in paper["authors"])
        for paper in papers
    )


# assert has_author(papers, "vaswani") is True
# assert has_author(papers, "Vaswani") is True
# assert has_author(papers, "patrick") is True
# assert has_author(papers, "kowalska") is True
# assert has_author(papers, "hinton") is False
# assert has_author([], "vaswani") is False
# assert has_author(papers, "") is False

# print("All tests passed")

# print(has_author(papers, "vaswani"))

papers = [
    {"title": "A", "year": 2024},
    {"title": "B", "year": 2024},
    {"title": "C", "year": 2020},
]


def group_titles_by_year(papers: list[dict]) -> dict[int, list[str]]:
    grouped_titles: dict[int, list[str]] = {}
    for paper in papers:
        year = paper["year"]
        title = paper["title"]
        if year not in grouped_titles:
            grouped_titles[year] = []
        grouped_titles[year].append(title)
    return grouped_titles


# assert group_titles_by_year(papers) == {
#     2024: ["A", "B"],
#     2020: ["C"],
# }

# assert group_titles_by_year([]) == {}

# print("All tests passed")

# print(group_titles_by_year(papers))


def count_by_year(papers: list[dict]) -> dict[int, int]:
    year_count: dict[int, int] = {}
    for paper in papers:
        year = paper["year"]
        if year not in year_count:
            year_count[year] = 0
        year_count[year] += 1
    return year_count


print(count_by_year(papers))
