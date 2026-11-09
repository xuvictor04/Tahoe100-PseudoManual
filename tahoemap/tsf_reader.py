"""tsf_reader - read the Explorer's data files (TSF1 shards) with Python and numpy only.

Every data file of the Explorer (OUT/explorer/web/d/*.js, OUT/explorer/data/**/*.js) is one ASCII line:

    TAHOE_SHARD("<id>","<base64 of zlib.compress(container)>");

The container (docs/explorer-data.md has the full format):

    bytes 0..3     b"TSF1"
    bytes 4..7     H, the header length (uint32, little-endian)
    bytes 8..8+H   the header: UTF-8 JSON, padded with spaces to a multiple of 8 bytes
    from B0 = 8 + H rounded up to 8: the blobs (offsets are relative to B0)

The header lists the arrays ({"t": type, "shape": [...], "off": offset, "n": bytes, "sh": 1 when stored
byte-planar}) and the tables ({"n": rows, "cols": [...]}). A column is numeric like an array, or "str" (the values in
the header, null = missing) or "dict" (a list of distinct values "d" and an array of codes "c"). Numbers are
little-endian; NaN marks a missing float; "na" gives the value that marks a missing integer.

Use:
    python tsf_reader.py FILE.js          prints what the file holds
    from tsf_reader import read_shard     header, arrays, tables = read_shard("d/g/00/0000.js")

arrays: {name: numpy array with its exact stored bytes}; tables: {name: {column: numpy array or list}}.
"""

import base64
import json
import re
import struct
import sys
import zlib

import numpy as np

MAGIC = b"TSF1"
TYPES = {"f32": "<f4", "f16": "<f2", "f64": "<f8", "i8": "i1", "u8": "u1", "i16": "<i2", "u16": "<u2",
         "i32": "<i4", "u32": "<u4"}
LINE = re.compile(r'^TAHOE_SHARD\("([^"]+)","([A-Za-z0-9+/=]*)"\);\s*$')


def unwrap(text):
    """(id, container bytes) of a shard file's text."""
    m = LINE.match(text.strip("﻿"))
    if not m:
        raise ValueError("not a TAHOE_SHARD line")
    return m.group(1), zlib.decompress(base64.b64decode(m.group(2)))


def blob(body, b0, spec, shape=None):
    """The numpy array a header entry describes (exact bytes; a copy owning its memory)."""
    dt = np.dtype(TYPES[spec["t"]])
    raw = body[b0 + spec["off"]: b0 + spec["off"] + spec["n"]]
    if spec.get("sh") and dt.itemsize > 1:
        raw = np.frombuffer(raw, np.uint8).reshape(dt.itemsize, -1).T.tobytes()
    a = np.frombuffer(raw, dt).copy()
    return a.reshape(shape if shape is not None else spec.get("shape", [a.size]))


def decode(body):
    """(header, arrays, tables) of a container (the bytes inside the zlib stream)."""
    if body[:4] != MAGIC:
        raise ValueError("not a TSF1 container")
    hl = struct.unpack("<I", body[4:8])[0]
    head = json.loads(body[8:8 + hl].decode("utf-8"))
    b0 = 8 + ((hl + 7) // 8) * 8
    arrays = {k: blob(body, b0, v) for k, v in head.get("arrays", {}).items()}
    tables = {}
    for name, t in head.get("tables", {}).items():
        cols = {}
        for c in t["cols"]:
            if c["t"] == "str":
                cols[c["name"]] = list(c["v"])
            elif c["t"] == "dict":
                codes = blob(body, b0, c["c"], [t["n"]])
                d = c["d"]
                cols[c["name"]] = [d[int(i)] for i in codes]
            else:
                cols[c["name"]] = blob(body, b0, c, [t["n"]])
        tables[name] = cols
    return head, arrays, tables


def read_shard(path):
    """(header, arrays, tables) of a shard file."""
    with open(path, encoding="ascii") as fh:
        sid, body = unwrap(fh.read())
    head, arrays, tables = decode(body)
    if head.get("id") != sid:
        raise ValueError(f"{path}: the line names shard {sid}, its header {head.get('id')}")
    return head, arrays, tables


def main(argv):
    for p in argv:
        head, arrays, tables = read_shard(p)
        print(f"{p}: shard {head['id']} ({head.get('kind')}), run {head.get('run')}")
        for k, a in arrays.items():
            print(f"  array {k}: {a.dtype} {list(a.shape)}")
        for k, t in tables.items():
            print(f"  table {k}: {head['tables'][k]['n']} rows; columns " + ", ".join(t))
        for k, v in sorted((head.get("meta") or {}).items()):
            s = json.dumps(v)
            print(f"  meta {k}: {s[:100]}" + ("..." if len(s) > 100 else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
