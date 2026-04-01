from arxiv_app.models import Paper


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


def select_discovery_papers(papers: list[Paper], query: str, limit: int = 5) -> list[Paper]:
    """Returns sorted papers by score and if score is the same, by year"""
    return sorted(
        papers, key=lambda paper: (
            title_match_score(paper.title, query), 
            paper.year), 
        reverse=True
    )[:limit]
    
