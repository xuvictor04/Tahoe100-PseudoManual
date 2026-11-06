"""common - shared helpers: logging, the output layout, stage stamps, safe writes, index tables."""

import hashlib
import json
import os
import re
import time

import numpy as np
import pandas as pd

from . import tlib as T

log = T.log

# ----------------------------------------------------------------------------- output layout
# <out>/atlas      the build and the method-v3 effects (same layout as the old tahoe_atlas.py, so an old atlas folder
#                  can be reused);  <out>/tensor  per-cell-line layer;  <out>/tables  fold-change tables;
# <out>/embed      gene / drug / line vectors;  <out>/relations  gene-gene relations;  <out>/graph  nodal map;
# <out>/reference  public annotations;  <out>/validation;  <out>/vault  Obsidian;  <out>/map  interactive map;
# <out>/stages     one stamp per finished stage.
STAGES = ["build", "effects", "tensor", "tables", "embed", "reference", "relations", "graph", "validate",
          "vault", "map"]


def folder(out, name):
    d = os.path.join(out, name)
    os.makedirs(d, exist_ok=True)
    return d


def mark_output(out):
    """The old scripts index every parquet under the data folder unless the folder holds this marker."""
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, ".not_tahoe_input")
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("tahoemap output: not Tahoe-100M input data\n")


def stamp_stage(out, stage, version, info=None):
    d = folder(out, "stages")
    rec = {"stage": stage, "version": version, "finished": time.strftime("%Y-%m-%d %H:%M:%S"),
           "info": info or {}}
    tmp = os.path.join(d, stage + ".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1, default=str)
    os.replace(tmp, os.path.join(d, stage + ".json"))


def read_stamp(out, stage):
    p = os.path.join(out, "stages", stage + ".json")
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def clear_stamps_from(out, stage):
    """A stage that runs again makes every later stage out of date."""
    for s in STAGES[STAGES.index(stage):]:
        p = os.path.join(out, "stages", s + ".json")
        if os.path.exists(p):
            os.remove(p)


# ----------------------------------------------------------------------------- files
def save_npy(path, arr):
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        np.save(fh, arr)
    os.replace(tmp, path)


def open_memmap(path, shape, dtype):
    return np.lib.format.open_memmap(path, mode="w+", dtype=dtype, shape=tuple(int(s) for s in shape))


def load_npy(path, mmap=True):
    return np.load(path, mmap_mode="r" if mmap else None)


def write_parquet(df, path):
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    os.replace(tmp, path)


def write_csv(df, path):
    tmp = path + ".tmp"
    df.to_csv(tmp, index=False)
    os.replace(tmp, path)


def write_json(obj, path):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, default=_json_default)
    os.replace(tmp, path)


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)


def read_effects_index(fxd):
    """The index tables of atlas/effects with stable dtypes (dose and plate are strings, as the atlas wrote them)."""
    str_cols = {"sample": str, "plate": str, "dose": str, "drug": str, "well": str, "cell_line_id": str}
    genes = pd.read_csv(os.path.join(fxd, "genes.csv"), dtype={"symbol": str, "label": str, "kind": str})
    wells = pd.read_csv(os.path.join(fxd, "wells.csv"), dtype=str_cols, keep_default_na=False,
                        na_values=[""])
    for c in ("drug", "dose", "plate", "sample", "well"):
        if c in wells:
            wells[c] = wells[c].fillna("").astype(str)
    wells["is_dmso"] = wells["is_dmso"].astype(str).str.lower().isin(["true", "1"])
    for c in ("used_in_drugdose", "unreliable_plate", "position_not_correctable"):
        if c in wells:
            wells[c] = wells[c].astype(str).str.lower().isin(["true", "1"])
    dd = pd.read_csv(os.path.join(fxd, "drugdose.csv"), dtype={"drug": str, "dose": str, "plates": str,
                                                                "wells": str, "flags": str},
                     keep_default_na=False, na_values=[""])
    dd["flags"] = dd["flags"].fillna("").astype(str)
    lines = pd.read_csv(os.path.join(fxd, "lines.csv"), dtype={"cell_line_id": str})
    plates = pd.read_csv(os.path.join(fxd, "plates.csv"), dtype={"plate": str})
    info = {}
    p = os.path.join(os.path.dirname(fxd), "info.json")
    for cand in (os.path.join(fxd, "info.json"), p):
        if os.path.exists(cand):
            with open(cand, encoding="utf-8") as fh:
                info.update(json.load(fh))
    return {"genes": genes, "wells": wells, "drugdose": dd, "lines": lines, "plates": plates, "info": info}


# ----------------------------------------------------------------------------- names
_BAD = re.compile(r'[\\/:*?"<>|#^\[\]]')
_RESERVED = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}


def safe_filename(name, maxlen=120):
    """A file name every OS and Obsidian accept; keeps letters, digits, spaces, parentheses, dots, dashes."""
    s = _BAD.sub("_", str(name)).strip().rstrip(".")
    s = re.sub(r"\s+", " ", s)
    if s.upper().split(".")[0] in _RESERVED:
        s = "_" + s
    return s[:maxlen] or "_"


def stable_seed(*parts):
    """A seed that is the same in every process and on every machine (Python's hash() is salted)."""
    h = hashlib.blake2b("|".join(str(p) for p in parts).encode(), digest_size=8).digest()
    return int.from_bytes(h, "little") % (2 ** 32)
