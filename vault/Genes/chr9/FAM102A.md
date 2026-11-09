---
symbol: "FAM102A"
type: "gene"
col: 9416
ensembl_id: "ENSG00000167106"
name: "estrogen-induced osteoclastogenesis regulator 1"
location: "9q34.11"
module: 161
arm: "+"
pooled_cpm: 43.16
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# FAM102A

*estrogen-induced osteoclastogenesis regulator 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +10.3, q 3e-22, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 0.05 µM: 0.752× (z -4.1, q 0.017, down in 18 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHDC1]] (+0.65, fdr 8e-06), [[TNK2]] (+0.59, fdr 1e-05), [[EPB41]] (+0.59, fdr 1e-05); moves opposite to [[TFAM]] (-0.58, fdr 3e-05), [[PCNX4]] (-0.54, fdr 2e-05), [[NOL11]] (-0.52, fdr 1e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SPNS2]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZMIZ1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +10.3 | 3e-22 | 34/45 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +9.1 | 3e-17 | 37/44 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +7.2 | 1e-10 | 26/44 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +6.0 | 2e-07 | 26/45 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.9 | 5e-07 | 24/44 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.8 | 5e-07 | 26/45 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.3 | 1e-05 | 27/43 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 3e-05 | 25/44 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +4.1 | 0.002 | 17/45 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.023 | 9/46 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.4 | 0.033 | 10/45 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.061 | 15/45 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.2 | 0.061 | 22/45 (KATO III, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.063 | 10/46 (NCI-H23, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.088 | 17/45 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.096 | 12/45 (J82, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.752×** | -4.1 | 0.017 | 18/45 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.755×** | -4.0 | 0.017 | 23/45 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.025 | 21/44 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.030 | 17/45 (Hs 766T, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.785×** | -3.5 | 0.061 | 18/45 (A-172, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.3 | 0.070 | 18/45 (KATO III, SW1417, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -3.3 | 0.070 | 20/44 (A498, NCI-H1573, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.075 | 14/46 (A-172, A498, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.845× | -3.1 | 0.12 | 10/45 (SW 1271, HCT15, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.12 | 13/44 (SW 900, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.6) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[RKO (line)]] | wt | 28.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.25× (z +10.9) | [[Harringtonine (drug)]] 5 µM 0.165× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 24.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[Panc 03.27 (line)]] | alt | 41.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.6) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[AsPC-1 (line)]] | alt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.76× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 34.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.41× (z +8.6) | — |
| [[A-172 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[TNK2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[EPB41]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC25A29]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[UNC5B]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ARHGEF10L]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RTN4R]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PEDS1]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[SLC7A5]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RBCK1]] | +0.53 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[DOP1B]] | +0.53 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[CDS1]] | +0.52 | +0.40 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAM]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PCNX4]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NOL11]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MTREX]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TRMT6]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MED1]] | -0.51 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[TRMT5]] | -0.51 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[WDR33]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[MRPL50]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TFPI]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TAF2]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[DDX20]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPNS2]] | B | SPNS2 activity raises FAM102A's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without SPNS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[EPS8L2]] | B | EPS8L2 activity raises FAM102A's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without EPS8L2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[CDS1]] | B | CDS1 activity raises FAM102A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without CDS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[F11R]] | B | F11R activity raises FAM102A's level | lines that do not express F11R (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without F11R | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[CDS1]] | B | CDS1 activity weakens FAM102A's drug response | lines that do not express CDS1 (17) vs lines expressing it (28) | the lines without CDS1 respond 1.33× as strongly (z diff -0.90); strongest at Panobinostat 0.5 µM: 2.10x vs 1.35x (z diff -2.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZMIZ1]] | C | ZMIZ1 activity raises FAM102A's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without ZMIZ1 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMIZ1]] | C | FAM102A activity raises ZMIZ1's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without FAM102A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |
| [[TFAM]] | C | FAM102A activity lowers TFAM's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 1.77× higher at baseline in the lines without FAM102A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |
| [[MED1]] | C | FAM102A activity lowers MED1's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 1.38× higher at baseline in the lines without FAM102A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |
| [[MAP4K2]] | C | FAM102A activity lowers MAP4K2's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 2.22× higher at baseline in the lines without FAM102A | 0.071 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent |
| [[CLP1]] | C | FAM102A activity lowers CLP1's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 2.16× higher at baseline in the lines without FAM102A | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.8, 2.3); signed map (-18.6, 32.8). **Vector** length 113, 29.6% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.8 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -3.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | estrogen-induced osteoclastogenesis regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,940,582-127,980,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Eeig1, bA203J24.7, SYM-3A; previously C9orf132, FAM102A |
| Gene groups (HGNC) | NT-C2 domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T9C2](https://www.uniprot.org/uniprotkb/Q5T9C2) (Early estrogen-induced gene 1 protein):

> Key component of TNFSF11/RANKL- and TNF-induced osteoclastogenesis pathways, thereby mediates bone resorption in pathological bone loss conditions (By similarity). Required for TNFSF11/RANKL-induced osteoclastogenesis via its interaction with TNFRSF11A/RANK, thereby facilitates the downstream transcription of NFATC1 and activation of PLCG2 (By similarity). Facilitates recruitment of the transcriptional repressor PRDM1/BLIMP1 to the promoter of the anti-osteoclastogenesis gene IRF8, thereby …

**Summary**, from NCBI Gene [399665](https://www.ncbi.nlm.nih.gov/gene/399665):

> Predicted to be involved in positive regulation of osteoclast differentiation. Predicted to be located in cytoplasm; membrane raft; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31419) · Entrez [399665](https://www.ncbi.nlm.nih.gov/gene/399665) · UniProt [Q5T9C2](https://www.uniprot.org/uniprotkb/Q5T9C2) · Ensembl [ENSG00000167106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167106)

## Data

Gene col 9416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9416); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9416]; `tensor/DDL_lfc|DDL_z.npy` [9416]; `embed/gene_vectors.npy` [9416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9416 or target_col == 9416). Every well: [[FAM102A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM102A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
