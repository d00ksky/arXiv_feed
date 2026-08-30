from arxiv_app.arxiv_client import _cache_path


def test_different_category_cache_path():
    query = "retrieval"
    category = "cs.IR"

    result_with_category = _cache_path(query, 10, category)
    result_without_category = _cache_path(query, 10)

    assert result_with_category != result_without_category
