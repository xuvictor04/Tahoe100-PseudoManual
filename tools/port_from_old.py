#!/usr/bin/env python3
"""Port the build + method-v3 effects from the old scripts, verbatim, by syntax tree.

    python3 port.py OLD_REPO OUT_PKG_DIR

Writes OUT_PKG_DIR/tlib.py (the needed part of tahoe_mtap_gankyrin.py) and OUT_PKG_DIR/atlas_core.py (the needed part
of tahoe_atlas.py). Every function and constant is copied character for character, in its original order; only the
module header (imports) is new. The closure starts from the build and effects entry points and follows every name.
"""
import ast
import hashlib
import os
import sys

OLD, OUT = sys.argv[1], sys.argv[2]
A_SRC = open(os.path.join(OLD, "tahoe_atlas.py"), encoding="utf-8").read()
T_SRC = open(os.path.join(OLD, "tahoe_mtap_gankyrin.py"), encoding="utf-8").read()

A_ROOTS = ["cmd_build", "cmd_effects", "_build_group", "_file_plate", "EFFECTS_README", "FX", "flags_for",
           "gene_flags", "has_artifact", "ARTIFACT_FLAGS", "dose_shape", "NOISE_RNA_RE", "norm_sf", "robust_z",
           "spearman", "signif", "gene_flag_col", "position_flag", "drug_best_dose", "TOP", "N_PCS"]
T_ROOTS = ["start_run_log", "log_exit", "safe_console", "keep_awake", "py_cmd", "salt_base", "bh",
           "robust_center_scale", "null_threshold", "MIN_CELLS", "LFC_MIN", "MIN_LINES", "METHOD_VERSION",
           "POS_CLEAN_Z", "PLATE_SCALE_MIN_WELLS", "COMPOSITION_FLAG", "NULL_FRAC", "dose_text", "mark_unreliable"]


def top_defs(src):
    tree = ast.parse(src)
    d = {}
    order = []
    for node in tree.body:
        names = []
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            names = [node.name]
        elif isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            names += [e.id for t in node.targets if isinstance(t, ast.Tuple) for e in t.elts if isinstance(e, ast.Name)]
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names = [node.target.id]
        elif isinstance(node, ast.Try):           # e.g. the scipy / pure-Python fallback block of norm_sf
            for sub in ast.walk(node):
                if isinstance(sub, (ast.FunctionDef, ast.ClassDef)):
                    names.append(sub.name)
                elif isinstance(sub, ast.Assign):
                    names += [t.id for t in sub.targets if isinstance(t, ast.Name)]
        for n in names:
            d[n] = node
        if names:
            order.append(node)
    return tree, d, order


def refs(node):
    names, tnames = set(), set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            names.add(n.id)
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "T":
            tnames.add(n.attr)
    return names, tnames


_, DA, OA = top_defs(A_SRC)
_, DT, OT = top_defs(T_SRC)
need = {"A": set(), "T": set()}
stack = [("A", x) for x in A_ROOTS] + [("T", x) for x in T_ROOTS]
while stack:
    mod, name = stack.pop()
    D = DA if mod == "A" else DT
    if name not in D:
        continue
    node = D[name]
    if id(node) in need[mod]:
        continue
    need[mod].add(id(node))
    names, tn = refs(node)
    for n in names:
        if n in D:
            stack.append((mod, n))
    for n in tn:
        stack.append(("T", n))

# A's own 'log = T.log' is kept (it is in the closure as a name); A's 'HERE' and import guard are replaced.
SKIP_A = {"HERE"}


def node_name(node):
    if hasattr(node, "name"):
        return node.name
    if isinstance(node, ast.Assign):
        t = node.targets[0]
        return t.id if isinstance(t, ast.Name) else ",".join(e.id for e in t.elts)
    if isinstance(node, ast.Try):
        return "try:" + ",".join(sub.name for sub in ast.walk(node) if isinstance(sub, ast.FunctionDef))
    return "?"


def segment(src, node):
    lines = src.splitlines(keepends=True)
    start = node.lineno
    # keep decorators and the comment block directly above
    if getattr(node, "decorator_list", None):
        start = min([d.lineno for d in node.decorator_list] + [start])
    return "".join(lines[start - 1:node.end_lineno])


def emit(src, order, ids, skip=()):
    out, seen = [], set()
    for node in order:
        if id(node) not in ids or id(node) in seen:
            continue
        seen.add(id(node))
        nm = node_name(node)
        if nm in skip:
            continue
        txt = segment(src, node)
        out.append(txt)
    return out


T_HEADER = '''"""tlib - the shared library part of the old tahoe_mtap_gankyrin.py that the build and the effects need.

Ported verbatim (function by function, by syntax tree) from tahoe_mtap_gankyrin.py at commit 28cd834 of
xuvictor04/Tahoe100-PseudoManual (branch claude/tahoe100m-gene-pipeline-lodlx7). Do not edit the copied bodies by
hand: tests/test_port.py checks that they still match the method they came from. New code goes in other modules.
"""

import argparse
import contextlib
import glob
import json
import math
import multiprocessing as mp
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import time
import traceback
from collections import defaultdict

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

'''

A_HEADER = '''"""atlas_core - the build (one pass over every cell -> counts per well x cell line x gene) and the method-v3 effects
(the corrected effect of every drug-dose on every gene and line), ported verbatim from the old tahoe_atlas.py.

Ported function by function (by syntax tree) from tahoe_atlas.py at commit 28cd834 of xuvictor04/Tahoe100-PseudoManual
(branch claude/tahoe100m-gene-pipeline-lodlx7). Only the module header (imports) is new; every function body is the
original. tahoemap.tensor re-derives the per-cell-line residuals from these same functions and checks itself against
the saved well effects. docs/method.md explains the method.
"""

import argparse
import glob
import json
import math
import multiprocessing as mp
import os
import re
import shutil
import sys
import time
import traceback
import warnings
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

from . import tlib as T

'''

os.makedirs(OUT, exist_ok=True)
t_parts = emit(T_SRC, OT, need["T"])
a_parts = emit(A_SRC, OA, need["A"], skip=SKIP_A)

with open(os.path.join(OUT, "tlib.py"), "w", encoding="utf-8") as fh:
    fh.write(T_HEADER + "\n\n".join(p.rstrip("\n") + "\n" for p in t_parts))
with open(os.path.join(OUT, "atlas_core.py"), "w", encoding="utf-8") as fh:
    fh.write(A_HEADER + "\n\n".join(p.rstrip("\n") + "\n" for p in a_parts))
print("tlib:", len(t_parts), "defs,", sum(p.count("\n") for p in t_parts), "lines")
print("atlas_core:", len(a_parts), "defs,", sum(p.count("\n") for p in a_parts), "lines")
# a manifest of what was copied, with a hash of each segment, for the port test
man = []
for mod, src, order, ids, skip in (("tlib", T_SRC, OT, need["T"], ()), ("atlas_core", A_SRC, OA, need["A"], SKIP_A)):
    for node in order:
        if id(node) not in ids:
            continue
        nm = node_name(node)
        if nm in skip:
            continue
        seg = segment(src, node)
        man.append(f"{mod}\t{nm}\t{node.lineno}\t{hashlib.sha256(seg.encode()).hexdigest()[:16]}")
with open(os.path.join(OUT, "PORT_MANIFEST.tsv"), "w", encoding="utf-8") as fh:
    fh.write("module\tname\tsource_line\tsha256_16\n" + "\n".join(man) + "\n")
