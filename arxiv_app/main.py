import argparse
from arxiv_app.arxiv_client import fetch_papers
from arxiv_app.normalization import normalize_papers
from arxiv_app.logic import (
    filter_papers_after_year,
    filter_papers_by_author,
    most_cited_papers,
)
from arxiv_app.validation import non_negative_int
from arxiv_app.render import (
    render_stats,
    render_discovery_view,
)

from arxiv_app.stats import (
    unique_authors,
    count_papers_by_year,
    most_common_author,
    top_n_authors,
)

from arxiv_app.ranking import select_discovery_papers

from arxiv_app.digest import (
    generate_paper_digests,
)

from arxiv_app.llm_client import openai_generate_text

import os

from arxiv_app.email_client import send_email


def main():
    parser = argparse.ArgumentParser(description="arXiv CLI tool")

    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--year", type=int, help="Filter papers after year")
    parser.add_argument("--author", help="Filter papers by author substring")
    parser.add_argument("--limit", type=int, default=5, help="Limit number of results")
    parser.add_argument(
        "--cache-ttl",
        type=non_negative_int,
        default=600,
        help="Cache TTL in seconds (default 600, 0 disables cache)",
    )
    parser.add_argument("--sort", choices=["newest", "oldest"], help="Sort by year")
    parser.add_argument("--top-cited", type=int, help="Show top cited papers")
    parser.add_argument(
        "--stats", action="store_true", help="Show statistics about papers"
    )
    parser.add_argument("--send-email", action="store_true")
    parser.add_argument("--category", help="Choose category")

    args = parser.parse_args()

    # Fetch and normalize papers before applying filters and discovery selection.
    interest = args.query
    raw = fetch_papers(
        args.query, args.category, max_results=args.limit * 5, cache_ttl=args.cache_ttl
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
        most_common_author_name = most_common_author(papers)
        count_papers_year = count_papers_by_year(papers)
        total_papers = len(papers)
        top_authors = top_n_authors(papers, 3)
        stats_str = render_stats(
            total_papers,
            count_papers_year,
            uniq_authors,
            most_common_author_name,
            top_authors,
        )
        print(stats_str)

    if args.sort == "oldest":
        papers = sorted(papers, key=lambda paper: paper.year)
    elif args.sort == "newest":
        papers = sorted(papers, key=lambda paper: paper.year, reverse=True)

    ranked_discovery_papers = select_discovery_papers(papers, args.query, args.limit)
    # Here we are printing papers after all filters

    if not ranked_discovery_papers:
        print("No papers found.")
    else:
        ai_summaries = generate_paper_digests(
            ranked_discovery_papers, interest, openai_generate_text
        )
        if args.send_email:
            sender = os.environ.get("EMAIL_SENDER")
            recipient = os.environ.get("EMAIL_RECIPIENT")
            app_password = os.environ.get("EMAIL_APP_PASSWORD")

            if not sender or not recipient or not app_password:
                raise RuntimeError("Missing required email environment variables")

            body = render_discovery_view(
                ranked_discovery_papers, ai_summaries, use_color=False
            )

            html_body = f""""<article>
  <header>
    <h1>Here is you digest!</h1>
    <p>{body}</p>
  </header>
  <p>That's all folks!</p>
</article>"""

            subject = f"arxiv Digest {interest}"
            send_email(
                subject, body, sender, recipient, app_password, html_body=html_body
            )
        print(render_discovery_view(ranked_discovery_papers, ai_summaries))


if __name__ == "__main__":
    main()
