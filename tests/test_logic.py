from arxiv_app.logic import (
    parse_selection,
    paper_at_index,
    summary_snippet
)
from arxiv_app.models import Paper

def make_paper(title: str) -> Paper:
    return Paper(
        title=title,
        year=2024,
        citations=0,
        authors=["Test Author"],
        id=f"test-id-{title}",
        summary="Test summary",
    )



def test_parse_selection_returns_int_for_number():
    result = parse_selection("3")
    
    assert result == 3    

def test_parse_selection_returns_none_for_empty_string():
    result = parse_selection("")
    
    assert result is None

def test_parse_selection_returns_none_for_non_number():
    result = parse_selection("qwerty")
    
    assert result is None

def test_paper_at_index_returns_first_paper_for_index_one():
    papers = [
        make_paper("first"),
        make_paper("Second"),
    ]
    
    result = paper_at_index(papers, 1)
    
    assert result == papers[0]
    

def test_paper_at_index_returns_none_for_out_of_range_index():
    papers = [
        make_paper("first"),
        make_paper("Second"),
    ]
    
    result = paper_at_index(papers, 3)
    
    assert result is None

def test_paper_at_index_returns_none_for_zero():
    papers = [
        make_paper("first"),
        make_paper("Second"),
    ]
    
    result = paper_at_index(papers, 0)
    
    assert result is None

def test_summary_snippet_returns_original_text_when_short_enough():
    result = summary_snippet("short text", 30)
    
    assert result == "short text"

def test_summary_snippet_truncates_long_text():    
    result = summary_snippet("abcdef", 3)
    
    assert result == "abc..."