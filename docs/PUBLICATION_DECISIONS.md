# Publication decisions before public release

This file records decisions that should be made deliberately rather than inferred by an agent.

## v1.2 Release Gate — APPROVED 2026-09-24

The human froze v1.2 scope around PR #2 and TASK-001, confirmed the theme Multi-Agent Workflow / Agent Governance, and authorized Codex to complete QA, metadata, PR readiness and merge, tag, GitHub Release and PDF/DOCX assets, Pages deployment, smoke tests, and canonical-state updates without stepwise approval. Use the actual release date and preserve the v1.1 snapshot. Escalate only the conditions in `AGENTS.md` and `CURRENT_PHASE.md`.

## 1. License — COMPLETE

Author confirmed on **2026-09-16** that v1.1 continues under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Implementation:

- `LICENSE.md` added with scope and attribution guidance.
- `CITATION.cff` records `CC-BY-4.0`.
- `_quarto.yml` records the license and displays it in the HTML footer.
- README and website index state the license.

The license applies only to material for which the author holds the necessary rights; third-party material retains its own rights/licensing status.

## 2. Release date

Current visible edition is `2026-09`. Choose the exact public release date when creating the first GitHub/Zenodo release.

## 3. Zenodo DOI

Recommended after the GitHub repository is public and v1.1 release assets are final. Connect/import the repository or upload the frozen PDF/DOCX release assets, then record the DOI in:

- `README.md`
- `CITATION.cff`
- website index
- PDF/DOCX only in a future patch/version if desired; do not silently alter the frozen v1.1 files solely to add the DOI.

## 4. Start Guide link — COMPLETE

Current public URL: <https://How-Tze.github.io/psych-ai-start-guide/>.
