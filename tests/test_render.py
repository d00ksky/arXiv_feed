from arxiv_app.render import (
    render_discovery_view,
)

from arxiv_app.models import (
    Paper,
    RankedPaper,
)


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
    result = render_discovery_view(
        ranked_papers,
        ai_summaries=[
            "Paper two examines ranking signals used in scientific search.",
        ],
    )

    assert "query appears in title" in result
    assert paper.id in result


def test_render_discovery_view_can_disable_terminal_colors():
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
    result = render_discovery_view(
        ranked_papers,
        ai_summaries=[
            "Paper two examines ranking signals used in scientific search.",
        ],
        use_color=False,
    )

    assert "\033[" not in result
    assert paper.title in result
