from arxiv_client import fetch_papers
from logic import (
    get_limited_titles_after_year,
    format_authors,
)

def main():
    papers = [
        {
            "id": "http://arxiv.org/abs/2501.02842v1",
            "title": "Foundations of GenIR",
            "authors": ["Qingyao Ai", "Jingtao Zhan", "Yiqun Liu"],
            "year": 2025,
        },
        {
            "title": "The Annotated Transformer",
            "year": 2018,
            "authors": ["Rush"],
        },
    ]

    titles = get_limited_titles_after_year(papers, 2017, 5)
    print(titles)

    print(format_authors(papers[0]["authors"]))


if __name__ == "__main__":
    main()


