---
symbol: "FGFR1"
type: "gene"
col: 1198
ensembl_id: "ENSG00000077782"
name: "fibroblast growth factor receptor 1"
location: "8p11.23"
module: 154
arm: "+"
pooled_cpm: 119.35
n_lines_expressing: 42
n_dd_up: 49
n_dd_down: 1
n_dd_up_clean: 29
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# FGFR1

*fibroblast growth factor receptor 1* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.89× (z +23.0, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.742× (z -4.6, q 0.002, down in 23 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 11 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.278×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.321×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.204×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTNA]] (+0.65, fdr 1e-05), [[PIK3CD]] (+0.60, fdr 7e-06), [[NPTX1]] (+0.60, fdr 1e-05); moves opposite to [[TAF8]] (-0.48, fdr 4e-05), [[KAT7]] (-0.48, fdr 1e-04), [[YLPM1]] (-0.47, fdr 5e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); 5 go from it, the strongest it → [[BCAS4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +23.0 | 0e+00 | 35/40 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +12.8 | 7e-35 | 35/40 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.82×** | +8.9 | 1e-16 | 31/40 (MIA PaCa-2, A-427, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.74×** | +8.6 | 2e-15 | 30/40 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +8.4 | 7e-15 | 33/40 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.9 | 2e-13 | 26/41 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.62×** | +7.4 | 9e-12 | 30/40 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.62×** | +7.4 | 9e-12 | 31/40 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.5 | 6e-09 | 26/40 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +6.5 | 6e-09 | 25/40 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +6.4 | 1e-08 | 28/41 (A-427, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +5.9 | 1e-07 | 27/40 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.8 | 4e-07 | 29/40 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 2e-06 | 30/41 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +5.2 | 7e-06 | 22/40 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.0 | 2e-05 | 24/40 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.7 | 8e-05 | 27/40 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.3 | 5e-04 | 20/40 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.70×** | +4.3 | 5e-04 | 23/39 (SW480, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 6e-04 | 22/41 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 6e-04 | 24/40 (SW480, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.001 | 18/40 (LOX-IMVI, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 11 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.278×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.321×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.742×** | -4.6 | 0.002 | 23/40 (HOP62, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.804× | -3.4 | 0.18 | 18/40 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.817× | -3.2 | 0.25 | 17/40 (AsPC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.25 | 17/39 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.825× | -3.0 | 0.25 | 17/40 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.819× | -3.0 | 0.25 | 20/39 (AsPC-1, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 1,150 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -17.1) |
| [[SW480 (line)]] | alt | 99.5 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +27.6) | — |
| [[NCI-H460 (line)]] | wt | 104 | 12 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.13× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.3 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.0× (z +36.4) | — |
| [[AsPC-1 (line)]] | alt | 159 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +32.7) | — |
| [[NCI-H1573 (line)]] | alt | 70.6 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +16.3) | — |
| [[A-427 (line)]] | wt | 282 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.95× (z +22.6) | — |
| [[NCI-H23 (line)]] | alt | 83.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 217 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.3) | — |
| [[A498 (line)]] | wt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +23.0) | — |
| [[BT-474 (line)]] | alt | 64.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 58.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 128 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 79.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 47.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +22.8) | — |
| [[PANC-1 (line)]] | alt | 42.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.3) | — |
| [[A549 (line)]] | wt | 210 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 258 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.9) | [[Clobetasol propionate (drug)]] 0.5 µM 0.306× (z -9.1) |
| [[J82 (line)]] | alt | 321 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.88× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.3) | — |
| [[RKO (line)]] | wt | 188 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.6) | — |
| [[LoVo (line)]] | wt | 48.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +16.8) | — |
| [[NCI-H2347 (line)]] | alt | 57.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.33× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 36.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.0) | — |
| [[CFPAC-1 (line)]] | alt | 184 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 40.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.25× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 287 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.1) | — |
| [[hTERT-HPNE (line)]] | wt | 235 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 342 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 257 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 95.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +16.7) | — |
| [[SW 900 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.3) | — |
| [[C-33 A (line)]] | alt | 143 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNA]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 | pathway: Constitutive Signaling by Aberrant PI3K in Cancer; STRING 924 |
| [[NPTX1]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[KHDRBS3]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SMS]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[FNBP1]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SH3BP5]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ICAM5]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CSRP2]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PPP2R5B]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[HLA-L-1]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF8]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[KAT7]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[YLPM1]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[DDX23]] | -0.45 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[CPSF7]] | -0.45 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ARMC8]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[COX10]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises FGFR1's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without G0S2 | 0.029 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[CYRIA]] | B | CYRIA activity raises FGFR1's level | lines that do not express CYRIA (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without CYRIA | 0.057 | ⚠ within organs, on part of the lines; also absent: PTGS2, ATP10A, VCAN |
| [[DYRK3]] | B | DYRK3 activity raises FGFR1's level | lines that do not express DYRK3 (7) vs lines expressing it (43) | 4.31× lower at baseline in the lines without DYRK3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ROBO3, DZIP1L; maybe low, not absent |
| [[TNFRSF11A]] | B | TNFRSF11A activity lowers FGFR1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.12× higher at baseline in the lines without TNFRSF11A | 0.085 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[LRP1]] | C | LRP1 activity raises FGFR1's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAS4]] | B | FGFR1 activity raises BCAS4's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.47× lower at baseline in the lines without FGFR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[DSE]] | B | FGFR1 activity raises DSE's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.90× lower at baseline in the lines without FGFR1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[DYRK3]] | B | FGFR1 activity raises DYRK3's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without FGFR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[FSCN1]] | B | FGFR1 activity raises FSCN1's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without FGFR1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[PIK3CD]] | B | FGFR1 activity raises PIK3CD's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.52× lower at baseline in the lines without FGFR1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, -2.9); signed map (-5.5, 48.5). **Vector** length 106, 32.2% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | +5.1 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.6 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | -3.9 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.8 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,400,215-38,468,834 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H2, H3, H4, H5, CEK, FLG, BFGFR, N-SAM; previously FLT2, KAL2 |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Fibroblast growth factor receptor family |
| Hallmark sets | ANGIOGENESIS |
| Reactome | 42 pathways, smallest: Signaling by plasma membrane FGFR1 fusions; FGFR1b ligand binding and activation; Epithelial-Mesenchymal Transition (EMT) during gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P11362](https://www.uniprot.org/uniprotkb/P11362) (Fibroblast growth factor receptor 1):

> Tyrosine-protein kinase that acts as a cell-surface receptor for fibroblast growth factors and plays an essential role in the regulation of embryonic development, cell proliferation, differentiation and migration. Required for normal mesoderm patterning and correct axial organization during embryonic development, normal skeletogenesis and normal development of the gonadotropin-releasing hormone (GnRH) neuronal system. Phosphorylates PLCG1, FRS2, GAB1 and SHB. Ligand binding leads to the …

**Summary**, from NCBI Gene [2260](https://www.ncbi.nlm.nih.gov/gene/2260):

> The protein encoded by this gene is a member of the fibroblast growth factor receptor (FGFR) family, where amino acid sequence is highly conserved between members and throughout evolution. FGFR family members differ from one another in their ligand affinities and tissue distribution. A full-length representative protein consists of an extracellular region, composed of three immunoglobulin-like domains, a single hydrophobic membrane-spanning segment and a cytoplasmic tyrosine kinase domain. The …

**Accessions** — [HGNC:3688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3688) · Entrez [2260](https://www.ncbi.nlm.nih.gov/gene/2260) · UniProt [P11362](https://www.uniprot.org/uniprotkb/P11362) · Ensembl [ENSG00000077782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077782)

## Data

Gene col 1198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1198); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1198]; `tensor/DDL_lfc|DDL_z.npy` [1198]; `embed/gene_vectors.npy` [1198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1198 or target_col == 1198). Every well: [[FGFR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
