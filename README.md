# arXiv Feed

A tool for discovering and understanding new arXiv papers in a more personalized and interactive way.

The goal of this project is to build an intelligent feed for arXiv research papers, similar to a mix of Feedly and Reddit, but designed specifically for scientific papers and enhanced with an AI assistant.

Instead of manually browsing arXiv or RSS feeds, the application helps users discover the most relevant papers in their areas of interest and understand them faster.

---

# Project Vision

The long-term goal is to create a personalized research assistant that:

- monitors arXiv for topics the user cares about
- builds a personalized feed of new papers
- filters and ranks papers by relevance
- helps the user quickly understand and evaluate papers
- allows deeper exploration with AI assistance

Example workflow:

1. User defines topics or queries of interest.
2. The system fetches new papers from arXiv.
3. Papers are filtered and ranked for the user.
4. The user sees a personalized feed of relevant research.
5. The user can explore each paper with AI assistance.

---

# Key Features (Planned)

### Smart arXiv Feed

- fetch latest papers from arXiv
- filter by topic, author, or year
- ranking and recommendation of relevant papers
- personalized research feed

### AI Reading Assistant

For each paper the user can:

- generate a TL;DR summary
- get explanations at different difficulty levels
- translate complex passages
- compare papers
- extract key ideas and contributions

### Personalization

The system will adapt to the user by learning:

- preferred topics
- reading patterns
- level of expertise
- preferred types of papers

Over time this should improve the ranking and recommendations in the feed.

---

# Architecture Direction

The system is designed around a clear data pipeline:

arXiv API → normalization → Paper model → logic → rendering → CLI / UI

Key principles:

- normalize raw API data into a clean internal model (`Paper`)
- keep logic separate from rendering
- build composable functions for filtering, ranking, and analysis
- gradually extend the system with AI features

---

# AI Strategy

This project **does not aim to train a custom model initially**.

Instead it focuses on:

- using existing LLM APIs for summarization and explanation
- building strong retrieval and ranking logic
- improving personalization through user behavior

Custom models may be explored later for specific tasks such as:

- paper classification
- recommendation ranking
- difficulty prediction

---

# Current Stage

This project currently includes:

- arXiv API client
- normalization pipeline
- `Paper` data model
- filtering and ranking logic
- CLI interface

Future stages will add:

- AI summarization
- semantic search
- personalized ranking
- interactive exploration of papers
