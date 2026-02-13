from arxiv_client import fetch_papers
from normalization import normalize_papers
from logic import (
    get_limited_titles_after_year,
    format_authors,
    filter_papers_by_author,
    extract_titles,
    limit_results
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

    raw = fetch_papers("AI", max_results = 15)
    papers = normalize_papers(raw)
    filtered = filter_papers_by_author(papers, 'ai')
    titles = extract_titles(filtered)
    limited = limit_results(titles, 5)
    
    print(limited)



if __name__ == "__main__":
    main()



