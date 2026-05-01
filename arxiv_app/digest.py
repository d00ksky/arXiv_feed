from arxiv_app.arxiv_client import fetch_papers
from arxiv_app.models import Paper
from arxiv_app.normalization import normalize_papers
from arxiv_app.ranking import select_discovery_papers
from arxiv_app.render import render_interest_digest


def top_papers_for_interest(papers: list[Paper], interest: str, limit: int = 5) -> list[Paper]:
    return select_discovery_papers(papers, interest, limit) 


def digest_for_interest_query(interest: str, limit: int = 5, fetch_limit: int = 20) -> str:
    raw = fetch_papers(interest, max_results=fetch_limit)
    papers = normalize_papers(raw)
    selected = top_papers_for_interest(papers, interest, limit)
    return render_interest_digest(interest, selected)
