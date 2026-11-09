---
symbol: "FRG1CP"
type: "gene"
col: 15996
ensembl_id: "ENSG00000282826"
name: "FSHD region gene 1 family member C, pseudogene"
location: "20q11.1"
module: 45
arm: "+"
pooled_cpm: 21.59
n_lines_expressing: 35
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# FRG1CP

*FSHD region gene 1 family member C, pseudogene* — 20q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.84× (z +10.5, q 4e-23, up in 24 of 28 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 3.11×, A549 3.19×, NCI-H460 3.43×, PANC-1 2.05×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.37×, A549 3.28×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.747× (z -7.1, q 8e-10, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC19]] (+0.65, fdr 2e-05), [[SNX1]] (+0.64, fdr 1e-05), [[PLA2G12A]] (+0.64, fdr 2e-05); moves opposite to [[CYREN]] (-0.62, fdr 2e-05), [[ST7L]] (-0.61, fdr 2e-05), [[HIVEP1]] (-0.59, fdr 7e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[COQ8A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15996.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 3.11×, A549 3.19×, NCI-H460 3.43×, PANC-1 2.05×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.37×, A549 3.28×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +10.5 | 4e-23 | 24/28 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +8.7 | 8e-16 | 16/26 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.4 | 1e-14 | 16/22 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +5.3 | 2e-05 | 16/32 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.25×** | +3.9 | 0.013 | 14/30 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -7.1 | 8e-10 | 19/33 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -7.0 | 9e-10 | 20/32 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -5.5 | 7e-06 | 18/32 (SNU-423, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.810×** | -5.1 | 4e-05 | 16/32 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.745×** | -5.0 | 5e-05 | 16/32 (PANC-1, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.742×** | -4.9 | 7e-05 | 18/32 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.796×** | -3.9 | 0.007 | 11/32 (SNU-423, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.801×** | -3.8 | 0.010 | 12/32 (SW480, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.808×** | -3.7 | 0.016 | 11/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 53.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 27.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.108× (z -12.0) |
| [[HS-578T (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 59.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.3) |
| [[A-427 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 33.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC19]] | +0.65 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SNX1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PLA2G12A]] | +0.64 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PAPSS1]] | +0.63 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[MED30]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ORC4]] | +0.63 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[HACE1]] | +0.62 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[LMBRD1]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[TMEM9]] | +0.62 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DPY30]] | +0.61 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MINDY3]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.61 | +0.55 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYREN]] | -0.62 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ST7L]] | -0.61 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[HIVEP1]] | -0.59 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[PCF11]] | -0.58 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[WARS2-AS1]] | -0.57 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.56 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[SON]] | -0.55 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.55 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[ASXL2]] | -0.55 | -0.57 / -0.29 | both halves | 3e-04 |  |
| [[GALNT7-DT]] | -0.55 | -0.46 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[KDM6B]] | -0.55 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[PRDM15]] | -0.55 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[ADCK1]] | -0.54 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COQ8A]] | B | FRG1CP activity lowers COQ8A's level | lines that do not express FRG1CP (15) vs lines expressing it (35) | 1.40× higher at baseline in the lines without FRG1CP | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000291100, BDNF, GUCY1B1 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.0, -7.6); signed map (-30.6, -7.8). **Vector** length 52.0, 9.65% of its response variance represented; |z| ≥ 3 in 507 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +10.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.0 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member C, pseudogene |
| Locus type | pseudogene |
| Location | 20q11.1 — chr20:28,580,709-28,602,664 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51762) · Entrez [100289097](https://www.ncbi.nlm.nih.gov/gene/100289097) · Ensembl [ENSG00000282826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000282826)

## Data

Gene col 15996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15996); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15996]; `tensor/DDL_lfc|DDL_z.npy` [15996]; `embed/gene_vectors.npy` [15996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15996 or target_col == 15996). Every well: [[FRG1CP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1CP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
