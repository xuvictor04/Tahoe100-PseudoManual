---
symbol: "CAT"
type: "gene"
col: 4288
ensembl_id: "ENSG00000121691"
name: "catalase"
location: "11p13"
module: 45
arm: "+"
pooled_cpm: 32.31
n_lines_expressing: 49
n_dd_up: 41
n_dd_down: 10
n_dd_up_clean: 36
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CAT

*catalase* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.17× (z +12.1, q 3e-31, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.530× (z -9.9, q 1e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCPEP1]] (+0.75, fdr 7e-06), [[TMEM14A]] (+0.74, fdr 7e-06), [[ALAD]] (+0.74, fdr 7e-06); moves opposite to [[E2F3]] (-0.69, fdr 7e-06), [[KCNJ14]] (-0.68, fdr 7e-06), [[CRK]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FRRS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +12.1 | 3e-31 | 38/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +11.1 | 5e-26 | 44/47 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +10.3 | 2e-22 | 37/47 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.53×** | +9.5 | 4e-19 | 35/47 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +9.3 | 1e-18 | 35/47 (SW1417, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.2 | 3e-14 | 29/41 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +8.0 | 7e-14 | 39/47 (C32, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.5 | 7e-09 | 29/46 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.3 | 2e-08 | 21/36 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.2 | 3e-08 | 30/47 (KATO III, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **2.05×** | +5.9 | 2e-07 | 36/46 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Mifepristone (drug)]] 5 µM |  | **1.44×** | +5.5 | 2e-06 | 25/47 (LS 180, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 5e-06 | 25/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.7 | 1e-04 | 17/38 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +4.6 | 2e-04 | 21/47 (SW1417, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.69×** | +4.3 | 6e-04 | 17/45 (PANC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.001 | 18/47 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.002 | 15/47 (KATO III, J82, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.530×** | -9.9 | 1e-20 | 35/47 (SNU-423, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -9.6 | 3e-19 | 26/46 (Hs 766T, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -8.2 | 5e-14 | 32/47 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.665×** | -6.4 | 3e-08 | 29/47 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.711×** | -5.3 | 1e-05 | 23/47 (A498, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -5.0 | 5e-05 | 20/47 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.739×** | -4.7 | 2e-04 | 21/46 (SW480, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.746×** | -4.6 | 3e-04 | 20/47 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.624×** | -3.9 | 0.007 | 16/46 (Hs 766T, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.7 | 0.011 | 19/46 (Hs 766T, HOP62, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.4 | 0.035 | 15/45 (A-172, C-33 A, …) | all doses, flat | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM |  | 0.809× | -3.0 | 0.12 | 10/47 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 170 | 0 | 13 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -14.9) |
| [[SW480 (line)]] | alt | 30.1 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.372× (z -10.2) |
| [[A498 (line)]] | wt | 54.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.371× (z -9.2) |
| [[SW1417 (line)]] | alt | 46.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 46.9 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.22× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -11.1) |
| [[SNU-423 (line)]] | alt | 64.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -12.2) |
| [[A-172 (line)]] | wt | 29.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.300× (z -9.6) |
| [[A549 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 20.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.38× (z +9.7) | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 28.3 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0672× (z -9.3) |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.59× (z +9.0) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.213× (z -9.6) |
| [[A-427 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCPEP1]] | +0.75 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[TMEM14A]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ALAD]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[ORC4]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[HMGN3]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[STX7]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ARL3]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[USP48]] | +0.68 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | -0.69 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[KCNJ14]] | -0.68 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[CRK]] | -0.68 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[MIRLET7IHG]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[AGO2]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | -0.66 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[HCG18]] | -0.66 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[MYH3]] | -0.65 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.65 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[SLC20A2]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.63 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TLNRD1]] | -0.63 | -0.69 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRRS1]] | C | FRRS1 activity lowers CAT's level | lines that do not express FRRS1 (3) vs lines expressing it (47) | 2.90× higher at baseline in the lines without FRRS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGEF10L, WDR49, CPT1B; maybe low, not absent |
| [[CAPN5]] | C | CAPN5 activity raises CAT's level | lines that do not express CAPN5 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CAPN5 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22, PLEKHF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.859). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.3, -8.6); signed map (-28.7, -7.6). **Vector** length 124, 34.3% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Iron uptake and transport* (reactome, mean cos +0.53 to 6); *Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +11.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.1 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.9 | +8.0 |
|  | [[NG25 (drug)]] 5 µM |  | +6.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.7 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.4 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.7 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -8.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | catalase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,438,934-34,472,060 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Catalase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, BILE_ACID_METABOLISM, PEROXISOME, XENOBIOTIC_METABOLISM, HEME_METABOLISM, ADIPOGENESIS |
| Reactome | 11 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes; Detoxification of Reactive Oxygen Species |
| Matched by | ensembl_id |

**Function**, from UniProt [P04040](https://www.uniprot.org/uniprotkb/P04040) (Catalase):

> Catalyzes the degradation of hydrogen peroxide (H(2)O(2)) generated by peroxisomal oxidases to water and oxygen, thereby protecting cells from the toxic effects of hydrogen peroxide. Promotes growth of cells including T-cells, B-cells, myeloid leukemia cells, melanoma cells, mastocytoma cells and normal and transformed fibroblast cells.

**Summary**, from NCBI Gene [847](https://www.ncbi.nlm.nih.gov/gene/847):

> This gene encodes catalase, a key antioxidant enzyme in the bodies defense against oxidative stress. Catalase is a heme enzyme that is present in the peroxisome of nearly all aerobic cells. Catalase converts the reactive oxygen species hydrogen peroxide to water and oxygen and thereby mitigates the toxic effects of hydrogen peroxide. Oxidative stress is hypothesized to play a role in the development of many chronic or late-onset diseases such as diabetes, asthma, Alzheimer's disease, systemic …

**Accessions** — [HGNC:1516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1516) · Entrez [847](https://www.ncbi.nlm.nih.gov/gene/847) · UniProt [P04040](https://www.uniprot.org/uniprotkb/P04040) · Ensembl [ENSG00000121691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121691)

## Data

Gene col 4288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4288); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4288]; `tensor/DDL_lfc|DDL_z.npy` [4288]; `embed/gene_vectors.npy` [4288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4288 or target_col == 4288). Every well: [[CAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
