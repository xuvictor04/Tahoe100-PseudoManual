---
symbol: "OVAAL"
type: "gene"
col: 14094
ensembl_id: "ENSG00000236719"
name: "ovarian adenocarcinoma amplified long non-coding RNA"
location: "1q25.3"
module: 22
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 5
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# OVAAL

*ovarian adenocarcinoma amplified long non-coding RNA* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.36× (z +13.4, q 4e-38, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.270×).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM241B]] (+0.50, fdr 6e-04), [[NEIL2]] (+0.50, fdr 2e-04), [[TMEM241]] (+0.49, fdr 0.001, ⚠ not reproduced), [[MKRN2]] (+0.49, fdr 3e-04); moves opposite to [[SIX5]] (-0.53, fdr 1e-04), [[SKA2]] (-0.52, fdr 2e-04), [[PCNT]] (-0.51, fdr 7e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CSAG1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.36×** | +13.4 | 4e-38 | 0/3 | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.28×** | +12.0 | 6e-31 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.22×** | +9.0 | 4e-17 | 1/2 (LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.17×** | +8.4 | 6e-15 | 2/2 (SK-MEL-2, LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.83×** | +8.3 | 8e-15 | 0/2 | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.95×** | +5.5 | 3e-06 | 1/3 (LOX-IMVI) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.29×** | +5.3 | 8e-06 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.88×** | +5.2 | 2e-05 | 0/3 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.01×** | +5.0 | 3e-05 | 2/3 (SK-MEL-2, LOX-IMVI) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.68×** | +4.8 | 7e-05 | 1/2 (SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.52×** | +4.7 | 1e-04 | 1/2 (SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.3 | 8e-04 | 1/3 (SK-MEL-2) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +4.0 | 0.002 | 0/2 | top dose only | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.78×** | +3.7 | 0.008 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.008 | 2/3 (LOX-IMVI, KATO III) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.99×** | +3.5 | 0.017 | 0/2 | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +3.1 | 0.059 | 2/2 (SK-MEL-2, LOX-IMVI) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +3.1 | 0.062 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14094.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.270×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.543× | -3.0 | 0.72 | 0/3 | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.546× | -3.0 | 0.72 | 1/3 (KATO III) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 65.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.3) |
| [[A-172 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.276 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM241B]] | +0.50 | +0.39 / +0.22 | both halves | 6e-04 |  |
| [[NEIL2]] | +0.50 | +0.38 / +0.31 | both halves | 2e-04 |  |
| [[TMEM241]] | +0.49 | +0.18 / +0.45 | ⚠ not reproduced | 0.001 |  |
| [[MKRN2]] | +0.49 | +0.46 / +0.28 | both halves | 3e-04 |  |
| [[ATP6V0D2]] | +0.49 | +0.29 / +0.42 | both halves | 3e-04 |  |
| [[DFFA]] | +0.49 | +0.33 / +0.32 | both halves | 2e-04 |  |
| [[TMEM161A]] | +0.48 | +0.45 / +0.24 | both halves | 4e-04 |  |
| [[MFSD9]] | +0.48 | +0.16 / +0.39 | ⚠ not reproduced | 0.001 |  |
| [[NT5C3B]] | +0.47 | +0.45 / +0.25 | both halves | 4e-04 |  |
| [[CYB5R1]] | +0.47 | +0.41 / +0.27 | both halves | 3e-04 |  |
| [[PACC1]] | +0.46 | +0.33 / +0.31 | both halves | 2e-04 |  |
| [[GNPTAB]] | +0.46 | +0.39 / +0.27 | both halves | 3e-04 |  |
| [[DUXAP9]] | +0.46 | +0.34 / +0.34 | both halves | 1e-04 |  |
| [[LINC00698]] | +0.45 | +0.31 / +0.47 | both halves | 2e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX5]] | -0.53 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[SKA2]] | -0.52 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[PCNT]] | -0.51 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[SCLT1]] | -0.50 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[DLEU2]] | -0.49 | -0.36 / -0.32 | both halves | 2e-04 | same gene group |
| [[BAHCC1]] | -0.49 | -0.22 / -0.40 | both halves | 6e-04 |  |
| [[PHF19]] | -0.49 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[STK11]] | -0.48 | -0.31 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[TNRC18]] | -0.48 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[EP300]] | -0.47 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[KBTBD2]] | -0.47 | -0.27 / -0.32 | both halves | 3e-04 |  |
| [[NUCKS1]] | -0.46 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[RGL2]] | -0.46 | -0.23 / -0.36 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSAG1]] | C | CSAG1 activity raises OVAAL's level | lines that do not express CSAG1 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without CSAG1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, ENSG00000226043, LINC02616; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction -0.371). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.4, -53.2); signed map (-11.0, -55.9). **Vector** length 6.27, 1.55% of its response variance represented; |z| ≥ 3 in 56 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.5 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +0.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.4 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.3 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.2 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.2 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -0.3 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.1 | +0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.1 | -2.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.1 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.1 | +0.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ovarian adenocarcinoma amplified long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q25.3 — chr1:180,509,380-180,566,523 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LINC01131, OVAL, RMEL2 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [148756](https://www.ncbi.nlm.nih.gov/gene/148756):

> Predicted to enable pre-mRNA branch point binding activity. Predicted to be involved in mRNA branch site recognition. Predicted to be part of U2 snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49422) · Entrez [148756](https://www.ncbi.nlm.nih.gov/gene/148756) · Ensembl [ENSG00000236719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236719)

## Data

Gene col 14094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14094); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14094]; `tensor/DDL_lfc|DDL_z.npy` [14094]; `embed/gene_vectors.npy` [14094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14094 or target_col == 14094). Every well: [[OVAAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OVAAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
