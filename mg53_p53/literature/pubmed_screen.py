#!/usr/bin/env python3
"""Reproducible PubMed screen for MG53/TRIM72 literature.

1. Retrieves every PubMed record whose title/abstract mentions TRIM72 / MG53 / mitsugumin 53
   (NCBI E-utilities, no API key needed; ~3 requests/s max).
2. Saves them to pubmed_trim72_records.csv (pmid, year, journal, first author, title, doi, abstract).
3. Screens title+abstract with keyword groups relevant to the evidence map and writes
   pubmed_keyword_hits.csv (one row per record x keyword group) and pubmed_keyword_counts.csv.
4. Runs a few targeted co-occurrence queries directly in PubMed (counts + PMIDs) and writes
   pubmed_targeted_queries.csv, so "searched and found nothing" statements are recomputable.

Run:  python3 pubmed_screen.py            (writes into the folder of this script)
Results depend on the date of the run (PubMed grows); the date is written to pubmed_run_info.txt.
"""
import csv
import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OUT = os.environ.get("MG53_OUT") or os.path.dirname(os.path.abspath(__file__))   # run_mg53_p53.py sets MG53_OUT
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
TOOL = "tahoe_mg53_literature_screen"

MAIN_QUERY = ('(TRIM72[tiab] OR MG53[tiab] OR "mitsugumin 53"[tiab] OR "mitsugumin-53"[tiab] '
              'OR mitsugumin53[tiab] OR "tripartite motif containing 72"[tiab] '
              'OR "tripartite motif-containing 72"[tiab] OR "tripartite motif protein 72"[tiab])')

# keyword groups screened in title+abstract (case-insensitive regex)
KEYWORDS = {
    "p53": r"\bp53\b|\btp53\b|trp53",
    "MDM2": r"\bmdm2\b|\bhdm2\b",
    "apoptosis": r"apoptos|apoptot",
    "anthracycline": r"doxorubicin|adriamycin|anthracyclin|epirubicin|idarubicin|daunorubicin|daunomycin",
    "DNA_damage": r"dna damage|genotoxic|double[- ]strand break|\bγ-?h2ax\b|gamma-?h2ax|\batm\b|\batr\b",
    "cancer": r"cancer|tumou?r|carcinoma|neoplas|malignan|oncogen|metasta",
    "promoter_TF": r"promoter|transcription factor|myod|mef2|myogenin|\bmyf5\b|enhancer|e-box|transcriptional regulation",
    "expression_regulation": r"upregulat|downregulat|up-regulat|down-regulat|induc(e|ed|es|tion) .{0,40}(mg53|trim72)",
    "glucocorticoid": r"glucocorticoid|dexamethasone|cortisol|corticosterone",
    "insulin_IRS1": r"\birs-?1\b|insulin receptor substrate|insulin resistance",
    "FAK": r"\bfak\b|focal adhesion kinase|\bptk2\b",
    "RISK_PI3K_AKT": r"\bpi3k\b|\bakt\b|\bgsk3|\berk1/2|\brisk\b pathway|reperfusion injury salvage kinase",
    "NFkB": r"nf-?κb|nf-?kappa ?b|nfkb|\bikk|\bikba",
    "oxidation_oligomer": r"oligomer|disulfide|cys242|c242|cysteine 242|redox|oxidi[sz]",
    "secretion_serum": r"secret|serum mg53|circulating|myokine|cardiokine|recombinant human mg53|rhmg53",
    "ubiquitination": r"ubiquitin|e3 ligase|proteasom|degradation",
    "ischemia": r"ischemi|ischaemi|reperfusion|infarct",
    "cardiotoxicity": r"cardiotoxic|cardiomyopathy",
    "ferroptosis": r"ferroptos",
    "SUMO_ZNF": r"sumo|\bznf\b|zinc finger",
}

# targeted PubMed queries (count + first PMIDs)
TARGETED = {
    "TRIM72/MG53 AND p53": MAIN_QUERY + ' AND (p53[tiab] OR TP53[tiab] OR "tumor protein p53"[tiab] OR Trp53[tiab])',
    "TRIM72/MG53 AND p53 (all fields incl. MeSH)": MAIN_QUERY + ' AND (p53 OR TP53 OR "Tumor Suppressor Protein p53"[MeSH])',
    "TRIM72/MG53 AND MDM2": MAIN_QUERY + ' AND (MDM2[tiab] OR HDM2[tiab])',
    "TRIM72/MG53 AND anthracycline": MAIN_QUERY + ' AND (doxorubicin[tiab] OR adriamycin[tiab] OR anthracycline*[tiab] OR epirubicin[tiab] OR idarubicin[tiab] OR daunorubicin[tiab])',
    "TRIM72/MG53 AND idarubicin": MAIN_QUERY + ' AND (idarubicin[tiab])',
    "TRIM72/MG53 AND cancer": MAIN_QUERY + ' AND (cancer[tiab] OR tumor[tiab] OR tumour[tiab] OR carcinoma[tiab] OR neoplasm*[tiab])',
    "TRIM72/MG53 AND promoter/transcription": MAIN_QUERY + ' AND (promoter[tiab] OR MyoD[tiab] OR MEF2*[tiab] OR "transcription factor"[tiab] OR "transcriptional regulation"[tiab])',
    "TRIM72/MG53 AND glucocorticoid": MAIN_QUERY + ' AND (glucocorticoid*[tiab] OR dexamethasone[tiab])',
    "TRIM72/MG53 AND DNA damage": MAIN_QUERY + ' AND ("DNA damage"[tiab] OR genotoxic[tiab] OR ATM[tiab])',
    "TRIM72/MG53 AND apoptosis": MAIN_QUERY + ' AND (apoptosis[tiab] OR apoptotic[tiab])',
    "TRIM72/MG53 AND ferroptosis": MAIN_QUERY + ' AND (ferroptosis[tiab])',
    "TRIM72/MG53 AND NF-kB": MAIN_QUERY + ' AND ("NF-kB"[tiab] OR "NF-kappaB"[tiab] OR NFkB[tiab] OR "nuclear factor kappa"[tiab] OR "NF-κB"[tiab])',
    "TRIM72/MG53 AND homoharringtonine/omacetaxine": MAIN_QUERY + ' AND (homoharringtonine[tiab] OR omacetaxine[tiab])',
    "TRIM72/MG53 AND auranofin/thioredoxin": MAIN_QUERY + ' AND (auranofin[tiab] OR thioredoxin[tiab])',
    "TRIM72/MG53 AND CDK inhibitor/dinaciclib": MAIN_QUERY + ' AND (dinaciclib[tiab] OR "CDK9"[tiab] OR "transcriptional CDK"[tiab])',
    "TRIM72/MG53 AND topoisomerase": MAIN_QUERY + ' AND (topoisomerase[tiab] OR topotecan[tiab] OR camptothecin[tiab] OR etoposide[tiab])',
    "TRIM72/MG53 AND ATF3/ISR": MAIN_QUERY + ' AND (ATF3[tiab] OR ATF4[tiab] OR "integrated stress response"[tiab] OR CHOP[tiab] OR "ER stress"[tiab])',
    "TRIM72/MG53 AND hypoxia/HIF": MAIN_QUERY + ' AND (HIF-1*[tiab] OR hypoxia[tiab])',
    "TRIM72/MG53 AND microRNA": MAIN_QUERY + ' AND (microRNA*[tiab] OR miRNA*[tiab] OR "miR-"[tiab])',
    "p53 target gene screens mentioning TRIM72 (all fields)": '(TRIM72 OR MG53) AND ("p53 target" OR "p53-target" OR "p53 binding site" OR "p53 response element")',
}


def get(url, params, tries=4):
    params = dict(params, tool=TOOL)
    data = urllib.parse.urlencode(params).encode()
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=60) as r:
                return r.read()
        except Exception as e:  # network hiccup: back off and retry
            if i == tries - 1:
                raise
            time.sleep(2 + 3 * i)
    return b""


def esearch(term, retmax=100000):
    raw = get(EU + "esearch.fcgi", {"db": "pubmed", "term": term, "retmax": retmax, "retmode": "json"})
    time.sleep(0.4)
    js = json.loads(raw)["esearchresult"]
    return int(js["count"]), js.get("idlist", [])


def text_of(el):
    return "".join(el.itertext()).strip() if el is not None else ""


def efetch(pmids):
    recs = []
    for i in range(0, len(pmids), 150):
        chunk = pmids[i:i + 150]
        raw = get(EU + "efetch.fcgi", {"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"})
        time.sleep(0.4)
        root = ET.fromstring(raw)
        for art in root.findall(".//PubmedArticle"):
            mc = art.find("MedlineCitation")
            pmid = text_of(mc.find("PMID"))
            a = mc.find("Article")
            title = text_of(a.find("ArticleTitle"))
            abst = " ".join(text_of(x) for x in a.findall("Abstract/AbstractText"))
            journal = text_of(a.find("Journal/ISOAbbreviation")) or text_of(a.find("Journal/Title"))
            year = text_of(a.find("Journal/JournalIssue/PubDate/Year"))
            if not year:
                md = text_of(a.find("Journal/JournalIssue/PubDate/MedlineDate"))
                m = re.search(r"(19|20)\d\d", md)
                year = m.group(0) if m else ""
            au = a.find("AuthorList/Author")
            first = ""
            if au is not None:
                first = (text_of(au.find("LastName")) + " " + text_of(au.find("Initials"))).strip() or text_of(au.find("CollectiveName"))
            n_auth = len(a.findall("AuthorList/Author"))
            doi = ""
            for aid in art.findall("PubmedData/ArticleIdList/ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = text_of(aid)
            ptypes = ";".join(text_of(p) for p in a.findall("PublicationTypeList/PublicationType"))
            recs.append(dict(pmid=pmid, year=year, journal=journal, first_author=first, n_authors=n_auth,
                             title=title, doi=doi, pub_types=ptypes, abstract=abst))
    return recs


def main():
    run_date = datetime.date.today().isoformat()
    n, ids = esearch(MAIN_QUERY)
    print(f"main query: {n} records", file=sys.stderr)
    recs = efetch(ids)
    recs.sort(key=lambda r: (r["year"], r["pmid"]))
    cols = ["pmid", "year", "journal", "first_author", "n_authors", "title", "doi", "pub_types", "abstract"]
    with open(os.path.join(OUT, "pubmed_trim72_records.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(recs)

    hits, counts = [], {}
    for r in recs:
        txt = (r["title"] + " " + r["abstract"]).lower()
        for k, pat in KEYWORDS.items():
            m = re.search(pat, txt)
            if m:
                counts[k] = counts.get(k, 0) + 1
                s = max(0, m.start() - 160)
                hits.append(dict(keyword=k, pmid=r["pmid"], year=r["year"], first_author=r["first_author"],
                                 journal=r["journal"], title=r["title"],
                                 context=re.sub(r"\s+", " ", txt[s:m.end() + 160])))
    with open(os.path.join(OUT, "pubmed_keyword_hits.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["keyword", "pmid", "year", "first_author", "journal", "title", "context"])
        w.writeheader()
        w.writerows(hits)
    with open(os.path.join(OUT, "pubmed_keyword_counts.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["keyword", "regex", "n_records_with_hit", "n_records_screened"])
        for k, pat in KEYWORDS.items():
            w.writerow([k, pat, counts.get(k, 0), len(recs)])

    rows = []
    for name, q in TARGETED.items():
        c, pm = esearch(q, retmax=200)
        rows.append(dict(query_name=name, n_hits=c, pmids=";".join(pm), query=q))
        print(f"{name}: {c}", file=sys.stderr)
    with open(os.path.join(OUT, "pubmed_targeted_queries.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["query_name", "n_hits", "pmids", "query"])
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(OUT, "pubmed_run_info.txt"), "w") as f:
        f.write(f"run_date\t{run_date}\nmain_query\t{MAIN_QUERY}\nn_records\t{len(recs)}\n")


if __name__ == "__main__":
    main()
