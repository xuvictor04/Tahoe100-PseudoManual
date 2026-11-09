---
symbol: "CXXC5"
type: "gene"
col: 10137
ensembl_id: "ENSG00000171604"
name: "CXXC finger protein 5"
location: "5q31.2"
module: 59
arm: "+"
pooled_cpm: 47.56
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 20
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# CXXC5

*CXXC finger protein 5* — 5q31.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.80×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.491× (z -8.1, q 3e-13, down in 29 of 38 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.521× (z -7.0, q 7e-10, down in 27 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBP]] (+0.73, fdr 7e-06), [[ATP8B1]] (+0.59, fdr 1e-05), [[CBX4]] (+0.59, fdr 3e-05); moves opposite to [[DCTD]] (-0.60, fdr 1e-05), [[ZNF731P]] (-0.55, fdr 4e-05), [[ELK3]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ADGRG1]] → it (grade B ⚠); 20 go from it, the strongest it → [[DBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10137.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.80×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | 1.33× | +3.4 | 0.20 | 15/38 (HOP62, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.31× | +3.4 | 0.20 | 13/38 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | 1.32× | +3.2 | 0.20 | 16/38 (SHP-77, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.21× | +3.2 | 0.20 | 15/38 (hTERT-HPNE, CHP-212, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.33× | +3.1 | 0.20 | 16/36 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.21 | 11/39 (SK-MEL-2, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.491×** | -8.1 | 3e-13 | 29/38 (SW480, SW1417, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -7.0 | 7e-10 | 27/37 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.550×** | -6.8 | 2e-09 | 28/38 (SW480, HT-29, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.562×** | -6.3 | 4e-08 | 22/30 (HCT15, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.589×** | -6.0 | 2e-07 | 25/38 (SW480, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.3 | 9e-06 | 23/36 (COLO 205, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.616×** | -5.3 | 1e-05 | 25/37 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.631×** | -5.2 | 1e-05 | 23/35 (HCT15, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.632×** | -5.2 | 1e-05 | 24/38 (COLO 205, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.637×** | -5.1 | 2e-05 | 26/38 (A-172, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -4.7 | 2e-04 | 24/38 (HOP62, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.644×** | -4.6 | 2e-04 | 20/33 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.758×** | -4.4 | 4e-04 | 25/38 (SW480, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.760×** | -4.4 | 4e-04 | 24/38 (HT-29, SW480, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.681×** | -4.4 | 5e-04 | 22/38 (SW480, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -4.2 | 1e-03 | 24/38 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -3.7 | 0.005 | 23/37 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.015 | 18/38 (COLO 205, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -3.4 | 0.015 | 18/39 (HOP62, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.025 | 18/36 (SHP-77, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.1 | 0.037 | 22/38 (A-172, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.042 | 16/38 (H4, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.753×** | -3.1 | 0.042 | 16/37 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.765×** | -3.0 | 0.048 | 20/38 (HepG2/C3A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.766×** | -3.0 | 0.050 | 19/38 (SHP-77, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 155 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -14.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.329× (z -14.1) |
| [[SW480 (line)]] | alt | 92.0 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -22.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.293× (z -11.9) |
| [[COLO 205 (line)]] | alt | 119 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -21.0) |
| [[HT-29 (line)]] | alt | 114 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -14.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.4) |
| [[SW 900 (line)]] | alt | 53.7 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.6) |
| [[HOP62 (line)]] | alt | 59.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -10.5) |
| [[PANC-1 (line)]] | alt | 85.3 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.303× (z -9.2) |
| [[A498 (line)]] | wt | 82.2 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -12.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.245× (z -9.5) |
| [[LS 180 (line)]] | wt | 47.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.1) |
| [[SW1417 (line)]] | alt | 172 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -15.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 76.1 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -9.5) |
| [[HCT15 (line)]] | alt | 75.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0697× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.2) |
| [[HS-578T (line)]] | alt | 98.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CHP-212 (line)]] | wt | 133 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.172× (z -9.0) |
| [[KATO III (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 60.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.436× (z -8.5) |
| [[H4 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -9.4) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.80× (z +11.8) ⚠ position not correctable | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ATP8B1]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CBX4]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[GALM]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GPRC5C]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[BMF]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MYLIP]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 | pathway: Signaling by Nuclear Receptors |
| [[VASN]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CBX8]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[RAB30]] | +0.56 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[EFNA1]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTD]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ELK3]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MAPKAP1]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TTL]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SEC14L1]] | -0.53 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[NBPF20]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[THOC5]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[HARS1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[IRAK1]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG1]] | B | ADGRG1 activity raises CXXC5's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 3.60× lower at baseline in the lines without ADGRG1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[BDKRB2]] | B | BDKRB2 activity raises CXXC5's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.37× lower at baseline in the lines without BDKRB2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[DEPP1]] | B | DEPP1 activity raises CXXC5's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without DEPP1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[TOP2A]] | B | TOP2A activity raises CXXC5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LNX1]] | B | LNX1 activity raises CXXC5's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without LNX1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[TCEA3]] | B | TCEA3 activity raises CXXC5's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without TCEA3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity raises CXXC5's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without LINC00511 | 0.087 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[ZNF608]] | B | ZNF608 activity raises CXXC5's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without ZNF608 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[RORC]] | B | RORC activity raises CXXC5's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without RORC | 0.097 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[ZMIZ1]] | C | ZMIZ1 activity raises CXXC5's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 4.28× lower at baseline in the lines without ZMIZ1 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DBP]] | B | CXXC5 activity raises DBP's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without CXXC5 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[CBX4]] | B | CXXC5 activity raises CBX4's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without CXXC5 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[TEF]] | B | CXXC5 activity raises TEF's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without CXXC5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[RASSF7]] | B | CXXC5 activity raises RASSF7's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without CXXC5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[THRA]] | B | CXXC5 activity raises THRA's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without CXXC5 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[MAPKAP1]] | B | CXXC5 activity strengthens MAPKAP1's drug response | lines that do not express CXXC5 (10) vs lines expressing it (39) | the lines without CXXC5 respond 0.53× as strongly (z diff +2.35); strongest at Dinaciclib 0.05 µM: 0.84x vs 1.44x (z diff +5.7) | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PLEKHH3]] | B | CXXC5 activity raises PLEKHH3's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without CXXC5 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[BMF]] | B | CXXC5 activity raises BMF's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without CXXC5 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[NBPF20]] | B | CXXC5 activity lowers NBPF20's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.64× higher at baseline in the lines without CXXC5 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[ATL1]] | B | CXXC5 activity raises ATL1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without CXXC5 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[LNX1]] | B | CXXC5 activity raises LNX1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.56× lower at baseline in the lines without CXXC5 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[AHDC1]] | B | CXXC5 activity raises AHDC1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without CXXC5 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (21.9, -4.8); signed map (-5.2, 14.1). **Vector** length 115, 32.2% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -5.1 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.0 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.6 | -4.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.5 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | CXXC finger protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,647,299-139,683,882 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC195, RINF, WID |
| Gene groups (HGNC) | Zinc fingers CXXC-type |
| Reactome | 3 pathways, smallest: Estrogen-dependent gene expression; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LFL8](https://www.uniprot.org/uniprotkb/Q7LFL8) (CXXC-type zinc finger protein 5):

> May indirectly participate in activation of the NF-kappa-B and MAPK pathways. Acts as a mediator of BMP4-mediated modulation of canonical Wnt signaling activity in neural stem cells (By similarity). Required for DNA damage-induced ATM phosphorylation, p53 activation and cell cycle arrest. Involved in myelopoiesis. Transcription factor. Binds to the oxygen responsive element of COX4I2 and represses its transcription under hypoxia conditions (4% oxygen), as well as normoxia conditions (20% …

**Summary**, from NCBI Gene [51523](https://www.ncbi.nlm.nih.gov/gene/51523):

> The protein encoded by this gene is a retinoid-inducible nuclear protein containing a CXXC-type zinc finger motif. The encoded protein is involved in myelopoiesis, is required for DNA damage-induced p53 activation, regulates the differentiation of C2C12 myoblasts into myocytes, and negatively regulates cutaneous wound healing. Several transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:26943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26943) · Entrez [51523](https://www.ncbi.nlm.nih.gov/gene/51523) · UniProt [Q7LFL8](https://www.uniprot.org/uniprotkb/Q7LFL8) · Ensembl [ENSG00000171604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171604)

## Data

Gene col 10137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10137); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10137]; `tensor/DDL_lfc|DDL_z.npy` [10137]; `embed/gene_vectors.npy` [10137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10137 or target_col == 10137). Every well: [[CXXC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXXC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
