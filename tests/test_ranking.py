from arxiv_app.ranking import (
    title_match_score,
    paper_match_score,
    select_discovery_papers,
    explain_paper_match,
)

from arxiv_app.models import Paper


def test_title_match_score_scoring_for_full_query():
    title = "Large Language Models for Search"
    query = "large language models"
    result = title_match_score(title, query)

    assert result == 10


def test_title_match_score_scores_individual_words_without_full_query():
    result = title_match_score(
        "Language Agents and Model Reasoning",
        "language model",
    )

    assert result == 4


def make_paper(title: str, summary: str, year: int = 2024) -> Paper:
    return Paper(
        title=title,
        year=year,
        citations=0,
        authors=["Test Author"],
        id=f"test-id-{title}",
        summary=summary,
    )


def test_paper_match_score_uses_summary():
    paper = make_paper(
        title="Unrelated title",
        summary="This paper is about large language models.",
    )

    result = paper_match_score(paper, "large language models")

    assert result == 5


def test_select_discovery_papers_sorts_by_score():

    weak_paper = make_paper(
        title="Unrelated title",
        summary="This mentions language once.",
    )

    strong_paper = make_paper(
        title="Large language models for search",
        summary="This paper is about large, even more large language models.",
    )

    papers = [weak_paper, strong_paper]

    result = select_discovery_papers(
        papers,
        query="large language model",
        limit=2,
    )

    assert result == [strong_paper, weak_paper]


def test_select_discovery_papers_by_year_if_score_is_the_same():

    old_paper = make_paper(
        title="Completely unrelated",
        summary="Nothing useful here",
        year=2020,
    )

    new_paper = make_paper(
        title="Also unrelated",
        summary="Still nothing useful",
        year=2024,
    )

    query = "large language models"
    limit = 2

    papers = [old_paper, new_paper]

    result = select_discovery_papers(papers, query, limit)

    assert result == [new_paper, old_paper]


def test_explain_paper_match_returns_reasons_for_title_match():
    paper = make_paper(
        title="Large Language Models for Search",
        summary="This paper explains retrieval systems.",
    )

    result = explain_paper_match(paper, "large language models")

    assert "query appears in title" in result
    assert "title contains word: large" in result
    assert "title contains word: language" in result
    assert "title contains word: models" in result


paper = make_paper(
    title="Large Language Models for Search",
    summary="This paper explains retrieval systems.",
)

assert explain_paper_match(paper, "") == []
assert explain_paper_match(paper, "   ") == []
