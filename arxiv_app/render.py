

def render_paper_line(index: int, paper: dict) -> str:
    title = paper["title"]
    authors = paper["authors"]
    year = paper["year"]
    authors_str = ", ".join(authors)
    result = f"{index}. ({year}) {title}"
    if authors:
        result += " - " + authors_str
            
    return result
