---
symbol: "NACA"
type: "gene"
col: 12230
ensembl_id: "ENSG00000196531"
name: "nascent polypeptide associated complex subunit alpha"
location: "12q13.3"
module: 43
arm: "+"
pooled_cpm: 227.76
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NACA

*nascent polypeptide associated complex subunit alpha* — 12q13.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +7.4, q 8e-11, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 4.10×, NCI-H1792 4.46×, HOP62 3.42×, MIA PaCa-2 3.77×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 3.68×, A549 3.15×, LoVo 2.96×, A498 2.84×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL37]] (+0.90, fdr 7e-06, ⚠ RPL37 in the vector space only through flagged drug-doses), [[RPL30]] (+0.90, fdr 7e-06, ⚠ RPL30 in the vector space only through flagged drug-doses), [[RPL5]] (+0.90, fdr 7e-06), [[RPL19]] (+0.89, fdr 7e-06), [[RPL17]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12230.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 4.10×, NCI-H1792 4.46×, HOP62 3.42×, MIA PaCa-2 3.77×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 3.68×, A549 3.15×, LoVo 2.96×, A498 2.84×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.4 | 8e-11 | 48/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.1 | 3e-10 | 42/44 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.78×** | +5.3 | 2e-05 | 47/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.4 | 0.001 | 38/45 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.7 | 0.028 | 40/47 (C32, COLO 205, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.38× | +3.0 | 0.23 | 36/48 (KATO III, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.793× | -3.0 | 0.83 | 27/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 247 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 207 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 361 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 344 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 227 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 231 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 207 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 275 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 159 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 168 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 206 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 188 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 341 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 230 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 284 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 265 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 306 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 308 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL37]] ⚠ | +0.90 | +0.85 / +0.91 | both halves | 7e-06 | STRING 908; ⚠ in the vector space only through flagged drug-doses |
| [[RPL30]] ⚠ | +0.90 | +0.84 / +0.90 | both halves | 7e-06 | STRING 980; ⚠ in the vector space only through flagged drug-doses |
| [[RPL5]] | +0.90 | +0.85 / +0.92 | both halves | 7e-06 | STRING 980 |
| [[RPL19]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 | STRING 985 |
| [[RPS6]] ⚠ | +0.86 | +0.81 / +0.86 | both halves | 7e-06 | STRING 913; ⚠ in the vector space only through flagged drug-doses |
| [[RPL17]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | STRING 982 |
| [[RPL34]] | +0.86 | +0.77 / +0.91 | both halves | 7e-06 | STRING 959 |
| [[RPL21]] ⚠ | +0.86 | +0.81 / +0.83 | both halves | 7e-06 | STRING 971; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.86 | +0.79 / +0.89 | both halves | 7e-06 | STRING 955 |
| [[RPS3]] ⚠ | +0.85 | +0.77 / +0.88 | both halves | 7e-06 | STRING 855; ⚠ in the vector space only through flagged drug-doses |
| [[RPL7]] | +0.85 | +0.81 / +0.88 | both halves | 7e-06 | STRING 981 |
| [[RPL11]] | +0.85 | +0.81 / +0.90 | both halves | 7e-06 | STRING 965 |
| [[RPL23]] | +0.85 | +0.79 / +0.87 | both halves | 7e-06 | STRING 962 |
| [[RPS8]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 | STRING 914 |
| [[RPS4X]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | STRING 727 |
| [[RPL35A]] | +0.84 | +0.74 / +0.88 | both halves | 7e-06 | STRING 964 |
| [[RPL31]] | +0.84 | +0.74 / +0.88 | both halves | 7e-06 | STRING 973 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.893). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-44.9, -28.8); signed map (-59.9, -5.6). **Vector** length 72.0, 37.3% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.77 to 55); *Peptide chain elongation* (reactome, mean cos +0.78 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.78 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | -0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.4 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | +0.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | +0.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.8 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | nascent polypeptide associated complex subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,712,305-56,731,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NACA1, Alpha-NAC |
| Reactome | 3 pathways, smallest: Dengue Virus Genome Translation and Replication; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [E9PAV3](https://www.uniprot.org/uniprotkb/E9PAV3) (Nascent polypeptide-associated complex subunit alpha, muscle-specific form):

> Cardiac- and muscle-specific transcription factor. May act to regulate the expression of genes involved in the development of myotubes. Plays a critical role in ventricular cardiomyocyte expansion and regulates postnatal skeletal muscle growth and regeneration. Involved in the organized assembly of thick and thin filaments of myofibril sarcomeres (By similarity).

**Summary**, from NCBI Gene [4666](https://www.ncbi.nlm.nih.gov/gene/4666):

> This gene encodes a protein that associates with basic transcription factor 3 (BTF3) to form the nascent polypeptide-associated complex (NAC). This complex binds to nascent proteins that lack a signal peptide motif as they emerge from the ribosome, blocking interaction with the signal recognition particle (SRP) and preventing mistranslocation to the endoplasmic reticulum. This protein is an IgE autoantigen in atopic dermatitis patients. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:7629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7629) · Entrez [4666](https://www.ncbi.nlm.nih.gov/gene/4666) · UniProt [E9PAV3](https://www.uniprot.org/uniprotkb/E9PAV3) · Ensembl [ENSG00000196531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196531)

## Data

Gene col 12230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12230); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12230]; `tensor/DDL_lfc|DDL_z.npy` [12230]; `embed/gene_vectors.npy` [12230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12230 or target_col == 12230). Every well: [[NACA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NACA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
