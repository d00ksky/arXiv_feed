
# papers = [
#     {"title": "Attention Is All You Need", "year": 2017},
#     {"title": "Deep Residual Learning", "year": 2015},
#     {"title": "The Annotated Transformer", "year": 2018},
#     {"title": "A Survey on Transformers", "year": 2020},
# ]

# n

def filter_papers_after_year(papers, year):
    papers_after = []
    for paper in papers:
        if paper["year"] > year:
            papers_after.append(paper)
    return papers_after


def extract_titles(papers):
    titles = []
    for paper in papers:
        titles.append(paper["title"])
    return titles

def get_titles_after_year(papers, year):
    papers_after = filter_papers_after_year(papers, year)
    titles_after = extract_titles(papers_after)
    return titles_after
    

def limit_results(items, limit):
    limited_result = []
    for i in range(limit):
        if i < len(items):
            limited_result.append(items[i])
    return limited_result


def get_limited_titles_after_year(papers, year, limit):
    titles_after = get_titles_after_year(papers, year)
    limited = limit_results(titles_after, limit)
    return limited

authors = []
def format_authors(authors):
    formatted_authors = ""
    for i in range(len(authors)):
        if i > 0:
            formatted_authors = formatted_authors + ", "
        formatted_authors = formatted_authors + authors[i]
    return formatted_authors
  
def filter_papers_by_author(papers, author_query):
    filtered = []
    for paper in papers:
        for author in paper["authors"]:
            if author_query.lower() in author.lower():
                filtered.append(paper)
                break
                
    return filtered