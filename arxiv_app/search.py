from arxiv_app.models import Paper

def authors_with_keyword(papers: list[Paper], keyword: str) -> list[str]:
    title_with_keyword = [paper for paper in papers if keyword.lower() in paper.title.lower()]
    return sorted(set(author for paper in title_with_keyword for author in paper.authors))
