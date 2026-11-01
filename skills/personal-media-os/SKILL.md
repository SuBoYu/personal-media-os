---
name: personal-media-os
description: Build a personal social content workflow from brand discovery and daily notes through platform drafts, per-post approval, and publication reconciliation. Use for personal brand setup or ongoing cross-platform content management, not general social browsing or software implementation.
---

# Personal Media OS

Help a person share their actual life and work in their own voice. Keep raw stories separate from publication records. A workflow import is complete when the user has a usable destination, a concise brand brief, and one next action—not when every platform is automated.

## Route by current need

- **Onboarding:** inspect available tools; ask about goals, audience, desired voice, boundaries, capacity and existing sources. Use established answers and ask at most three questions per round. Produce a short brand brief for review before generating a monthly calendar.
- **Capture:** record an actual event, feeling, source and public/private boundary. A question awaiting an answer is an idea, not a finished draft. Never infer a personal experience from a suggested topic.
- **Plan:** choose a sustainable cadence and a few themes grounded in the brief. Suggested dates are editorial dates, not scheduled jobs. Store plans apart from content queues.
- **Draft:** use one source story for platform-specific versions; retain source links and unknown facts. Prepare the selected platform first; other platforms are optional.
- **Publish or reconcile:** read [publishing.md](references/publishing.md) before interacting with a composer or recording an outcome.
- **Notion setup or cleanup:** read [notion.md](references/notion.md) before database changes. Reuse the user's existing databases and relations.

## Capability fallback

Use connected document tools when present. Inspect their live schema and access restrictions rather than hardcoding tool names. With no writable source, deliver Markdown/JSON for manual import and clearly identify what was not saved. With no supported browser or official publisher, prepare drafts and exact manual steps; don't label them published.

For a local workflow, use the repo's `scripts/media_os.py init --workspace PATH` if a shell is available and the user selected a local destination. Never run uninspected remote installation scripts or store personal content in this public repo.

## Voice and factual integrity

Treat tone preferences as user-specific, not universal. Preserve their edits. Ask about missing motivations or experiences instead of inventing them. Avoid turning every hobby into a professional lesson. Record product claims from current sources and distinguish documented features from tested behavior.

## Pause and completion

When strategy is unsettled or the user pauses publishing, record the pause in the user's work area; keep drafts available. Resume only the specific work requested. No recurring monitoring or unattended publishing is enabled by this skill.

At completion, link actual saved artifacts, state their status and the next step. Never claim installation, login, scheduling, or publishing based only on a prompt, attempted action, or local file.
