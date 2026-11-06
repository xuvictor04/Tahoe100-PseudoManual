# Design contract: the physics views of the map, and the literature-review agents

Engineering contract for two additions. User-facing docs: `docs/review.md` and the map's own help panel.

---

## Part 1 — the map gets tabs, three of them physics simulations (`tahoemap/html_map.py`)

`OUT/map/gene_map.html` stays ONE self-contained file (no network, no external JS/CSS). It gets a tab bar; each tab
is a separate display with its own canvas and controls; the side panel (selected gene: partners, drugs, lines) and the
search box are shared by all tabs, and selecting a gene in one tab selects it in all.

| Tab | What it shows |
|---|---|
| Nodal map | the existing t-SNE layout of 1 − \|cos\| (opposite genes together) |
| Signed vector map | the existing t-SNE layout of 1 − cos (opposite genes apart) |
| Physics: neighbourhood | a live force simulation of the selected gene, its partners and (depth 2) their partners |
| Physics: module | a live force simulation of one module (all its members and the edges among them) |
| Physics: all genes | a live force simulation of every gene in the space, started from the nodal-map positions |
| How to read this | the help text (what each tab means, colours, controls) |

**The simulation** (one engine shared by the three physics tabs, vanilla JS, typed arrays):
- **Springs** on graph edges: attractive force ∝ weight × (distance − rest length), weight = |cos|, rest length
  shorter for stronger edges. Edges come from `graph/edges.parquet` (the kNN graph that defines the modules) for the
  module and all-genes tabs, and from each gene's top partners (`relations`, as already embedded) for the
  neighbourhood tab, filtered by the tab's controls (minimum |cos|, evidence: both halves / also one half).
- **Repulsion** between every pair of nodes (Coulomb-like, 1/d), computed with a Barnes-Hut quadtree (θ ≈ 0.8) so
  15,000 nodes stay interactive; a weak pull to the centre; velocity damping; an "alpha" that cools so the layout
  settles, and is re-heated by any change.
- **The sign switch**: "opposite genes attract" (red edges are springs like green ones → the nodal view: both arms
  of a pathway form one cluster) vs "opposite genes repel" (red edges push their two genes apart → the signed view:
  the − arm separates from the + arm). Flipping it re-heats the simulation so the user watches the arms part.
- **Interaction**: pan/zoom, drag a node (its neighbours follow), double-click to pin/unpin, click to select (side
  panel), pause/resume, re-heat, reset; sliders for repulsion strength, spring strength, minimum |cos|; colour by
  module or by arm; labels for the selected gene, its partners and (when zoomed in) everyone.
- **Neighbourhood tab**: depth 1 or 2 (default 2), at most N nodes (default 300; the strongest partners first);
  edges green (moves with) / red (moves opposite), thickness ∝ |cos|; the centre gene is pinned at the start.
- **Module tab**: a module picker (dropdown + "module of the selected gene"), its label and arms; nodes coloured by
  arm; optional dimmed ring of 1-hop outside genes.
- **All-genes tab**: nodes start at the nodal-map coordinates; edges hidden while moving (drawn for the selected
  gene only); a frame-time budget so the page stays responsive (several ticks per frame when fast, fewer when slow).
- Data: embed `graph/edges.parquet` compactly (index pairs + quantised cos) — target ≤ +4 MB at 177,000 edges; the
  page must still open in a few seconds at 15,000 genes.

---

## Part 2 — the literature-review agents (`tahoemap/review/`)

One agent run per entity (gene, drug, cell line) reads a **dossier** of what the data say about that entity, searches
the literature, and returns a structured **review**: what is established (with citations), what in the data is
unexpected, which expected connections are missing, and what is contradicted. Every request and response is saved.
API keys can run out mid-run and be switched; the run resumes where it stopped.

### Surface

The Anthropic Python SDK (`anthropic`; every request streamed: `client.beta.messages.stream(...)` as a context manager,
then `get_final_message()`), our own agent loop (so every turn is logged and
every error is typed), custom tools we execute locally, and Anthropic's server tools for the web. Model: every agent
defaults to `claude-opus-5-5` (the user can choose per agent: `--model`, or the agent file). Effort via
`output_config={"effort": ...}` (reviewers `high`, checker `medium` by default); adaptive thinking (omit `thinking`);
refusal fallback opted in by default: `betas=["server-side-fallback-2026-07-01"]`, `fallbacks="default"`; prompt
caching: the system prompt (agent + skills) carries `cache_control`, and top-level `cache_control={"type":
"ephemeral"}` caches the growing conversation. Append each `response.content` unchanged to the messages (thinking and
server-tool blocks included; an empty `content` is never sent back). `max_tokens` by effort: 64K up to `high`, 128K
at `xhigh` / `max`. `stop_reason`: `tool_use` → run our tools, return all results in one user message;
`pause_turn` → resend as is; `refusal` → record status `refused` with `stop_details.category` (but when
`stop_details.recommended_model` is set the fallback model was not tried: a temporary `failed`, retried later);
`max_tokens` → a nudge (two cut-offs in a row end the attempt); `end_turn` without a submitted review → a nudge (two in
a row: status `no_review`). Each user message after the first ends with a budget line (spend and requests so far; near
the cap or `max_turns`: submit now), appended and never edited, so the cached prefix stays stable.
Before writing SDK calls, read (do not guess):
`/tmp/claude-0/bundled-skills/2.1.319/80c569fdc02ccc03f6aacbfd35f8757c/claude-api/` → `python/claude-api/README.md`,
`python/claude-api/tool-use.md`, `shared/tool-use-concepts.md`, `shared/error-codes.md`, `shared/prompt-caching.md`,
`shared/model-migration.md` (search "fallbacks" and "Claude Opus 5.5"). Installed: `anthropic` 2.6.0.

### Files and interfaces

```
tahoemap/review/
  __init__.py
  agents/            gene-reviewer.md, drug-reviewer.md, line-reviewer.md, citation-checker.md
  skills/            literature-search/SKILL.md, reading-tahoe-data/SKILL.md, connection-audit/SKILL.md,
                     citations/SKILL.md, writing-the-note/SKILL.md
  definitions.py     load_agent(name) -> AgentDef ; load_skill(name) -> str
  dossier.py         entities(out, kinds) -> DataFrame ; build(out, kind, name) -> Dossier
  tools.py           custom tool schemas + execute(name, input, ctx) ; server_tools(web, max_uses)
  verify.py          check_ids(review, ctx) ; build_check_prompt(review, abstracts) ; CHECK_TOOL schema
  keys.py            KeyPool
  history.py         History (per run JSONL) ; Ledger (append-only JSONL of attempts)
  runner.py          run(out, ...) ; status(out) ; the agent loop
  fake.py            a scripted fake client for tests (no network, no key)
```

**Agent and skill files** use Claude Code's markdown format, so they also work if copied into `.claude/agents/` and
`.claude/skills/`:
- agent: YAML frontmatter `name`, `description`, `model` (default `claude-opus-5-5`), `effort`, `tools` (list of tool
  names: custom + `web_search` / `web_fetch`), `skills` (list), `max_turns`, `max_usd`; body = system prompt.
- skill: `skills/<name>/SKILL.md`, frontmatter `name`, `description`; body = instructions. The runner appends the
  bodies of the agent's skills to its system prompt (stable order → cacheable).
- `AgentDef` = dataclass(name, description, model, effort, tools, skills, max_turns, max_usd, system: str) where
  `system` = body + the skills' bodies.

**Dossier** (`dossier.build(out, kind, name)` → `Dossier(kind, name, entity_id, text, data)`): markdown text (≤ ~8,000
tokens, size-bounded) + the same facts as a dict. Built only from the run's outputs (tables, relations, graph,
validation, reference, embed). Contents:
- gene: identity (HGNC name, location, UniProt function snippet); expression (lines measured, level); strongest clean
  drug-doses up / down (pooled) and strongest per-line responses; module, arm, module label; **data partners**: top 25
  moving with and top 25 moving opposite (cos, evidence, fdr, mutual rank, specificity, locus / readthrough, known:
  STRING score / shared pathway / gene group); **known but absent**: literature-known partners (STRING ≥ 700, or a
  shared Hallmark / Reactome pathway ≤ 100 genes, at most 30) that are NOT among its 100 data partners, each with its
  cosine to the gene if both are in the space, else the reason (not measured / not in the vector space); novel
  candidate pairs involving the gene.
- drug: targets, MOA, approval; per dose: wells, flags, genes up/down; top genes up / down at the best trustworthy dose;
  target genes' own mRNA response; modules it moves; lines it depletes / that respond most; nearest drugs by vector.
- line: organ, drivers, TP53 status; genes specifically high / low at baseline; strongest responses; drug-doses that
  deplete it; components it responds to more / less than the typical line.
- `entities(out, kinds)` → columns kind, name, entity_id (`gene:<col>`, `drug:<name>`, `line:<cell_line_id>`),
  label, priority (higher first: lines and drugs first; genes by novel-candidate pairs, strong reproducible
  partners, module label, significant clean drug-doses).

**Tools** (`tools.py`): custom tools, all `strict: true`, executed locally, results as text:
- `pubmed_search(query, max_results ≤ 20)` → PMID, year, journal, title (NCBI E-utilities esearch + esummary; 3
  requests/s, or 10 with `NCBI_API_KEY`; polite `tool`/`email` parameters configurable; on-disk cache in
  `OUT/review/cache/`).
- `pubmed_abstracts(pmids ≤ 10)` → title, year, journal, abstract text (efetch), cached.
- `europepmc_search(query, max_results ≤ 20)` → PMID/PMCID/DOI, year, title, cached.
- `tahoe_lookup(kind, name)` → the short dossier summary of another gene / drug / line (so an agent can check a
  partner), bounded length.
- `submit_review(...)` — the final answer (the loop ends when it is called with a valid payload). Schema:
  `summary` (str), `established` (list of {partner_or_topic, relation, data_evidence, citations: [PMID/DOI strings],
  confidence}), `unexpected` (list of {observation, data_evidence, why_unexpected, literature_checked: [queries],
  confidence}), `missing` (list of {expected_connection, source (STRING/pathway/literature), data_status, likely_reason,
  citations}), `contradicted` (list of {claim, data_evidence, citations}), `connection_verdicts` (list of {partner,
  verdict ∈ established | indirect | plausible | unexpected | contradicted, citations}), `open_questions` (list of
  str), `note_markdown` (the vault note body, with citations as `[PMID:123](https://pubmed.ncbi.nlm.nih.gov/123/)`).
- server tools (when `--web`, default on): `{"type": "web_search_20260209", "name": "web_search", "max_uses": N}`,
  `{"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": N}` (do not also declare code execution).
- `execute(name, input, ctx)`; `ctx` = ToolContext(out, entity, cache_dir, http settings).

**Verification** (`verify.py`): after a review is submitted: (1) `check_ids`: every cited PMID exists (esummary) — a
nonexistent PMID removes that citation and marks the item `unverified`; (2) unless `--verify ids`, the
**citation-checker** agent gets each claim with the abstracts of its citations and returns, through a strict
`submit_check` tool, a verdict per claim (supported / partly / not supported / not checkable). The stored review
carries both. Default `--verify llm`.

**Keys** (`keys.py`): `KeyPool(keys_file=None, env=True, interactive=bool)`. Sources in order: `--keys-file PATH` (one
key per line, `#` comments; warn if readable by others), `ANTHROPIC_API_KEYS` (comma-separated) and
`ANTHROPIC_API_KEY`, else the SDK's default credential chain (`anthropic.Anthropic()` resolves an `ant auth` profile).
`key_id` = last 4 characters + a short hash; keys are never written to disk or logs (scrub them from error text).
Classify errors by the SDK's typed exceptions / `.type`:
- **dead key** (rotate, retry the entity from the start with the next key): `AuthenticationError` (401),
  `PermissionDeniedError` (403), status 402 / `type == "billing_error"`, `EnforcedSpendLimitReachedError`,
  `OrganizationOnHoldError`.
- **wait** (SDK retries once first; then exponential backoff with jitter up to 10 min, no rotation): `RateLimitError`,
  `OverloadedError` / 529, ≥ 500, an error event in the middle of a stream; `APIConnectionError`, `APITimeoutError`
  and a stream cut short ("lost responses") only twice, each charged a conservative estimate when it may have
  reached the API (an attempt over its cap only through estimates is `failed`, not `over_budget`).
- **systematic**: the same error on 5 entities in a row stops the run (exit code 4); those failures are not counted
  against the entities (ledger `note` lines).
- **entity failure** (record, move on): 400 other than billing, 404, 413.
When every key is dead: interactive (a TTY) → ask for a new key with `getpass` ("press Enter to stop"); otherwise
(and on Enter or Ctrl-C) → **pause**: unfinished entities stay pending, exit code 3, message: add a key and run
again. The main thread asks (the pool lock is not held while asking); a key given to `--keys-file` instead of a path
is refused without being shown.

**History and ledger** (`history.py`):
- `OUT/review/history/<kind>/<safe name>/<run_id>.jsonl` — every event of one attempt: `start` (agent, model,
  effort, key_id, system prompt sha256, tool list, dossier sha256, code version), `request` (the messages appended
  since the previous request), `response` (`response.to_dict()` in full, usage, cost), `tool` (name, input, result —
  results longer than 20,000 characters truncated with a note), `error` (typed class, status, scrubbed message),
  `end` (status, totals). The system prompt and dossier text are stored once per attempt in the `start` event.
- `OUT/review/ledger.jsonl` — one line per finished attempt: entity_id, kind, name, run_id, agent, model, status
  (`done`, `refused`, `no_review`, `over_budget`, `failed`, `paused`, `key_rotated`), cost_usd, input / output /
  cache tokens, web searches, n_requests, n_tool_calls, key_id, started, finished, error. The latest line per
  entity is its state (`done` and `refused` are final unless `--redo`; `failed` is retried up to 2 times, then only
  with `--retry-failed`). Lines with status `note` (a late response's cost, an uncounted systematic failure) are
  bookkeeping, not states. Every line is written after a newline guard, so a line cut by a crash never swallows the
  next one.
- Outputs: `OUT/review/reviews/<kind>/<safe name>.json` (submitted payload + verification + metadata),
  `OUT/review/notes/<kind>/<safe name>.md` (note body for the vault), `OUT/review/connections.parquet` and
  `OUT/review/findings.parquet` (built by `status --tables` / at the end of each run from the review JSONs).

**Cost**: price table per model (USD / MTok: input, output, cache write 1.25× input, cache read 0.1× input ...
`claude-opus-5-5` 4 / 20, `claude-sonnet-5-5` 2 / 10, `claude-haiku-5-5` 0.10 / 0.50; web search $0.01 each); cost
from `response.usage` (per `usage.iterations` entry when present, at that entry's model). Per-entity cap
(`--per-entity-usd`, default from the agent file, e.g. 3.00): exceeding it ends the attempt (`over_budget`, the
partial history kept). Total cap `--max-usd` (no default: unlimited only when the user says so; the runner refuses to
start without `--max-usd` or `--limit` unless `--no-cap` is given, and prints the projected cost first).

**Runner / CLI**: `python -m tahoemap review <plan|run|status|tables>` (also `tahoe review ...`):
- `plan` → writes `OUT/review/queue.parquet` (entities in priority order) and prints counts + a cost projection
  (from the dossier sizes; after some reviews, from the mean real cost per kind).
- `run` → options `--kinds gene,drug,line`, `--only NAMES` (comma list or @file), `--limit N`, `--max-usd X`,
  `--per-entity-usd Y`, `--concurrency 4` (threads; each owns one entity's loop), `--model`, `--effort`,
  `--verify llm|ids|off`, `--web/--no-web`, `--web-max-uses 5`, `--keys-file`, `--redo`, `--retry-failed`,
  `--recheck` (only the verification stored reviews lack: the id look-ups, the citation checker), `--dry-run` (writes
  the dossiers and the first request of each to `OUT/review/dry_run/`, calls nothing), `--fake SCRIPT` (tests).
- `status` → counts by status and kind, spend total and per kind, projected cost of the rest, dead keys (ids only).
- Ctrl-C / SIGTERM / SIGHUP: finish no new entities, mark running ones `paused` (a review already submitted is
  stored as `done`, its unfinished verification marked not run), write the ledger, exit (130 / 143 / 129). A response
  arriving after its attempt was closed is recorded (a `late` history event, a ledger `note`). `review/.run.lock`
  holds pid, host and process start time; a lock whose process is gone is stale (POSIX and Windows).
- The vault stage splices `OUT/review/notes/...` into the gene / drug / line notes under "## What the literature says"
  (a callout: AI-agent review, model, date, verification counts, link to the history file) and adds a `literature`
  column (connection verdict) to the partner tables; the map's side panel shows the verdicts.

**Duplicate**: `python -m tahoemap duplicate DEST` (`tahoe duplicate DEST`) copies a finished output folder for the
review work: large immutable arrays (atlas, tensor, tables, embed, relations, graph) are hard-linked when on the same
file system (else copied), everything else is copied; writes `DEST/duplicated_from.json` (source, date, code commit,
stage stamps). With `--repo DIR` it also clones this code repository into DIR (`git clone`), so code and outputs of
the review copy can evolve separately.
