---
symbol: "PIK3CB"
type: "gene"
col: 578
ensembl_id: "ENSG00000051382"
name: "phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit beta"
location: "3q22.3"
module: 159
arm: "+"
pooled_cpm: 130.26
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 12
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# PIK3CB

*phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit beta* — 3q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.457× (z -25.7, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK2G]] (+0.66, fdr 1e-05), [[CDC14B]] (+0.59, fdr 2e-05), [[REPS1]] (+0.58, fdr 4e-05); moves opposite to [[PCF11]] (-0.59, fdr 6e-05), [[JAM2]] (-0.58, fdr 9e-05), [[ATXN1L]] (-0.56, fdr 2e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[RSRC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | 1.31× | +3.5 | 0.28 | 23/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.28× | +3.2 | 0.44 | 16/49 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.27× | +3.0 | 0.44 | 14/49 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.457×** | -25.7 | 0e+00 | 47/49 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.587×** | -17.4 | 0e+00 | 37/48 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.516×** | -15.5 | 0e+00 | 39/44 (SNU-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.549×** | -14.6 | 0e+00 | 40/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.555×** | -14.3 | 4e-44 | 42/49 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.558×** | -14.2 | 2e-43 | 39/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -12.8 | 8e-36 | 40/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.533×** | -12.8 | 2e-35 | 40/45 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.587×** | -12.4 | 1e-33 | 34/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -11.3 | 1e-27 | 37/50 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -10.4 | 2e-23 | 35/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.656×** | -10.2 | 8e-23 | 36/48 (NCI-H460, SW 900, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.663×** | -9.9 | 1e-21 | 36/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -9.8 | 4e-21 | 36/47 (SW1417, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.742×** | -7.2 | 2e-11 | 29/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -6.5 | 3e-09 | 23/48 (A-427, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -6.0 | 5e-08 | 25/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.700×** | -4.5 | 1e-04 | 25/48 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.701×** | -4.5 | 2e-04 | 27/48 (SW 900, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.826×** | -3.8 | 0.002 | 19/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.003 | 25/48 (A498, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.863× | -3.4 | 0.012 | 16/49 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.026 | 18/47 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 106 | 0 | 16 (10 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.226× (z -22.4) |
| [[SW 900 (line)]] | alt | 119 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -27.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -22.2) |
| [[HS-578T (line)]] | alt | 121 | 0 | 12 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.295× (z -14.2) |
| [[PANC-1 (line)]] | alt | 191 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -25.6) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 0 | 10 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.231× (z -18.4) |
| [[NCI-H2347 (line)]] | alt | 196 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -21.9) |
| [[LoVo (line)]] | wt | 143 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -25.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -20.5) |
| [[SW1417 (line)]] | alt | 228 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -19.9) |
| [[SW480 (line)]] | alt | 159 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -24.1) |
| [[A498 (line)]] | wt | 108 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 99.9 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -24.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -21.1) |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.1) |
| [[HOP62 (line)]] | alt | 70.9 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -17.9) |
| [[A-172 (line)]] | wt | 73.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 167 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -16.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -21.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.6) |
| [[C32 (line)]] | wt | 76.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.281× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -22.7) |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -15.9) |
| [[J82 (line)]] | alt | 82.2 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.333× (z -13.3) |
| [[KATO III (line)]] | alt | 216 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -20.3) |
| [[SNU-423 (line)]] | alt | 116 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.3) |
| [[COLO 205 (line)]] | alt | 197 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -25.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.210× (z -17.8) |
| [[HT-29 (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 71.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -12.7) |
| [[LS 180 (line)]] | wt | 135 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 161 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -18.9) |
| [[RKO (line)]] | wt | 112 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.9) |
| [[A-427 (line)]] | wt | 203 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -24.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.641× (z -9.5) |
| [[HCT15 (line)]] | alt | 131 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.6) |
| [[SNU-1 (line)]] | wt | 170 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.2) |
| [[SW48 (line)]] | wt | 163 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -13.0) |
| [[A549 (line)]] | wt | 92.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -14.7) |
| [[BT-474 (line)]] | alt | 109 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.7) |
| [[Hs 766T (line)]] | wt | 135 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 62.9 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -10.8) |
| [[AN3 CA (line)]] | alt | 100 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.198× (z -10.3) |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[CDC14B]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 | pathway: MAPK family signaling cascades |
| [[REPS1]] | +0.58 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[SERAC1]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CPOX]] | +0.56 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SPAST]] | +0.55 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[LRRC1]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.55 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[RALGPS2]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[NR2C1]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[BCR]] | +0.55 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[ARHGAP44]] | +0.54 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCF11]] | -0.59 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[JAM2]] | -0.58 | -0.57 / -0.36 | both halves | 9e-05 | pathway: Cell surface interactions at the vascular wall |
| [[ATXN1L]] | -0.56 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ANKRD17-DT]] | -0.55 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[CHD1-DT]] | -0.54 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[MFF-DT]] | -0.54 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[KDM6B]] | -0.54 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[METTL6]] | -0.53 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.52 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | -0.52 | -0.56 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[IPO9-AS1]] | -0.52 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[ARRDC3-AS1]] | -0.51 | -0.57 / -0.24 | both halves | 4e-04 |  |
| [[PNISR-AS1]] | -0.51 | -0.46 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIK3CB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSRC1]] | B | PIK3CB activity lowers RSRC1's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[BOLA3]] | B | PIK3CB activity raises BOLA3's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ENSG00000224621]] | B | PIK3CB activity raises ENSG00000224621's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[KAT6B]] | B | PIK3CB activity lowers KAT6B's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZNF33A]] | B | PIK3CB activity lowers ZNF33A's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ACTR2]] | B | PIK3CB activity raises ACTR2's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ARPC5L]] | B | PIK3CB activity raises ARPC5L's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[DNM1L]] | B | PIK3CB activity raises DNM1L's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ENSG00000290183]] | B | PIK3CB activity lowers ENSG00000290183's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[NME1]] | B | PIK3CB activity raises NME1's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[RETREG2]] | B | PIK3CB activity lowers RETREG2's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SH3BGRL3]] | B | PIK3CB activity raises SH3BGRL3's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.3, 8.3); signed map (-37.0, -5.9). **Vector** length 91.0, 27.2% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.0 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.5 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.5 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -25.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.7 | -12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -12.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,652,698-138,834,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PIK3C1 |
| Gene groups (HGNC) | Phosphatidylinositol 3-kinase family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 74 pathways, smallest: Co-stimulation by ICOS; Signaling by LTK in cancer; Erythropoietin activates Phosphoinositide-3-kinase (PI3K) |
| Matched by | ensembl_id |

**Function**, from UniProt [P42338](https://www.uniprot.org/uniprotkb/P42338) (Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit beta isoform):

> Phosphoinositide-3-kinase (PI3K) phosphorylates phosphatidylinositol derivatives at position 3 of the inositol ring to produce 3-phosphoinositides. Uses ATP and PtdIns(4,5)P2 (phosphatidylinositol 4,5-bisphosphate) to generate phosphatidylinositol 3,4,5-trisphosphate (PIP3). PIP3 plays a key role by recruiting PH domain-containing proteins to the membrane, including AKT1 and PDPK1, activating signaling cascades involved in cell growth, survival, proliferation, motility and morphology. Involved …

**Summary**, from NCBI Gene [5291](https://www.ncbi.nlm.nih.gov/gene/5291):

> This gene encodes an isoform of the catalytic subunit of phosphoinositide 3-kinase (PI3K). These kinases are important in signaling pathways involving receptors on the outer membrane of eukaryotic cells and are named for their catalytic subunit. The encoded protein is the catalytic subunit for PI3Kbeta (PI3KB). PI3KB has been shown to be part of the activation pathway in neutrophils which have bound immune complexes at sites of injury or infection. Alternative splicing results in multiple …

**Accessions** — [HGNC:8976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8976) · Entrez [5291](https://www.ncbi.nlm.nih.gov/gene/5291) · UniProt [P42338](https://www.uniprot.org/uniprotkb/P42338) · Ensembl [ENSG00000051382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051382)

## Data

Gene col 578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 578); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 578]; `tensor/DDL_lfc|DDL_z.npy` [578]; `embed/gene_vectors.npy` [578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 578 or target_col == 578). Every well: [[PIK3CB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3CB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
