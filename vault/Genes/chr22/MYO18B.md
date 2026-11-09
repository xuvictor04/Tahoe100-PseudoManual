---
symbol: "MYO18B"
type: "gene"
col: 5449
ensembl_id: "ENSG00000133454"
name: "myosin XVIIIB"
location: "22q12.1"
module: 61
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 34
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# MYO18B

*myosin XVIIIB* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.7× (z +23.4, q 0e+00, up in 8 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.93× (z +14.9, q 0e+00, up in 15 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.266×, SHP-77 0.257×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.130×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.378×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRD-AS1]] (+0.67, fdr 7e-06), [[KIAA2012]] (+0.66, fdr 7e-06), [[SGCZ]] (+0.64, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.7×** | +23.4 | 0e+00 | 8/12 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.1×** | +22.8 | 0e+00 | 1/4 (NCI-H661) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **8.29×** | +18.0 | 0e+00 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +14.9 | 0e+00 | 15/22 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +10.2 | 2e-22 | 11/26 (C32, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +9.3 | 1e-18 | 9/22 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +8.6 | 4e-16 | 18/28 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +6.6 | 4e-09 | 15/28 (SHP-77, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +6.0 | 2e-07 | 12/29 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.80×** | +5.7 | 6e-07 | 13/26 (HepG2/C3A, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.8 | 8e-05 | 3/17 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +4.3 | 8e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.004 | 5/28 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.005 | 6/22 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.008 | 10/26 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.020 | 6/28 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.023 | 3/28 (J82, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.024 | 2/27 (HEC-1-A, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.025 | 6/22 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5449.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.266×, SHP-77 0.257×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.130×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.378×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | 0.776× | -3.6 | 0.18 | 4/29 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.681× | -3.3 | 0.26 | 3/29 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 58.2 | 2 (1 ⚠) | 3 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.77× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.48× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.3) |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -10.2) |
| [[HOP62 (line)]] | alt | 1.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 49.5× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.967 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRD-AS1]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[KIAA2012]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.61 | +0.39 / +0.74 | both halves | 5e-05 |  |
| [[OPCML]] | +0.61 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[SORCS1]] | +0.61 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[ATP8A2]] | +0.60 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[LINC02511]] | +0.60 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ELAVL3]] | +0.59 | +0.38 / +0.70 | both halves | 7e-05 |  |
| [[SLC51A]] | +0.59 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[SLIT1]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TMPRSS9]] | +0.59 | +0.44 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.5, 32.2); signed map (30.6, 19.3). **Vector** length 37.5, 5.33% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +18.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +22.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +23.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +5.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | myosin XVIIIB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:25,742,144-26,031,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BK125H2.1 |
| Gene groups (HGNC) | Myosin heavy chains, class XVIII |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUG5](https://www.uniprot.org/uniprotkb/Q8IUG5) (Unconventional myosin-XVIIIb):

> May be involved in intracellular trafficking of the muscle cell when in the cytoplasm, whereas entering the nucleus, may be involved in the regulation of muscle specific genes. May play a role in the control of tumor development and progression; restored MYO18B expression in lung cancer cells suppresses anchorage-independent growth.

**Summary**, from NCBI Gene [84700](https://www.ncbi.nlm.nih.gov/gene/84700):

> The protein encoded by this gene may regulate muscle-specific genes when in the nucleus and may influence intracellular trafficking when in the cytoplasm. The encoded protein functions as a homodimer and may interact with F actin. Mutations in this gene are associated with lung cancer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18150) · Entrez [84700](https://www.ncbi.nlm.nih.gov/gene/84700) · UniProt [Q8IUG5](https://www.uniprot.org/uniprotkb/Q8IUG5) · Ensembl [ENSG00000133454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133454)

## Data

Gene col 5449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5449); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5449]; `tensor/DDL_lfc|DDL_z.npy` [5449]; `embed/gene_vectors.npy` [5449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5449 or target_col == 5449). Every well: [[MYO18B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO18B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
