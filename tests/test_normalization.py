from arxiv_app.normalization import (
    normalize_paper,
    normalize_papers,
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
    
    assert isinstance(result, Paper)
    assert result.title == "Test Paper"
    assert result.year == 2024
    assert result.authors == ["Alice", "Bob"]
    assert result.id == "http://arxiv.org/abs/1234.5678"
    assert result.summary == "This is a test summary."
    assert result.citations == 0
    

def test_normalize_papers_converts_raw_dicts_to_papers():
    raw_papers = [
    {
        "id": "http://arxiv.org/abs/1111.1111",
        "title": "First Test Paper",
        "authors": ["Alice"],
        "published": "2023-01-15T10:00:00Z",
        "summary": "First summary.",
    },
    {
        "id": "http://arxiv.org/abs/2222.2222",
        "title": "Second Test Paper",
        "authors": ["Bob", "Charlie"],
        "published": "2024-06-20T12:30:00Z",
        "summary": "Second summary.",
    },
    ]
    
    result = normalize_papers(raw_papers)
    
    assert len(result) == 2

    assert isinstance(result[0], Paper)
    assert isinstance(result[1], Paper)
    
    assert result[0].title == "First Test Paper"
    assert result[0].year == 2023
    assert result[0].authors == ["Alice"]
    assert result[0].id == "http://arxiv.org/abs/1111.1111"
    assert result[0].summary == "First summary."
    assert result[0].citations == 0
    
    assert result[1].title == "Second Test Paper"
    assert result[1].year == 2024
    assert result[1].authors == ["Bob", "Charlie"]
    assert result[1].id == "http://arxiv.org/abs/2222.2222"
    assert result[1].summary == "Second summary."
    assert result[1].citations == 0