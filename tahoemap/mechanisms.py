"""mechanisms - which mechanism class each screened drug is in, and Tahoe's and ChEMBL's annotations side by side.

Not a stage: the reference stage calls assign_classes() and writes the three tables below; every later stage reads
them through drug_annotations(), drug_mechanisms() and drug_classes() (or the helpers members(), classes_by_drug(),
class_info(), class_text(), trap_class()).

The classes, their rules and their sources are code constants in tahoemap/data/drug_classes.json (cited, like
tahoemap/data/control_sets.json). A drug is in a class by one of three routes, and each membership row names its
route in 'source':
    code constant (tahoemap/data/drug_classes.json; <citation>)    'molecule_classes', by the molecule key of the
                                                                    Tahoe name or of the matched ChEMBL name
    ChEMBL <release>: <mechanism text> (<ChEMBL id>)                'mechanism_rules' on ChEMBL's curated mechanisms
    WHO ATC <code> (via ChEMBL)                                     'atc_rules' on the ATC codes ChEMBL reports
Tahoe's own annotation (targets, moa-fine, moa-broad) is never changed and never makes a class: it is shown next to
ChEMBL's, with an alert where they disagree ('Targets differ', 'Mechanism differs', 'Action differs', 'Identity
unsure'). Tubulin drugs: a drug that is both a stabiliser and a destabiliser by the rules keeps only
TUBULIN_STABILISER, and that row's source says so ('not counted as a destabiliser: ...').

The three tables (reference/):
    drug_annotations.parquet   one row per drug (DRUG_COLUMNS): Tahoe's annotation, the matched ChEMBL molecule,
                               its mechanisms, actions, targets and ATC codes, mechanism_classes (class labels,
                               '; '-joined), annotation_status, annotation_alert and annotation_note (' | '-joined)
    drug_mechanisms.parquet    one row per (drug, ChEMBL mechanism) (MECH_COLUMNS); target_genes ', '-joined
    drug_classes.parquet       one row per (drug, class) (CLASS_COLUMNS): label, effect, poison, targets ('; '-joined
                               symbols or the regular expression), verb, source ('; '-joined)
Without ChEMBL (offline and not cached) the tables hold the constant classes only, and every drug's annotation_status
is 'ChEMBL not loaded'. On an output made before these tables existed the readers compute that constant-only result
from the drugs of atlas/effects/drugdose.csv, so every reader works offline and on older outputs.
"""

import json
import os
import re

import numpy as np
import pandas as pd

from . import tlib as T

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "drug_classes.json")
# trailing words of a drug name that name its salt or hydrate form ('Ixazomib citrate' -> 'Ixazomib'); direction.py
# reads them from here
SALT_WORDS = ("acetate", "besylate", "bitartrate", "bromide", "calcium", "chloride", "citrate", "dihydrochloride",
              "dimaleate", "dimesylate", "disodium", "ditosylate", "fumarate", "hemifumarate", "hydrobromide",
              "hydrochloride", "hydrate", "lactate", "maleate", "malate", "mesylate", "monohydrate", "phosphate",
              "potassium", "sesquihydrate", "sodium", "succinate", "sulfate", "tartrate", "tosylate",
              "trifluoroacetate", "trihydrochloride", "hcl", "tfa")
CATIONS = ("calcium", "sodium", "potassium", "magnesium", "zinc", "lithium")
GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon", "κ": "kappa", "ω": "omega"}
NAME_RULES = ("name", "salt_base", "cation_first", "molecule_key")      # tried in this order (each also Greek-spelt)
NAME_RULE_TEXT = {"name": "the Tahoe name", "salt_base": "the name without the salt in brackets",
                  "cation_first": "the salt written first", "molecule_key": "the name without trailing salt words"}
SHORT_LIST = 8                                 # genes named in an alert text before 'and N more (all N: ...)'
DRUG_COLUMNS = ["drug", "salt_base", "tahoe_targets", "tahoe_moa_fine", "tahoe_moa_broad", "pubchem_cid", "inchikey",
                "chembl_id", "chembl_name", "chembl_max_phase", "chembl_matched_by", "chembl_n_mechanisms",
                "chembl_mechanisms", "chembl_actions", "chembl_targets", "chembl_atc", "mechanism_classes",
                "annotation_status", "annotation_alert", "annotation_note"]
MECH_COLUMNS = ["drug", "chembl_id", "mechanism_of_action", "action_type", "direction", "target_chembl_id",
                "target_name", "target_type", "target_organism", "target_genes", "n_target_genes", "binding_site",
                "direct_interaction", "classes", "refs"]
CLASS_COLUMNS = ["drug", "class", "label", "effect", "poison", "targets", "verb", "source"]
FILES = {"annotations": "drug_annotations.parquet", "mechanisms": "drug_mechanisms.parquet",
         "classes": "drug_classes.parquet"}
NOT_LOADED = "ChEMBL not loaded"
# ChEMBL's mechanism text for a molecule whose mechanism it does not know: such a row is kept in drug_mechanisms, but
# the drug counts as having no ChEMBL mechanism (status NO_MECH_UNKNOWN; not counted in chembl_with_mechanism)
UNKNOWN_MECHANISMS = ("unknown",)
NO_MECH_UNKNOWN = "no ChEMBL mechanism (ChEMBL: Unknown)"
CONSTANT = "code constant (tahoemap/data/drug_classes.json; {})"
STAB, DESTAB = "TUBULIN_STABILISER", "TUBULIN_DESTABILISER"

_RULES = {}
_TABLES = {}


# ----------------------------------------------------------------------------- the rules
def load_rules(path=DATA):
    """The json of drug_classes.json (read once per path)."""
    key = os.path.abspath(path)
    if key not in _RULES:
        with open(path, encoding="utf-8") as fh:
            _RULES[key] = json.load(fh)
    return _RULES[key]


def class_info(cls):
    """The json entry of class `cls` (label, effect, poison, targets, verb, why, source); {} when unknown."""
    return dict(load_rules()["classes"].get(cls) or {})


def class_order():
    """The class keys in json order."""
    return list(load_rules()["classes"])


def known_mechanism(text):
    """True when a ChEMBL mechanism text names a mechanism (not '' and not 'Unknown', UNKNOWN_MECHANISMS). Also takes
    a '; '-joined list (drug_annotations chembl_mechanisms): True when any of its texts does."""
    for t in str(text or "").split("; "):
        t = re.sub(r"\s*\([^)]*\)\s*$", "", t.strip())      # without a ' (species)' suffix
        if t and t.lower() not in UNKNOWN_MECHANISMS:
            return True
    return False


def molecule_key(name):
    """A compound's molecule, as the class constants are keyed: tlib.salt_base (a trailing bracketed salt removed),
    trailing salt and hydrate words removed (SALT_WORDS), Greek letters spelt out, upper case.
    'Doxorubicin (hydrochloride)' -> 'DOXORUBICIN'; 'Methylprednisolone succinate' -> 'METHYLPREDNISOLONE';
    'Betamethasone dipropionate' -> 'BETAMETHASONE DIPROPIONATE'; 'Docetaxel (Trihydrate)' -> 'DOCETAXEL'."""
    w = str(T.salt_base(name)).split()
    while len(w) > 1 and w[-1].lower().strip(",.") in SALT_WORDS:
        w.pop()
    s = " ".join(w)
    return "".join(GREEK.get(c, c) for c in s).upper()


def action_direction(action_type):
    """'up' (the drug raises its target's activity), 'down' (lowers it) or '' for a ChEMBL action type
    (drug_classes.json 'action_direction')."""
    a = str(action_type or "").strip().upper()
    ad = load_rules()["action_direction"]
    return "up" if a in ad["up"] else "down" if a in ad["down"] else ""


def _targets_text(t):
    return t if isinstance(t, str) else "; ".join(t or [])


def _targets_match(t, symbol):
    s = str(symbol or "").upper()
    if not s:
        return False
    if isinstance(t, str):
        return bool(t) and re.search(t, s) is not None
    return s in {str(x).upper() for x in (t or [])}


def trap_class(class_keys, symbol):
    """The 'trap' class among class_keys whose targets include symbol (a listed symbol, or the class's regular
    expression), else None. E.g. (['TOP2_POISON'], 'TOP2A') -> 'TOP2_POISON'."""
    for k in class_keys or ():
        info = class_info(k)
        if info.get("effect") == "trap" and _targets_match(info.get("targets"), symbol):
            return k
    return None


# ----------------------------------------------------------------------------- matching (ChEMBL)
def _choose(d, mols):
    """(parent ids, matched_by, note, identity_alert) of one drug's ChEMBL record d: the structure (PubChem id ->
    InChIKey) and the name rules (NAME_RULES order), combinations by the name of each part. When structure and name
    point to different molecules: two stereo forms of one compound -> the one named in ChEMBL; a loose name match ->
    the structure; else an 'Identity unsure' alert."""
    def par(i):
        return mols[i]["parent"] if i in mols else i

    def named(p):
        return bool(mols.get(p, {}).get("pref_name"))

    def first(hits):
        for h in sorted(hits, key=lambda h: (NAME_RULES.index(h.get("rule", "name")), h["field"] != "pref_name")):
            ps = sorted({par(i) for i in h["ids"]})
            if ps:
                return ps, h
        return [], None
    if d.get("parts"):
        ids = []
        for p in d["parts"]:
            ps, _h = first(p["hits"])
            ps = [x for x in ps if named(x)] or ps
            if len(ps) == 1:
                ids.append(ps[0])
        if ids and len(ids) == len(d["parts"]):
            return ids, "name of each part (a combination)", "", ""
    S = sorted({par(i) for i in d.get("structure_ids") or []})
    N, h = first(d.get("names") or [])
    nrule = f"{NAME_RULE_TEXT[h['rule']]} = a ChEMBL {h['field'].replace('_', ' ')}" if h else ""
    note = []
    for lab, X in (("structure", S), ("name", N)):
        if len(X) > 1:
            note.append(f"The {lab} matches {len(X)} ChEMBL molecules ({', '.join(X)}).")
    S = S if len(S) <= 1 else [p for p in S if named(p)][:1] if sum(map(named, S)) == 1 else []
    N = N if len(N) <= 1 else [p for p in N if named(p)][:1] if sum(map(named, N)) == 1 else []
    s, n = (S[0] if S else ""), (N[0] if N else "")
    if s and s == n:
        return [s], "structure and name", " ".join(note), ""
    if s and not n:
        return [s], "structure (PubChem id)", " ".join(note), ""
    if n and not s:
        return [n], f"name ({nrule})", " ".join(note), ""
    if not s:
        return [], "not found", " ".join(note), ""
    weak = h["rule"] in ("molecule_key", "cation_first") or h["field"] == "synonym"
    pick, other = (s, n) if named(s) and (weak or not named(n)) else (n, s)
    ks, kn = mols.get(s, {}).get("inchikey", ""), mols.get(n, {}).get("inchikey", "")
    stereo = bool(ks and kn and ks[:14] == kn[:14])
    pn = mols.get(pick, {}).get("pref_name") or "no name in ChEMBL"
    on = mols.get(other, {}).get("pref_name") or "no name in ChEMBL"
    how = ("structure (PubChem id)" if pick == s else f"name ({nrule})") + "; name and structure differ"
    if stereo:
        note.append(f"The name and the PubChem id point to two ChEMBL records of one compound in different stereo "
                    f"forms. Used {pick} ({pn}), not {other} ({on}).")
        return [pick], how, " ".join(note), ""
    if pick == s and named(s) and weak:
        note.append(f"Only a loose name match ({nrule}) points to {other} ({on}); the PubChem id points to {pick} "
                    f"({pn}), which is used.")
        return [pick], how, " ".join(note), ""
    return [pick], how + " (different compounds)", " ".join(note), (
        f"Identity unsure. The {'name' if pick == n else 'PubChem id'} points to {pick} ({pn}); the "
        f"{'PubChem id' if pick == n else 'name'} points to another compound, {other} ({on}). ChEMBL data shown "
        f"are for {pick}.")


def _rule_hits(rule, genes, action, text, tname, ttype, molnames, human):
    if not rule.get("any_species") and not human:
        return False
    if "genes_any" in rule and not genes & set(rule["genes_any"]):
        return False
    if "genes_regex" in rule and not any(re.search(rule["genes_regex"], g) for g in genes):
        return False
    if "actions" in rule and action not in rule["actions"]:
        return False
    if "target_name_regex" in rule and not re.search(rule["target_name_regex"], tname, re.I):
        return False
    if "text_regex" in rule and not re.search(rule["text_regex"], text.strip(), re.I):
        return False
    if "target_types" in rule and ttype not in rule["target_types"]:
        return False
    if "target_types_not" in rule and ttype in rule["target_types_not"]:
        return False
    if "exclude_regex" in rule and re.search(rule["exclude_regex"], f"{tname} {text}", re.I):
        return False
    return not set(rule.get("except_molecules", [])) & set(molnames)


def _short(xs, what="ChEMBL mechanism table"):
    xs = sorted(xs)
    if len(xs) <= SHORT_LIST:
        return ", ".join(xs)
    return ", ".join(xs[:SHORT_LIST]) + f" and {len(xs) - SHORT_LIST} more (all {len(xs)}: {what})"


def _tahoe_direction(fine, broad):
    s = (fine or "").lower()
    if re.search(r"\bagonist|activator|inducer", s) and "antagonist" not in s:
        return "up", fine
    if re.search(r"inhibitor|antagonist|blocker", s):
        return "down", fine
    b = (broad or "").lower()
    return ("up", broad) if "activator" in b else ("down", broad) if "inhibitor" in b else ("unclear", "")


def _split(s):
    return [x.strip().upper() for x in str(s or "").replace(";", ",").replace("|", ",").split(",")
            if x.strip() and x.strip().upper() not in ("NAN", "NONE", "NA", "-")]


def _release(snap):
    """'37' from ChEMBL's 'ChEMBL_37' (the release named in a ChEMBL source)."""
    r = str((snap or {}).get("chembl_release") or "").strip()
    return re.sub(r"^chembl[_ ]*", "", r, flags=re.I) or "release unknown"


def _drug_frame(drugs):
    d = pd.DataFrame(drugs).copy()
    for c in ("drug", "targets", "moa_fine", "moa_broad", "pubchem_cid", "tahoe_note"):
        d[c] = d[c].fillna("").astype(str) if c in d else ""
    d["drug"] = d["drug"].astype(str)
    return d[["drug", "targets", "moa_fine", "moa_broad", "pubchem_cid", "tahoe_note"]].reset_index(drop=True)


# ----------------------------------------------------------------------------- the classes
def assign_classes(drugs, snapshot=None, rules=None, hgnc=None):
    """(annotations, mechanisms, classes, stats) for the drugs (a table with drug, targets, moa_fine, moa_broad,
    pubchem_cid: Tahoe's metadata, verbatim) and the ChEMBL snapshot of the reference stage (None: ChEMBL not loaded,
    constant classes only). hgnc = the HGNC table (reference.read_hgnc), for UniProt accession -> approved symbol and
    the gene families of the 'Targets differ' alert (else ChEMBL's gene symbol, no family check)."""
    rules = rules or load_rules()
    up, down = set(rules["action_direction"]["up"]), set(rules["action_direction"]["down"])
    cls_info = rules["classes"]
    order = {k: i for i, k in enumerate(cls_info)}
    mrules = rules["mechanism_rules"]
    atc_rules = rules["atc_rules"]
    mol_cls = {k: v for k, v in rules["molecule_classes"].items() if not k.startswith("_")}
    notm = {c: {k: v for k, v in x.items() if not k.startswith("_")}
            for c, x in (rules.get("not_members") or {}).items() if not c.startswith("_") and isinstance(x, dict)}
    tahoe_cls = {k: set(v) for k, v in rules["tahoe_moa_classes"].items() if not k.startswith("_")}
    linked = rules["linked_targets"]
    acc2sym, groups = {}, {}
    if hgnc is not None:
        for sym, u, gg in zip(hgnc["symbol"], hgnc["uniprot_ids"], hgnc["gene_group"]):
            for acc in str(u or "").split("|"):
                if acc:
                    acc2sym.setdefault(acc, sym)
            if gg:
                groups[sym.upper()] = set(gg.split("|"))
    have = snapshot is not None
    snap = snapshot or {"drugs": [], "molecules": {}, "mechanisms": [], "targets": {}}
    rel = _release(snap)
    rec_of = {d["drug"]: d for d in snap.get("drugs") or []}
    mols, targets = snap.get("molecules") or {}, snap.get("targets") or {}
    by_parent = {}
    for m in snap.get("mechanisms") or []:
        by_parent.setdefault(m["parent"], []).append(m)

    def tinfo(tid):
        t = targets.get(tid) or {}
        gs = sorted({(acc2sym.get(c["accession"]) or c["gene_symbol"] or "").upper()
                     for c in t.get("components") or [] if c.get("type") == "PROTEIN"} - {""})
        return t, gs, t.get("organism") == "Homo sapiens"

    def constants(cls, key):
        mc = mol_cls.get(key)
        if mc:
            for k_ in mc["classes"]:
                cls.setdefault(k_, []).append(CONSTANT.format(mc["source"]))

    def not_member_notes(keys):
        out = []
        for c, xs in notm.items():
            for k_ in dict.fromkeys(keys):
                if k_ in xs:
                    out.append(f"Not counted as a {cls_info.get(c, {}).get('label', c)}: {xs[k_]} "
                               "(tahoemap/data/drug_classes.json, not_members).")
        return out

    def finish(drug, cls, mrow_start):
        """Tubulin: a stabiliser is not also counted as a destabiliser. Then one class row per class."""
        if STAB in cls and DESTAB in cls:
            dst = list(dict.fromkeys(cls.pop(DESTAB)))
            cls[STAB].append(f"not counted as a destabiliser: {cls[STAB][0]} (the destabiliser rules also matched: "
                             + " / ".join(dst) + ")")
            for mr in mrows[mrow_start:]:
                mr["classes"] = ", ".join(x for x in mr["classes"].split(", ") if x and x != DESTAB)
        rows = []
        for k_ in sorted(cls, key=lambda k: order.get(k, len(order))):
            ci = cls_info.get(k_, {})
            rows.append({"drug": drug, "class": k_, "label": ci.get("label", k_), "effect": ci.get("effect", "none"),
                         "poison": bool(ci.get("poison")), "targets": _targets_text(ci.get("targets")),
                         "verb": ci.get("verb", "") if ci.get("effect") == "trap" else "",
                         "source": "; ".join(dict.fromkeys(cls[k_]))})
        crows.extend(rows)
        return "; ".join(r["label"] for r in rows)

    drows, mrows, crows = [], [], []
    name_only = str(snap.get("structure_route", "")).startswith("PubChem not reached")   # reference.NAME_ONLY
    for r in _drug_frame(drugs).itertuples(index=False):
        T_ = set(_split(r.targets))
        d = rec_of.get(r.drug)
        row = {"drug": r.drug, "salt_base": T.salt_base(r.drug), "tahoe_targets": r.targets,
               "tahoe_moa_fine": r.moa_fine, "tahoe_moa_broad": r.moa_broad, "pubchem_cid": r.pubchem_cid,
               "inchikey": (d or {}).get("inchikey", ""), "chembl_id": "", "chembl_name": "",
               "chembl_max_phase": np.nan, "chembl_matched_by": "", "chembl_n_mechanisms": 0, "chembl_mechanisms": "",
               "chembl_actions": "", "chembl_targets": "", "chembl_atc": "", "mechanism_classes": "",
               "annotation_status": "", "annotation_alert": "", "annotation_note": ""}
        cls = {}
        mkey = molecule_key(r.drug)
        constants(cls, mkey)
        if d is None:
            notes = ["ChEMBL was not loaded for this drug in this run " +
                     ("(offline, and the cache does not hold it)." if have else
                      "(offline and not cached, or the download failed: reference/sources.json)."),
                     *not_member_notes([mkey])] + ([r.tahoe_note + "."] if r.tahoe_note else [])
            row.update(annotation_status=NOT_LOADED, annotation_note=" | ".join(notes),
                       mechanism_classes=finish(r.drug, cls, len(mrows)))
            drows.append(row)
            continue
        pids, how, note, idalert = _choose(d, mols)
        pms = [mols.get(p, {}) for p in pids]
        molnames = [(p.get("pref_name") or "").upper() for p in pms]
        ms = sorted((m for p in pids for m in by_parent.get(p, [])), key=lambda m: (m["mechanism_of_action"],
                                                                                   m["target"]))
        m0 = len(mrows)
        known = [m for m in ms if known_mechanism(m["mechanism_of_action"])]   # 'Unknown' is no mechanism
        C, texts, on_t = set(), [], []
        for m in ms:
            t, gs, human = tinfo(m["target"])
            g = set(gs)
            if human:
                C |= g
            tn, tt = t.get("pref_name", ""), t.get("type", "")
            org = "" if not t or human else f" ({t.get('organism') or 'species not given'})"
            txt = m["mechanism_of_action"] + org
            texts.append(txt)
            a = m["action_type"]
            dr = "up" if a in up else "down" if a in down else ""
            hit = [x["class"] for x in mrules if _rule_hits(x, g, a, m["mechanism_of_action"], tn, tt, molnames, human)]
            if STAB in hit:                     # a mechanism that stabilises tubulin is not also a destabiliser
                hit = [x for x in hit if x != DESTAB]
            for k_ in dict.fromkeys(hit):
                cls.setdefault(k_, []).append(f"ChEMBL {rel}: {m['mechanism_of_action']} ({m['parent']})")
            on_t.append((g if human else set(), dr, txt))
            mrows.append({"drug": r.drug, "chembl_id": m["parent"], "mechanism_of_action": m["mechanism_of_action"],
                          "action_type": a, "direction": {"up": "activates", "down": "inhibits"}.get(dr, ""),
                          "target_chembl_id": m["target"], "target_name": tn, "target_type": tt,
                          "target_organism": t.get("organism", ""), "target_genes": ", ".join(gs),
                          "n_target_genes": len(gs), "binding_site": m["binding_site_comment"],
                          "direct_interaction": m["direct_interaction"], "classes": ", ".join(dict.fromkeys(hit)),
                          "refs": "; ".join(m["refs"])})
        for pm in pms:
            for code in pm.get("atc") or []:
                for x in atc_rules:
                    if code.startswith(x["prefix"]):
                        for k_ in x["classes"]:
                            cls.setdefault(k_, []).append(f"WHO ATC {code} (via ChEMBL)")
        ckeys = [molecule_key(p.get("pref_name") or "") for p in pms if p.get("pref_name")]
        for k_ in dict.fromkeys(ckeys):
            if k_ != mkey:
                constants(cls, k_)
        alerts, notes, status = [], [], []
        if idalert:
            status.append("identity unsure")
            alerts.append(idalert)
        if not pids:
            status.append("not found in ChEMBL")
            notes.append(f"Not found in ChEMBL by structure (PubChem id {r.pubchem_cid or 'not given'}) or by name.")
        elif not ms:
            status.append("no ChEMBL mechanism")
            notes.append(f"ChEMBL has this molecule ({' + '.join(pids)}) but no curated mechanism for it.")
        elif not known:
            status.append(NO_MECH_UNKNOWN)
            notes.append(f"ChEMBL has this molecule ({' + '.join(pids)}) and records its mechanism as 'Unknown': no "
                         "mechanism is known to ChEMBL.")
        link = [x for x in linked if C & set(x["chembl"]) and T_ & set(x["tahoe"])]
        if T_ and C and not T_ & C:
            fam = sorted(set().union(*(groups.get(x, set()) for x in T_)) & set().union(*(groups.get(x, set())
                                                                                          for x in C)))
            if link:
                status.append("targets linked")
                notes.append(f"The sources name different proteins that work together. Tahoe: {_short(T_)}. ChEMBL: "
                             f"{_short(C)}. {link[0]['why']} ({link[0]['source']}).")
            else:
                status.append("targets differ" + (", same family" if fam else ""))
                alerts.append("Targets differ" + (f" within one gene family ({fam[0]})" if fam else "") +
                              f". Tahoe lists {_short(T_)}. ChEMBL's mechanism names {_short(C)}.")
        elif T_ and C and T_ < C:
            status.append("ChEMBL lists more targets")
            notes.append(f"Tahoe lists {_short(T_)}. ChEMBL's mechanism covers {len(C)} genes: {_short(C)}.")
        elif T_ and C and not T_ <= C:
            status.append("targets overlap")
            notes.append(f"Both list {_short(T_ & C)}. Only Tahoe lists {_short(T_ - C)}." +
                         (f" Only ChEMBL lists {_short(C - T_)}." if C - T_ else ""))
        elif not T_ and C:
            status.append("only ChEMBL lists targets")
        tc = tahoe_cls.get(r.moa_fine)
        if tc is not None and known and not tc & set(cls):
            status.append("mechanism differs")
            alerts.append(f"Mechanism differs. Tahoe: {r.moa_fine}. ChEMBL: " + "; ".join(dict.fromkeys(texts)) + ".")
        if r.moa_fine.strip().lower() in ("", "unclear") and known:
            status.append("only ChEMBL gives a mechanism")
            notes.append(f"Tahoe's mechanism is '{r.moa_fine or 'not given'}'. ChEMBL: "
                         + "; ".join(dict.fromkeys(texts)) + ".")
        td, tsrc = _tahoe_direction(r.moa_fine, r.moa_broad)
        on = [x for x in on_t if x[1] and (not T_ & C or x[0] & T_)]
        if td in ("up", "down") and len({x[1] for x in on}) == 1 and on[0][1] != td and not link:
            status.append("action differs")
            alerts.append(f"Action differs. Tahoe: {tsrc}. ChEMBL: " + "; ".join(dict.fromkeys(x[2] for x in on))
                          + ".")
        if not status and known:
            status.append("agree")
        if note:
            notes.append(note)
        if r.tahoe_note:                         # Tahoe's annotation from drugdose.csv (no metadata file or PubChem id)
            notes.append(r.tahoe_note + ".")
        elif name_only and r.pubchem_cid:        # the snapshot was made without PubChem
            notes.append("PubChem was not reached when ChEMBL was fetched: this drug was matched by name only, "
                          "without the structure (InChIKey) check.")
        notes.extend(not_member_notes([mkey] + ckeys))
        row.update(chembl_id=" + ".join(pids), chembl_name=" + ".join(p.get("pref_name", "") for p in pms),
                   chembl_max_phase=max([float(p["max_phase"]) for p in pms if p.get("max_phase") is not None],
                                        default=np.nan),
                   chembl_matched_by=how, chembl_n_mechanisms=len(ms),
                   chembl_mechanisms="; ".join(dict.fromkeys(texts)),
                   chembl_actions=", ".join(sorted({m["action_type"] for m in ms if m["action_type"]})),
                   chembl_targets=", ".join(sorted(C)),
                   chembl_atc=", ".join(c for p in pms for c in p.get("atc") or []),
                   mechanism_classes=finish(r.drug, cls, m0), annotation_status="; ".join(status),
                   annotation_alert=" | ".join(alerts), annotation_note=" | ".join(notes))
        drows.append(row)
    D = pd.DataFrame(drows, columns=DRUG_COLUMNS)
    M = pd.DataFrame(mrows, columns=MECH_COLUMNS)
    K = pd.DataFrame(crows, columns=CLASS_COLUMNS)
    D["chembl_max_phase"] = D["chembl_max_phase"].astype(np.float64)
    D["chembl_n_mechanisms"] = D["chembl_n_mechanisms"].astype(np.int32)
    M["n_target_genes"] = M["n_target_genes"].astype(np.int32)
    M["direct_interaction"] = pd.to_numeric(M["direct_interaction"], errors="coerce").astype("Int8")
    K["poison"] = K["poison"].astype(bool)
    for X, cols in ((D, DRUG_COLUMNS), (M, MECH_COLUMNS), (K, CLASS_COLUMNS)):
        for c in cols:
            if X[c].dtype == object:
                X[c] = X[c].fillna("").astype(str)
    st = {"drugs": int(len(D)), "chembl_matched": int((D["chembl_id"] != "").sum()),
          "chembl_with_mechanism": int(sum(known_mechanism(x) for x in D["chembl_mechanisms"])),
          "annotation_alerts": int((D["annotation_alert"] != "").sum()),
          "annotation_status": {k: int(v) for k, v in
                                D["annotation_status"].str.split("; ").explode().value_counts().items() if k},
          "mechanism_classes": {k: int(v) for k, v in K["class"].value_counts().items()}}
    return D, M, K, st


# ----------------------------------------------------------------------------- readers
def _tables(out):
    """(annotations, mechanisms, classes) of an output: reference/'s files when all three exist, else the
    constant-only result for the drugs of atlas/effects/drugdose.csv (cached per output and file state)."""
    rd = os.path.join(out, "reference")
    paths = [os.path.join(rd, FILES[k]) for k in ("annotations", "mechanisms", "classes")]

    def stamp(p):
        try:
            return os.stat(p).st_mtime_ns
        except OSError:
            return None
    key = (os.path.abspath(out), tuple(stamp(p) for p in paths))
    if key in _TABLES:
        return _TABLES[key]
    if all(k is not None for k in key[1]):
        res = tuple(pd.read_parquet(p) for p in paths)
    else:
        drugs = pd.DataFrame(columns=["drug", "targets", "moa_fine", "moa_broad", "pubchem_cid"])
        if os.path.exists(os.path.join(out, "atlas", "effects", "drugdose.csv")):
            from .reference import tahoe_drugs                  # reference imports this module
            drugs = tahoe_drugs(out)
        res = assign_classes(drugs, None)[:3]
    for k in [k for k in _TABLES if k[0] == key[0]]:
        del _TABLES[k]
    _TABLES[key] = res
    return res


def drug_annotations(out):
    """reference/drug_annotations.parquet (DRUG_COLUMNS), or the constant-only result (no ChEMBL)."""
    return _tables(out)[0]


def drug_mechanisms(out):
    """reference/drug_mechanisms.parquet (MECH_COLUMNS); no rows without ChEMBL."""
    return _tables(out)[1]


def drug_classes(out):
    """reference/drug_classes.parquet (CLASS_COLUMNS), or the constant-only result (no ChEMBL)."""
    return _tables(out)[2]


def members(out, cls):
    """The Tahoe drug names in class cls, sorted."""
    K = drug_classes(out)
    return sorted(set(K.loc[K["class"] == cls, "drug"].astype(str)))


def classes_by_drug(out):
    """{drug: [class keys in json order]} for every drug of the annotations ([] when it is in no class)."""
    order = {k: i for i, k in enumerate(class_order())}
    res = {str(d): [] for d in drug_annotations(out)["drug"]}
    K = drug_classes(out)
    for d, c in zip(K["drug"].astype(str), K["class"].astype(str)):
        res.setdefault(d, []).append(c)
    return {d: sorted(dict.fromkeys(v), key=lambda k: order.get(k, len(order))) for d, v in res.items()}


def class_text(out, drug):
    """'{label} ({sources})' of each class of the drug, '; '-joined in json order; '' when it is in none."""
    K = drug_classes(out)
    k = K[K["drug"].astype(str) == str(drug)]
    if not len(k):
        return ""
    order = {c: i for i, c in enumerate(class_order())}
    k = k.assign(_o=k["class"].map(lambda c: order.get(c, len(order)))).sort_values("_o", kind="stable")
    return "; ".join(f"{lab} ({src})" for lab, src in zip(k["label"], k["source"]))
