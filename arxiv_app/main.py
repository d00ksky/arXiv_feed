import argparse
from arxiv_client import fetch_papers
from normalization import normalize_papers
from logic import (
    filter_papers_after_year,
    filter_papers_by_author,
    extract_titles,
    limit_results
)
from validation import non_negative_int
from render import render_paper_line
# n

def main():
    parser = argparse.ArgumentParser(description="arXiv CLI tool")

    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--year", type=int, help="Filter papers after year")
    parser.add_argument("--author", help="Filter papers by author substring")
    parser.add_argument("--limit", type=int, default=5, help="Limit number of results")
    parser.add_argument("--cache-ttl", type=non_negative_int, default=600, help="Cache TTL in seconds (default 600, 0 disables cache)")

    args = parser.parse_args()

    raw = fetch_papers(args.query, max_results = args.limit * 5)
    papers = normalize_papers(raw)
    
    if args.year is not None:
        papers = filter_papers_after_year(papers, args.year)
        
    if args.author is not None:
        papers = filter_papers_by_author(papers, args.author)
        
    # titles = extract_titles(papers)
    # titles = limit_results(titles, args.limit)
    
    # for i, title in enumerate(titles, start=1):
    #     print(f"{i}. {title}")
    
    for i, paper in enumerate(papers, start=1):
        formatted = render_paper_line(i, paper)
        print(formatted)
    



if __name__ == "__main__":
    main()



