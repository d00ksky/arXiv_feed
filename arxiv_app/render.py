from arxiv_app.models import (
    Paper,
    RankedPaper,
)
from arxiv_app.ranking import select_discovery_papers
import html


RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"


def render_paper_line(index: int, paper: Paper) -> str:
    title = paper.title
    authors = paper.authors
    year = paper.year
    authors_str = ", ".join(authors)
    result = f"{index}. ({year}) {title}"
    if authors:
        result += " - " + authors_str

    return result


def render_paper_list(papers: list[Paper]) -> str:
    lines = []
    for index, paper in enumerate(papers, start=1):
        lines.append(render_paper_line(index, paper))
    return "\n".join(lines)


def render_stats(
    total_papers: int,
    years: dict[int, int],
    unique_authors_count: int,
    most_common_author: str | None,
    top_n_authors: list[tuple[str, int]] | None,
) -> str:
    total_papers_str = f"Total papers: {total_papers}"
    if not years:
        years_str = "Years covered: N/A"
    else:
        years_str = f"Years covered: {min(years)}-{max(years)}"
    unique_authors_count_str = f"Unique authors: {unique_authors_count}"
    if most_common_author is None:
        most_common_author_string = "Most common author: N/A"
    else:
        most_common_author_string = f"Most common author: {most_common_author}"
    if top_n_authors is None:
        top_n_authors_string = "Top authors: N/A"
    else:
        top_n_authors_string = ", ".join(
            f"{author} ({count})" for author, count in top_n_authors
        )
    lines = [
        total_papers_str,
        years_str,
        unique_authors_count_str,
        most_common_author_string,
        top_n_authors_string,
    ]
    return "\n".join(lines)


def render_discovery_view(
    papers: list[RankedPaper], ai_summaries: list[str], use_color: bool = True
) -> str:
    view = []
    index = 1

    bold = BOLD if use_color else ""
    cyan = CYAN if use_color else ""
    reset = RESET if use_color else ""

    for ranked_paper in papers:
        paper = ranked_paper.paper
        view.append(f"{index}. ({paper.year}) {bold}{paper.title}{reset}")
        view.append(f"   {cyan}AI Summary:{reset} {ai_summaries[index - 1]}")
        view.append(f"   {cyan}Why selected:{reset} {', '.join(ranked_paper.reasons)}")
        view.append(f"   {cyan}URL: {reset}{paper.id}")
        index += 1

    return "\n".join(view)


def render_interest_digest(
    interest: str, papers: list[RankedPaper], ai_summaries: list[str]
) -> str:
    lines = []
    lines.append(f"Interest: =={interest}==")
    lines.append("")
    lines.append(render_discovery_view(papers, ai_summaries))
    return "\n".join(lines)


def digest_for_interest(
    interest: str, papers: list[Paper], ai_summaries: list[str], limit: int = 5
) -> str:
    selected_papers = select_discovery_papers(papers, interest, limit)
    return render_interest_digest(interest, selected_papers, ai_summaries)


def digest_for_interests(
    interests: list[str], papers: list[Paper], ai_summaries: list[str], limit: int = 5
) -> str:
    sections = []
    for interest in interests:
        sections.append(digest_for_interest(interest, papers, ai_summaries, limit))
    return "\n\n".join(sections)


def render_discovery_html(
    ranked_papers: list[RankedPaper], ai_summaries: list[str]
) -> str:
    view = []
    index = 1
    for ranked_paper in ranked_papers:
        paper = ranked_paper.paper
        view.append(
            f"<header><h1>{index}. ({paper.year}) {html.escape(paper.title)}</h1></header>"
        )
        view.append(f"<p>   AI Summary: {html.escape(ai_summaries[index - 1])}</p>")
        view.append(f"<p>   Why selected: {', '.join(ranked_paper.reasons)}</p>")
        safe_url = html.escape(paper.id, quote=True)
        view.append(f'<p>   URL: <a href="{safe_url}">Go to paper</a></p>')
        index += 1

    body = "\n".join(view)
    return f"<article>{body}</article>"
