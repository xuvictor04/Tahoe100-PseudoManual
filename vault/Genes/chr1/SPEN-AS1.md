---
symbol: "SPEN-AS1"
type: "gene"
col: 11053
ensembl_id: "ENSG00000179743"
name: "SPEN antisense RNA 1"
location: "1p36.21"
module: 35
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SPEN-AS1

*SPEN antisense RNA 1* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.53× (z +25.6, q 0e+00, up in 37 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALINC1]] (+0.80, fdr 7e-06), [[ANKHD1-DT]] (+0.80, fdr 7e-06), [[PAXBP1-AS1]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.53×** | +25.6 | 0e+00 | 37/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +11.3 | 2e-27 | 24/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +10.9 | 3e-25 | 18/23 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +10.6 | 4e-24 | 5/6 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +10.6 | 5e-24 | 26/37 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +9.8 | 1e-20 | 10/13 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +8.0 | 1e-13 | 24/36 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +6.6 | 3e-09 | 16/46 (SW480, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.7 | 6e-07 | 17/47 (Hs 766T, J82, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +5.3 | 5e-06 | 15/45 (BT-474, HEC-1-A, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.1 | 2e-05 | 7/26 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.9 | 0.004 | 4/22 (RKO, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 4/47 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.009 | 8/33 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.010 | 7/38 (A-427, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.010 | 7/42 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.015 | 10/46 (Hs 766T, J82, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.017 | 2/22 (HEC-1-A, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.053 | 7/45 (C32, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.751× | -3.1 | 0.95 | 11/35 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.17 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.5× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +11.7) | — |
| [[J82 (line)]] | alt | 5.70 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 5.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 3.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 5.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +10.0) | — |
| [[KATO III (line)]] | alt | 7.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +9.3) | — |
| [[LoVo (line)]] | wt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.9) | — |
| [[SW480 (line)]] | alt | 7.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.3) | — |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALINC1]] | +0.80 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ANKHD1-DT]] | +0.80 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.79 | +0.78 / +0.67 | both halves | 7e-06 | same gene group |
| [[KMT2E-AS1]] | +0.78 | +0.65 / +0.53 | both halves | 1e-05 | same gene group |
| [[LINC01090]] | +0.77 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[DDX19A-DT]] | +0.77 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.76 | +0.59 / +0.71 | both halves | 7e-06 | same gene group |
| [[PPP1R9A-AS1]] | +0.76 | +0.72 / +0.55 | both halves | 1e-05 | same gene group |
| [[FAM174B]] | +0.76 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[PJVK]] | +0.76 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[EFCAB5]] | +0.75 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[USP34-DT]] | +0.75 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPEN-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.1, 22.2); signed map (30.1, -2.2). **Vector** length 58.4, 8.21% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +25.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | SPEN antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.21 — chr1:15,834,474-15,848,147 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ37453 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55937) · Entrez [729614](https://www.ncbi.nlm.nih.gov/gene/729614) · Ensembl [ENSG00000179743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179743)

## Data

Gene col 11053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11053); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11053]; `tensor/DDL_lfc|DDL_z.npy` [11053]; `embed/gene_vectors.npy` [11053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11053 or target_col == 11053). Every well: [[SPEN-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPEN-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
