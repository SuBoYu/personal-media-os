# Product scope — v0.1

## Promise

Download once, start setup with one prompt. The user gets a reusable brand-and-content workflow, not someone else's persona or an automatic social account takeover.

## Delivered MVP

- Portable Skill and a plain-document entry point for environments without skill installation.
- Local workspace initialization with no remote calls or third-party Python packages.
- Example brief and editorial schema guidance; Notion setup is agent-mediated through the user's connected tools, not a bundled API client.
- A single-source content model, platform versions, explicit approvals and publication reconciliation.
- A distributable Skill ZIP generated only from allowlisted resources.

## Capability tiers

| Environment | Expected result |
| --- | --- |
| Chat with readable attachments | Interview, brief, drafts and manual publishing instructions |
| Host with Skills | Reusable invocation after the user installs through the host |
| Notion connection with edit access | Reuse/create tracker after inspecting bindings and destination |
| Controlled browser and signed-in account | Prepare and publish supported posts after approval |
| Official publisher + OAuth | Future adapter; not included in this release |

The one-prompt flow must expose unsupported capabilities early. It cannot silently install a connector, grant OAuth, bypass login, or create a scheduled job.

## Acceptance scenarios

1. New user without Notion: receives a local brief and one next action, no fabricated database URL.
2. Existing Notion workspace: reuses matching sources and channels; repeating onboarding creates no duplicate databases.
3. User edits a preview: the previous approval cannot authorize the new version.
4. Publication response is uncertain: reconciliation happens before any retry.
5. Publication succeeds, database write fails: retry only the database write.
6. User pauses: no further publishing; plans remain optional.
7. All distribution artifacts exclude private workspace files and account IDs.

Python tests verify initialization, refusal to overwrite and packaging isolation. These scenarios still need cross-account host testing before a broad product release.

## Next releases

First validate onboarding with two fresh users. Then package a plugin using the current official plugin specification, add verified Notion bindings, and only then consider official publishing adapters. Do not advertise a connector or plugin as shipped before those tests and packaging are complete.

Repository name, visibility and license are owner decisions. No license grant is included until the owner selects one.
