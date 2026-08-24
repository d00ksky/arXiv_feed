from arxiv_app.models import RankedPaper
from collections.abc import Callable


def build_paper_digest_prompt(
    ranked_paper: RankedPaper,
    interest: str,
) -> str:

    title = ranked_paper.paper.title
    summary = ranked_paper.paper.summary
    prompt = "Give 2-3 sentences summarizing paper in the context of interest"

    full_prompt = (
        f"Title: {title} \nSummary: {summary} \nInterest: {interest} \nPrompt: {prompt}"
    )

    return full_prompt


def generate_paper_digest(
    ranked_paper: RankedPaper,
    interest: str,
    generate_text: Callable[[str], str],
) -> str:
    prompt = build_paper_digest_prompt(ranked_paper, interest)
    return generate_text(prompt)


def generate_paper_digests(
    ranked_papers: list[RankedPaper], interest: str, generate_text: Callable[[str], str]
) -> list[str]:
    return [
        generate_paper_digest(ranked_paper, interest, generate_text)
        for ranked_paper in ranked_papers
    ]
