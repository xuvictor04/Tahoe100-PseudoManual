---
symbol: "RPA1"
type: "gene"
col: 5310
ensembl_id: "ENSG00000132383"
name: "replication protein A1"
location: "17p13.3"
module: 57
arm: "+"
pooled_cpm: 52.96
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# RPA1

*replication protein A1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.75× (z +10.4, q 1e-22, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.340× (z -28.4, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT21]] (+0.82, fdr 7e-06), [[SKP2]] (+0.79, fdr 7e-06), [[UBAC1]] (+0.77, fdr 7e-06); moves opposite to [[FAM200A]] (-0.71, fdr 7e-06), [[NEPRO-AS1]] (-0.71, fdr 7e-06), [[SLC22A1]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +10.4 | 1e-22 | 45/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +8.6 | 2e-15 | 42/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.55×** | +8.2 | 6e-14 | 43/48 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.56×** | +7.9 | 4e-13 | 28/41 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.33×** | +5.3 | 2e-05 | 25/49 (SK-MEL-2, PANC-1, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +5.1 | 3e-05 | 27/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +5.0 | 6e-05 | 22/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.020 | 14/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.20×** | +3.4 | 0.041 | 16/48 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.043 | 18/47 (RKO, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.043 | 13/48 (NCI-H460, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.20×** | +3.3 | 0.052 | 19/47 (J82, HepG2/C3A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.078 | 13/47 (A549, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.340×** | -28.4 | 0e+00 | 43/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -17.7 | 0e+00 | 44/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.396×** | -17.3 | 0e+00 | 43/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -10.1 | 1e-21 | 43/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.689×** | -6.9 | 4e-10 | 33/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -4.8 | 1e-04 | 29/48 (HCT15, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.865× | -3.8 | 0.010 | 21/48 (HOP62, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.809×** | -3.7 | 0.018 | 18/47 (C32, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.842× | -3.2 | 0.083 | 12/48 (HepG2/C3A, A-172, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.850× | -3.0 | 0.13 | 13/48 (RKO, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -19.3) |
| [[PANC-1 (line)]] | alt | 52.5 | 4 (4 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.8) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.8) |
| [[A-172 (line)]] | wt | 70.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -24.9) |
| [[HEC-1-A (line)]] | alt | 78.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 52.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.4) |
| [[A498 (line)]] | wt | 74.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -17.9) |
| [[C32 (line)]] | wt | 44.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.7) |
| [[HOP62 (line)]] | alt | 48.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -20.2) |
| [[A549 (line)]] | wt | 53.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 34.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.3) |
| [[COLO 205 (line)]] | alt | 46.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -12.4) |
| [[HS-578T (line)]] | alt | 64.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.0) |
| [[LS 180 (line)]] | wt | 40.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 86.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.1) |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -16.0) |
| [[SW 900 (line)]] | alt | 98.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.0) |
| [[SW480 (line)]] | alt | 79.3 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -14.7) |
| [[A-427 (line)]] | wt | 37.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.5) |
| [[AN3 CA (line)]] | alt | 66.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.6) |
| [[BT-474 (line)]] | alt | 40.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.3) |
| [[H4 (line)]] | wt | 59.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.0) |
| [[HCT15 (line)]] | alt | 77.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.2) |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -9.9) |
| [[J82 (line)]] | alt | 72.7 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.2) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.8) |
| [[KATO III (line)]] | alt | 58.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -16.8) |
| [[LoVo (line)]] | wt | 26.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.88× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 44.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -19.2) |
| [[SNU-1 (line)]] | wt | 58.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.3) |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.9) |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.102× (z -9.8) |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.1) |
| [[HT-29 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.242× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 68.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.7) |
| [[SW 1271 (line)]] | alt | 75.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -8.7) |
| [[SW48 (line)]] | wt | 62.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.4) |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | +0.82 | +0.83 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SKP2]] | +0.79 | +0.74 / +0.74 | both halves | 7e-06 | pathway: DNA Replication |
| [[UBAC1]] | +0.77 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.75 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.75 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[NDC1]] | +0.74 | +0.84 / +0.69 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[SHQ1]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[PMS2P3-1]] | +0.73 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[SETD3]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[NAP1L4]] | +0.71 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[WDR5]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | -0.71 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | -0.71 | -0.74 / -0.58 | both halves | 7e-06 |  |
| [[SLC22A1]] | -0.70 | -0.77 / -0.62 | both halves | 7e-06 |  |
| [[RAB30-DT]] | -0.70 | -0.78 / -0.52 | both halves | 1e-05 |  |
| [[HELQ]] | -0.70 | -0.75 / -0.53 | both halves | 1e-05 | STRING 486 |
| [[PBDC1]] | -0.68 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.68 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[KRCC1]] | -0.68 | -0.72 / -0.58 | both halves | 8e-06 |  |
| [[ZNF764]] | -0.68 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[UTP3]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ZNF75A]] | -0.67 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[C14orf119]] | -0.67 | -0.68 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises RPA1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KATNAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[GSPT2]] | B | GSPT2 activity raises RPA1's level | lines that do not express GSPT2 (14) vs lines expressing it (36) | 1.12× lower at baseline in the lines without GSPT2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PALM2AKAP2, KCNN4, MDFIC |
| [[GGH]] | B | GGH activity raises RPA1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without GGH | 0.055 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[ARL14]] | B | ARL14 activity lowers RPA1's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.21× higher at baseline in the lines without ARL14 | 0.075 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises RPA1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without DSCC1 | 0.098 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.2, -15.0); signed map (-38.9, -12.5). **Vector** length 137, 40.8% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.1 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.0 | +8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +5.7 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -13.0 | -17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -12.3 | -17.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.8 | -28.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.9 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | replication protein A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,829,702-1,900,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | REPA1, RPA70, HSSB, RF-A, RP-A |
| Gene groups (HGNC) | Nucleotide excision repair |
| Hallmark sets | MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 74 pathways, smallest: Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha); Removal of the Flap Intermediate |
| Matched by | ensembl_id |

**Function**, from UniProt [P27694](https://www.uniprot.org/uniprotkb/P27694) (Replication protein A 70 kDa DNA-binding subunit):

> As part of the heterotrimeric replication protein A complex (RPA/RP-A), binds and stabilizes single-stranded DNA intermediates that form during DNA replication or upon DNA stress. It prevents their reannealing and in parallel, recruits and activates different proteins and complexes involved in DNA metabolism. Thereby, it plays an essential role both in DNA replication and the cellular response to DNA damage. In the cellular response to DNA damage, the RPA complex controls DNA repair and DNA …

**Summary**, from NCBI Gene [6117](https://www.ncbi.nlm.nih.gov/gene/6117):

> This gene encodes the largest subunit of the heterotrimeric Replication Protein A (RPA) complex, which binds to single-stranded DNA (ssDNA), forming a nucleoprotein complex that plays an important role in DNA metabolism, being involved in DNA replication, repair, recombination, telomere maintenance, and co-ordinating the cellular response to DNA damage through activation of the ataxia telangiectasia and Rad3-related protein (ATR) kinase. The nucleoprotein complex protects the single-stranded …

**Accessions** — [HGNC:10289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10289) · Entrez [6117](https://www.ncbi.nlm.nih.gov/gene/6117) · UniProt [P27694](https://www.uniprot.org/uniprotkb/P27694) · Ensembl [ENSG00000132383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132383)

## Data

Gene col 5310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5310); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5310]; `tensor/DDL_lfc|DDL_z.npy` [5310]; `embed/gene_vectors.npy` [5310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5310 or target_col == 5310). Every well: [[RPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
