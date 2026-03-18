import argparse
from arxiv_client import fetch_papers
from normalization import normalize_papers
from logic import (
    filter_papers_after_year,
    filter_papers_by_author,
    most_cited_papers,
    unique_authors,
    count_papers_by_year,
)
from validation import non_negative_int
from render import (
    render_paper_line,
    render_stats,
    render_paper_list,
)
from models import Paper
# n

def main():
    parser = argparse.ArgumentParser(description="arXiv CLI tool")

    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--year", type=int, help="Filter papers after year")
    parser.add_argument("--author", help="Filter papers by author substring")
    parser.add_argument("--limit", type=int, default=5, help="Limit number of results")
    parser.add_argument("--cache-ttl", type=non_negative_int, default=600, help="Cache TTL in seconds (default 600, 0 disables cache)")
    parser.add_argument("--sort", choices=["newest", "oldest"], help="Sort by year")
    parser.add_argument("--top-cited", type=int, help="Show top cited papers")
    parser.add_argument("--stats", action="store_true", help="Show statistics about papers")


    args = parser.parse_args()


    raw = fetch_papers(
        args.query, 
        max_results = args.limit * 5,
        cache_ttl=args.cache_ttl,
        )
    papers = normalize_papers(raw)
    
    if args.year is not None:
        papers = filter_papers_after_year(papers, args.year)
        
    if args.author is not None:
        papers = filter_papers_by_author(papers, args.author)
    
    if args.top_cited is not None:
        papers = most_cited_papers(papers, args.top_cited)
        
    if args.stats:
        uniq_authors = len(unique_authors(papers))
        count_papers_year = count_papers_by_year(papers)
        total_papers = len(papers)
        stats_str = render_stats(total_papers, count_papers_year, uniq_authors)
        print(stats_str)
    
    if args.sort == "oldest":
        papers = sorted(papers, key=lambda paper: paper.year)
    elif args.sort == "newest":
        papers = sorted(papers, key=lambda paper: paper.year, reverse=True)
        
    
    # titles = extract_titles(papers)
    # titles = limit_results(titles, args.limit)
    
    # for i, title in enumerate(titles, start=1):
    #     print(f"{i}. {title}")
    
    for i, paper in enumerate(papers, start=1):
        formatted = render_paper_line(i, paper)
        print(formatted)
    



if __name__ == "__main__":
    main()



