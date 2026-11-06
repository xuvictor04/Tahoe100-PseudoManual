"""definitions - the agent and skill files of the review agents.

    load_agent(name) -> AgentDef      agents/<name>.md: YAML frontmatter + body (the system prompt)
    load_skill(name) -> str           skills/<name>/SKILL.md: the body (frontmatter removed)
    list_agents(), list_skills()      the names available

The files use Claude Code's markdown format, so they also work when copied into `.claude/agents/` and
`.claude/skills/`. Agent frontmatter:

    name         the agent's name (= file name without .md)
    description  one paragraph: what the agent does
    model        default model (claude-opus-5-5 when absent); the runner's --model overrides it
    effort       output_config effort: low | medium | high | xhigh | max (high when absent)
    tools        list of tool names: custom tools of tools.py (pubmed_search, pubmed_abstracts, europepmc_search,
                 tahoe_lookup, submit_review), verify.CHECK_TOOL's submit_check, and the server tools web_search /
                 web_fetch. A YAML list ([a, b] or one '- a' per line) or a comma-separated string (Claude Code style)
    skills       list of skill names; their bodies are appended to the system prompt in this order
    max_turns    the most model requests of one attempt (40 when absent)
    max_usd      the default per-entity cost cap in USD (3.00 when absent); the runner's --per-entity-usd overrides it

`AgentDef.system` = the agent body, then each skill wrapped as <skill name="..."> ... </skill>, in the order of
`skills`. The text depends only on the files, so it is identical between runs and cacheable (prompt caching).

The frontmatter parser here is a small YAML subset (no dependency): `key: value` scalars (quoted or not, numbers,
true/false), inline lists `[a, b]`, block lists (`key:` then `- item` lines), folded / literal blocks (`key: >` or
`key: |` then indented lines). Anything else raises ValueError with the file and line.
"""

import hashlib
import os
import re
from dataclasses import dataclass, field

from . import AGENTS_DIR, SKILLS_DIR

DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_EFFORT = "high"
DEFAULT_MAX_TURNS = 40
DEFAULT_MAX_USD = 3.00
EFFORTS = ("low", "medium", "high", "xhigh", "max")
SERVER_TOOLS = ("web_search", "web_fetch")
# custom tools this package executes (tools.py + verify.CHECK_TOOL); kept here so loading an agent needs no imports
CUSTOM_TOOLS = ("pubmed_search", "pubmed_abstracts", "europepmc_search", "tahoe_lookup", "submit_review",
                "submit_check")
SUBMIT_TOOLS = ("submit_review", "submit_check")


@dataclass
class AgentDef:
    """One agent: its frontmatter fields and `system` = body + the bodies of its skills."""
    name: str
    description: str
    model: str
    effort: str
    tools: list
    skills: list
    max_turns: int
    max_usd: float
    system: str
    path: str = ""
    extra: dict = field(default_factory=dict)        # frontmatter keys this module does not use

    @property
    def system_sha256(self):
        return hashlib.sha256(self.system.encode("utf-8")).hexdigest()

    @property
    def custom_tools(self):
        """The tools of this agent that we execute locally (stable order of the frontmatter)."""
        return [t for t in self.tools if t not in SERVER_TOOLS]

    @property
    def server_tools(self):
        return [t for t in self.tools if t in SERVER_TOOLS]

    @property
    def submit_tool(self):
        """The tool whose valid call ends the agent's loop (submit_review or submit_check), or None."""
        for t in self.tools:
            if t in SUBMIT_TOOLS:
                return t
        return None


# ----------------------------------------------------------------------------- frontmatter
def _scalar(v):
    v = v.strip()
    if not v:
        return ""
    if (v[0] == v[-1]) and v[0] in "\"'" and len(v) >= 2:
        s = v[1:-1]
        return s.replace('\\"', '"') if v[0] == '"' else s.replace("''", "'")
    low = v.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if low in ("null", "~"):
        return None
    if re.fullmatch(r"[-+]?\d+", v):
        return int(v)
    if re.fullmatch(r"[-+]?(\d+\.\d*|\.\d+|\d+)([eE][-+]?\d+)?", v):
        return float(v)
    return v


def _inline_list(v):
    inner = v.strip()[1:-1].strip()
    if not inner:
        return []
    out, cur, q = [], "", None
    for ch in inner:                              # split on commas outside quotes
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            cur += ch
        elif ch == ",":
            out.append(_scalar(cur))
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(_scalar(cur))
    return out


def parse_frontmatter(text, path="<text>"):
    """(frontmatter dict, body) of a markdown file that starts with a '---' block; ({}, text) without one."""
    t = text.lstrip("\ufeff").replace("\r\n", "\n")
    if not t.startswith("---"):
        return {}, text
    lines = t.split("\n")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError(f"{path}: frontmatter starts with '---' but has no closing '---'")
    fm, i = {}, 1
    while i < end:
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", raw)
        if not m or raw[0].isspace():
            raise ValueError(f"{path}:{i + 1}: cannot read frontmatter line {raw!r}")
        key, val = m.group(1), m.group(2).rstrip()
        i += 1
        if val in (">", "|", ">-", "|-"):
            block = []
            while i < end and (not lines[i].strip() or lines[i][0].isspace()):
                block.append(lines[i].strip())
                i += 1
            fm[key] = (" ".join(b for b in block if b) if val.startswith(">") else "\n".join(block)).strip()
        elif val == "":
            items = []
            while i < end and re.match(r"^\s+-\s*", lines[i]):
                items.append(_scalar(re.sub(r"^\s+-\s*", "", lines[i])))
                i += 1
            fm[key] = items if items else ""
        elif val.startswith("[") and val.endswith("]"):
            fm[key] = _inline_list(val)
        else:
            fm[key] = _scalar(val)
    body = "\n".join(lines[end + 1:])
    return fm, body.strip("\n") + "\n"


def _as_list(v):
    if v is None or v == "":
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in str(v).split(",") if x.strip()]


# ----------------------------------------------------------------------------- loading
def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def list_agents(agents_dir=None):
    d = agents_dir or AGENTS_DIR
    return sorted(f[:-3] for f in os.listdir(d) if f.endswith(".md")) if os.path.isdir(d) else []


def list_skills(skills_dir=None):
    d = skills_dir or SKILLS_DIR
    if not os.path.isdir(d):
        return []
    return sorted(n for n in os.listdir(d) if os.path.exists(os.path.join(d, n, "SKILL.md")))


def skill_path(name, skills_dir=None):
    return os.path.join(skills_dir or SKILLS_DIR, name, "SKILL.md")


def load_skill_def(name, skills_dir=None):
    """(frontmatter, body) of skills/<name>/SKILL.md."""
    p = skill_path(name, skills_dir)
    if not os.path.exists(p):
        raise FileNotFoundError(f"No skill '{name}' ({p}); skills: {', '.join(list_skills(skills_dir)) or 'none'}")
    fm, body = parse_frontmatter(_read(p), p)
    if fm.get("name") and fm["name"] != name:
        raise ValueError(f"{p}: frontmatter name '{fm['name']}' differs from its folder '{name}'")
    return fm, body


def load_skill(name, skills_dir=None):
    """The body of skills/<name>/SKILL.md (instructions, frontmatter removed)."""
    return load_skill_def(name, skills_dir)[1]


def compose_system(body, skills, skills_dir=None):
    """The system prompt: the agent body, then each skill as <skill name="..."> ... </skill> in the given order."""
    parts = [body.rstrip()]
    if skills:
        parts.append("# Skills\n\nThe skills below are part of these instructions; follow them.")
    for s in skills:
        fm, sb = load_skill_def(s, skills_dir)
        desc = str(fm.get("description", "")).strip()
        head = f'<skill name="{s}">' + (f"\n<!-- {desc} -->" if desc else "")
        parts.append(f"{head}\n{sb.strip()}\n</skill>")
    return "\n\n".join(parts) + "\n"


def load_agent(name, agents_dir=None, skills_dir=None):
    """agents/<name>.md -> AgentDef (system = body + its skills' bodies). `name` may also be a path to a .md file."""
    p = name if name.endswith(".md") and os.path.exists(name) else os.path.join(agents_dir or AGENTS_DIR,
                                                                              name + ".md")
    if not os.path.exists(p):
        raise FileNotFoundError(f"No agent '{name}' ({p}); agents: {', '.join(list_agents(agents_dir)) or 'none'}")
    fm, body = parse_frontmatter(_read(p), p)
    nm = str(fm.get("name") or os.path.basename(p)[:-3])
    tools = _as_list(fm.get("tools"))
    unknown = [t for t in tools if t not in CUSTOM_TOOLS + SERVER_TOOLS]
    if unknown:
        raise ValueError(f"{p}: unknown tools {unknown}; known: {', '.join(CUSTOM_TOOLS + SERVER_TOOLS)}")
    skills = _as_list(fm.get("skills"))
    effort = str(fm.get("effort") or DEFAULT_EFFORT).strip().lower()
    if effort not in EFFORTS:
        raise ValueError(f"{p}: effort '{effort}' is not one of {', '.join(EFFORTS)}")
    try:
        max_turns = int(fm.get("max_turns") or DEFAULT_MAX_TURNS)
        max_usd = float(fm.get("max_usd") or DEFAULT_MAX_USD)
    except (TypeError, ValueError):
        raise ValueError(f"{p}: max_turns must be an integer and max_usd a number") from None
    if max_turns < 1 or max_usd <= 0:
        raise ValueError(f"{p}: max_turns must be >= 1 and max_usd > 0")
    known = {"name", "description", "model", "effort", "tools", "skills", "max_turns", "max_usd"}
    return AgentDef(name=nm, description=str(fm.get("description") or "").strip(),
                    model=str(fm.get("model") or DEFAULT_MODEL).strip(), effort=effort, tools=tools, skills=skills,
                    max_turns=max_turns, max_usd=max_usd, system=compose_system(body, skills, skills_dir), path=p,
                    extra={k: v for k, v in fm.items() if k not in known})
