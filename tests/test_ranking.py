from arxiv_app.ranking import (
    title_match_score,
    paper_match_score,
    select_discovery_papers
)

from arxiv_app.models import Paper

# - title_match_score daje punkty za pełne query
# - title_match_score daje punkty za pojedyncze słowa
# - paper_match_score bierze pod uwagę summary
# - select_discovery_papers sortuje po score


# pełne query w tytule = +4
# "large" w tytule = +2
# "language" w tytule = +2
# "models" w tytule = +2

# razem = 10

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
    # arrange: weak_paper, strong_paper

    # act: result = select_discovery_papers(...)

    # assert: result == [...]
    
    