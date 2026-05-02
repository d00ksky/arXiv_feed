from arxiv_app.ranking import (
    title_match_score,
    paper_match_score,
    select_discovery_papers
)

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