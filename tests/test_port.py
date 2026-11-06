#!/usr/bin/env python3
"""test_port.py - prove that tahoemap/atlas_core.py and tahoemap/tlib.py are still the old method, verbatim.

    python3 tests/test_port.py                      # takes the old scripts from git (commit 28cd834)
    python3 tests/test_port.py --old /path/to/old   # or from a checkout of the old branch

Re-runs tools/port_from_old.py on the old tahoe_atlas.py / tahoe_mtap_gankyrin.py and compares the result with the
committed modules character for character. Any hand edit of a ported function makes this fail.
"""

import argparse
import filecmp
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
OLD_COMMIT = "28cd834"
FILES = ("tahoe_atlas.py", "tahoe_mtap_gankyrin.py")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", default=None, help="folder holding the old tahoe_atlas.py and tahoe_mtap_gankyrin.py")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        old = a.old
        if old is None:
            old = os.path.join(tmp, "old")
            os.makedirs(old)
            for f in FILES:
                r = subprocess.run(["git", "-C", REPO, "show", f"{OLD_COMMIT}:{f}"], capture_output=True)
                if r.returncode:
                    sys.exit(f"cannot read {f} at {OLD_COMMIT} from git (fetch the old branch, or pass --old): "
                             + r.stderr.decode(errors="replace").strip())
                with open(os.path.join(old, f), "wb") as fh:
                    fh.write(r.stdout)
        out = os.path.join(tmp, "pkg")
        subprocess.run([sys.executable, os.path.join(REPO, "tools", "port_from_old.py"), old, out], check=True,
                       capture_output=True)
        bad = [f for f in ("atlas_core.py", "tlib.py", "PORT_MANIFEST.tsv")
               if not filecmp.cmp(os.path.join(out, f), os.path.join(REPO, "tahoemap", f), shallow=False)]
    if bad:
        print("FAIL: differs from a fresh port of the old scripts:", ", ".join(bad))
        sys.exit(1)
    print("PASS: atlas_core.py, tlib.py and PORT_MANIFEST.tsv are a verbatim port of the old method")


if __name__ == "__main__":
    main()
