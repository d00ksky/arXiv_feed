from arxiv_app.render import (
    render_discovery_view,
    render_discovery_html,
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


def test_render_discovery_html():

    paper = make_paper(
        title="Retrieval < Scientific Search",
        summary="A system for ranking arXiv papers.",
        year=2024,
        id="http://arxiv.org/abs/2608.13495v1",
    )

    ranked_paper = RankedPaper(
        paper=paper,
        score=6,
        reasons=["query appears < in title"],
    )

    ranked_papers = [ranked_paper]
    ai_summary = "Paper two examines ranking signals used in scientific search."
    result = render_discovery_html(
        ranked_papers,
        ai_summaries=[
            ai_summary,
        ],
    )

    assert ai_summary in result
    assert 'href="http://arxiv.org/abs/2608.13495v1' in result
    assert "Retrieval &lt; Scientific Search" in result
    expected_link = f'<a href="{paper.id}">Go to paper</a>'
    assert expected_link in result
    assert "query appears &lt; in title" in result
