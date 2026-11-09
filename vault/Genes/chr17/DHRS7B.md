---
symbol: "DHRS7B"
type: "gene"
col: 3017
ensembl_id: "ENSG00000109016"
name: "dehydrogenase/reductase 7B"
location: "17p11.2"
module: 71
arm: "+"
pooled_cpm: 40.42
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DHRS7B

*dehydrogenase/reductase 7B* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +21.0, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -15.5, q 0e+00, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.604× (z -9.3, q 2e-18, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF200]] (+0.73, fdr 7e-06), [[RFWD3]] (+0.72, fdr 7e-06), [[POLA2]] (+0.70, fdr 7e-06); moves opposite to [[LAMP2]] (-0.60, fdr 3e-05), [[EEF2]] (-0.55, fdr 3e-05), [[CREG1]] (-0.55, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SMYD4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +21.0 | 0e+00 | 43/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.81×** | +10.9 | 3e-25 | 45/48 (LoVo, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.78×** | +10.3 | 2e-22 | 34/47 (HOP62, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.73×** | +10.1 | 5e-22 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +10.0 | 1e-21 | 35/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.68×** | +8.6 | 7e-16 | 41/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.47×** | +7.1 | 1e-10 | 33/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 9e-08 | 28/47 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.39×** | +5.8 | 4e-07 | 29/46 (SK-MEL-2, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +5.2 | 1e-05 | 27/47 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +4.7 | 2e-04 | 23/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.28×** | +4.4 | 5e-04 | 23/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.024 | 16/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -15.5 | 0e+00 | 37/47 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.460×** | -13.8 | 1e-40 | 39/47 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.516×** | -11.7 | 1e-29 | 31/41 (SHP-77, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -9.3 | 2e-18 | 33/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -8.4 | 5e-15 | 28/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.615×** | -8.3 | 1e-14 | 34/44 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.785×** | -4.5 | 6e-04 | 21/48 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.796×** | -4.2 | 0.002 | 19/48 (KATO III, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.661×** | -4.0 | 0.004 | 19/48 (Panc 03.27, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.788×** | -3.9 | 0.005 | 20/48 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.8 | 0.008 | 2/48 (MIA PaCa-2, SW 1088) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.765×** | -3.5 | 0.020 | 10/48 (A-172, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~4% of this change | **0.831×** | -3.4 | 0.029 | 19/47 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.882× | -3.3 | 0.044 | 14/48 (SHP-77, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.044 | 18/48 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.054 | 13/48 (J82, A498, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.724×** | -3.1 | 0.062 | 8/48 (NCI-H460, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.832×** | -3.0 | 0.073 | 14/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.7 | 2 (1 ⚠) | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -11.4) |
| [[KATO III (line)]] | alt | 74.8 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 78.3 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -22.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 93.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -9.7) |
| [[SW480 (line)]] | alt | 54.8 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.468× (z -9.6) |
| [[LoVo (line)]] | wt | 34.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -15.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 40.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -14.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 34.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 67.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.4 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.300× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 40.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -17.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 43.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -11.9) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 24.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.230× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 56.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.288× (z -9.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -8.7) |
| [[HCT15 (line)]] | alt | 41.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 46.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.5) | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -11.0) ⚠ toxic |
| [[A498 (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0849× (z -10.1) |
| [[BT-474 (line)]] | alt | 32.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +11.3) | — |
| [[RKO (line)]] | wt | 53.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -13.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 52.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.5) | — |
| [[SW48 (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF200]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[POLA2]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[WDR53]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[LRR1]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[HAUS8]] | +0.68 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[HROB]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PHF5A]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[IPPK]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[FEN1]] | +0.64 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[ASF1B]] | +0.63 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[LIN9]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | -0.60 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[EEF2]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CREG1]] | -0.55 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[SPTAN1]] | -0.55 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[KIDINS220]] | -0.54 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[RAD23B]] | -0.53 | -0.30 / -0.70 | both halves | 2e-04 |  |
| [[APP]] | -0.53 | -0.39 / -0.64 | both halves | 5e-05 |  |
| [[SYNJ2BP]] | -0.52 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[SPTBN1]] | -0.52 | -0.29 / -0.64 | both halves | 2e-04 |  |
| [[SNX15]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CDC73]] | -0.51 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[PCBP2]] | -0.51 | -0.26 / -0.59 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DHRS7B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers DHRS7B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers DHRS7B's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ANXA1]] | B | ANXA1 activity lowers DHRS7B's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.34× higher at baseline in the lines without ANXA1 | 0.098 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[ZNF367]] | C | ZNF367 activity raises DHRS7B's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without ZNF367 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens DHRS7B's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.14× as strongly (z diff -0.70); rises at some drug-doses, falls at others (74% from rises): Doxorubicin (hydrochloride) 5 µM: 1.77x vs 1.41x (z diff -2.3); Dinaciclib 5 µM: 0.41x vs 0.56x (z diff -2.2); Mitoxantrone (dihydrochloride) 5 µM: 1.50x vs 1.21x (z diff -2.0) | 0.552 over the table, 0.028 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMYD4]] | C | DHRS7B's natural level strengthens SMYD4's drug response | DHRS7B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.38; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.7, -48.8); signed map (-42.2, -44.3). **Vector** length 107, 28.9% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +21.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.2 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | +3.7 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -4.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | -15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:21,123,364-21,193,265 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566O084, MGC8916, CGI-93, SDR32C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Plasmalogen biosynthesis; Wax and plasmalogen biosynthesis; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IAN0](https://www.uniprot.org/uniprotkb/Q6IAN0) (Peroxisomal reductase activating PPAR-gamma):

> Reductase required for adipogenesis and activation of PPARG nuclear receptor. Can convert acyl and alkyl dihydroxyacetone-phosphate (DHAP) into glycerolipids and ether lipids, respectively, synthesizing ether-linked phospholipids that act as agonists for PPARG. Also regulates adipogenesis by preventing adipocyte browning: following import into the nucleus, interacts with PRDM16, inhibiting the interaction between PRDM16 and PPARG and preventing differentiation of brown adipocytes.

**Summary**, from NCBI Gene [25979](https://www.ncbi.nlm.nih.gov/gene/25979):

> Predicted to enable DNA-binding transcription factor binding activity and transcription corepressor activity. Predicted to be involved in fat cell differentiation and neutrophil differentiation. Predicted to act upstream of or within several processes, including adipose tissue development; brown fat cell differentiation; and regulation of cold-induced thermogenesis. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24547) · Entrez [25979](https://www.ncbi.nlm.nih.gov/gene/25979) · UniProt [Q6IAN0](https://www.uniprot.org/uniprotkb/Q6IAN0) · Ensembl [ENSG00000109016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109016)

## Data

Gene col 3017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3017); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3017]; `tensor/DDL_lfc|DDL_z.npy` [3017]; `embed/gene_vectors.npy` [3017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3017 or target_col == 3017). Every well: [[DHRS7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
