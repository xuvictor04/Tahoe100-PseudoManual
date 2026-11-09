---
symbol: "AGFG2"
type: "gene"
col: 2749
ensembl_id: "ENSG00000106351"
name: "ArfGAP with FG repeats 2"
location: "7q22.1"
module: 97
arm: "+"
pooled_cpm: 8.98
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 26
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# AGFG2

*ArfGAP with FG repeats 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.6× (z +36.2, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.725× (z -5.0, q 4e-04, down in 13 of 46 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINA5]] (+0.65, fdr 7e-06), [[SORT1]] (+0.61, fdr 4e-05), [[PNKD]] (+0.61, fdr 3e-05); moves opposite to [[CSTF3]] (-0.61, fdr 1e-04), [[LINC01829]] (-0.56, fdr 5e-04), [[LINC00944]] (-0.54, fdr 0.001, ⚠ not reproduced), [[ATXN10]] (-0.53, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PPL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.6×** | +36.2 | 0e+00 | 46/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **9.09×** | +33.9 | 0e+00 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.08×** | +33.9 | 0e+00 | 46/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.26×** | +18.1 | 0e+00 | 44/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +16.9 | 0e+00 | 28/41 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.25×** | +12.4 | 2e-33 | 31/42 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.42×** | +9.9 | 6e-21 | 30/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +5.9 | 3e-07 | 16/47 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.3 | 8e-06 | 12/47 (SK-MEL-2, J82, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +5.0 | 4e-05 | 17/43 (LoVo, A498, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.8 | 8e-05 | 6/46 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.37×** | +4.6 | 2e-04 | 3/15 (PANC-1, HS-578T, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 2e-04 | 8/46 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.75×** | +4.5 | 3e-04 | 6/39 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 5e-04 | 13/47 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.33×** | +4.2 | 8e-04 | 10/45 (HS-578T, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 13/47 (HS-578T, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -5.0 | 4e-04 | 13/46 (HepG2/C3A, HT-29, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -4.2 | 0.007 | 17/46 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.848× | -3.6 | 0.055 | 16/46 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.785×** | -3.5 | 0.057 | 7/44 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.857× | -3.4 | 0.085 | 4/47 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.816× | -3.1 | 0.16 | 6/45 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.819× | -3.1 | 0.17 | 7/45 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 49.7 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -17.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.3) |
| [[A-172 (line)]] | wt | 4.74 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 16.0× (z +10.6) | [[Naproxen (drug)]] 5 µM 0.0807× (z -9.2) |
| [[LS 180 (line)]] | wt | 9.16 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.67× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[A549 (line)]] | wt | 5.08 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 18.6× (z +10.4) | [[Thymol (drug)]] 0.5 µM 0.0898× (z -8.7) |
| [[C32 (line)]] | wt | 10.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0805× (z -13.5) |
| [[HOP62 (line)]] | alt | 3.91 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 14.7× (z +11.1) | — |
| [[J82 (line)]] | alt | 7.18 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +11.0) | — |
| [[LoVo (line)]] | wt | 3.53 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 31.7× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 5.88 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.87 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 9.35× (z +10.3) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0756× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 2.71 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 9.91 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 6.62× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SNU-423 (line)]] | alt | 5.17 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 15.2× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0603× (z -10.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[A498 (line)]] | wt | 6.58 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.3× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 8.03 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.0× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 7.05 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 16.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.52× (z +11.1) | — |
| [[KATO III (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 3.10 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 22.3× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.69 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 20.6× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 7.30 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.16× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 8.89 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +11.1) | — |
| [[RKO (line)]] | wt | 6.36 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 24.0× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 7.90 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 22.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.91× (z +14.1) | — |
| [[SW480 (line)]] | alt | 13.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.28× (z +16.3) | — |
| [[A-427 (line)]] | wt | 10.2 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 6.29× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[CFPAC-1 (line)]] | alt | 15.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 23.7× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.217× (z -8.6) |
| [[SW 900 (line)]] | alt | 5.83 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 13.0× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINA5]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SORT1]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PNKD]] | +0.61 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[PACSIN2]] | +0.60 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[GALM]] | +0.59 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[NCMAP]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[DNM2]] | +0.57 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ALAD]] | +0.57 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[THRA]] | +0.57 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[TMEM245]] | +0.56 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[FN3KRP]] | +0.56 | +0.24 / +0.39 | both halves | 5e-04 |  |
| [[CEP131]] | +0.56 | +0.20 / +0.44 | ⚠ not reproduced | 8e-04 |  |
| [[PHKA2]] | +0.55 | +0.27 / +0.40 | both halves | 3e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF3]] | -0.61 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[LINC01829]] | -0.56 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[LINC00944]] | -0.54 | -0.15 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[ATXN10]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.53 | -0.15 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[YARS2]] | -0.52 | -0.31 / -0.29 | both halves | 2e-04 |  |
| [[KTN1-AS1]] | -0.51 | -0.40 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[SPOPL-DT]] | -0.51 | -0.42 / -0.22 | both halves | 6e-04 |  |
| [[RNF217-AS1]] | -0.51 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[PRDM5]] | -0.50 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[ST7]] | -0.50 | -0.22 / -0.22 | both halves | 6e-04 |  |
| [[POU6F1]] | -0.50 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[WNT3]] | -0.49 | -0.23 / -0.32 | both halves | 5e-04 |  |
| [[GPATCH2]] | -0.49 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[CRPPA]] | -0.49 | -0.31 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPL]] | B | PPL activity raises AGFG2's level | lines that do not express PPL (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without PPL | 0.004 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[RORC]] | B | RORC activity raises AGFG2's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without RORC | 0.020 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[TJP3]] | B | TJP3 activity raises AGFG2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without TJP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[SORT1]] | B | SORT1 activity raises AGFG2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without SORT1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises AGFG2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without SORL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[SERPINA5]] | B | SERPINA5 activity raises AGFG2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without SERPINA5 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[MPP7]] | B | MPP7 activity raises AGFG2's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without MPP7 | 0.075 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[CPA6]] | B | CPA6 activity lowers AGFG2's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 1.34× higher at baseline in the lines without CPA6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[NRTN]] | C | NRTN activity raises AGFG2's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without NRTN | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.4, 5.5); signed map (-4.2, 19.8). **Vector** length 81.1, 16.2% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.6 | +33.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +36.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +33.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.8 | +4.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +0.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with FG repeats 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,539,203-100,568,220 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RABR; previously HRBL |
| Gene groups (HGNC) | ArfGAPs |
| Matched by | ensembl_id |

UniProt [O95081](https://www.uniprot.org/uniprotkb/O95081) carries no function annotation.

**Summary**, from NCBI Gene [3268](https://www.ncbi.nlm.nih.gov/gene/3268):

> This gene is a member of the HIV-1 Rev binding protein (HRB) family and encodes a protein with one Arf-GAP zinc finger domain, several phe-gly (FG) motifs, and four asn-pro-phe (NPF) motifs. This protein interacts with Eps15 homology (EH) domains and plays a role in the Rev export pathway, which mediates the nucleocytoplasmic transfer of proteins and RNAs. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, …

**Accessions** — [HGNC:5177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5177) · Entrez [3268](https://www.ncbi.nlm.nih.gov/gene/3268) · UniProt [O95081](https://www.uniprot.org/uniprotkb/O95081) · Ensembl [ENSG00000106351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106351)

## Data

Gene col 2749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2749); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2749]; `tensor/DDL_lfc|DDL_z.npy` [2749]; `embed/gene_vectors.npy` [2749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2749 or target_col == 2749). Every well: [[AGFG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGFG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
