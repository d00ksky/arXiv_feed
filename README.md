A personalized research feed and AI assistant for discovering and understanding arXiv papers.

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

1. User selects a topic or provides an area of interest.
2. The system fetches recent papers from arXiv.
3. The system filters, ranks, and selects a small useful set instead of showing everything.
4. The user sees a compact discovery view of relevant papers or themes.
5. The user chooses a topic or paper to inspect more deeply.
6. The system shows more detailed information and, later, AI assistance.

---

# Current Product Framing

The current CLI is a prototype interface for validating the product logic, not the final product itself.

This project is not meant to become a collection of random CLI filters, paper statistics, or developer-only helper commands. The real product direction is a discovery-first arXiv assistant that helps the user quickly notice what is worth paying attention to, then go deeper only where needed.

The default experience should favor:

- a compact discovery view instead of a raw dump of all matching papers
- a small selected set of relevant papers or topics instead of maximum volume
- low-noise presentation in the first view, with more detail shown only on demand

This means the initial view may intentionally hide less important metadata, such as authors, until the user chooses to inspect a topic or paper more deeply.

---

# Key Features (Planned)

### Smart arXiv Feed

- fetch latest papers from arXiv
- surface the most relevant recent papers for a topic or interest area
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

# Product Discipline

New CLI options, filters, and helper functions should only be added when they clearly support the core workflow:

1. fetch relevant papers
2. rank or select useful results
3. present a meaningful discovery view
4. let the user inspect a selected topic or paper more deeply
5. later improve personalization and AI assistance

If a task is useful mainly as Python practice but not clearly useful to the product yet, it should stay as an isolated exercise rather than being added directly to the main app.

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
