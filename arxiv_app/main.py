from arxiv_client import fetch_papers
from normalization import normalize_papers
from logic import (
    get_limited_titles_after_year,
    format_authors,
    filter_papers_by_author
)

def main():
    # papers = [
    #     {
    #         "id": "http://arxiv.org/abs/2501.02842v1",
    #         "title": "Foundations of GenIR",
    #         "authors": ["Qingyao Ai", "Jingtao Zhan", "Yiqun Liu"],
    #         "year": 2025,
    #     },
    #     {
    #         "title": "The Annotated Transformer",
    #         "year": 2018,
    #         "authors": ["Rush"],
    #     },
    # ]

    # titles = get_limited_titles_after_year(papers, 2017, 5)
    # print(titles)

    # print(format_authors(papers[0]["authors"]))

    raw = fetch_papers("AI")
    papers = normalize_papers(raw)
    titles = get_limited_titles_after_year(papers, 2022, 5)
    authors = format_authors(papers[0]["authors"])
    filtered = filter_papers_by_author(papers, 'ai')
    
    print(f"len raw = {len(raw)}, len papers = {len(papers)}")
    print(titles)
    print(authors)
    print(f'filtered authors = {filtered}')


if __name__ == "__main__":
    main()



