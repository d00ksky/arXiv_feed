from arxiv_app.models import Paper

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
    # 2. Title B
    
    # 2023
    # 3. Title C    
    view = []
    index = 1
    papers_by_year = {}
    
    for paper in papers:
        if paper.year not in papers_by_year:
            papers_by_year[paper.year] = []
        papers_by_year[paper.year].append(paper.title)
    
        
    for year in sorted(papers_by_year, reverse=True):
        if view:
            view.append("")
        view.append(f"[{year}]")
        for title in papers_by_year[year]:
            view.append(f"{index}. {title}")
            index += 1
             
    return "\n".join(view)
 
def render_paper_detail(paper: Paper) -> str:
    line = []
    line.append(f"Title: {paper.title}")
    line.append(f"Year: {paper.year}")
    authors_str = ", ".join(paper.authors)
    line.append(f"Authors: {authors_str}")
    return "\n".join(line)
