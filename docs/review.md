# Literature-review agents

`tahoe review` sends AI agents through a finished run: one agent per gene, drug or cell line reads what the run's
data say about it, searches the literature, and writes a cited review. The reviews go into the Obsidian vault (a
section **What the literature says** in each reviewed note, and a **Literature** column in the gene notes' partner
tables) and into the HTML map (a small `lit:` badge next to a partner in the side panel).

It is optional, it costs money (an Anthropic API key is needed), and it never changes the run's data: you can run it
on part of the genes, stop it, and resume it whenever you like. The engineering contract is
[DESIGN-review-and-physics.md](DESIGN-review-and-physics.md), Part 2; the code is `tahoemap/review/`.

```bash
tahoe review plan                                  # the queue, in priority order, and what it would cost
tahoe review run --dry-run --limit 3               # the dossiers and first requests of 3 entities; sends nothing
tahoe review run --kinds line --max-usd 75         # the 50 cell lines (~$60 projected), at most $75
tahoe review status                                # counts, spend, projected cost of the rest, dead keys
tahoe vault; tahoe map                             # put the reviews into the vault and the map (or: tahoe run)
```

Contents: [What the agents do](#what-the-agents-do-and-do-not-do) · [Agents and skills](#the-agents-and-skills) ·
[Costs](#costs) · [Keys](#keys) · [Running, stopping, resuming](#running-stopping-resuming) ·
[Histories and the ledger](#histories-and-the-ledger) · [Verification](#verification) ·
[In the vault and the map](#in-the-vault-and-the-map) · [The duplicate workflow](#the-duplicate-workflow) ·
[Windows and macOS](#windows-and-macos)

## What the agents do, and do not do

For each entity the runner builds a **dossier** from the run's own outputs (tables, relations, graph, validation,
reference annotations, vector space) — for a gene: its identity, expression, the drug-doses that raise and lower it,
its module and arm, its 25 strongest partners each way with their evidence, the literature-known partners that are
*not* among its data partners, and its novel candidate pairs; for a drug: targets, mechanism, the genes each dose
moves, the lines it depletes, the nearest drugs; for a cell line: organ, drivers, TP53, the genes specifically high
or low, the drugs that deplete it. `tahoe review run --dry-run` writes the dossiers so you can read them.

The agent then:

- searches PubMed and Europe PMC (our own tools, run on your machine; cached in `review/cache/`), and the web
  (Anthropic's server-side web search and web fetch; `--no-web` turns them off);
- looks up other genes, drugs and lines of the run (`tahoe_lookup`) to check a partner;
- reads the abstracts of the papers it wants to cite;
- submits a structured **review**: a summary; what is **established** (with citations); what in the data is
  **unexpected**; which expected connections are **missing** (and the likely reason); what is **contradicted**; a
  **verdict for each connection** it judged (established, indirect, plausible, unexpected, contradicted); open
  questions; and the text of the vault section.

After it submits, every cited PMID / DOI is looked up, and a second agent, the **citation checker**, compares each
claim with the abstracts it cites ([Verification](#verification)).

The agents do **not**: change any table, number, note section or map position of the run (their output lives in
`review/` and is only *shown* by the vault and the map); run analyses of their own; read full texts behind paywalls
(they read abstracts, and open pages through web fetch); see each other's reviews; or get checked by a person. A
review is a set of leads with references, not an established fact: the vault says so in every reviewed note.

What leaves your machine: the dossier (gene / drug / line names and this run's numbers) and the conversation go to
the Anthropic API; search queries go to NCBI E-utilities, Europe PMC and Crossref (at most 3 requests a second each;
10 with `NCBI_API_KEY`; set `NCBI_EMAIL` to give NCBI a contact address).

## The agents and skills

| Agent (`tahoemap/review/agents/`) | Reviews | Default model, effort | Per-entity cap |
|---|---|---|---|
| `gene-reviewer.md` | one gene: drug responses, partners, missing / contradicted connections | `claude-opus-5-5`, high | $3.00 |
| `drug-reviewer.md` | one drug: mechanism vs response, genes, modules, depleted lines, similar drugs | `claude-opus-5-5`, high | $3.00 |
| `line-reviewer.md` | one cell line: identity, drivers, specific genes, drugs that deplete it | `claude-opus-5-5`, high | $3.00 |
| `citation-checker.md` | the claims of a submitted review against their abstracts | `claude-opus-5-5`, medium | $0.50 |

| Skill (`tahoemap/review/skills/<name>/SKILL.md`) | What it teaches |
|---|---|
| `reading-tahoe-data` | what every number of a dossier means and how far it can be trusted |
| `connection-audit` | the verdict rubric and how to fill the review's sections |
| `literature-search` | searching PubMed / Europe PMC well (symbols, aliases, MeSH, drug salts), when to stop |
| `citations` | which papers may be cited for what, PMID / DOI formats, retractions |
| `writing-the-note` | the vault section: structure, length, tone, links |

The files are in **Claude Code's markdown format**: YAML frontmatter, then the text. An agent's frontmatter has
`name`, `description`, `model`, `effort`, `tools`, `skills`, `max_turns` (requests per attempt) and `max_usd` (the
per-entity cap); its body is the system prompt, and the runner appends the bodies of its skills, always in the same
order (so the prompt is cached between requests and entities). To change what the agents do, edit these files: the
next run uses them (the history of each review records the sha256 of the exact system prompt it got). Keep the
changes in git (or in the clone of the [duplicate workflow](#the-duplicate-workflow)) so you know which prompt wrote
which review. `--model` and `--effort` override the files for one run, for all reviewers (`--model
claude-sonnet-5-5`) or per agent (`--model gene=claude-sonnet-5-5,checker=claude-haiku-5-5`; agents: gene, drug,
line, checker, reviewers, all).

**Using them interactively in Claude Code**: copy `tahoemap/review/agents/*.md` into a project's `.claude/agents/`
and the `tahoemap/review/skills/*` folders into `.claude/skills/`. Claude Code does not have tahoemap's own tools
(`pubmed_search`, `pubmed_abstracts`, `europepmc_search`, `tahoe_lookup`, `submit_review`), so in the copies replace
the `tools:` line with Claude Code's (for example `tools: Read, Grep, Bash, WebSearch, WebFetch`) or delete it, and
delete any field your Claude Code version does not accept (`effort`, `max_turns`, `max_usd` are for tahoemap's
runner). Give the agent a dossier — `tahoe review run --dry-run --only NQO1 --limit 1` writes
`review/dry_run/gene/NQO1.dossier.md` — and the look-ups (`tahoe gene NQO1`, `tahoe pair NQO1 HMOX1`). A review
written that way is not verified and not spliced into the vault; only `tahoe review run` does both.

## Costs

**Prices** the runner counts with (USD per million tokens; `PRICES` in `tahoemap/review/runner.py`; check the
current price list before a large run):

| Model | Input | Output | Cache write (5 min) | Cache read |
|---|---|---|---|---|
| `claude-opus-5-5` (default) | 4.00 | 20.00 | 5.00 (1.25x input) | 0.20 |
| `claude-sonnet-5-5` | 2.00 | 10.00 | 2.50 | 0.20 |
| `claude-haiku-5-5` (prompts ≤ 100K tokens) | 0.10 | 0.50 | 0.125 | 0.01 |

Web searches cost $0.01 each. The cost of every response is computed from its `usage` (each `usage.iterations`
entry at its own model, so a response finished by a fallback model is counted at that model's price) and stored in
the history and the ledger.

**Per-entity estimate**: before any review of a kind exists, the runner estimates from the size of the agent's
system prompt and tool definitions and of a few dossiers: ~14 requests whose context grows by ~2,500 tokens each
(read from the cache), the output per request at the agent's effort (low 800 ... high 2,500 ... max 6,000 tokens), 3
web searches and the citation check. Once 3 entities of a kind are reviewed, the mean of their **real** cost replaces
the estimate. `tahoe review plan` prints the projection per kind and in total; `tahoe review status` projects the
rest. On the synthetic test data the estimate is ~$1.17 per gene and ~$1.16 per drug or line (Opus 5.5, effort
high, `--verify llm`); `--model claude-sonnet-5-5 --verify ids` roughly halves it.

**How many**: the queue holds every gene with a response or a place in the vector space — about **15,000 genes** on
the full data — plus ~379 drugs and 50 lines. At ~$1.2 an entity, **a full gene pass costs on the order of $18,000**;
the drugs and lines together ~$500. So start small and project from real costs:

1. `tahoe review plan` (free): the queue and the projection.
2. `tahoe review run --dry-run --limit 5` (free): read a few dossiers and the exact first requests.
3. `tahoe review run --limit 20` (or `--only NQO1,HMOX1,TP53` / `--only @genes.txt`): ~$25; then
   `tahoe review status` shows the real cost per entity, and the projection of the rest uses it.
4. Then by priority: the queue puts the 50 lines first, then the drugs, then the genes in order of interest (novel
   candidate pairs, strong reproducible partners, labelled modules, many clean drug responses). `--kinds line,drug`,
   then `--kinds gene --limit 500 --max-usd 600`, and so on: each run continues where the last stopped.

**Caps**: `--per-entity-usd Y` (default: the agent file's `max_usd`, $3.00): an attempt that has spent it stops
(status `over_budget`; its partial history is kept); the citation checker has its own cap ($0.50). `--max-usd X`: no
new entity starts once the run has spent X, and the running ones pause. The runner **refuses to start** without
`--max-usd` or `--limit` (unless you give `--no-cap`), and always prints the projected cost first. `--concurrency N`
(default 4) reviews N entities at once; it changes speed, not cost.

## Keys

The runner looks for keys in this order and uses them in that order:

1. `--keys-file FILE`: one key a line; blank lines and `# comments` are ignored.
   ```text
   # tahoe review keys
   sk-ant-api03-AAAA...
   sk-ant-api03-BBBB...
   ```
   Make it readable only by you (`chmod 600 FILE`); the runner warns when other users can read it.
2. `ANTHROPIC_API_KEYS` (comma-separated), then `ANTHROPIC_API_KEY`.
3. With none of these, the SDK's own credentials (`ANTHROPIC_AUTH_TOKEN`, or a profile of the `ant` CLI) if found.

Prefer the file or the environment over typing a key on a command line (shell history, process lists);
`read -rs ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY` sets it without echoing it or keeping it in the
history.

**Keys are never written anywhere**: they live in the runner's memory only. Histories, the ledger, logs and
`review/keys_state.json` name a key by its **id** — its last 4 characters and a short hash, e.g. `KEY1-f2e60909` —
and every error message is scrubbed of anything that looks like a key before it is stored or printed.

**Rotation and running out of credit**: an error that means the key itself no longer works — 401 (invalid), 403
(no permission), 402 / `billing_error` (credit used up), a spend limit reached, an organisation on hold — marks the
key **dead** (`tahoe review status` lists dead key ids), and the entity in progress **restarts from the beginning
with the next key** (the cut-off attempt is recorded as `key_rotated`, with its history and cost). Rate limits,
overload (429, 529), server errors and network errors do not rotate: the SDK retries, then the runner waits with
exponential back-off (up to 10 minutes, Retry-After honoured) and retries the same request.

When **every** key is dead:

- in the foreground (a terminal), the run asks: *Paste a new Anthropic API key (it is not saved anywhere), or press
  Enter to stop*. A pasted key is used at once (and only for this run);
- in the background, or when you press Enter, the run **pauses**: the entities not finished stay pending, the exit
  code is 3, and the message says to add a key. Add credit or a key (`ANTHROPIC_API_KEY`, `ANTHROPIC_API_KEYS`, the
  keys file) and run **the same command again**: it continues with the entities still pending.

## Running, stopping, resuming

`tahoe review run` runs **in the foreground** by default, so that it can ask for a new key: keep the terminal open
(or use `screen` / `tmux`). Ctrl-C stops it cleanly: no new entity starts, the ones in progress get 15 seconds and are
then marked `paused`, the ledger and the tables are written (a second Ctrl-C stops at once).

`tahoe review run --background ...` runs it as a job like `tahoe run` (safe to log out): `tahoe` shows that it runs
and its last lines, `tahoe log` follows it, `tahoe stop` stops it as Ctrl-C does. A job cannot ask for a key, so it
needs `--keys-file` or `ANTHROPIC_API_KEY(S)`, and it pauses (exit code 3) when they are all used up. One review run
at a time per output folder (`review/.run.lock`); `tahoe review run` refuses while a pipeline job runs on the folder.

| Option | |
|---|---|
| `--kinds gene,drug,line` | which kinds (default all) |
| `--only NAMES` / `--only @FILE` | these entities only: names, gene symbols or ids (`gene:12`, `drug:Bortezomib`, `line:CVCL_0023`), comma-separated, or one a line in FILE |
| `--limit N` | start at most N entities (in queue order) |
| `--max-usd X`, `--per-entity-usd Y`, `--no-cap` | see [Costs](#costs) |
| `--model`, `--effort` | override the agent files (see above) |
| `--verify llm\|ids\|off` | see [Verification](#verification) (default llm) |
| `--no-web`, `--web-max-uses 5` | Anthropic's web search / fetch off, or the uses per request |
| `--concurrency 4` | entities at once |
| `--redo` | review again entities that are done |
| `--dry-run` | write the dossiers and first requests to `review/dry_run/`; send nothing |

**Resuming** needs nothing special: the latest ledger line of each entity is its state, and a run starts only what
is not final. `done` and `refused` (the model declined; `stop_details.category` is recorded) are final unless
`--redo`; `failed` and `no_review` (it never submitted) are retried, up to 3 attempts; `over_budget` is retried only
with a higher `--per-entity-usd`; `paused` and `key_rotated` start again from the beginning.

## Histories and the ledger

Everything is under `<output>/review/`:

| Path | What |
|---|---|
| `queue.parquet` | the entities in priority order with their state (`tahoe review plan`) |
| `ledger.jsonl` | one line per finished attempt (append-only) |
| `history/<kind>/<name>/<run_id>.jsonl` | every event of one attempt |
| `reviews/<kind>/<name>.json` | the submitted review + its verification + metadata (model, date, cost, history path ...) |
| `notes/<kind>/<name>.md` | the vault section the agent wrote |
| `connections.parquet`, `findings.parquet` | every connection verdict / every finding of every review, one row each (rebuilt at the end of each run and by `tahoe review tables`) |
| `dry_run/`, `cache/`, `keys_state.json`, `review.log` | dry-run files, the literature cache, key ids and which are dead, the log |

A **ledger** line: entity_id, kind, name, run_id, agent, model, status (`done`, `refused`, `no_review`,
`over_budget`, `failed`, `paused`, `key_rotated`), cost_usd, input / output / cache-write / cache-read tokens, web
searches, number of requests and tool calls, key id, start and end time, the error (scrubbed), and the path of its
history file.

A **history** file holds one JSON object a line, in order: `start` (agent, model, effort, key id, the full system
prompt and its sha256, the tool definitions, the full dossier and its sha256, the code version, the request
settings), then for every API call a `request` (the messages added since the previous request) and a `response`
(the whole response as returned, with usage and cost), a `tool` event per tool call (input, result — cut at 20,000
characters — whether it failed, seconds), `error` events (class, status, request id, the scrubbed message, what the
runner did), the citation checker's own `start` / `request` / `response` events, and `end` (status and totals). The
dossier is stored once, in `start`; the first request refers to it as `{{dossier}}`.

To read one:

```bash
H=~/Tahoe-100M/tahoemap/review/history/gene/NQO1/20261106-211743-42278a.jsonl
jq -c '{event, agent, name, cost_usd}' "$H"                  # the outline
jq -r 'select(.event=="tool") | "\(.name) \(.input|tostring)"' "$H"   # every tool call
jq -r 'select(.event=="start") | .dossier' "$H" | head -50   # the dossier the agent got
```

or in Python (`python3`, from the repository folder):

```python
from tahoemap.review.history import read_jsonl, conversation
ev = read_jsonl("/path/to/review/history/gene/NQO1/20261106-211743-42278a.jsonl")
for e in ev:
    print(e["event"], e.get("agent"), e.get("name", ""), e.get("cost_usd", ""))
msgs = conversation(ev)                       # the reviewer's messages exactly as last sent
checker = conversation(ev, "citation-checker")
import pandas as pd
led = pd.read_json("/path/to/review/ledger.jsonl", lines=True)   # every attempt
print(led.groupby(["kind", "status"])["cost_usd"].agg(["count", "sum"]))
```

## Verification

`--verify llm` (the default) does both steps, `--verify ids` only the first, `--verify off` neither:

1. **Ids**: every cited PMID is looked up in PubMed, every DOI in Europe PMC and Crossref. A citation that does not
   exist is removed from its item, the item is marked `unverified`, and in the note the link becomes "PMID:n
   (citation removed: not found in PubMed)". Retracted papers stay cited but are listed. A paper cited without
   having been retrieved in the session is flagged (and the agent was asked to read it before submitting).
2. **Claims**: the citation checker gets each claim (established, missing, contradicted, connection verdicts) with
   the abstracts of its citations and gives a verdict per claim: supported, partly, not supported, not checkable.

The review JSON keeps both (`verification.ids`, `verification.llm`, `verification.counts`, and a `check` on each
item); the vault's callout gives the counts. "Supported" means *the abstract says so*, not that the claim is true.

## In the vault and the map

The vault and map stages read `review/` when it holds reviews; without reviews nothing in them changes. After a
review run, `tahoe` (status) shows the vault and map out of date ("the literature reviews changed"); `tahoe run`, or
`tahoe vault` then `tahoe map`, rebuilds them (about two minutes on the full data).

- A reviewed gene, drug or line note gets the tag `#literature-review`, a `literature_review` date in its
  frontmatter, and a section **What the literature says** (in a gene note after "Where it sits"; in a drug or line
  note before "Data"): a callout — written by an AI agent, which agent, model and effort, the date, the verification
  counts, and relative links to the history file and the review JSON (they are in the run folder, outside the
  vault: Obsidian shows the link, open the file in a text editor) — then the agent's text, then its connection
  verdicts. Wikilinks the agent wrote are kept only where the vault has that note.
- A gene note's partner tables get a **Literature** column when a partner shown has a verdict: the verdict of this
  gene's review on that partner, else the partner's review's verdict on this gene (marked with its name), with the
  cited papers linked.
- The map's side panel shows a `lit: established` (etc.) badge next to such a partner; hover it for the citation
  count.

## The duplicate workflow

Reviews take days and money, and you may want the review layer to evolve (new prompts, new models) without touching
the finished run. Keep the run as it is, and review a copy:

```bash
# 1. a finished run, kept as it is (do not run stages in it again; it stays the reference)
tahoe run --out ~/tm/main
# 2. a copy for the review work, with its own clone of the code
tahoe duplicate ~/tm/review1 --out ~/tm/main --repo ~/tahoemap-review
# 3. the review on the copy, with the clone's code and agent files
~/tahoemap-review/tahoe review plan --out ~/tm/review1
~/tahoemap-review/tahoe review run --out ~/tm/review1 --kinds line,drug --max-usd 50
~/tahoemap-review/tahoe vault --out ~/tm/review1
~/tahoemap-review/tahoe map --out ~/tm/review1
```

`tahoe duplicate DEST` copies the output folder (`--out`, or the default one): the large arrays and tables (`atlas`,
`tensor`, `tables`, `embed`, `relations`, `graph`) are **hard-linked** when DEST is on the same file system — they
take no extra space, and because every stage writes a new file and swaps it in, a stage that runs again in either
copy replaces its file there without touching the other — and everything else (vault, map, validation, reference)
is copied (on the full data mostly the vault, ~0.6 GB, and the build's CSV tables). It writes `DEST/duplicated_from.json`: the source, the date, the code commit
(and whether the code had uncommitted changes), and the stage stamps. `--repo DIR` also `git clone`s this code
repository into DIR, so the copy's code (and its agent and skill files) can change on their own; edit and commit
there. Call the clone's `tahoe` by its path (do not run `tahoe setup` in the clone, which would point the `tahoe`
command at it); both use the same Python environment.

## Windows and macOS

- **macOS**: `tahoe review` works as on Linux. A long foreground run on a laptop: keep it awake with
  `caffeinate -i tahoe review run ...` (the pipeline keeps itself awake; the review does not). `--background` jobs
  get their own process group, so `tahoe stop` reaches them.
- **Windows** (no `tahoe` wrapper; PowerShell, from the repository folder, with the venv's Python):
  ```powershell
  $env:ANTHROPIC_API_KEY = "sk-ant-..."      # for this window only; or --keys-file C:\Users\me\keys.txt
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review plan --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review run --out C:\tahoe\out --limit 20
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review status --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap vault --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap map --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap duplicate D:\tm\review1 --out C:\tahoe\out --repo C:\tahoe\review-repo
  ```
  The run works in that window (keep it open; it asks there for a new key when all have run out); Ctrl-C pauses it
  and the same command resumes it. There is no background mode. The keys-file permission check is POSIX only: keep
  the file in your own profile folder. Hard links need the copy on the same NTFS volume (else the files are copied).
