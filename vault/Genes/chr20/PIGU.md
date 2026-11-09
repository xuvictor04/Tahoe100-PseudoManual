---
symbol: "PIGU"
type: "gene"
col: 2145
ensembl_id: "ENSG00000101464"
name: "phosphatidylinositol glycan anchor biosynthesis class U"
location: "20q11.22"
module: 33
arm: "+"
pooled_cpm: 55.96
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PIGU

*phosphatidylinositol glycan anchor biosynthesis class U* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.18× (z +4.2, q 0.017, up in 18 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 1.33× (z +3.8, q 0.047, up in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (HT-29 2.57×; ⚠ cell-cycle shift, explains ~20% of this change); [[Belinostat (drug)]] 5 µM in 1 line (HT-29 2.49×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.431× (z -30.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL2]] (+0.73, fdr 7e-06), [[KNOP1]] (+0.70, fdr 7e-06), [[PDSS1]] (+0.69, fdr 7e-06); moves opposite to [[MKLN1-AS]] (-0.68, fdr 1e-05), [[GPR137C]] (-0.62, fdr 2e-05), [[LINC02035]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2145.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (HT-29 2.57×; ⚠ cell-cycle shift, explains ~20% of this change); [[Belinostat (drug)]] 5 µM in 1 line (HT-29 2.49×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.2 | 0.017 | 18/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.047 | 11/48 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.075 | 12/48 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.18 | 8/48 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.431×** | -30.3 | 0e+00 | 47/48 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.523×** | -23.3 | 0e+00 | 42/48 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.464×** | -19.5 | 0e+00 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.491×** | -17.4 | 0e+00 | 40/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -15.7 | 0e+00 | 37/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.543×** | -14.9 | 0e+00 | 39/47 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -14.8 | 0e+00 | 45/48 (SW480, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -14.6 | 0e+00 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.584×** | -13.6 | 2e-40 | 37/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.592×** | -13.4 | 6e-39 | 39/49 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -13.0 | 1e-36 | 37/49 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -12.5 | 5e-34 | 35/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.722×** | -11.7 | 4e-30 | 35/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -11.6 | 2e-29 | 29/45 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -10.6 | 2e-24 | 29/42 (Panc 03.27, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.672×** | -10.1 | 2e-22 | 36/47 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -9.7 | 1e-20 | 31/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.833× | -6.5 | 2e-09 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -6.4 | 5e-09 | 22/49 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.806×** | -5.5 | 1e-06 | 23/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.2 | 0 | 17 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -25.1) |
| [[HOP62 (line)]] | alt | 59.1 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -24.1) |
| [[SW1417 (line)]] | alt | 84.4 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -21.1) |
| [[SW480 (line)]] | alt | 66.4 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -19.6) |
| [[PANC-1 (line)]] | alt | 57.8 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -18.0) |
| [[BT-474 (line)]] | alt | 295 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -17.2) |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 55.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.9) |
| [[LS 180 (line)]] | wt | 38.8 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.5) |
| [[SNU-1 (line)]] | wt | 65.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.226× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 60.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0943× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -15.6) |
| [[RKO (line)]] | wt | 51.0 | 0 | 6 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.4) |
| [[SHP-77 (line)]] | alt | 78.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 54.2 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -11.7) |
| [[Hs 766T (line)]] | wt | 80.1 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.1) |
| [[KATO III (line)]] | alt | 61.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -13.2) |
| [[LoVo (line)]] | wt | 34.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 73.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.1) |
| [[A549 (line)]] | wt | 49.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.2) |
| [[C-33 A (line)]] | alt | 67.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -11.8) |
| [[H4 (line)]] | wt | 56.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 83.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -15.1) |
| [[HT-29 (line)]] | alt | 40.6 | 2 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.2) ⚠ cell-cycle shift, explains ~20% of this change | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.5) |
| [[J82 (line)]] | alt | 85.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 52.0 | 0 | 4 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.289× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.3) |
| [[SNU-423 (line)]] | alt | 54.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.0) |
| [[COLO 205 (line)]] | alt | 58.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 38.4 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.293× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 54.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.6) |
| [[A-172 (line)]] | wt | 31.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.3) |
| [[A-427 (line)]] | wt | 62.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.282× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 54.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -12.9) |
| [[SW48 (line)]] | wt | 38.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -9.4) |
| [[A498 (line)]] | wt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.8) |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.106× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.345× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -14.4) |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0714× (z -9.1) |
| [[C32 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL2]] | +0.73 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[KNOP1]] | +0.70 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PDSS1]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[DHX57]] | +0.68 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[RMND1]] | +0.67 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[PRMT7]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[IQCB1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.64 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[VPS37C]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[WRN]] | +0.63 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKLN1-AS]] | -0.68 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[GPR137C]] | -0.62 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[LINC02035]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[PDIA3P1]] | -0.61 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[LINC01208]] | -0.61 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[FAM120AOS]] | -0.60 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | -0.60 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[PSMD7-DT]] | -0.60 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[CAPN3]] | -0.59 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SIX4]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TSGA10]] | -0.59 | -0.54 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIGU's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.2, -18.8); signed map (-41.5, -19.4). **Vector** length 111, 31.7% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.8 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -30.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -15.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -14.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -11.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class U |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,560,542-34,698,790 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA346K17.2, GAB1, PIG-U; previously CDC91L1 |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol transamidase complex |
| Reactome | 2 pathways, smallest: Attachment of GPI anchor to uPAR; Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H490](https://www.uniprot.org/uniprotkb/Q9H490) (GPI-anchor transamidase component PIGU):

> Component of the glycosylphosphatidylinositol-anchor (GPI-anchor) transamidase (GPI-T) complex that catalyzes the formation of the linkage between a proprotein and a GPI-anchor and participates in GPI anchored protein biosynthesis. Binds the lipid portion of GPI-anchor. May act as an organizer in the transmembrane layer to recruit other subunits, and thus is essential for assembly of the complex.

**Summary**, from NCBI Gene [128869](https://www.ncbi.nlm.nih.gov/gene/128869):

> The protein encoded by this gene shares similarity with Saccharomyces cerevisiae Cdc91, a predicted integral membrane protein that may function in cell division control. The protein encoded by this gene is the fifth subunit of GPI transamidase that attaches GPI-anchors to proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15791) · Entrez [128869](https://www.ncbi.nlm.nih.gov/gene/128869) · UniProt [Q9H490](https://www.uniprot.org/uniprotkb/Q9H490) · Ensembl [ENSG00000101464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101464)

## Data

Gene col 2145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2145); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2145]; `tensor/DDL_lfc|DDL_z.npy` [2145]; `embed/gene_vectors.npy` [2145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2145 or target_col == 2145). Every well: [[PIGU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
