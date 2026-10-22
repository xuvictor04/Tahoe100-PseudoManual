#!/usr/bin/env python3
"""Database / full-text checks behind the MG53 (TRIM72) evidence map.

Answers, with public resources, the questions that a PubMed abstract screen cannot:
  1. Is TRIM72 a p53 target gene?
       a) Fischer 2017 (Oncogene, PMID 28288132) census: Table S1 (literature-curated p53 targets),
          Table S2 (3,661 genes called direct p53 targets in >=1 of 16 genome-wide data sets),
          Table S3 (high-confidence list).            -> fischer2017_p53_census_check.csv
       b) ChIP-Atlas (hg38) TP53 ChIP-seq peaks within +-5 kb and +-10 kb of each TSS,
          all public TP53 ChIP-seq experiments.        -> chipatlas_tp53_binding_check.csv
  2. Where is TRIM72 mRNA expressed in normal human tissue? (Human Protein Atlas consensus nTPM)
                                                        -> hpa_trim72_tissue_rna.csv
  3. Europe PMC searches (title/abstract incl. preprints, and full text) -> europepmc_queries.csv
  4. Do the TRIM-p53 reviews mention TRIM72?  Which TRIMs do they list?  What does the
     2025 review on E3 ligases in doxorubicin cardiotoxicity say about TRIM72 (full text of
     Jiang 2024 is paywalled)?                          -> trim_p53_reviews_check.csv,
                                                           tachibana2025_trim72_excerpt.txt
  5. Do open-access MG53-in-cancer papers report any p53 / MDM2 / p21 data?
                                                        -> cancer_fulltext_p53_check.csv

Downloads go to ./downloads/<source>/ (data only; xlsx/tsv/xml are parsed, never executed).
Run:  python3 external_checks.py      (needs internet; ~2 min; pandas + openpyxl)
Public resources change over time (ChIP-Atlas adds experiments); the run date is written
to external_checks_run_info.txt.
"""
import csv
import datetime
import json
import os
import re
import time
import urllib.parse
import urllib.request

import pandas as pd

OUT = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(OUT, "downloads")
UA = {"User-Agent": "Mozilla/5.0 (tahoe-mg53-literature-check)"}

REF_GENES = ["TRIM72", "CDKN1A", "MDM2", "BBC3", "PMAIP1", "ATF3", "TRIM22", "TRIM32", "TRIM24", "PML",
             "TRIM8", "TRIM3", "TRIM67", "TRIML2", "TRIM65", "TRIM59", "TRIM39", "TRIM29", "TRIM25",
             "TRIM28", "GAPDH", "ACTB"]


def fetch(url, dest=None, tries=4, data=None):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA, data=data)
            with urllib.request.urlopen(req, timeout=120) as r:
                b = r.read()
            if dest:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(b)
            return b
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(3 + 5 * i)


# ---------------------------------------------------------------- 1a Fischer 2017
def fischer():
    base = ("https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fonc.2016.502/"
            "MediaObjects/41388_2017_BFonc2016502_MOESM{}_ESM.xlsx")
    d = os.path.join(DL, "fischer2017")
    files = {}
    for n, name in [(5, "S1"), (6, "S2"), (7, "S3")]:
        p = os.path.join(d, f"TableS{name[-1]}_MOESM{n}.xlsx")
        if not os.path.exists(p):
            fetch(base.format(n), p)
        files[name] = p
    s1 = pd.read_excel(files["S1"], header=0)
    s2 = pd.read_excel(files["S2"], header=0)
    s3 = pd.read_excel(files["S3"], header=0)
    sym1 = set(s1["Gene Symbol"].dropna().astype(str))
    sym3 = set(s3["Gene Symbol"].dropna().astype(str))
    s2 = s2.set_index(s2["Gene Symbol"].astype(str))
    rows = []
    for g in REF_GENES:
        r = dict(gene=g, in_tableS1_literature=g in sym1, in_tableS2_genomewide=g in s2.index,
                 in_tableS3_high_confidence=g in sym3, n_tableS1_genes=len(sym1), n_tableS2_genes=len(s2),
                 n_tableS3_genes=len(sym3))
        if g in s2.index:
            x = s2.loc[[g]].iloc[0]
            r["S2_sum_direct_target_0to16"] = x["sum direct target (0..16)"]
            r["S2_sum_direct_regulation_-16to16"] = x["sum direct regulation score (-16..0..16)"]
            r["S2_p53_ChIP_5kb_sum_0to15"] = x["p53 ChIP 5kb sum (0..15)"]
            r["S2_p53_expression_score_-20to20"] = x["p53 Expression Score (-20..0..20)"]
        rows.append(r)
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "fischer2017_p53_census_check.csv"), index=False)
    print("Fischer 2017: TRIM72 in S1/S2/S3:", rows[0]["in_tableS1_literature"], rows[0]["in_tableS2_genomewide"],
          rows[0]["in_tableS3_high_confidence"])


# ---------------------------------------------------------------- 1b ChIP-Atlas
def chipatlas():
    d = os.path.join(DL, "chipatlas")
    rows = []
    for win in [5, 10]:
        p = os.path.join(d, f"TP53.{win}.tsv")
        if not os.path.exists(p):
            fetch(f"https://chip-atlas.dbcls.jp/data/hg38/target/TP53.{win}.tsv", p)
        df = pd.read_csv(p, sep="\t", index_col=0)
        avg = df.iloc[:, 0]
        X = df.iloc[:, 1:]
        nb = (X > 0).sum(axis=1)
        rank = avg.rank(ascending=False, method="average")
        for g in REF_GENES:
            if g in df.index:
                bound = X.columns[(X.loc[g] > 0).values]
                rows.append(dict(window_kb=win, gene=g, listed=True, avg_score=round(float(avg[g]), 3),
                                 n_experiments_bound=int(nb[g]), n_experiments_total=X.shape[1],
                                 rank_by_avg=float(rank[g]), n_genes_listed=len(df),
                                 bound_experiments=";".join(bound) if len(bound) <= 12 else f"{len(bound)} experiments"))
            else:
                rows.append(dict(window_kb=win, gene=g, listed=False, avg_score=0, n_experiments_bound=0,
                                 n_experiments_total=X.shape[1], rank_by_avg=None, n_genes_listed=len(df),
                                 bound_experiments=""))
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "chipatlas_tp53_binding_check.csv"), index=False)
    t = [r for r in rows if r["gene"] == "TRIM72"]
    print("ChIP-Atlas TRIM72:", [(r["window_kb"], r["n_experiments_bound"], r["n_experiments_total"]) for r in t])


# ---------------------------------------------------------------- 2 HPA
def hpa():
    tissues = ["skeletal_muscle", "tongue", "heart_muscle", "lung", "kidney", "liver", "colon", "pancreas",
               "stomach", "breast", "skin", "brain"]
    cols = "g,eg," + ",".join(f"t_RNA_{t}" for t in tissues)
    url = ("https://www.proteinatlas.org/api/search_download.php?search=TRIM72&format=json&columns="
           + cols + "&compress=no")
    p = os.path.join(DL, "hpa", "hpa_trim72_tissue.json")
    b = fetch(url, p)
    js = [r for r in json.loads(b) if r.get("Gene") == "TRIM72"]
    rows = []
    for k, v in js[0].items():
        m = re.match(r"Tissue RNA - (.+) \[nTPM\]", k)
        if m:
            rows.append(dict(tissue=m.group(1), nTPM=float(v), source="Human Protein Atlas consensus", url=url))
    pd.DataFrame(rows).sort_values("nTPM", ascending=False).to_csv(
        os.path.join(OUT, "hpa_trim72_tissue_rna.csv"), index=False)
    print("HPA:", {r["tissue"]: r["nTPM"] for r in rows})


# ---------------------------------------------------------------- 3 Europe PMC
EPMC_QUERIES = {
    "title/abstract (incl. preprints): TRIM72/MG53 AND p53":
        '(TITLE_ABS:TRIM72 OR TITLE_ABS:MG53 OR TITLE_ABS:"mitsugumin 53" OR TITLE_ABS:"mitsugumin-53") '
        'AND (TITLE_ABS:p53 OR TITLE_ABS:TP53)',
    "title/abstract (incl. preprints): TRIM72/MG53 AND (MDM2 OR DNA damage OR genotoxic)":
        '(TITLE_ABS:TRIM72 OR TITLE_ABS:MG53 OR TITLE_ABS:"mitsugumin 53") AND '
        '(TITLE_ABS:MDM2 OR TITLE_ABS:"DNA damage" OR TITLE_ABS:genotoxic)',
    "title/abstract (incl. preprints): TRIM72/MG53 AND anthracyclines":
        '(TITLE_ABS:TRIM72 OR TITLE_ABS:MG53) AND (doxorubicin OR anthracycline OR daunorubicin OR epirubicin OR idarubicin)',
    "full text: TRIM72/MG53 AND MDM2 (any position)":
        '(TRIM72 OR MG53 OR "mitsugumin 53") AND (MDM2 OR HDM2)',
    "full text: TRIM72 AND 'p53 target'": '"TRIM72" AND "p53 target"',
}


def europepmc():
    rows = []
    for name, q in EPMC_QUERIES.items():
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
            dict(query=q, format="json", pageSize=100, resultType="lite"))
        js = json.loads(fetch(url))
        res = js["resultList"]["result"]
        rows.append(dict(query_name=name, n_hits=js["hitCount"],
                         ids=";".join(str(r.get("pmid") or r.get("id")) for r in res),
                         titles=" || ".join(r.get("title", "")[:110] for r in res[:15]), query=q))
        time.sleep(0.5)
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "europepmc_queries.csv"), index=False)
    print("Europe PMC:", [(r["query_name"][:50], r["n_hits"]) for r in rows])


def epmc_fulltext(pmcid):
    p = os.path.join(DL, "pmc_fulltext", f"{pmcid}.xml")
    if not os.path.exists(p):
        fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML", p)
        time.sleep(0.4)
    t = open(p, encoding="utf-8", errors="replace").read()
    body = re.sub(r"<ref-list.*?</ref-list>", " ", t, flags=re.S)  # drop the reference list
    clean = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))
    return clean(t), clean(body)


# ---------------------------------------------------------------- 4 TRIM-p53 reviews
REVIEWS = {"PMC8209353": "Liu J et al. 2021 Genes Dis 'Tumor suppressor p53 cross-talks with TRIM family proteins' (PMID 34179310)",
           "PMC6479553": "Valletti A et al. 2019 Int J Mol Sci 'Targeting chemoresistant tumors: could TRIM proteins-p53 axis be a possible answer?' (PMID 30974870)",
           "PMC12608693": "Tachibana S et al. 2025 Int J Mol Sci 'Ubiquitin E3 ligases and p53 in doxorubicin-induced cardiotoxicity' (PMID 41226293)"}


def reviews():
    rows = []
    for pmcid, label in REVIEWS.items():
        full, body = epmc_fulltext(pmcid)
        trims = sorted(set(re.findall(r"\bTRIM\d+\b", body)), key=lambda s: int(s[4:]))
        rows.append(dict(pmcid=pmcid, review=label, n_chars_body=len(body),
                         mentions_TRIM72=bool(re.search(r"TRIM\s?72", body)), mentions_MG53=("MG53" in body),
                         TRIM_genes_mentioned=";".join(trims)))
        if pmcid == "PMC12608693":
            i = body.find("3.4. TRIM72")
            j = body.find("3.5.", i)
            with open(os.path.join(OUT, "tachibana2025_trim72_excerpt.txt"), "w") as f:
                f.write(label + "\nSection 3.4 (verbatim from Europe PMC full text):\n\n")
                f.write(body[i:j].strip() if i >= 0 and j > i else "SECTION NOT FOUND")
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "trim_p53_reviews_check.csv"), index=False)
    print("Reviews:", [(r["pmcid"], r["mentions_TRIM72"], r["mentions_MG53"]) for r in rows])


# ---------------------------------------------------------------- 5 cancer papers, p53 data?
CANCER_OA = {"PMC10326024": "Fang 2023 cyclin D1 (PMID 37414783)", "PMC8439062": "Li H 2021 G3BP2 NSCLC (PMID 34521423)",
             "PMC9300626": "Ma X 2022 RAC1 HCC (PMID 35858925)", "PMC9461659": "Gupta P 2022 colorectal (PMID 36147477)",
             "PMC11416540": "Wang XL 2024 KIF11 PDAC (PMID 39265509)", "PMC11417184": "Faleti 2024 FAK CRC (PMID 39315132)",
             "PMC8997701": "Wang Z 2022 breast PPP3CA (PMID 35324524)"}


def cancer_p53():
    rows = []
    pat = r"\bp53\b|\bTP53\b|\bTrp53\b|\bMDM2\b|\bMdm2\b|\bp21\b|\bCDKN1A\b"
    for pmcid, label in CANCER_OA.items():
        full, body = epmc_fulltext(pmcid)
        ctx = [body[max(0, m.start() - 120):m.end() + 80] for m in re.finditer(pat, body)][:3]
        rows.append(dict(pmcid=pmcid, paper=label, n_mentions_body=len(re.findall(pat, body)),
                         n_mentions_incl_references=len(re.findall(pat, full)), n_chars_body=len(body),
                         contexts_in_body=" || ".join(ctx)))
    pd.DataFrame(rows).to_csv(os.path.join(OUT, "cancer_fulltext_p53_check.csv"), index=False)
    print("Cancer full texts p53/MDM2/p21 mentions (body):", [(r["pmcid"], r["n_mentions_body"]) for r in rows])


def main():
    fischer()
    chipatlas()
    hpa()
    europepmc()
    reviews()
    cancer_p53()
    with open(os.path.join(OUT, "external_checks_run_info.txt"), "w") as f:
        f.write(f"run_date\t{datetime.date.today().isoformat()}\n")


if __name__ == "__main__":
    main()
