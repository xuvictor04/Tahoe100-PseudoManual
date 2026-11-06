"""review - literature-review agents for the genes, drugs and cell lines of a finished run.

One agent run per entity reads a dossier of what the run's outputs say about the entity (`dossier.py`), searches the
literature with local tools (`tools.py`: PubMed, Europe PMC, look-ups in the run) and Anthropic's web tools, and
submits a structured review: what is established (with citations), what in the data is unexpected, which expected
connections are missing, what is contradicted. `verify.py` checks every cited id against PubMed / Crossref and has a
citation-checker agent compare each claim with the abstracts it cites.

    agents/<name>.md            agent definitions (Claude Code format: YAML frontmatter + system prompt)
    skills/<name>/SKILL.md      skills; their bodies are appended to the system prompt of the agents that list them
    definitions.py              load_agent(name) -> AgentDef ; load_skill(name) -> str
    dossier.py                  entities(out, kinds) -> DataFrame ; build(out, kind, name) -> Dossier
    tools.py                    custom tool schemas, execute(name, input, ctx), server_tools(web, max_uses)
    verify.py                   check_ids(review, ctx) ; build_check_prompt(review, abstracts) ; CHECK_TOOL
    keys.py, history.py, runner.py, fake.py   key pool, histories and ledger, the agent loop, a fake client

Everything is written under OUT/review/ (see docs/DESIGN-review-and-physics.md, Part 2). Nothing in this package
calls the Anthropic API at import time; the dossiers, tools and verification run without a key.
"""

import os

VERSION = 1                       # bump when the dossier, tool or review formats change

HERE = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.join(HERE, "agents")
SKILLS_DIR = os.path.join(HERE, "skills")

KINDS = ("gene", "drug", "line")


def review_dir(out, *parts):
    """The folder OUT/review/<parts...>, created if missing (join file names to it yourself)."""
    p = os.path.join(out, "review", *parts)
    os.makedirs(p, exist_ok=True)
    return p
