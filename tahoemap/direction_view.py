"""direction_view - the direction stage's edges (OUT/direction) as every surface reads and words them: the vault, the
map, the look-ups and the literature-review dossiers all take them from here, so that they show the same rows in the
same order with the same words.

    dv = direction_view.load(out)       # None when the direction stage has not run (an older output)
    dv.upstream("CDKN1A")               # who probably acts on the gene: rows whose target is the gene
    dv.downstream("TP53")               # what the gene probably acts on: rows whose source is the gene, gene targets
    dv.cells("TP53")                    # the gene as the source of a sensitivity row (cells under a drug-dose)
    dv.for_drugdose(12)                 # sensitivity rows whose target_dd is drug-dose row 12 (drugdose.csv)
    dv.for_drug("Dexamethasone")        # {"cells": the drug's drug-doses' sensitivity rows, "targets": the
                                        #  drug_target rows in which it is one of the compounds}
    shown, n_more, n_more_alert = cap(rows, 10)       # the cap rule (rule 1)
    edge_line(row)                      # 'TP53 → CDKN1A  [B]  TP53 activity strengthens CDKN1A's drug response ...'

A gene is given by its col (int: genes.csv; exact, the vault's choice) or its symbol (str, any letter case).

Rows. Every listing is a DataFrame of display rows in ORDER - grade A, B, C, then q (smallest first), then |effect|
(|contrast|, largest first), then p, kind, source, target: deterministic. A display row is an edge of edges.parquet,
except that edges which are one and the same test for several sources are one row naming them all: drug_target edges
of targets that share the same compounds and the same result (e.g. 6 HDAC isoforms x 44 genes, 264 edges, 44 rows),
and expression-null edges of genes absent from exactly the same lines (direction version 5: the edges' test_id; an
older output: the same kind, target, compounds or group, mechanism, effect, sign and p). Rows whose target is a
drug-dose's phenotype (target_type 'cells' or, version 5, 'response': the lines' response strength) are the 'cells'
role: dv.cells(gene) and dv.for_drugdose(dd) list them. Such a row lists every source (`sources`,
`source` = their ', '-joined names) and the edges it stands for (`members`, edge ids = rows of edges.parquet); its
alerts are the union of theirs. collapse=False gives the edges one by one. Nothing is dropped, ever: a doubtful row
keeps its place with its alerts (rule 1), and a capped list says how many more there are and how many of those carry
an alert.

Columns added to edges.parquet's (README.md there documents those): edge_id, members (tuple of edge ids), sources
(tuple of str), source_cols (tuple of int), n_sources, has_alert (bool: n_alerts > 0), has_note (n_notes > 0), order
(int: rank in ORDER over all rows), effect (|contrast|), target_drug / target_dose (the drug and dose of target_dd; ''
for gene targets).

Reasons in four tiers (direction VERSION 3; every reason is kept, in exactly one): alerts (⚠: a doubt about this
arrow; has_alert), notes (graded reasons below their thresholds: shown muted, in full where there is room, else as
short labels), caveats (the same on every row of a kind: KIND_CAVEATS, stated once per list - kind_caveats,
caveat_header) and support (evidence for it). alerts_all holds them all in the original order. An output of an
older stage (no tier columns) is read as before: alerts = every reason, the other tiers empty (Direction.tiered
False).

Wording (plain words; the direction is PROBABLE - from cell lines, not proof of direct regulation): arrow / edge_arrow
('X → Y', '->' for consoles that cannot show it: common.printable / ascii_signs), sign_word / sign_text (what the
source's activity does to the target: raises / lowers a level or the cells' numbers, strengthens / weakens a drug
response - RESPONSE kinds, SIGN_RESPONSE_NOTE -, or 'not inferred'), kind_text / KIND_SHORT (the evidence),
GRADE_WORDS / grade_legend, CAVEAT / CAVEAT_SHORT / caveat_lines, alert_short / alert_long / alert_reasons,
note_reasons / notes_short / notes_long, caveat_reasons / kind_caveats / caveat_header, support_reasons /
support_short / support_long, edge_line / texts (all of a row's texts at once), more_text and counts_text (for capped
lists), expected_text and CONTROLS_CAVEAT (the controls' expected false arrows).

Speed: load() reads the folder once (cached per output folder while edges.parquet is unchanged) and indexes the rows
by gene col, symbol, drug-dose and compound, so a look-up is a dictionary access, not a scan (the vault calls it once
per gene note at 16,643 genes: ~2 s for upstream + downstream + cells of every gene). The frames a look-up returns
are views of the shared tables (an empty result is one shared empty frame): read them, copy before changing them.
"""

import functools
import json
import math
import os
import re

import numpy as np
import pandas as pd

from . import tlib as T
from .common import ALERT, ALERT_ASCII, ARROW, ARROW_ASCII, Q_ZERO, ascii_signs, cap_keep, printable

__all__ = ["ALERT", "ALERT_ASCII", "ARROW", "ARROW_ASCII", "CAVEAT", "CAVEAT_LINES", "CAVEAT_SHORT", "Direction",
           "CONTROLS_CAVEAT", "GRADES", "GRADE_SHORT", "GRADE_WORDS", "KINDS", "KIND_CAVEATS", "KIND_SHORT",
           "KIND_WORDS", "ORDER", "MIXED", "RESPONSE", "SIGN_RESPONSE_NOTE", "TIERS", "TIER_WORDS", "alert_long",
           "expected_text", "alert_reasons", "alert_short", "all_reasons", "arrow", "ascii_signs", "available", "cap",
           "caveat_header", "caveat_lines", "caveat_reasons", "counts_text", "edge_arrow", "edge_line", "fmt_q",
           "grade_legend", "kind_caveats", "kind_text", "load", "more_text", "note_reasons", "notes_long",
           "notes_short", "order", "printable", "q_text", "sign_text", "sign_word", "source_text", "support_long",
           "support_reasons", "support_short", "texts"]

KINDS = ("genotype_response", "genotype_baseline", "genotype_sensitivity", "genotype_selectivity", "null_response",
         "null_baseline", "null_sensitivity", "null_selectivity", "drug_target", "level",
         "level_sensitivity")                                          # as direction.KINDS
GRADES = ("A", "B", "C")
ORDER = "grade A, B, C, then q (smallest first), then |effect| (largest first), then p, kind, source, target"
SENSITIVITY = ("genotype_sensitivity", "null_sensitivity", "level_sensitivity")
SELECTIVITY = ("genotype_selectivity", "null_selectivity")          # the target is the lines' response to a drug-dose
RESPONSE = ("genotype_response", "null_response", "level")          # the target is a gene's drug response
DRUGDOSE_TARGETS = ("cells", "response")                            # target types that are a drug-dose's phenotype
MIXED = 0.25        # as direction.MIXED: rise_share between this and 1 - this = the target rises and falls
TIERS = ("alerts", "notes", "caveats", "support")                    # as direction.TIERS
# as direction.KIND_CAVEATS, in the words the edges hold them (a '; ' inside one reason is written ', ')
KIND_CAVEATS = {
    "drug_target": ("drugs can act on other proteins too",),
    "level": ("from natural expression differences between lines, tissue and other differences can mimic it",
              "a stronger correlation one way can reflect how precisely, or how closely to a shared cause, each "
              "gene's level is measured, rather than which gene acts first"),
    "level_sensitivity": ("from natural expression differences between lines, tissue and other differences can mimic "
                          "it",)}
TIER_WORDS = {
    "alerts": f"{ALERT} alerts: reasons to doubt this arrow",
    "notes": "notes: reasons kept below their thresholds, and context (not a doubt about this arrow by themselves)",
    "caveats": "caveats: what every arrow of its kind carries (stated once above a list)",
    "support": "support: evidence for the arrow"}

# ----------------------------------------------------------------------------- words
CAVEAT_SHORT = "probable direction, from the screen's cell lines: not proof of direct regulation"
CAVEAT = ("A probable direction, from the screen's cell lines - not proof of direct regulation. A → B → C looks like "
          "A → C, and another alteration carried by the same lines can be the real cause; there is one time point "
          "(~24 h), and drugs act on proteins, not on mRNA.")
CAVEAT_LINES = (
    "It is not proof of direct regulation: A → B → C looks like A → C, and another alteration carried by the same "
    "lines can be the real cause (the co-occurrence alerts name the ones the metadata records).",
    "'Not recorded' is not 'wild type': the metadata lists driver alterations, and a line may carry one that is not "
    "listed.",
    "One time point (~24 h): fast and slow effects are mixed; compensation and feedback are not seen.",
    "Drugs act on proteins, not on mRNA, and a compound can act on other proteins than its listed target.",
    "An arrow from a gene's natural level comes from natural differences between lines: tissue and other "
    "differences can produce the same pattern, and a stronger correlation one way can come from one gene's level "
    "being measured more precisely, not from it acting first.")
GRADE_WORDS = {
    "A": "strong: a recorded mutation, at least 5 lines on each side compared within organs, significant over the "
         "whole table, no other recorded alteration and no heavily mutated lines concentrated on a side, fewer than "
         "20% of the group's arrows expected false, not resting on a correction, the mean over all its drug-doses "
         "going its way, not a floor, measured in at least half of each side's lines, and for a response strength "
         "seen at 2 or more doses (read any alert or note it still carries)",
    "B": "worth taking seriously - read its alerts: a mutation result with alerts (another alteration on either "
         "side, compared across organs, the mean going the other way, ...) or only 3-4 lines on a side, a natural "
         "knockout with at least 5 lines lacking the gene, or compounds annotated to act on the gene",
    "C": "a glimpse, a lead to check, not a finding: a gene's natural level, a result significant only within "
         "its own group, a comparison the tissue can explain (tissue-confounded), a natural knockout with few lines "
         "or inside an expression programme (more than 10 other line sets overlap), source and target at the same "
         "locus, or compounds that trap their target (TOP1 / TOP2 poisons: the sign is not inferred)"}
GRADE_SHORT = {"A": "strong", "B": "read its alerts", "C": "a glimpse"}
KIND_SHORT = {
    "genotype_response": "mutation: response", "genotype_baseline": "mutation: level",
    "genotype_sensitivity": "mutation: cells", "genotype_selectivity": "mutation: response strength",
    "null_response": "not expressed: response", "null_baseline": "not expressed: level",
    "null_sensitivity": "not expressed: cells", "null_selectivity": "not expressed: response strength",
    "drug_target": "drug target: level", "level": "natural level: response",
    "level_sensitivity": "natural level: cells"}
KIND_WORDS = {
    "genotype_response": "a recorded mutation of the source and the target's drug response",
    "genotype_baseline": "a recorded mutation of the source and the target's baseline level",
    "genotype_sensitivity": "a recorded mutation of the source and how many cells remain under a drug-dose",
    "genotype_selectivity": "a recorded mutation of the source and how strongly the lines respond to a drug-dose "
                            "(genes beyond the per-line cut against the line's typical drug-dose)",
    "null_response": "lines that do not express the source (natural knockouts) and the target's drug response",
    "null_baseline": "lines that do not express the source (natural knockouts) and the target's baseline level",
    "null_sensitivity": "lines that do not express the source (natural knockouts) and how many cells remain under a "
                        "drug-dose",
    "null_selectivity": "lines that do not express the source (natural knockouts) and how strongly the lines respond "
                        "to a drug-dose",
    "drug_target": "compounds annotated to act on the source and the target's level",
    "level": "the source's natural level across lines and the target's drug response (a glimpse)",
    "level_sensitivity": "the source's natural level across lines and how many cells remain under a drug-dose (a "
                         "glimpse)"}
MECH_WORDS = {"loss of function": "loss-of-function mutation", "gain of function": "gain-of-function mutation",
              "altered (any record)": "alteration (mechanism not recorded)"}

# short labels of the alert reasons direction.py writes (the first pattern that matches a reason labels it)
_SHORT = [
    # direction version 5
    (r"^the compounds are (?:TOP1 poisons|TOP2 poisons|PARP trappers|microtubule stabilisers)",
     "poison: sign not inferred"),
    (r" also act on DNA directly \(", "also act on DNA"),
    (r": Tahoe lists .* ChEMBL lists ", "annotations disagree"),
    (r": Tahoe and ChEMBL give different actions on ", "annotations disagree"),
    (r"^supported by 2 compounds only", "2 compounds only"),
    (r"^one test for (\d+) targets", r"one test for \1 targets"),
    (r"^one test for (\d+) genes absent", r"one test for \1 genes"),
    (r"^the mean over all \d+ of its drug-doses goes the other way", "mean goes the other way"),
    (r" mostly falls under these drugs and is .* lower at baseline", "floor"),
    (r"^random comparison groups give about .*: (?:about )?(under 1|\d+)% of them may be false",
     r"expected false \1% (group)"),
    (r"^over the whole table the controls expect", "controls: expected false (kind)"),
    (r"^heavily mutated lines: ", "heavily mutated lines"),
    (r"comparison lines are heavily mutated", "heavily mutated comparison lines"),
    (r"^loss of function is the metadata's inference", "loss of function inferred (missense)"),
    (r"^same locus: ", "same locus"),
    (r"is also absent from most of the ", "co-absent with the target"),
    (r"^an expression programme: ", "programme: direction not identifiable"),
    (r"would appear for any gene \((under 1|\d+)%\)", r"non-specific \1%"),
    (r": (?:about )?(under 1|\d+)% of them would appear for any set of lines", r"non-specific \1%"),
    (r"^also at ", "also at other doses"),
    (r"^one dose only: ", "one dose only"),
    (r"^drug-doses of translation inhibitors carry", "translation inhibitors"),
    # earlier versions
    (r"^significant within this group", "within its group only (a lead)"),
    (r"^significant among the genes tested for this drug-dose", "within its drug-dose only (a lead)"),
    (r"^few lines \((\d+) vs (\d+)\)", r"few lines (\1 vs \2)"),
    (r"^the lines' organs are not known", "organs unknown"),
    (r"^tissue-confounded", "tissue-confounded"),
    (r"^compared across organs", "across organs"),
    (r"^compared within organs: ", "within organs, on part of the lines"),
    (r"^mechanism not recorded for", "mechanism partly not recorded"),
    (r"lines also carry a (gain|loss)-of-", "mixed mechanisms"),
    (r"^co-occurs with (.*)", "co-occurs"),
    (r"^the altered lines are mostly lines without", "anti-occurs"),
    (r"^another gene's alterations sit on the other side", "other side"),
    (r"^other genes are absent from most of these lines too", "also absent"),
    (r"^(\S+) itself is not expressed in (\d+) of the (\d+) ", r"\1 not expressed in \2 of the \3 altered lines"),
    (r"are absent from exactly the same lines", "co-absent genes"),
    (r"other gene\(s\) are absent from exactly these lines", "co-absent genes"),
    (r"carry a recorded loss of", "deletion recorded too"),
    (r"x its pooled level \(maybe low", "maybe low, not absent"),
    (r"^the difference exists only relative to", "rests on the correction"),
    (r"^the reference genes at .* respond", "the reference differs"),
    (r"^no global-sensitivity correction at", "partly uncorrected"),
    (r"too few other genes respond to check for a resistance", "line-wide correction only"),
    (r" measured in \d+ of the \d+ and \d+ of the", "target measured in part of the lines"),
    (r"lower at baseline in the", "lower baseline (lost expression?)"),
    (r"goes the other way at some", "both ways"),
    (r" rises at some .* and falls at others", "rises at some drug-doses, falls at others"),
    (r"^none of its drug-doses is significant pooled", "not significant pooled"),
    (r"own shuffles of the labels", "its own permutation p"),
    (r"artifact flags", "artifact flags"),
    (r"is also absent from most of these lines", "co-absent with the target"),
    (r"cell counts are less trustworthy", "cell counts less trustworthy"),
    (r"^from natural expression differences", "tissue can mimic it"),
    (r"^a stronger correlation one way", "precision caveat"),
    (r"^the reverse .*could not be tested", "direction unclear"),
    (r"^the reverse .*is not clearly weaker", "direction unclear"),
    (r"^drugs can act on other proteins", "off-target possible"),
    (r"^consistent across (\d+) compounds", r"\1 compounds"),
    (r"targets named share these compounds", "shared targets"),
    (r"^the supporting compounds also share", "shared targets"),
    (r"mechanism \(inhibitor or activator\) is not recorded", "sign not inferred"),
]
_SHORT = [(re.compile(p), r) for p, r in _SHORT]


def _g(row, k, default=None):
    """row[k] for a dict / Series row, getattr for a namedtuple row (DataFrame.itertuples)."""
    try:
        v = row[k]
    except (KeyError, TypeError, IndexError):
        v = getattr(row, k, default)
    if v is None:
        return default
    return v


def _num(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return float("nan")
    return x


def fmt_q(x, na="-"):
    """A p or q value: '3e-05' below 0.001, else three decimals; an exact 0 (below what float32 holds) reads
    common.Q_ZERO ('< 1e-45'), as common.fmt_q writes it."""
    x = _num(x)
    if not np.isfinite(x):
        return na
    if x == 0:
        return Q_ZERO
    if x < 1e-3:
        return f"{x:.0e}"
    t = f"{x:.3f}"
    if x < 0.10 and float(t) >= 0.10:                 # just under the 0.10 cut: never shown as 0.100
        t = f"{math.floor(x * 1e4) / 1e4:.4f}"
    return t


def _txt(text, ascii):
    return ascii_signs(text) if ascii else text


# ----------------------------------------------------------------------------- arrows, signs, kinds
def arrow(source, target, ascii=False):
    """'SOURCE → TARGET' ('->' with ascii=True; a console printer passes the text through common.printable)."""
    return f"{source} {ARROW_ASCII if ascii else ARROW} {target}"


def source_text(row, max_names=None):
    """The source of a row: one gene, or the names of a collapsed row (sources), ', '-joined; with max_names, the
    first max_names and '(+k more)'."""
    srcs = list(_g(row, "sources", ()) or ()) or [str(_g(row, "source", ""))]
    if max_names is not None and len(srcs) > max_names:
        return ", ".join(srcs[:max_names]) + f" (+{len(srcs) - max_names} more)"
    return ", ".join(srcs)


def edge_arrow(row, ascii=False, max_names=None):
    """The row as 'X → Y' (a collapsed row: 'X1, X2, X3 → Y')."""
    return arrow(source_text(row, max_names), _g(row, "target", ""), ascii)


def _sign(row):
    s = _num(_g(row, "sign", 0))
    return int(np.sign(s)) if np.isfinite(s) else 0


SIGN_RESPONSE_NOTE = ("For a drug response the sign says how strongly the target responds, in its own direction "
                      "at each drug-dose: 'strengthens' = a stronger response - a higher rise where it rises, a deeper "
                      "fall where it falls -, 'weakens' = a weaker one. Read induction or repression from the listed "
                      "drug-doses (rise_share: the share of the evidence from rises); an arrow whose target rises at "
                      "some drug-doses and falls at others is alerted ('rises at some drug-doses, falls at others'), "
                      "and its sign then says nothing about induction or repression. 'Raises' / 'lowers' are about a "
                      "level or the cells' numbers.")


def sign_word(sign, kind=None):
    """+1 'raises', -1 'lowers', 0 'not inferred'; for a response kind (RESPONSE: the target is a gene's drug response,
    whose sign is how strongly it responds in its own direction) or a response strength (SELECTIVITY) 'strengthens' /
    'weakens'."""
    s = _num(sign)
    s = int(np.sign(s)) if np.isfinite(s) else 0
    if s and str(kind or "") in RESPONSE + SELECTIVITY:
        return "strengthens" if s > 0 else "weakens"
    return "raises" if s > 0 else ("lowers" if s < 0 else "not inferred")


# the trap classes of direction.TRAP_NAMES: mechanism_class -> (plural, what the drugs do to the source)
TRAP_WORDS = {"TOP1 poison": ("TOP1 poisons", "trap {t} on DNA"), "TOP2 poison": ("TOP2 poisons", "trap {t} on DNA"),
              "PARP trapper": ("PARP trappers", "trap {t} on DNA"),
              "microtubule stabiliser": ("microtubule stabilisers", "freeze microtubules (they bind {t})")}


def _dd_of(tgt, prefix):
    return tgt[len(prefix):] if tgt.startswith(prefix) else tgt


def _target_object(row):
    kind = str(_g(row, "kind", ""))
    tgt = str(_g(row, "target", ""))
    tt = str(_g(row, "target_type", "gene") or "gene")
    if kind in SELECTIVITY or tt == "response":
        return f"the response to {_dd_of(tgt, 'response to ')}"
    if kind in SENSITIVITY or tt == "cells":
        return f"the cells' numbers under {_dd_of(tgt, 'cells under ')}"
    if kind.endswith("baseline") or kind == "drug_target":
        return f"{tgt}'s level"
    return f"{tgt}'s drug response"


def _prog(row):
    v = _num(_g(row, "programme_sets", -1))
    return int(v) if np.isfinite(v) else -1


def sign_text(row):
    """What the source does to the target, in words. A recorded mutation: 'TP53 activity strengthens CDKN1A's drug
    response' (a response: how strongly the target responds in its own direction - SIGN_RESPONSE_NOTE), 'KEAP1 activity
    lowers NQO1's level', '... lowers the cells' numbers under Doxorubicin 5 µM (makes them more sensitive)', 'KRAS
    activity strengthens the response to Trametinib 0.5 µM'. A natural knockout (version 5: not an experiment on the
    gene, so 'may'): 'lines without MTAP have fewer cells under Pemetrexed 5 µM (MTAP may protect the cells)', 'lines
    without KRT15 have less SEMA4B (KRT15 may raise it)'; inside an expression programme: 'co-expressed with KRT15
    across lines: which acts on which is not identifiable'. A drug target: "compounds annotated to inhibit MTOR lower
    RPL3's level (MTOR's activity may raise it)"; a trap class: "TOP2 poisons raise TP53's level; TOP2A's own effect on
    it is not inferred (the drugs trap TOP2A on DNA)". A level edge: "NFE2L2's natural level strengthens NQO1's drug
    response". Same locus: 'CDKN2B and CDKN2A lie at the same locus: which acts on which cannot be told'. The sign is
    the effect of the SOURCE's activity (for a drug target: an inhibitor that raises the target means the source's
    activity lowers it)."""
    kind = str(_g(row, "kind", ""))
    src = source_text(row)
    tgt = str(_g(row, "target", ""))
    obj = _target_object(row)
    s = _sign(row)
    same_locus = str(_g(row, "same_locus", False)).lower() in ("true", "1")
    if kind == "drug_target":
        eff = str(_g(row, "drug_effect", "") or "")
        ev = "raise" if eff == "raises" else ("lower" if eff == "lowers" else "move")
        mc = str(_g(row, "mechanism_class", "") or "")
        if mc in TRAP_WORDS:
            pl, verb = TRAP_WORDS[mc]
            return (f"{pl} {ev} {tgt}'s level; {src}'s own effect on it is not inferred (the drugs "
                    f"{verb.format(t=src)})")
        mech = str(_g(row, "mechanism", "") or "")
        if s == 0:
            return (f"compounds annotated to target {src} {ev} {tgt}'s level; the direction of {src}'s own effect is "
                    "not inferred (the mechanism is not recorded)")
        act = "activate" if mech == "activator" else "inhibit"
        whose = "their" if len(list(_g(row, "sources", ()) or ())) > 1 else f"{src}'s"
        return f"compounds annotated to {act} {src} {ev} {tgt}'s level ({whose} activity may " \
               f"{'raise' if s > 0 else 'lower'} it)"
    if s == 0:
        if same_locus:
            return f"{src} and {tgt} lie at the same locus: which acts on which cannot be told"
        if kind.startswith("null") and _prog(row) > 10:
            return f"co-expressed with {src} across lines: which acts on which is not identifiable"
        return f"the direction of {src}'s effect on {obj} is not inferred (the mechanism is not recorded)"
    if kind.startswith("null"):
        if kind == "null_baseline":
            return f"lines without {src} have {'less' if s > 0 else 'more'} {tgt} ({src} may " \
                   f"{'raise' if s > 0 else 'lower'} it)"
        if kind == "null_response":
            return f"lines without {src} show a {'weaker' if s > 0 else 'stronger'} {tgt} drug response ({src} may " \
                   f"{'strengthen' if s > 0 else 'weaken'} it)"
        if kind == "null_sensitivity":
            return f"lines without {src} have {'fewer' if s > 0 else 'more'} cells under " \
                   f"{_dd_of(tgt, 'cells under ')} ({src} may " \
                   f"{'protect the cells' if s > 0 else 'make the cells more sensitive'})"
        return f"lines without {src} respond {'less' if s > 0 else 'more'} strongly to {_dd_of(tgt, 'response to ')} " \
               f"({src} may {'strengthen' if s > 0 else 'weaken'} the response)"
    who = f"{src}'s natural level" if kind.startswith("level") else f"{src} activity"
    out = f"{who} {sign_word(s, kind)} {obj}"
    if kind in SENSITIVITY or _g(row, "target_type", "gene") == "cells":
        out += " (protects the cells)" if s > 0 else " (makes them more sensitive)"
    return out


_RX_GENO = re.compile(r"^(\S+) (recorded as loss of function|recorded as gain of function|altered \(any record\)) "
                      r"\((\d+) lines: (.*)\) vs not recorded \((\d+)\)$")
_RX_ALLELE = re.compile(r"^(\S+) (.*?) \((\d+) lines(?:: (.*?))?\) vs other lines \((\d+); (.*)\)$")


def _comp_short(comp):
    return comp.replace(" with a missense change", " missense").replace(
        " truncating, splice or deletion only", " truncating, splice or deletion")


def kind_text(row):
    """The evidence of a row in plain words: 'TP53 change recorded as loss of function in 10 lines (8 missense, 2
    truncating, splice or deletion) vs 8 not recorded'; 'KRAS codon G12 recorded in 6 lines (G12C 2, G12D 2, G12S 1,
    G12V 1) vs 12 other lines (4 of them with another KRAS change)'; 'lines that do not express MTAP (5) vs lines
    expressing it (13)'; "NFE2L2's natural level across 18 lines (lineage-adjusted; a glimpse)"; 'compounds annotated to
    inhibit MTOR: 3 of 6 lower it (Rapamycin, ...)'; 'compounds that trap TOP2A on DNA (TOP2 poisons): 3 of 5 raise it
    (...)'. Older outputs (group words of direction version 4): 'recorded loss-of-function mutation of TP53 in 10 lines
    vs 8 not recorded'."""
    kind = str(_g(row, "kind", ""))
    src = source_text(row)
    na, ni, nl = (int(_num(_g(row, k, -1))) if np.isfinite(_num(_g(row, k, -1))) else -1
                  for k in ("n_altered", "n_intact", "n_lines"))
    grp = str(_g(row, "group", "") or "")
    if kind.startswith("genotype"):
        m = _RX_GENO.match(grp)
        if m:
            how = m.group(2).replace("altered (any record)", "recorded as altered (mechanism not recorded for all)")
            return (f"{m.group(1)} change {how} in {m.group(3)} lines ({_comp_short(m.group(4))}) vs {m.group(5)} not "
                    "recorded")
        m = _RX_ALLELE.match(grp)
        if m:
            return (f"{m.group(1)} {m.group(2)} recorded in {m.group(3)} lines" + (f" ({m.group(4)})" if m.group(4)
                                                                                   else "")
                    + f" vs {m.group(5)} other lines ({m.group(6)})")
        mech = MECH_WORDS.get(str(_g(row, "mechanism", "")), f"{_g(row, 'mechanism', '')} alteration")
        return f"recorded {mech} of {src} in {na} lines vs {ni} not recorded"
    if kind.startswith("null"):
        many = int(_num(_g(row, "n_sources", 1)) or 1) > 1 or len(list(_g(row, "sources", ()) or ())) > 1
        return f"lines that do not express {src} ({na}) vs lines expressing {'them' if many else 'it'} ({ni})"
    if kind.startswith("level"):
        return f"{src}'s natural level across {nl} lines (lineage-adjusted; a glimpse)"
    if kind == "drug_target":
        raw = str(_g(row, "compounds_supporting", "") or "")
        head, _, rest = raw.partition("also significant: ")
        sup = [x for x in head.split("; ") if x.strip()]
        rest = rest.strip()
        nc, ns = int(_num(_g(row, "n_compounds", -1))), int(_num(_g(row, "n_supporting", -1)))
        eff = str(_g(row, "drug_effect", "") or "")
        verb = (eff if ns == 1 else eff[:-1]) if eff in ("raises", "lowers") else ("moves" if ns == 1 else "move")
        mc = str(_g(row, "mechanism_class", "") or "")
        mech = str(_g(row, "mechanism", "") or "")
        if mc in TRAP_WORDS:
            who = f"compounds that {TRAP_WORDS[mc][1].format(t=src)} ({TRAP_WORDS[mc][0]})"
        elif mech in ("inhibitor", "activator") or mech.startswith("inhibitor"):
            who = f"compounds annotated to {'activate' if mech == 'activator' else 'inhibit'} {src}"
        else:
            who = f"compounds annotated to target {src}"
        listed = ", ".join(sup) + (f"; also significant: {rest}" if rest else "")
        return f"{who}: {ns} of {nc} {verb} it" + (f" ({listed})" if listed else "")
    return KIND_WORDS.get(kind, kind)


def grade_legend(style="long"):
    """The grade legend as lines: 'A: strong: ...' (style 'long') or 'A strong' (style 'short')."""
    if style == "short":
        return [f"{g} {GRADE_SHORT[g]}" for g in GRADES]
    return [f"{g}: {GRADE_WORDS[g]}" for g in GRADES]


def caveat_lines():
    """The standing caveat, as a list of sentences (what an arrow does not say)."""
    return list(CAVEAT_LINES)


# ----------------------------------------------------------------------------- alerts
def _reasons(x, col):
    """The reasons of a row's column col, or of a text ('' or ['⚠ '] + '; '-joined reasons)."""
    t = x if isinstance(x, str) else str(_g(x, col, "") or "")
    t = t.strip()
    if t.startswith(ALERT):
        t = t[len(ALERT):].strip()
    return [r.strip() for r in t.split("; ") if r.strip()]


def alert_reasons(alerts):
    """The reasons of an alerts text ('' or '⚠ ' + '; '-joined reasons; a row, or the text itself): the alerts tier
    (an output of an older stage: every reason)."""
    return _reasons(alerts, "alerts")


def note_reasons(row):
    """The notes of a row (or a notes text): graded reasons below their thresholds, and context."""
    return _reasons(row, "notes")


def caveat_reasons(row):
    """The caveats of a row (or a caveats text): what every arrow of its kind carries (kind_caveats)."""
    return _reasons(row, "caveats")


def support_reasons(row):
    """The support of a row (or a support text): evidence for the arrow."""
    return _reasons(row, "support")


def all_reasons(row):
    """Every reason of a row in the stage's order (alerts_all; an older output: its alerts)."""
    every = _reasons(row, "alerts_all") if not isinstance(row, str) else []
    return every or alert_reasons(row)


def kind_caveats(kind):
    """The caveats every arrow of a kind carries (KIND_CAVEATS; () for a kind without one)."""
    return KIND_CAVEATS.get(str(kind or ""), ())


def caveat_header(rows, ascii=False, short=False):
    """The caveats of a list's kinds, to state once above the list (rows: display rows with 'kind', or kinds):
    "Every arrow of the kind 'drug target: level' carries this caveat: drugs can act on other proteins too." - one
    sentence per kind present that has caveats; short: "drug target: level - drugs can act on other proteins too";
    '' when none."""
    if rows is None:
        return ""
    kinds = list(rows["kind"].astype(str).unique()) if hasattr(rows, "columns") else [str(k) for k in rows]
    from_rows = {}
    if hasattr(rows, "columns") and "caveats" in rows.columns and len(rows):
        for k_, t_ in zip(rows["kind"].astype(str), rows["caveats"].fillna("").astype(str)):
            for x in _reasons(t_, "caveats"):
                lst = from_rows.setdefault(k_, [])
                if x not in lst:
                    lst.append(x)
    out = []
    for k in KINDS:
        cv = tuple(from_rows.get(k, ())) or kind_caveats(k)
        if k in kinds and cv:
            if short:
                out.append(f"{KIND_SHORT.get(k, k)} - " + "; ".join(cv))
            elif tuple(cv) == tuple(kind_caveats(k)):
                out.append(f"Every arrow of the kind '{KIND_SHORT.get(k, k)}' carries "
                           f"{'this caveat' if len(cv) == 1 else 'these caveats'}: " + "; ".join(cv) + ".")
            else:                              # from the rows (direction version 5: e.g. each family's controls)
                out.append(f"The arrows of the kind '{KIND_SHORT.get(k, k)}' carry "
                           f"{'this caveat' if len(cv) == 1 else 'these caveats (each arrow the ones of its family)'}: "
                           + "; ".join(cv) + ".")
    return _txt(("; " if short else " ").join(out), ascii)


def _short_label(reason):
    for rx, rep in _SHORT:
        m = rx.search(reason)
        if m:
            if rep == "co-occurs":
                names = re.findall(r"([A-Za-z0-9._-]+)-altered lines", reason)
                return "co-occurs with " + ", ".join(names) if names else "co-occurs"
            if rep == "anti-occurs":
                names = re.findall(r"([A-Za-z0-9._-]+) alteration \(phi", reason)
                return (f"mostly lines without a recorded {', '.join(names)} alteration" if names else
                        "mostly lines without another alteration")
            if rep == "other side":
                names = re.findall(r"([A-Za-z0-9._-]+) alterations are in \d+ of the", reason)
                return (f"{', '.join(names)} alterations on the other side" if names else
                        "another alteration on the other side")
            if rep == "also absent":
                names = re.findall(r"([A-Za-z0-9._-]+)(?: \(\+\d+ absent from the same lines\))? \(overlap", reason)
                return f"also absent: {', '.join(names)}" if names else "other genes also absent"
            return m.expand(rep) if "\\" in rep else rep
    return reason if len(reason) <= 48 else reason[:45].rstrip() + "..."


def alert_short(alerts, ascii=False):
    """The alerts of a row (or an alerts text) in a few words: '⚠ tissue-confounded; few lines (3 vs 15)'; '' when
    it has none. Every reason keeps a label (a reason without a known label: its first words)."""
    labels = list(dict.fromkeys(_short_label(r) for r in alert_reasons(alerts)))
    return _txt(f"{ALERT} " + "; ".join(labels), ascii) if labels else ""


def alert_long(alerts, ascii=False):
    """The alerts of a row in full ('⚠ ' + every reason, '; '-joined), '' when it has none."""
    r = alert_reasons(alerts)
    return _txt(f"{ALERT} " + "; ".join(r), ascii) if r else ""


def _labels(reasons):
    return "; ".join(dict.fromkeys(_short_label(r) for r in reasons))


def notes_short(row, ascii=False):
    """The notes of a row in a few words ('within organs, on part of the lines; artifact flags'; no sign), '' when
    it has none."""
    return _txt(_labels(note_reasons(row)), ascii)


def notes_long(row, ascii=False):
    """The notes of a row in full ('; '-joined; no sign), '' when it has none."""
    return _txt("; ".join(note_reasons(row)), ascii)


def support_short(row, ascii=False):
    """The support of a row in a few words ('3 compounds'; 'deletion recorded too'), '' when none."""
    return _txt(_labels(support_reasons(row)), ascii)


def support_long(row, ascii=False):
    """The support of a row in full, '' when none."""
    return _txt("; ".join(support_reasons(row)), ascii)


# ----------------------------------------------------------------------------- lines and texts
def _count(row, col, reasons):
    v = _num(_g(row, col, np.nan))
    return int(v) if np.isfinite(v) else len(reasons)


def texts(row, ascii=False, max_names=None):
    """Every text of a row at once, for a surface to compose: arrow, source, target, grade, grade_words, sign
    (+1/-1/0), sign_word, sign_text, kind, kind_short, kind_text, reading (direction.py's sentence), q, p,
    q_group, q_text, alerts_short, alerts_long, has_alert, n_alerts, notes_short, notes_long, has_note, n_notes,
    caveats_long, n_caveats, support_short, support_long, n_support, n_sources."""
    g = str(_g(row, "grade", ""))
    out = {"arrow": edge_arrow(row, ascii, max_names), "source": source_text(row, max_names),
           "target": str(_g(row, "target", "")), "grade": g, "grade_words": GRADE_WORDS.get(g, ""),
           "sign": _sign(row), "sign_word": sign_word(_g(row, "sign", 0), _g(row, "kind", "")),
           "sign_text": sign_text(row), "kind": str(_g(row, "kind", "")),
           "kind_short": KIND_SHORT.get(str(_g(row, "kind", "")), str(_g(row, "kind", ""))),
           "kind_text": kind_text(row), "reading": str(_g(row, "reading", "") or ""),
           "q": fmt_q(_g(row, "q")), "p": fmt_q(_g(row, "p")), "q_group": fmt_q(_g(row, "q_group")),
           "q_text": q_text(row),
           "alerts_short": alert_short(row), "alerts_long": alert_long(row),
           "has_alert": bool(alert_reasons(row)), "n_sources": int(_g(row, "n_sources", 1) or 1)}
    nr, cr, sr = note_reasons(row), caveat_reasons(row), support_reasons(row)
    out.update({"n_alerts": len(alert_reasons(row)), "notes_short": notes_short(row), "notes_long": notes_long(row),
                "has_note": bool(nr), "n_notes": len(nr), "caveats_long": "; ".join(cr), "n_caveats": len(cr),
                "support_short": support_short(row), "support_long": "; ".join(sr), "n_support": len(sr)})
    if ascii:
        out = {k: (ascii_signs(v) if isinstance(v, str) else v) for k, v in out.items()}
    return out


def q_text(row):
    """'q 0.003'; a result significant only within its own group (or drug-dose): 'q 0.24 over the table, 0.006 within
    its group'."""
    q, qg = _num(_g(row, "q")), _num(_g(row, "q_group"))
    if np.isfinite(q) and q >= 0.10 and np.isfinite(qg) and qg < 0.10:
        where = "its drug-dose" if str(_g(row, "kind", "")) == "level_sensitivity" else "its group"
        return f"q {fmt_q(q)} over the table, {fmt_q(qg)} within {where}"
    return f"q {fmt_q(q)}"


def edge_line(row, ascii=False, alerts="short", max_names=None, notes=True):
    """One line for a row: 'TP53 → CDKN1A  [A]  TP53 activity raises CDKN1A's drug response (mutation: response;
    q 0.003)  ⚠ ...  · notes: ...'. alerts: 'short', 'long' or 'none'; notes: True / 'short' (the notes' short
    labels), 'long' (in full) or False / 'none'. The kind's caveats are not repeated on the line (caveat_header
    states them once above a list)."""
    t = texts(row, ascii, max_names)
    al = {"short": t["alerts_short"], "long": t["alerts_long"]}.get(alerts, "")
    nt = {"short": t["notes_short"], "long": t["notes_long"]}.get("short" if notes is True else notes, "")
    dot = "-" if ascii else "·"
    return f"{t['arrow']}  [{t['grade']}]  {t['sign_text']} ({t['kind_short']}; {t['q_text']})" + (
        f"  {al}" if al else "") + (f"  {dot} notes: {nt}" if nt else "")


CONTROLS_CAVEAT = ("'Up to' is the 95% upper bound of that estimate: the controls are a small sample (no false arrow "
                   "from 60 random groups still allows about 3 per 60 groups), and the natural-level controls are one "
                   "shuffle each. The estimate can be low when the real groups overlap other alterations, tissue "
                   "programmes or each other, which random groups do not.")


def expected_text(x, fmt="{:.2f}", na="-"):
    """An expected-false count of controls.json with its 95% upper bound: '0.00 (up to 1.90)'; na when missing."""
    x = x or {}
    v, u = _num(x.get("expected_false")), _num(x.get("expected_false_upper"))
    if not np.isfinite(v):
        return na
    return fmt.format(v) + (f" (up to {fmt.format(u)})" if np.isfinite(u) else "")


def more_text(n_more, n_more_alert, what="rows"):
    """'12 more rows (5 of them with an alert ⚠)' for what a capped list leaves out ('' when nothing)."""
    if n_more <= 0:
        return ""
    w = what[:-1] if n_more == 1 and what.endswith("s") and not what.endswith("ss") else what
    return f"{n_more:,} more {w}" + (f" ({n_more_alert:,} of them with an alert {ALERT})" if n_more_alert else "")


def counts_text(rows, what="rows"):
    """'12 rows, 5 with ⚠, 3 with notes; grade A 2, B 3, C 7; every row of a kind carries that kind's caveat (stated
    above)' ('none' for an empty list; 'row' is `what` in the singular). 'with notes' when the rows hold the notes
    count (n_notes); the caveat clause when a kind with caveats is among them (caveat_header gives the text to state
    above)."""
    n = 0 if rows is None else len(rows)
    if not n:
        return "none"
    k = int(rows["has_alert"].sum()) if "has_alert" in rows else 0
    gr = rows["grade"].value_counts()
    w = what[:-1] if n == 1 and what.endswith("s") else what
    out = f"{n:,} {w}, {k:,} with {ALERT}"
    if "n_notes" in rows:
        out += f", {int((pd.to_numeric(rows['n_notes'], errors='coerce').fillna(0) > 0).sum()):,} with notes"
    out += "; grade " + ", ".join(f"{g} {int(gr.get(g, 0)):,}" for g in GRADES)
    if "kind" in rows and any(kind_caveats(x) for x in rows["kind"].astype(str).unique()):
        one = what[:-1] if what.endswith("s") and not what.endswith("ss") else what
        out += f"; every {one} of a kind carries that kind's caveat (stated above)"
    return out


def cap(rows, n):
    """The cap rule (rule 1) on a listing in ORDER: the n strongest rows, and any of the n strongest without an alert
    that fall beyond them, in order. Returns (shown rows, how many more, how many of those carry an alert). n None:
    all."""
    if rows is None or not len(rows):
        return rows, 0, 0
    alert = rows["has_alert"].to_numpy(dtype=bool) if "has_alert" in rows else \
        np.array([bool(alert_reasons(a)) for a in rows["alerts"]], dtype=bool)
    keep = cap_keep(alert, n)
    rest = np.setdiff1d(np.arange(len(rows)), keep)
    return rows.iloc[keep], int(rest.size), int(alert[rest].sum())


def order(df):
    """df (edges or display rows) in ORDER: grade A, B, C, then q, then |effect| (|contrast|, largest first), then p,
    kind, source, target. Deterministic (stable sort)."""
    if df is None or not len(df):
        return df
    k = pd.DataFrame({"g": df["grade"].map({g: i for i, g in enumerate(GRADES)}).fillna(9).to_numpy(),
                      "q": pd.to_numeric(df["q"], errors="coerce").fillna(np.inf).to_numpy(),
                      "e": -pd.to_numeric(df["contrast"], errors="coerce").abs().fillna(-np.inf).to_numpy(),
                      "p": pd.to_numeric(df["p"], errors="coerce").fillna(np.inf).to_numpy(),
                      "k": df["kind"].map({x: i for i, x in enumerate(KINDS)}).fillna(99).to_numpy(),
                      "s": df["source"].astype(str).to_numpy(), "t": df["target"].astype(str).to_numpy()})
    o = k.sort_values(list(k.columns), kind="mergesort").index.to_numpy()
    return df.iloc[o]


# ----------------------------------------------------------------------------- loading
_CACHE = {}


def available(out):
    """The direction stage's edges exist in this output folder."""
    return os.path.exists(os.path.join(out, "direction", "edges.parquet"))


def load(out, cache=True):
    """The direction stage's results as a Direction (rows indexed for look-ups), or None when the stage has not run
    (an output folder made before it existed, or the stage not finished). Cached per folder while edges.parquet is
    unchanged."""
    p = os.path.join(out, "direction", "edges.parquet")
    if not os.path.exists(p):
        return None
    st = os.stat(p)
    key = os.path.abspath(out)
    sig = (st.st_mtime_ns, st.st_size)
    if cache and key in _CACHE and _CACHE[key][0] == sig:
        return _CACHE[key][1]
    d = Direction(out)
    if cache:
        _CACHE[key] = (sig, d)
    return d


def _read_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def _natural(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", str(s))]


def _compounds_of(row):
    """drug_target: the class's compounds ('compounds' column; for an edges table without it, from the group text
    'X inhibitors: A, B (2 compounds)')."""
    c = str(row.get("compounds", "") or "")
    if c:
        return [x for x in c.split("; ") if x]
    g = str(row.get("group", "") or "")
    m = re.match(r"^.*?s: (.*) \(\d+ compounds\)$", g)
    return [x.strip() for x in m.group(1).split(", ")] if m else []


class Direction:
    """OUT/direction read once: edges (the edges of edges.parquet in ORDER, with edge_id and has_alert), rows (the
    display rows, collapsed, in ORDER, with the added columns of the module docstring), groups (groups.parquet),
    controls (controls.json), info (info.json), and the look-ups."""

    def __init__(self, out):
        self.out = out
        d = os.path.join(out, "direction")
        e = pd.read_parquet(os.path.join(d, "edges.parquet"))
        e = e.reset_index(drop=True)
        e["edge_id"] = np.arange(len(e), dtype=np.int64)
        for c, v in (("compounds", ""), ("compounds_supporting", ""), ("drug_effect", "")):
            if c not in e:
                e[c] = v
        if len(e) and (e["kind"] == "drug_target").any():         # an edges table without the columns: derive them
            dt = e["kind"] == "drug_target"
            miss = dt & (e["compounds"].fillna("") == "")
            if miss.any():
                e.loc[miss, "compounds"] = ["; ".join(_compounds_of(r)) for r in e[miss].to_dict("records")]
            miss = dt & (e["drug_effect"].fillna("") == "")
            if miss.any():
                e.loc[miss, "drug_effect"] = np.where(e.loc[miss, "reading"].str.contains(" lowers "), "lowers",
                                                      "raises")
        self.tiered = _ensure_tiers(e)
        e["has_alert"] = e["n_alerts"].to_numpy() > 0
        e["has_note"] = e["n_notes"].to_numpy() > 0
        self.edges = order(e).reset_index(drop=True)
        self.groups = pd.read_parquet(os.path.join(d, "groups.parquet")) if os.path.exists(
            os.path.join(d, "groups.parquet")) else pd.DataFrame()
        if len(self.groups.columns) and "alerts" in self.groups:
            for c, v in (("notes", ""), ("alerts_all", None)):
                if c not in self.groups:                     # an older stage: alerts = every reason
                    self.groups[c] = v if v is not None else [
                        "; ".join(alert_reasons(str(a or ""))) for a in self.groups["alerts"]]
        self.controls = _read_json(os.path.join(d, "controls.json"))
        self.info = _read_json(os.path.join(d, "info.json"))
        self._drugdoses()
        self.rows = self._collapse(self.edges)
        self._index()

    # ---- the drug-doses of the sensitivity targets
    def _drugdoses(self):
        self.dd = None
        p = os.path.join(self.out, "atlas", "effects", "drugdose.csv")
        if os.path.exists(p):
            try:
                self.dd = pd.read_csv(p, dtype={"drug": str, "dose": str}, keep_default_na=False,
                                      na_values=[""], usecols=lambda c: c in ("drug", "dose", "conc"))
            except (OSError, ValueError):
                self.dd = None
        e = self.edges
        drug = np.full(len(e), "", dtype=object)
        dose = np.full(len(e), "", dtype=object)
        if len(e):
            tdd = e["target_dd"].to_numpy(dtype=np.int64)
            nd = len(self.dd) if self.dd is not None else 0
            ok = (tdd >= 0) & (tdd < nd)
            if ok.any():
                drug[ok] = self.dd["drug"].astype(str).to_numpy(dtype=object)[tdd[ok]]
                if "dose" in self.dd:
                    dose[ok] = self.dd["dose"].astype(str).to_numpy(dtype=object)[tdd[ok]]
            tgt = e["target"].astype(str).to_numpy(dtype=object)
            for i in np.flatnonzero((tdd >= 0) & ~ok):              # no drugdose.csv: 'cells under DRUG DOSE µM'
                m = re.match(r"^cells under (.*?)(?: (\S+) µM)?$", tgt[i])
                if m:
                    drug[i], dose[i] = m.group(1), m.group(2) or ""
        e["target_drug"] = drug
        e["target_dose"] = dose

    # ---- one row per test
    def _collapse(self, e):
        """Display rows: drug_target edges that are one test for several targets (the same compounds, mechanism,
        target, effect and p) and expression-null edges of genes absent from exactly the same lines (same group,
        target and p) become one row naming every source. Everything else stays as it is. Works on plain arrays and
        writes each column once (a cell-by-cell write into a string column is slow at full scale)."""
        n = len(e)
        src = e["source"].astype(str).to_numpy(dtype=object)
        scol = e["source_col"].to_numpy(dtype=np.int64)
        eid = e["edge_id"].to_numpy(dtype=np.int64)
        kind = e["kind"].astype(str).to_numpy(dtype=object)
        new = {"members": [(int(i),) for i in eid], "sources": [(s_,) for s_ in src],
               "source_cols": [(int(c_),) for c_ in scol], "n_sources": np.ones(n, dtype=np.int64)}
        cols = {c_: e[c_].to_numpy(dtype=object).copy() for c_ in ("source", "reading", "group") + _TEXT_TIERS}
        cols["source_col"] = scol.copy()
        for c_ in _N_TIERS:
            cols[c_] = e[c_].to_numpy(dtype=np.int64).copy()
        cols["has_alert"] = e["has_alert"].to_numpy(dtype=bool).copy()
        cols["has_note"] = e["has_note"].to_numpy(dtype=bool).copy()
        drop = np.zeros(n, dtype=bool)
        dt = kind == "drug_target"
        nl = np.array([str(k_).startswith("null") for k_ in kind], dtype=bool)
        if n and (dt | nl).any():
            if "test_id" in e.columns:                                 # direction version 5: one id per test
                keys = pd.DataFrame({"tid": e["test_id"].to_numpy(dtype=np.int64)})
            else:
                keys = pd.DataFrame({
                    "kind": kind, "target": e["target"].astype(str).to_numpy(dtype=object),
                    "tc": e["target_col"].to_numpy(dtype=np.int64), "tdd": e["target_dd"].to_numpy(dtype=np.int64),
                    "group": np.where(nl, e["group"].fillna("").astype(str).to_numpy(dtype=object), ""),
                    "comp": np.where(dt, e["compounds"].fillna("").astype(str).to_numpy(dtype=object), ""),
                    "mech": np.where(dt, e["mechanism"].fillna("").astype(str).to_numpy(dtype=object), ""),
                    "eff": np.where(dt, e["drug_effect"].fillna("").astype(str).to_numpy(dtype=object), ""),
                    "sign": e["sign"].to_numpy(dtype=np.int64),
                    "ns": np.where(dt, e["n_supporting"].to_numpy(dtype=np.int64), -1),
                    "nc": np.where(dt, e["n_compounds"].to_numpy(dtype=np.int64), -1),
                    "p": e["p"].to_numpy(dtype=np.float64)})
            pos_of = np.flatnonzero(dt | nl)
            for ix in keys.iloc[pos_of].groupby(list(keys.columns), sort=False, dropna=False).indices.values():
                if len(ix) < 2:
                    continue
                pos = sorted((int(x) for x in pos_of[ix]), key=lambda j_: _natural(src[j_]))
                m = self._merged(pos, src, scol, eid, cols, e)
                i0 = pos[0]
                for c_ in ("members", "sources", "source_cols"):
                    new[c_][i0] = m[c_]
                new["n_sources"][i0] = m["n_sources"]
                for c_ in ("source", "source_col", "reading", "group", "has_alert", "has_note") + _TEXT_TIERS \
                        + _N_TIERS:
                    cols[c_][i0] = m[c_]
                drop[pos[1:]] = True
        rows = e.copy()
        for c_, v in cols.items():
            rows[c_] = v if c_ not in ("source", "reading", "group") + _TEXT_TIERS else pd.array(v, dtype=e[c_].dtype)
        for c_, v in new.items():
            rows[c_] = pd.Series(v, index=rows.index, dtype=object) if c_ != "n_sources" else v
        rows = rows[~drop]
        rows = order(rows).reset_index(drop=True)
        rows["order"] = np.arange(len(rows), dtype=np.int64)
        rows["effect"] = pd.to_numeric(rows["contrast"], errors="coerce").abs()
        return rows

    @staticmethod
    def _merged(pos, src, scol, eid, cols, e):
        """The display row of the edges at positions pos (one test, several sources): every source named, alerts
        merged."""
        i0 = pos[0]
        srcs = tuple(str(src[j]) for j in pos)
        scs = tuple(int(scol[j]) for j in pos)
        joined = ", ".join(srcs)
        shared, coabs, co_names, co_total = [], False, [], 0

        def special(x):
            """A member's reason that the merged row words once for all its sources (both are alerts)."""
            return x.startswith("the supporting compounds also share ") or bool(_COABS.search(x))
        for j in pos:
            for x in all_reasons(str(cols["alerts_all"][j] or "")):
                if x.startswith("the supporting compounds also share "):
                    shared += [s_.strip() for s_ in x[len("the supporting compounds also share "):].split(":")[0]
                               .split(", ")]
                    continue
                m_ = _COABS.search(x)
                if m_:                       # 'N other gene(s) are absent from exactly these lines (B, C, ...)'
                    coabs = True
                    co_total = max(co_total, int(m_.group(1)) + 1)
                    co_names += [s_.strip() for s_ in m_.group(2).split(", ") if s_.strip() and s_.strip() != "..."]
        tier = {}
        for c_ in _TEXT_TIERS:
            got = []
            for j in pos:
                for x in _reasons(str(cols[c_][j] or ""), c_):
                    if x not in got and not special(x):
                        got.append(x)
            tier[c_] = got
        reasons = tier["alerts"]
        kind = str(e["kind"].iat[i0])
        reading, group = str(cols["reading"][i0]), str(cols["group"][i0])
        if kind == "drug_target":
            comps = str(e["compounds"].iat[i0] or "").replace("; ", ", ")
            reasons.append(f"the {len(srcs)} targets named share these compounds ({comps}) and this result: any of "
                           "them could be the cause")
            others = [s_ for s_ in dict.fromkeys(shared) if s_ and s_ not in srcs]
            if others:
                reasons.append(f"the supporting compounds also share {', '.join(others)}: any of them could be the "
                               "cause instead")
            reading = reading.replace(f" {src[i0]} ", f" {joined} ", 1).replace(
                f"({src[i0]} activity may", "(their activity may")
            group = re.sub(r"^\S+ ", f"{joined} ", group, count=1)
        elif coabs or len(srcs) > 1:
            # every gene absent from these lines, also those that are not a source of this row (the stage writes a
            # response or baseline row only to each gene's own related partners)
            others = [s_ for s_ in dict.fromkeys(co_names) if s_ not in srcs]
            n_rest = max(0, co_total - len(srcs) - len(others))
            extra = (f" and {', '.join(others)}" if others else "") + (f" and {n_rest} more" if n_rest else "")
            reasons.append(f"the {len(srcs)} genes named{extra} are absent from exactly the same lines: any of them "
                           "could be the cause" if len(srcs) > 1 else
                           f"{srcs[0]}{extra} are absent from exactly the same lines: any of them could be the cause")
            g0 = group.split(" ")[0] if group else ""
            if len(srcs) > 1 and g0:          # the reading names the line set's first gene: name them all
                reading = reading.replace(f"lines without {g0}", f"lines without {joined}").replace(
                    f"lines expressing {g0}", "lines expressing them")
        merged_new = [r_ for r_ in reasons if r_ not in tier["alerts_all"]]   # the reasons this merge adds
        tier["alerts_all"] = tier["alerts_all"] + merged_new

        def plain(rs):
            return "; ".join(r_.replace("; ", ", ") for r_ in rs)
        out = {"source": joined, "source_col": scs[0] if len(set(scs)) == 1 else -1, "sources": srcs,
               "source_cols": scs, "n_sources": len(srcs), "members": tuple(int(eid[j]) for j in pos),
               "reading": reading, "group": group, "has_alert": bool(reasons), "has_note": bool(tier["notes"]),
               "alerts": f"{ALERT} " + plain(reasons) if reasons else ""}
        for c_ in ("notes", "caveats", "support", "alerts_all"):
            out[c_] = plain(tier[c_])
        for c_ in TIERS:
            out[f"n_{c_}"] = len(tier[c_])
        return out

    # ---- indexes
    def _index(self):
        """Positions (in ORDER) per key, for the display rows and for the edges: upstream (gene targets, by target
        col / symbol), downstream (gene targets, by every source's col / symbol), cells (sensitivity rows, by
        source), drug-dose, drug (name and salt base) and compound."""
        self._ix = {k: {} for k in ("up_col", "up_sym", "down_col", "down_sym", "cells_col", "cells_sym", "dd", "drug",
                                    "comp", "e_up_col", "e_up_sym", "e_down_col", "e_down_sym", "e_cells_col",
                                    "e_cells_sym")}
        ix = self._ix

        def add(name, key, i):
            ix[name].setdefault(key, []).append(i)
        r = self.rows
        cells = r["target_type"].astype(str).isin(DRUGDOSE_TARGETS).to_numpy() if len(r) else np.zeros(0, bool)
        for i, (ss, cc, t, tc, dd, drug, kind, comps) in enumerate(zip(
                r["sources"], r["source_cols"], r["target"], r["target_col"], r["target_dd"], r["target_drug"],
                r["kind"], r["compounds"])):
            role = "cells" if cells[i] else "down"
            for s_, c_ in zip(ss, cc):
                add(f"{role}_sym", str(s_).upper(), i)
                if int(c_) >= 0:
                    add(f"{role}_col", int(c_), i)
            if not cells[i]:
                add("up_sym", str(t).upper(), i)
                if int(tc) >= 0:
                    add("up_col", int(tc), i)
            if int(dd) >= 0:
                add("dd", int(dd), i)
                for k in _drug_keys(drug):
                    add("drug", k, i)
            if kind == "drug_target":
                for c_ in str(comps or "").split("; "):
                    for nm_ in c_.split(" / "):          # one molecule under several names: 'A / A citrate'
                        for k in _drug_keys(nm_):
                            add("comp", k, i)
        e = self.edges
        ecells = e["target_type"].astype(str).isin(DRUGDOSE_TARGETS).to_numpy() if len(e) else np.zeros(0, bool)
        for i, (s_, c_, t, tc) in enumerate(zip(e["source"], e["source_col"], e["target"], e["target_col"])):
            role = "e_cells" if ecells[i] else "e_down"
            add(f"{role}_sym", str(s_).upper(), i)
            if int(c_) >= 0:
                add(f"{role}_col", int(c_), i)
            if not ecells[i]:
                add("e_up_sym", str(t).upper(), i)
                if int(tc) >= 0:
                    add("e_up_col", int(tc), i)
        for d in ix.values():
            for k in d:
                d[k] = np.array(sorted(set(d[k])), dtype=np.int64)
        self._empty_rows = self.rows.iloc[:0]
        self._empty_edges = self.edges.iloc[:0]

    def _take(self, pos, collapse=True, kinds=None):
        """The rows (collapse) or edges at positions pos (ascending = in ORDER), optionally of these kinds only. An
        empty result is a shared empty frame: treat every result as read-only (copy before changing it)."""
        if not len(pos):
            return self._empty_rows if collapse else self._empty_edges
        sub = (self.rows if collapse else self.edges).iloc[pos]
        if kinds is not None:
            sub = sub[sub["kind"].isin(list(kinds))]
        return sub

    def _gene(self, gene, role, collapse):
        pre = "" if collapse else "e_"
        if isinstance(gene, (int, np.integer)):
            pos = self._ix[f"{pre}{role}_col"].get(int(gene), _EMPTY)
        else:
            pos = self._ix[f"{pre}{role}_sym"].get(str(gene).strip().upper(), _EMPTY)
        return pos

    # ---- look-ups
    def upstream(self, gene, collapse=True, kinds=None):
        """Rows whose target is the gene (col or symbol): who probably acts on it. In ORDER."""
        return self._take(self._gene(gene, "up", collapse), collapse, kinds)

    def downstream(self, gene, collapse=True, kinds=None):
        """Rows whose source is the gene (or one of a collapsed row's sources) and whose target is a gene: what it
        probably acts on. In ORDER."""
        return self._take(self._gene(gene, "down", collapse), collapse, kinds)

    def cells(self, gene, collapse=True, kinds=None):
        """Rows whose source is the gene and whose target is the cells under a drug-dose (sensitivity kinds): how it
        probably acts on the cells' growth under a drug. In ORDER."""
        return self._take(self._gene(gene, "cells", collapse), collapse, kinds)

    def for_drugdose(self, dd):
        """Sensitivity rows whose target_dd is drug-dose row dd (atlas/effects/drugdose.csv). In ORDER."""
        return self._take(self._ix["dd"].get(int(dd), _EMPTY))

    def sensitivity(self, drug):
        """Sensitivity rows at any drug-dose of the drug (its name as in drugdose.csv or its salt base, any case). In
        ORDER."""
        return self._take(_union(self._ix["drug"], _drug_keys(drug)))

    def drug_targets(self, drug, collapse=True):
        """drug_target rows in which the drug is one of the class's compounds (name or salt base, any case). In
        ORDER; collapse=False: the edges one by one."""
        pos = _union(self._ix["comp"], _drug_keys(drug))
        rows = self._take(pos)
        if collapse:
            return rows
        ids = sorted({i for m in rows["members"] for i in m})
        return self.edges[self.edges["edge_id"].isin(ids)]

    def for_drug(self, drug, collapse=True):
        """{'cells': sensitivity(drug), 'targets': drug_targets(drug)}."""
        return {"cells": self.sensitivity(drug), "targets": self.drug_targets(drug, collapse)}

    def gene_counts(self, gene):
        """{'upstream': n, 'downstream': n, 'cells': n, 'with_alert': n of them} - display rows."""
        u, d, c = self.upstream(gene), self.downstream(gene), self.cells(gene)
        return {"upstream": len(u), "downstream": len(d), "cells": len(c),
                "with_alert": int(u["has_alert"].sum() + d["has_alert"].sum() + c["has_alert"].sum())}

    def members(self, row):
        """The edges (edges.parquet rows, in ORDER) a display row stands for."""
        return self.edges[self.edges["edge_id"].isin(list(_g(row, "members", ()) or ()))]

    def group(self, row):
        """The groups.parquet record of a genotype or expression-null row's comparison (its lines, organs, alerts)
        as a dict, or None (drug_target and level rows have none)."""
        if not len(self.groups) or not str(_g(row, "kind", "")).startswith(("genotype", "null")):
            return None
        g = self.groups[self.groups["description"] == _g(row, "group", "")]
        return g.iloc[0].to_dict() if len(g) else None

    def control_alerts(self, key, v):
        """The alert marks of a positive control of controls.json (key, its dict): {name: has an alert} for the arrows
        it names (per_gene genes, drug-dose targets, KEAP1 genes). From the control's own flags; for an older
        controls.json without them, from the edges (kind, source TP53 / KEAP1, target)."""
        out = {}
        if "per_gene" in v:
            for x in v["per_gene"]:
                if "alert" in x:
                    out[str(x["gene"])] = bool(x["alert"])
                elif x.get("edge"):
                    out[str(x["gene"])] = self._edge_alert("genotype_response", "TP53", str(x["gene"]))
        elif "drugdoses_tested" in v:
            fl = v.get("drugdoses_alert")
            for i, t in enumerate(v.get("drugdoses") or []):
                out[str(t)] = bool(fl[i]) if fl is not None and i < len(fl) else \
                    self._edge_alert("genotype_sensitivity", "TP53", str(t))
        elif v.get("genes"):
            fl = v.get("genes_alert")
            src = key.split(" ")[0] if key else "KEAP1"
            for i, t in enumerate(v.get("genes") or []):
                out[str(t)] = bool(fl[i]) if fl is not None and i < len(fl) else \
                    self._edge_alert("genotype_baseline", src, str(t))
        return out

    def _edge_alert(self, kind, source, target):
        e = self.edges
        if not len(e):
            return False
        m = (e["kind"] == kind) & (e["source"].astype(str) == source) & (e["target"].astype(str) == target)
        return bool(e.loc[m, "has_alert"].any())

    def counts(self):
        """{kind: {grade: n display rows}} and the totals."""
        r = self.rows
        out = {k: {g: int(((r["kind"] == k) & (r["grade"] == g)).sum()) for g in GRADES} for k in KINDS}
        return {"by_kind": out, "rows": int(len(r)), "edges": int(len(self.edges)),
                "with_alert": int(r["has_alert"].sum()) if len(r) else 0}


_EMPTY = np.zeros(0, dtype=np.int64)
_COABS = re.compile(r"(\d+) other gene\(s\) are absent from exactly these lines \((.*)\)")
_TEXT_TIERS = ("alerts", "notes", "caveats", "support", "alerts_all")
_N_TIERS = ("n_alerts", "n_notes", "n_caveats", "n_support")


def _ensure_tiers(e):
    """Give an edges table of an older stage (no tier columns) the tier columns in place: alerts = every reason (as
    before), notes / caveats / support empty, alerts_all = every reason, the counts from the texts. Returns whether the
    table had the tiers (direction VERSION 3)."""
    tiered = all(c in e for c in _TEXT_TIERS + _N_TIERS)
    if not len(e.columns):
        return tiered
    if "alerts" not in e:
        e["alerts"] = ""
    e["alerts"] = e["alerts"].fillna("").astype(str)
    if not tiered:
        for c in ("notes", "caveats", "support"):
            if c not in e:
                e[c] = ""
        if "alerts_all" not in e:
            e["alerts_all"] = ["; ".join(alert_reasons(a)) for a in e["alerts"]]
        e["n_alerts"] = np.array([len(alert_reasons(a)) for a in e["alerts"]], dtype=np.int16)
        for c in ("notes", "caveats", "support"):
            if f"n_{c}" not in e:
                e[f"n_{c}"] = np.array([len(_reasons(str(t or ""), c)) for t in e[c]], dtype=np.int16)
    for c in ("notes", "caveats", "support", "alerts_all"):
        e[c] = e[c].fillna("").astype(str)
    if "art_share" not in e:
        e["art_share"] = np.float32(np.nan)
    if "drugdoses_all" not in e:
        e["drugdoses_all"] = ""
    return tiered


@functools.lru_cache(maxsize=None)
def _drug_keys(name):
    """The keys a drug is found by: its name and its salt base, lower case."""
    s = str(name or "").strip()
    if not s:
        return ()
    keys = [s.lower()]
    try:
        b = str(T.salt_base(s)).strip().lower()
    except Exception:  # noqa: BLE001  (an odd name: its own key only)
        b = ""
    if b and b not in keys:
        keys.append(b)
    return tuple(keys)


def _union(index, keys):
    parts = [index[k] for k in keys if k in index]
    if not parts:
        return _EMPTY
    return np.unique(np.concatenate(parts))
