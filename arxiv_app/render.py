from models import Paper

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


def render_stats(total_papers: int, years: dict[int, int], unique_authors_count: int) -> str:
    total_papers_str = f"Total papers: {total_papers}"
    years_str = f"Years covered: {min(years)}-{max(years)}"
    unique_authors_count_str = f"Unique authors: {unique_authors_count}"
    lines = [total_papers_str, years_str, unique_authors_count_str]
    return "\n".join(lines)
