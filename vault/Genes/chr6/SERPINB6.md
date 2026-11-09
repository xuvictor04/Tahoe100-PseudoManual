---
symbol: "SERPINB6"
type: "gene"
col: 4542
ensembl_id: "ENSG00000124570"
name: "serpin family B member 6"
location: "6p25.2"
module: 148
arm: "+"
pooled_cpm: 81.72
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 37
n_dd_up_clean: 2
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# SERPINB6

*serpin family B member 6* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.07× (z +4.6, q 0.003, up in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.22× (z +3.8, q 0.027, up in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 1.95×, HT-29 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 2.23×, LS 180 2.09×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.278× (z -34.6, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (70 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTR]] (+0.58, fdr 3e-05), [[UBE3B]] (+0.55, fdr 0.001, ⚠ one half only (not replicated)), [[FBF1]] (+0.54, fdr 3e-04), [[ATRIP]] (+0.53, fdr 3e-04); moves opposite to [[DDX19B]] (-0.52, fdr 6e-04), [[CHN2]] (-0.50, fdr 3e-05), [[ZNF790-AS1]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COL27A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4542.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 1.95×, HT-29 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 2.23×, LS 180 2.09×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.6 | 0.003 | 2/48 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 0.003 | 21/47 (SW480, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.027 | 22/46 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.045 | 17/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.22 | 13/47 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.24 | 16/47 (SK-MEL-2, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.278×** | -34.6 | 0e+00 | 45/47 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.220×** | -28.9 | 0e+00 | 47/47 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.237×** | -27.5 | 0e+00 | 45/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.244×** | -26.9 | 0e+00 | 46/47 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.380×** | -18.5 | 0e+00 | 42/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.385×** | -18.2 | 0e+00 | 44/47 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -17.6 | 0e+00 | 45/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.421×** | -15.9 | 0e+00 | 44/47 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.495×** | -13.4 | 3e-39 | 45/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.537×** | -11.8 | 1e-30 | 43/47 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.538×** | -11.8 | 2e-30 | 42/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -11.4 | 1e-28 | 41/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.553×** | -11.3 | 5e-28 | 42/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -10.6 | 1e-24 | 39/46 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -10.1 | 3e-22 | 43/48 (LoVo, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.371×** | -9.9 | 2e-21 | 43/47 (SNU-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -9.8 | 2e-21 | 38/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 281 | 0 | 23 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0559× (z -37.7) |
| [[SNU-1 (line)]] | wt | 168 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -24.5) |
| [[NCI-H23 (line)]] | alt | 79.7 | 0 | 15 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0909× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.232× (z -22.0) |
| [[J82 (line)]] | alt | 109 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -24.8) |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0913× (z -24.7) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -32.3) |
| [[LoVo (line)]] | wt | 130 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0840× (z -29.0) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -32.4) |
| [[SW480 (line)]] | alt | 35.1 | 2 (2 ⚠) | 9 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.192× (z -19.8) |
| [[LS 180 (line)]] | wt | 97.4 | 1 (1 ⚠) | 9 | [[Dinaciclib (drug)]] 5 µM 2.09× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 173 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0986× (z -25.9) |
| [[NCI-H460 (line)]] | wt | 68.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -26.6) |
| [[PANC-1 (line)]] | alt | 99.6 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -25.5) |
| [[HOP62 (line)]] | alt | 88.7 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -17.0) |
| [[Hs 766T (line)]] | wt | 91.2 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -18.2) |
| [[HS-578T (line)]] | alt | 62.2 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -29.5) |
| [[A-427 (line)]] | wt | 46.3 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.238× (z -14.3) |
| [[A549 (line)]] | wt | 77.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -21.7) |
| [[HCT15 (line)]] | alt | 108 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 46.0 | 0 | 8 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 35.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.5) |
| [[C32 (line)]] | wt | 57.6 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.6) |
| [[hTERT-HPNE (line)]] | wt | 83.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.9) |
| [[KATO III (line)]] | alt | 76.5 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -24.7) |
| [[RPMI-7951 (line)]] | alt | 82.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -22.2) |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -17.2) |
| [[A498 (line)]] | wt | 41.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 57.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -30.5) |
| [[H4 (line)]] | wt | 79.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 64.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.9) |
| [[RKO (line)]] | wt | 72.1 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -12.4) |
| [[COLO 205 (line)]] | alt | 41.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.3) |
| [[HT-29 (line)]] | alt | 39.6 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.256× (z -12.2) |
| [[AN3 CA (line)]] | alt | 108 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -18.8) |
| [[NCI-H2347 (line)]] | alt | 50.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -16.7) |
| [[SW1417 (line)]] | alt | 56.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 41.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.399× (z -9.6) |
| [[BT-474 (line)]] | alt | 40.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -10.8) |
| [[C-33 A (line)]] | alt | 34.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 61.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.2) |
| [[SW 1271 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0587× (z -13.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 49.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.9) |
| [[CHP-212 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTR]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[UBE3B]] | +0.55 | +0.17 / +0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[FBF1]] | +0.54 | +0.27 / +0.39 | both halves | 3e-04 |  |
| [[ATRIP]] | +0.53 | +0.29 / +0.43 | both halves | 3e-04 |  |
| [[CCDC200]] | +0.53 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[INAFM2]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[LINC01135]] | +0.52 | +0.21 / +0.45 | both halves | 7e-04 |  |
| [[CSRNP2]] | +0.51 | +0.28 / +0.34 | both halves | 3e-04 |  |
| [[ING2-DT]] | +0.50 | +0.18 / +0.44 | ⚠ not reproduced | 9e-04 |  |
| [[PITRM1]] | +0.50 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[PPP1R14B-AS1]] | +0.48 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[LINC01358]] | +0.48 | +0.28 / +0.33 | both halves | 3e-04 |  |
| [[POLDIP2]] | +0.48 | +0.20 / +0.48 | both halves | 7e-04 |  |
| [[RABL2B]] | +0.48 | +0.21 / +0.44 | both halves | 6e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19B]] | -0.52 | -0.21 / -0.54 | both halves | 6e-04 |  |
| [[CHN2]] | -0.50 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[ZNF790-AS1]] | -0.48 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[PPARGC1A]] | -0.48 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[WBP2NL]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZNF444]] | -0.47 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[RAB4A]] | -0.47 | -0.17 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[GUSBP18]] | -0.47 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[MTMR8]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[C1QTNF3]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[RASAL1]] | -0.46 | -0.20 / -0.46 | both halves | 7e-04 |  |
| [[TOMM20]] | -0.46 | -0.21 / -0.36 | both halves | 7e-04 |  |
| [[FOXP2]] | -0.45 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LINC02253]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL27A1]] | B | COL27A1 activity raises SERPINB6's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.88× lower at baseline in the lines without COL27A1 | 0.044 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises SERPINB6's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without ZNF341-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[RNF217]] | B | RNF217 activity raises SERPINB6's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 1.39× lower at baseline in the lines without RNF217 | 0.055 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[LINC02999]] | B | LINC02999 activity lowers SERPINB6's level | lines that do not express LINC02999 (43) vs lines expressing it (7) | 2.19× higher at baseline in the lines without LINC02999 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, GCG, SFTPA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (20.2, -10.6); signed map (18.5, -9.6). **Vector** length 74.5, 21.1% of its response variance represented; |z| ≥ 3 in 1,569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.3 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -13.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -11.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -9.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -7.6 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:2,948,159-2,972,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTI, CAP; previously PI6, DFNB91 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 4 pathways, smallest: Dissolution of Fibrin Clot; Neutrophil degranulation; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P35237](https://www.uniprot.org/uniprotkb/P35237) (Serpin B6):

> May be involved in the regulation of serine proteinases present in the brain or extravasated from the blood (By similarity). Inhibitor of cathepsin G, kallikrein-8 and thrombin. May play an important role in the inner ear in the protection against leakage of lysosomal content during stress and loss of this protection results in cell death and sensorineural hearing loss.

**Summary**, from NCBI Gene [5269](https://www.ncbi.nlm.nih.gov/gene/5269):

> The protein encoded by this gene is a member of the serpin (serine proteinase inhibitor) superfamily, and ovalbumin(ov)-serpin subfamily. It was originally discovered as a placental thrombin inhibitor. The mouse homolog was found to be expressed in the hair cells of the inner ear. Mutations in this gene are associated with nonsyndromic progressive hearing loss, suggesting that this serpin plays an important role in the inner ear in the protection against leakage of lysosomal content during …

**Accessions** — [HGNC:8950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8950) · Entrez [5269](https://www.ncbi.nlm.nih.gov/gene/5269) · UniProt [P35237](https://www.uniprot.org/uniprotkb/P35237) · Ensembl [ENSG00000124570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124570)

## Data

Gene col 4542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4542); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4542]; `tensor/DDL_lfc|DDL_z.npy` [4542]; `embed/gene_vectors.npy` [4542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4542 or target_col == 4542). Every well: [[SERPINB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
