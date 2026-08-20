from arxiv_app.models import (
    RankedPaper,
    Paper,
)

from arxiv_app.digest import (
    build_paper_digest_prompt,
    generate_paper_digest,
    generate_paper_digests,
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


def test_build_paper_digest_prompt_contains_paper_data():
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

    interest = "retrieval"

    full_prompt = build_paper_digest_prompt(ranked_paper, interest)

    assert paper.title in full_prompt
    assert paper.summary in full_prompt
    assert interest in full_prompt


def fake_generate_text(prompt: str) -> str:
    return "Test AI summary"


def test_generate_paper_digest_returns_generated_text():

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

    interest = "retrieval"

    result = generate_paper_digest(ranked_paper, interest, fake_generate_text)

    assert result == "Test AI summary"


def test_generate_paper_digests_generates_summary_for_each_paper():

    paper_1 = make_paper(
        title="Retrieval for Scientific Search",
        summary="A system for ranking arXiv papers.",
        year=2024,
        id="http://arxiv.org/abs/2608.13495v1",
    )

    ranked_paper_1 = RankedPaper(
        paper=paper_1,
        score=6,
        reasons=["query appears in title"],
    )

    paper_2 = make_paper(
        title="Scientific Search ranking",
        summary="A system for ranking arXiv retrieval papers.",
        year=2026,
        id="http://arxiv.org/abs/2608.13495v2",
    )

    ranked_paper_2 = RankedPaper(
        paper=paper_2,
        score=6,
        reasons=["query appears in summary"],
    )

    interest = "retrieval"

    received_prompts: list[str] = []

    def tracking_generate_text(prompt: str) -> str:
        received_prompts.append(prompt)
        return f"AI summary {len(received_prompts)}"

    result = generate_paper_digests(
        [ranked_paper_1, ranked_paper_2],
        interest,
        tracking_generate_text,
    )

    assert result == ["AI summary 1", "AI summary 2"]
    assert len(received_prompts) == 2
    assert paper_1.title in received_prompts[0]
    assert paper_2.title in received_prompts[1]
