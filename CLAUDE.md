# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

FLYSTAR77 STUDIO OS — not a software application, but a rule-driven **AI video production management system**. The repo is the studio's brain: Markdown rule files define how a short film gets produced (planning → storyboard → character → generation → rough cut → final cut → color → sound → export → promotion), and a small set of stdlib-only Python scripts automate the file/folder bookkeeping around that pipeline. There is no app to build, lint, or test in the conventional sense — "correctness" here means the folder structure, naming conventions, and generated JSON/Markdown stay consistent with the rule files.

Everything is written in Japanese. Preserve that when editing rule docs or generated production files.

## Rule files — read in this order before doing anything

Every rule doc restates the same priority list; treat it as authoritative for any decision about where a file goes or how a cut should be edited:

1. `OPERATING_MANUAL.md` — the master doc: studio vision, org chart, 5 operating layers (制作/編集/広報/品質管理/自動化), naming rules, color/camera/audio rules, per-CUT editing exceptions (CUT17/CUT18), release specs.
2. `PRODUCTION_BIBLE.md` — points to `ProductionBible/RULE.md` for detailed folder rules.
3. `AI_RULES.md` — full role split across the AI team, incl. per-role specialties/prohibitions/required-reading (see below), and the "Golden Rule": AI performs *emotion*, not line-reading.
4. `CODEX_RULES.md` — the detailed operating rulebook for the folder/automation role this agent (Claude Code) fills; written under the older name "Codex" but still authoritative for what Claude Code may automate vs. must hand off.
5. `PALMIER_RULES.md` — inputs/outputs contract for handing a cut project to Palmier for editing.
6. `AI_WORKFLOW_V1.md` — the standard CINE→SOUL→CUT→MASTER relay for generating a single CUT's storyboard/prompt brief (`Projects/<title>/Storyboard/CUT<NN>.md`), used across all MV/drama/movie productions. The four role names aren't yet defined in `AI_RULES.md` (see `Obsidian_Vault/03_Company/Decisions/2026-07-09_未決事項リスト.md` item 1) — until that's resolved, whichever AI is asked performs all four passes itself to reproduce the relay shape.

Also load `PROMPT_GUIDE.md` (generation-prompt structure), `IMAGE_GENERATION_POLICY.md` (image generation engine standard: Higgsfield + GPT Image; Nano Banana excluded from production; Soul 2 restricted to non-production creative work), `QUALITY_CONTROL.md` (pre-export checklist), and `GITHUB_OPERATIONS.md` (branching/CI/large-file policy) when the task touches those areas.

## Org chart and this agent's role (Claude Code = CTO)

- **FLY77STAR U. — CEO**: final decision-maker. All decisions are confirmed by FLY77STAR U.
- **ChatGPT / Claude (chat)**: planning, strategy, world-building, screenplay, prompt design, owns the Production Bible. **Not this agent** — if a task is actually planning/direction/story work rather than repo/file/automation work, that's this role's job, not Claude Code's.
- **Claude Code (CTO, this agent)**: GitHub operations, web publishing (Netlify), folder/file organization, generating edit hand-off artifacts (`EDIT_PLAN.md`, `edit_project.json`), automation scripts, CI/structure validation, plus Production Package design, Image QC, and Director Approval support for image/video generation. **This agent does not execute production image/video generation** (Production Policy Version 1.3, `IMAGE_GENERATION_POLICY.md`) — a 2026-07-11 exception that let Claude Code execute Higgsfield/GPT Image generation for WAKE UP Panel04 was rescinded the same day after a technical-verification task confirmed the Higgsfield MCP tools are not callable (approval-gated) from this environment; generation execution reverted to FLY77STAR U./GPT Image. Top-priority rule (v1.2, still in force): if an MCP tool, external service, or API call is blocked (approval-pending, permission denial, unknown spec), stop — never substitute a guessed value or fallback config — and report what was attempted, what blocked it, what is/isn't known, and what needs FLY77STAR U.'s input. If the same generation seed can't be technically obtained, the generation owner should fall back to using the Director-approved pilot take itself as the baseline for the next-resolution pass, rather than guessing a seed. Studio OS v1.3 (`AI_WORKFLOW_V1.md`) additionally separates investigation tasks (MCP/API/Higgsfield/Git/external services/model or permission checks) from production tasks (Production Package/image or video generation/QC/Documentation): if a blocker surfaces during investigation, do not proceed to production tasks — resolve the technical issue and report to FLY77STAR U. first, then resume production once resolved. Production Environment health takes priority over Production output.
- **Higgsfield / GPT Image**: character/visual generation (external tools, operated by FLY77STAR U./GPT Image side). Standard production engine as of 2026-07-11 (`IMAGE_GENERATION_POLICY.md`); Nano Banana is excluded from the production flow, and Higgsfield Soul 2.0 ("Soul 2") is restricted to non-production creative work (artist photos, fashion cuts, SNS visuals, mood pieces, concept art) — never used for Character Master.
- **Seedance / Gemini Omni Flash**: MV/video generation, lip-sync, character performance (external tools).
- **Palmier**: rough cut, timeline generation, dialogue/BGM sync, fades, final export (external tool). Claude Code prepares its inputs; Claude Code never does Palmier's job itself.
- **ElevenLabs**: narration/voice generation.
- **Obsidian**: company memory / internal wiki (reference only, not an authoritative rule source).
- **GitHub**: asset repository (this repo).
- **Netlify**: official site deployment.

Full per-role specialties/prohibitions/required-reading live in `AI_RULES.md` — this is a summary for orientation, not the source of truth.

### This agent's boundaries

- Do: repo/file/folder management, automation scripts, CI/structure validation, generating `Edit/EDIT_PLAN.md` / `Edit/edit_project.json` / `Edit/PALMIER_HANDOFF.md`, Netlify deploy config, GitHub operations.
- Don't: decide world-building/story/screenplay direction (that's ChatGPT/Claude chat's job — surface it, don't invent it), perform the actual timeline edit or export (that's Palmier's job — prepare its inputs instead), run destructive/irreversible operations (force push, production deploy, deleting tracked content) without explicit user confirmation even when technically capable.
- **End of task**: always summarize what changed in Japanese, and commit to Git if the change warrants it (per `AI_RULES.md` Common Rules).

## AI Production Policy (ads/CM/client work only)

Full policy text lives in `PRODUCTION_BIBLE.md` and `OPERATING_MANUAL.md` — this is Claude Code's operational checklist derived from it. Applies only to advertising/CM/client-work deliverables, not the studio's own narrative shorts (e.g. `Distances`).

- Never treat a raw Suno-only (or similar AI-music-only) track, or any AI-only-generated asset, as the final commercial deliverable — that requires human re-arrangement/re-recording/mix/master first. Flag it rather than packaging it as final.
- When generating/updating hand-off or delivery artifacts (`Delivery/`, `Edit/PALMIER_HANDOFF.md`, export notes) for ad/CM/client work, include a record of what was AI-generated and with which tool — don't silently omit this.
- Lyrics, composition/arrangement direction, melody direction, staging intent, and final creative sign-off are FLY77STAR U.'s calls, not this agent's — surface open decisions to FLY77STAR U. rather than deciding them.
- Don't reference or imply a tie-in with a real brand, competition, or company name unless formal permission is already confirmed in the project's files; if the work is a fictional brand or CM-style piece, make sure that's explicitly labeled as fiction somewhere in the deliverable/handoff notes.

## Known non-standard project: `StudioOpening`

`Projects/StudioOpening` does not follow the standard project layout above — it uses a different structure (`Palmier/`, `Edit/`, `Assets/Videos/...`) inherited from an external Palmier bundle export, and several of its subfolder names carry a trailing colon (`Assets:`, `Videos:`, `Output:`, etc.) and/or a leading space, including a duplicate near-identical pair (`" Assets:"` and `"Assets:"`). None of the automation scripts (`validate_structure.py`, `import_assets.py`, `generate_palmier_json.py`) can operate on it as-is — they're written for the `Distances`-style layout. Treat it as a legacy/manual project; don't run the standard scripts against it, and don't rename/merge its folders without explicit user sign-off, since the `.palmier` bundles inside may be referenced by path from the external Palmier tool.

## Commands

All scripts are pure Python 3 stdlib (no `requirements.txt`/venv needed). CLI conventions are **not** consistent across scripts — some take `--root`/`--project`, others take a positional project path:

```bash
# Create a new project scaffold (standard folders + starter files)
python3 scripts/create_project.py NewProjectName --cuts 18 [--root .]

# Validate standard folders, required files, project.json/CUT_LIST.json consistency
python3 scripts/validate_structure.py --project Distances [--root .]

# Generate Edit/EDIT_PLAN.md from CUT_LIST.json
python3 scripts/generate_edit_plan.py --project Distances [--force] [--root .]

# Organize Import/ into CUT/Audio/Dialogue/Unsorted, update CUT_LIST.json (positional path, not --project)
python3 scripts/import_assets.py Projects/Distances --dry-run
python3 scripts/import_assets.py Projects/Distances --apply
python3 scripts/import_assets.py Projects/Distances --assign Unsorted/video_001.mp4 CUT17

# Generate Palmier's edit_project.json from CUT_LIST.json + EDIT_PLAN.md (positional path)
python3 scripts/generate_palmier_json.py Projects/Distances [--output PATH]

# Watch external folders (per config.json) and auto-import new assets
python3 scripts/watch_import.py --project Distances --once --dry-run
python3 scripts/watch_import.py --project Distances --once
python3 scripts/watch_import.py --project Distances   # long-running, Ctrl+C to stop

# Vault Manager: file a decided-today item into Obsidian_Vault/ (not Projects/)
python3 scripts/vault_manager.py registry                                            # list known entities
python3 scripts/vault_manager.py file --category character --target MIU --text "..." # character/costume/mv/prompt/discovery/decision
python3 scripts/vault_manager.py daily-log --did "..." --done "..." --next "..."      # Daily Log (今日やったこと/完成したこと/次回やること)
python3 scripts/vault_manager.py next-action --project WAKE_UP --add "..." --done "..."
python3 scripts/vault_manager.py changelog --limit 20
```

CI (`.github/workflows/validate.yml`) runs `python scripts/validate_structure.py --project Distances` on every push/PR.

`vault_manager.py` is the odd one out in this list: everything else above operates on `Projects/` (the GitHub production folders); `vault_manager.py` operates only on `Obsidian_Vault/` (the Obsidian knowledge base — see `Obsidian_Vault/00_Start_Here/FLY77STAR_Philosophy.md` and `Obsidian_Vault/03_Company/検索システム設計書.md` for that system's design). It routes a single already-classified decision into one of seven areas — Daily Log, Discovery (発見/失敗/改善点/アイデア/次回試したい), Decision Log (採用/却下/採用理由), Character Bible, Costume Bible (採用された正史のみ; rejected options go in Decision Log instead), MV Bible (脚本/絵コンテ/CUT/プロンプト per project), Prompt Library — auto-linking known entity names, checking for literal duplicates, leaving a one-line pointer in that day's Daily Studio Report, and appending to `Obsidian_Vault/00_Start_Here/変更履歴.md`. It does not classify free text for you — that judgment call is made by whoever calls it (a human, or Claude Code reading the raw text). `vault_manager.py ingest` is a documented-but-unimplemented stub for a future adapter that would extract decisions from an exported ChatGPT conversation.

Caution when testing any of the above with `--dry-run`/no-op flags: several still write report files as a side effect even in dry-run mode (`import_assets.py` always rewrites `Edit/import_report.md`, `watch_import.py` rewrites `Edit/watch_import_report.md`). If you run these just to sanity-check behavior, check `git diff` afterward and revert the report file if it clobbered a meaningful prior report.

## Per-project structure and file relationships

Each project lives at `Projects/<name>/` with standard subfolders (`Import`, `Unsorted`, `CUT`, `Audio`, `Dialogue`, `Reference`, `Prompt`, `Edit`, `Storyboard`, `Color`, `QC`, `Delivery`, `Export`) — except `StudioOpening`, see above. The data flow across scripts:

```
CUT_LIST.json  (per-CUT role, recommendedSeconds, dialogue flag, asset path)
   ↓ generate_edit_plan.py
Edit/EDIT_PLAN.md  (timeline table: CUT | timeline | duration | role | dialogue sync)
   ↓ generate_palmier_json.py  (also reads project.json + scans media under CUT/Audio/Dialogue/Reference)
Edit/edit_project.json  (schema "flystar77.palmier.edit_project.v1": full timeline, tracks, transitions,
                          fades, BGM/dialogue/environment sync plans, export targets — this is what gets
                          handed to Palmier)
```

`import_assets.py` is the other producer/consumer of `CUT_LIST.json`: it classifies files dropped in `Import/` by filename (`CUT_RE` regex `cut[\s_-]*(?<!\d)(1[0-8]|0?[1-9])(?!\d)` — the `(?<!\d)` guards against misparsing e.g. `cut19` as `CUT09`), routes video/image to `CUT/`, dialogue-hinted audio to `Dialogue/`, everything else audio to treated as music/BGM, and anything it can't confidently assign a CUT number to goes to `Unsorted/` for manual `--assign`. It never overwrites existing CUT files — collisions get `_take02`, `_take03`, etc.

`generate_palmier_json.py`'s project name/title (timeline name, export filenames) is derived from `CUT_LIST.json`/`project.json`, so it's safe to run against any project. Its per-CUT *creative timing* is still **Distances-specific** and hardcoded as Python literals, not generic config: `DIALOGUE_HOLDS` (pre-roll/post-hold timing for CUT06/CUT12/CUT17), `transition_for()`/`fade_for()`/`bgm_sync_for()`/`environment_for()` (hardcoded behavior for CUT01/02/05/09/11/15/17/18). A new project reusing this generator will silently get Distances' CUT06/12/17/18 timing applied to its own cuts — these functions need generalizing (e.g. reading timing from `CUT_LIST.json` per cut) before they're meaningful for another title.

`watch_import.py` reads `config.json` for `watchFolders` per project, polls them, copies new supported media (`.png/.jpg/.jpeg/.webp/.mp4/.mov/.wav/.mp3`) into that project's `Import/`, then invokes `import_assets.py`; state is tracked in `Edit/watch_state.json` and a report written to `Edit/watch_import_report.md`.

## Naming conventions (enforced by `import_assets.py`'s regex, not just documentation)

- CUT video: `CUT01.mp4` … `CUT18.mp4`
- Dialogue: `CUT06_dialogue.wav`
- Prompt: `CUT06_Dreamina.md`
- CUT detection regex matches `cut` (any case) + optional separators + `1`-`18`, guarded so it can't start mid-way through a longer number; anything outside that range or unmatched goes to `Unsorted/`.

## Git conventions (from `GITHUB_OPERATIONS.md`)

- Branches: `main` (stable/deliverable), `develop` (in-progress), `project/<name>` (per-title work), `automation/<feature>` (script changes).
- PR checklist expects: no violation of `OPERATING_MANUAL.md`/`PRODUCTION_BIBLE.md`, `validate_structure.py` passing, naming rules followed, `Edit/EDIT_PLAN.md` updated alongside any edit-instruction change, and no accidental large finished-video commits.
- Large-file policy: only intentional finished deliverables are tracked; `.gitignore` excludes `Exports/*.mp4` and `Projects/*/Export/*.mp4`.
