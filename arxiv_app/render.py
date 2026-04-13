from arxiv_app.models import Paper
from arxiv_app.logic import summary_snippet
from arxiv_app.ranking import select_discovery_papers


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


def render_stats(total_papers: int, years: dict[int, int], unique_authors_count: int, most_common_author: str | None, top_n_authors: list[tuple[str, int]] | None) -> str:
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
        top_n_authors_string = ", ".join(f"{author} ({count})" for author, count in top_n_authors)
    lines = [total_papers_str, years_str, unique_authors_count_str, most_common_author_string, top_n_authors_string]
    return "\n".join(lines)


def render_discovery_view(papers: list[Paper]) -> str:
    # 2024
    # 1. Title A
    # Summary: ...
    # 2. Title B
    #Summary: ...
    
    # 2023
    # 3. Title C    
    #Summary: ...
    view = []
    index = 1
    papers_by_year = {}
    
    for paper in papers:
        if paper.year not in papers_by_year:
            papers_by_year[paper.year] = []
        papers_by_year[paper.year].append(paper)
    
        
    for year in sorted(papers_by_year, reverse=True):
        if view:
            view.append("")
        view.append(f"[{year}]")
        for paper in papers_by_year[year]:
            view.append(f"{index}. {BOLD}{paper.title}{RESET}")
            view.append(f"   {CYAN}Summary:{RESET} {summary_snippet(paper.summary, 150)}\n")
            index += 1
             
    return "\n".join(view)
 
 
 
def render_paper_detail(paper: Paper) -> str:
    lines = []
    lines.append(f"Title: {paper.title}")
    lines.append(f"Year: {paper.year}")
    authors_str = ", ".join(paper.authors)
    lines.append(f"Authors: {authors_str}")
    lines.append(f"Summary: {paper.summary}")
    return "\n".join(lines) 


def render_interest_digest(interest: str, papers: list[Paper]) -> str:
    lines = []
    lines.append(f"Interest: =={interest}==")
    lines.append("")
    lines.append(render_discovery_view(papers))
    return "\n".join(lines)


def digest_for_interest(interest: str, papers: list[Paper], limit: int = 5) -> str:
    selected_papers = select_discovery_papers(papers, interest, limit)
    return render_interest_digest(interest, selected_papers)
 
def digest_for_interests(interests: list[str], papers: list[Paper], limit: int = 5) -> str:
    sections = []
    for interest in interests:
        sections.append(digest_for_interest(interest, papers, limit)) 
    return "\n\n".join(sections)