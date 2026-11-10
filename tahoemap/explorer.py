"""explorer - the Explorer: static web pages over every result of a run, with complete and exact data.

Stage `explorer` (after `map`). It writes OUT/explorer/:

    web/        the pages and their data, published as the GitHub Pages branch 'site': the app (index.html, app.js,
                app.css from tahoemap/explorer_app/), d/ (the data files: core, flags, hosts, search, below, ddarr,
                genes, space/, linecpm, sets, groups, val, docs, files, the gene buckets g/, the lines l/, the modules
                m/, the direction groups dg/, the drugs dr/) and map/ (a copy of the gene map)
    data/       the large files, published as a separate repository: x/ one file per gene (per-line lfc and z,
                per-well values and raw counts, plate baselines) and p/ one file per drug-dose (every gene's pooled
                values)
    data_dd/    optional (--with-line-dd): y/ one file per drug-dose with every gene's per-line lfc and z
    manifest.json   every file with its volume and bytes, the run id and the moves of the size guard

Every data file is one line `TAHOE_SHARD("<id>","<base64 of zlib(TSF1 container)>");` (docs/explorer-data.md has
the format and the full list of files, arrays, tables and columns; tahoemap/tsf_reader.py reads them with numpy).

Rules this module keeps (the "do not hide" rules of the design):
- nothing is capped or filtered: every list holds every source row (the stage counts the rows of each source table
  over its files and writes the counts to the stamp; it stops when a count differs);
- a flag never removes anything: flags are stored next to the values, as the exact strings the tables stage writes
  (tables.flag_strings; the stage stops unless they equal tables/drug_effects.parquet on every row);
- values are the stored bytes: pooled values float32 as in atlas/effects, per-line values float16 as in tensor/;
- text is never shortened;
- a size limit moves data from the web volume to the data volume and never drops it; when moving is not enough the
  stage stops and leaves its files in OUT/explorer.tmp.

Memory and time on the real data (16,643 genes x 1,132 drug-doses x 50 lines): about 3 GB at the peak and 15 to 25
minutes; the stamp records the bytes per volume, the row counts, each step's time and the peak memory.
"""

import base64
import concurrent.futures as cf
import glob
import hashlib
import json
import math
import os
import re
import shutil
import struct
import sys
import threading
import time
import warnings
import zlib

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import tables as TB
from . import tsf_reader as TR
from .common import (find_git, git_out, log, read_effects_index, read_stamp, remove_file, replace_file,
                     stamp_stage)

VERSION = 2                       # 2: drug pages find drug_target arrows by salt base (direction_view's rule);
#                                   control sets matched by whole drug name; one driver row per gene
BUCKET = 16                       # genes per gene bucket d/g/NN/BBBB.js
DG_PER_SHARD = 32                 # direction comparisons per d/dg/KKK.js
FLAG_CHUNK = 64                   # drug-doses per call of tables.flag_strings
LINE_CHUNK = 256                  # genes per block of the per-line pass
ZLIB_LEVEL = 6
PAGES_MAX_MB = 905                # web volume above this (MiB of 2**20 bytes = 0.949 GB, about 50 MB below GitHub
#                                   Pages' 1 GB): the size guard moves parts to the data volume
FILE_WARN_MB = 50                 # a file above this (MiB) is reported; GitHub warns above 50 MiB
FILE_MAX_MB = 95                  # a file above this stops the stage (GitHub refuses files above 100 MiB)
MAX_ENTRIES = 1000                # entries per folder
MAX_PATH = 80                     # characters of a path relative to its volume
SELF_CHECK_EVERY = 97             # step G decodes every 97th data file (and every top-level web data file)
I32_NA = -2 ** 31                 # the missing-value mark of an integer column stored as i32
U8_NA = 255                       # ... of a boolean column stored as u8, and of nl for the summed modules
APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "explorer_app")
CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The size guard: parts moved, in this order, from the web volume to the data volume until the web volume fits.
# A moved part of web file d/<id>.js is in data file w/<id>.js (core.js 'where' lists the moves).
MOVES = (("l.ms", "l/", "array", "ms", "line-major module scores (d/l/LL.js 'ms')"),
         ("g.rel", "g/", "table", "rel", "each gene's 100 partner rows (d/g/NN/BBBB.js 'rel')"),
         ("m.ms", "m/", "array", "ms", "module-major module scores (d/m/MMM.js 'ms')"))

# Plain words for every flag token tables.flag_strings writes (shown next to the flags on every page).
FLAG_WORDS = {
    "toxic": "The drug killed many cells at this dose: its wells kept far fewer cells than the plate's other drug "
             "wells, and a higher dose did not undo the loss. Changes here can come from dying cells. Artifact flag.",
    "low cells (technical?)": "The wells kept fewer cells than the plate's other drug wells, but the loss does not "
                              "look like killing (one well only, or a higher dose kept its cells). Read with care. "
                              "Not an artifact flag.",
    "plate-row cell shift": "The plate row of these wells had other cell counts or RNA per cell than the rest of the "
                            "plate; the values are compared within the row. Not an artifact flag.",
    "transcription drop": "The cells made much less RNA (fewer genes or fewer counts per cell) than in the plate's "
                          "other drug wells, so many genes seem to fall together. Artifact flag.",
    "cell-cycle shift": "The share of cells in S or G2/M phase moved (the S_PHASE or G2M_PHASE module changed). A gene "
                        "that goes with the cell cycle then changes for that reason alone. Artifact flag.",
    "cell-cycle shift (explains ~N% here)": "The drug-dose moved the cell cycle, but for this gene the shift explains "
                                            "only about N% of the change (from the gene's own cell-cycle slopes, "
                                            "doubled for safety). So here it is not an artifact flag.",
    "composition shift": "The make-up of the cells' RNA libraries moved (by 0.2 log2 or more); the values are "
                         "corrected for it. Not an artifact flag.",
    "noisy plate (z scaled)": "The plate (or this gene on it) was noisier than comparable plates, so z was divided by "
                              "the plate factor (more than 1.2). Not an artifact flag.",
    "unreliable plate only": "Every used well of this drug-dose is on the plate marked unreliable. Artifact flag.",
    "position not correctable": "A used well could not be corrected for its position on the plate (too few clean "
                                "wells of other drugs at that position). Artifact flag.",
    "position correction uncertain": "For this gene, a used well had fewer than 3 clean wells of other drugs at its "
                                     "position, so its position effect was not removed. Artifact flag.",
    "position effect removed": "A well-position effect larger than 0.2 log2 was removed for this gene; the values are "
                               "after the correction (data/x/ files hold the removed part as poseff). Not an "
                               "artifact flag.",
    "wells disagree": "The replicate wells disagree (r < 0.1 over the most changed genes, although many genes "
                      "changed). Artifact flag.",
}
CC_CLEARED_RE = re.compile(r"^cell-cycle shift \(explains ~\d+% here\)$")

# What each data-file array holds (core.js meta 'arrays'; the pages show it next to the values).
ARRAY_DOCS = {
    "g": {"cols": "gene columns of the bucket (col: row of tables/genes.parquet)",
          "lfc": "pooled corrected log2 fold change, genes x drug-doses (atlas/effects/DD_lfc.npy, exact float32)",
          "z": "pooled z, genes x drug-doses (DD_z.npy, exact)", "q_up": "BH q for a rise (DD_qup.npy, exact)",
          "q_dn": "BH q for a fall (DD_qdn.npy, exact)",
          "flag": "index into d/flags.js: the gene-level flag string of every (gene, drug-dose), as "
                  "tables.flag_strings writes it",
          "nl": "per (gene, drug-dose), counted over the 50 lines: [measured, up2, down2, upT, downT]: lines with a "
                "value; lines with per-line z >= 2 and fold >= 1.2 (up) or z <= -2 and fold <= 1/1.2 (down; the "
                "drug_effects n_lines_* rule); lines with |per-line z| >= t (calibrated cut, core.js "
                "line_z_threshold) and fold >= 1.5 that way (the line_effects rule)",
          "cc": "cc_share at the cell-cycle-flagged drug-doses (core.js arrays cc_dd, in that order): the share of "
                "the change the cell-cycle shift would explain; NaN without slopes",
          "pat": "dose pattern code (core.js PATTERNS) per (gene, drug, [up, down]); drugs in the order of "
                 "tables/drugs.parquet",
          "lcen": "line_center (tensor): robust centre of the gene's per-line values in each line",
          "lsc": "line_scale (tensor): robust spread (1.4826 MAD) used as the per-line z divisor",
          "gvec": "gene vector in the vector space (embed/gene_vectors.npy); NaN outside the space"},
    "x": {"lfc": "per-line corrected log2 fold change, drug-doses x lines (tensor/DDL_lfc.npy, exact float16)",
          "z": "per-line z, drug-doses x lines (tensor/DDL_z.npy, exact float16)",
          "poseff": "the well-position effect removed, per drug-dose (DD_poseff.npy)",
          "w1": "per well: effect before the position correction (W1.npy)",
          "w2": "per well: corrected effect (W2.npy; DD_lfc is the mean over a drug-dose's used wells)",
          "wz": "per well: robust z of the corrected effect (Z.npy)",
          "counts": "per well: raw UMI counts of the gene summed over the well's cells (tensor/well_counts.npy); "
                    "raw CPM = counts / well_umi x 1e6 (computed in the page)",
          "wpu": "per well: 1 = position correction uncertain for this gene (posunc.npy)",
          "pbase": "plates x lines: the line's baseline log2 CPM on the plate, the reference of every fold change "
                   "(tensor/plate_base.npy)",
          "poff": "per plate: how far the plate's DMSO wells sit below its drug-well median (plate_offset.npy); add "
                  "it to an lfc for a rough DMSO-referenced value",
          "slot": "96 plate positions (A1..H12): median shift of all drugs at that position (slot_median.npy)",
          "psg": "per plate-and-dose group: the gene's z divisor (plate_scale_gene.npy)"},
    "p": {"lfc": "every column's pooled corrected log2 fold change at this drug-dose (DD_lfc row, exact)",
          "z": "pooled z (DD_z row)", "q_up": "BH q for a rise", "q_dn": "BH q for a fall",
          "poseff": "position effect removed (DD_poseff row)", "flag": "index into d/flags.js",
          "nl": "lines counted as in the gene buckets (255 = no per-line values: a summed module)",
          "pat": "the drug's dose pattern for each column, [up, down] (-1 = not computed: a summed module)",
          "cc": "cc_share (only at a cell-cycle-flagged drug-dose)",
          "ms": "module scores, modules x lines (graph/module_scores.npy at this drug-dose, exact float16)"},
    "y": {"lfc": "per-line lfc of every gene at this drug-dose, genes x lines (tensor/DDL_lfc.npy, exact)",
          "z": "per-line z, genes x lines (tensor/DDL_z.npy, exact)"},
}

# R11: where every file of OUT is in the explorer (or why it is not). Patterns: '*' within a folder, '**' anything.
INVENTORY = [
    ("atlas/effects/DD_lfc.npy", "web d/g/ lfc (per gene); data p/ lfc (per drug-dose)", "gene: Drugs; drug-dose: "
     "All genes", "pooled corrected log2 fold change (exact float32)"),
    ("atlas/effects/DD_z.npy", "web d/g/ z; data p/ z", "gene: Drugs; drug-dose: All genes", "pooled z"),
    ("atlas/effects/DD_qup.npy", "web d/g/ q_up; data p/ q_up", "gene: Drugs", "BH q for a rise"),
    ("atlas/effects/DD_qdn.npy", "web d/g/ q_dn; data p/ q_dn", "gene: Drugs", "BH q for a fall"),
    ("atlas/effects/DD_poseff.npy", "data x/ poseff and p/ poseff", "gene: Drugs (with per-line data)",
     "the position effect removed"),
    ("atlas/effects/DD_posunc.npy", "in the flag codes (web d/g/ flag, data p/ flag)", "every flags column",
     "'position correction uncertain' per (drug-dose, gene)"),
    ("atlas/effects/DD_A.npy", "web d/ddarr.js DD_A", "drug-dose: Lines; line: Sensitivity", "cells left per line"),
    ("atlas/effects/DD_Az.npy", "web d/ddarr.js DD_Az", "drug-dose: Lines; line: Sensitivity", "its z"),
    ("atlas/effects/DD_beta.npy", "web d/ddarr.js DD_beta", "drug-dose: Lines", "response strength per line"),
    ("atlas/effects/DD_rcor.npy", "web d/ddarr.js DD_rcor", "drug-dose: Lines", "its correlation"),
    ("atlas/effects/DD_r2_modules.npy", "web d/ddarr.js DD_r2_modules", "drug-dose: Lines", "S / G2M / proteasome"),
    ("atlas/effects/W1.npy", "data x/ w1", "gene: Baseline & wells", "per well, before the position correction"),
    ("atlas/effects/W2.npy", "data x/ w2", "gene: Baseline & wells", "per well, corrected"),
    ("atlas/effects/Z.npy", "data x/ wz", "gene: Baseline & wells", "per well z"),
    ("atlas/effects/posunc.npy", "data x/ wpu", "gene: Baseline & wells", "per well position-uncertain flag"),
    ("atlas/effects/A2.npy", "web d/ddarr.js A2", "drug-dose: Wells", "per well x line relative abundance"),
    ("atlas/effects/zA.npy", "web d/ddarr.js zA", "drug-dose: Wells", "its z"),
    ("atlas/effects/VA.npy", "web d/ddarr.js VA", "drug-dose: Wells", "its counting variance"),
    ("atlas/effects/beta.npy", "web d/ddarr.js wbeta", "drug-dose: Wells", "per well x line response strength"),
    ("atlas/effects/rcor.npy", "web d/ddarr.js wrcor", "drug-dose: Wells", "its correlation"),
    ("atlas/effects/r2_modules.npy", "web d/ddarr.js wr2", "drug-dose: Wells", "per well x line module effects"),
    ("atlas/effects/line_cpm.npy", "web d/linecpm.js line_cpm", "gene: Baseline; line: Baseline", "baseline CPM"),
    ("atlas/effects/expr_mask.npy", "web d/linecpm.js expr_mask", "gene: Baseline", "the atlas's expression rule"),
    ("atlas/effects/slot_median.npy", "data x/ slot", "gene: Baseline & wells", "plate-position landscape"),
    ("atlas/effects/plate_offset.npy", "data x/ poff", "gene: Baseline & wells", "DMSO offset per plate"),
    ("atlas/effects/plate_scale_gene.npy", "data x/ psg", "gene: Baseline & wells", "the gene's z divisor"),
    ("atlas/effects/genes.csv", "web d/genes.js agenes", "Browse genes", "the column index (genes and modules)"),
    ("atlas/effects/wells.csv", "web d/core.js wells (tables/wells.parquet: the same columns plus w, umi_total)",
     "drug-dose: Wells; plate", "well index"),
    ("atlas/effects/drugdose.csv", "web d/core.js drugdoses (tables/drugdoses.parquet: the same columns and more)",
     "drug-dose: QC", "drug-dose index"),
    ("atlas/effects/lines.csv", "web d/core.js lines (tables/lines.parquet: the same columns and more)", "line",
     "line index"),
    ("atlas/effects/plates.csv", "web d/core.js plates", "plate", "plate order of plate_offset"),
    ("atlas/effects/plate_scale.csv", "web d/core.js plate_scale", "plate", "plate factors"),
    ("atlas/effects/failed_wells.csv", "web d/core.js failed_wells", "plate", "wells left out as failed"),
    ("atlas/effects/composition_shift.parquet", "web d/l/ comp", "line: Wells", "per (well, line) library shift"),
    ("atlas/effects/modules.json", "web d/core.js meta effects_modules", "About", "members of the summed modules"),
    ("atlas/effects/info.json", "web d/core.js meta info", "About", "effects settings"),
    ("atlas/effects/complete.json", "web d/core.js meta info", "About", "effects completion record"),
    ("atlas/effects/README_effects.md", "web d/docs.js", "About", "documentation"),
    ("atlas/pseudobulk/*", "not published", "Files", "the build: raw summed counts per (well, line) profile for "
     "every Tahoe token (about 21 GB on the real data); everything after it is in the explorer"),
    ("atlas/sample_map.csv", "web d/core.js sample_map", "plate", "every well's Tahoe metadata"),
    ("atlas/build_info.json", "web d/core.js meta info", "About", "build counts"),
    ("atlas/file_index.json", "not published", "Files", "paths of the input files on the computer that ran it"),
    ("atlas/well_position_check.csv", "web d/val.js", "Files", "barcode-field check of the well positions"),
    ("atlas/reused_from.json", "not published", "Files", "where a reused build came from (a path)"),
    ("atlas/reports/**", "not in the explorer", "Files", "the atlas's text reports (the results branch has them "
     "with export --with-effects)"),
    ("atlas/angles/**", "not published", "Files", "a folder of the old atlas scripts (empty)"),
    ("hf/**", "not published", "Files", "input files a streamed build fetched (Tahoe-100M itself)"),
    ("tensor/DDL_lfc.npy", "data x/ lfc (and data_dd y/ when built)", "gene: Cell lines", "per-line lfc (float16)"),
    ("tensor/DDL_z.npy", "data x/ z (and data_dd y/)", "gene: Cell lines", "per-line z (float16)"),
    ("tensor/R.npy", "not published", "Files", "per (gene, well, line) values (about 4.4 GB on the real data); "
     "data x/ holds their means per drug-dose (lfc) and the per-well values pooled over lines (w1, w2, wz)"),
    ("tensor/line_center.npy", "web d/g/ lcen", "gene: Baseline", "per-line centre"),
    ("tensor/line_scale.npy", "web d/g/ lsc", "gene: Baseline", "per-line spread"),
    ("tensor/line_measured.npy", "web d/linecpm.js line_measured", "gene: Baseline", "the line truly expresses it"),
    ("tensor/plate_base.npy", "data x/ pbase", "gene: Baseline & wells", "baseline of every fold change"),
    ("tensor/well_counts.npy", "data x/ counts", "gene: Baseline & wells", "raw counts"),
    ("tensor/well_umi.npy", "web d/core.js well_umi", "drug-dose: Wells", "total UMI per well"),
    ("tensor/well_line_cells.npy", "web d/ddarr.js well_line_cells", "drug-dose: Wells", "cells per well and line"),
    ("tensor/well_line_umi.npy", "web d/ddarr.js well_line_umi", "drug-dose: Wells", "UMI per well and line"),
    ("tensor/info.json", "web d/core.js meta info", "About", "tensor settings and checks"),
    ("tables/genes.parquet", "web d/genes.js genes; d/g/ genes", "Browse genes; gene", "per-gene summary"),
    ("tables/drug_effects.parquet", "web d/g/ arrays (every gene x drug-dose, a superset); d/dr/ de", "gene: Drugs",
     "the stored (gene, drug-dose) rows; the explorer holds all of them and every other pair"),
    ("tables/line_effects.parquet", "web d/g/ le; d/l/ le", "gene: Cell lines; line: Genes", "gene x line"),
    ("tables/drug_line_top.parquet", "web d/g/ dlt", "gene: Cell lines", "strongest (drug-dose, line) cells"),
    ("tables/drugdoses.parquet", "web d/core.js drugdoses", "drug-dose: QC", "per drug-dose"),
    ("tables/drugs.parquet", "web d/core.js drugs", "drug", "per drug"),
    ("tables/lines.parquet", "web d/core.js lines", "line", "per line"),
    ("tables/plates.parquet", "web d/core.js plates", "plate", "per plate"),
    ("tables/wells.parquet", "web d/core.js wells", "drug-dose: Wells; plate", "per well"),
    ("tables/README.md", "web d/docs.js", "About", "column documentation"),
    ("tables/info.json", "web d/core.js meta info", "About", "row counts, per-line cut, cell-cycle rule"),
    ("embed/gene_vectors.npy", "web d/g/ gvec", "gene: Correlations", "gene vectors"),
    ("embed/gene_unit.npy", "web d/space/u.js", "gene: Correlations", "unit gene vectors"),
    ("embed/gene_unit_half1.npy", "web d/space/h1.js", "gene: Correlations", "half-1 unit vectors"),
    ("embed/gene_unit_half2.npy", "web d/space/h2.js", "gene: Correlations", "half-2 unit vectors"),
    ("embed/included_cols.npy", "web d/space/u.js included", "gene: Correlations", "genes in the space"),
    ("embed/gene_row_mean.npy", "web d/space/u.js row_mean", "About", "standardisation"),
    ("embed/gene_row_scale.npy", "web d/space/u.js row_scale", "About", "standardisation"),
    ("embed/context_vectors.npy", "web d/space/ctx.js", "drug-dose: Vector space", "context vectors"),
    ("embed/drugdose_vectors.npy", "web d/ddarr.js drugdose_vectors", "drug-dose: Vector space", "vectors"),
    ("embed/drug_vectors.npy", "web d/ddarr.js drug_vectors", "drug: Similar drugs", "vectors"),
    ("embed/line_baseline_vectors.npy", "web d/ddarr.js line_baseline_vectors", "line: Vector space", "vectors"),
    ("embed/line_response_vectors.npy", "web d/ddarr.js line_response_vectors", "line: Vector space", "vectors"),
    ("embed/singular_values.npy", "web d/ddarr.js singular_values", "About", "singular values"),
    ("embed/genes.parquet", "web d/genes.js egenes; d/g/ egenes", "gene", "per gene in the space"),
    ("embed/contexts.parquet", "web d/ddarr.js contexts", "drug-dose: Vector space", "the contexts"),
    ("embed/drugdoses.parquet", "web d/core.js edd", "drug-dose", "fit status"),
    ("embed/drugs.parquet", "web d/core.js edrugs; d/dr/ edrug", "drug", "per drug in the space"),
    ("embed/components.parquet", "web d/core.js components", "line: Vector space", "components"),
    ("embed/broad_components.csv", "web d/core.js broad", "About", "broad components removed"),
    ("embed/info.json", "web d/core.js meta info", "About", "space settings"),
    ("relations/gene_relations.parquet", "web d/g/ rel (by gene) and relb (by partner)", "gene: Partners",
     "the 100 strongest partners of each gene"),
    ("relations/fdr_curve.csv", "web d/core.js fdr_curve", "gene: Correlations", "fdr of any pair"),
    ("relations/info.json", "web d/core.js meta info", "About", "counts"),
    ("graph/nodes.parquet", "web d/g/ node; d/m/ members; d/search.js g module, arm", "gene; module",
     "map positions, module, arm"),
    ("graph/edges.parquet", "web d/g/ gedge; d/m/ edges", "gene: Partners; module", "kNN edges"),
    ("graph/modules.parquet", "web d/core.js modules; d/m/ module", "module", "per module"),
    ("graph/module_scores.npy", "web d/l/ ms, d/m/ ms; data p/ ms", "module; line; drug-dose", "per line"),
    ("graph/module_pooled_z.npy", "web d/ddarr.js module_pooled_z; d/m/ pz", "module; drug-dose", "pooled"),
    ("graph/info.json", "web d/core.js meta info", "About", "module rule"),
    ("direction/edges.parquet", "web d/g/ dir, d/dg/ edges, d/dr/ dir", "gene: Direction; group; drug",
     "probable direction arrows"),
    ("direction/groups.parquet", "web d/groups.js; d/dg/ groups; d/g/ dgrp; d/l/ grp", "group; line: Genetics",
     "the comparisons"),
    ("direction/controls.json", "web d/val.js meta direction_controls", "About", "controls"),
    ("direction/info.json", "web d/core.js meta info", "About", "counts per kind and grade"),
    ("direction/README.md", "web d/docs.js", "About", "column documentation"),
    ("reference/annotations.parquet", "web d/g/ ann; d/search.js g", "gene: Annotation", "public annotation"),
    ("reference/gene_sets.parquet", "web d/sets.js; d/g/ sets", "set; gene: Annotation", "gene-set memberships"),
    ("reference/string_pairs.parquet", "web d/g/ string", "gene: Partners", "STRING pairs"),
    ("reference/sources.json", "web d/core.js meta info", "About", "provenance"),
    ("reference/downloads/**", "not published", "Files", "the raw public files (download cache)"),
    ("validation/control_sets.csv", "web d/val.js", "set", "control sets"),
    ("validation/drug_moa.csv", "web d/val.js; d/dr/ moa", "drug", "mechanism classes"),
    ("validation/module_enrichment.csv", "web d/val.js; d/m/ enr", "module", "enrichment"),
    ("validation/module_labels.csv", "web d/core.js mlabels; d/val.js", "module", "labels"),
    ("validation/novel_edges.csv", "web d/val.js; d/g/ nedge", "gene: Partners", "novel pairs"),
    ("validation/novel_members.csv", "web d/val.js; d/g/ nmem; d/m/ nmem", "module", "novel members"),
    ("validation/opposite_pairs.csv", "web d/val.js", "About", "opposite modules"),
    ("validation/metrics.json", "web d/val.js meta metrics", "About", "headline numbers"),
    ("validation/report.md", "web d/val.js meta report", "About", "validation report"),
    ("validation/README.md", "web d/docs.js", "About", "column documentation"),
    ("vault/**", "the results branch vault/ (Obsidian notes); every page links to its note", "links",
     "notes made from the same tables"),
    ("map/gene_map.html", "web map/gene_map.html (a copy that links back to the explorer)", "Map", "the map"),
    ("stages/*.json", "web d/core.js meta stamps", "About", "one record per finished stage"),
    ("explorer/**", "the explorer itself", "Files", "this explorer"),
    ("explorer.tmp/**", "not published", "Files", "an explorer build in progress or stopped by the size guard"),
    ("explorer.old/**", "not published", "Files", "an explorer being replaced"),
    ("review/**", "not in the explorer: the literature reviews are shown in the vault and the map", "Files",
     "literature reviews"),
    ("run_options.json", "web d/core.js meta run_options", "About", "options given to earlier runs"),
    ("run.log", "not published", "Files", "the pipeline log"),
    ("pipeline_console.log", "not published", "Files", "console output of a background run"),
    ("console.log", "not published", "Files", "console output of a background job started with the tahoe launcher"),
    ("console.log.prev", "not published", "Files", "the console output of the job before it (tahoe launcher)"),
    ("download.log", "not published", "Files", "the log of a download started with the tahoe launcher"),
    (".not_tahoe_input", "not published", "Files", "marker: this folder is output, not input"),
    (".pipeline.lock", "not published", "Files", "a run in progress"),
    (".job.pid", "not published", "Files", "a background run's process id"),
    ("duplicated_from.json", "not published", "Files", "where a duplicated output came from"),
    ("README.md", "not published", "Files", "the results branch README (export)"),
    ("MANIFEST.tsv", "not published", "Files", "the results branch file list (export)"),
    (".gitattributes", "not published", "Files", "git settings of an export"),
    ("**.tmp", "not published", "Files", "an unfinished write"),
    ("**.part", "not published", "Files", "an unfinished download or copy"),
]
DOC_FILES = ("tables/README.md", "direction/README.md", "validation/README.md", "atlas/effects/README_effects.md")
INFO_FILES = ("atlas/build_info.json", "atlas/effects/info.json", "atlas/effects/complete.json",
              "atlas/effects/modules.json", "tensor/info.json", "tables/info.json", "embed/info.json",
              "relations/info.json", "graph/info.json", "direction/info.json", "reference/sources.json",
              "run_options.json")


def _glob_re(pattern):
    out = ""
    i = 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif pattern[i] == "*":
            out += "[^/]*"
            i += 1
        elif pattern[i] == "?":
            out += "[^/]"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile("^" + out + "$")


_INV_RE = [(_glob_re(p), p) for p, *_ in INVENTORY]


def inventory_pattern(rel):
    """The INVENTORY pattern a file of OUT (path relative to OUT, '/'-separated) falls under, or None."""
    for rx, p in _INV_RE:
        if rx.match(rel):
            return p
    return None


# ----------------------------------------------------------------------------- shard paths
def g_id(b):
    return f"g/{b // 100:02d}/{b:04d}"


def x_id(col):
    return f"x/{col // 1000:02d}/{col:05d}"


def p_id(dd):
    return f"p/{dd // 100:02d}/{dd:04d}"


def y_id(dd):
    return f"y/{dd // 100:02d}/{dd:04d}"


def l_id(line):
    return f"l/{line:02d}"


def m_id(m):
    return f"m/{m:03d}"


def dg_id(k):
    return f"dg/{k:03d}"


def dr_id(i):
    return f"dr/{i:03d}"


PATHS = {"g": "d/g/{b//100:02d}/{b:04d}.js (b = col // 16)", "mod": "d/g/mod.js",
         "x": "x/{col//1000:02d}/{col:05d}.js (data volume)", "p": "p/{dd//100:02d}/{dd:04d}.js (data volume)",
         "y": "y/{dd//100:02d}/{dd:04d}.js (data_dd volume)", "l": "d/l/{line:02d}.js", "m": "d/m/{module:03d}.js",
         "dg": "d/dg/{k:03d}.js (k = comparison index // 32; d/groups.js column _dg)",
         "dr": "d/dr/{i:03d}.js (i = row of tables/drugs.parquet)",
         "moved": "a part moved by the size guard from web d/<id>.js is in data w/<id>.js"}


# ----------------------------------------------------------------------------- TSF1 container
MAGIC = TR.MAGIC
_TYPE = {"<f4": "f32", "<f2": "f16", "<f8": "f64", "|i1": "i8", "|u1": "u8", "<i2": "i16", "<u2": "u16",
         "<i4": "i32", "<u4": "u32"}


class _Blobs:
    """The blob area of a container being written: each array 8-aligned, numbers little-endian, arrays with items
    of more than one byte stored byte-planar ('sh': 1)."""

    def __init__(self):
        self.parts = []
        self.off = 0

    def add(self, a, shape=True):
        a = np.asarray(a)
        if a.dtype == bool:
            a = a.astype(np.uint8)
        a = np.ascontiguousarray(a.astype(a.dtype.newbyteorder("<"), copy=False))
        t = _TYPE[a.dtype.str]
        raw = a.tobytes()
        sh = a.dtype.itemsize > 1
        if sh:
            raw = np.frombuffer(raw, np.uint8).reshape(-1, a.dtype.itemsize).T.tobytes()
        return self.raw(raw, t, int(sh), list(a.shape) if shape else None)

    def raw(self, raw, t, sh, shape=None):
        pad = (-self.off) % 8
        if pad:
            self.parts.append(b"\0" * pad)
            self.off += pad
        spec = {"t": t, "off": self.off, "n": len(raw), "sh": sh}
        if shape is not None:
            spec["shape"] = shape
        self.parts.append(raw)
        self.off += len(raw)
        return spec


def _jsonable(o):
    """o with numpy scalars as Python numbers, NaN / infinity as None, tuples as lists (JSON without NaN)."""
    if isinstance(o, dict):
        return {str(k): _jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_jsonable(v) for v in o]
    if isinstance(o, np.ndarray):
        return _jsonable(o.tolist())
    if isinstance(o, (bool, np.bool_)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (float, np.floating)):
        f = float(o)
        return f if math.isfinite(f) else None
    if o is None or isinstance(o, (int, str)):
        return o
    if o is pd.NA or o is pd.NaT:
        return None
    return str(o)


def _str_values(vals, isna):
    return [None if m else (x if isinstance(x, str) else str(x)) for x, m in zip(vals, isna)]


def _enc_col(name, s, bl):
    """Header entry of one table column (values into the blob area). 'pd' keeps the pandas dtype, so that read_shard
    gives back the column as it was."""
    dt = s.dtype
    pdn = str(dt)
    n = len(s)
    if isinstance(dt, pd.CategoricalDtype):
        s = s.astype(object)
        dt = s.dtype
    if dt == np.dtype(bool):
        return {"name": name, "pd": pdn, **bl.add(s.to_numpy(dtype=np.uint8), shape=False)}
    if isinstance(dt, pd.BooleanDtype):
        m = s.isna().to_numpy()
        v = np.where(m, U8_NA, s.fillna(False).to_numpy(dtype=bool).astype(np.uint8)).astype(np.uint8)
        return {"name": name, "pd": pdn, "na": U8_NA, **bl.add(v, shape=False)}
    if isinstance(dt, np.dtype) and dt.kind in "iu":
        v = s.to_numpy()
        if dt.itemsize == 8:
            if n == 0 or (int(v.min()) > I32_NA and int(v.max()) < 2 ** 31):
                v = v.astype(np.int32)
            else:
                v = v.astype(np.float64)
        return {"name": name, "pd": pdn, **bl.add(v, shape=False)}
    if pd.api.types.is_extension_array_dtype(dt) and pd.api.types.is_integer_dtype(dt):
        m = s.isna().to_numpy()
        v = s.to_numpy(dtype=np.float64, na_value=np.nan)
        ok = v[~m]
        if ok.size == 0 or (ok.min() > I32_NA and ok.max() < 2 ** 31):
            return {"name": name, "pd": pdn, "na": I32_NA,
                    **bl.add(np.where(m, I32_NA, np.nan_to_num(v)).astype(np.int32), shape=False)}
        return {"name": name, "pd": pdn, **bl.add(v, shape=False)}
    if isinstance(dt, np.dtype) and dt.kind == "f":
        return {"name": name, "pd": pdn, **bl.add(s.to_numpy(), shape=False)}
    if pd.api.types.is_extension_array_dtype(dt) and pd.api.types.is_float_dtype(dt):
        return {"name": name, "pd": pdn, **bl.add(s.to_numpy(dtype=np.float64, na_value=np.nan), shape=False)}
    vals = s.to_numpy(dtype=object)
    isna = np.asarray(pd.isna(vals), dtype=bool) if n else np.zeros(0, dtype=bool)
    nn = vals[~isna]
    if pdn == "object" and nn.size and all(isinstance(x, (bool, np.bool_)) for x in nn):
        v = np.where(isna, U8_NA, np.array([bool(x) if not m else False for x, m in zip(vals, isna)], dtype=np.uint8))
        return {"name": name, "pd": "object:bool", "na": U8_NA, **bl.add(v.astype(np.uint8), shape=False)}
    if pdn == "object" and nn.size and all(isinstance(x, (int, float, np.integer, np.floating))
                                           and not isinstance(x, (bool, np.bool_)) for x in nn):
        v = np.array([np.nan if m else float(x) for x, m in zip(vals, isna)], dtype=np.float64)
        return {"name": name, "pd": "object:num", **bl.add(v, shape=False)}
    strs = _str_values(vals, isna)
    if n >= 8:
        codes, uniq = pd.factorize(pd.Series(strs, dtype=object), use_na_sentinel=True)
        if len(uniq) * 2 <= n:
            d = [str(u) for u in uniq]
            if (codes < 0).any():
                codes = np.where(codes < 0, len(d), codes)
                d.append(None)
            ct = np.uint8 if len(d) <= 256 else (np.uint16 if len(d) <= 65536 else np.uint32)
            return {"name": name, "pd": pdn, "t": "dict", "d": d, "c": bl.add(codes.astype(ct), shape=False)}
    return {"name": name, "pd": pdn, "t": "str", "v": strs}


def _enc_table(df, bl):
    return {"n": int(len(df)), "cols": [_enc_col(str(c), df[c], bl) for c in df.columns]}


def encode(sid, run, kind, arrays=None, tables=None, meta=None):
    """The TSF1 container (bytes, before zlib) of a shard: arrays {name: numpy array}, tables {name: DataFrame},
    meta {name: JSON value}."""
    bl = _Blobs()
    head = {"fmt": 1, "id": sid, "run": run, "kind": kind, "meta": _jsonable(meta or {}), "arrays": {}, "tables": {}}
    for k, a in (arrays or {}).items():
        head["arrays"][k] = bl.add(a)
    for k, df in (tables or {}).items():
        head["tables"][k] = _enc_table(df, bl)
    return _container(head, bl.parts)


def _container(head, parts):
    h = json.dumps(head, sort_keys=True, ensure_ascii=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    return MAGIC + struct.pack("<I", len(h)) + h + b" " * ((-len(h)) % 8) + b"".join(parts)


def shard_text(sid, body, level=ZLIB_LEVEL):
    return f'TAHOE_SHARD("{sid}","' + base64.b64encode(zlib.compress(body, level)).decode("ascii") + '");\n'


def write_shard(path, sid, run, kind, arrays=None, tables=None, meta=None):
    """Write one shard file (TSF1 in a TAHOE_SHARD line); returns its bytes."""
    text = shard_text(sid, encode(sid, run, kind, arrays, tables, meta))
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(text)
    return len(text)


def _restore(spec, values):
    """A decoded column as the pandas Series it was written from (dtype from 'pd')."""
    pdn = spec.get("pd", "")
    if spec["t"] in ("str", "dict"):
        return pd.Series(values, dtype=object)
    v = values
    if "na" in spec:
        m = v == spec["na"]
        if pdn == "boolean":
            return pd.Series(pd.arrays.BooleanArray(np.where(m, 0, v).astype(bool), m))
        if pdn == "object:bool":
            return pd.Series([None if mm else bool(x) for x, mm in zip(v, m)], dtype=object)
        if pdn[:1] in ("I", "U"):
            return pd.Series(pd.arrays.IntegerArray(np.where(m, 0, v).astype(np.int64), m)).astype(pdn)
        return pd.Series(v)
    if pdn == "bool":
        return pd.Series(v.astype(bool))
    if pdn in ("int64", "uint64", "int32", "int16", "int8", "uint8", "uint16", "uint32"):
        return pd.Series(v.astype(pdn))
    if pdn[:1] in ("I", "U") and spec["t"] == "f64":
        return pd.Series(pd.array([None if x != x else int(x) for x in v], dtype=pdn))
    return pd.Series(v)


def read_shard(path):
    """(header, arrays, tables) of a shard file: arrays {name: numpy array, exact bytes}, tables {name: DataFrame
    with the dtypes it was written with}."""
    head, arrays, raw = TR.read_shard(path)
    tables = {}
    for name, cols in raw.items():
        specs = {c["name"]: c for c in head["tables"][name]["cols"]}
        tables[name] = pd.DataFrame({k: _restore(specs[k], v) for k, v in cols.items()},
                                    index=pd.RangeIndex(head["tables"][name]["n"]))
    return head, arrays, tables


def split_container(body, take_arrays=(), take_tables=()):
    """Container surgery for the size guard: (kept, taken) headers and blob lists of a decoded container, the taken
    entries' bytes copied as they are (no re-encoding: the values stay the stored bytes)."""
    hl = struct.unpack("<I", body[4:8])[0]
    head = json.loads(body[8:8 + hl].decode("utf-8"))
    b0 = 8 + ((hl + 7) // 8) * 8
    keep, take = _Blobs(), _Blobs()
    hk = {**head, "arrays": {}, "tables": {}}
    ht = {**head, "arrays": {}, "tables": {}}

    def copy(spec, bl):
        raw = body[b0 + spec["off"]: b0 + spec["off"] + spec["n"]]
        return {**spec, **bl.raw(raw, spec["t"], spec.get("sh", 0), spec.get("shape"))}

    for k, spec in head.get("arrays", {}).items():
        bl, h = (take, ht) if k in take_arrays else (keep, hk)
        h["arrays"][k] = copy(spec, bl)
    for k, t in head.get("tables", {}).items():
        bl, h = (take, ht) if k in take_tables else (keep, hk)
        cols = []
        for c in t["cols"]:
            if c["t"] == "str":
                cols.append(c)
            elif c["t"] == "dict":
                cols.append({**c, "c": copy(c["c"], bl)})
            else:
                cols.append(copy(c, bl))
        h["tables"][k] = {**t, "cols": cols}
    return (hk, keep.parts), (ht, take.parts)


# ----------------------------------------------------------------------------- volumes (writing)
class Volume:
    """One output volume (web, data, data_dd) being written under OUT/explorer.tmp: shards are encoded by the caller,
    compressed and written by a thread pool (zlib and the file writes release the GIL)."""

    def __init__(self, root, name, prefix, run, pool, sem):
        self.root, self.name, self.prefix, self.run = root, name, prefix, run
        self.pool, self.sem = pool, sem
        self.futures = []
        self.lock = threading.Lock()
        self.files = {}                                        # relative path -> bytes
        os.makedirs(root, exist_ok=True)

    def rel(self, sid):
        return f"{self.prefix}{sid}.js"

    def shard(self, sid, kind, arrays=None, tables=None, meta=None):
        body = encode(sid, self.run, kind, arrays, tables, meta)
        self.submit(self.rel(sid), lambda: shard_text(sid, body))

    def raw_shard(self, sid, body):
        self.submit(self.rel(sid), lambda: shard_text(sid, body))

    def text(self, rel, text):
        self.submit(rel, lambda: text)

    def submit(self, rel, make):
        path = os.path.join(self.root, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.sem.acquire()
        try:
            self.futures.append(self.pool.submit(self._job, rel, path, make))
        except BaseException:
            self.sem.release()
            raise
        if len(self.futures) > 4096:
            self.wait()

    def _job(self, rel, path, make):
        try:
            data = make()
            b = data.encode("utf-8") if isinstance(data, str) else data
            with open(path, "wb") as fh:
                fh.write(b)
            with self.lock:
                self.files[rel] = len(b)
        finally:
            self.sem.release()

    def wait(self):
        fs, self.futures = self.futures, []
        for f in fs:
            f.result()

    def copy(self, src, rel, text=None):
        """A file copied (or text written) to <path>.tmp, then moved over <path> with common.replace_file: a hard
        link to the old file (an export) keeps its bytes, and on Windows a file held open is named, never left
        half-written."""
        path = os.path.join(self.root, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        if text is None:
            shutil.copyfile(src, tmp)
        else:
            with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
        replace_file(tmp, path)
        self.files[rel] = os.path.getsize(path)

    def remove(self, rel):
        remove_file(os.path.join(self.root, *rel.split("/")))
        self.files.pop(rel, None)

    def bytes(self, prefix=""):
        return sum(v for k, v in self.files.items() if k.startswith(prefix))


class Acct:
    """R1: which rows of each source table reached which view (a view = a table in a family of shards). Each record
    table carries _row (its row in the source), so a view's coverage is the set of rows it holds."""

    def __init__(self):
        self.n = {}                                            # source -> rows
        self.want = {}                                         # (source, view) -> rows the view must hold
        self.cov = {}                                          # (source, view) -> bool array

    def source(self, src, n):
        self.n[src] = int(n)

    def expect(self, src, view, n):
        self.want[(src, view)] = int(n)
        self.cov.setdefault((src, view), np.zeros(self.n[src], dtype=bool))

    def add(self, src, view, rows):
        c = self.cov.setdefault((src, view), np.zeros(self.n[src], dtype=bool))
        c[np.asarray(rows, dtype=np.int64)] = True

    def report(self):
        """{source: {"rows": n, "views": {view: [held, must hold]}}} and the views where they differ."""
        rep, bad = {}, []
        for (src, view), want in sorted(self.want.items()):
            got = int(self.cov[(src, view)].sum())
            rep.setdefault(src, {"rows": self.n[src], "views": {}})["views"][view] = [got, want]
            if got != want:
                bad.append(f"{src} -> {view}: {got:,} of {want:,} rows")
        for src, n in self.n.items():
            rep.setdefault(src, {"rows": n, "views": {}})
            if not any(w == n for (s, _v), w in self.want.items() if s == src):
                bad.append(f"{src}: no view holds all {n:,} rows")
        return rep, bad


# ----------------------------------------------------------------------------- sources (reading)
class Src:
    """The run's outputs the explorer reads (OUT/<stage>/...), on demand. A missing optional source gives an empty
    table and is listed in core.js meta 'missing' (the pages name the file and say it is missing)."""

    def __init__(self, out):
        self.out = out
        self.fx = os.path.join(out, "atlas", "effects")
        self.ix = read_effects_index(self.fx)
        g = self.ix["genes"]
        self.gK = int((g["kind"] == "gene").sum())
        self.C = len(g)
        self.D = len(self.ix["drugdose"])
        self.L = len(self.ix["lines"])
        self.W = len(self.ix["wells"])
        self.P = len(self.ix["plates"])
        self.missing = []
        self._cache = {}

    def path(self, rel):
        return os.path.join(self.out, *rel.split("/"))

    def has(self, rel):
        return os.path.exists(self.path(rel))

    def df(self, rel, cache=False):
        """The table as the pipeline wrote it, with _row (its row number) as the first column."""
        if rel in self._cache:
            return self._cache[rel]
        p = self.path(rel)
        if not os.path.exists(p):
            if rel not in self.missing:
                self.missing.append(rel)
            df = pd.DataFrame()
        elif rel.endswith(".parquet"):
            df = pd.read_parquet(p)
        else:
            df = pd.read_csv(p)
        df = _compact_strings(df.reset_index(drop=True))
        df.insert(0, "_row", np.arange(len(df), dtype=np.int32))
        if cache:
            self._cache[rel] = df
        return df

    def drop(self, rel):
        self._cache.pop(rel, None)

    def npy(self, rel, mmap=True):
        p = self.path(rel)
        if not os.path.exists(p):
            if rel not in self.missing:
                self.missing.append(rel)
            return None
        return np.load(p, mmap_mode="r" if mmap else None)

    def json(self, rel):
        p = self.path(rel)
        if not os.path.exists(p):
            return None
        try:
            with open(p, encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return None

    def text(self, rel, root=None):
        p = os.path.join(root, *rel.split("/")) if root else self.path(rel)
        if not os.path.exists(p):
            return None
        with open(p, encoding="utf-8", errors="replace") as fh:
            return fh.read()


def _compact_strings(df):
    """Columns held as Python objects get a typed dtype, values unchanged: text as pyarrow strings (a fraction of the
    memory of Python strings under pandas 2; pandas 3 reads them so already), True / False / missing as pandas
    'boolean' (so that every file stores such a column the same way, whatever rows it holds)."""
    for c in df.columns:
        if df[c].dtype != object or not len(df):
            continue
        kind = pd.api.types.infer_dtype(df[c], skipna=True)
        try:
            if kind == "string":
                df[c] = df[c].astype("string[pyarrow]")
            elif kind == "boolean":
                df[c] = df[c].astype("boolean")
        except (ImportError, TypeError, ValueError):
            continue
    return df


def run_id(out):
    """The first 12 hex characters of sha256 over the sorted (stage, version, finished) of every other stage's stamp
    and this module's VERSION: shards of another run are refused by the pages."""
    recs = []
    for p in sorted(glob.glob(os.path.join(out, "stages", "*.json"))):
        st = read_stamp(out, os.path.basename(p)[:-5])
        if st and st.get("stage") != "explorer":
            recs.append([str(st.get("stage")), str(st.get("version")), str(st.get("finished"))])
    recs.sort()
    blob = json.dumps({"stamps": recs, "explorer": VERSION}, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:12]


def assets_sha(app_dir=APP_DIR):
    """sha256 over tahoemap/explorer_app/** (paths and bytes); None when the folder is missing."""
    if not os.path.isdir(app_dir):
        return None
    h = hashlib.sha256()
    for root, dirs, files in os.walk(app_dir):
        dirs.sort()
        for f in sorted(files):
            p = os.path.join(root, f)
            h.update(os.path.relpath(p, app_dir).replace(os.sep, "/").encode("utf-8") + b"\0")
            with open(p, "rb") as fh:
                h.update(fh.read().replace(b"\r\n", b"\n"))
    return h.hexdigest()


def _github_repo(code_root=CODE_ROOT):
    """(owner, repo) of the code checkout's origin on github.com, or None."""
    url = git_out(find_git(), code_root, "remote", "get-url", "origin", timeout=10) or ""
    m = re.search(r"github\.com[:/]+([^/]+)/([^/]+?)(?:\.git)?/?$", url.strip())
    return (m.group(1), m.group(2)) if m else None


def _peak_rss_mb():
    """Peak resident memory of this process in MB (None where it cannot be told)."""
    try:
        import resource
        r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return round(r / (1024.0 * 1024.0) if sys.platform == "darwin" else r / 1024.0, 1)
    except (ImportError, OSError, ValueError):
        pass
    try:
        import psutil
        mi = psutil.Process().memory_info()
        return round(getattr(mi, "peak_wset", mi.rss) / 1e6, 1)
    except Exception:  # noqa: BLE001
        pass
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes

            class PMC(ctypes.Structure):
                _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
                            ("PeakWorkingSetSize", ctypes.c_size_t), ("WorkingSetSize", ctypes.c_size_t),
                            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                            ("QuotaNonPagedPoolUsage", ctypes.c_size_t), ("PagefileUsage", ctypes.c_size_t),
                            ("PeakPagefileUsage", ctypes.c_size_t)]
            c = PMC()
            c.cb = ctypes.sizeof(PMC)
            h = ctypes.windll.kernel32.GetCurrentProcess()
            if ctypes.windll.psapi.GetProcessMemoryInfo(h, ctypes.byref(c), c.cb):
                return round(c.PeakWorkingSetSize / 1e6, 1)
        except Exception:  # noqa: BLE001
            return None
    return None


def _slices(keys, starts, stops):
    """Row ranges [a, b) of sorted integer keys for each [start, stop)."""
    return np.searchsorted(keys, starts, "left"), np.searchsorted(keys, stops, "left")


class Keyed:
    """A table sorted (stably) by one or two integer key columns, sliced by key range."""

    def __init__(self, df, *keys):
        self.df = df
        self.idx = {}
        for k in keys:
            if k in df:
                v = pd.to_numeric(df[k], errors="coerce").fillna(-1).to_numpy(dtype=np.int64)
            else:
                v = np.full(len(df), -1, dtype=np.int64)
            o = np.argsort(v, kind="stable")
            self.idx[k] = (o, v[o])

    def pos(self, k, lo, hi):
        """Row positions (into df) whose key k is in [lo, hi)."""
        o, v = self.idx[k]
        a, b = np.searchsorted(v, lo, "left"), np.searchsorted(v, hi, "left")
        return o[a:b]

    def rows(self, lo, hi, *keys):
        """The rows with any of the keys in [lo, hi), in source order (each once)."""
        keys = keys or tuple(self.idx)
        p = np.unique(np.concatenate([self.pos(k, lo, hi) for k in keys])) if keys else np.zeros(0, np.int64)
        return self.df.iloc[p]


# ----------------------------------------------------------------------------- the build
def _rmtree(path):
    """Remove a folder tree; on Windows a file in use is retried and named (common.remove_file)."""
    if not os.path.isdir(path):
        return
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            p = os.path.join(root, f)
            try:
                remove_file(p)
            except PermissionError:
                os.chmod(p, 0o666)
                remove_file(p)
        for d in dirs:
            os.rmdir(os.path.join(root, d))
    os.rmdir(path)


def _names(df, col):
    return df[col].fillna("").astype(str).to_numpy(dtype=object) if col in df else np.full(len(df), "", object)


class NpyRows:
    """A C-order .npy file read along its first axis with plain file reads (seek + readinto): rows(a, b) is a new
    array of rows a..b-1, exact. Unlike np.load(mmap_mode='r'), the pages read do not stay mapped in the process, so
    its peak memory counts only the blocks in use."""

    def __init__(self, path):
        self.path = path
        self.fh = open(path, "rb")
        version = np.lib.format.read_magic(self.fh)
        read = {(1, 0): np.lib.format.read_array_header_1_0, (2, 0): np.lib.format.read_array_header_2_0}.get(
            tuple(version))
        shape, fortran, dtype = read(self.fh) if read else np.lib.format._read_array_header(self.fh, version)
        if fortran:
            self.fh.close()
            raise SystemExit(f"explorer: {path} is stored in Fortran order; expected C order (the tensor stage's)")
        self.shape, self.dtype, self.offset = tuple(shape), np.dtype(dtype), self.fh.tell()
        self.row_bytes = int(np.prod(self.shape[1:], dtype=np.int64)) * self.dtype.itemsize

    def rows(self, a, b):
        a, b = max(0, int(a)), min(self.shape[0], int(b))
        arr = np.empty((max(0, b - a),) + self.shape[1:], dtype=self.dtype)
        if arr.size:
            self.fh.seek(self.offset + a * self.row_bytes)
            got = self.fh.readinto(memoryview(arr).cast("B"))
            if got != arr.nbytes:
                raise SystemExit(f"explorer: {self.path} ended early (rows {a}-{b}: {got:,} of {arr.nbytes:,} bytes)")
        return arr

    def close(self):
        self.fh.close()


class Build:
    """One explorer build: OUT/explorer.tmp/{web,data[,data_dd]} written step by step (A..G), then swapped in."""

    def __init__(self, out, site_url=None, data_url=None, line_dd=False, pages_max_mb=PAGES_MAX_MB, pooled_r=False):
        self.out = os.path.abspath(out)
        self.site_url, self.data_url, self.line_dd = site_url, data_url, bool(line_dd)
        self.pages_max_mb, self.pooled_r = float(pages_max_mb), bool(pooled_r)
        self.S = S = Src(self.out)
        self.run = run_id(self.out)
        self.tmp = os.path.join(self.out, "explorer.tmp")
        _rmtree(self.tmp)
        self.workers = max(1, min(8, os.cpu_count() or 1))
        self.pool = cf.ThreadPoolExecutor(max_workers=self.workers)
        self.sem = threading.BoundedSemaphore(3 * self.workers)
        self.web = Volume(os.path.join(self.tmp, "web"), "web", "d/", self.run, self.pool, self.sem)
        self.data = Volume(os.path.join(self.tmp, "data"), "data", "", self.run, self.pool, self.sem)
        self.ddv = (Volume(os.path.join(self.tmp, "data_dd"), "data_dd", "", self.run, self.pool, self.sem)
                    if self.line_dd else None)
        self.acct = Acct()
        self.times, self.warnings, self.moves = {}, [], []
        self.checks = {}
        self.gK, self.C, self.D, self.L, self.W, self.P = S.gK, S.C, S.D, S.L, S.W, S.P
        self.genes = self.load("tables/genes.parquet", cache=True)
        self.sym = _names(S.ix["genes"], "symbol")
        self.label = _names(S.ix["genes"], "label")
        self.drugs = self.load("tables/drugs.parquet", cache=True)
        if not len(self.drugs):
            names = sorted(dict.fromkeys(_names(S.ix["drugdose"], "drug")))
            self.drugs = pd.DataFrame({"_row": np.arange(len(names), dtype=np.int32), "drug": names})
        self.drug_names = _names(self.drugs, "drug")
        self.drug_i = {d: i for i, d in enumerate(self.drug_names)}
        self.dd_drug = _names(S.ix["drugdose"], "drug")
        self.drug_of_dd = np.array([self.drug_i.get(d, -1) for d in self.dd_drug], dtype=np.int32)
        ln = S.ix["lines"]
        names = _names(ln, "cell_name") if "cell_name" in ln else _names(ln, "cell_line_id")
        self.line_name = np.where(names == "", _names(ln, "cell_line_id"), names).astype(object)
        self.line_id = _names(ln, "cell_line_id")
        self.tinfo = S.json("tables/info.json") or {}
        self.t_line = float(self.tinfo.get("line_z_threshold", TB.LINE_Z_FLOOR))
        self.vault = self._vault_paths()

    # ---- helpers
    def load(self, rel, cache=False):
        df = self.S.df(rel, cache=cache)
        if rel not in self.acct.n:
            self.acct.source(rel, len(df))
        return df

    def want(self, rel, view, n=None):
        self.acct.expect(rel, view, self.acct.n[rel] if n is None else n)

    def got(self, rel, view, df):
        if len(df):
            self.acct.add(rel, view, df["_row"].to_numpy())

    def step(self, name, fn):
        t0 = time.time()
        log(f"  explorer step {name} ...")
        fn()
        for v in self.volumes():
            v.wait()
        self.times[name] = round(time.time() - t0, 1)
        log(f"  explorer step {name} done in {self.times[name]:.1f} s (peak memory {_peak_rss_mb()} MB)")

    def volumes(self):
        return [v for v in (self.web, self.data, self.ddv) if v is not None]

    def _vault_paths(self):
        """vault/.tahoemap-paths.json (written by the vault stage): note paths by gene col, drug, line, module, plate;
        else every link goes to vault/Home.md."""
        d = self.S.json("vault/.tahoemap-paths.json")
        if not isinstance(d, dict):
            return {"available": False, "home": "vault/Home.md"}
        return {"available": True, "home": "vault/Home.md", **{k: v for k, v in d.items() if isinstance(v, dict)}}

    def vault_path(self, kind, *keys):
        """The vault note of an entity (the first of keys the paths file knows), 'vault/...'; vault/Home.md without the
        paths file; None when the paths file has no note for it."""
        if not self.vault.get("available"):
            return self.vault["home"]
        d = self.vault.get(kind) or {}
        for k in keys:
            p = d.get(str(k))
            if p:
                p = str(p).replace("\\", "/")
                return p if p.startswith("vault/") else "vault/" + p
        return None

    # ---------------------------------------------------------------- step A: the small web files
    def step_a(self):
        self.a_genes()
        self.a_search()
        self.a_below()
        self.a_ddarr()
        self.a_space()
        self.a_linecpm()
        self.a_sets()
        self.a_groups()
        self.a_val()
        self.a_docs()
        self.a_files()

    def a_genes(self):
        S = self.S
        ag = S.ix["genes"].reset_index(drop=True).copy()
        ag.insert(0, "_row", np.arange(len(ag), dtype=np.int32))
        self.acct.source("atlas/effects/genes.csv", len(ag))
        eg = self.load("embed/genes.parquet")
        for rel, df in (("tables/genes.parquet", self.genes), ("embed/genes.parquet", eg),
                        ("atlas/effects/genes.csv", ag)):
            self.want(rel, "genes.js")
            self.got(rel, "genes.js", df)
        self.web.shard("genes", "genes", tables={"genes": self.genes, "egenes": eg, "agenes": ag},
                       meta={"what": "every column of tables/genes.parquet (genes), embed/genes.parquet (egenes) "
                                     "and atlas/effects/genes.csv (agenes: also the 3 summed modules)"})

    def a_search(self):
        g = self.genes
        keep = [c for c in ("col", "symbol", "label", "ensembl_id", "noise_rna") if c in g]
        tg = g[["_row"] + keep].copy()
        ann = self.load("reference/annotations.parquet", cache=True)
        ac = [c for c in ("hgnc_id", "hgnc_symbol", "name", "aliases", "prev_symbols", "entrez_id", "uniprot",
                          "location", "chrom", "biotype", "locus_type") if c in ann]
        if len(ann) and "col" in ann and "col" in tg:
            tg = tg.merge(ann[["col"] + ac].drop_duplicates("col"), on="col", how="left", sort=False)
        eg = self.load("embed/genes.parquet")
        if "included" in eg and "col" in tg:
            tg = tg.merge(eg[["col", "included"]].drop_duplicates("col"), on="col", how="left", sort=False)
        nodes = self.load("graph/nodes.parquet", cache=True)
        if len(nodes) and "col" in tg and {"col", "module"} <= set(nodes.columns):
            # module (0 = in the space, in no module; empty = not in the vector space) and arm of every gene
            nd = nodes[["col", "module"] + (["arm"] if "arm" in nodes else [])].drop_duplicates("col")
            tg = tg.merge(nd, on="col", how="left", sort=False)
            tg["module"] = tg["module"].astype("Int32")
        td = self.drugs[[c for c in ("_row", "drug", "salt_base", "targets", "moa_fine", "moa_broad", "approved")
                         if c in self.drugs]]
        ln = self.load("tables/lines.parquet", cache=True)
        tl = ln[[c for c in ("_row", "line", "cell_name", "cell_line_id", "Cell_ID_DepMap", "Organ", "drivers",
                             "driver_changes", "tp53_status") if c in ln]]
        mods = self.load("graph/modules.parquet", cache=True)
        labs = self.load("validation/module_labels.csv", cache=True)
        tm = mods[[c for c in ("_row", "module", "n_genes", "top_plus", "top_minus") if c in mods]].copy()
        if len(labs) and "label" in labs and "module" in tm:
            tm = tm.merge(labs[["module", "label"]].drop_duplicates("module"), on="module", how="left", sort=False)
        gs = self.load("reference/gene_sets.parquet", cache=True)
        sc = [c for c in ("source", "set", "set_id", "set_size", "n_present") if c in gs]
        ts = gs[sc].drop_duplicates(subset=[c for c in ("source", "set") if c in gs]) if sc else pd.DataFrame()
        gr = self.load("direction/groups.parquet", cache=True)
        tq = gr[[c for c in ("_row", "group_id", "kind", "gene", "gene_col", "description") if c in gr]]
        self.web.shard("search", "search", tables={"g": tg, "d": td, "l": tl, "m": tm, "s": ts.reset_index(drop=True),
                                                   "q": tq},
                       meta={"what": "the fields the search box looks in: genes (g), drugs (d), lines (l), modules "
                                     "(m), gene sets (s), direction groups (q); genes below the detection cut are in "
                                     "below.js"})

    def a_below(self):
        from . import tlib as T
        fi = self.S.json("atlas/file_index.json") or {}
        files = [f for f in fi.get("gene", []) or [] if os.path.exists(f)]
        meta = {"what": "Tahoe genes below the atlas's detection cut (pooled level under 2 CPM): they have no column "
                        "and no effects; listed so that a missing gene is not mistaken for an unknown one"}
        tab = pd.DataFrame({"symbol": pd.Series([], dtype=object), "ensembl_id": pd.Series([], dtype=object),
                            "token_id": pd.Series([], dtype=np.int64)})
        if files:
            gm = T.read_tables(files, ["token_id", "gene_symbol", "ensembl_id"])
            tok = set(pd.to_numeric(self.S.ix["genes"]["token"][:self.gK], errors="coerce").dropna().astype(int))
            gm = gm[~gm["token_id"].isin(tok)]
            sy = gm["gene_symbol"].fillna(gm["ensembl_id"]).astype(str)
            tab = pd.DataFrame({"symbol": sy.to_numpy(dtype=object),
                                "ensembl_id": gm["ensembl_id"].astype(object).to_numpy(),
                                "token_id": pd.to_numeric(gm["token_id"], errors="coerce").to_numpy()})
            o = sorted(range(len(tab)), key=lambda i: (tab["symbol"].iat[i].lower(), tab["symbol"].iat[i],
                                                         str(tab["ensembl_id"].iat[i])))
            tab = tab.iloc[o].reset_index(drop=True)
            meta.update(available=True, source="Tahoe gene metadata (atlas/file_index.json 'gene': "
                                               + ", ".join(os.path.basename(f) for f in files) + ")")
        else:
            meta.update(available=False, reason="the Tahoe gene metadata is not reachable from this run "
                                                "(atlas/file_index.json 'gene' lists no existing file)")
        self.n_below = len(tab)
        self.web.shard("below", "below", tables={"b": tab}, meta=meta)

    def a_ddarr(self):
        S = self.S
        arrays, missing = {}, []
        for name, rel in (("DD_A", "atlas/effects/DD_A.npy"), ("DD_Az", "atlas/effects/DD_Az.npy"),
                          ("DD_beta", "atlas/effects/DD_beta.npy"), ("DD_rcor", "atlas/effects/DD_rcor.npy"),
                          ("DD_r2_modules", "atlas/effects/DD_r2_modules.npy"),
                          ("well_line_cells", "tensor/well_line_cells.npy"),
                          ("well_line_umi", "tensor/well_line_umi.npy"),
                          ("module_pooled_z", "graph/module_pooled_z.npy"),
                          ("drugdose_vectors", "embed/drugdose_vectors.npy"),
                          ("drug_vectors", "embed/drug_vectors.npy"),
                          ("line_baseline_vectors", "embed/line_baseline_vectors.npy"),
                          ("line_response_vectors", "embed/line_response_vectors.npy"),
                          ("singular_values", "embed/singular_values.npy"),
                          ("A2", "atlas/effects/A2.npy"), ("zA", "atlas/effects/zA.npy"),
                          ("VA", "atlas/effects/VA.npy"),
                          ("wbeta", "atlas/effects/beta.npy"), ("wrcor", "atlas/effects/rcor.npy"),
                          ("wr2", "atlas/effects/r2_modules.npy")):
            a = S.npy(rel, mmap=False)
            if a is None:
                missing.append(rel)
            else:
                arrays[name] = a
        wells = S.ix["wells"]
        min_cells = int(S.ix["info"].get("min_cells") or 30)
        usable = np.zeros((self.D, self.L), dtype=np.uint8)
        if "well_line_cells" in arrays:
            ddr = wells["drugdose_row"].to_numpy(dtype=np.int64)
            used = wells["used_in_drugdose"].to_numpy(dtype=bool) & (ddr >= 0)
            np.add.at(usable, ddr[used], (arrays["well_line_cells"][used] >= min_cells).astype(np.uint8))
        arrays["usable"] = usable
        ctx = self.load("embed/contexts.parquet")
        self.want("embed/contexts.parquet", "ddarr.js")
        self.got("embed/contexts.parquet", "ddarr.js", ctx)
        self.web.shard("ddarr", "ddarr", arrays=arrays, tables={"contexts": ctx},
                       meta={"min_cells": min_cells, "missing": missing,
                             "usable": "used wells of the drug-dose where the line has at least min_cells cells "
                                       "(0: the line has no value there for that reason)",
                             "sources": {"DD_*": "atlas/effects", "wbeta, wrcor, wr2": "atlas/effects/beta.npy, "
                                         "rcor.npy, r2_modules.npy (per well x line)",
                                         "module_pooled_z": "graph/module_pooled_z.npy (row m-1 = module m)"}})

    def a_space(self):
        S = self.S
        inc = S.npy("embed/included_cols.npy", mmap=False)
        if inc is None:
            return
        inc = np.asarray(inc, dtype=np.int64)
        for name, rel in (("u", "embed/gene_unit.npy"), ("h1", "embed/gene_unit_half1.npy"),
                          ("h2", "embed/gene_unit_half2.npy")):
            U = S.npy(rel, mmap=False)
            if U is None:
                continue
            rest = np.ones(len(U), dtype=bool)
            rest[inc] = False
            only = bool(np.isnan(U[rest]).all())
            arrays = {"included": inc.astype(np.int32), "unit": U[inc] if only else U}
            meta = {"source": rel, "rows": "included" if only else "all",
                    "what": ("rows of included_cols (every other row of the file is NaN: genes outside the space)"
                             if only else "every row of the file")}
            if name == "u":
                for k, r in (("row_mean", "embed/gene_row_mean.npy"), ("row_scale", "embed/gene_row_scale.npy")):
                    a = S.npy(r, mmap=False)
                    if a is not None:
                        arrays[k] = a
            self.web.shard(f"space/{name}", "space", arrays=arrays, meta=meta)
        cv = S.npy("embed/context_vectors.npy", mmap=False)
        if cv is not None:
            self.web.shard("space/ctx", "space", arrays={"vectors": cv},
                           meta={"source": "embed/context_vectors.npy", "rows": "embed/contexts.parquet j"})

    def a_linecpm(self):
        S = self.S
        arrays = {}
        for name, rel in (("line_cpm", "atlas/effects/line_cpm.npy"), ("expr_mask", "atlas/effects/expr_mask.npy"),
                          ("line_measured", "tensor/line_measured.npy")):
            a = S.npy(rel, mmap=False)
            if a is not None:
                arrays[name] = a
        self.web.shard("linecpm", "linecpm", arrays=arrays,
                       meta={"what": "lines x columns: baseline CPM (line_cpm), the atlas's expression rule "
                                     "(expr_mask), lines x genes: the line truly expresses the gene (line_measured)"})

    def a_sets(self):
        gs = self.load("reference/gene_sets.parquet", cache=True)
        self.want("reference/gene_sets.parquet", "sets.js")
        self.got("reference/gene_sets.parquet", "sets.js", gs)
        self.web.shard("sets", "sets", tables={"sets": gs}, meta={"source": "reference/gene_sets.parquet"})

    def a_groups(self):
        """groups.js, and the comparison index the dg/ files use: every group (by group_id), then every edge 'group'
        text that names no group (by text). An edge belongs to the group whose description is its 'group' text."""
        gr = self.load("direction/groups.parquet", cache=True)
        ed = self.load("direction/edges.parquet", cache=True)
        order = (np.argsort(_names(gr, "group_id"), kind="stable") if len(gr) else np.zeros(0, dtype=np.int64))
        cmp_of_group = np.zeros(len(gr), dtype=np.int32)
        cmp_of_group[order] = np.arange(len(gr), dtype=np.int32)
        by_desc = {}
        desc = _names(gr, "description")
        for r in order:
            by_desc.setdefault(desc[r], int(cmp_of_group[r]))
        etext = _names(ed, "group")
        extra = sorted(set(etext) - set(by_desc))
        ex_k = {t: len(gr) + i for i, t in enumerate(extra)}
        self.edge_cmp = np.array([by_desc[t] if t in by_desc else ex_k[t] for t in etext], dtype=np.int32)
        self.group_cmp = cmp_of_group
        self.n_cmp = len(gr) + len(extra)
        g2 = gr.copy()
        g2["_cmp"] = cmp_of_group
        g2["_dg"] = (cmp_of_group // DG_PER_SHARD).astype(np.int32)
        kinds = {}
        ek = _names(ed, "kind")
        for k, kd in zip(self.edge_cmp, ek):
            kinds.setdefault(int(k), set()).add(kd)
        cnt = np.bincount(self.edge_cmp, minlength=self.n_cmp) if self.n_cmp else np.zeros(0, np.int64)
        ks = np.array([ex_k[t] for t in extra], dtype=np.int32)
        cmp_df = pd.DataFrame({"_cmp": ks, "text": pd.Series(extra, dtype=object),
                               "kinds": pd.Series([", ".join(sorted(kinds.get(int(k), ()))) for k in ks], dtype=object),
                               "n_edges": cnt[ks].astype(np.int32) if len(ks) else np.zeros(0, np.int32),
                               "_dg": (ks // DG_PER_SHARD).astype(np.int32)})
        g2["_n_edges"] = cnt[cmp_of_group].astype(np.int32) if len(gr) else np.zeros(0, np.int32)
        self.want("direction/groups.parquet", "groups.js")
        self.got("direction/groups.parquet", "groups.js", g2)
        self.web.shard("groups", "groups", tables={"groups": g2, "cmp": cmp_df},
                       meta={"what": "every direction group (every column), with _cmp (its comparison number), _dg "
                                     "(its d/dg/ file) and _n_edges (its arrows); cmp lists the comparisons that "
                                     "only arrows name (drug targets, gene levels)", "per_shard": DG_PER_SHARD})

    def a_val(self):
        tabs = {}
        for name, rel in (("control_sets", "validation/control_sets.csv"), ("drug_moa", "validation/drug_moa.csv"),
                          ("module_enrichment", "validation/module_enrichment.csv"),
                          ("module_labels", "validation/module_labels.csv"),
                          ("novel_edges", "validation/novel_edges.csv"),
                          ("novel_members", "validation/novel_members.csv"),
                          ("opposite_pairs", "validation/opposite_pairs.csv"),
                          ("well_position_check", "atlas/well_position_check.csv")):
            df = self.load(rel, cache=rel != "atlas/well_position_check.csv")
            self.want(rel, "val.js")
            self.got(rel, "val.js", df)
            tabs[name] = df
        S = self.S
        self.web.shard("val", "val", tables=tabs,
                       meta={"metrics": S.json("validation/metrics.json"), "report": S.text("validation/report.md"),
                             "direction_controls": S.json("direction/controls.json")})

    def a_docs(self):
        S = self.S
        docs = {rel: S.text(rel) for rel in DOC_FILES if S.has(rel)}
        dd = os.path.join(CODE_ROOT, "docs")
        if os.path.isdir(dd):
            for f in sorted(os.listdir(dd)):
                if f.endswith(".md"):
                    docs["docs/" + f] = S.text(f, root=dd)
        self.web.shard("docs", "docs", meta={"docs": docs})

    def a_files(self):
        """files.js: the "What is where" table (INVENTORY) with the files and bytes of each pattern in this OUT."""
        n, b, unmapped = {}, {}, []
        skip = {"explorer", "explorer.tmp", "explorer.old"}
        for root, dirs, files in os.walk(self.out):
            rel_root = os.path.relpath(root, self.out).replace(os.sep, "/")
            if rel_root == ".":
                dirs[:] = sorted(d for d in dirs if d not in skip)
            else:
                dirs.sort()
            for f in sorted(files):
                rel = f if rel_root == "." else f"{rel_root}/{f}"
                if rel in ("stages/explorer.json", "stages/explorer.json.tmp"):
                    continue                                   # this stage's own record (written after the files)
                p = inventory_pattern(rel)
                try:
                    sz = os.path.getsize(os.path.join(root, f))
                except OSError:
                    sz = 0
                if p is None:
                    unmapped.append((rel, sz))
                    continue
                n[p] = n.get(p, 0) + 1
                b[p] = b.get(p, 0) + sz
        tab = pd.DataFrame({"pattern": [p for p, *_ in INVENTORY], "where": [w for _, w, _, _ in INVENTORY],
                            "view": [v for _, _, v, _ in INVENTORY], "what": [x for *_, x in INVENTORY],
                            "files": np.array([n.get(p, 0) for p, *_ in INVENTORY], dtype=np.int64),
                            "bytes": np.array([b.get(p, 0) for p, *_ in INVENTORY], dtype=np.float64)})
        um = pd.DataFrame({"path": pd.Series([u for u, _ in unmapped], dtype=object),
                           "bytes": np.array([s for _, s in unmapped], np.float64)})
        self.unmapped = [u for u, _ in unmapped]
        if unmapped:
            self.warnings.append(f"{len(unmapped)} file(s) of OUT are not described in explorer.INVENTORY: "
                                 + ", ".join(self.unmapped[:20]) + (" ..." if len(unmapped) > 20 else ""))
        self.web.shard("files", "files", tables={"files": tab, "unmapped": um},
                       meta={"what": "every file pattern of the output folder, where it is in the explorer (or why "
                                     "not), the view that shows it, and its files and bytes in this run"})

    # ---------------------------------------------------------------- step B: the per-line pass (data x/, nl)
    def step_b(self):
        S = self.S
        if S.npy("tensor/DDL_lfc.npy") is None or S.npy("tensor/DDL_z.npy") is None:
            raise SystemExit("explorer: tensor/DDL_lfc.npy or DDL_z.npy is missing; run the 'tensor' stage first")
        # the per-line tensor is read block by block with plain file reads, not mapped: a mapped file's pages stay
        # in the process while it runs and would count in its peak memory (2 x 1.9 GB on the real data)
        DL, DZ = NpyRows(S.path("tensor/DDL_lfc.npy")), NpyRows(S.path("tensor/DDL_z.npy"))
        try:
            self._step_b(S, DL, DZ)
        finally:
            DL.close()
            DZ.close()

    def _step_b(self, S, DL, DZ):
        gK, C, D = self.gK, self.C, self.D
        meas = np.asarray(S.npy("tensor/line_measured.npy", mmap=False), dtype=bool)
        W1, W2, WZ = (S.npy(f"atlas/effects/{n}.npy") for n in ("W1", "W2", "Z"))
        CNT, PU = S.npy("tensor/well_counts.npy"), S.npy("atlas/effects/posunc.npy")
        PE = S.npy("atlas/effects/DD_poseff.npy")
        PB = S.npy("tensor/plate_base.npy")
        small = {k: S.npy(r, mmap=False) for k, r in (("poff", "atlas/effects/plate_offset.npy"),
                                                       ("slot", "atlas/effects/slot_median.npy"),
                                                       ("psg", "atlas/effects/plate_scale_gene.npy"))}
        small = {k: np.ascontiguousarray(np.asarray(v).T) for k, v in small.items() if v is not None}
        self.NL = np.full((C, D, 5), U8_NA, dtype=np.uint8)
        de = self.load("tables/drug_effects.parquet", cache=True)
        dk = Keyed(de, "col")
        dcol, ddd = (pd.to_numeric(de[c]).to_numpy(np.int64) for c in ("col", "dd")) if len(de) else (None, None)
        lu_bad = 0
        lu_n = 0

        def cols_T(M, g0, g1):
            return None if M is None else np.ascontiguousarray(np.asarray(M[:, g0:g1]).T)

        for g0 in range(0, gK, LINE_CHUNK):
            g1 = min(gK, g0 + LINE_CHUNK)
            rl, rz = DL.rows(g0, g1), DZ.rows(g0, g1)                        # genes x drug-doses x lines, exact
            Z, X = rz.astype(np.float32), rl.astype(np.float32)
            masks = TB.line_counts(Z, X, self.t_line, measured=meas[:, g0:g1], masks=True)
            self.NL[g0:g1] = np.stack([m.sum(axis=2) for m in masks], axis=-1).astype(np.uint8)
            pos = dk.pos("col", g0, g1)
            if pos.size:                                                    # drug_effects lines_up / lines_down
                gi, di = dcol[pos] - g0, ddd[pos]
                Zm = np.where(meas[:, g0:g1].T[:, None, :], Z, np.nan)[gi, di]
                lu = TB._line_lists(self.line_name, Zm, masks[1][gi, di], 1)
                ld = TB._line_lists(self.line_name, Zm, masks[2][gi, di], -1)
                lu_bad += int((lu != de["lines_up"].iloc[pos].fillna("").to_numpy(dtype=object)).sum())
                lu_bad += int((ld != de["lines_down"].iloc[pos].fillna("").to_numpy(dtype=object)).sum())
                lu_n += 2 * pos.size
            del Z, X, masks
            w = {k: cols_T(M, g0, g1) for k, M in (("w1", W1), ("w2", W2), ("wz", WZ), ("counts", CNT),
                                                     ("wpu", PU), ("poseff", PE))}
            pb = None if PB is None else np.ascontiguousarray(np.asarray(PB[:, :, g0:g1]).transpose(2, 0, 1))
            for i, col in enumerate(range(g0, g1)):
                arrays = {"lfc": rl[i], "z": rz[i]}
                for k in ("poseff", "w1", "w2", "wz", "counts", "wpu"):
                    if w[k] is not None:
                        arrays[k] = w[k][i]
                if pb is not None:
                    arrays["pbase"] = pb[i]
                for k, v in small.items():
                    arrays[k] = v[col]
                self.data.shard(x_id(col), "gene-lines", arrays=arrays,
                                meta={"col": col, "symbol": self.sym[col], "label": self.label[col]})
            if (g0 // LINE_CHUNK) % 16 == 0 or g1 == gK:
                log(f"    per-line pass: genes {g0:,}-{g1:,} of {gK:,} (peak memory {_peak_rss_mb()} MB)")
        for col in range(gK, C):                                            # the summed modules
            arrays = {}
            for k, M in (("poseff", PE), ("w1", W1), ("w2", W2), ("wz", WZ), ("wpu", PU)):
                if M is not None:
                    arrays[k] = np.asarray(M[:, col])
            for k, v in small.items():
                arrays[k] = v[col]
            self.data.shard(x_id(col), "gene-lines", arrays=arrays,
                            meta={"col": col, "symbol": self.sym[col], "label": self.label[col], "module": True,
                                  "absent": "per-line values, raw counts and plate baselines: the tensor holds genes "
                                            "only (a summed module has no per-line layer)"})
        self.checks["lines_up_down"] = {"compared": lu_n, "different": lu_bad,
                                        "rule": "drug_effects lines_up / lines_down (12 names at most) equal the "
                                                "names computed from the per-line values (tables._line_lists)"}
        if lu_bad:
            raise SystemExit(f"explorer: {lu_bad:,} of {lu_n:,} drug_effects lines_up / lines_down differ from the "
                             "per-line values (tensor and tables do not match: rerun 'tables')")

    # ---------------------------------------------------------------- step C: pooled values, flags, data p/
    def step_c(self):
        S = self.S
        gK, C, D = self.gK, self.C, self.D
        fx = S.fx

        def full(name):
            return np.array(np.load(os.path.join(fx, f"{name}.npy"), mmap_mode="r"), dtype=np.float32)

        self.LFC, self.Zp, self.QU, self.QD = (full(n) for n in ("DD_lfc", "DD_z", "DD_qup", "DD_qdn"))
        self.PEp = full("DD_poseff") if S.has("atlas/effects/DD_poseff.npy") else np.zeros((D, C), np.float32)
        F = TB.gene_flag_inputs(self.out)
        if F["gK"] != gK:
            raise SystemExit(f"explorer: tables.gene_flag_inputs gives {F['gK']} genes, the effects {gK}")
        dd_flags = F["dd_flags"]
        pu, pe, ps, sh, cl = F["posunc"], F["poseff"], F["pscale"], F["cc_share"], F["cc_cleared"]
        self.flag_s, self.flag_ix = [""], {"": 0}
        FL = np.zeros((D, C), dtype=np.uint32)
        for d0 in range(0, D, FLAG_CHUNK):
            d1 = min(D, d0 + FLAG_CHUNK)
            d = np.repeat(np.arange(d0, d1), gK)
            g = np.tile(np.arange(gK), d1 - d0)
            s, _ = TB.flag_strings(dd_flags, d, pu[d, g], pe[d, g], ps[d, g], TB.cc_pct(sh[d, g], cl[d, g]))
            FL[d0:d1, :gK] = self._codes(s).reshape(d1 - d0, gK)
        if C > gK:                       # the summed modules: the atlas's gene-level rule on the module's column
            pum = np.asarray(np.load(os.path.join(fx, "DD_posunc.npy"), mmap_mode="r")[:, gK:], dtype=bool) \
                if S.has("atlas/effects/DD_posunc.npy") else np.zeros((D, C - gK), dtype=bool)
            psm = TB._dd_gene_scale(S.ix["wells"], fx, D, C)[:, gK:]
            d = np.repeat(np.arange(D), C - gK)
            g = np.tile(np.arange(C - gK), D)
            s, _ = TB.flag_strings(dd_flags, d, pum[d, g], self.PEp[:, gK:][d, g], psm[d, g], None)
            FL[:, gK:] = self._codes(s).reshape(D, C - gK)
        n_codes = len(self.flag_s)
        self.FL = FL.astype(np.uint16) if n_codes <= 65536 else FL
        self.flag_clean = np.array([not A.has_artifact(x) for x in self.flag_s], dtype=bool)
        self.CCS = sh                                                      # D x gK float32 (NaN outside cc rows)
        self.cc_dd = np.flatnonzero(F["cc_dd"]).astype(np.int32)
        del F, pu, pe, ps, cl, FL
        # dose patterns per (gene, drug): tables.dose_patterns over the drugs of drugdose.csv, in tables/drugs order
        dd = S.ix["drugdose"]
        dnames, _dod, _rows, grid = TB.drug_grid(_names(dd, "drug"), dd["conc"].to_numpy(dtype=np.float64))
        Pu, Pd = TB.dose_patterns(np.ascontiguousarray(self.Zp[:, :gK]), grid)
        pos = {n: i for i, n in enumerate(dnames)}
        sel = np.array([pos.get(n, -1) for n in self.drug_names], dtype=np.int64)
        self.PAT = np.full((gK, len(self.drug_names), 2), -1, dtype=np.int8)
        ok = sel >= 0
        self.PAT[:, ok, 0] = Pu[sel[ok]].T
        self.PAT[:, ok, 1] = Pd[sel[ok]].T
        del Pu, Pd
        self.c_flags()
        ms = S.npy("graph/module_scores.npy")
        cc_set = set(self.cc_dd.tolist())
        for dd_ in range(D):
            di = int(self.drug_of_dd[dd_])
            pat = np.full((C, 2), -1, dtype=np.int8)
            if di >= 0:
                pat[:gK] = self.PAT[:, di, :]
            arrays = {"lfc": self.LFC[dd_], "z": self.Zp[dd_], "q_up": self.QU[dd_], "q_dn": self.QD[dd_],
                      "poseff": self.PEp[dd_], "flag": self.FL[dd_], "nl": self.NL[:, dd_, :], "pat": pat}
            if dd_ in cc_set:
                cc = np.full(C, np.nan, dtype=np.float32)
                cc[:gK] = self.CCS[dd_]
                arrays["cc"] = cc
            if ms is not None:
                arrays["ms"] = np.asarray(ms[:, dd_, :])
            self.data.shard(p_id(dd_), "drugdose", arrays=arrays,
                            meta={"dd": dd_, "drug": self.dd_drug[dd_],
                                  "dose": str(S.ix["drugdose"]["dose"].iloc[dd_])})
        if self.pooled_r:
            zq = np.clip(np.rint(self.Zp[:, :gK].T * 100.0), -32767, 32767)
            zq = np.where(np.isfinite(self.Zp[:, :gK].T), zq, -32768).astype(np.int16)
            self.web.shard("pooledr", "pooledr", arrays={"zq": zq},
                           meta={"what": "ranking helper: pooled z x 100 rounded to int16 (genes x drug-doses; -32768 "
                                         "= NaN), for ranking every gene by pooled-profile r; the exact values are in "
                                         "the gene buckets", "na": -32768})

    def _codes(self, s):
        """Codes into the flag dictionary for an object array of flag strings (new strings get the next code)."""
        codes, uniq = pd.factorize(pd.Series(s, dtype=object), use_na_sentinel=False)
        m = np.empty(len(uniq), dtype=np.uint32)
        for i, u in enumerate(uniq):
            u = "" if u is None or (isinstance(u, float) and u != u) else str(u)
            k = self.flag_ix.get(u)
            if k is None:
                k = self.flag_ix[u] = len(self.flag_s)
                self.flag_s.append(u)
            m[i] = k
        return m[codes]

    def c_flags(self):
        """d/flags.js: the dictionary of every distinct gene-level flag string, its clean bit and its tokens by kind."""
        art = set(A.ARTIFACT_FLAGS)
        a, c, cc, unknown = [], [], [], set()
        for s in self.flag_s:
            toks = [t for t in s.split("; ") if t]
            a.append("; ".join(t for t in toks if t in art))
            cc.append("; ".join(t for t in toks if CC_CLEARED_RE.match(t)))
            c.append("; ".join(t for t in toks if t not in art and not CC_CLEARED_RE.match(t)))
            unknown |= {t for t in toks if t not in FLAG_WORDS and not CC_CLEARED_RE.match(t)}
        n = np.bincount(self.FL.ravel().astype(np.int64), minlength=len(self.flag_s)).astype(np.float64)
        self.flag_words_missing = sorted(unknown)
        if unknown:
            self.warnings.append("flag tokens without plain words in explorer.FLAG_WORDS: "
                                 + ", ".join(sorted(unknown)))
        tab = pd.DataFrame({"s": pd.Series(self.flag_s, dtype=object), "clean": self.flag_clean,
                            "art": pd.Series(a, dtype=object), "cav": pd.Series(c, dtype=object),
                            "ccc": pd.Series(cc, dtype=object), "n": n})
        self.web.shard("flags", "flags", tables={"flags": tab},
                       meta={"what": "flag code -> the exact gene-level flags string (tables.flag_strings); clean = no "
                                     "artifact flag; art = artifact tokens, cav = other (caveat) tokens, ccc = the "
                                     "cleared cell-cycle token; n = (drug-dose, column) cells with this code",
                             "words": FLAG_WORDS, "artifact_flags": list(A.ARTIFACT_FLAGS),
                             "no_words": self.flag_words_missing, "dtype": "u16" if len(self.flag_s) <= 65536
                             else "u32"})

    # ---------------------------------------------------------------- step D: drug_effects check, gene buckets
    def d_verify(self):
        """Every tables/drug_effects.parquet row is reproduced exactly by the explorer's arrays: lfc, fold, z, q, flags,
        clean, cc_share, n_lines_*, pattern_*, symbol, drug, dose, conc; and its rows are exactly the notable
        (gene, drug-dose) pairs (|z| >= KEEP_Z or q < Q_CUT). Stops the stage on any difference."""
        de = self.load("tables/drug_effects.parquet", cache=True)
        n = len(de)
        bad = {}
        if n:
            c = pd.to_numeric(de["col"]).to_numpy(np.int64)
            d = pd.to_numeric(de["dd"]).to_numpy(np.int64)

            def f32(name, ref):
                v = np.ascontiguousarray(de[name].to_numpy(dtype=np.float32))
                r = np.ascontiguousarray(ref, dtype=np.float32)
                bad[name] = int((v.view(np.uint32) != r.view(np.uint32)).sum())

            f32("lfc", self.LFC[d, c])
            f32("z", self.Zp[d, c])
            f32("q_up", self.QU[d, c])
            f32("q_down", self.QD[d, c])
            f32("fold", (2.0 ** self.LFC[d, c]).astype(np.float32))
            f32("cc_share", self.CCS[d, c])
            fs = np.array(self.flag_s, dtype=object)[self.FL[d, c]]
            bad["flags"] = int((fs != de["flags"].fillna("").to_numpy(dtype=object)).sum())
            bad["clean"] = int((self.flag_clean[self.FL[d, c]] != de["clean"].to_numpy(dtype=bool)).sum())
            for k, name in enumerate(("n_lines_measured", "n_lines_up", "n_lines_down")):
                bad[name] = int((self.NL[c, d, k].astype(np.int64) != de[name].to_numpy(dtype=np.int64)).sum())
            di = self.drug_of_dd[d]
            for k, name in enumerate(("pattern_up", "pattern_down")):
                code = np.where(di >= 0, self.PAT[c, np.maximum(di, 0), k], -1)
                pat = np.array(list(TB.PATTERNS) + [None], dtype=object)[np.where(code < 0, len(TB.PATTERNS), code)]
                bad[name] = int((pat != de[name].to_numpy(dtype=object)).sum())
            bad["symbol"] = int((_names(self.genes, "symbol")[c] != _names(de, "symbol")).sum()) \
                if "symbol" in self.genes else 0
            ddt = self.S.ix["drugdose"]
            bad["drug"] = int((self.dd_drug[d] != _names(de, "drug")).sum())
            bad["dose"] = int((_names(ddt, "dose")[d] != _names(de, "dose")).sum())
            bad["conc"] = int((ddt["conc"].to_numpy(dtype=np.float64)[d] != de["conc"].to_numpy(np.float64)).sum())
            gK = self.gK
            keep = (np.abs(self.Zp[:, :gK]) >= TB.KEEP_Z) | (self.QU[:, :gK] < TB.Q_CUT) | (self.QD[:, :gK] < TB.Q_CUT)
            pairs = np.unique(d * gK + c)
            bad["notable_pairs"] = int(abs(int(keep.sum()) - n) + (pairs.size != n) + int((~keep[d, c]).sum()))
        self.checks["drug_effects"] = {"rows": n, "different": bad,
                                       "rule": "every row equals the explorer's arrays (floats bit for bit); the rows "
                                               "are exactly the pairs with |z| >= 3 or q < 0.10"}
        wrong = {k: v for k, v in bad.items() if v}
        if wrong:
            raise SystemExit("explorer: tables/drug_effects.parquet is not reproduced exactly by the explorer's arrays "
                             "(rows differing per column: " + ", ".join(f"{k} {v:,}" for k, v in wrong.items())
                             + "); the explorer is not written")
        self.want("tables/drug_effects.parquet", "arrays (verified)")
        self.got("tables/drug_effects.parquet", "arrays (verified)", de)
        log(f"    drug_effects: all {n:,} rows reproduced exactly (flags, clean, counts, patterns, values)")

    def bucket_sources(self):
        """{table name in a gene bucket: (source, Keyed table, key columns)}."""
        rel = self.load("relations/gene_relations.parquet", cache=True)
        relb = rel[[c for c in ("_row", "col_a", "col_b", "rank", "cos", "evidence", "alert") if c in rel]]
        spec = (("genes", "tables/genes.parquet", None, ("col",)),
                ("egenes", "embed/genes.parquet", None, ("col",)),
                ("ann", "reference/annotations.parquet", None, ("col",)),
                ("sets", "reference/gene_sets.parquet", None, ("col",)),
                ("string", "reference/string_pairs.parquet", None, ("col_a", "col_b")),
                ("le", "tables/line_effects.parquet", None, ("col",)),
                ("dlt", "tables/drug_line_top.parquet", None, ("col",)),
                ("rel", "relations/gene_relations.parquet", rel, ("col_a",)),
                ("relb", "relations/gene_relations.parquet", relb, ("col_b",)),
                ("node", "graph/nodes.parquet", None, ("col",)),
                ("gedge", "graph/edges.parquet", None, ("col_a", "col_b")),
                ("dir", "direction/edges.parquet", None, ("source_col", "target_col")),
                ("dgrp", "direction/groups.parquet", None, ("gene_col",)),
                ("nmem", "validation/novel_members.csv", None, ("col",)),
                ("nedge", "validation/novel_edges.csv", None, ("col_a", "col_b")))
        out = {}
        for name, src, df, keys in spec:
            if df is None:
                df = self.load(src, cache=src in ("tables/line_effects.parquet", "graph/nodes.parquet",
                                                  "graph/edges.parquet", "direction/edges.parquet",
                                                  "validation/novel_members.csv", "reference/gene_sets.parquet",
                                                  "direction/groups.parquet", "reference/annotations.parquet"))
            K = Keyed(df, *keys)
            self.want(src, f"g.{name}", len(K.rows(0, self.gK)))
            out[name] = (src, K, keys)
        return out

    def step_d(self):
        self.d_verify()
        S = self.S
        gK, C = self.gK, self.C
        srcs = self.bucket_sources()
        lc = S.npy("tensor/line_center.npy", mmap=False)
        ls = S.npy("tensor/line_scale.npy", mmap=False)
        gv = S.npy("embed/gene_vectors.npy", mmap=False)
        CCc = self.CCS[self.cc_dd] if self.cc_dd.size else None
        nb = (gK + BUCKET - 1) // BUCKET
        for b in range(nb):
            c0, c1 = b * BUCKET, min(gK, (b + 1) * BUCKET)
            cols = np.arange(c0, c1)
            arrays = {"cols": cols.astype(np.int32), "lfc": self.LFC[:, c0:c1].T, "z": self.Zp[:, c0:c1].T,
                      "q_up": self.QU[:, c0:c1].T, "q_dn": self.QD[:, c0:c1].T, "flag": self.FL[:, c0:c1].T,
                      "nl": self.NL[c0:c1], "pat": self.PAT[c0:c1]}
            if CCc is not None:
                arrays["cc"] = CCc[:, c0:c1].T
            for k, a in (("lcen", lc), ("lsc", ls), ("gvec", gv)):
                if a is not None:
                    arrays[k] = a[c0:c1]
            tables = {}
            for name, (src, K, keys) in srcs.items():
                t = K.rows(c0, c1, *keys)
                if name == "dir" and len(t):
                    s_in = t["source_col"].between(c0, c1 - 1).to_numpy(dtype=bool)
                    t_in = t["target_col"].between(c0, c1 - 1).to_numpy(dtype=bool)
                    t = t.assign(_role=np.where(s_in & t_in, "both", np.where(s_in, "source", "target")).astype(object))
                tables[name] = t
                self.got(src, f"g.{name}", t)
            tables["vault"] = pd.DataFrame({"col": cols.astype(np.int32),
                                            "gene": pd.Series([self.vault_path("gene", c) for c in cols], dtype=object),
                                            "plates": pd.Series([self.vault_path("plates", c) for c in cols],
                                                                dtype=object)})
            self.web.shard(g_id(b), "gene-bucket", arrays=arrays, tables=tables,
                           meta={"bucket": b, "cols": [c0, c1], "symbols": [self.sym[c] for c in cols]})
            if b % 200 == 0 or b == nb - 1:
                log(f"    gene buckets: {b + 1:,} of {nb:,} (peak memory {_peak_rss_mb()} MB)")
        del srcs
        for rel in ("relations/gene_relations.parquet", "reference/string_pairs.parquet"):
            S.drop(rel)
        if C > gK:
            ag = S.ix["genes"].reset_index(drop=True)
            ag.insert(0, "_row", np.arange(len(ag), dtype=np.int32))
            self.web.shard("g/mod", "gene-modules",
                           arrays={"cols": np.arange(gK, C, dtype=np.int32), "lfc": self.LFC[:, gK:].T,
                                   "z": self.Zp[:, gK:].T, "q_up": self.QU[:, gK:].T, "q_dn": self.QD[:, gK:].T,
                                   "flag": self.FL[:, gK:].T},
                           tables={"agenes": ag.iloc[gK:C]},
                           meta={"what": "the summed atlas modules (S_PHASE, G2M_PHASE, PROTEASOME): pooled values and "
                                         "flags (the atlas's gene-level rule on the module column); they have no "
                                         "per-line values"})

    # ---------------------------------------------------------------- step E: lines, modules, groups, drugs, app
    def step_e(self):
        self.e_lines()
        self.S.drop("tables/line_effects.parquet")
        self.e_modules()
        self.e_dg()
        self.e_drugs()
        self.S.drop("tables/drug_effects.parquet")
        self.e_map()
        self.e_app()

    def e_lines(self):
        S = self.S
        le = self.load("tables/line_effects.parquet", cache=True)
        K = Keyed(le, "line")
        self.want("tables/line_effects.parquet", "l.le")
        comp = self.load("atlas/effects/composition_shift.parquet")
        cid = _names(comp, "cell_line_id")
        self.want("atlas/effects/composition_shift.parquet", "l.comp", int(np.isin(cid, self.line_id).sum()))
        gr = self.load("direction/groups.parquet", cache=True)
        side = {}
        for col, sd in (("altered_lines", "altered"), ("intact_lines", "intact")):
            for r, txt in enumerate(_names(gr, col)):
                for nm in (x.strip() for x in txt.split(", ")):
                    if nm:
                        side.setdefault(nm, []).append((r, sd))
        gid = _names(gr, "group_id")
        ms = S.npy("graph/module_scores.npy")
        for li in range(self.L):
            name = self.line_name[li]
            rows = sorted(side.get(name, []))
            grp = pd.DataFrame({"_grp": np.array([r for r, _ in rows], dtype=np.int32),
                                "group_id": pd.Series([gid[r] for r, _ in rows], dtype=object),
                                "side": pd.Series([sd for _, sd in rows], dtype=object)})
            t_le = K.rows(li, li + 1)
            t_comp = comp.iloc[np.flatnonzero(cid == self.line_id[li])]
            self.got("tables/line_effects.parquet", "l.le", t_le)
            self.got("atlas/effects/composition_shift.parquet", "l.comp", t_comp)
            arrays = {} if ms is None else {"ms": np.ascontiguousarray(ms[:, :, li])}
            self.web.shard(l_id(li), "line", arrays=arrays, tables={"le": t_le, "grp": grp, "comp": t_comp},
                           meta={"line": li, "cell_name": name, "cell_line_id": self.line_id[li],
                                 "vault": self.vault_path("line", li, name, self.line_id[li])})

    def e_modules(self):
        S = self.S
        mods = self.load("graph/modules.parquet", cache=True)
        labs = self.load("validation/module_labels.csv", cache=True)
        nodes = self.load("graph/nodes.parquet", cache=True)
        ged = self.load("graph/edges.parquet", cache=True)
        enr = self.load("validation/module_enrichment.csv", cache=True)
        nmem = self.load("validation/novel_members.csv", cache=True)
        pz, ms = S.npy("graph/module_pooled_z.npy", mmap=False), S.npy("graph/module_scores.npy")
        mod_of = dict(zip(pd.to_numeric(nodes["col"]).astype(int), pd.to_numeric(nodes["module"]).astype(int))) \
            if len(nodes) else {}
        ma = np.array([mod_of.get(int(a), -1) for a in ged["col_a"]], dtype=np.int64) if len(ged) else np.zeros(0)
        mb = np.array([mod_of.get(int(b), -2) for b in ged["col_b"]], dtype=np.int64) if len(ged) else np.zeros(0)
        ged_m = ged.assign(_module=np.where(ma == mb, ma, -1))
        ms_list = sorted(set(pd.to_numeric(mods["module"]).astype(int))) if len(mods) else []
        if len(nodes) and (pd.to_numeric(nodes["module"]) == 0).any():
            ms_list = [0] + [m for m in ms_list if m != 0]
        Kn, Ke, Kr, Km = Keyed(nodes, "module"), Keyed(ged_m, "_module"), Keyed(enr, "module"), Keyed(nmem, "module")
        Kmod, Klab = Keyed(mods, "module"), Keyed(labs, "module")
        mset = set(ms_list)
        for src, df, view in (("graph/nodes.parquet", nodes, "m.members"),
                              ("validation/module_enrichment.csv", enr, "m.enr"),
                              ("validation/novel_members.csv", nmem, "m.nmem"),
                              ("graph/modules.parquet", mods, "m.module"),
                              ("validation/module_labels.csv", labs, "m.label")):
            k = pd.to_numeric(df["module"], errors="coerce") if "module" in df else pd.Series([], dtype=float)
            self.want(src, view, int(k.isin(mset).sum()))
        self.want("graph/edges.parquet", "m.edges", int(np.isin(ged_m["_module"], list(mset)).sum()))
        for m in ms_list:
            t = {"module": Kmod.rows(m, m + 1), "label": Klab.rows(m, m + 1), "members": Kn.rows(m, m + 1),
                 "enr": Kr.rows(m, m + 1), "nmem": Km.rows(m, m + 1),
                 "edges": Ke.rows(m, m + 1).drop(columns="_module")}
            for name, src in (("module", "graph/modules.parquet"), ("label", "validation/module_labels.csv"),
                              ("members", "graph/nodes.parquet"), ("enr", "validation/module_enrichment.csv"),
                              ("nmem", "validation/novel_members.csv"), ("edges", "graph/edges.parquet")):
                self.got(src, {"module": "m.module", "label": "m.label", "members": "m.members", "enr": "m.enr",
                               "nmem": "m.nmem", "edges": "m.edges"}[name], t[name])
            arrays = {}
            if m >= 1 and pz is not None and m - 1 < len(pz):
                arrays["pz"] = pz[m - 1]
            if m >= 1 and ms is not None and m - 1 < ms.shape[0]:
                arrays["ms"] = np.asarray(ms[m - 1])
            self.web.shard(m_id(m), "module", arrays=arrays, tables=t,
                           meta={"module": m, "vault": self.vault_path("module", m) if m else None,
                                 "what": "module 0 = the genes in the space that no module took" if m == 0 else ""})

    def e_dg(self):
        gr = self.load("direction/groups.parquet", cache=True)
        ed = self.load("direction/edges.parquet", cache=True)
        g2 = gr.assign(_cmp=self.group_cmp)
        e2 = ed.assign(_cmp=self.edge_cmp)
        Kg, Ke = Keyed(g2, "_cmp"), Keyed(e2, "_cmp")
        self.want("direction/groups.parquet", "dg.groups")
        self.want("direction/edges.parquet", "dg.edges")
        for k in range((self.n_cmp + DG_PER_SHARD - 1) // DG_PER_SHARD):
            lo, hi = k * DG_PER_SHARD, (k + 1) * DG_PER_SHARD
            tg, te = Kg.rows(lo, hi), Ke.rows(lo, hi)
            self.got("direction/groups.parquet", "dg.groups", tg)
            self.got("direction/edges.parquet", "dg.edges", te)
            self.web.shard(dg_id(k), "dir-groups", tables={"groups": tg, "edges": te},
                           meta={"cmp": [lo, min(hi, self.n_cmp)]})

    def e_drugs(self):
        de = self.load("tables/drug_effects.parquet", cache=True)
        ed = self.load("direction/edges.parquet", cache=True)
        edr = self.load("embed/drugs.parquet")
        moa = self.load("validation/drug_moa.csv", cache=True)
        ctl = self.load("validation/control_sets.csv", cache=True)
        Kde = Keyed(de, "dd")
        Ked = Keyed(ed, "target_dd")
        dt_index = drug_target_index(_names(ed, "kind"), _names(ed, "compounds"))
        ctl_lists = [list(row) for row in ctl[[c for c in ("best_dd_up", "best_dd_down") if c in ctl]].fillna("")
                     .astype(str).itertuples(index=False)]
        edrug_of = {d: i for i, d in enumerate(_names(edr, "drug"))}
        moa_of = {m: i for i, m in enumerate(_names(moa, "moa_fine"))}
        dd_of = {}
        for i, d in enumerate(self.drug_of_dd):
            dd_of.setdefault(int(d), []).append(i)
        dose_of_dd = _names(self.S.ix["drugdose"], "dose")
        self.want("tables/drug_effects.parquet", "dr.de")
        self.want("embed/drugs.parquet", "dr.edrug", int(np.isin(_names(edr, "drug"), self.drug_names).sum()))
        tdd = pd.to_numeric(ed["target_dd"], errors="coerce").fillna(-1).to_numpy() if len(ed) else np.zeros(0)
        # what each drug page must hold, by the rule the vault and the look-ups use (direction_view.Direction:
        # drug_target rows whose compounds name the drug or its salt base, plus rows at one of its drug-doses);
        # computed apart from the page's own index, so a page that misses an arrow stops the stage
        ref = _drug_direction_reference(self.out, self.drug_names, dd_of, tdd)
        moa_col = _names(self.drugs, "moa_fine")
        differ, on_pages = [], set()
        for i, name in enumerate(self.drug_names):
            dds = dd_of.get(i, [])
            p = np.concatenate([Kde.pos("dd", d, d + 1) for d in dds]) if dds else np.zeros(0, np.int64)
            t_de = de.iloc[np.sort(p)]
            q = drug_target_rows(dt_index, name)
            for d in dds:
                q |= set(Ked.pos("target_dd", d, d + 1).tolist())
            t_dir = ed.iloc[sorted(q)]
            on_pages |= q
            if i in ref["rows"]:
                got = set(t_dir["_row"].tolist()) if len(t_dir) else set()
                if got != ref["rows"][i]:
                    differ.append(f"{name}: {len(got)} on the page, {len(ref['rows'][i])} by direction_view")
            t_ed = edr.iloc[[edrug_of[name]]] if name in edrug_of else edr.iloc[0:0]
            t_moa = moa.iloc[[moa_of[moa_col[i]]]] if moa_col[i] in moa_of else moa.iloc[0:0]
            t_ctl = ctl.iloc[control_set_rows(ctl_lists, name, sorted({dose_of_dd[d] for d in dds}))]
            self.got("tables/drug_effects.parquet", "dr.de", t_de)
            self.got("direction/edges.parquet", "dr.dir", t_dir)
            self.got("embed/drugs.parquet", "dr.edrug", t_ed)
            self.web.shard(dr_id(i), "drug", tables={"de": t_de, "dir": t_dir, "edrug": t_ed, "moa": t_moa,
                                                     "ctl": t_ctl},
                           meta={"drug": name, "drug_index": i, "dds": dds, "vault": self.vault_path("drug", name)})
        # the rows the drug pages must hold in all: by direction_view's rule (else, without it, the pages' own)
        self.want("direction/edges.parquet", "dr.dir",
                  len(set().union(*ref["rows"].values())) if ref["ok"] else len(on_pages))
        self.checks["drug_direction"] = {
            "drugs": len(ref["rows"]), "different": len(differ), "examples": differ[:10],
            "rule": "each drug page holds exactly the arrows direction_view.Direction gives for the drug (drug_target "
                    "rows whose compounds name it or its salt base, as the vault and the look-ups list them) plus the "
                    "rows at one of its drug-doses" + ("" if ref["ok"] else f" (not compared: {ref['why']})")}
        if differ:
            raise SystemExit(f"explorer: {len(differ):,} drug page(s) do not hold the arrows direction_view gives "
                             f"for the drug (" + "; ".join(differ[:5]) + "); the explorer is not written")

    def e_map(self):
        p = self.S.path("map/gene_map.html")
        if not os.path.exists(p):
            self.map_note = "OUT/map/gene_map.html is missing: run the 'map' stage"
            return
        with open(p, encoding="utf-8") as fh:
            page = fh.read()
        page, n = re.subn(r'"explorer_base"\s*:\s*(?:"(?:[^"\\]|\\.)*"|null)', '"explorer_base":"../"', page)
        self.map_note = (f"copied; explorer_base set to '../' ({n} place(s))" if n else
                         "copied as it is (the map has no explorer_base key yet)")
        self.web.copy(None, "map/gene_map.html", text=page)

    def e_app(self):
        self.assets = assets_sha()
        self.app_note = write_app(self.web.copy)
        self.web.copy(None, ".nojekyll", text="")


def drug_target_index(kinds, compounds):
    """{drug key: edge rows} of the drug_target edges: each compound of a class ('; '-joined), under each of its names
    (' / '-joined: one molecule under several names), is indexed by direction_view._drug_keys (its name and its salt
    base, lower case), the rule the vault and the look-ups use."""
    from .direction_view import _drug_keys
    idx = {}
    for r, (k, comps) in enumerate(zip(kinds, compounds)):
        if k != "drug_target" or not comps:
            continue
        for c in str(comps).split("; "):
            for nm in c.split(" / "):
                for key in _drug_keys(nm):
                    idx.setdefault(key, set()).add(r)
    return idx


def drug_target_rows(index, name):
    """The drug_target edge rows (a set) whose compounds name the drug or its salt base (drug_target_index)."""
    from .direction_view import _drug_keys
    out = set()
    for key in _drug_keys(name):
        out |= index.get(key, set())
    return out


def _drug_direction_reference(out, drug_names, dd_of, tdd):
    """Per drug index, the edges.parquet rows its page must hold, from direction_view.Direction (drug_targets, the
    vault's and the look-ups' rule) and the rows at its drug-doses. {'ok', 'why', 'rows': {i: set}}."""
    try:
        from .direction_view import Direction
        V = Direction(out)
    except Exception as e:  # noqa: BLE001  (an output without direction, or an older one: nothing to compare)
        return {"ok": False, "why": f"direction_view could not read direction/ ({type(e).__name__}: {e})", "rows": {}}
    rows = {}
    for i, name in enumerate(drug_names):
        want = {int(x) for x in V.drug_targets(name, collapse=False)["edge_id"].tolist()}
        for d in dd_of.get(i, []):
            want |= {int(x) for x in np.flatnonzero(tdd == d)}
        rows[i] = want
    return {"ok": True, "why": "", "rows": rows}


def control_set_rows(lists, name, doses):
    """The rows of validation/control_sets.csv whose best_dd_up or best_dd_down list names one of the drug's
    drug-doses. lists: per row, its list texts ('; '-joined items '<drug> <dose> uM (<mean z>[, flags])'). An item
    names the drug when it starts with '<drug> <dose> uM (' for one of the drug's doses: the drug name is compared
    whole, so 'Irinotecan' does not take the items of 'Irinotecan (hydrochloride)'."""
    pre = tuple(f"{name} {d} uM (" for d in doses)
    if not pre:
        return []
    rows = []
    for r, texts in enumerate(lists):
        if any(t.startswith(pre) or any(f"; {p}" in t for p in pre) for t in texts if t):
            rows.append(r)
    return rows


def write_app(copy):
    """The app files from tahoemap/explorer_app/ (index.html, app.css, js/*.js joined in name order as app.js) and
    tsf_reader.py, through copy(src_path, rel, text=None); without the app folder a short index.html that says the
    page files are missing. Returns a note for the stamp."""
    idx, css, jsd = (os.path.join(APP_DIR, f) for f in ("index.html", "app.css", "js"))
    copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tsf_reader.py"), "tsf_reader.py")
    if not os.path.isfile(idx):
        copy(None, "index.html", text=MISSING_APP_HTML)
        return "tahoemap/explorer_app is missing: index.html says so; every data file is written"
    copy(idx, "index.html")
    if os.path.isfile(css):
        copy(css, "app.css")
    parts = []
    for f in sorted(os.listdir(jsd)) if os.path.isdir(jsd) else []:
        if f.endswith(".js"):
            with open(os.path.join(jsd, f), encoding="utf-8") as fh:
                parts.append(f"// ---- {f}\n" + fh.read().rstrip("\n") + "\n")
    copy(None, "app.js", text="".join(parts))
    return f"app files copied from tahoemap/explorer_app ({len(parts)} script files joined into app.js)"


MISSING_APP_HTML = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Tahoe-100M explorer: app files missing</title></head>
<body style="font-family:sans-serif;max-width:46em;margin:2em auto;line-height:1.5">
<h1>The explorer's page files are missing</h1>
<p>This folder holds every data file of the explorer, but not the page itself. The page files (index.html, app.js,
app.css) come from the folder tahoemap/explorer_app of the code. That folder was not in the code that ran this
stage.</p>
<p>What to do: update the code, then run the explorer stage again (python -m tahoemap explorer). Only the page files
are copied again.</p>
<p>The data are complete. MANIFEST.tsv lists every file. d/core.js, d/g/ (one file per 16 genes) and the data folder
next to this one (x/ per gene, p/ per drug-dose) hold every value. tsf_reader.py reads any of these files in Python.
</p>
</body></html>
"""


# ----------------------------------------------------------------------------- step F: data_dd (optional)
def step_f(B):
    """data_dd y/: per drug-dose, every gene's per-line lfc and z (genes x lines, exact float16), from the tensor
    read in blocks of 128 drug-doses (about 430 MB of memory on the real data)."""
    S = B.S
    DL, DZ = S.npy("tensor/DDL_lfc.npy"), S.npy("tensor/DDL_z.npy")
    for d0 in range(0, B.D, 128):
        d1 = min(B.D, d0 + 128)
        bl, bz = np.asarray(DL[:, d0:d1, :]), np.asarray(DZ[:, d0:d1, :])
        for j, dd in enumerate(range(d0, d1)):
            B.ddv.shard(y_id(dd), "drugdose-lines", arrays={"lfc": bl[:, j, :], "z": bz[:, j, :]},
                        meta={"dd": dd, "drug": B.dd_drug[dd]})
        B.ddv.wait()
        del bl, bz


# ----------------------------------------------------------------------------- step G: core, guard, checks, swap
BASELINE_NOTE = ("Fold change = this drug-dose vs the same cell line's median over the plate's drug wells, NOT DMSO; "
                 "corrected for library-size (composition) shift and well position. The DMSO offset per plate is on "
                 "the gene's Baseline tab.")


# Column definitions of the tables whose stage has no column docs of its own (from those stages' module docstrings).
# The validation CSVs are read from validation/README.md (VALIDATION_README_RE); tables/ and direction/ from their
# stages' DOCS dictionaries.
_REL_DOCS = {
    "col_a": "gene column of this gene (row of atlas/effects/genes.csv)", "symbol_a": "its symbol",
    "col_b": "gene column of the partner", "symbol_b": "the partner's symbol",
    "rank": "rank of the partner among this gene's 100 strongest partners by |cos| (1 = strongest)",
    "cos": "signed cosine of the two genes' unit vectors = correlation of their denoised response profiles over "
           "every (drug-dose, cell line) context; + they go up and down together, - they move opposite",
    "abs_cos": "|cos|",
    "z_gene": "that cosine as a robust z against all of this gene's cosines (median and 1.4826 x MAD): how "
              "exceptional this partner is for this gene",
    "cos_half1": "the same cosine in the space fitted on the first random half of the compounds",
    "cos_half2": "the same cosine in the space fitted on the second half",
    "fdr": "sign-concordance false discovery rate, read at t = min(|cos_half1|, |cos_half2|) on "
           "relations/fdr_curve.csv (1 when the two halves disagree in sign)",
    "evidence": "'both halves': same sign in the full space and in both halves, min |half cos| >= 0.2 and fdr <= "
                "0.10 (replicated); 'one half': |cos| >= 0.5 in one half only (not replicated); otherwise 'not "
                "reproduced'",
    "reproducible": "evidence is 'both halves'", "coords_known": "both genes have genomic coordinates",
    "same_chrom": "the two genes are on the same chromosome",
    "distance_bp": "the gap between the two genes in base pairs (same chromosome only)",
    "same_strand": "the two genes are on the same strand", "locus": "the two genes are 50 kb or less apart",
    "readthrough_risk": "same strand, 20 kb or less apart, and the 5' gene at least 8x more expressed: "
                        "transcription running past the 5' gene can make the pair correlate without any regulation",
    "shared_gene_group": "the two genes share an HGNC gene group (family)",
    "shared_pathway": "the two genes share a Hallmark set or a Reactome pathway of 300 genes or fewer",
    "string_score": "STRING combined score of the pair (pairs with 400 or more are kept; empty: no STRING link)",
    "known": "a known relation: a shared gene group, a shared pathway or a STRING link",
    "both_annotated": "both genes have an HGNC record and coordinates",
    "rank_ba": "the rank of this gene in the partner's own list (empty: this gene is not among the partner's 100)",
    "z_ba": "the z of the pair from the partner's side (empty when rank_ba is empty)",
    "mutual_rank": "max(rank, rank_ba)",
    "specificity": "min(|z_gene|, |z_ba|): how exceptional the pair is for both genes",
    "novel_candidate": "mutual_rank <= 10, specificity >= 4, evidence 'both halves', fdr <= 0.05, |cos| >= 0.5, not "
                       "known, not the same locus, and both genes annotated (and only when the sources that define "
                       "'known' loaded)",
    "alert": "'' or '⚠ ' + every reason to doubt the pair, in plain words; the pair keeps its ranked place"}
_SPACE = "the vector space (embed stage)"
EXTRA_DOCS = {
    "relations/gene_relations.parquet": _REL_DOCS,
    "relations/fdr_curve.csv": {
        "t": "a threshold on the other half's |cos|",
        "pairs_agree": "selected pairs whose sign agrees in the other half, with |other-half cos| >= t",
        "pairs_disagree": "selected pairs whose sign disagrees, with |other-half cos| >= t",
        "fdr": "(pairs_disagree + 1) / pairs_agree, made monotone: the false discovery rate of a pair read at t"},
    "graph/nodes.parquet": {
        "col": "gene column", "symbol": "gene symbol",
        "module": "the gene's module: a Louvain community of the kNN graph (0 = in the vector space, in no module)",
        "arm": "'+' or '-': the side of the module's main direction the gene is on ('-' only when the module has a "
               "real opposite arm; empty for module 0)",
        "axis_proj": "the gene's position along its module's main direction (+ arm high, - arm low)",
        "x": "nodal map x (t-SNE, distance 1 - |cos|: genes moving opposite land together)", "y": "nodal map y",
        "xs": "signed map x (t-SNE, distance 1 - cos: genes moving opposite land apart)", "ys": "signed map y",
        "degree": "edges of the kNN graph (graph/edges.parquet) touching the gene",
        "xm": "nodal map x, spread layout (the modules moved apart as blocks)", "ym": "nodal map y, spread layout",
        "xsm": "signed map x, spread layout (the module arms moved apart as blocks)", "ysm": "signed map y, spread "
                                                                                             "layout"},
    "graph/edges.parquet": {
        "col_a": "gene column of one gene", "col_b": "gene column of the other",
        "cos": "their signed cosine in the vector space; an edge links a gene to its 15 strongest partners with "
               "|cos| >= 0.3 whose relation is replicated (both halves) or strong in one half (|cos| >= 0.5)",
        "sign": "+1: they move together; -1: they move opposite"},
    "graph/modules.parquet": {
        "module": "module number", "n_genes": "its genes", "n_plus": "genes on its + arm",
        "n_minus": "genes on its - arm (0: a single-armed module)",
        "top_plus": "the + arm's genes by |projection| on the module's main direction, cut at 15 with the cap rule "
                    "(n_plus says how many there are; every member is on the module's page); 'SYMBOL ⚠' = in the "
                    "space only through drug-doses with an alert",
        "top_minus": "the same for the - arm (n_minus says how many there are)",
        "x": "mean nodal-map x of its genes", "y": "mean nodal-map y of its genes",
        "xs": "mean signed-map x of its genes", "ys": "mean signed-map y of its genes",
        "drugs_up": "the 8 drug-doses with the highest pooled module z, flagged ones in their ranked place with "
                    "their flags (every drug-dose is on the module's page)",
        "drugs_down": "the 8 drug-doses with the lowest pooled module z (same rule)",
        "responsive_lines": "the 8 lines with the largest mean |module score| over its 8 strongest drug-doses "
                            "(every line's scores are on the module's page)",
        "mean_cos_within_plus": "mean cosine between genes of the + arm",
        "mean_cos_within_minus": "mean cosine between genes of the - arm",
        "mean_cos_between_arms": "mean cosine between a + gene and a - gene",
        "arms_opposite": "the module has a real - arm: 5 or more genes on that side and a mean cosine between the "
                         "arms of -0.2 or less"},
    "reference/annotations.parquet": {
        "col": "gene column", "symbol": "Tahoe's gene symbol", "ensembl_id": "Ensembl gene id",
        "hgnc_id": "HGNC id of the matched record", "hgnc_symbol": "HGNC approved symbol",
        "name": "HGNC approved name", "locus_group": "HGNC locus group", "locus_type": "HGNC locus type",
        "location": "cytoband", "chrom": "chromosome", "start": "start (GRCh38, Ensembl r112)",
        "end": "end (GRCh38)", "strand": "strand", "biotype": "Ensembl biotype",
        "aliases": "HGNC alias symbols, '|'-joined (aliases are reused across genes: tentative)",
        "prev_symbols": "HGNC previous symbols, '|'-joined", "gene_groups": "HGNC gene groups (families), "
                                                                           "'|'-joined",
        "entrez_id": "NCBI Gene (Entrez) id", "uniprot": "UniProt accession (the reviewed entry)",
        "protein_name": "UniProt recommended protein name",
        "function": "UniProt FUNCTION text (evidence tags removed)", "ncbi_summary": "NCBI RefSeq gene summary",
        "matched_by": "how the gene was matched to its HGNC record: ensembl_id, symbol, prev_symbol, alias_symbol "
                      "(tentative) or none"},
    "reference/gene_sets.parquet": {
        "source": "hallmark, reactome or hgnc_group", "set": "set name", "col": "gene column of the member",
        "symbol": "member symbol", "set_id": "the source's id of the set",
        "set_size": "genes in the set at the source", "n_present": "its genes among Tahoe genes"},
    "reference/string_pairs.parquet": {
        "col_a": "gene column of one gene (col_a < col_b)", "col_b": "gene column of the other",
        "score": "STRING v12 combined score (400 or more kept; the best over the genes' proteins)"},
    "embed/genes.parquet": {
        "col": "gene column", "symbol": "gene symbol", "label": "unique gene label",
        "included": f"the gene is in {_SPACE}",
        "n_responsive_contexts": "contexts (drug-dose x line, of active trustworthy drug-doses) where its per-line "
                                 "|z| >= 3",
        "vector_norm": "length of its gene vector (empty: not in the space)",
        "represented_fraction": "share of its standardised response the space reproduces (empty: not in the space)",
        "noise_rna": "a noise-class RNA (atlas NOISE_RNA_RE on the symbol: 7SK, snoRNA, snRNA, mitochondrial, "
                     "ribosomal-protein pseudogenes, replication histones, ENSG-only names): kept out of the space; "
                     "all its effects are in the other tabs",
        "n_sig_drugdoses": "drug-doses with a significant pooled change of the gene (q < 0.1 and >= 1.2x), any flags",
        "n_sig_drugdoses_clean": "... of them without an artifact flag for this gene",
        "line_evidence": "per-line evidence: |z| >= max(5, the calibrated per-line cut) in >= 2 lines of one "
                         "trustworthy drug-dose",
        "line_evidence_clean": "the same at a drug-dose without an alert for this gene",
        "evidence_flagged_only": "in the space only through drug-doses that carry an alert for it (shown with ⚠)"},
    "embed/drugs.parquet": {
        "drug": "drug name", "dose": "the dose whose vector the drug gets (its best trustworthy dose: most "
                                     "significant genes, ties to the higher dose)",
        "dd": "that drug-dose's index", "n_sig_genes": "significant genes at that dose",
        "trusted": "the dose is technically trustworthy (False: the drug has no trustworthy dose)",
        "flags": "that drug-dose's flags", "moa_fine": "mechanism class", "targets": "listed targets",
        "alert": "'' or '⚠ ' + why the drug's vector may be weak (an untrusted dose, or an artifact flag)"},
    "embed/drugdoses.parquet": {
        "dd": "drug-dose index", "drug": "drug", "dose": "dose", "conc": "concentration (µM)",
        "n_sig_genes": "significant genes (up + down)", "flags": "the drug-dose's flags",
        "active_context": "its contexts were used to fit the space",
        "fit_status": "'in the fit', or why not (technically untrustworthy, or not active)",
        "half": "the random half of the compounds it belongs to (1 or 2; for the reproducibility check)",
        "vector_norm": "length of its drug-dose vector (projected also when not in the fit)"},
    "embed/contexts.parquet": {
        "j": "context number (row of embed/context_vectors.npy)", "dd": "drug-dose index",
        "line": "line index", "drug": "drug", "dose": "dose", "cell_line_id": "Cellosaurus id",
        "cell_name": "cell line name", "half": "the random half of the compounds the drug-dose belongs to"},
    "embed/components.parquet": {
        "component": "component number (1 = largest)", "variance_pct_of_space": "its share of the space's variance (%)",
        "top_pos_genes": "genes at its positive end, cut at 15 with the cap rule ('SYMBOL ⚠' = in the space only "
                         "through flagged drug-doses)",
        "top_neg_genes": "genes at its negative end (same rule)",
        "top_pos_drugdoses": "drug-doses at its positive end, cut at 10 with the cap rule, flagged ones with their "
                             "flags",
        "top_neg_drugdoses": "drug-doses at its negative end (same rule)",
        "most_sensitive_lines": "the 8 lines whose response along it is strongest (every line's value is on the "
                                "line pages' Vector space tab)"},
    "embed/broad_components.csv": {
        "fit": "which fit: the full space or one of the two halves",
        "component": "component number before removal", "variance_pct": "its share of the variance (%)",
        "genes_following": "genes with |r| >= 0.3 to it",
        "removed": "removed as a broad axis (global toxicity or shutdown): among the first 3 components and followed "
                   "by >= 5% of the genes (and >= 200)"},
}
VALIDATION_HEAD_RE = re.compile(r"^## (\S+\.csv) - (.*)$")
VALIDATION_ROW_RE = re.compile(r"^\| (`[^|]+`) \| (.*) \|\s*$")


def validation_docs(text):
    """{validation/<file>.csv: {"intro", "cols"}} from the tables of validation/README.md ('## <file>.csv - <what>'
    then rows '| `a`, `b` | meaning |')."""
    out, cur = {}, None
    for line in (text or "").splitlines():
        m = VALIDATION_HEAD_RE.match(line)
        if m:
            cur = out.setdefault(f"validation/{m.group(1)}", {"intro": m.group(2), "cols": {}})
            continue
        if line.startswith("## "):
            cur = None
            continue
        m = VALIDATION_ROW_RE.match(line)
        if cur is not None and m:
            for name in re.findall(r"`([^`]+)`", m.group(1)):
                cur["cols"][name] = m.group(2).strip()
    return out


def _column_docs(S=None):
    docs = {f"tables/{k}": {"intro": v[0], "cols": v[1]} for k, v in TB.DOCS.items()}
    docs.update({k: {"intro": "", "cols": dict(v)} for k, v in EXTRA_DOCS.items()})
    try:
        from . import validate as VA
        text = S.text("validation/README.md") if S is not None and S.has("validation/README.md") else None
        docs.update(validation_docs(text or VA.README))
    except Exception as e:  # noqa: BLE001  (the docs are optional; the pages say a column has no description)
        log(f"  explorer: validation column docs not read ({type(e).__name__}: {e})")
    try:
        from . import direction as Dm
        for k, name in (("direction/edges.parquet", "EDGE_DOCS"), ("direction/groups.parquet", "GROUP_DOCS")):
            d = getattr(Dm, name, None)
            if isinstance(d, dict):
                docs[k] = {"intro": "", "cols": {str(c): (v if isinstance(v, str) else str(v)) for c, v in d.items()}}
    except Exception as e:  # noqa: BLE001  (the docs are optional; the pages say a column has no description)
        log(f"  explorer: direction column docs not read ({type(e).__name__}: {e})")
    return docs


def _drivers(ln):
    """core.js 'drivers': one row per (line, driver gene), in the order of tables/lines 'drivers'. 'type' holds every
    variant type recorded for the gene in the line ('; '-joined: 'Frameshift; Missense; Stopgain'), 'change' every
    protein change of the gene ('driver_changes'; the source does not tie a change to a type, so neither does this
    row). A gene named only in driver_changes gets a row with no type; nothing is dropped."""
    rows = []
    for li, (drv, chg) in enumerate(zip(_names(ln, "drivers"), _names(ln, "driver_changes"))):
        ch, order, types = {}, [], {}
        for item in (x.strip() for x in drv.split("; ")):
            if not item:
                continue
            m = re.match(r"^(.+?)\((.*)\)$", item)
            gene, typ = (m.group(1), m.group(2)) if m else (item, "")
            if gene not in types:
                order.append(gene)
                types[gene] = []
            if typ and typ not in types[gene]:
                types[gene].append(typ)
        for item in (x.strip() for x in chg.split("; ")):
            if not item:
                continue
            parts = item.split(" ", 1)
            gene, change = (parts[0], parts[1]) if len(parts) == 2 else (item, "")
            if gene not in types:
                order.append(gene)
                types[gene] = []
            if change:
                ch.setdefault(gene, []).append(change)
        for gene in order:
            rows.append((li, gene, "; ".join(types[gene]), "; ".join(ch.get(gene, []))))
    return pd.DataFrame({"line": np.array([r[0] for r in rows], dtype=np.int16),
                         "gene": pd.Series([r[1] for r in rows], dtype=object),
                         "type": pd.Series([r[2] for r in rows], dtype=object),
                         "change": pd.Series([r[3] for r in rows], dtype=object)})


def g_core(B):
    S = B.S
    tabs = {}
    for name, rel in (("drugdoses", "tables/drugdoses.parquet"), ("edd", "embed/drugdoses.parquet"),
                      ("drugs", "tables/drugs.parquet"), ("edrugs", "embed/drugs.parquet"),
                      ("lines", "tables/lines.parquet"), ("plates", "tables/plates.parquet"),
                      ("wells", "tables/wells.parquet"), ("plate_scale", "atlas/effects/plate_scale.csv"),
                      ("failed_wells", "atlas/effects/failed_wells.csv"), ("sample_map", "atlas/sample_map.csv"),
                      ("modules", "graph/modules.parquet"), ("mlabels", "validation/module_labels.csv"),
                      ("components", "embed/components.parquet"), ("broad", "embed/broad_components.csv"),
                      ("fdr_curve", "relations/fdr_curve.csv")):
        df = B.drugs if name == "drugs" else B.load(rel, cache=rel in ("tables/lines.parquet",
                                                                        "graph/modules.parquet",
                                                                        "validation/module_labels.csv"))
        if rel not in B.acct.n:
            B.acct.source(rel, len(df))
        B.want(rel, "core.js")
        B.got(rel, "core.js", df)
        tabs[name] = df
    tabs["drivers"] = _drivers(tabs["lines"])
    arrays = {"cc_dd": B.cc_dd, "drug_of_dd": B.drug_of_dd}
    wu = S.npy("tensor/well_umi.npy", mmap=False)
    if wu is not None:
        arrays["well_umi"] = np.asarray(wu, dtype=np.float64)
    stamps = {}
    for p in sorted(glob.glob(os.path.join(B.out, "stages", "*.json"))):
        st = read_stamp(B.out, os.path.basename(p)[:-5])
        if st and st.get("stage") != "explorer":
            stamps[str(st.get("stage"))] = st
    repo = _github_repo()
    gr = B.load("direction/groups.parquet", cache=True)
    ed = B.load("direction/edges.parquet", cache=True)
    from . import relations as REL
    inc = S.npy("embed/included_cols.npy", mmap=False)
    meta = {
        "run": B.run, "explorer_version": VERSION,
        "versions": {k: v.get("version") for k, v in stamps.items()},
        "commit": git_out(find_git(), CODE_ROOT, "rev-parse", "HEAD", timeout=20),
        "site_url": B.site_url, "data_url": B.data_url, "repo": f"{repo[0]}/{repo[1]}" if repo else None,
        "results_url": f"https://github.com/{repo[0]}/{repo[1]}/tree/results" if repo else None,
        "counts": {"genes": B.gK, "columns": B.C, "drugdoses": B.D, "lines": B.L, "wells": B.W, "plates": B.P,
                   "drugs": len(B.drug_names), "modules": len(tabs["modules"]), "groups": len(gr),
                   "comparisons": int(B.n_cmp), "arrows": len(ed), "flags": len(B.flag_s), "below": B.n_below,
                   "buckets": (B.gK + BUCKET - 1) // BUCKET, "cc_drugdoses": int(B.cc_dd.size),
                   "drug_effects": B.acct.n.get("tables/drug_effects.parquet", 0),
                   "included": int(np.asarray(inc).size) if inc is not None else None},
        "constants": {"Q_CUT": TB.Q_CUT, "LFC_MIN": TB.LFC_MIN, "KEEP_Z": TB.KEEP_Z, "LINE_Z": TB.LINE_Z,
                      "STRONG_LFC": TB.STRONG_LFC, "line_z_threshold": B.t_line,
                      "min_cells": S.ix["info"].get("min_cells"),
                      "unreliable_plates": S.ix["info"].get("unreliable_plates", []), "DEPLETE_Z": TB.DEPLETE_Z,
                      "ABUNDANCE_UNTRUSTED": list(TB.ABUNDANCE_UNTRUSTED), "ARTIFACT_FLAGS": list(A.ARTIFACT_FLAGS),
                      "CC_CLEARED": TB.CC_CLEARED, "PATTERNS": list(TB.PATTERNS),
                      "MAX_LINES_LISTED": TB.MAX_LINES_LISTED, "TOP_CELLS": TB.TOP_CELLS,
                      "PLATE_SCALE_FLAG": A.PLATE_SCALE_FLAG, "MIN_LINES": int(A.MIN_LINES),
                      "MIN_SIG_BETA": int(A.MIN_SIG_BETA), "BUCKET": BUCKET, "DG_PER_SHARD": DG_PER_SHARD,
                      "REPRO_MIN": REL.REPRO_MIN, "REPRO_FDR": REL.REPRO_FDR, "ONE_HALF": REL.ONE_HALF,
                      "REL_TOP": REL.TOP},
        "FLAG_WORDS": FLAG_WORDS, "column_docs": _column_docs(S), "arrays": ARRAY_DOCS, "paths": PATHS,
        "where": {m["part"]: "data" for m in B.moves}, "moves": B.moves, "missing": S.missing,
        "stamps": stamps, "info": {rel: S.json(rel) for rel in INFO_FILES if S.has(rel)},
        "vault": {"available": B.vault.get("available"), "home": B.vault.get("home"),
                  "plate": {str(k): B.vault_path("plate", k) for k in (B.vault.get("plate") or {})}},
        "map": getattr(B, "map_note", ""), "app": getattr(B, "app_note", ""), "baseline_note": BASELINE_NOTE,
        "line_dd": B.line_dd, "pooled_r": B.pooled_r}
    B.web.shard("core", "core", arrays=arrays, tables=tabs, meta=meta)


def _hosts_text(B):
    du = B.data_url.rstrip("/") + "/" if B.data_url else None
    dd = du.replace("-data/", "-data-dd/", 1) if du and B.line_dd and "-data/" in du else None
    h = {"run": B.run, "data": [du] if du else [], "data_dd": [dd] if dd else [], "release": []}
    return "TAHOE_HOSTS(" + json.dumps(h, sort_keys=True, separators=(",", ":")) + ");\n"


WEB_README = """# Tahoe-100M explorer (web volume)

Open index.html in a browser (or the GitHub Pages site made from this folder).

- d/ holds the data files: one line each, TAHOE_SHARD("<id>","<base64 of zlib>"); tsf_reader.py reads them in Python.
- The per-line values (x/), every gene at one drug-dose (p/) and parts moved by the size guard (w/) are in the data
  volume (the folder data next to this one, or the data repository named in d/hosts.js).
- MANIFEST.tsv lists every file with its bytes and sha256. docs/explorer-data.md (in the code) describes every file.
"""
DATA_README = """# Tahoe-100M explorer (data volume)

The large data files of the explorer: x/NN/<col>.js per gene (per-line lfc and z, per-well values, raw counts, plate
baselines), p/NN/<dd>.js per drug-dose (every gene's pooled values) and w/ (parts the size guard moved here from the
web volume). Each file is one line, TAHOE_SHARD("<id>","<base64 of zlib>"); tsf_reader.py (in the web volume) reads
them. MANIFEST.tsv lists every file with its bytes and sha256.
"""


def g_guard(B):
    """The size guard: above pages_max_mb, MOVES are applied in order (web part -> data w/<id>) until the web volume
    fits. Returns True when it fits."""
    limit = B.pages_max_mb * 2 ** 20
    size = B.web.bytes()
    B.web_before_moves = size
    if size <= limit:
        return True
    log(f"    web volume {size / 2 ** 20:,.1f} MiB is above --pages-max-mb {B.pages_max_mb:g}: moving parts to the "
        "data volume (nothing is dropped)")
    for mid, prefix, what, name, desc in MOVES:
        freed, n = 0, 0
        for rel in sorted(r for r in B.web.files if r.startswith("d/" + prefix) and r.endswith(".js")):
            path = os.path.join(B.web.root, *rel.split("/"))
            with open(path, encoding="ascii") as fh:
                sid, body = TR.unwrap(fh.read())
            hl = struct.unpack("<I", body[4:8])[0]
            head = json.loads(body[8:8 + hl].decode("utf-8"))
            if name not in head.get("arrays" if what == "array" else "tables", {}):
                continue
            (hk, pk), (ht, pt) = split_container(body, take_arrays=(name,) if what == "array" else (),
                                                 take_tables=(name,) if what == "table" else ())
            hk["meta"] = {**hk.get("meta", {}), "moved": {name: "w/" + sid}}
            ht.update(id="w/" + sid, kind="moved", meta={"from": sid, "part": name, "move": mid})
            text = shard_text(sid, _container(hk, pk))
            with open(path, "w", encoding="ascii", newline="\n") as fh:
                fh.write(text)
            freed += B.web.files[rel] - len(text)
            B.web.files[rel] = len(text)
            B.data.raw_shard("w/" + sid, _container(ht, pt))
            n += 1
        B.data.wait()
        size = B.web.bytes()
        B.moves.append({"part": mid, "what": desc, "files": n, "bytes_freed": int(freed),
                        "web_bytes_after": int(size)})
        log(f"    moved {desc}: {n:,} files, {freed / 2 ** 20:,.1f} MiB; web volume now {size / 2 ** 20:,.1f} MiB")
        if size <= limit:
            return True
    return False


def _parts(vol):
    out = {}
    for rel, b in vol.files.items():
        segs = rel.split("/")
        key = "/".join(segs[:2]) + "/" if len(segs) > 2 else rel
        out[key] = out.get(key, 0) + b
    return dict(sorted(out.items(), key=lambda kv: -kv[1]))


def g_limits(B):
    """Files <= FILE_MAX_MB (reported above FILE_WARN_MB), folders <= MAX_ENTRIES entries, paths <= MAX_PATH ASCII
    characters; returns the list of problems that stop the stage."""
    bad, warn, rep = [], [], {}
    for v in B.volumes():
        entries = {}
        big = 0
        for rel, b in v.files.items():
            if b > FILE_MAX_MB * 2 ** 20:
                bad.append(f"{v.name}/{rel} is {b / 2 ** 20:,.1f} MiB (limit {FILE_MAX_MB} MiB)")
            elif b > FILE_WARN_MB * 2 ** 20:
                warn.append(f"{v.name}/{rel} is {b / 2 ** 20:,.1f} MiB (above {FILE_WARN_MB} MiB)")
            big = max(big, b)
            if len(rel) > MAX_PATH or not rel.isascii():
                bad.append(f"{v.name}/{rel}: path longer than {MAX_PATH} characters or not ASCII")
            segs = rel.split("/")
            for i in range(len(segs)):
                entries.setdefault("/".join(segs[:i]), set()).add(segs[i])
        most = max(entries.items(), key=lambda kv: len(kv[1])) if entries else ("", set())
        if len(most[1]) > MAX_ENTRIES:
            bad.append(f"{v.name}/{most[0]} holds {len(most[1]):,} entries (limit {MAX_ENTRIES:,})")
        rep[v.name] = {"files": len(v.files), "largest_file_bytes": int(big), "most_entries": len(most[1]),
                       "most_entries_folder": most[0] or ".", "longest_path": max((len(r) for r in v.files), default=0)}
    B.warnings += warn
    B.checks["limits"] = {**rep, "problems": bad, "warnings": warn}
    return bad


def _col_diff(a, b):
    """Number of values that differ between a source column and a decoded one (floats bit for bit, NaN included)."""
    a = pd.Series(a).reset_index(drop=True)
    b = pd.Series(b).reset_index(drop=True)
    if len(a) != len(b):
        return max(len(a), len(b))
    if isinstance(a.dtype, np.dtype) and a.dtype.kind == "f":
        x = np.ascontiguousarray(a.to_numpy())
        try:
            y = np.ascontiguousarray(b.to_numpy(dtype=x.dtype))
        except (TypeError, ValueError):
            return len(a)
        return int((x.view(f"u{x.itemsize}") != y.view(f"u{y.itemsize}")).sum())
    xa = a.astype(object).where(a.notna(), None).tolist()
    xb = b.astype(object).where(b.notna(), None).tolist()
    return sum(1 for u, v in zip(xa, xb) if not (u == v or (u is None and v is None)))


def table_diff(src, dec, projection=False):
    """{column: differing values} between a decoded table (with _row) and its source table (with _row = row number);
    derived columns (other names starting with '_') are not compared. projection: the decoded table may lack source
    columns."""
    out = {}
    if not len(dec):
        return out
    rows = dec["_row"].to_numpy(dtype=np.int64)
    if rows.size and (rows.min() < 0 or rows.max() >= len(src)):
        return {"_row": int(rows.size)}
    ref = src.iloc[rows].reset_index(drop=True)
    for c in dec.columns:
        if c.startswith("_") and c != "_row":
            continue
        if c not in ref:
            out[c] = len(dec)
            continue
        n = _col_diff(ref[c], dec[c])
        if n:
            out[c] = n
    if not projection:
        for c in ref.columns:
            if c not in dec:
                out[c] = len(dec)
    return out


TABLE_SOURCES = {
    ("gene-bucket", "genes"): "tables/genes.parquet", ("gene-bucket", "egenes"): "embed/genes.parquet",
    ("gene-bucket", "ann"): "reference/annotations.parquet", ("gene-bucket", "sets"): "reference/gene_sets.parquet",
    ("gene-bucket", "string"): "reference/string_pairs.parquet", ("gene-bucket", "le"): "tables/line_effects.parquet",
    ("gene-bucket", "dlt"): "tables/drug_line_top.parquet", ("gene-bucket", "rel"): "relations/gene_relations.parquet",
    ("gene-bucket", "relb"): "relations/gene_relations.parquet", ("gene-bucket", "node"): "graph/nodes.parquet",
    ("gene-bucket", "gedge"): "graph/edges.parquet", ("gene-bucket", "dir"): "direction/edges.parquet",
    ("gene-bucket", "dgrp"): "direction/groups.parquet", ("gene-bucket", "nmem"): "validation/novel_members.csv",
    ("gene-bucket", "nedge"): "validation/novel_edges.csv", ("moved", "rel"): "relations/gene_relations.parquet",
    ("genes", "genes"): "tables/genes.parquet", ("genes", "egenes"): "embed/genes.parquet",
    ("sets", "sets"): "reference/gene_sets.parquet", ("groups", "groups"): "direction/groups.parquet",
    ("ddarr", "contexts"): "embed/contexts.parquet",
    ("val", "control_sets"): "validation/control_sets.csv", ("val", "drug_moa"): "validation/drug_moa.csv",
    ("val", "module_enrichment"): "validation/module_enrichment.csv",
    ("val", "module_labels"): "validation/module_labels.csv", ("val", "novel_edges"): "validation/novel_edges.csv",
    ("val", "novel_members"): "validation/novel_members.csv",
    ("val", "opposite_pairs"): "validation/opposite_pairs.csv",
    ("val", "well_position_check"): "atlas/well_position_check.csv",
    ("core", "drugdoses"): "tables/drugdoses.parquet", ("core", "edd"): "embed/drugdoses.parquet",
    ("core", "drugs"): "tables/drugs.parquet", ("core", "edrugs"): "embed/drugs.parquet",
    ("core", "lines"): "tables/lines.parquet", ("core", "plates"): "tables/plates.parquet",
    ("core", "wells"): "tables/wells.parquet", ("core", "plate_scale"): "atlas/effects/plate_scale.csv",
    ("core", "failed_wells"): "atlas/effects/failed_wells.csv", ("core", "sample_map"): "atlas/sample_map.csv",
    ("core", "modules"): "graph/modules.parquet", ("core", "mlabels"): "validation/module_labels.csv",
    ("core", "components"): "embed/components.parquet", ("core", "broad"): "embed/broad_components.csv",
    ("core", "fdr_curve"): "relations/fdr_curve.csv",
    ("line", "le"): "tables/line_effects.parquet", ("line", "comp"): "atlas/effects/composition_shift.parquet",
    ("module", "module"): "graph/modules.parquet", ("module", "label"): "validation/module_labels.csv",
    ("module", "members"): "graph/nodes.parquet", ("module", "enr"): "validation/module_enrichment.csv",
    ("module", "nmem"): "validation/novel_members.csv", ("module", "edges"): "graph/edges.parquet",
    ("dir-groups", "groups"): "direction/groups.parquet", ("dir-groups", "edges"): "direction/edges.parquet",
    ("drug", "de"): "tables/drug_effects.parquet", ("drug", "dir"): "direction/edges.parquet",
    ("drug", "edrug"): "embed/drugs.parquet", ("drug", "moa"): "validation/drug_moa.csv",
    ("drug", "ctl"): "validation/control_sets.csv",
}
PROJECTIONS = {("gene-bucket", "relb")}


class Expect:
    """The values each data file must hold, from the sources (the self-check of step G and the tests): arrays by
    shard kind, tables by TABLE_SOURCES."""

    def __init__(self, out, B=None):
        self.out, self.B = out, B
        self.S = B.S if B is not None else Src(out)
        self._npy = {}
        self._df = {}
        if B is not None:
            self.LFC, self.Zp, self.QU, self.QD, self.PEp = B.LFC, B.Zp, B.QU, B.QD, B.PEp
            self.FL, self.NL, self.PAT, self.CCS, self.cc_dd = B.FL, B.NL, B.PAT, B.CCS, B.cc_dd
        else:
            self.LFC = self.Zp = None

    def npy(self, rel):
        if rel not in self._npy:
            self._npy[rel] = self.S.npy(rel)
        return self._npy[rel]

    def df(self, rel):
        if rel not in self._df:
            if self.B is not None and rel in self.B.S._cache:
                self._df[rel] = self.B.S._cache[rel]
            elif rel == "tables/drugs.parquet" and self.B is not None:
                self._df[rel] = self.B.drugs
            else:
                self._df[rel] = self.S.df(rel)
        return self._df[rel]

    def arrays(self, head):
        """{array name: expected numpy array} for a decoded header (pooled matrices only when a Build is given)."""
        k, m, sid = head.get("kind"), head.get("meta") or {}, head.get("id", "")
        e = {}
        pooled = self.LFC is not None

        def f(rel):
            return self.npy(rel)
        if k == "gene-bucket" or k == "gene-modules":
            c0, c1 = (m["cols"][0], m["cols"][1]) if k == "gene-bucket" else (self.S.gK, self.S.C)
            e["cols"] = np.arange(c0, c1, dtype=np.int32)
            if pooled:
                e.update(lfc=self.LFC[:, c0:c1].T, z=self.Zp[:, c0:c1].T, q_up=self.QU[:, c0:c1].T,
                         q_dn=self.QD[:, c0:c1].T, flag=self.FL[:, c0:c1].T)
                if k == "gene-bucket":
                    e.update(nl=self.NL[c0:c1], pat=self.PAT[c0:c1])
                    if self.cc_dd.size:
                        e["cc"] = self.CCS[self.cc_dd][:, c0:c1].T
            else:
                for n, rel in (("lfc", "DD_lfc"), ("z", "DD_z"), ("q_up", "DD_qup"), ("q_dn", "DD_qdn")):
                    e[n] = np.asarray(f(f"atlas/effects/{rel}.npy")[:, c0:c1]).T
            if k == "gene-bucket":
                for n, rel in (("lcen", "tensor/line_center.npy"), ("lsc", "tensor/line_scale.npy"),
                               ("gvec", "embed/gene_vectors.npy")):
                    if f(rel) is not None:
                        e[n] = f(rel)[c0:c1]
        elif k == "gene-lines":
            col = int(m["col"])
            gK = self.S.gK
            if col < gK:
                e["lfc"] = f("tensor/DDL_lfc.npy")[col]
                e["z"] = f("tensor/DDL_z.npy")[col]
                e["counts"] = np.asarray(f("tensor/well_counts.npy")[:, col])
                e["pbase"] = np.asarray(f("tensor/plate_base.npy")[:, :, col])
            for n, rel in (("poseff", "DD_poseff"), ("w1", "W1"), ("w2", "W2"), ("wz", "Z"), ("poff", "plate_offset"),
                           ("slot", "slot_median"), ("psg", "plate_scale_gene")):
                a = f(f"atlas/effects/{rel}.npy")
                if a is not None:
                    e[n] = np.asarray(a[:, col])
            e["wpu"] = np.asarray(f("atlas/effects/posunc.npy")[:, col]).astype(np.uint8)
        elif k == "drugdose":
            dd = int(m["dd"])
            for n, rel in (("lfc", "DD_lfc"), ("z", "DD_z"), ("q_up", "DD_qup"), ("q_dn", "DD_qdn"),
                           ("poseff", "DD_poseff")):
                e[n] = np.asarray(f(f"atlas/effects/{rel}.npy")[dd])
            if pooled:
                e.update(flag=self.FL[dd], nl=self.NL[:, dd, :])
            if f("graph/module_scores.npy") is not None and "ms" in (head.get("arrays") or {}):
                e["ms"] = np.asarray(f("graph/module_scores.npy")[:, dd, :])
        elif k == "drugdose-lines":
            dd = int(m["dd"])
            e["lfc"] = np.asarray(f("tensor/DDL_lfc.npy")[:, dd, :])
            e["z"] = np.asarray(f("tensor/DDL_z.npy")[:, dd, :])
        elif k == "line" and "ms" in (head.get("arrays") or {}):
            e["ms"] = np.asarray(f("graph/module_scores.npy")[:, :, int(m["line"])])
        elif k == "module":
            mm = int(m["module"])
            if mm >= 1 and "pz" in (head.get("arrays") or {}):
                e["pz"] = f("graph/module_pooled_z.npy")[mm - 1]
            if mm >= 1 and "ms" in (head.get("arrays") or {}):
                e["ms"] = np.asarray(f("graph/module_scores.npy")[mm - 1])
        elif k == "moved" and m.get("part") == "ms":
            src = m.get("from", "")
            if src.startswith("l/"):
                e["ms"] = np.asarray(f("graph/module_scores.npy")[:, :, int(src[2:])])
            elif src.startswith("m/"):
                e["ms"] = np.asarray(f("graph/module_scores.npy")[int(src[2:]) - 1])
        elif k == "linecpm":
            for n, rel in (("line_cpm", "atlas/effects/line_cpm.npy"), ("expr_mask", "atlas/effects/expr_mask.npy"),
                           ("line_measured", "tensor/line_measured.npy")):
                if f(rel) is not None:
                    e[n] = np.asarray(f(rel))
        elif k == "space" and sid == "space/ctx":
            e["vectors"] = f("embed/context_vectors.npy")
        elif k == "space":
            inc = np.asarray(f("embed/included_cols.npy"))
            rel = {"space/u": "embed/gene_unit.npy", "space/h1": "embed/gene_unit_half1.npy",
                   "space/h2": "embed/gene_unit_half2.npy"}[sid]
            U = np.asarray(f(rel))
            e["included"] = inc.astype(np.int32)
            e["unit"] = U[inc] if m.get("rows") == "included" else U
        elif k == "core" and f("tensor/well_umi.npy") is not None:
            e["well_umi"] = np.asarray(f("tensor/well_umi.npy"), dtype=np.float64)
        return e

    def check(self, path):
        """Problems found in one data file (empty when it holds exactly what its sources hold)."""
        head, arrays, tables = read_shard(path)
        probs = []
        run = self.B.run if self.B is not None else run_id(self.out)
        if head.get("run") != run:
            probs.append(f"run {head.get('run')} is not {run}")
        for n, want in self.arrays(head).items():
            got = arrays.get(n)
            want = np.asarray(want)
            if want.dtype == bool:
                want = want.astype(np.uint8)
            if got is None:
                probs.append(f"array {n} missing")
            elif got.dtype != want.dtype or got.shape != want.shape or \
                    np.ascontiguousarray(got).tobytes() != np.ascontiguousarray(want).tobytes():
                probs.append(f"array {n} differs ({got.dtype} {got.shape} vs {want.dtype} {want.shape})")
        for name, df in tables.items():
            src = TABLE_SOURCES.get((head.get("kind"), name))
            if src is None or "_row" not in df:
                continue
            d = table_diff(self.df(src), df, projection=(head.get("kind"), name) in PROJECTIONS)
            if d:
                probs.append(f"table {name} differs from {src}: {d}")
        return [f"{os.path.basename(path)} ({head.get('id')}): {p}" for p in probs]


def _sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def write_manifest(vol):
    """MANIFEST.tsv of a volume: path, bytes, sha256 of every other file, sorted by path."""
    rels = sorted(r for r in vol.files if r != "MANIFEST.tsv")
    shas = list(vol.pool.map(lambda r: _sha(os.path.join(vol.root, *r.split("/"))), rels)) if rels else []
    text = "path\tbytes\tsha256\n" + "".join(f"{r}\t{vol.files[r]}\t{s}\n" for r, s in zip(rels, shas))
    vol.copy(None, "MANIFEST.tsv", text=text)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def step_g(B):
    g_core(B)
    B.web.copy(None, "d/hosts.js", text=_hosts_text(B))
    B.web.copy(None, "README.md", text=WEB_README)
    B.data.copy(None, "README.md", text=DATA_README)
    for v in B.volumes():
        v.copy(None, ".gitattributes", text="* -text\n")
        v.wait()
    t0 = time.time()
    fits = g_guard(B)
    if B.moves:
        g_core(B)                                      # core.js 'where' names the moved parts
        B.web.wait()
        fits = B.web.bytes() <= B.pages_max_mb * 2 ** 20
    B.times["G guard"] = round(time.time() - t0, 1)
    for v in B.volumes():
        n = sum(1 for r in v.files if r.endswith(".js") and r not in ("d/hosts.js", "app.js", "probe.js"))
        probe = {"run": B.run, "volume": v.name, "shards": n, "explorer_version": VERSION,
                 "counts": {"genes": B.gK, "columns": B.C, "drugdoses": B.D, "lines": B.L}}
        v.copy(None, "probe.js", text="TAHOE_PROBE(" + json.dumps(probe, sort_keys=True, separators=(",", ":"))
               + ");\n")
    rep, bad = B.acct.report()
    B.complete, B.complete_bad = rep, bad
    problems = g_limits(B)
    t0 = time.time()
    g_selfcheck(B)
    B.times["G self-check"] = round(time.time() - t0, 1)
    sums = {v.name: write_manifest(v) for v in B.volumes()}
    man = {"run": B.run, "explorer_version": VERSION, "manifest_sha256": sums, "moves": B.moves,
           "fits": bool(fits), "pages_max_mb": B.pages_max_mb,
           "volumes": {v.name: {"files": len(v.files), "bytes": v.bytes()} for v in B.volumes()},
           "files": [[v.name, r, v.files[r]] for v in B.volumes() for r in sorted(v.files)]}
    with open(os.path.join(B.tmp, "manifest.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(man, fh, separators=(",", ":"), sort_keys=True)
    if bad:
        raise SystemExit("explorer: some rows of the sources are missing from the explorer (R1): " + "; ".join(bad)
                         + f". Nothing was replaced; the files are in {B.tmp}")
    if problems:
        raise SystemExit("explorer: file limits exceeded: " + "; ".join(problems[:20])
                         + f". Nothing was replaced; the files are in {B.tmp}")
    if not fits:
        parts = _parts(B.web)
        raise SystemExit(
            f"explorer: the web volume is {B.web.bytes() / 2 ** 20:,.1f} MiB after every move, above --pages-max-mb "
            f"{B.pages_max_mb:g}. Nothing is dropped to fit, so the stage stops. Moved: "
            + "; ".join(f"{m['what']} ({m['bytes_freed'] / 2 ** 20:,.1f} MiB)" for m in B.moves)
            + ". Web parts (MiB): " + ", ".join(f"{k} {b / 2 ** 20:,.1f}" for k, b in list(parts.items())[:12])
            + f". Raise --pages-max-mb, or publish elsewhere. The complete files are in {B.tmp} (manifest.json lists "
              "the moves).")
    swap(B.out, B.tmp)


def g_selfcheck(B):
    """Decode every SELF_CHECK_EVERY-th data file of every volume and every top-level web data file, and compare them
    with the sources (arrays bit for bit, table rows by _row). Stops the stage on any difference."""
    shards = []
    for v in B.volumes():
        for r in sorted(v.files):
            if r.endswith(".js") and r not in ("d/hosts.js", "probe.js", "app.js"):
                shards.append((v, r))
    pick = [s for i, s in enumerate(shards) if i % SELF_CHECK_EVERY == 0]
    pick += [(B.web, r) for r in sorted(B.web.files) if re.match(r"^d/(?:space/)?[a-z0-9]+\.js$", r)
             and r != "d/hosts.js" and (B.web, r) not in pick]
    E = Expect(B.out, B)
    probs = []
    for v, r in pick:
        probs += E.check(os.path.join(v.root, *r.split("/")))
    B.checks["self_check"] = {"files": len(pick), "of": len(shards), "problems": probs[:50], "n_problems": len(probs)}
    if probs:
        raise SystemExit(f"explorer: the self-check found {len(probs)} difference(s) between the written files and "
                         "the sources: " + "; ".join(probs[:10]) + f". Nothing was replaced; the files are in {B.tmp}")
    log(f"    self-check: {len(pick):,} files decoded and compared with the sources: no difference")


def swap(out, tmp):
    """explorer.tmp -> explorer, through explorer.old (common.replace_file names a folder held open on Windows). When
    the new folder cannot be moved in, the old explorer is moved back, so OUT/explorer is never left missing."""
    final, old = os.path.join(out, "explorer"), os.path.join(out, "explorer.old")
    _rmtree(old)
    moved = False
    if os.path.isdir(final):
        replace_file(final, old)
        moved = True
    try:
        replace_file(tmp, final)
    except BaseException:
        if moved and not os.path.exists(final):
            try:
                replace_file(old, final)
            except OSError as e:
                log(f"  explorer: the previous explorer stays in {old} ({type(e).__name__}: {e})")
        raise
    _rmtree(old)


def estimate_bytes(S, line_dd=False):
    """A rough upper estimate of the explorer's bytes on disk (for the free-space check)."""
    per_col = 0.75 * S.D * S.L * 4 + S.W * 17 + S.D * 4 + S.P * S.L * 4
    est = 1.34 * (S.C * per_col + S.D * S.C * 25 + 2e8)
    if line_dd:
        est += 1.34 * 0.75 * S.D * S.gK * S.L * 4
    return est


def run(out, site_url=None, data_url=None, line_dd=False, pages_max_mb=PAGES_MAX_MB, pooled_r=False):
    """Build OUT/explorer (see the module docstring). site_url: the published pages (for the links the pages show);
    data_url: where the data volume is published (raw.githubusercontent.com URL of the data repository, branch);
    line_dd: also the data_dd volume; pages_max_mb: the size guard's limit for the web volume (MiB); pooled_r: also
    d/pooledr.js (the ranking helper for pooled-profile r against every gene)."""
    t0 = time.time()
    out = os.path.abspath(out)
    log(f"Explorer: building {os.path.join(out, 'explorer')}")
    with warnings.catch_warnings(), np.errstate(all="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        B = Build(out, site_url, data_url, line_dd, pages_max_mb, pooled_r)
        est = estimate_bytes(B.S, line_dd)
        free = shutil.disk_usage(out).free
        if free < 1.3 * est:
            raise SystemExit(f"explorer: {free / 1e9:.1f} GB free on the output's disk; the explorer needs about "
                             f"{est / 1e9:.1f} GB (and 30% to spare). Free some space and run it again.")
        try:
            B.step("A", B.step_a)
            B.step("B", B.step_b)
            B.step("C", B.step_c)
            B.step("D", B.step_d)
            B.step("E", B.step_e)
            if line_dd:
                B.step("F", lambda: step_f(B))
            B.step("G", lambda: step_g(B))
        finally:
            B.pool.shutdown(wait=True)
    info = {"version": VERSION, "run": B.run, "assets_sha": getattr(B, "assets", None), "site_url": site_url,
            "data_url": data_url, "line_dd": bool(line_dd), "pooled_r": bool(pooled_r),
            "pages_max_mb": float(pages_max_mb),
            "volumes": {v.name: {"files": len(v.files), "bytes": v.bytes(), "mb": round(v.bytes() / 1e6, 1)}
                        for v in B.volumes()},
            "web_bytes_before_moves": int(getattr(B, "web_before_moves", B.web.bytes())), "moves": B.moves,
            "parts": {v.name: _parts(v) for v in B.volumes()},
            "complete": B.complete, "complete_ok": not B.complete_bad, "checks": B.checks,
            "warnings": B.warnings, "missing": B.S.missing, "unmapped_files": getattr(B, "unmapped", []),
            "flag_words_missing": getattr(B, "flag_words_missing", []), "map": getattr(B, "map_note", ""),
            "app": getattr(B, "app_note", ""), "steps_s": B.times, "peak_rss_mb": _peak_rss_mb(),
            "minutes": round((time.time() - t0) / 60, 2)}
    stamp_stage(out, "explorer", VERSION, info)
    vb = info["volumes"]
    log(f"Explorer done -> {os.path.join(out, 'explorer')}: web {vb['web']['mb']:,} MB ({vb['web']['files']:,} files), "
        f"data {vb['data']['mb']:,} MB ({vb['data']['files']:,} files)"
        + (f", data_dd {vb['data_dd']['mb']:,} MB" if "data_dd" in vb else "")
        + (f"; moved to the data volume: {', '.join(m['part'] for m in B.moves)}" if B.moves else "")
        + f" ({info['minutes']} min, peak memory {info['peak_rss_mb']} MB)")
    for w in B.warnings:
        log(f"  explorer WARNING: {w}")
    return info


def refresh_assets(out):
    """Copy the app files again into OUT/explorer/web (when only tahoemap/explorer_app changed): MANIFEST.tsv,
    manifest.json and the stamp's assets_sha are updated; the data files are not touched."""
    web = os.path.join(out, "explorer", "web")
    if not os.path.isdir(web):
        raise SystemExit(f"explorer: {web} does not exist; run the explorer stage first")
    pool = cf.ThreadPoolExecutor(max_workers=2)
    try:
        v = Volume(web, "web", "d/", None, pool, threading.BoundedSemaphore(4))
        for root, _dirs, files in os.walk(web):
            for f in files:
                p = os.path.join(root, f)
                v.files[os.path.relpath(p, web).replace(os.sep, "/")] = os.path.getsize(p)
        note = write_app(v.copy)
        if not os.path.isfile(os.path.join(APP_DIR, "index.html")):
            for rel in ("app.js", "app.css"):
                if rel in v.files:
                    v.remove(rel)
        sha = write_manifest(v)
    finally:
        pool.shutdown(wait=True)
    p = os.path.join(out, "explorer", "manifest.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            man = json.load(fh)
        man["files"] = [f for f in man.get("files", []) if f[0] != "web"] + [["web", r, v.files[r]]
                                                                             for r in sorted(v.files)]
        man.setdefault("manifest_sha256", {})["web"] = sha
        man.setdefault("volumes", {})["web"] = {"files": len(v.files), "bytes": v.bytes()}
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(man, fh, separators=(",", ":"), sort_keys=True)
    st = read_stamp(out, "explorer")
    if st is not None:
        info = st.get("info") or {}
        info.update(assets_sha=assets_sha(), app=note)
        info.setdefault("volumes", {})["web"] = {"files": len(v.files), "bytes": v.bytes(),
                                                 "mb": round(v.bytes() / 1e6, 1)}
        stamp_stage(out, "explorer", st.get("version", VERSION), info)
    log(f"Explorer: app files refreshed in {web} ({note})")
    return note
