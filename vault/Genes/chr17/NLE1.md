---
symbol: "NLE1"
type: "gene"
col: 1051
ensembl_id: "ENSG00000073536"
name: "notchless homolog 1"
location: "17q12"
module: 33
arm: "+"
pooled_cpm: 6.73
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 16
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NLE1

*notchless homolog 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.96× (z +9.4, q 3e-18, up in 31 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.40× (z +6.4, q 4e-08, up in 17 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.401× (z -18.2, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1B]] (+0.82, fdr 7e-06), [[TMEM177]] (+0.81, fdr 7e-06), [[SNHG17]] (+0.79, fdr 7e-06); moves opposite to [[GNAS]] (-0.68, fdr 1e-05), [[C2]] (-0.64, fdr 4e-05), [[SMIM14]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.96×** | +9.4 | 3e-18 | 31/45 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.40×** | +6.4 | 4e-08 | 17/40 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.1 | 2e-07 | 12/31 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.02×** | +5.2 | 3e-05 | 7/43 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.9 | 1e-04 | 7/44 (LoVo, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 1e-04 | 13/46 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.82×** | +4.4 | 7e-04 | 7/38 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 7e-04 | 9/41 (HCT15, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.4 | 7e-04 | 7/18 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +4.4 | 7e-04 | 12/47 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 7e-04 | 9/45 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +4.3 | 9e-04 | 8/35 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +4.2 | 0.001 | 15/45 (NCI-H2347, C32, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.001 | 10/45 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.77×** | +4.2 | 0.001 | 7/40 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.001 | 17/41 (HT-29, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.002 | 4/33 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.002 | 0/34 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 10/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.004 | 3/43 (SHP-77, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.401×** | -18.2 | 0e+00 | 37/41 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -7.7 | 3e-12 | 19/42 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.722×** | -6.5 | 2e-08 | 19/42 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -5.9 | 5e-07 | 18/37 (C-33 A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.659×** | -5.9 | 5e-07 | 17/44 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.6 | 2e-06 | 21/46 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.661×** | -5.6 | 2e-06 | 15/43 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.728×** | -4.5 | 6e-04 | 12/46 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.737×** | -4.3 | 0.001 | 17/42 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.008 | 7/45 (MIA PaCa-2, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.010 | 6/45 (HOP62, CHP-212, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.605×** | -3.7 | 0.010 | 4/45 (C32, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.7 | 0.010 | 6/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.047 | 11/47 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.837× | -3.2 | 0.054 | 12/45 (MIA PaCa-2, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.056 | 10/45 (SK-MEL-2, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.661×** | -3.0 | 0.073 | 4/44 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.11 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -18.0) |
| [[C-33 A (line)]] | alt | 9.94 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0631× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 9.11 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -15.4) |
| [[A-427 (line)]] | wt | 10.0 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0917× (z -8.8) |
| [[A498 (line)]] | wt | 7.66 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.5) |
| [[BT-474 (line)]] | alt | 5.14 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 0.5 µM 0.0799× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.2) |
| [[J82 (line)]] | alt | 5.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 6.00 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 7.42 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.5) |
| [[RKO (line)]] | wt | 13.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -10.6) |
| [[SHP-77 (line)]] | alt | 8.50 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -8.8) |
| [[SW48 (line)]] | wt | 12.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0673× (z -9.4) |
| [[SW480 (line)]] | alt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.7) |
| [[A-172 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1B]] | +0.82 | +0.81 / +0.80 | both halves | 7e-06 | STRING 784 |
| [[TMEM177]] | +0.81 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[SNHG17]] | +0.79 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[WDR3]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 | same gene group; STRING 671 |
| [[TSEN2]] | +0.77 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[FXN]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[RRP1B]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 | STRING 799 |
| [[DCAF4]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 | same gene group |
| [[ASB13]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[DDX55]] | +0.72 | +0.57 / +0.74 | both halves | 1e-05 | STRING 571 |
| [[DHODH]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.68 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[C2]] | -0.64 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[SMIM14]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[YPEL5]] | -0.63 | -0.38 / -0.63 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NLE1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises NLE1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without MCOLN2 | 0.026 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[FAM78B]] | B | FAM78B activity raises NLE1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.37× lower at baseline in the lines without FAM78B | 0.066 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[MAP2K1]] | B | MAP2K1 activity raises NLE1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[TSEN2]] | C | TSEN2 activity raises NLE1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.911). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.7, -41.3); signed map (-8.2, -51.5). **Vector** length 83.2, 15.9% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.61 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.65 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.65 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.2 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.2 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +5.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -18.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | notchless homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,128,730-35,142,304 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10458, Rsa4; previously NLE |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVX2](https://www.uniprot.org/uniprotkb/Q9NVX2) (Notchless protein homolog 1):

> Plays a role in regulating Notch activity. Plays a role in regulating the expression of CDKN1A and several members of the Wnt pathway, probably via its effects on Notch activity. Required during embryogenesis for inner mass cell survival (By similarity).

**Summary**, from NCBI Gene [54475](https://www.ncbi.nlm.nih.gov/gene/54475):

> Predicted to be involved in regulation of Notch signaling pathway. Predicted to act upstream of or within several processes, including chordate embryonic development; hematopoietic stem cell homeostasis; and positive regulation of canonical Wnt signaling pathway. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19889) · Entrez [54475](https://www.ncbi.nlm.nih.gov/gene/54475) · UniProt [Q9NVX2](https://www.uniprot.org/uniprotkb/Q9NVX2) · Ensembl [ENSG00000073536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073536)

## Data

Gene col 1051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1051); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1051]; `tensor/DDL_lfc|DDL_z.npy` [1051]; `embed/gene_vectors.npy` [1051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1051 or target_col == 1051). Every well: [[NLE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
