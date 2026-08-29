# for testing fetch_papers
from arxiv_app.arxiv_client import (
    _build_query_url,
)


def test_build_query_url():
    query = "large language models"
    max_results = 5

    url = _build_query_url(query, max_results)

    assert "max_results=5" in url
    assert "sortBy=submittedDate" in url
    assert "sortOrder=descending" in url
    assert "search_query=all:large+language+models" in url


def test_build_query_url_can_filter_by_category():
    url = _build_query_url("retrieval", 25, category="cs.IR")

    assert "all:retrieval" in url
    assert "AND" in url
    assert "cat:cs.IR" in url
