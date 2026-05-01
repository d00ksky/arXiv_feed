from arxiv_app.logic import parse_selection

def test_parse_selection_returns_int_for_number():
    result = parse_selection("3")
    assert result == 3    

def test_parse_selection_returns_none_for_empty_string():
    result = parse_selection("")
    assert result == None

def test_parse_selection_returns_none_for_non_number():
    ...

def test_paper_at_index_returns_correct_paper():
    ...

def test_paper_at_index_returns_none_for_out_of_range_index():
    ...

def test_summary_snippet_returns_original_text_when_short_enough():
    ...

def test_summary_snippet_truncates_long_text():
    ...