

def render_paper_line(index: int, paper: dict) -> str:
    title = str(paper["title"])
    authors = paper["authors"]
    year = str(paper["year"])
    authors_str = ", ".join(authors)
    result = f"{index}. ({year}) {title}"
    if authors:
        result = result + " - " + authors_str
            
    return result
