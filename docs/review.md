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
*not* among its data partners, and its novel candidate pairs. Nothing is left out of a dossier for a flag: a drug-dose
with an artifact flag for the gene (the tables stage's flags of record, which include `like a neighbouring well`), a
single-line cell at such a drug-dose, or a partner without the same sign in both halves of the compounds (or a
lineage pair, or read-sharing copies) keeps its ranked place, marked ⚠ with the reason in plain words (for a
cell-cycle shift: how much of this gene's change it would explain), and each list says how many items carry an
alert; a list capped at N shows the N strongest plus any of the N strongest without an alert that would fall below
them. The words of the neighbouring-well and translation-inhibitor flags stand under the list that shows them; the
`lines moved / measured` count names the drug-dose's wells (`· one well`: the lines are not replicate treatments).
For a drug: Tahoe's annotation (targets, mechanism) and ChEMBL's (with the release, the matched molecule, its
mechanisms and targets) side by side, ⚠ where they disagree, the drug's mechanism classes with their sources, the
dose table with each dose's plate and well and its neighbouring-well reading, the genes each dose moves (the full
lists at the best trustworthy dose - an active dose without an artifact flag - and, marked as flagged, at the drug's
vector dose when that one carries a flag; when no dose is trustworthy the dossier says so and lists the flags), the
lines it depletes, the nearest drugs; for a cell line: organ, drivers, TP53 (`not recorded` = no TP53 alteration in
the metadata: presumed wild type, not confirmed), its Cellosaurus links (written out, because web fetch opens only
URLs that appear in the conversation), the genes specifically high or low, the drugs that deplete it.
`tahoe review run --dry-run` writes the dossiers so you can read them.

A gene's dossier also has its **probable direction** (from the direction stage, [direction.md](direction.md)): the
arrows that point to it, those that go from it, and those to the cells under a drug, each with its grade, what the
source's activity does to the target, the evidence, q and its alerts, in the same order as in the vault (a long list
is capped by the same rule, and says how many more arrows there are). The reviewer can then say whether the
literature knows the arrow, and in which direction. The arrows are probable (from cell lines, not proof of direct
regulation), and the dossier says so.

The agent then:

- searches PubMed and Europe PMC (our own tools, run on your machine; cached in `review/cache/`), and the web
  (Anthropic's server-side web search and web fetch; `--no-web` turns them off);
- looks up other genes, drugs and lines of the run (`tahoe_lookup`) to check a partner;
- reads the abstracts of the papers it wants to cite;
- submits a structured **review**: a summary; what is **established** (with citations); what in the data is
  **unexpected**; which expected connections are **missing** (and the likely reason); what is **contradicted**; a
  **verdict for each connection** it judged (established, indirect, plausible, unexpected, contradicted), with the
  relation the papers report and the direction and numbers in the data; open questions; and the text of the vault
  section (it writes no line about verification: a line generated after the checks says what was checked).

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

'default' is the model `DEFAULT_MODEL` of `tahoemap/review/definitions.py` (an agent file's `model:` line or `--model`
overrides it).

| Agent (`tahoemap/review/agents/`) | Reviews | Model, effort | Per-entity cap |
|---|---|---|---|
| `gene-reviewer.md` | one gene: drug responses, partners, missing / contradicted connections | default, high | $3.00 |
| `drug-reviewer.md` | one drug: mechanism vs response, genes, modules, depleted lines, similar drugs | default, high | $3.00 |
| `line-reviewer.md` | one cell line: identity, drivers, specific genes, drugs that deplete it | default, high | $3.00 |
| `citation-checker.md` | the claims of a submitted review against their abstracts | default, medium | $0.50 |

| Skill (`tahoemap/review/skills/<name>/SKILL.md`) | What it teaches |
|---|---|
| `reading-tahoe-data` | what every number of a dossier means and how far it can be trusted |
| `connection-audit` | the verdict rubric and how to fill the review's sections |
| `literature-search` | searching PubMed / Europe PMC well (symbols, aliases, MeSH, drug salts), when to stop |
| `citations` | which papers may be cited for what, PMID / DOI formats, retractions |
| `writing-the-note` | the vault section: structure, length, tone, links |

The files are in the usual **agent-file markdown format**: YAML frontmatter, then the text. An agent's frontmatter has
`name`, `description`, `model`, `effort`, `tools`, `skills`, `max_turns` (requests per attempt) and `max_usd` (the
per-entity cap); its body is the system prompt, and the runner appends the bodies of its skills, always in the same
order (so the prompt is cached between requests and entities). To change what the agents do, edit these files: the
next run uses them (the history of each review records the sha256 of the exact system prompt it got). Keep the
changes in git (or in the clone of the [duplicate workflow](#the-duplicate-workflow)) so you know which prompt wrote
which review. `--model` and `--effort` override the files for one run, for all reviewers (`--model MODEL`) or per
agent (`--model gene=MODEL,checker=MODEL`, with the model identifiers of `PRICES` in `tahoemap/review/runner.py`;
agents: gene, drug, line, checker, reviewers, all).

**Using them interactively in a coding assistant** that reads agent and skill files in this format: copy
`tahoemap/review/agents/*.md` into the project's agents folder of that assistant and the `tahoemap/review/skills/*`
folders into its skills folder. Such an assistant does not have tahoemap's own tools (`pubmed_search`,
`pubmed_abstracts`, `europepmc_search`, `tahoe_lookup`, `submit_review`), so in the copies replace the `tools:` line
with the assistant's own (for example `tools: Read, Grep, Bash, WebSearch, WebFetch`) or delete it, and delete any
field it does not accept (`effort`, `max_turns`, `max_usd` are for tahoemap's runner). Give the agent a dossier — `tahoe review run --dry-run --only NQO1 --limit 1` writes
`review/dry_run/gene/NQO1.dossier.md` — and the look-ups (`tahoe gene NQO1`, `tahoe pair NQO1 HMOX1`). A review
written that way is not verified and not spliced into the vault; only `tahoe review run` does both.

## Costs

**Prices** the runner counts with: `PRICES` in `tahoemap/review/runner.py`, per model, in USD per million tokens
(input, output, cache write for 5 minutes at 1.25x the input price, cache read); the default model costs 4.00 per
million input and 20.00 per million output tokens. Check the provider's current price list before a large run.

Web searches cost $0.01 each. The cost of every response is computed from its `usage` (each `usage.iterations`
entry at its own model, so a response finished by a fallback model is counted at that model's price) and stored in
the history and the ledger. Every request is **streamed** (so a long answer is never cut by an HTTP timeout), with
room for 64,000 output tokens (thinking included) at effort low to high and 128,000 at `xhigh` / `max`. A response
**lost on the way** — a timeout, a dropped connection, a stream that breaks off — may still have been billed, so it is
charged a conservative **estimate** (the whole context at the full input price, plus the output of a long answer:
twice the attempt's longest answer so far, at least 16,000 tokens; about $0.5 with the default agents, twice that
when the SDK had re-sent it) to the attempt and to the run's total, so the caps stay safe; it is marked as estimated
(`estimated_usd` in the ledger, `estimated_cost_usd` on the history's error event, and in `tahoe review status`). A
request that never reached the API (the connection could not be made, or the request could not even be written on
this machine — a malformed key, say) is not charged. An attempt that reaches its cap only through these estimates is
recorded as `failed` (a network problem: a later run retries it), not `over_budget`. A request still **in flight
when a stopping run closes its attempt** (after the 15-second grace, or at a second Ctrl-C) may be billed too: it
gets the same estimate, on the attempt's ledger line and on a history error event (`InFlightAtStop`). If its answer
still arrives before the program ends, that answer's real cost replaces the estimate (its `note` line carries the
difference, which can be negative, and minus the estimate as `estimated_usd`, so the totals hold the real cost); if
it is lost then, a `note` line adds whatever that loss is charged beyond the estimate already counted.

**Per-entity estimate**: before any review of a kind exists, the runner estimates from the size of the agent's
system prompt and tool definitions and of a few dossiers: ~14 requests whose context grows by ~2,500 tokens each
(read from the cache), the output per request at the agent's effort (low 800 ... high 2,500 ... max 6,000 tokens), 3
web searches and the citation check. Once 3 entities of a kind are reviewed with the reviewer model, effort and
`--verify` mode the plan or run asks for now, the mean of their **real** cost (every attempt but `--recheck` ones)
replaces the estimate; reviews made with other settings are not counted (the projection says how many there are).
`tahoe review plan` prints the projection per kind and in total; `tahoe review status` projects the rest. On the
synthetic test data the estimate is ~$1.17 per gene and ~$1.16 per drug or line (the default model, effort high,
`--verify llm`); a model at half the price (`--model MODEL`) with `--verify ids` roughly halves it.

**How many**: the queue holds every gene with a response or a place in the vector space — about **15,000 genes** on
the full data — plus ~379 drugs and 50 lines. At ~$1.2 an entity, **a full gene pass costs on the order of $18,000**;
the drugs and lines together ~$500. So start small and project from real costs:

1. `tahoe review plan` (free): the queue and the projection.
2. `tahoe review run --dry-run --limit 5` (free): read a few dossiers and the exact first requests.
3. `tahoe review run --limit 20` (or `--only NQO1,HMOX1,TP53` / `--only @genes.txt`): ~$25; then
   `tahoe review status` shows the real cost per entity, and the projection of the rest uses it.
4. Then by priority: the queue puts the 50 lines first, then the drugs, then the genes in order of interest (novel
   candidate pairs, strong partners with the same sign in both halves of the compounds, modules labelled by a strong
   gene set or by the drug class that drives them, many clean drug responses). `--kinds line,drug`,
   then `--kinds gene --limit 500 --max-usd 600`, and so on: each run continues where the last stopped.

**Caps**: `--per-entity-usd Y` (default: the agent file's `max_usd`, $3.00): an attempt that has spent it stops
(status `over_budget`; its partial history is kept); the citation checker has its own cap ($0.50). The agent knows
where it stands: every message the runner sends it after the dossier ends with a line such as *[runner] Budget:
$1.20 of $3.00 used; 7 of 40 requests made.*, and past 75% of the cap (or 3 requests before its `max_turns`) the
line asks it to stop searching and submit, on the last request it can make firmly — so a review is stored rather
than cut off. `--max-usd X`: no new entity starts once the run has spent X, and the running ones pause (a review
already submitted is still stored). The runner **refuses to start** without
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
   Make it readable only by you (`chmod 600 FILE`); the runner warns when other users can read it. A key given
   to `--keys-file` (or to `--fake`) by mistake, instead of a file's path, is refused without being printed or
   logged — clear it from your shell history.
2. `ANTHROPIC_API_KEYS` (comma-separated), then `ANTHROPIC_API_KEY`.
3. With none of these, the SDK's own credentials (`ANTHROPIC_AUTH_TOKEN`, or a profile of the `ant` CLI) if found.

Prefer the file or the environment over typing a key on a command line (shell history, process lists);
`read -rs ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY` sets it without echoing it or keeping it in the
history. A malformed key — one with a line break, a space or another character a key cannot hold, say two keys in
`ANTHROPIC_API_KEY` from `export ANTHROPIC_API_KEY="$(cat keys.txt)"` — is never sent: it counts as dead from the
start (`tahoe review status` lists it with the reason), so the run uses the next key or pauses for one.

**Keys are never written anywhere**: they live in the runner's memory only. Histories, the ledger, logs and
`review/keys_state.json` name a key by its **id** — its last 4 characters and a short hash, e.g. `KEY1-f2e60909` —
and every error message is scrubbed of anything that looks like a key before it is stored or printed.

**Rotation and running out of credit**: an error that means the key itself no longer works — 401 (invalid), 403
(no permission), 402 / `billing_error` (credit used up), a spend limit reached, an organisation on hold — marks the
key **dead** (`tahoe review status` lists dead key ids), and the entity in progress **restarts from the beginning
with the next key** (the cut-off attempt is recorded as `key_rotated`, with its history and cost). Rate limits,
overload (429, 529) and server errors do not rotate: the SDK retries once, then the runner waits with exponential
back-off (up to 10 minutes, Retry-After honoured) and retries the same request, up to 12 times. Timeouts and
dropped connections get a small budget of their own: the request is sent again at most twice (after the SDK's own
retry), then the entity fails; each lost response is charged an estimate ([Costs](#costs)).

A refusal is final (`refused`) — except when the API says the fallback model was not tried because it was
rate-limited or overloaded (`stop_details.recommended_model` is set): that is temporary, so the attempt is recorded
as `failed` (with `transient_refusal`, the category and `recommended_model` in the ledger, and a log line naming the
model) and the entity is retried by a later run.

**The same error on every entity** does not sweep the whole queue: when **5 entities in a row** fail with the same
error, the run stops with exit code **4** and says which error. Those failures are not counted against the entities
(a ledger `note` line each); fix the cause and run the same command again. Which errors count:

- the **network** — timeouts, connections dropped or refused, streams cut short (all one error here, since a
  failing network alternates between them) — and rate limits, overload or server errors that outlast the 12
  back-offs: these are never one entity's own, so 5 in a row stop the run **at any point**, also after reviews of the
  run have succeeded;
- any other error — say the model is not available to your organisation (404), a beta not enabled for it (400), a
  request too large (413) — only **before the API has answered a request of the run**. Once a response has come
  back, the API, the key, the model and the network work, so such failures are the entities' own: counted, and the
  run goes on. If an error of this kind that stopped a run was the entities' own after all (say a request too large
  for each of 5 neighbours in the queue), run the same command again as it is: an entity that already stopped a run
  with that error no longer counts toward a stop, so the next run goes on past them, and their failures count from
  then on (left alone after 3 like any other).

When the fifth failure comes while other entities are still being reviewed, the run first waits for them (no new
entity starts): if one of them gets an answer from the API, the run goes on (and counts the failures); if none is
left running without one, it stops. So a stop never throws away the work of a review that was going well.

When **every** key is dead:

- in the foreground (a terminal; on Windows stdin, stdout and stderr must all be the console window, so a run
  started with `Start-Process` and its output redirected to files does not ask), the run asks: *Paste a new Anthropic
  API key (it is not saved anywhere), or press Enter to stop*. A pasted key is used at once (and only for this run). Ctrl-C at that prompt works like Enter: the
  prompt ends at once, the terminal is left as it was (echo on), and the run pauses as below (exit code 3);
- in the background, with `--no-prompt`, or when you press Enter, the run **pauses**: the entities not finished stay pending, the exit
  code is 3, and the message says to add a key. Add credit or a key (`ANTHROPIC_API_KEY`, `ANTHROPIC_API_KEYS`, the
  keys file) and run **the same command again**: it continues with the entities still pending.

## Running, stopping, resuming

`tahoe review run` runs **in the foreground** by default, so that it can ask for a new key: keep the terminal open
(or use `screen` / `tmux`). Ctrl-C stops it cleanly: no new entity starts, the ones in progress get 15 seconds and are
then marked `paused` — except one whose review was already submitted (it was being verified): that review is
**stored as done**, with its verification as far as it got and the rest marked not run (`review run --recheck`
completes it) — and the ledger and the tables are written (a second Ctrl-C stops at once). Closing the terminal
(SIGHUP), `tahoe stop` (SIGTERM) and `tahoe review stop` stop it the same way (exit codes 129, 143, 143; Ctrl-C 130;
Ctrl-Break on Windows 149): `tahoe stop` (with the same `--out`) finds a run in the foreground of another terminal
through `review/.run.lock`; `tahoe review stop` (`python -m tahoemap review stop --out ...`, on every system) asks
the run named there to stop through a file, `review/.stop`, and waits until it has ended. A request still in
flight when its attempt is closed is charged an estimate ([Costs](#costs)); a response that arrives after its attempt
was closed is still counted: a `note` line in the ledger and a `late` event in the history.

`tahoe review run --background ...` runs it as a job like `tahoe run` (safe to log out): `tahoe` shows that it runs
and its last lines, `tahoe log` follows it, `tahoe stop` stops it as Ctrl-C does. A job cannot ask for a key, so it
needs `--keys-file` or `ANTHROPIC_API_KEY(S)`, and it pauses (exit code 3) when they are all used up. One review run
at a time per output folder (`review/.run.lock`, which holds the run's process id, computer and start time); a lock
whose process is gone — also on Windows, after a closed window or a reboot — is removed by the next run, and
`tahoe review status` says whether the lock is live or stale. `tahoe review run` refuses while a pipeline command
computes on the folder (a `tahoe` job, or any `run` or stage command: it holds `OUT/.pipeline.lock`).

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
| `--retry-failed` | also retry the entities left alone after 3 failed attempts (not the done ones) |
| `--recheck` | only complete the verification of stored reviews that lack it (see below); no reviewer runs |
| `--dry-run` | write the dossiers and first requests to `review/dry_run/`; send nothing |
| `--no-prompt` | never ask for a key when every key is used up: pause (exit code 3) instead (a run nobody watches) |

**Resuming** needs nothing special: the latest ledger line of each entity is its state, and a run starts only what
is not final. `done` and `refused` (the model declined; `stop_details.category` is recorded) are final unless
`--redo`; `failed` and `no_review` (it never submitted) are retried, up to 3 attempts (then left alone:
`--retry-failed` tries them again); `over_budget` is retried only with a higher `--per-entity-usd`; `paused` and
`key_rotated` start again from the beginning.

**Completing a verification**: a review stored while its verification could not finish — the run stopped during
the citation check, every key ran out there, PubMed / Crossref could not be reached, or it ran with `--verify ids`
and you now want the claims checked — is `done`, and `tahoe review status` counts it. `tahoe review run --recheck
--max-usd 5` (with `--verify llm`, the default, or `--verify ids`) runs only what it lacks — the id look-ups and / or
the citation checker — on the stored review, rewrites its JSON and note, and adds a `done` ledger line (`recheck`)
with the checker's cost (projected ~$0.10 each with the default checker); the reviewer is not run again. A
`--recheck` that is itself stopped (Ctrl-C, SIGTERM, SIGHUP, the `--max-usd` cap, no key left) before its citation
check has finished — whether the check was cut off or never started — leaves the stored review and note as they
were (no `done` line), with a ledger `note` line (`recheck: paused`) for its cost: the review still counts as lacking
its verification, and the next `--recheck` completes it.

## Histories and the ledger

Everything is under `<output>/review/`:

| Path | What |
|---|---|
| `queue.parquet` | the entities the last `tahoe review plan` selected (all, or its `--kinds` / `--only`), in priority order with their state; `tahoe review status` always counts every entity, whatever the last plan selected |
| `ledger.jsonl` | one line per finished attempt (append-only) |
| `ledger.unwritten.jsonl` | only when `ledger.jsonl` could not be written for a whole run (on Windows: open in Excel): the lines that waited; read as part of the ledger, and moved into it by the next run |
| `history/<kind>/<name>/<run_id>.jsonl` | every event of one attempt |
| `reviews/<kind>/<name>.json` | the submitted review + its verification + metadata (model, date, cost, history path ...) |
| `notes/<kind>/<name>.md` | the vault section the agent wrote |
| `connections.parquet`, `findings.parquet` | every connection verdict / every finding of every review, one row each, with its check (`check_status`, `shown_verdict`), its citations and the retracted papers among them (`citations`, `retracted`: `PMID:1;DOI:x`) (rebuilt at the end of each run and by `tahoe review tables`) |
| `dry_run/`, `cache/`, `keys_state.json`, `review.log` | dry-run files, the literature cache, key ids and which are dead, the log |

A **ledger** line: entity_id, kind, name, run_id, agent, model, status (`done`, `refused`, `no_review`,
`over_budget`, `failed`, `paused`, `key_rotated`), cost_usd (with `estimated_usd`, the part estimated for lost
responses), input / output / cache-write / cache-read tokens, web searches, number of requests and tool calls, key
id, start and end time, the error (scrubbed), the path of its history file, and the reviewer's `effort` and the
`--verify` mode (what its cost depends on, for the projection); a done line also has the verification's state
(`ids_status`, `llm_status`). Lines with status `note` are bookkeeping, not attempts: the cost of a response that
arrived after its attempt was closed (`late`; when an estimate was charged for it at the close, the difference,
with `replaces_estimate_usd`), an estimate for a response lost after its attempt was closed (`late`,
`estimated_usd`), a failure the run put down to a systematic error (`uncount_failed`, with the error's
`signature`), or a `--recheck` stopped before it finished (`recheck`); they never change an entity's state. A line
cut short by a crash or a full disk is skipped, and the next line is still read.

A **history** file holds one JSON object a line, in order: `start` (agent, model, effort, key id, the full system
prompt and its sha256, the tool definitions, the full dossier and its sha256, the code version, the request
settings), then for every API call a `request` (the messages added since the previous request) and a `response`
(the whole response as returned, with usage and cost), a `tool` event per tool call (input, result — cut at 20,000
characters — whether it failed, seconds), `error` events (class, status, request id, the scrubbed message, what the
runner did; for a lost response the estimate charged for it), the citation checker's own `start` / `request` /
`response` events, and `end` (status and totals; after it only `late` events). The
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

1. **Ids**: every cited PMID is looked up in PubMed, every DOI in Europe PMC and Crossref (DOIs are read whole,
   parentheses included: `10.1016/S0092-8674(00)81096-3`). A citation that does not exist is removed from its item,
   the item is marked `unverified`, and in the note the link becomes "PMID:n (citation removed: not found in
   PubMed)". The note may cite only papers that an item of the review cites (only those are checked against a
   claim): any other PMID or DOI in it becomes "PMID:n (citation removed: cited only in this text ...)" and is
   counted (the agent is warned once at submission). Every common way a note can name a paper is read: PubMed, NCBI
   (`ncbi.nlm.nih.gov/pubmed/...`, also the search form `ncbi.nlm.nih.gov/pubmed?term=123`) and Europe PMC
   (`europepmc.org/article/MED/...`) links, bare URLs, "PMID 123", "PMIDs 1, 2 and 3" and "PMIDs 1, 2, and 3",
   "PubMed ID 123", doi.org links (`10.x%2Fy` included), "DOI:10.x/y" and "DOI 10.x/y" (as the search tools print
   DOIs), and a DOI inside a publisher's or preprint URL (in its path or an `id=` parameter:
   `biorxiv.org/content/10.1101/...v1`, `journals.plos.org/...?id=10.1371/...`; a bioRxiv version and a trailing
   `/full` or `.pdf` are dropped). A link or bare URL to a removed paper goes whole, whatever its form: link text
   over several lines, a title in "...", '...' or (...), an image; a reference-style link (`[text][1]`, `[1][]`,
   `[1]` with `[1]: url` elsewhere) is replaced by the marker and its definition deleted. PMC ids (PMC links,
   "PMCID PMC123") and Europe PMC links to other records (a preprint's PPR id ...) are always removed, since the
   review cites papers by PMID or DOI only. A paper cited under both its ids is one paper: when an item cites its
   PMID and the note links its DOI (or the reverse), and PubMed's or Europe PMC's record of it gives both, the note
   keeps the link and the paper is counted once.
   A percent-encoded DOI stays as written when its escapes do not decode to a DOI (a quote, a space, a tag, a `%`),
   and an id is written so that it forms no tag and no Obsidian comment (`%%`), so the check never writes markup
   into the note. **Retractions**: a PMID whose PubMed type is *Retracted Publication*, or a DOI that Europe PMC
   types so or whose Crossref record carries a retraction (Crossref's update notices, which include the Retraction
   Watch data), stays cited but is marked on its item (`retracted_citations`), marked "(retracted paper)" where the
   note cites it (after the link's closing parenthesis, or after each reference-style link to it; never inside a
   link destination, where it would be read as a hidden title, nor in a definition, which shows nothing), and
   counted among the papers an item cites (a retracted paper cited only in the note is removed like any other, and
   not counted); a retraction *notice* is not itself counted as retracted (items list notices in
   `retraction_notices`). Ids that could not be looked up (a service down) are kept and marked
   (`unchecked_citations`). A paper cited without having been retrieved in the session is flagged (and the agent was
   asked to read it before submitting).
2. **Claims**: the citation checker gets each claim (established, missing, contradicted, connection verdicts) with
   the abstracts of its citations, the relation in this run's data the claim is about (each connection verdict
   carries `relation`, what the papers report, and `data_evidence`, the direction and numbers in the data), and for
   a connection verdict the rubric's strict meaning ("established" needs a paper on the relation itself: the same
   pathway or complex alone is not enough; "indirect" needs a paper per gene, which `submit_review` already
   enforces). It gives a verdict per claim - supported, partly, not supported, not checkable - and the direction
   the papers report compared with the data; papers that report the opposite direction do not support an
   "established" (a "supported" or "partly" given against the direction is stored as not supported).

The review JSON keeps both. Every connection verdict, and every other item that cites (or cited) a paper, carries
`check_status` - `supported`, `partly`, `not_supported`, `not_checkable` (the checker's verdict; also: ids valid but
no claim check), `unchecked` (an id not verified) or `citations_removed` (every citation was not found) - and
`shown_verdict`, the verdict to display: the agent's, or `unverified` when the status is `not_supported` or
`citations_removed`. An item that cites a retracted paper keeps its verdict there and lists the paper in
`retracted_citations`; the vault and the map add a marker and, when the item cites nothing else, show it as
unverified (see below). The top level has `verification` (`ids`: checked, removed, unchecked, retracted ...; `llm`:
status done / not_run / failed and the counts per verdict; `counts`) and `note_footer`, a provenance line generated
from those counts and shown under the note (the agents are told never to write their own; a sentence of the stored
note that only vouches for its own verification, such as "citations were checked against PubMed and their
abstracts" or the old "AI-generated ..." footer ("This review is" or "was AI-generated ..."), is dropped, while a
sentence that says anything more, such as what a search found, is kept whole; what surrounds a dropped sentence
keeps its form: a list item left empty goes with its marker, an item that goes on keeps its marker and a nested
item its indentation, and an emphasis opened or closed in the dropped sentence is closed or opened in the kept
text it covered, so no stray `**` or `_` is left). The counts are of papers: a paper cited under its PMID and its
DOI counts once (`verification.ids.same_paper` maps the other id to the one that stands for it). "Supported" means
*the abstract says so*, not that the claim is true.

## In the vault and the map

The vault and map stages read `review/` when it holds reviews; without reviews nothing in them changes. After a
review run, `tahoe` (status) shows the vault and map out of date ("the literature reviews changed"); `tahoe run`, or
`tahoe vault` then `tahoe map`, rebuilds them (about two minutes on the full data). The verdicts come from
`review/connections.parquet`, rebuilt at the end of every review run; when that table is older than a review JSON
(a run killed before its end), or was written by an older version without its `retracted` column, it is ignored and
the verdicts are read from the JSONs (`tahoe review tables` rebuilds it), and the vault and map show out of date
until they are rebuilt. An entity with two review JSONs (a copy kept by hand, say) is shown from its latest review
only (the later `reviewed` time, then the later run id): its note, its verdicts in the partner tables and its badges
in the map alike, even when the latest review gave no verdict. A change in how reviews are drawn (such as the
retraction marker) also makes the vault and the map out of date, so `tahoe run` redraws them.

- A reviewed gene, drug or line note gets the tag `#literature-review`, a `literature_review` date in its
  frontmatter, and a section **What the literature says** (in a gene note after "Where it sits"; in a drug or line
  note before "Data"): a callout — written by an AI agent, which agent, model and effort, the date, the
  verification, and relative links to the history file and the review JSON (they are in the run folder, outside
  the vault: Obsidian shows the link, open the file in a text editor) — then the agent's text, then its connection
  verdicts, then the provenance line generated from the verification (`note_footer`). The callout's verification
  sentence is built from the review's `verification` counts: how many cited ids were looked up, removed as not
  found, or could not be looked up (a service down: "every cited id looked up" is said only when none was left
  unchecked; the claims citing such an id are marked "ids not checked", unless the citation checker read their
  abstracts and graded them all the same, which the sentence then says, as their labels show the checker's verdict),
  retracted papers, papers cited without having been read (those the id check left cited: a made-up id it removed
  is not counted again), how many connection verdicts and other claims are shown as unverified (by the rule of the
  labels below: not supported, no cited paper found, or every cited paper retracted), and whether the citation
  checker ran (its counts), was not run or failed (`review run --recheck` completes it).
- The agent's text is cleaned before it goes into the note: no raw HTML (script, iframe, img, a, style ... any tag
  is removed), no HTML or Obsidian (`%%`) comment, no image (inline, reference or shortcut `![name]`) or embedded
  note, no link other than markdown links to PubMed, doi.org, Europe PMC, NCBI and Cellosaurus (any other link keeps
  only its text; a reference definition to another site is removed wherever it is, in a blockquote, callout or list
  item too, and so is one whose label starts with `^` but is no footnote's, such as `[^a b]:`; a bare URL to
  another site, a `//host` or an e-mail address is not made a link: a zero-width space goes where an autolinker
  would start one, also when `/` or `@` is written as an escape or an entity), code fences closed and shown as plain
  code (no `dataviewjs`, `mermaid` ..., in a blockquote, callout or list item too), no Dataview inline query (a code
  span or a fenced or indented code block whose text starts with `=` or `$=`, after any space or line break, gets a
  zero-width space before it), no setext heading, its own headings demoted below the note's. What a removal puts
  back together is cleaned too: links and images become text before reference definitions are removed, and `<` is
  escaped again at the end, so `<[img](x) src=x onerror=...>` or `<\url ...>` is text, not a tag. The cleaning
  takes linear time, also on long runs of unclosed `<!--`, `<?` or `<script>`. A sentence in which the agent only
  vouches for its own verification
  ("Citations were checked against PubMed and their abstracts.", its own "AI-generated ..." footer), and the
  disclaimers in its paragraph, are dropped by the rule the runner applies to the notes it stores: the generated
  line replaces them. A sentence that says anything more is kept whole ("Citations were checked, but none links
  PIR to HMOX1 in hypoxia." stays).
  Wikilinks the agent wrote are kept only where the vault has that note. Partner names and citation ids in the
  generated lines and tables are escaped.
- A gene note's partner tables get a **Literature** column when a partner shown has a verdict: the verdict of this
  gene's review on that partner, else the partner's review's verdict on this gene (marked with its name), with the
  cited papers linked. Every verdict is shown with its check, from `shown_verdict` and `check_status`:
  `established (supported)`, `established (partly supported)`, `established (not checked)` (the ids exist; the
  claim was not checked against the abstracts), `established (ids not checked)` (not looked up), and
  **unverified** when the citation checker found the cited abstracts do not support it or none of its papers exists
  (`unverified (agent: established; citations not found)`): such a verdict is never shown as established.
- **Retracted papers.** A verdict that cites a retracted paper says so after its label, `established (supported)
  (cites a retracted paper)`, and the paper is marked "(retracted)" after its link. A retracted paper is no support,
  so a verdict whose only papers are retracted reads `unverified (cites a retracted paper) (agent: established; only
  retracted papers cited)`, never established, whatever the citation check said; one that also cites a paper that
  stands keeps its verdict and its check, with the marker. A review stored before retractions were recorded shows
  no marker: nothing about its papers' retraction is known.
- When a review gives one partner several verdicts, one is shown, in the vault and the map alike: the strongest
  verified one (established, contradicted, indirect, plausible, unexpected, among those supported, partly supported
  or with valid ids, and citing something besides retracted papers; between equal ones, one citing no retracted
  paper), else the agent's first ("of 2 verdicts it gave").
- The map's side panel shows the same label as a badge next to such a partner (`lit: established (supported)`,
  `lit: unverified`, `lit: indirect (not checked) (cites a retracted paper)` ...); hover it for what the agent said,
  what the check found (and which cited paper is retracted) and the citation count.

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
`tensor`, `tables`, `embed`, `relations`, `graph`, `direction`) are **hard-linked** when DEST is on the same file system
— they take no extra space, and because every stage writes a new file and swaps it in, a stage that runs again in either
copy replaces its file there without touching the other (on Windows only while no program has that file open in either
copy: a hard-linked file is one file under two names, and a file in use cannot be replaced there) — and everything else
(vault, map, validation, reference) is copied (on the full data mostly the vault, ~0.6 GB, and the build's CSV tables).
It writes `DEST/duplicated_from.json`: the source, the date, the code commit (and whether the code had uncommitted
changes), and the stage stamps. `--repo DIR` also `git clone`s this code repository into DIR, so the copy's code (and
its agent and skill files) can change on their own; edit and commit there. Call the clone's `tahoe` by its path (do not
run `tahoe setup` in the clone, which would point the `tahoe` command at it); both use the same Python environment.

## Windows and macOS

- **macOS**: `tahoe review` works as on Linux. A long foreground run on a laptop: keep it awake with
  `caffeinate -i tahoe review run ...` (the pipeline keeps itself awake; the review does not). `--background` jobs
  get their own process group, so `tahoe stop` reaches them.
- **Windows** (no `tahoe` wrapper; PowerShell, with the venv's Python, from the folder of the code to run:
  `python -m tahoemap` uses the `tahoemap` folder of the current folder, so for the duplicate workflow
  `Set-Location C:\tahoe\review-repo` first, or the original's code and agent files run, without a message):
  ```powershell
  $env:ANTHROPIC_API_KEY = "sk-ant-..."      # for this window only; or --keys-file C:\Users\me\keys.txt
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review plan --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review run --out C:\tahoe\out --limit 20
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review status --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap review stop --out C:\tahoe\out     # from another window
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap vault --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap map --out C:\tahoe\out
  C:\tahoe\.venv\Scripts\python.exe -m tahoemap duplicate D:\tm\review1 --out C:\tahoe\out --repo C:\tahoe\review-repo
  ```
  - The run works in its window (keep it open; it asks there for a new key when all have run out); Ctrl-C or
    Ctrl-Break pauses it and the same command resumes it. From another window, `review stop` (above) stops it the
    same way and waits for it to end. `Stop-Process`, `taskkill /F` and Task Manager end it at once: the entities in
    progress are neither paused nor stored, and are paid for again next run. Closing its window closes them at once
    (no 15-second grace: a review already submitted is stored, the others are paused). The computer is kept awake
    while it runs (a laptop still sleeps when its lid is closed). There is no background mode.
  - A run started with `Start-Process` (its output redirected to files, or a hidden window) cannot ask for a key:
    give it `--keys-file` (or the key in the environment) and `--no-prompt`; it pauses with exit code 3 when every
    key is used up.
  - git (for `duplicate --repo`, and the commit recorded with every review): put the folder of `git.exe` on PATH
    (for a portable MinGit its `cmd` folder) or set `$env:TAHOE_GIT = "C:\path\to\git.exe"`. Without it,
    `duplicate --repo` says that git was not found, and the reviews record the commit as unknown.
  - The keys file and `--only @FILE` may be UTF-8 (with or without a BOM) or UTF-16 (what Windows PowerShell's `>`
    and `Out-File` write). Quote the `@` in PowerShell: `--only '@genes.txt'` (unquoted it is splatting). The
    keys-file permission check is POSIX only: keep the file in your own profile folder.
  - Hard links need the copy on the same NTFS volume (else the files are copied). A file in use cannot be replaced
    on Windows, and a hard-linked file is the same file in both copies: do not run a stage again in either copy (say
    `embed` or `graph`) while a review or a look-up runs on the other; the stage would stop with "Cannot replace ...
    another program has it open" (nothing is lost; run it again afterwards).
  - A review file that another program holds when the run writes it (a sync or antivirus tool, an editor) is tried
    again for a few seconds; if it still cannot be written, the attempt is recorded as `failed` with the review kept
    in its history (the end event's `unstored_review`), and the entity is reviewed again next run. A `ledger.jsonl`
    open in Excel cannot be appended to: its lines wait (`ledger.unwritten.jsonl`) and are moved in later.
