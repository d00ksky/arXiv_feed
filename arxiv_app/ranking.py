from arxiv_app.models import Paper


def title_match_score(title: str, query: str) -> int:
    score = 0
    query_lower = query.lower()
    title_lower = title.lower()
    if query_lower in title_lower:
        score += 4
    for word in query_lower.split():
        if word and word in title_lower:
            score += 2
    return score


def paper_match_score(paper: Paper, query: str) -> int:
    score = title_match_score(paper.title, query)
    query_lower = query.lower()
    summary_lower = paper.summary.lower()
    if query_lower in summary_lower:
        score += 2
    for word in query_lower.split():
        if word and word in summary_lower:
            score += 1
    return score
    ...


def select_discovery_papers(papers: list[Paper], query: str, limit: int = 5) -> list[Paper]:
    """Returns sorted papers by score and if score is the same, by year"""
    #ranking currently uses title + summary score + recency
    #this is a heuristic V1 ranking
    return sorted(
        papers, key=lambda paper: (
            paper_match_score(paper, query), 
            paper.year), 
        reverse=True
    )[:limit]
    
