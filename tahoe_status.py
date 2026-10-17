#!/usr/bin/env python3
"""
tahoe_status.py - the status screen and small helpers behind the 'tahoe' command (standard library only).

    python3 tahoe_status.py status --data ~/Tahoe-100M        # what 'tahoe status' prints
    python3 tahoe_status.py status --data DIR --atlas-out DIR2/atlas --panel-out DIR2/gene_panel   (other folders)

It only reads: the scripts' own logs (the latest run of each = the part after the last '=====' header line), the job
files that 'tahoe' keeps in <data>/.tahoe, and the process list (ps), so it also sees runs that were started by hand
(e.g. 'nohup python3 tahoe_atlas.py compute > /dev/null 2>&1 &' from the data folder).
Output made by an older method than the repo's scripts (the atlas's effects/complete.json version, the panel's
results/run_info.json method_version) shows as 'done, but outdated (method vN)'; 'facts' then says what 'tahoe run'
redoes (atlas_plan, panel_plan): only the effects and angles when the atlas build is complete, only the panel's
analysis when its extract is complete.
Other subcommands, used by 'tahoe': next, facts, blockers, gate, stopinfo, logfile, briefcheck, zip, smoke.
"""

import argparse
import filecmp
import glob
import json
import math
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
import zipfile

SCRIPTS = {"tahoe_atlas.py": "atlas", "tahoe_gene_panel.py": "panel", "tahoe_mtap_gankyrin.py": "mtap"}
LONG = {"atlas": {"compute", "build", "effects", "angles", "all"},      # commands that read the whole dataset
        "panel": {"extract", "analyze", "all"},
        "mtap": {"extract", "analyze", "all", "coreg"}}
VALUE_OPTS = {"--data", "--out", "--workers", "--batch-size", "--limit-files", "--layout", "--min-cells", "--angles",
              "--focus-genes", "--model", "--budget", "--max-turns", "--parallel", "--permission-mode", "--genes",
              "--mtap-null", "--tp53-wt", "--tp53-altered", "--prior", "--extra-genes", "--pcs", "--seed",
              "--unreliable-plates", "--atlas"}
JOBS = ["download", "atlas", "panel", "mtap", "agents"]
LABEL = {"download": "Download", "atlas": "Atlas", "panel": "Gene panel", "mtap": "MTAP/Gankyrin", "agents": "Agents"}
NAME = {"download": "the download", "atlas": "the atlas", "panel": "the gene panel",
        "mtap": "the MTAP/Gankyrin trial", "agents": "the agents"}
LOGNAME = {"atlas": "atlas.log", "panel": "gene_panel.log", "mtap": "mtap_gankyrin.log"}
EXPECTED_FILES = 3388           # expression files of the full download (used when the file names do not say)
META_TABLES = ["gene_metadata", "sample_metadata", "cell_line_metadata", "drug_metadata"]
FALLBACK_TAG = "<!-- agent did not write its report"
ANGLES_ATLAS = 9                # tahoe_atlas.ANGLES
# fixed guesses (minutes), used only when the log holds no earlier run to measure: shown as 'about'
EST = {"effects": 15, "angles": 5, "analyze": 5, "mtap_analyze": 3, "agent_round": 12, "overview": 8}
RATIO = {"effects": 0.4, "angles": 0.2}     # of the build's duration (the user's real run: 10.8 / 4.2 / 2.3 min)
DEPS = {"panel": ["download", "atlas", "mtap"], "atlas": ["download"], "mtap": ["download"], "download": [],
        "agents": ["atlas", "panel"]}        # a queued job does not start when one of these it waited for ended badly
REPO = os.path.dirname(os.path.abspath(__file__))
ADVISORY = re.compile(r"hard drive|^\s*WARNING|^\s*note:", re.I)    # log lines that are advice, not progress
# a script path named in an agent brief (quoted when it holds spaces): its look-up commands run that file
_SCRIPT = r"tahoe_(?:atlas|gene_panel|mtap_gankyrin)\.py"
SCRIPT_REF = re.compile(rf"'([^'\n]*{_SCRIPT})'|\"([^\"\n]*{_SCRIPT})\"|([^\s`'\"]*{_SCRIPT})")
# the method version each part's output records, and the constant in the repo's script that it must match
VERSION_OF = {"atlas": ("tahoe_atlas.py", "EFFECTS_VERSION"), "panel": ("tahoe_gene_panel.py", "PANEL_METHOD"),
              "mtap": ("tahoe_mtap_gankyrin.py", "METHOD_VERSION")}
HEADER = re.compile(r"^===== (\S+)\s*(.*?) started (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)(?: \| .*)? =====\s*$")
STAMP = re.compile(r"^\[(\d\d):(\d\d):(\d\d)\] ?(.*)$")
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")


# ============================================================================= small helpers
def real(p):
    return os.path.realpath(os.path.expanduser(p)) if p else p


def read_text(path, default=None):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read().strip()
    except OSError:
        return default


def read_tail(path, nbytes):
    """The last `nbytes` of a file as text (None when it cannot be read)."""
    try:
        size = os.path.getsize(path)
        with open(path, "rb") as fh:
            if size > nbytes:
                fh.seek(size - nbytes)
            return fh.read().decode("utf-8", "replace")
    except OSError:
        return None


def mtime(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return 0.0


def num(n):
    return f"{n:,}"


def dur(sec):
    m = int(round(max(sec, 0) / 60))
    if m < 1:
        return "less than 1 min"
    if m < 60:
        return f"{m} min"
    h, m = divmod(m, 60)
    return f"{h} h {m} min" if m else f"{h} h"


def clock(t, now):
    lt, ln = time.localtime(t), time.localtime(now)
    return time.strftime("%H:%M" if (lt.tm_year, lt.tm_yday) == (ln.tm_year, ln.tm_yday) else "%b %d %H:%M", lt)


def tilde(p):
    home = os.path.expanduser("~")
    p = str(p)
    return "~" + p[len(home):] if home and home != "/" and (p == home or p.startswith(home + os.sep)) else p


def home_tilde(text):
    """Every path below the home folder in a message as ~/..."""
    home = os.path.expanduser("~")
    return text.replace(home + os.sep, "~" + os.sep) if home and home != "/" else text


def parse_opts(tokens):
    """(first positional = the script's command, {option: value}) from a script's arguments."""
    cmd, opts, i = None, {}, 0
    while i < len(tokens):
        t = tokens[i]
        if t.startswith("--"):
            if "=" in t:
                k, v = t.split("=", 1)
                opts[k] = v
            elif t in VALUE_OPTS and i + 1 < len(tokens):
                opts[t] = tokens[i + 1]
                i += 1
            else:
                opts[t] = True
        elif cmd is None:
            cmd = t
        i += 1
    return cmd, opts


# ============================================================================= processes
def python_script_index(args):
    """Index of the script in a python command line's arguments (after options such as -u, -W ignore, -X utf8),
    or None (python -c / -m, or no script)."""
    k = 0
    while k < len(args):
        x = args[k]
        if x == "--":
            return k + 1 if k + 1 < len(args) else None
        if not x.startswith("-") or x == "-":
            return k
        if x.startswith("--"):
            k += 2 if x == "--check-hash-based-pycs" else 1
            continue
        flags = x[1:]
        for i, c in enumerate(flags):
            if c in "cm":
                return None
            if c in "WX":                       # these take a value: attached (-Wignore) or the next argument
                k += 1 if i + 1 < len(flags) else 2
                break
        else:
            k += 1
    return None


def etime_seconds(x):
    """ps's elapsed time ([[dd-]hh:]mm:ss) in seconds (0 when unreadable)."""
    try:
        days, _, rest = x.rpartition("-")
        f = [int(v) for v in rest.split(":")]
        while len(f) < 3:
            f.insert(0, 0)
        return (int(days) if days else 0) * 86400 + f[0] * 3600 + f[1] * 60 + f[2]
    except ValueError:
        return 0


class Procs:
    """Every process (ps), and which of them are runs of these scripts for one data folder."""

    def __init__(self, data):
        self.data = real(data)
        self.forms = sorted({os.path.abspath(os.path.expanduser(data)), self.data}, key=len, reverse=True)
        self.table = {}
        self.ok = True              # False: ps failed, so what runs is unknown ('blockers' and 'facts' then refuse)
        try:
            r = subprocess.run(["ps", "-ww", "-e", "-o", "pid=,ppid=,etime=,args="], capture_output=True, text=True,
                               timeout=30)
            txt = r.stdout
            self.ok = r.returncode == 0
        except Exception:  # noqa: BLE001  (no ps, or it hung)
            txt, self.ok = "", False
        now = time.time()
        for line in txt.splitlines():
            parts = line.split(None, 3)
            if len(parts) < 3 or not parts[0].isdigit() or not parts[1].isdigit():
                continue
            pid = int(parts[0])
            self.table[pid] = {"pid": pid, "ppid": int(parts[1]), "args": parts[3] if len(parts) > 3 else "",
                               "start": now - etime_seconds(parts[2])}
        if not self.table:
            self.ok = False
        self.table.pop(os.getpid(), None)
        self.found = [x for x in (self.classify(p) for p in self.table.values()) if x]

    def argv(self, p):
        try:
            with open(f"/proc/{p['pid']}/cmdline", "rb") as fh:
                raw = fh.read().rstrip(b"\0")
            if raw:
                return [a.decode("utf-8", "replace") for a in raw.split(b"\0")]
        except OSError:
            pass
        # no /proc (macOS): ps prints the arguments joined by spaces; keep a data folder with spaces in one piece
        s, keep = p["args"], {}
        for k, form in enumerate(self.forms):
            if " " in form and form in s:
                tok = f"\x01{k}\x01"
                s = s.replace(form, tok)
                keep[tok] = form
        out = []
        for x in s.split():
            for tok, form in keep.items():
                x = x.replace(tok, form)
            out.append(x)
        return out

    @staticmethod
    def cwd(pid):
        try:
            return os.readlink(f"/proc/{pid}/cwd")
        except OSError:
            pass
        if shutil.which("lsof"):                    # macOS
            try:
                out = subprocess.run(["lsof", "-a", "-p", str(pid), "-d", "cwd", "-Fn"], capture_output=True,
                                     text=True, timeout=10).stdout
                for x in out.splitlines():
                    if x.startswith("n/"):
                        return x[1:]
            except Exception:  # noqa: BLE001
                pass
        return None

    def mine(self, pid, folder):
        """Is `folder` (relative to the process's working folder) this data folder? Unknown counts as yes."""
        if folder and os.path.isabs(os.path.expanduser(folder)):
            return real(folder) == self.data
        cwd = self.cwd(pid)
        if cwd is None:
            return True
        return real(os.path.join(cwd, folder or ".")) == self.data

    def classify(self, p):
        a = p["args"]
        if not any(k in a for k in ("_job", "tahoe_", "download", "Tahoe")):
            return None
        argv = self.argv(p)
        if not argv:
            return None
        exe = os.path.basename(argv[0])
        if "_job" in argv:                                      # a background job of 'tahoe'
            i = argv.index("_job")
            if i + 2 < len(argv) and i >= 1 and os.path.basename(argv[i - 1]).startswith("tahoe") \
                    and real(argv[i + 2]) == self.data:
                return {"pid": p["pid"], "kind": "runner", "job": argv[i + 1]}
            return None
        if exe in ("bash", "sh", "dash", "zsh") and any(os.path.basename(x) == "00_download_tahoe.sh" for x in argv):
            k = [os.path.basename(x) for x in argv].index("00_download_tahoe.sh")
            dest = argv[k + 1] if k + 1 < len(argv) else os.path.expanduser("~/Tahoe-100M")
            return {"pid": p["pid"], "kind": "proc", "job": "download"} if self.mine(p["pid"], dest) else None
        rest = argv[1:]
        if exe.startswith("python"):
            k = python_script_index(rest)
            if k is None:
                return None
            exe = os.path.basename(rest[k])
            rest = rest[k + 1:]
        if exe in SCRIPTS:
            cmd, opts = parse_opts(rest)
            job = SCRIPTS[exe]
            if cmd == "agents":
                kind, part = "agents", job
            elif cmd in LONG[job]:
                kind, part = job, None
            else:
                return None                                     # check, bundle, lookup: quick
            if not self.mine(p["pid"], opts.get("--data")):
                return None
            out = opts.get("--out")
            if out and not os.path.isabs(os.path.expanduser(out)):
                cwd = self.cwd(p["pid"])
                out = os.path.join(cwd, out) if cwd else None
            return {"pid": p["pid"], "kind": "proc", "job": kind, "part": part, "cmd": cmd, "script": exe,
                    "out": real(out) if out else None, "start": p.get("start")}
        if exe in ("hf", "huggingface-cli") and "download" in rest and any("Tahoe-100M" in x for x in rest):
            _cmd, opts = parse_opts(rest)
            dest = opts.get("--local-dir")
            return {"pid": p["pid"], "kind": "proc", "job": "download"} if dest and self.mine(p["pid"], dest) \
                else None
        return None

    def descendants(self, pids):
        kids = {}
        for p in self.table.values():
            kids.setdefault(p["ppid"], []).append(p["pid"])
        out, todo = [], list(pids)
        while todo:
            x = todo.pop()
            for c in kids.get(x, []):
                if c not in out and c not in pids:
                    out.append(c)
                    todo.append(c)
        return out

    def runner_pid(self, pid):
        """The pid of the 'tahoe' job (runner) a process runs under, or None (= started by hand)."""
        runners = {f["pid"] for f in self.found if f["kind"] == "runner"}
        seen = set()
        while pid and pid not in seen:
            seen.add(pid)
            if pid in runners:
                return pid
            pid = self.table.get(pid, {}).get("ppid")
        return None

    def runner_of(self, pid):
        """The 'tahoe' job (runner) a process runs under, or None (= started by hand)."""
        r = self.runner_pid(pid)
        return next((f["job"] for f in self.found if f["kind"] == "runner" and f["pid"] == r), None)

    def of(self, job, kind="proc"):
        return [f for f in self.found if f["job"] == job and f["kind"] == kind]


# ============================================================================= logs
class Section:
    """One run in a script's log (default: the latest): header (script, command, start) and its [HH:MM:SS] lines."""

    def __init__(self, path, rows=None, h=None):
        self.path, self.ok = path, False
        self.lines, self.start, self.command, self.title, self.opts = [], None, None, "", {}
        if rows is None:
            text = read_tail(path, 8_000_000)
            if text is None:
                return
            rows = text.splitlines()
            h = next((i for i in range(len(rows) - 1, -1, -1) if rows[i].startswith("===== ")), None)
        if h is None:
            return
        end = next((i for i in range(h + 1, len(rows)) if rows[i].startswith("===== ")), len(rows))
        m = HEADER.match(rows[h])
        if not m:
            return
        self.ok = True
        self.title = (m.group(1) + " " + m.group(2)).strip()
        self.command, self.opts = parse_opts(m.group(2).split())
        try:
            self.start = time.mktime(time.strptime(m.group(3), "%Y-%m-%d %H:%M:%S"))
        except ValueError:
            self.start = mtime(path)
        day0 = time.mktime(time.strptime(m.group(3)[:10], "%Y-%m-%d"))
        t_prev, day = self.start, 0
        for raw in rows[h + 1:end]:
            s = STAMP.match(raw)
            if s:
                tod = int(s.group(1)) * 3600 + int(s.group(2)) * 60 + int(s.group(3))
                t = day0 + day * 86400 + tod
                if t < t_prev - 12 * 3600:                          # past midnight
                    day += 1
                    t += 86400
                t_prev = max(t_prev, t)
                self.lines.append((t, s.group(4), True))
            elif raw.strip():
                self.lines.append((t_prev, raw, False))             # traceback lines and the like

    def stamped(self):
        return [(t, m) for t, m, st in self.lines if st]

    def find(self, prefix):
        for t, msg, stamped in self.lines:
            if stamped and msg.startswith(prefix):
                return t, msg
        return None

    def last(self, skip=None):
        """The last time-stamped line (not a traceback line; none that `skip` matches)."""
        for t, msg, stamped in reversed(self.lines):
            if stamped and msg.strip() and not (skip and skip.search(msg)):
                return t, msg
        return None

    def ending(self):
        """('crashed', reason) / ('failed', reason) / ('stopped', how) / None: how the run ended, from its lines."""
        for i, (t, msg, stamped) in enumerate(self.lines):
            if not stamped:
                continue
            if msg.startswith("CRASHED"):
                tb = []
                for _t, m, st in self.lines[i + 1:]:
                    if st:
                        break
                    tb.append(m.strip())
                reason = tb[-1] if tb else "a Python error"
                return "crashed", reason, t
            if msg.startswith("STOPPED by"):
                how = msg[len("STOPPED "):].strip()
                return "stopped", "stopped with 'tahoe stop'" if "tahoe stop" in how else "stopped " + how, t
            if msg.startswith("STOPPED"):
                return "failed", msg.split(":", 1)[1].strip() if ":" in msg else msg, t
        return None


def all_sections(path):
    """Every run in a log (its last 8 MB), oldest first."""
    text = read_tail(path, 8_000_000)
    if text is None:
        return []
    rows = text.splitlines()
    secs = [Section(path, rows, i) for i, r in enumerate(rows) if r.startswith("===== ")]
    return [x for x in secs if x.ok]


def last_console_lines(path, n=3):
    """The error lines of a job's console output (check FAIL lines, Python errors), else its last lines. Reads only
    the end of the file (a download's console holds hours of progress bars) and splits progress-bar updates."""
    text = read_tail(path, 65536) or ""
    rows = [ANSI.sub("", r).rstrip() for r in re.split(r"\r|\n|(?=\[tahoe\] \d\d:\d\d)", text) if r]
    rows = [r for r in rows if r.strip() and not r.startswith("[tahoe]")]
    fails = [r for r in rows if r.startswith("[FAIL]")]
    if fails:
        return fails[:4]
    errs = [r for r in rows if re.search(r"error|Error|FAIL|STOPPED|Traceback|No such file|not found|denied|Killed",
                                         r)]
    pick = errs[-n:] if errs else rows[-n:]
    return [p.strip() for p in pick]


# ============================================================================= one job's view
class Ctx:
    def __init__(self, args):
        self.args = args
        self.now = time.time()
        self.data = real(args.data)
        self.state = real(args.state) if args.state else os.path.join(self.data, ".tahoe")
        self.out = {"atlas": real(args.atlas_out) if args.atlas_out else os.path.join(self.data, "atlas"),
                    "panel": real(args.panel_out) if args.panel_out else os.path.join(self.data, "gene_panel"),
                    "mtap": real(args.mtap_out) if args.mtap_out else os.path.join(self.data, "mtap_gankyrin")}
        self.me = getattr(args, "me", None) or "tahoe"
        self.procs = Procs(self.data)
        self.jf = {j: self.job_files(j) for j in JOBS}
        self.V = None                   # the views, once collect() ran
        self._ver = {}                  # the method versions of the repo's scripts (read once)
        self._expr = None               # the download's expression files (expression_now, read once)

    def job_files(self, job):
        """The files 'tahoe' keeps for a background job, and whether its runner is alive."""
        def rd(ext):
            return read_text(os.path.join(self.state, f"{job}.{ext}"))
        info = {"pid": rd("pid"), "queued": rd("queued"), "started": rd("started"), "exit": rd("exit"),
                "what": rd("what"), "created": rd("created"), "step": rd("step"), "skipped": rd("skipped"),
                "after": (rd("after") or "").split(), "console": os.path.join(self.state, f"{job}.console")}
        alive = [f["pid"] for f in self.procs.of(job, "runner")]
        info["alive"] = alive
        for k in ("started", "created"):
            try:
                info[k] = float(info[k]) if info[k] else None
            except ValueError:
                info[k] = None
        try:
            info["seq"] = int(info["queued"]) if info["queued"] else None
        except ValueError:
            info["seq"] = 0
        ex = (info["exit"] or "").split()
        info["rc"] = int(ex[0]) if ex and ex[0].lstrip("-").isdigit() else None
        info["ended"] = float(ex[1]) if len(ex) > 1 and ex[1].replace(".", "").isdigit() else None
        info["how"] = ex[2] if len(ex) > 2 else ""
        return info

    def is_queued(self, job):
        jf = self.jf[job]
        return bool(jf["alive"]) and jf["queued"] is not None

    def is_running(self, job):
        if job == "agents":
            return bool(self.procs.of("agents")) or (bool(self.jf["agents"]["alive"]) and not self.is_queued("agents"))
        return bool(self.procs.of(job)) or (bool(self.jf[job]["alive"]) and not self.is_queued(job))

    def logpath(self, job, part=None):
        if job == "download":
            return self.jf["download"]["console"]
        if job == "agents":
            return os.path.join(self.out[part or "atlas"], "agents.log")
        for f in self.procs.of(job):
            if f.get("out"):
                return os.path.join(f["out"], LOGNAME[job])
        return os.path.join(self.out[job], LOGNAME[job])

    # ---- readiness from the output files
    def stamp(self, job):
        """The file that records the method version of a part's output: the atlas's effects/complete.json (written
        last by 'effects'), the panel's / trial's results/run_info.json (written last by 'analyze'; runs before
        method v3 wrote none)."""
        return os.path.join(self.out[job], "effects", "complete.json") if job == "atlas" else \
            os.path.join(self.out[job], "results", "run_info.json")

    def version(self, job):
        """(method version the output records, the version the repo's script writes); None when unknown (no
        stamp, or a repo script that predates version stamps)."""
        if job not in self._ver:
            name, const = VERSION_OF[job]
            m = re.search(rf"^{const} = (\d+)", read_text(os.path.join(REPO, name), "") or "", re.M)
            self._ver[job] = int(m.group(1)) if m else None
        have = None
        try:
            with open(self.stamp(job), encoding="utf-8") as fh:
                have = json.load(fh).get("version" if job == "atlas" else "method_version")
            have = int(have) if have is not None else None
        except (OSError, ValueError, AttributeError, TypeError):
            pass
        return have, self._ver[job]

    def atlas_version(self):
        return self.version("atlas")

    def outdated(self, job):
        """True when finished output of `job` was made by an older method than the repo's script (the atlas: its
        effects; the gene panel and the MTAP/Gankyrin trial: their analysis) and must be computed again. The gene
        panel is also outdated when its extract predates the repo's built-in gene list (panel_list_outdated: new
        genes were added, so 'all' extracts again)."""
        done = os.path.join(self.out[job], "effects", "complete.json") if job == "atlas" else \
            os.path.join(self.out[job], "results", "summary.txt")
        if not os.path.exists(done):
            return False
        have, want = self.version(job)
        stale = want is not None and have != want
        if job == "panel":
            stale = stale or self.panel_list_outdated()
        return stale

    def panel_list_version(self):
        """(the panel_list of the panel's extract, the PANEL_LIST the repo's tahoe_gene_panel.py defines); a part
        None when unknown. An extract from before the constant existed reads as list 1."""
        if "panel_list" not in self._ver:
            m = re.search(r"^PANEL_LIST = (\d+)", read_text(os.path.join(REPO, "tahoe_gene_panel.py"), "") or "", re.M)
            self._ver["panel_list"] = int(m.group(1)) if m else None
        have = None
        try:
            with open(os.path.join(self.out["panel"], "extract_info.json"), encoding="utf-8") as fh:
                have = int(json.load(fh).get("panel_list") or 1)
        except (OSError, ValueError, AttributeError, TypeError):
            pass
        return have, self._ver["panel_list"]

    def panel_list_outdated(self):
        """True when the panel's extract was made with an older built-in gene list than the repo's (new genes were
        added since: 'tahoe run' / 'tahoe panel' re-extracts and analyses again)."""
        have, want = self.panel_list_version()
        return have is not None and want is not None and have < want

    def atlas_outdated(self):
        return self.outdated("atlas")

    def ready(self, job):
        """Finished, current output: the atlas's effects of this method plus a finished 'angles' after them (its
        angles/complete.json; every brief newer than the effects: older ones describe other numbers), the panel's
        analysis of this method with its briefs."""
        o = self.out.get(job)
        if job == "atlas":                 # every brief (an interrupted or failed 'angles' leaves older ones) and
            cj = os.path.join(o, "effects", "complete.json")      # the angles' own stamp, written last, are newer
            aj = os.path.join(o, "angles", "complete.json")
            briefs = glob.glob(os.path.join(o, "angles", "*", "brief.md"))
            return os.path.exists(cj) and not self.outdated("atlas") and bool(briefs) and \
                all(mtime(b) >= mtime(cj) for b in briefs) and os.path.exists(aj) and mtime(aj) >= mtime(cj)
        if job == "panel":
            return os.path.exists(os.path.join(o, "results", "summary.txt")) and not self.outdated("panel") and \
                bool(glob.glob(os.path.join(o, "angles", "*", "brief.md")))
        if job == "mtap":
            return os.path.exists(os.path.join(o, "results", "summary.txt"))
        return False

    def report_current(self, part, brief):
        """True when the agent of this brief has a report newer than the brief (the next 'agents' run skips it)."""
        name = os.path.basename(os.path.dirname(brief))
        for r in glob.glob(os.path.join(self.out[part], "reports", f"[0-9][0-9]_{name}.md")):
            head = read_text(r, "")[:600]
            if mtime(r) >= mtime(brief) and os.path.getsize(r) >= 200 and FALLBACK_TAG not in head:
                return True
        return False

    def reports(self, part):
        """(current reports, agent folders): a report is current when it is newer than its brief."""
        briefs = glob.glob(os.path.join(self.out[part], "angles", "*", "brief.md"))
        return sum(self.report_current(part, b) for b in briefs), len(briefs)


def base_view(ctx, job, sec, done_markers):
    """State of atlas / panel / mtap from processes, the job files and the latest log section."""
    jf, now = ctx.jf[job], ctx.now
    v = {"job": job, "state": "none", "by": None, "lines": [], "since": None, "sec": sec, "reason": []}
    procs = ctx.procs.of(job)
    fresh = sec.ok and (jf["started"] is None or sec.start >= jf["started"] - 5)
    if procs:
        v["state"] = "running"
        v["by"] = "tahoe" if ctx.procs.runner_of(procs[0]["pid"]) else "hand"
        v["since"] = sec.start if sec.ok and fresh else (jf["started"] or now)
        if not fresh and jf["started"]:
            v["starting"] = True
        p0 = min((p.get("start") or now) for p in procs)
        if not sec.ok or sec.start < p0 - 30:    # the log's latest run is an older one: this run has not logged yet
            v["starting"], v["since"] = True, p0
        if v["by"] == "hand" and jf["alive"] and jf["queued"] is not None:
            v["also_queued"] = True             # 'tahoe' queued the same job: it waits for this run
        return v
    if jf["alive"]:
        if jf["queued"] is not None:
            v["state"] = "queued"
            v["since"] = jf["created"]
            return v
        v["state"] = "running"
        v["by"] = "tahoe"
        v["since"] = jf["started"] or now
        v["starting"] = True
        return v
    if jf["rc"] is not None and (jf["ended"] or 0) >= (sec.start or 0) - 5:
        if jf["how"] == "skipped":
            v["state"], v["ended"] = "skipped", jf["ended"]
            v["waited"] = jf["skipped"] or "the run it waited for ended badly"
            return v
        if jf["how"] == "stopped":
            v["state"], v["ended"] = "stopped", jf["ended"]
            v["reason"] = [f"stopped with '{ctx.me} stop' at {clock(jf['ended'] or now, now)}"]
            return v
        if jf["how"] == "cancelled":
            v["cancelled"] = jf["ended"]
        elif jf["rc"] != 0 and not fresh:
            v["state"], v["ended"] = "failed", jf["ended"]
            v["reason"] = [f"exit code {jf['rc']}" + (" (killed: often out of memory)" if jf["rc"] == 137 else "")] \
                + last_console_lines(jf["console"])
            return v
        elif jf["rc"] != 0 and fresh and not sec.ending():
            v["state"], v["ended"] = "failed", jf["ended"]
            v["reason"] = [f"exit code {jf['rc']}" + (" (killed: often out of memory)" if jf["rc"] == 137 else ""),
                           f"last line: {sec.last()[1].strip() if sec.last() else '-'}"]
            return v
    if not sec.ok:
        v["state"] = "done" if ctx.ready(job) else "none"
        return v
    v["since"] = sec.start
    end = sec.ending()
    if end:
        kind, reason, t = end
        v["ended"] = t
        if kind == "stopped":
            v["state"], v["reason"] = "stopped", [reason + f" at {clock(t, now)}"]
        else:
            v["state"], v["reason"] = "failed", [("crashed: " if kind == "crashed" else "") + reason]
        return v
    marker = done_markers.get(sec.command)
    hit = sec.find(marker) if marker else None
    if hit:
        v["state"], v["ended"] = "done", hit[0]
        return v
    last = sec.last()
    v["state"] = "stopped"
    v["ended"] = last[0] if last else sec.start
    v["reason"] = [KILLED]
    return v


KILLED = "ended without finishing (killed, often by running out of memory, or the computer restarted)"


# ---- the atlas
def atlas_view(ctx):
    sec = Section(ctx.logpath("atlas"))
    v = base_view(ctx, "atlas", sec, {"compute": "Computation done", "build": "Build done",
                                      "effects": "Effects done", "angles": "Angles done", "all": "Agents done"})
    now = ctx.now
    if v["state"] == "running" and sec.ok and not v.get("starting"):
        atlas_progress(ctx, sec, v)
    elif v["state"] == "done":
        b = sec.find("Build done")
        e = sec.find("Effects done")
        a = sec.find("Angles done")
        bits = []
        if b:
            m = re.search(r"Build done: ([\d,]+) cells", b[1])
            if m:
                bits.append(f"{m.group(1)} cells")
        if e:
            m = re.search(r"Effects done: ([\d,]+) genes x ([\d,]+) drug-doses x (\d+) lines", e[1])
            if m:
                bits.append(f"{m.group(1)} genes x {m.group(2)} drug-doses x {m.group(3)} lines")
        if a and "FAILED:" in a[1]:
            bits.append("angles that FAILED: " + a[1].split("FAILED:", 1)[1].strip())
        if sec.ok:
            v["at"] = finished_at(sec, v, now, "compute")
            if bits:
                v["lines"].append("; ".join(bits))
        if not ctx.ready("atlas") and sec.command in ("build", "effects"):
            v["state"] = "partial"
            v["lines"].append(("effects and angles" if sec.command == "build" else "angles") + " not run yet")
    if v["state"] in ("done", "partial", "none") and ctx.atlas_outdated():
        v["state"] = "outdated"
        v["lines"].append(f"{made_with(ctx, 'atlas', 'computed')}: '{ctx.me} run' "
                          + ("redoes its effects and angles (the build is reused)" if atlas_built(ctx)
                             else "computes it again (finished plates are reused)"))
    return v


def made_with(ctx, job, verb):
    """'computed with method v2 (now v3)' / 'analysed before method v3' for an outdated part."""
    have, want = ctx.version(job)
    return f"{verb} with method v{have} (now v{want})" if have else f"{verb} before method v{want}"


def panel_list_added(ctx):
    """What the newest built-in gene list added (PANEL_LIST_NOTE in tahoe_gene_panel.py), for the outdated message;
    a plain fallback when the constant cannot be read."""
    m = re.search(r'^PANEL_LIST_NOTE = "([^"\n]*)"', read_text(os.path.join(REPO, "tahoe_gene_panel.py"), "") or "",
                  re.M)
    return m.group(1) if m else "the genes it now adds"


def panel_gene_list_outdated(ctx, job):
    """The panel is outdated only because its extract predates the repo's genes (its method version is current)."""
    return job == "panel" and ctx.panel_list_outdated() and ctx.version(job)[0] == ctx.version(job)[1]


# ---- time estimates from the earlier runs in the same log (every run appends to it)
def files_of_section(sec):
    for _t, msg in sec.stamped():
        m = re.match(r"([\d,]+) files on \d+ plates", msg) or re.match(r"Finding the plate of each of ([\d,]+) files",
                                                                        msg)
        if m:
            return int(m.group(1).replace(",", ""))
    return None


def atlas_phases(sec):
    """{phase: minutes} of the atlas phases this run finished: build (only when it read every plate itself),
    effects, angles (only when it ran all of them)."""
    t, reused = {}, False
    for tt, msg in sec.stamped():
        if re.match(r"[\d,]+ files on \d+ plates", msg):
            t.setdefault("b0", tt)
        elif re.match(r"\s+\S+ already built \(", msg):
            reused = True
        elif msg.startswith("Build done"):
            t["b1"] = tt
        elif msg.startswith("Pass 1"):
            t.setdefault("e0", tt)
        elif msg.startswith("Effects done"):
            t["e1"] = tt
        elif msg.startswith("Angle: ") or msg.startswith("Focus: "):
            t.setdefault("a0", tt)
        elif msg.startswith("Angles done"):
            t["a1"] = tt
    ph = {}
    if "b0" in t and "b1" in t and not reused:
        ph["build"] = (t["b1"] - t["b0"]) / 60.0
    if "e0" in t and "e1" in t:
        ph["effects"] = (t["e1"] - t["e0"]) / 60.0
    if "a0" in t and "a1" in t and not sec.opts.get("--angles"):
        ph["angles"] = (t["a1"] - t["a0"]) / 60.0
    return ph


def atlas_history(sec):
    """{phase: minutes} from the latest earlier runs in this log on the same number of files."""
    out = {}
    n_cur = files_of_section(sec) if sec.ok else None
    for s in reversed(all_sections(sec.path)):
        if sec.ok and abs((s.start or 0) - (sec.start or 0)) < 1:
            continue                                        # the run going on now
        n = files_of_section(s)
        if n_cur and n and abs(n - n_cur) > 0.1 * n_cur:
            continue                                        # a trial on fewer files
        for k, x in atlas_phases(s).items():
            out.setdefault(k, x)
    return out


def atlas_estimates(sec, build_total=None):
    """{'effects': (minutes, how), 'angles': (minutes, how)}: how = 'last' (measured in an earlier run here),
    'scaled' (from this machine's build time) or 'fixed' (a guess)."""
    hist = atlas_history(sec)
    b = build_total or atlas_phases(sec).get("build") or hist.get("build")
    share = min(1.0, (files_of_section(sec) or EXPECTED_FILES) / EXPECTED_FILES)    # a smaller download: faster
    est = {}
    for k in ("effects", "angles"):
        if k in hist:
            est[k] = (hist[k], "last")
        elif b:
            est[k] = (max(1.0, RATIO[k] * b), "scaled")
        else:
            est[k] = (max(1.0, EST[k] * share), "fixed")
    return est


def fmt_min(x, how="fixed"):
    """'~7 min' (measured), 'about 7 min' (a guess), 'under 1 min'."""
    if x < 1:
        return "under 1 min"
    return ("~" if how in ("last", "data") else "about ") + dur(x * 60)


def as_last(*hows):
    return " (as last time)" if "last" in hows else ""


def finished_at(sec, v, now, default):
    """' at 19:05 (took 1 h 3 min)' for the head line; the command too when it is not the usual one."""
    end = v.get("ended") or sec.start
    what = "" if sec.command == default else f" ('{sec.command}')"
    return f" at {clock(end, now)}{what} (took {dur(end - sec.start)})"


def atlas_progress(ctx, sec, v):
    now = ctx.now
    phase, N, P, W = "start", None, None, None
    plates, done_plates, fx_plates, angles_done, angle_now, focus = {}, {}, 0, 0, None, 0
    t_phase = sec.start
    for t, msg in sec.stamped():
        if msg.startswith("Indexing parquet files") or "parquet files since the last index" in msg:
            phase, t_phase = "index", t
        elif msg.startswith("Finding the plate of each of"):
            phase, t_phase = "find", t
            m = re.search(r"of ([\d,]+) files", msg)
            N = int(m.group(1).replace(",", "")) if m else N
        elif re.match(r"[\d,]+ files on \d+ plates", msg):
            m = re.match(r"([\d,]+) files on (\d+) plates -> one group per plate, (\d+) at a time", msg)
            if m:
                N, P, W = int(m.group(1).replace(",", "")), int(m.group(2)), int(m.group(3))
            phase, t_phase = "build", t
        elif re.match(r"\s{3,}\S+: \d+/\d+ files, ", msg):
            m = re.match(r"\s+(\S+): (\d+)/(\d+) files, ([\d,]+) cells, ~(\d+) min left", msg)
            if m:
                plates[m.group(1)] = {"k": int(m.group(2)), "n": int(m.group(3)), "left": int(m.group(5)), "t": t}
        elif re.match(r"\s+\S+ (done|already built) \(\d+/\d+ plates", msg):
            m = re.match(r"\s+(\S+) (done|already built) \((\d+)/(\d+) plates", msg)
            done_plates[m.group(1)] = m.group(2)
            P = int(m.group(4))
        elif msg.startswith("Build done"):
            phase, t_phase = "built", t
        elif msg.startswith("Pass 1"):
            phase, t_phase = "fx1", t
        elif msg.startswith("Pass 2"):
            phase = "fx2"
        elif re.match(r"\s+\S+: \d+ wells(?:$|;)", msg):        # method v3 adds '; median composition shift ...'
            fx_plates += 1
        elif msg.startswith("Well-position correction"):
            phase = "fx_pos"
        elif msg.startswith("Growth"):
            phase = "fx_growth"
        elif msg.startswith("Per drug and dose"):
            phase = "fx_dd"
        elif msg.startswith("FDR within each gene"):
            phase = "fx_fdr"
        elif msg.startswith("Pass 3"):
            phase = "fx3"
        elif msg.startswith("Effects done"):
            phase, t_phase = "fxdone", t
        elif msg.startswith("Angle: "):
            if phase != "angles":
                t_phase = t
            phase, angle_now = "angles", msg[len("Angle: "):].replace(" ...", "")
        elif re.match(r"\s+\S+ done in \d+ s", msg) or msg.lstrip().startswith("ERROR in angle"):
            angles_done += 1
        elif msg.startswith("Focus: "):
            if phase != "angles":
                t_phase = t
            phase, angle_now = "angles", "focus " + msg[len("Focus: "):].replace(" ...", "")
            focus += 1
        elif msg.startswith("Angles done"):
            phase, t_phase = "angdone", t
        elif msg.startswith("Computation done"):
            phase = "bundle"
        elif msg.startswith("Running ") and " agents, " in msg:
            phase, t_phase = "agents", t
    since = lambda t: (now - t) / 60.0  # noqa: E731
    left = None
    if phase == "index":
        step = "indexing the download (one time; reads only the file footers)"
    elif phase == "find":
        step = f"build: finding the plate of each of {num(N) if N else 'the'} files"
    elif phase in ("build", "start") and N:
        pb = os.path.join(ctx.out["atlas"], "pseudobulk")
        files_of = plate_files(pb)
        read = 0
        for name in done_plates:          # a finished plate: its file list, else its 'k/n' lines, else the average
            read += files_of.get(name) or plates.get(name, {}).get("n") or round(N / max(P or 1, 1))
        for name, x in plates.items():
            if name not in done_plates:
                read += x["k"]
        read = N if P and len(done_plates) >= P else min(read, N)
        pct = 100.0 * read / N if N else 0
        step = f"build: {num(read)} of {num(N)} files read ({pct:.0f}%), {len(done_plates)} of {P} plates done"
        running = [x for name, x in plates.items() if name not in done_plates]
        n_run = min(W or P, P - len(done_plates)) if P else 0
        waiting = max(0, (P or 0) - len(done_plates) - n_run)
        reused = any(x == "already built" for x in done_plates.values())
        if P and len(done_plates) >= P:
            step += "; combining them"
            est = atlas_estimates(sec)
            left = f"{fmt_min(est['effects'][0] + est['angles'][0] + 1, est['effects'][1])} for combine, effects " \
                f"and angles{as_last(est['effects'][1], est['angles'][1])}"
        elif running or (done_plates and read and since(t_phase) > 0):
            el = since(t_phase)
            b_left = max([max(0.0, x["left"] - since(x["t"])) for x in running] + [0.0])
            if (waiting or not running) and read and el > 0:    # plates waiting or just begun: the overall speed
                b_left = max(b_left, (N - read) / (read / el))
            est = atlas_estimates(sec, None if reused else el + b_left)
            fx = est["effects"][0] + est["angles"][0]
            how = est["effects"][1]
            left = f"~{max(1, round(b_left))} min build + {fmt_min(fx, how)} effects/angles" \
                + as_last(how, est["angles"][1])
        elif n_run:
            left = "known in a few minutes (after each plate's first 25 files)"
    elif phase == "built":
        step = "build done; effects starting"
        est = atlas_estimates(sec)
        left = f"{fmt_min(est['effects'][0] + est['angles'][0], est['effects'][1])} for effects and angles" \
            + as_last(est["effects"][1], est["angles"][1])
    elif phase.startswith("fx") and phase != "fxdone":
        if P is None:                   # 'effects' alone (the build is reused): its plates are the build's groups
            P = len(glob.glob(os.path.join(ctx.out["atlas"], "pseudobulk", "group*_profiles.csv"))) or None
        words = {"fx1": "pass 1 of 3 (gene levels per cell line)",
                 "fx2": f"pass 2 of 3 (corrected effects), {fx_plates} of {P or '?'} plates",
                 "fx_pos": "pass 2 of 3, well-position correction", "fx_growth": "pass 2 of 3, growth",
                 "fx_dd": "pass 2 of 3, per drug and dose", "fx_fdr": "pass 2 of 3, FDR within each gene",
                 "fx3": "pass 3 of 3 (per-line response strength)"}
        step = "effects: " + words.get(phase, phase)
        est = atlas_estimates(sec)
        (e, eh), (a, ah) = est["effects"], est["angles"]
        e_left = e - since(t_phase)
        left = (f"{fmt_min(e_left, eh)} effects" if e_left >= 1 else "effects nearly done") \
            + f" + {fmt_min(a, ah)} angles{as_last(eh, ah)}"
    elif phase == "fxdone":
        step = "effects done; angles starting"
        a, ah = atlas_estimates(sec)["angles"]
        left = f"{fmt_min(a, ah)} for the angles{as_last(ah)}"
    elif phase == "angles":
        n_focus = len([g for g in str(sec.opts.get("--focus-genes", "MTAP,PSMD10")).split(",") if g.strip()])
        sel = str(sec.opts.get("--angles", "") or "")
        total = len([a for a in sel.split(",") if a.strip() and a.strip() != "focus"]) if sel else ANGLES_ATLAS
        total += n_focus if (not sel or "focus" in sel) else 0
        n_done = angles_done + max(0, focus - 1)
        step = f"angles: {min(n_done, total)} of {total} done (now: {angle_now})"
        a, ah = atlas_estimates(sec)["angles"]
        if sel or ah == "fixed":                            # no measure of this selection: by the count
            a_left = a * (total - n_done) / max(total, 1)
        else:
            a_left = a - since(t_phase)
        left = (fmt_min(a_left, ah) if a_left >= 1 else "about 1 min") + as_last(ah)
    elif phase in ("angdone", "bundle"):
        step = "writing the bundle (atlas_bundle.zip)"
        left = "under 1 min"
    elif phase == "agents":                    # 'tahoe_atlas.py all': the agents run inside the atlas log
        tmp = {"lines": []}
        agents_progress(sec, tmp, now)
        step = "agents: " + tmp["lines"][0]
        left = tmp["lines"][1].replace("time left: ", "") if len(tmp["lines"]) > 1 else None
    else:
        step = "starting"
    v["lines"].append(step)
    if left:
        v["lines"].append("time left: " + left)


def plate_files(pb):
    """{plate: number of files} of the plates the build has finished (pseudobulk/group*_files.txt)."""
    out = {}
    for f in glob.glob(os.path.join(pb, "group*_files.txt")):
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                n = sum(1 for x in fh if x.strip())
            with open(f.replace("_files.txt", "_samples.csv"), encoding="utf-8", errors="replace") as fh:
                fh.readline()
                row = fh.readline().strip().split(",")
            if len(row) >= 2:
                out[row[1]] = n
        except OSError:
            continue
    return out


# ---- the gene panel and the MTAP/Gankyrin trial (both extract with tahoe_mtap_gankyrin.cmd_extract)
PANEL_STEPS = [("Baseline by cell line", "baseline by cell line"),
               ("Expression of every extracted gene", "expression by line"),
               ("Well covariates", "well covariates"),
               ("Drug effects (corrected)", "drug effects"),
               ("Pathway scores and drug context", "pathway scores and drug context"),
               ("p53: WT vs altered", "p53 analyses"),
               ("Growth: MTAP-null", "growth screens"),
               ("Cell cycle (DMSO cells)", "cell cycle"),
               ("Co-regulation, cross-links", "co-regulation, cross-links, positive controls"),
               ("Writing summary and agent folders", "summary and agent folders")]
MTAP_STEPS = [("Baseline by cell line", "baseline by cell line"), ("Well covariates", "well covariates"),
              ("Drug effects (corrected)", "drug effects"), ("MTAP-null selective killing", "MTAP-null screen"),
              ("Gankyrin level vs drug response", "Gankyrin level screen"),
              ("Cell cycle (DMSO cells)", "cell cycle"), ("Writing summary", "summary")]


def extract_view(ctx, job):
    sec = Section(ctx.logpath(job))
    markers = ({"extract": "Well position from", "analyze": "Analysis done", "all": "Analysis done"} if job == "panel"
               else {"extract": "Well position from", "analyze": "Done. Start with", "all": "Done. Start with",
                     "coreg": "Done: results/coregulation"})
    v = base_view(ctx, job, sec, markers)
    now = ctx.now
    if v["state"] == "running" and sec.ok and not v.get("starting"):
        extract_progress(ctx, job, sec, v)
    elif v["state"] == "done" and sec.ok:
        extra = ""
        a = sec.find("Analysis done")
        if a and "failed:" in a[1]:
            extra = ": " + a[1].split(";", 1)[1].split(". Start with")[0].strip() if ";" in a[1] else ""
        d = sec.find("Done: ")
        if not extra and d:
            m = re.match(r"Done: ([\d,]+) cells", d[1])
            extra = f": {m.group(1)} cells" if m else ""
        v["at"] = finished_at(sec, v, now, "all")
        if extra:
            v["lines"].append(extra[2:])
        if sec.command == "extract" and not ctx.ready(job) and not ctx.outdated(job):
            v["state"] = "partial"
            v["lines"].append("analyze not run yet")
        if job == "panel" and ctx.ready("panel"):
            v["lines"] += panel_notes(ctx)
    if v["state"] in ("done", "partial", "none") and ctx.outdated(job):
        v["state"] = "outdated"
        if panel_gene_list_outdated(ctx, job):
            v["lines"].append(f"extracted with an older gene list (before {panel_list_added(ctx)}): "
                              f"'{ctx.me} run' extracts the new genes and analyses again")
        elif job == "panel":
            v["lines"].append(f"{made_with(ctx, job, 'analysed')}: '{ctx.me} run' "
                              + ("redoes its analysis (the extract is reused)" if extract_complete(ctx, job)
                                 else "runs it again"))
        else:                           # optional; the gene panel compares with it
            v["lines"].append(f"{made_with(ctx, job, 'analysed')} (optional: '{ctx.me} mtap' redoes it, then "
                              f"'{ctx.me} panel analyze')")
    return v


def panel_compare(ctx):
    """How the finished gene panel stands to the MTAP/Gankyrin trial: 'ok', 'none' (no trial here), 'running'
    (the trial runs or is queued), 'newer' (the trial finished after the panel's analyze)."""
    prior = os.path.join(ctx.out["panel"], "angles", "crosslinks", "prior")
    has_prior = os.path.isdir(prior) and bool(os.listdir(prior))
    if ctx.is_running("mtap") or ctx.is_queued("mtap"):
        return "running"
    if ctx.ready("mtap") and not ctx.outdated("mtap") and \
            mtime(os.path.join(ctx.out["mtap"], "results", "summary.txt")) > \
            mtime(os.path.join(ctx.out["panel"], "results", "summary.txt")):
        return "newer"
    return "ok" if has_prior else "none"


def panel_lacks_atlas(ctx):
    """True when the panel's analysis ran without the computed atlas it would use now: its agent briefs lack the
    genome-wide look-ups, or (method v3) it took no composition shift and plate factors from the atlas because the
    atlas was not computed with this method then, or the atlas's effects were computed again after it. Only for the
    atlas the panel looks for (<data>/atlas): for an atlas elsewhere a rerun would not help."""
    if real(ctx.out["atlas"]) != real(os.path.join(ctx.data, "atlas")):
        return False
    for b in glob.glob(os.path.join(ctx.out["panel"], "angles", "*", "brief.md")):
        if "not available (no computed atlas" in (read_text(b, "") or ""):
            return True
    ri_path = ctx.stamp("panel")
    try:
        with open(ri_path, encoding="utf-8") as fh:
            ri = json.load(fh)
    except (OSError, ValueError):
        return False
    if not isinstance(ri, dict):
        return False
    if "atlas not computed" in str(ri.get("composition_normalisation", "")):
        return True
    return ctx.ready("atlas") and mtime(ri_path) < mtime(ctx.stamp("atlas"))


def panel_notes(ctx):
    me, out = ctx.me, []
    c = panel_compare(ctx)
    if c == "running":
        out.append(f"not compared with the MTAP/Gankyrin trial yet (it runs; afterwards: {me} panel analyze)")
    elif c == "newer":
        out.append(f"not compared with the newest MTAP/Gankyrin trial yet: {me} panel analyze (minutes)")
    elif c == "none":
        out.append(f"not compared with MTAP/Gankyrin (optional: {me} mtap)")
    if panel_lacks_atlas(ctx):
        out.append("analysed without the current atlas (look-ups, composition shift, plate factors)"
                   + (f": {me} panel analyze (minutes)" if ctx.ready("atlas") else ""))
    return out


def extract_history(sec, job):
    """{'extract': min, 'analyze': min} measured in the latest earlier runs in this log (extract only when it read
    every file itself)."""
    steps = PANEL_STEPS if job == "panel" else MTAP_STEPS
    out = {}
    for s in reversed(all_sections(sec.path)):
        if sec.ok and abs((s.start or 0) - (sec.start or 0)) < 1:
            continue
        t = {}
        for tt, msg in s.stamped():
            m = re.match(r"([\d,]+) expression files \((\d[\d,]*) already done\)", msg)
            if m and m.group(2) == "0":
                t.setdefault("x0", tt)
            if msg.startswith("Done: ") and "cells" in msg:
                t["x1"] = tt
            if msg.startswith(steps[0][0]):
                t.setdefault("a0", tt)
            if msg.startswith("Analysis done") or msg.startswith("Done. Start with"):
                t["a1"] = tt
        if "x0" in t and "x1" in t:
            out.setdefault("extract", (t["x1"] - t["x0"]) / 60.0)
        if "a0" in t and "a1" in t:
            out.setdefault("analyze", (t["a1"] - t["a0"]) / 60.0)
    return out


def extract_progress(ctx, job, sec, v):
    now = ctx.now
    phase, N, W, prog, k_steps, genes = "start", None, None, None, None, None
    steps = PANEL_STEPS if job == "panel" else MTAP_STEPS
    t_an = None
    for t, msg in sec.stamped():
        if msg.startswith("Indexing parquet files"):
            phase = "index"
        m = re.match(r"([\d,]+) expression files \((\d[\d,]*) already done\), (\d+) workers", msg)
        if m:
            phase, N, W = "extract", int(m.group(1).replace(",", "")), int(m.group(3))
        m = re.match(r"\s+(\d+)/(\d+) files, ([\d,]+) cells, ETA (\d+) min", msg)
        if m:
            prog = (int(m.group(1)), int(m.group(2)), m.group(3), int(m.group(4)), t)
        if msg.startswith("Combining"):
            phase = "combine"
        if msg.startswith("Done: ") and "cells" in msg:
            phase = "extracted"
        for i, (pre, _w) in enumerate(steps):
            if msg.startswith(pre):
                phase, k_steps = "analyze", i
                t_an = t_an or t
        m = re.match(r"Drug effects \(corrected\) for (\d+) genes", msg)
        if m:
            genes = [0, int(m.group(1))]
        m = re.match(r"\s+(\d+)/(\d+) (?:genes|done) \(", msg)
        if m and genes:
            genes = [int(m.group(1)), int(m.group(2))]
        if msg.startswith("Analysis done") or msg.startswith("Done. Start with"):
            phase = "bundle"
    an, ah = extract_history(sec, job).get("analyze"), "last"
    if an is None:
        an, ah = float(EST["analyze"] if job == "panel" else EST["mtap_analyze"]), "fixed"
    left = None
    if phase == "index":
        step = "indexing the download (one time; reads only the file footers)"
    elif phase == "extract":
        if prog:
            i, n, cells, eta, t = prog
            step = f"extract: {num(i)} of {num(n)} files ({100.0 * i / max(n, 1):.0f}%), {cells} cells"
            left = f"~{max(1, round(eta - (now - t) / 60.0))} min extract (its estimate) + {fmt_min(an, ah)} " \
                f"analyze{as_last(ah)}"
        else:
            step = f"extract: starting ({num(N)} files, {W} workers)"
            left = "an estimate comes after the first minute"
    elif phase == "combine":
        step = "extract: combining the per-file tables"
        left = f"{fmt_min(an + 1, ah)} for combine and analyze{as_last(ah)}"
    elif phase == "extracted":
        step = "extract done; analyze starting"
        left = f"{fmt_min(an, ah)} for analyze{as_last(ah)}"
    elif phase == "analyze":
        what = steps[k_steps][1]
        if what == "drug effects" and genes:
            what += f" ({genes[0]} of {genes[1]} genes)"
        step = f"analyze: step {k_steps + 1} of {len(steps)}, {what}"
        a_left = an - (now - (t_an or now)) / 60.0
        left = (fmt_min(a_left, ah) if a_left >= 1 else "about 1 min") + as_last(ah)
    elif phase == "bundle":
        step = "writing the bundle"
        left = "under 1 min"
    else:
        step = "starting"
    v["lines"].append(step)
    if left:
        v["lines"].append("time left: " + left)


# ---- the agents (atlas/agents.log and gene_panel/agents.log; one 'tahoe agents' job can run both)
def agents_part(ctx, part):
    """State of one part (atlas / panel) of the agents: its own process, the 'tahoe agents' job (which runs the
    parts it names one after the other: job file 'what' = the parts, 'step' = the part running now) and its log."""
    sec = Section(os.path.join(ctx.out[part], "agents.log"))
    now = ctx.now
    v = {"part": part, "state": "none", "lines": [], "sec": sec, "reason": []}
    procs = [f for f in ctx.procs.of("agents") if f.get("part") == part]
    jf = ctx.jf["agents"]
    order = [p for p in (jf["what"] or "").split() if p in ("atlas", "panel")]
    step = jf["step"] if jf["step"] in order else None
    cur, nb = ctx.reports(part)
    if procs:
        v["state"] = "running"
        v["by"] = "tahoe" if ctx.procs.runner_of(procs[0]["pid"]) else "hand"
        if sec.ok:
            agents_progress(sec, v, now)
        return v
    if jf["alive"] and part in order:
        if jf["queued"] is not None or (step and order.index(part) > order.index(step)) \
                or (not step and order.index(part) > 0):
            v["state"] = "queued"
            return v
        if step == part or not step:
            v["state"], v["by"] = "running", "tahoe"
            v["lines"].append("starting")
            return v
        # an earlier part of the running job: finished, its log tells how
    if jf["rc"] is not None and part in order and step == part and (jf["ended"] or 0) >= (sec.start or 0) - 5:
        if jf["how"] == "stopped":
            v["state"] = "stopped"
            v["reason"] = [f"stopped with '{ctx.me} stop' at {clock(jf['ended'] or now, now)}"]
            return v
        if jf["rc"] != 0 and (not sec.ok or sec.start < (jf["started"] or 0) - 5):
            v["state"], v["reason"] = "failed", [f"exit code {jf['rc']}"] + last_console_lines(jf["console"])
            return v
    if not sec.ok:
        if cur:
            v["state"] = "done"
            v["lines"].append(f"{cur} of {nb} reports up to date")
        return v
    end = sec.ending()
    if end:
        kind, reason, t = end
        v["state"] = "stopped" if kind == "stopped" else "failed"
        v["reason"] = [("crashed: " if kind == "crashed" else "") + reason]
        return v
    dry = sec.find("Dry run:")
    if dry:
        m = re.search(r"Dry run: (\d+) agents planned.*Cost cap: (\d+) x \$([\d.]+) = \$([\d.]+)", dry[1])
        plan = (f": {m.group(1)} agents" + (" + overview" if "+ overview" in dry[1] else "") +
                f", cost cap ${m.group(4)}") if m else ""
        if cur:
            v["state"] = "done"
            v["lines"].append(f"{cur} of {nb} reports up to date (the latest run was a dry run{plan})")
        else:
            v["state"] = "dry"
            v["lines"].append("a dry run wrote the prompts" + plan)
        return v
    fin = sec.find("Agents done")
    if fin:
        m = re.search(r"Agents done: (\d+)/(\d+) wrote their report.*cost this run \$([\d.]+)", fin[1])
        v["state"] = "done" if cur >= nb else "partial"
        if m:
            ok, n, cost = int(m.group(1)), int(m.group(2)), m.group(3)
            v["lines"].append(f"finished {clock(fin[0], now)}: {ok} of {n} agents wrote their report "
                              f"(cost ${cost}); {cur} of {nb} reports up to date")
        return v
    v["state"] = "stopped"
    v["reason"] = [KILLED]
    return v


def agents_progress(sec, v, now):
    total, par, fin, started, cost, mins = None, 3, 0, 0, 0.0, []
    for _t, msg in sec.stamped():
        m = re.match(r"Running (\d+) agents, (\d+) at a time", msg)
        if m:
            total, par = int(m.group(1)), int(m.group(2))
        if re.match(r"Agent \S+: started", msg):
            started += 1
        m = re.match(r"Agent \S+: \S+ in ([\d.]+) min, \d+ turns, \$([\d.]+)", msg)
        if m:
            fin += 1
            mins.append(float(m.group(1)))
            cost += float(m.group(2))
    if total is None:
        v["lines"].append("starting")
        return
    allx = total + 1                                    # + the overview
    v["lines"].append(f"{fin} of {allx} agents finished, {max(0, started - fin)} working now (cost so far ${cost:.2f})")
    per = (sum(mins) / len(mins)) if mins else EST["agent_round"]
    rest = max(0, total - fin)
    left = math.ceil(rest / max(par, 1)) * per + (EST["overview"] if fin <= total else 0)
    v["lines"].append(f"time left: about {max(1, round(left))} min")


# ---- the download
def download_view(ctx):
    d = ctx.data
    jf = ctx.jf["download"]
    v = {"job": "download", "state": "none", "lines": [], "reason": []}
    files = glob.glob(os.path.join(d, "data", "*.parquet"))
    have = len(files)
    exp = 0
    for f in files:
        m = re.search(r"-of-(\d+)\.parquet$", f)
        if m:
            exp = max(exp, int(m.group(1)))
    if not have:                    # another layout: the atlas's index knows the expression files
        idx = os.path.join(ctx.out["atlas"], "file_index.json")
        try:
            with open(idx, encoding="utf-8") as fh:
                have = len([f for f in json.load(fh).get("expression", []) if os.path.exists(f)])
        except (OSError, ValueError):
            pass
    exp = exp or EXPECTED_FILES
    meta = [os.path.basename(f) for f in glob.glob(os.path.join(d, "metadata", "**", "*.parquet"), recursive=True)]
    meta += [os.path.basename(f) for f in glob.glob(os.path.join(d, "*.parquet"))]
    nmeta = sum(any(m.startswith(t) for m in meta) for t in META_TABLES)
    partial = glob.glob(os.path.join(d, ".cache", "huggingface", "download", "**", "*.incomplete"), recursive=True)
    v.update(have=have, expected=exp, meta=nmeta)
    counts = f"{num(have)} of {num(exp)} expression files, {nmeta} of {len(META_TABLES)} metadata tables"
    pct = f"{num(have)} of {num(exp)} expression files ({100.0 * have / exp:.0f}%), {nmeta} of {len(META_TABLES)} " \
          "metadata tables"
    running = bool(ctx.procs.of("download")) or bool(jf["alive"])
    if running:
        v["state"] = "running"
        v["by"] = "tahoe" if jf["alive"] else "hand"
        v["since"] = jf["started"] if jf["alive"] else None
        v["lines"].append(pct)
        start_n = read_text(os.path.join(ctx.state, "download.startcount"))
        if jf["started"] and start_n and start_n.isdigit():
            rate = (have - int(start_n)) / max(ctx.now - jf["started"], 1.0)
            if rate > 0 and have < exp:
                left = dur((exp - have) / rate)
                v["lines"].append(f"time left: {'about ' if left[0].isdigit() else ''}{left} at the current speed")
        return v
    if jf["rc"] is not None and jf["rc"] != 0:
        if jf["how"] == "stopped":
            v["state"], v["reason"] = "stopped", [f"stopped with '{ctx.me} stop'"]
        else:
            v["state"], v["reason"] = "failed", [f"exit code {jf['rc']}"] + last_console_lines(jf["console"])
        v["lines"].append(counts)
        return v
    if have >= exp and nmeta == len(META_TABLES) and not partial:
        v["state"] = "done"
    elif have or nmeta:
        v["state"] = "incomplete"
    v["lines"].append(counts + (f"; {len(partial)} file(s) half-downloaded" if partial else ""))
    return v


# ============================================================================= what 'tahoe run' does
def expression_now(ctx):
    """The expression files of the download as it is now (real paths): data/*.parquet (the Hugging Face layout),
    else the atlas's file index (another layout); empty when unknown. Read once per run of this script."""
    if ctx._expr is None:
        files = glob.glob(os.path.join(ctx.data, "data", "*.parquet"))
        ctx._expr = {real(f) for f in files}
        if not files:
            try:
                with open(os.path.join(ctx.out["atlas"], "file_index.json"), encoding="utf-8") as fh:
                    ctx._expr = {real(f) for f in json.load(fh).get("expression", []) if os.path.exists(f)}
            except (OSError, ValueError, AttributeError):
                pass
    return ctx._expr


def atlas_built(ctx):
    """True when the atlas holds a finished build of exactly the expression files the download holds now
    (build_info.json written after every plate's files, a full run, not a --limit-files trial): then 'effects' and
    'angles' redo the analysis from it without reading the cells again."""
    o = ctx.out["atlas"]
    bi = os.path.join(o, "build_info.json")
    try:
        with open(bi, encoding="utf-8") as fh:
            info = json.load(fh)
    except (OSError, ValueError):
        return False
    if not isinstance(info, dict) or info.get("limit_files") or not os.path.exists(os.path.join(o, "sample_map.csv")):
        return False
    lists = glob.glob(os.path.join(o, "pseudobulk", "group*_files.txt"))
    if not lists or (isinstance(info.get("groups"), int) and len(lists) != info["groups"]):
        return False
    built = set()
    for f in lists:
        base = f[:-len("_files.txt")]
        outs = [base + s for s in ("_profiles.csv", "_barcodes.csv", "_samples.csv", ".npy")]
        if not all(os.path.exists(x) for x in outs) or max(mtime(x) for x in outs + [f]) > mtime(bi) + 1:
            return False                    # a plate missing, or rewritten by a later build that did not finish
        built |= {real(x.strip()) for x in (read_text(f, "") or "").splitlines() if x.strip()}
    now = expression_now(ctx)
    return bool(now) and built == now


def extract_complete(ctx, job):
    """True when the gene panel's (or the MTAP/Gankyrin trial's) folder holds a finished extract of every
    expression file the download holds now (not a --limit-files trial): then 'analyze' (minutes) redoes the
    analysis from it."""
    o = ctx.out[job]
    try:
        with open(os.path.join(o, "extract_info.json"), encoding="utf-8") as fh:
            info = json.load(fh)
    except (OSError, ValueError):
        return False
    if not isinstance(info, dict) or info.get("limit_files") or \
            not all(os.path.exists(os.path.join(o, f)) for f in ("well_line.parquet", "sample_map.csv")):
        return False
    if job == "panel" and ctx.panel_list_outdated():     # the extract predates the repo's genes: 'all' re-extracts
        return False
    now = expression_now(ctx)
    try:
        with open(os.path.join(o, "file_index.json"), encoding="utf-8") as fh:
            used = {real(f) for f in json.load(fh).get("expression", [])}
    except (OSError, ValueError, AttributeError):
        used = None
    if now and used is not None and used != now:
        return False
    return not now or info.get("n_files") == len(now)


def brief_refs(ctx, part):
    """{script path: [agent names]}: the absolute tahoe_*.py paths named in the agent briefs of `part` that the next
    'agents' run gives its agents (<out>/angles/*/brief.md without an up-to-date report). Their look-up commands
    run those files."""
    out = {}
    for b in sorted(glob.glob(os.path.join(ctx.out[part], "angles", "*", "brief.md"))):
        if ctx.report_current(part, b):
            continue
        name = os.path.basename(os.path.dirname(b))
        for m in SCRIPT_REF.finditer(read_text(b, "") or ""):
            p = next(g for g in m.groups() if g)
            if os.path.isabs(p) and name not in out.get(p, []):
                out.setdefault(p, []).append(name)
    return out


def brief_problems(ctx, part):
    """(missing, copies), each {path: [agent names]}: script paths in those briefs that no longer exist (a copy
    since deleted or moved: every look-up would fail), and ones outside the repo (copies, e.g. in the data folder:
    they must stay until the briefs are written again from the repo)."""
    refs = brief_refs(ctx, part)
    missing = {p: n for p, n in refs.items() if not os.path.exists(p)}
    copies = {p: n for p, n in refs.items() if p not in missing and real(os.path.dirname(p)) != real(REPO)}
    return missing, copies


def run_plan(ctx, V):
    """The steps 'tahoe run' starts, per part ([] = nothing to do: current, or running / queued). After an update
    of the method only what it needs: the atlas's 'effects' and 'angles' when its build is complete (else
    'compute'), only 'angles' when the effects are current; the gene panel's 'analyze' when its extract is complete
    (else 'all'). Finished parts whose briefs name a missing script or a copy outside the repo get their briefs
    written again ('angles' / 'analyze'); the gene panel also when it ran without the current atlas (unless its
    agents ran). mtap: what 'tahoe mtap' does for an outdated MTAP/Gankyrin trial ('tahoe run' leaves it alone)."""
    plan = {"atlas": [], "panel": [], "mtap": []}

    def busy(j):
        return V[j]["state"] in ("running", "queued")
    if not busy("atlas"):
        if ctx.ready("atlas"):
            if any(brief_problems(ctx, "atlas")):
                plan["atlas"] = ["angles"]
        elif os.path.exists(ctx.stamp("atlas")) and not ctx.outdated("atlas"):
            plan["atlas"] = ["angles"]                  # effects current, angles not run since
        elif atlas_built(ctx):
            plan["atlas"] = ["effects", "angles"]
        else:
            plan["atlas"] = ["compute"]
    if not busy("panel"):
        if ctx.ready("panel"):
            agents_ran = V["agents"]["panel"]["state"] in ("done", "partial")
            atlas_soon = ctx.ready("atlas") or bool(plan["atlas"]) or busy("atlas")
            if any(brief_problems(ctx, "panel")) or (not agents_ran and atlas_soon and panel_lacks_atlas(ctx)):
                plan["panel"] = ["analyze"]
        elif extract_complete(ctx, "panel"):
            plan["panel"] = ["analyze"]
        else:
            plan["panel"] = ["all"]
    if not busy("mtap") and ctx.ready("mtap") and ctx.outdated("mtap"):
        plan["mtap"] = ["analyze"] if extract_complete(ctx, "mtap") else ["all"]
    return plan


def plan_words(plan):
    """'the atlas effects and angles (its build is reused), then the gene panel's analysis'."""
    a, p = plan["atlas"], plan["panel"]
    bits = []
    if a == ["compute"]:
        bits.append("the atlas")
    elif a == ["effects", "angles"]:
        bits.append("the atlas effects and angles (its build is reused)")
    elif a:
        bits.append("the atlas angles")
    if p == ["all"]:
        bits.append("the gene panel")
    elif p:
        bits.append("the gene panel's analysis (its extract is reused)")
    return ", then ".join(bits)


# ============================================================================= the screen
def collect(ctx):
    V = {"download": download_view(ctx), "atlas": atlas_view(ctx), "panel": extract_view(ctx, "panel"),
         "mtap": extract_view(ctx, "mtap")}
    V["agents"] = {"atlas": agents_part(ctx, "atlas"), "panel": agents_part(ctx, "panel")}
    ctx.V = V
    return V


def doomed(ctx, V, job):
    """'<the atlas>, which FAILED' when a run this queued job waits for (<state>/<job>.after) ended badly: the job
    will then not start (see cmd_gate); else None."""
    for j in ctx.jf[job]["after"]:
        if j not in DEPS.get(job, []) or j not in V:
            continue
        s = V[j]["state"]
        if s in ("running", "queued"):
            continue
        ok = s == "done" if j == "download" else s in ("done", "partial", "outdated")
        if not ok:
            word = {"failed": "FAILED", "stopped": "stopped without finishing", "skipped": "did not start either",
                    "incomplete": "is incomplete"}.get(s, "did not run")
            return f"{NAME[j]}, which {word}"
    return None


def waits_for(ctx, job):
    """What a queued job waits for, in words."""
    b = blockers(ctx, job)
    return " and ".join(NAME[x] for x in b) if b else "its turn"


def head_line(ctx, v, job):
    now = ctx.now
    s = v["state"]
    if s == "running":
        by = {"hand": ", started by hand", "tahoe": ""}.get(v.get("by"), "")
        since = v.get("since")
        return "RUNNING" + (f" since {clock(since, now)} ({dur(now - since)})" if since else "") + by
    if s == "queued":
        why = doomed(ctx, ctx.V, job) if ctx.V else None
        if why:
            return f"queued, but it will not start: it waited for {why}"
        b = blockers(ctx, job)
        if not b:
            return "queued: starts in a moment"
        return f"queued: starts by itself when {waits_for(ctx, job)} " + ("finish" if len(b) > 1 else "finishes")
    if s == "done":
        return "done" + v.get("at", "")
    if s == "partial":
        return "partly done" + v.get("at", "").replace(" at ", ": finished at ", 1)
    if s == "outdated":
        if panel_gene_list_outdated(ctx, job):
            return "done, but outdated (new genes in the panel)"
        want = ctx.version(job)[1]
        return "done, but outdated" + (f" (method v{want})" if want else "")
    if s == "skipped":                  # (once what it waited for is fine again, that reason is history)
        return f"not started: it waited for {v.get('waited')}" if ctx.V is None or doomed(ctx, ctx.V, job) \
            else "not started"
    if s == "failed":
        return "FAILED"
    if s == "stopped":
        return "STOPPED"
    if s == "incomplete":
        return "incomplete"
    if s == "dry":
        return "not run yet"
    return "not started"


def stale_copies(ctx):
    """Copies of the scripts in the data folder that differ from the repo's (tahoe runs the repo's)."""
    if real(REPO) == ctx.data:
        return []
    out = []
    for n in SCRIPTS:
        a, b = os.path.join(ctx.data, n), os.path.join(REPO, n)
        try:
            if os.path.isfile(a) and os.path.isfile(b) and not filecmp.cmp(a, b, shallow=False):
                out.append(n)
        except OSError:
            continue
    return out


def render(ctx, V, out=sys.stdout):
    width = max(60, min(shutil.get_terminal_size((80, 24)).columns, 120))
    pad = " " * 14

    def say(label, text, indent="", max_lines=2):
        """One item, wrapped onto lines indented 14 columns (never cut off at the window's edge)."""
        avail = width - 1 - len(pad)
        rows = textwrap.wrap(home_tilde(text), avail, initial_indent=indent, subsequent_indent=indent + "  ",
                             break_on_hyphens=False) or [""]
        if len(rows) > max_lines:
            rows = rows[:max_lines]
            rows[-1] = rows[-1][:avail - 4].rstrip() + " ..."
        for i, r in enumerate(rows):
            print(((f"{label:<14}" if label else pad) if i == 0 else pad) + r, file=out)

    def note(text):
        for r in textwrap.wrap(home_tilde(text), width - 1, subsequent_indent="  ", break_on_hyphens=False):
            print(r, file=out)

    now = ctx.now
    print(f"Tahoe-100M status  {tilde(ctx.data)}  ({time.strftime('%a %d %b %H:%M', time.localtime(now))})",
          file=out)
    if not os.path.isdir(ctx.data):
        print(f"\nThe data folder {tilde(ctx.data)} does not exist yet.", file=out)
        print(f"Next: {ctx.me} download   (or point TAHOE_DATA at your Tahoe-100M folder)", file=out)
        return
    if not getattr(ctx.args, "have_venv", 1):
        note(f"(Python environment {tilde(ctx.args.venv or '~/tahoe-venv')} not found: using {sys.executable}; "
             f"'{ctx.me} setup' creates it)")
    if not ctx.procs.ok:
        note("(The process list (ps) could not be read: runs going on may be missing below.)")
    print(file=out)
    for job in ("download", "atlas", "panel", "mtap"):
        v = V[job]
        if job == "mtap" and v["state"] == "none" and not os.path.isdir(ctx.out["mtap"]) \
                and not ctx.jf["mtap"]["alive"] and ctx.jf["mtap"]["rc"] is None:
            continue
        if job == "download":
            say(LABEL[job], head_line(ctx, v, job) + (": " + v["lines"][0] if v["lines"] else ""))
            rest = v["lines"][1:]
        else:
            say(LABEL[job], head_line(ctx, v, job))
            rest = v["lines"]
        for x in rest:
            say("", x)
        if v.get("also_queued"):
            say("", "also queued: another run of it starts when this one has finished")
        for x in v["reason"]:
            say("", x, max_lines=4)
        if v["state"] in ("running", "failed", "stopped") and job != "download":
            sec = v.get("sec")
            last = sec.last(ADVISORY) if sec is not None and sec.ok and not v.get("starting") else None
            if v["state"] == "running" and v.get("starting"):
                step = (ctx.jf[job]["step"] or "") if v.get("by") == "tahoe" else ""
                say("", "now: " + ("checking the setup (quick)" if step == "check" else "starting"))
            elif last and v["state"] == "running":
                say("", f"last line ({time.strftime('%H:%M:%S', time.localtime(last[0]))}): {last[1].strip()}")
        if job == "download" and v["state"] == "running":
            tail = last_console_lines(ctx.jf["download"]["console"], 1)
            if tail:
                say("", "last line: " + tail[-1])
    A = V["agents"]
    first = True
    for part in ("atlas", "panel"):
        a = A[part]
        if a["state"] == "none" and not a["lines"]:
            continue
        text = f"{'atlas' if part == 'atlas' else 'gene panel'}: " + agent_head(ctx, a)
        say(LABEL["agents"] if first else "", text)
        first = False
        for x in a["lines"]:
            say("", x, indent="  ")
        for x in a["reason"]:
            say("", x, indent="  ", max_lines=4)
        if a["state"] == "running" and a["sec"].ok and a["sec"].last():
            t, msg = a["sec"].last()
            say("", f"last line ({time.strftime('%H:%M:%S', time.localtime(t))}): {msg.strip()}", indent="  ")
    if first:
        say(LABEL["agents"], "not started")
    print(file=out)
    named = sorted({tilde(os.path.dirname(p)) for part in ("atlas", "panel") for p in brief_problems(ctx, part)[1]})
    if named:                           # agents still to run would call those copies: they must stay for now
        note(f"(The agent briefs name the scripts in {', '.join(named)}, not {tilde(REPO)}: keep those copies "
             f"until '{ctx.me} run' has written the briefs again from {tilde(REPO)}; then they may be deleted.)")
    else:
        stale = stale_copies(ctx)
        if stale:
            note(f"(Your copies in {tilde(ctx.data)} differ from {tilde(REPO)}, which {ctx.me} runs, and no agent "
                 f"brief names them. Once no run started by hand uses them, they may be deleted: "
                 f"cd {tilde(ctx.data)} && rm {' '.join(stale)})")
    if ctx.me != "tahoe":
        note(f"(Tip: '{ctx.me} setup' once, and plain 'tahoe' works from any folder.)")
    note("Next: " + next_step(ctx, V))


def agent_head(ctx, a):
    s = a["state"]
    if s == "running":
        return "RUNNING" + (", started by hand" if a.get("by") == "hand" else "")
    if s == "queued":
        return "queued (after the atlas agents)" if a["part"] == "panel" else "queued"
    return {"done": "done", "partial": "partly done", "failed": "FAILED", "stopped": "STOPPED",
            "dry": "not run yet", "none": "not started"}.get(s, s)


def bundle_fresh(ctx):
    z = os.path.join(ctx.data, "tahoe_bundles.zip")
    if not os.path.exists(z):
        return False
    src = [os.path.join(ctx.out["atlas"], "effects", "complete.json"),
           os.path.join(ctx.out["panel"], "results", "summary.txt")]
    src += glob.glob(os.path.join(ctx.out["atlas"], "reports", "*.md"))
    src += glob.glob(os.path.join(ctx.out["panel"], "reports", "*.md"))
    return mtime(z) >= max([mtime(f) for f in src] + [0])


def next_step(ctx, V):
    me = ctx.me
    st = {j: V[j]["state"] for j in ("download", "atlas", "panel", "mtap")}
    ag = {p: V["agents"][p]["state"] for p in ("atlas", "panel")}
    run = [j for j in ("download", "atlas", "panel", "mtap") if st[j] == "running"]
    agents_run = [p for p in ag if ag[p] == "running"]
    queued = [j for j in ("atlas", "panel", "mtap") if st[j] == "queued" and not doomed(ctx, V, j)]
    queued.sort(key=lambda j: (ctx.jf[j]["seq"] or 0, j))
    bad = [j for j in ("atlas", "mtap", "panel") if st[j] == "failed"]
    if st["download"] == "running":
        return f"nothing to type: the download goes on by itself ('{me} log download' to watch); then: {me} run"
    if (run or queued) and bad:                 # a failure first: the queue does not hide it
        going = NAME[run[0]] if run else NAME[queued[0]]
        return f"{NAME[bad[0]]} FAILED: '{me} log {bad[0]}' shows why ({going} goes on meanwhile)"
    if run or queued:
        if "atlas" in run and st["panel"] not in ("queued", "running") and not ctx.ready("panel"):
            return f"type '{me} panel' now - it starts by itself when the atlas finishes"
        then = [NAME[j] for j in queued]
        if not run:
            return f"nothing to type: {then[0]} starts in a moment ('{me} status' to check)"
        if not then:
            return f"nothing to type: {NAME[run[0]]} is running ('{me} log' to watch; safe to log out)"
        return f"nothing to type: {NAME[run[0]]} runs, then {', then '.join(then)} " + \
            ("starts by itself" if len(then) == 1 else "follow by themselves") + f" ('{me} log' to watch)"
    if agents_run or "queued" in ag.values():
        return f"nothing to type: the agents are running ('{me} log' to watch; safe to log out)"
    if bad:
        j = bad[0]
        again = f"{me} run" if j == "atlas" and not ctx.ready("panel") else f"{me} {j}"
        extra = f" (or '{me} panel' for the gene panel without it)" if j == "mtap" and st["panel"] == "skipped" \
            else ""
        return f"'{me} log {j}' shows the error; fix it, then type '{again}' again (finished work is reused){extra}"
    if st["download"] == "failed":
        return f"'{me} log download' shows the error; then type '{me} download' again (it resumes)"
    if st["download"] in ("none", "incomplete") and not ctx.ready("atlas"):
        return (f"{me} setup, then {me} download" if not getattr(ctx.args, "have_venv", 1)
                else f"{me} download" + ("   (it resumes)" if st["download"] == "incomplete" else ""))
    if not getattr(ctx.args, "have_venv", 1):
        return f"{me} setup   (one time: the Python environment the scripts run in)"
    plan = run_plan(ctx, V)
    old = [j for j in ("atlas", "panel") if st[j] == "outdated"]
    if old:                             # e.g. after 'tahoe update' brought a new method or new genes: one command
        method = [j for j in old if not panel_gene_list_outdated(ctx, j)]   # redoes it
        want = max((ctx.version(j)[1] or 0 for j in method), default=0)
        why = f"method v{want}" if method else "new genes in the panel"
        fast = plan["atlas"] != ["compute"] and plan["panel"] != ["all"]
        return f"{me} run   ({why}: {plan_words(plan) or 'what is out of date'}; " + \
            ("minutes: the cells are not read again; " if fast else "") + "safe to log out)"
    if not ctx.ready("atlas"):
        cmd = f"{me} run" if not ctx.ready("panel") else f"{me} atlas"
        if st["atlas"] in ("stopped", "partial"):
            return f"{cmd}   (continues where it stopped: finished work is reused)"
        return f"{cmd}   (" + ("the atlas, then the gene panel; " if not ctx.ready("panel") else "") + \
            "safe to log out)"
    if not ctx.ready("panel"):
        if st["panel"] in ("stopped", "partial"):
            return f"{me} panel   (continues where it stopped: finished work is reused)"
        if plan["panel"] == ["analyze"]:
            return f"{me} panel   (minutes: its analysis; the extracted cells are reused)"
        return f"{me} panel   (in the background; safe to log out)"
    panel_agents = ag["panel"] in ("done", "partial")
    if panel_compare(ctx) == "newer" and not panel_agents:
        return f"{me} panel analyze   (minutes: adds the comparison with the MTAP/Gankyrin trial)"
    if panel_lacks_atlas(ctx) and not panel_agents:
        return f"{me} panel analyze   (minutes: the gene panel's analysis with the current atlas: its look-ups, " \
            "composition shift and plate factors)"
    for part in ("atlas", "panel"):     # briefs whose look-ups would call a deleted script, or a copy
        missing, copies = brief_problems(ctx, part)
        if missing or copies:
            p = next(iter(missing or copies))
            why = f"they name {tilde(p)}, which no longer exists" if missing else f"they name the copy {tilde(p)}"
            return f"{me} run   (minutes: writes the {'atlas' if part == 'atlas' else 'gene panel'} agent briefs " \
                f"again from {tilde(REPO)}; {why})"
    for p in ("atlas", "panel"):
        if ag[p] == "failed":
            return f"'{me} log agents' shows the error; fix it, then '{me} agents {p}' (finished reports are kept)"
        if ag[p] == "stopped":
            return f"{me} agents {p}   (when you want them to go on; finished reports are kept)"
    real_run = {p: ag[p] in ("done", "partial") for p in ag}
    if not any(real_run.values()):
        if not bundle_fresh(ctx):
            return f"{me} bundle   (then upload the zip to Claude to check the numbers)"
        return f"upload tahoe_bundles.zip to Claude; once it has checked the numbers: {me} agents"
    for p in ("atlas", "panel"):
        if not real_run[p]:
            return f"{me} agents {p}"
        if ag[p] == "partial":
            return f"{me} agents {p}   (reruns only the missing reports)"
    if not bundle_fresh(ctx):
        return f"{me} bundle   (the zip now holds the reports: upload it to Claude)"
    return "all done: upload tahoe_bundles.zip to Claude to turn the reports into docs"


# ============================================================================= helpers for 'tahoe'
def blockers(ctx, job, runner=None):
    """Jobs that keep `job` (queued) from starting: anything running (also a run of the same job started by hand),
    or queued ahead of it. `runner` = the pid of the asking job's own runner (default: every runner of `job`)."""
    me = ctx.jf.get(job, {})
    own = {runner} if runner else set(me.get("alive") or [])
    out = []
    for f in ctx.procs.found:
        if f["kind"] == "proc" and ctx.procs.runner_pid(f["pid"]) not in own:
            out.append(f["job"])
    lock = read_text(os.path.join(ctx.state, f"{job}.lock", "pid"), "")
    for j in JOBS:
        jf = ctx.jf[j]
        alive = [p for p in jf["alive"] if p not in own]
        if not alive:
            continue
        if j == job:            # another runner of this job: only the one holding the job's lock goes on
            if lock.isdigit() and int(lock) in alive:
                out.append(j)
            continue
        if jf["queued"] is None:
            out.append(j)
        elif me.get("seq") is not None and jf["seq"] is not None and (jf["seq"], j) < (me["seq"], job):
            out.append(j)
    return list(dict.fromkeys(out))


def cmd_gate(ctx, job):
    """For a queued job whose wait is over: did the runs it waited for (<state>/<job>.after) end well?
    Exit 0 = start; 3 = do not start (prints '<the atlas>, which FAILED'); 4 = still going: wait on; 2 = unknown."""
    if not ctx.procs.ok:
        sys.exit(2)
    after = [j for j in ctx.jf[job]["after"] if j in DEPS.get(job, [])]
    if not after:
        return
    V = collect(ctx)
    if any(V[j]["state"] in ("running", "queued") for j in after):
        sys.exit(4)
    why = doomed(ctx, V, job)
    if why:
        print(why)
        sys.exit(3)


def took(ctx, job):
    """Minutes the latest full run of `job` took here (from its log), or None."""
    for s in reversed(all_sections(ctx.logpath(job))):
        if job == "atlas":
            if s.command != "compute" or any(re.match(r"\s+\S+ already built \(", m) for _t, m in s.stamped()):
                continue
            hit = s.find("Computation done")
        else:
            if s.command != "all" or not any(re.match(r"[\d,]+ expression files \(0 already done\)", m)
                                             for _t, m in s.stamped()):
                continue
            hit = s.find("Analysis done") or s.find("Done. Start with")
        if hit:
            return max(1, round((hit[0] - s.start) / 60.0))
    return None


def cmd_facts(ctx):
    V = collect(ctx)
    p = []
    for j in ("download", "atlas", "panel", "mtap"):
        p.append(f"{j}={V[j]['state']}")
        p.append(f"{j}_by={V[j].get('by') or ''}")
        if j != "download":
            p.append(f"{j}_ready={int(ctx.ready(j))}")
            since = V[j].get("since")
            p.append(f"{j}_since={clock(since, ctx.now) if since else ''}")
    p.append(f"download_have={V['download']['have']}")
    p.append(f"download_expected={V['download']['expected']}")
    for part in ("atlas", "panel"):
        p.append(f"agents_{part}={V['agents'][part]['state']}")
    running = [j for j in ("download", "atlas", "panel", "mtap") if V[j]["state"] == "running"]
    if any(V["agents"][x]["state"] == "running" for x in V["agents"]) or \
            (ctx.jf["agents"]["alive"] and ctx.jf["agents"]["queued"] is None):
        running.append("agents")
    queued = [j for j in JOBS if ctx.jf[j]["alive"] and ctx.jf[j]["queued"] is not None]
    p.append("running=" + " ".join(running))
    p.append("queued=" + " ".join(queued))
    seqs = [ctx.jf[j]["seq"] for j in queued if ctx.jf[j]["seq"] is not None]
    p.append(f"queue_last={max(seqs) if seqs else 0}")
    p.append(f"panel_seq={ctx.jf['panel']['seq'] or 0}")
    p.append(f"atlas_took={took(ctx, 'atlas') or ''}")
    p.append(f"panel_took={took(ctx, 'panel') or ''}")
    p.append(f"panel_lacks_atlas={int(ctx.ready('panel') and panel_lacks_atlas(ctx))}")
    plan = run_plan(ctx, V)                     # what 'tahoe run' / 'tahoe atlas' / 'tahoe panel' start
    for j in ("atlas", "panel", "mtap"):
        p.append(f"{j}_plan={' '.join(plan[j])}")
        p.append(f"{j}_outdated={int(ctx.outdated(j))}")
    # for 'Started: ...': the earlier runs in each log, the latest one included (an empty Section skips none)
    est = atlas_estimates(Section(ctx.logpath("atlas"), rows=[]))
    x, how = est["effects"][0] + est["angles"][0], est["effects"][1]
    p.append("atlas_redo=" + (f"the effects and angles took {fmt_min(x, how)} here last time" if how == "last"
                              else fmt_min(x, how)))
    an = extract_history(Section(ctx.logpath("panel"), rows=[]), "panel").get("analyze")
    p.append("panel_analyze=" + (f"the analysis took {fmt_min(an, 'last')} here last time" if an else "a few minutes"))
    p.append(f"ps_ok={int(ctx.procs.ok)}")
    print("\n".join(p))
    if not ctx.procs.ok:
        sys.exit(2)


def cmd_briefcheck(ctx, parts):
    """'tahoe agents' preflight: one line '<part>\\t<path>\\t<agents>' per script path that the briefs of the
    agents still to run name and that no longer exists (their look-ups would fail; 'tahoe run' writes them again)."""
    for part in parts.split():
        if part in ("atlas", "panel"):
            for path, names in brief_problems(ctx, part)[0].items():
                print(f"{part}\t{path}\t{', '.join(names[:3])}" + (f" and {len(names) - 3} more" if len(names) > 3
                                                                    else ""))


def cmd_stopinfo(ctx, job):
    """What 'tahoe stop JOB' kills: 'runner PID', 'proc PID LOG' (a script run, also one started by hand), and
    'child PID' (their worker processes)."""
    rows, roots = [], []
    for f in ctx.procs.of(job, "runner"):
        rows.append(f"runner {f['pid']} {'queued' if ctx.jf[job]['queued'] is not None else 'running'}")
        roots.append(f["pid"])
    for f in ctx.procs.of(job):
        part = f.get("part")
        log = ctx.logpath(job, part) if job != "download" else ""
        rows.append(f"proc {f['pid']} {log}")
        roots.append(f["pid"])
    for c in ctx.procs.descendants(roots):
        rows.append(f"child {c}")
    print("\n".join(rows))


def cmd_logfile(ctx, job):
    """The log to follow: the job's own log (the console output when the job failed before its log began)."""
    V = None
    if not job:
        V = collect(ctx)
        order = ["download", "atlas", "panel", "mtap"]
        for j in order:
            if V[j]["state"] == "running":
                job = j
                break
        else:
            if any(V["agents"][p]["state"] == "running" for p in V["agents"]) or ctx.jf["agents"]["alive"]:
                job = "agents"
            else:
                cands = [(mtime(ctx.logpath(j)), j) for j in ("atlas", "panel", "mtap")]
                cands += [(mtime(os.path.join(ctx.out[p], "agents.log")), "agents") for p in ("atlas", "panel")]
                cands += [(mtime(ctx.jf["download"]["console"]), "download")]
                cands.sort()
                job = cands[-1][1] if cands[-1][0] else "atlas"
    if job == "agents":
        V = V or collect(ctx)
        run = [p for p in ("atlas", "panel") if V["agents"][p]["state"] == "running"]
        part = run[0] if run else max(("atlas", "panel"), key=lambda p: mtime(os.path.join(ctx.out[p], "agents.log")))
        if not run and ctx.jf["agents"]["alive"] and ctx.jf["agents"]["step"] in ("atlas", "panel"):
            part = ctx.jf["agents"]["step"]
        path = os.path.join(ctx.out[part], "agents.log")
    else:
        path = ctx.logpath(job)
    jf = ctx.jf[job]
    sec = Section(path) if job != "download" else None
    if jf["rc"] not in (None, 0) and jf["how"] != "stopped" and os.path.exists(jf["console"]) and \
            (sec is None or not sec.ok or (sec.start or 0) < (jf["started"] or 0) - 5):
        path = jf["console"]
    print(f"{job} {path}")


def cmd_zip(out, files):
    tmp = out + ".tmp"
    n = 0
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_STORED) as z:     # the bundles are compressed already
        for f in files:
            if os.path.isfile(f):
                z.write(f, os.path.basename(f))
                n += 1
    if not n:
        os.remove(tmp)
        sys.exit(1)
    os.replace(tmp, out)
    print(f"{os.path.getsize(out) / 1e6:.1f} MB")


def cmd_smoke(results, rc, log):
    try:
        with open(results, encoding="utf-8") as fh:
            r = json.load(fh)
    except (OSError, ValueError):
        tail = last_console_lines(log, 2)
        print(f"Test did not finish (exit {rc}): {' | '.join(tail) or 'no output'}. Details: {tilde(log)}")
        return
    if mtime(results) < mtime(log) - 3600:
        print(f"Test did not finish (exit {rc}). Details: {tilde(log)}")
        return
    c = r.get("counts", {})
    secs = r.get("seconds_total", 0)
    if c.get("FAIL"):
        fails = [x for x in r.get("results", []) if x.get("status") == "FAIL"]
        first = f"{fails[0]['stage']}: {fails[0]['check']}" if fails else ""
        print(f"Test FAILED: {c.get('FAIL')} of {sum(c.values())} checks failed (first: {first}). "
              f"Details: {tilde(log)}")
    else:
        print(f"Test passed: {c.get('PASS', 0)} checks PASS, 0 FAIL" + (f", {c['WARN']} WARN" if c.get("WARN") else "")
              + f" ({dur(secs)}). Details: {tilde(log)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["status", "next", "facts", "blockers", "gate", "stopinfo", "logfile",
                                            "briefcheck", "zip", "smoke"])
    ap.add_argument("rest", nargs="*", help="zip: OUT FILE...; smoke: RESULTS.json EXIT_CODE LOG")
    ap.add_argument("--data", default=os.environ.get("TAHOE_DATA") or "~/Tahoe-100M", help="the data folder")
    ap.add_argument("--state", default=None, help="the job files of 'tahoe' (default: <data>/.tahoe)")
    ap.add_argument("--atlas-out", default=None, help="atlas output folder (default: <data>/atlas)")
    ap.add_argument("--panel-out", default=None, help="gene panel output folder (default: <data>/gene_panel)")
    ap.add_argument("--mtap-out", default=None, help="MTAP/Gankyrin output folder (default: <data>/mtap_gankyrin)")
    ap.add_argument("--job", default="", help="blockers / gate / stopinfo / logfile: the job; briefcheck: the "
                                              "parts ('atlas panel')")
    ap.add_argument("--runner", type=int, default=None, help="blockers: the pid of the asking job's runner")
    ap.add_argument("--me", default="tahoe", help="how the user calls the 'tahoe' command (for the Next line)")
    ap.add_argument("--venv", default=None, help="the Python environment folder (for messages)")
    ap.add_argument("--have-venv", type=int, default=1, help="0 when that environment is missing")
    args = ap.parse_args()
    if args.command == "zip":
        if len(args.rest) < 2:
            sys.exit("usage: tahoe_status.py zip OUT FILE...")
        return cmd_zip(args.rest[0], args.rest[1:])
    if args.command == "smoke":
        if len(args.rest) < 3:
            sys.exit("usage: tahoe_status.py smoke RESULTS.json EXIT_CODE LOG")
        return cmd_smoke(*args.rest[:3])
    ctx = Ctx(args)
    if args.command == "status":
        render(ctx, collect(ctx))
    elif args.command == "next":
        print(next_step(ctx, collect(ctx)))
    elif args.command == "facts":
        cmd_facts(ctx)
    elif args.command == "blockers":
        if not ctx.procs.ok:                    # what runs is unknown: never say 'nothing'
            sys.exit(2)
        print(" ".join(blockers(ctx, args.job, args.runner)))
    elif args.command == "gate":
        cmd_gate(ctx, args.job)
    elif args.command == "stopinfo":
        cmd_stopinfo(ctx, args.job)
    elif args.command == "logfile":
        cmd_logfile(ctx, args.job)
    elif args.command == "briefcheck":
        cmd_briefcheck(ctx, args.job)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:                     # 'tahoe status | head': the reader left early
        try:
            sys.stdout = open(os.devnull, "w")
        except OSError:
            pass
        sys.exit(0)
