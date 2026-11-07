#!/usr/bin/env python3
"""test_port.py - prove that tahoemap/atlas_core.py and tahoemap/tlib.py are still the old method, verbatim.

    python3 tests/test_port.py                      # takes the old scripts from git (commit 28cd834)
    python3 tests/test_port.py --old /path/to/old   # or from a checkout of the old branch
    TAHOE_GIT=C:\\path\\to\\git.exe python tests\\test_port.py   # git not on PATH (e.g. a portable MinGit)

Re-runs tools/port_from_old.py on the old tahoe_atlas.py / tahoe_mtap_gankyrin.py and compares the result with the
committed modules character for character (line endings aside: a checkout with Windows CRLF line endings is the same
text). Any hand edit of a ported function makes this fail.
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OLD_COMMIT = "28cd834"
FILES = ("tahoe_atlas.py", "tahoe_mtap_gankyrin.py")


def find_git():
    """git: $TAHOE_GIT, then PATH, then the usual Git for Windows places; None when there is none."""
    env = os.environ.get("TAHOE_GIT")
    if env:
        return env
    g = shutil.which("git")
    if g:
        return g
    if os.name == "nt":
        roots = [os.environ.get(v) for v in ("ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA")]
        cands = [os.path.join(r, *p) for r in roots if r for p in (("Git", "cmd", "git.exe"),
                                                                  ("Programs", "Git", "cmd", "git.exe"))]
        cands.append(os.path.join(os.path.dirname(REPO), "mingit", "cmd", "git.exe"))   # a MinGit next to the repo
        for c in cands:
            if os.path.isfile(c):
                return c
    return None


def same_text(a, b):
    """The two files hold the same text, CRLF and LF line endings counted as equal."""
    with open(a, "rb") as fa, open(b, "rb") as fb:
        return fa.read().replace(b"\r\n", b"\n") == fb.read().replace(b"\r\n", b"\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", default=None, help="folder holding the old tahoe_atlas.py and tahoe_mtap_gankyrin.py")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        old = a.old
        if old is None:
            git = find_git()
            if git is None:
                sys.exit("cannot find git (not on PATH): install Git, set TAHOE_GIT to git.exe, or pass --old with "
                         "a checkout of the old scripts")
            old = os.path.join(tmp, "old")
            os.makedirs(old)
            for f in FILES:
                r = subprocess.run([git, "-C", REPO, "show", f"{OLD_COMMIT}:{f}"], capture_output=True)
                if r.returncode:
                    sys.exit(f"cannot read {f} at {OLD_COMMIT} from git (fetch the old branch, or pass --old): "
                             + r.stderr.decode(errors="replace").strip())
                with open(os.path.join(old, f), "wb") as fh:
                    fh.write(r.stdout)
        out = os.path.join(tmp, "pkg")
        subprocess.run([sys.executable, os.path.join(REPO, "tools", "port_from_old.py"), old, out], check=True,
                       capture_output=True)
        bad = [f for f in ("atlas_core.py", "tlib.py", "PORT_MANIFEST.tsv")
               if not same_text(os.path.join(out, f), os.path.join(REPO, "tahoemap", f))]
    if bad:
        print("FAIL: differs from a fresh port of the old scripts:", ", ".join(bad))
        sys.exit(1)
    print("PASS: atlas_core.py, tlib.py and PORT_MANIFEST.tsv are a verbatim port of the old method")


if __name__ == "__main__":
    main()
