---
symbol: "GIPC1"
type: "gene"
col: 4411
ensembl_id: "ENSG00000123159"
name: "GIPC PDZ domain containing family member 1"
location: "19p13.12"
module: 85
arm: "+"
pooled_cpm: 31.49
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# GIPC1

*GIPC PDZ domain containing family member 1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.31× (z +18.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.609× (z -10.5, q 7e-23, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TECPR1]] (+0.69, fdr 2e-05), [[ANKRD27]] (+0.65, fdr 3e-05), [[GPRIN1]] (+0.62, fdr 6e-05); moves opposite to [[TGFB3]] (-0.63, fdr 5e-05), [[PDHX]] (-0.59, fdr 1e-04), [[C5orf15]] (-0.58, fdr 4e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ABLIM2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CYTH3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **3.31×** | +18.0 | 0e+00 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.15×** | +17.3 | 0e+00 | 45/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +16.5 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.53×** | +14.0 | 4e-42 | 43/47 (A-172, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.12×** | +11.3 | 1e-27 | 43/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +10.2 | 1e-22 | 44/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.34×** | +6.7 | 2e-09 | 37/48 (NCI-H460, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.4 | 1e-08 | 32/48 (A498, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-06 | 27/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.40×** | +4.9 | 7e-05 | 17/37 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.36×** | +4.7 | 1e-04 | 22/43 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.003 | 19/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.011 | 19/47 (PANC-1, HS-578T, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.6 | 0.011 | 18/43 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.022 | 11/47 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.049 | 9/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.056 | 14/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.058 | 16/47 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -10.5 | 7e-23 | 36/47 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.667×** | -8.6 | 3e-15 | 34/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -5.9 | 5e-07 | 4/49 (NCI-H661, SW 1271, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.730×** | -4.7 | 4e-04 | 22/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.054 | 19/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.054 | 14/48 (Hs 766T, SHP-77, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.853× | -3.3 | 0.061 | 14/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.654×** | -3.3 | 0.061 | 13/47 (BT-474, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Asciminib (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.061 | 17/47 (NCI-H1573, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.802×** | -3.3 | 0.061 | 13/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.799× | -3.1 | 0.11 | 5/47 (SK-MEL-2, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 54.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.437× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 16.9 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.67× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 19.9 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.26× (z +11.3) | — |
| [[A-172 (line)]] | wt | 71.2 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.43× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.7) |
| [[BT-474 (line)]] | alt | 99.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.4) |
| [[HOP62 (line)]] | alt | 14.2 | 4 | 0 | [[Belinostat (drug)]] 5 µM 5.64× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 7.99× (z +9.0) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0833× (z -10.3) |
| [[LoVo (line)]] | wt | 19.0 | 4 | 0 | [[Belinostat (drug)]] 5 µM 4.29× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 3 | 1 | [[Belinostat (drug)]] 5 µM 4.67× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 25.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.25× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0667× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 77.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +10.3) | — |
| [[SW480 (line)]] | alt | 16.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.44× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 39.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 26.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.45× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.81× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 9.87 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 7.19× (z +8.9) | — |
| [[RKO (line)]] | wt | 24.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.27× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.60× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 51.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.06× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.9) |
| [[HT-29 (line)]] | alt | 39.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.48× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -11.1) |
| [[PANC-1 (line)]] | alt | 23.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.90× (z +9.9) | — |
| [[A-427 (line)]] | wt | 40.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.342× (z -11.8) |
| [[A498 (line)]] | wt | 32.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.84× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.8) |
| [[C32 (line)]] | wt | 35.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 11.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.5× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 29.0 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.84× (z +8.8) | — |
| [[J82 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 17.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.67× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 14.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.69× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.88× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -8.8) |
| [[SW1417 (line)]] | alt | 60.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.2) |
| [[A549 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR1]] | +0.69 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.65 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[GPRIN1]] | +0.62 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[MAST3]] | +0.60 | +0.41 / +0.38 | both halves | 6e-05 | same gene group |
| [[AP2A2]] | +0.60 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.60 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[ETNK2]] | +0.60 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[KCTD21]] | +0.59 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[PIP5K1C]] | +0.59 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[LRFN3]] | +0.59 | +0.53 / +0.29 | both halves | 3e-04 |  |
| [[PROSER2]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TRIM11]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFB3]] | -0.63 | -0.40 / -0.44 | both halves | 5e-05 | pathway: Signaling by TGFB family members |
| [[PDHX]] | -0.59 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[C5orf15]] | -0.58 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[SNX5]] | -0.58 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[EIF4G2]] | -0.57 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[PNISR-AS1]] | -0.57 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[PRKAR1A]] | -0.57 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RWDD2B]] | -0.57 | -0.44 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[DECR1]] | -0.57 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[KMT2E-AS1]] | -0.57 | -0.33 / -0.32 | both halves | 1e-04 |  |
| [[PBLD]] | -0.56 | -0.28 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[ERCC6L2-AS1]] | -0.56 | -0.37 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[MPDU1]] | -0.56 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[LINC00910]] | -0.56 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[LPXN]] | -0.56 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM2]] | B | ABLIM2 activity raises GIPC1's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without ABLIM2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[CBLC]] | B | CBLC activity raises GIPC1's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.39× lower at baseline in the lines without CBLC | 0.081 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[TMX4]] | C | TMX4 activity lowers GIPC1's level | lines that do not express TMX4 (3) vs lines expressing it (47) | 1.81× higher at baseline in the lines without TMX4 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FUCA2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYTH3]] | C | GIPC1's natural level weakens CYTH3's drug response | GIPC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.07; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (1.9, 1.0); signed map (-40.4, -4.5). **Vector** length 120, 33.7% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.0 | +18.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.9 | +17.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.4 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -10.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.2 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.3 | -3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | GIPC PDZ domain containing family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,477,760-14,496,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIP-2, Hs.6454, GIPC, SEMCAP, GLUT1CBP, SYNECTIN, NIP; previously C19orf3, RGS19IP1 |
| Gene groups (HGNC) | PDZ domain containing; GIPC PDZ domain containing family |
| Reactome | 10 pathways, smallest: TGFBR3 regulates FGF2 signaling; FGFR1b ligand binding and activation; TGFBR3 regulates TGF-beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14908](https://www.uniprot.org/uniprotkb/O14908) (PDZ domain-containing protein GIPC1):

> May be involved in G protein-linked signaling.

**Summary**, from NCBI Gene [10755](https://www.ncbi.nlm.nih.gov/gene/10755):

> GIPC1 is a scaffolding protein that regulates cell surface receptor expression and trafficking (Lee et al., 2008 [PubMed 18775991]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:1226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1226) · Entrez [10755](https://www.ncbi.nlm.nih.gov/gene/10755) · UniProt [O14908](https://www.uniprot.org/uniprotkb/O14908) · Ensembl [ENSG00000123159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123159)

## Data

Gene col 4411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4411); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4411]; `tensor/DDL_lfc|DDL_z.npy` [4411]; `embed/gene_vectors.npy` [4411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4411 or target_col == 4411). Every well: [[GIPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
