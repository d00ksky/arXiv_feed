from arxiv_app.logic import paper_at_index

from arxiv_app.render import (
    render_paper_detail,
    render_discovery_view,
)

from arxiv_app.models import (
    Paper,
    RankedPaper,
)
# Paper
# → RankedPaper
# → paper_at_index(..., 1)
# → selected_ranked_paper.paper
# → render_paper_detail(...)


def make_paper(
    title: str,
    summary: str,
    year: int = 2024,
    id: str = "http://arxiv.org/abs/2608.13495v1",
) -> Paper:
    return Paper(
        title=title,
        year=year,
        citations=0,
        authors=["Test Author"],
        summary=summary,
        id=id,
    )


def test_selected_ranked_paper_can_be_rendered_as_detail():

    paper = make_paper(
        title="Retrieval for Scientific Search",
        summary="A system for ranking arXiv papers.",
        year=2024,
    )

    ranked_paper = RankedPaper(
        paper=paper,
        score=6,
        reasons=["query appears in title"],
    )

    ranked_papers = [ranked_paper]

    selected_ranked_paper = paper_at_index(ranked_papers, 1)

    assert selected_ranked_paper is not None

    result = render_paper_detail(selected_ranked_paper.paper)

    assert paper.title in result
    assert str(paper.year) in result
    assert paper.summary in result
    assert paper.id in result


def test_render_discovery_view_reasons():

    paper = make_paper(
        title="Retrieval for Scientific Search",
        summary="A system for ranking arXiv papers.",
        year=2024,
        id="http://arxiv.org/abs/2608.13495v1",
    )

    ranked_paper = RankedPaper(
        paper=paper,
        score=6,
        reasons=["query appears in title"],
    )

    ranked_papers = [ranked_paper]
    result = render_discovery_view(ranked_papers)

    assert "query appears in title" in result
    assert paper.id in result
