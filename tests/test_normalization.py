from arxiv_app.normalization import (
    normalize_paper,
)

from arxiv_app.models import Paper


def test_normalize_paper_converts_raw_dict_to_paper():
    raw_paper = {
    "id": "http://arxiv.org/abs/1234.5678",
    "title": "Test Paper",
    "authors": ["Alice", "Bob"],
    "published": "2024-05-01T12:00:00Z",
    "summary": "This is a test summary.",
}
    result = normalize_paper(raw_paper)
    
    assert result.title == "Test Paper"
    assert result.year == 2024
    assert result.authors == ["Alice", "Bob"]
    assert result.id == "http://arxiv.org/abs/1234.5678"
    assert result.summary == "This is a test summary."
    assert result.citations == 0
    