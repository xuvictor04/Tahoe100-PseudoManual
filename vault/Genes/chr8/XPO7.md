---
symbol: "XPO7"
type: "gene"
col: 5038
ensembl_id: "ENSG00000130227"
name: "exportin 7"
location: "8p21.3"
module: 36
arm: "+"
pooled_cpm: 77.68
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# XPO7

*exportin 7* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.92× (z +7.1, q 1e-09, up in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (LoVo 5.02×, KATO III 4.76×, LS 180 4.55×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LoVo 4.69×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.564× (z -16.7, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBGCP3]] (+0.70, fdr 7e-06), [[ORC5]] (+0.66, fdr 1e-05), [[CHCHD6]] (+0.65, fdr 1e-05); moves opposite to [[CATSPERG]] (-0.64, fdr 1e-05), [[HLA-E]] (-0.60, fdr 1e-05), [[LINC01004]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5038.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (LoVo 5.02×, KATO III 4.76×, LS 180 4.55×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.73×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LoVo 4.69×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +7.1 | 1e-09 | 29/49 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +6.2 | 1e-07 | 30/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +3.9 | 0.018 | 20/48 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 1.13× | +3.5 | 0.071 | 4/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.17× | +3.3 | 0.12 | 12/49 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -16.7 | 0e+00 | 46/49 (SW48, SHP-77, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -13.7 | 2e-40 | 36/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -10.1 | 2e-21 | 34/48 (H4, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -9.0 | 3e-17 | 29/48 (AN3 CA, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -7.6 | 5e-12 | 32/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -7.1 | 1e-10 | 36/50 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -6.4 | 1e-08 | 30/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.804×** | -6.4 | 1e-08 | 26/48 (SNU-1, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.725×** | -6.1 | 5e-08 | 27/45 (A549, SW 900, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -6.0 | 1e-07 | 22/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.746×** | -5.8 | 3e-07 | 30/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.767×** | -5.5 | 2e-06 | 30/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -5.4 | 3e-06 | 29/46 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.772×** | -5.3 | 4e-06 | 22/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.790×** | -4.9 | 4e-05 | 28/48 (SW480, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.7 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -20.0) |
| [[SW480 (line)]] | alt | 127 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 96.5 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -14.5) |
| [[A-172 (line)]] | wt | 85.3 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 49.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -18.5) |
| [[SW 900 (line)]] | alt | 76.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.2) |
| [[HOP62 (line)]] | alt | 51.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.3) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -14.4) |
| [[C32 (line)]] | wt | 48.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.0) |
| [[HS-578T (line)]] | alt | 121 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.4) |
| [[J82 (line)]] | alt | 40.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -11.3) |
| [[LoVo (line)]] | wt | 71.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.02× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -11.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 170 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -15.2) |
| [[SNU-1 (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.235× (z -17.8) |
| [[SW48 (line)]] | wt | 127 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -15.8) |
| [[A-427 (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.450× (z -13.8) |
| [[A498 (line)]] | wt | 98.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.8) |
| [[A549 (line)]] | wt | 77.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.1) |
| [[Hs 766T (line)]] | wt | 77.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 37.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 85.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.220× (z -17.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 96.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[RKO (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 76.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.423× (z -8.9) |
| [[BT-474 (line)]] | alt | 57.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.3) |
| [[C-33 A (line)]] | alt | 149 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.4) |
| [[CHP-212 (line)]] | wt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -12.8) |
| [[H4 (line)]] | wt | 103 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.8) |
| [[HCT15 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 62.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 88.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.76× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 87.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.55× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.9) |
| [[PANC-1 (line)]] | alt | 34.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.1) |
| [[SW1417 (line)]] | alt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBGCP3]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ORC5]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[DFFB]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LCLAT1]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ELAVL1]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[DLAT]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[COA1]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ERI3]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SKP2]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERG]] | -0.64 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[HLA-E]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.59 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[CD63]] | -0.58 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[BCL10-AS1]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[NPHS1]] | -0.58 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[HLA-B]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[HLA-A]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[KMT2E-AS1]] | -0.55 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[FAM117A]] | -0.55 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TP53INP2]] | -0.55 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[PKNOX1]] | -0.55 | -0.59 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises XPO7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PHLDA2]] | B | PHLDA2 activity lowers XPO7's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 1.68× higher at baseline in the lines without PHLDA2 | 0.079 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-17.7, -43.5); signed map (-13.2, -48.9). **Vector** length 111, 31.4% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +7.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.4 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | exportin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:21,919,662-22,006,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0745, EXP7; previously RANBP16 |
| Gene groups (HGNC) | Exportins |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIA9](https://www.uniprot.org/uniprotkb/Q9UIA9) (Exportin-7):

> Mediates the nuclear export of proteins (cargos) with broad substrate specificity. In the nucleus binds cooperatively to its cargo and to the GTPase Ran in its active GTP-bound form. Docking of this trimeric complex to the nuclear pore complex (NPC) is mediated through binding to nucleoporins. Upon transit of a nuclear export complex into the cytoplasm, disassembling of the complex and hydrolysis of Ran-GTP to Ran-GDP (induced by RANBP1 and RANGAP1, respectively) cause release of the cargo from …

**Summary**, from NCBI Gene [23039](https://www.ncbi.nlm.nih.gov/gene/23039):

> The transport of protein and large RNAs through the nuclear pore complexes (NPC) is an energy-dependent and regulated process. The import of proteins with a nuclear localization signal (NLS) is accomplished by recognition of one or more clusters of basic amino acids by the importin-alpha/beta complex; see MIM 600685 and MIM 602738. The small GTPase RAN (MIM 601179) plays a key role in NLS-dependent protein import. RAN-binding protein-16 is a member of the importin-beta superfamily of nuclear …

**Accessions** — [HGNC:14108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14108) · Entrez [23039](https://www.ncbi.nlm.nih.gov/gene/23039) · UniProt [Q9UIA9](https://www.uniprot.org/uniprotkb/Q9UIA9) · Ensembl [ENSG00000130227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130227)

## Data

Gene col 5038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5038); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5038]; `tensor/DDL_lfc|DDL_z.npy` [5038]; `embed/gene_vectors.npy` [5038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5038 or target_col == 5038). Every well: [[XPO7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPO7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
