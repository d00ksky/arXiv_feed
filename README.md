# arXiv Digest

A personal Python CLI that selects relevant arXiv papers, generates short AI summaries, and can deliver a digest by email.

The V1 goal is a small, useful digest delivered regularly for configured interests. Each item includes its title, source link, AI summary, and ranking reasons. [docs/v1.md](docs/v1.md) defines the scope and delivery stages.

## Current functionality

- Fetch recent arXiv results with a local cache.
- Normalize records into `Paper` objects and apply CLI filters.
- Rank matches deterministically using title and abstract text, with year as a tie-breaker.
- Return `RankedPaper` objects containing the original paper, score, and reasons.
- Generate AI summaries for selected papers using the OpenAI API.
- Render terminal output and plain-text/HTML email.

The CLI already connects these components. Reproducible dependency installation and AWS deployment are the next work; scheduled delivery and the remaining V1 requirements are still pending.

## Run in an existing environment

Run commands from the repository root, in the environment where the application dependencies are installed. The repository does not yet include a dependency manifest.

The application uses the `openai` package. Configure `OPENAI_API_KEY` in the environment. For email delivery, also configure `EMAIL_SENDER`, `EMAIL_RECIPIENT`, and `EMAIL_APP_PASSWORD`. The current email implementation uses Gmail SMTP with an app password.

```bash
python -m arxiv_app.main --help
python -m arxiv_app.main --query "large language models" --limit 3
python -m arxiv_app.main --query "large language models" --limit 3 --send-email
```

Digest generation calls the OpenAI API for selected papers, including when email delivery is disabled. The cache is stored in a local `cache/` directory. Provide credentials through the environment rather than committing their values.

## Run existing tests

In an environment with the test dependencies installed:

```bash
python -m pytest -q
```

## Next milestones

1. Reproduce a complete local digest run from a fresh environment.
2. Run the existing flow manually on AWS.
3. Add scheduled delivery and assess the usefulness of the received digests.
4. Complete the remaining V1 requirements in [docs/v1.md](docs/v1.md).

The local report fallback is deferred to the later V1 stage. It is not a prerequisite for the first private deployment. Initial private deployment is an intermediate milestone, not a declaration that all V1 requirements are finished.

## Development and learning

Work is organized around useful outcomes with room for independent implementation. Reviews and tests are proportionate to the change. See [AGENTS.md](AGENTS.md) for collaboration rules and [AI_HANDOFF.md](AI_HANDOFF.md) for the current state and next goal.

[ChatGPT project instructions](docs/chatgpt-project-instructions.md) contain the complete text to paste into the project's instruction field. They complement the repository rules; changing the file does not change ChatGPT settings.

## Longer-term ideas

Interactive exploration, semantic search, and deeper personalization remain possible future directions. They are outside the current V1 scope.
