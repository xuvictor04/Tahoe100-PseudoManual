---
symbol: "PLEKHN1"
type: "gene"
col: 11924
ensembl_id: "ENSG00000187583"
name: "pleckstrin homology domain containing N1"
location: "1p36.33"
module: 29
arm: "-"
pooled_cpm: 9.09
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 20
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PLEKHN1

*pleckstrin homology domain containing N1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.66× (z +4.5, q 0.003, up in 17 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.00× (z +4.1, q 0.008, up in 14 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.341× (z -9.6, q 3e-19, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLCF1]] (+0.68, fdr 7e-06), [[ZNF600]] (+0.57, fdr 5e-05), [[RNPEPL1]] (+0.56, fdr 2e-05); moves opposite to [[SLC44A1]] (-0.64, fdr 1e-05), [[TMEM123]] (-0.63, fdr 1e-05), [[MANEA]] (-0.62, fdr 7e-06).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MDFI]] → it (grade B ⚠); 20 go from it, the strongest it → cells under [[AT7519 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.5 | 0.003 | 17/33 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.1 | 0.008 | 7/16 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +4.1 | 0.008 | 14/35 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.89×** | +3.8 | 0.023 | 12/41 (C32, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +3.7 | 0.024 | 12/41 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.053 | 13/36 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.053 | 9/40 (MIA PaCa-2, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.77×** | +3.4 | 0.056 | 11/41 (LS 180, NCI-H1573, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.3 | 0.063 | 13/43 (HS-578T, KATO III, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.1 | 0.094 | 12/35 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.095 | 12/40 (HT-29, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.341×** | -9.6 | 3e-19 | 37/43 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.353×** | -9.3 | 4e-18 | 40/44 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.376×** | -8.7 | 4e-16 | 36/44 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -7.7 | 2e-12 | 29/42 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.480×** | -6.6 | 6e-09 | 32/44 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.248×** | -5.7 | 1e-06 | 33/41 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -5.4 | 4e-06 | 24/44 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.664×** | -5.2 | 2e-05 | 25/45 (KATO III, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.297×** | -4.9 | 5e-05 | 26/42 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.624×** | -4.2 | 0.001 | 19/43 (CFPAC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.621×** | -3.9 | 0.004 | 18/44 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.645×** | -3.9 | 0.004 | 20/40 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.657×** | -3.8 | 0.007 | 22/43 (LoVo, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.413×** | -3.6 | 0.014 | 15/44 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.017 | 18/45 (CFPAC-1, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.3) |
| [[A-172 (line)]] | wt | 6.48 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0468× (z -11.7) |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.0) |
| [[H4 (line)]] | wt | 10.5 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0707× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 8.15 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0603× (z -8.5) |
| [[HOP62 (line)]] | alt | 9.75 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.131× (z -9.5) |
| [[J82 (line)]] | alt | 9.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -8.5) |
| [[LoVo (line)]] | wt | 8.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 6.50 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0718× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 9.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -8.5) |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.8) |
| [[SNU-423 (line)]] | alt | 7.98 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0241× (z -14.3) |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCF1]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ZNF600]] | +0.57 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[RNPEPL1]] | +0.56 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[HOMER3]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[ZNF611]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R14B-AS1]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LAMB3]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CATSPERG]] | +0.54 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[TLNRD1]] | +0.53 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[IER5]] | +0.53 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[LCAT]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A1]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[MANEA]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 | STRING 448 |
| [[PRDX3]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[TMED10]] | -0.60 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SH3BGRL]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PPP1CC]] | -0.57 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MDH1]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ARL5A]] | -0.56 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ERLIN1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ATP5F1A]] | -0.55 | -0.41 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDFI]] | B | MDFI activity raises PLEKHN1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without MDFI | 0.075 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[ST6GALNAC2]] | B | ST6GALNAC2 activity raises PLEKHN1's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without ST6GALNAC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[PHLDA2]] | C | PHLDA2's natural level strengthens PLEKHN1's drug response | PHLDA2's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.23; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AT7519 (drug)]] 5 µM | C | PLEKHN1 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.39× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | PLEKHN1 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 1.55× the cells of the other lines | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[PF-06260933 (drug)]] 5 µM | C | PLEKHN1 activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 1.73× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[Raltitrexed (drug)]] 0.5 µM | C | PLEKHN1 activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 1.38× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[IQ 1 (drug)]] 5 µM | C | PLEKHN1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.68× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[POLD4]] | C | PLEKHN1 activity raises POLD4's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without PLEKHN1 | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16; co-absent with the target |
| cells under [[Infigratinib (drug)]] 5 µM | C | PLEKHN1 activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.54× the cells of the other lines | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | PLEKHN1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.57× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | PLEKHN1 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 1.43× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[PPP1R35]] | C | PLEKHN1 activity raises PPP1R35's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without PLEKHN1 | 0.048 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[NG25 (drug)]] 5 µM | C | PLEKHN1 activity raises the cells' numbers under NG25 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.49× the cells of the other lines | 0.054 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| cells under [[BI-3406 (drug)]] 5 µM | C | PLEKHN1 activity raises the cells' numbers under BI-3406 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.57× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.8, -20.6); signed map (1.6, 32.2). **Vector** length 74.6, 16.1% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.0 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing N1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:966,482-975,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434H2010 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q494U1](https://www.uniprot.org/uniprotkb/Q494U1) (Pleckstrin homology domain-containing family N member 1):

> Controls the stability of the leptin mRNA harboring an AU-rich element (ARE) in its 3' UTR, in cooperation with the RNA stabilizer ELAVL1. Decreases the stability of the leptin mRNA by antagonizing the function of ELAVL1 by inducing its atypical recruitment from the nucleus to the cytosol (By similarity). Binds to cardiolipin (CL), phosphatidic acid (PA), phosphatidylinositol 4-phosphate (PtdIns(4)P) and phosphatidylserine (PS). Promotes apoptosis by enhancing BAX-BAK heterooligomerization via …

**Summary**, from NCBI Gene [84069](https://www.ncbi.nlm.nih.gov/gene/84069):

> Enables phospholipid binding activity. Involved in 3'-UTR-mediated mRNA destabilization; positive regulation of apoptotic process; and response to hypoxia. Located in cytoskeleton; mitochondrial membrane; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25284) · Entrez [84069](https://www.ncbi.nlm.nih.gov/gene/84069) · UniProt [Q494U1](https://www.uniprot.org/uniprotkb/Q494U1) · Ensembl [ENSG00000187583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187583)

## Data

Gene col 11924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11924); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11924]; `tensor/DDL_lfc|DDL_z.npy` [11924]; `embed/gene_vectors.npy` [11924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11924 or target_col == 11924). Every well: [[PLEKHN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
