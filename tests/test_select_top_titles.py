import pytest

from drills.select_top_titles import select_top_titles


def test_selects_higher_scores_first():
    papers = [
        {"title": "Lower", "score": 5},
        {"title": "Higher", "score": 9},
    ]

    result = select_top_titles(
        papers,
        min_score=0,
        limit=2,
    )

    assert result == ["Higher", "Lower"]


def test_sorts_titles_alphabetically_when_scores_are_equal():
    papers = [
        {"title": "Zulu", "score": 8},
        {"title": "Alpha", "score": 8},
    ]

    result = select_top_titles(
        papers,
        min_score=0,
        limit=2,
    )

    assert result == ["Alpha", "Zulu"]


def test_filters_papers_below_minimum_score():
    papers = [
        {"title": "Keep me", "score": 7},
        {"title": "Remove me", "score": 3},
    ]

    result = select_top_titles(papers, min_score=4, limit=2)

    assert result == ["Keep me"]


def test_respects_limit():
    papers = [
        {"title": "Going on", "score": 9},
        {"title": "Keep me", "score": 7},
        {"title": "Remove me", "score": 3},
    ]

    result = select_top_titles(papers, min_score=0, limit=1)

    assert result == ["Going on"]


def test_raises_value_error_if_limit_is_negative():
    papers = [
        {"title": "Keep me", "score": 7},
        {"title": "Remove me", "score": 3},
    ]

    with pytest.raises(ValueError):
        select_top_titles(papers, min_score=0, limit=-1)
