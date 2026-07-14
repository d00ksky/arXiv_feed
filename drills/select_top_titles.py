def select_top_titles(
    papers: list[dict],
    min_score: int,
    limit: int,
) -> list[str]:

    if limit < 0:
        raise ValueError("limit cannot be negative")

    papers_titles_above_min_score = [
        paper for paper in papers if paper["score"] >= min_score
    ]

    sorted_papers_by_score = sorted(
        papers_titles_above_min_score,
        key=lambda paper: (-paper["score"], paper["title"]),
    )

    return [paper["title"] for paper in sorted_papers_by_score][:limit]
