---
symbol: "ABCD3"
type: "gene"
col: 3922
ensembl_id: "ENSG00000117528"
name: "ATP binding cassette subfamily D member 3"
location: "1p21.3"
module: 15
arm: "-"
pooled_cpm: 72.23
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ABCD3

*ATP binding cassette subfamily D member 3* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.90× (z +34.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.801× (z -5.6, q 1e-05, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HepG2/C3A 0.351×, C32 0.478×, SW480 0.639×, LoVo 0.638×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-1 0.167×, LoVo 0.438×, AN3 CA 0.155×, RKO 0.446×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.345×, RKO 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (68 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH3A2]] (+0.60, fdr 3e-05), [[SORT1]] (+0.57, fdr 1e-04), [[ARHGEF12]] (+0.54, fdr 3e-05); moves opposite to [[USP36]] (-0.56, fdr 2e-05), [[EIF3J-DT]] (-0.56, fdr 0.001, ⚠ one half only (not replicated)), [[RECQL5]] (-0.56, fdr 4e-04), [[PCF11-AS1]] (-0.55, fdr 3e-04).
> It sits in the **-** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.90×** | +34.3 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +28.1 | 0e+00 | 43/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.03×** | +27.9 | 0e+00 | 48/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.92×** | +27.0 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +14.7 | 0e+00 | 46/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +14.4 | 6e-45 | 43/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +10.6 | 2e-24 | 35/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.20×** | +10.1 | 5e-22 | 43/49 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +8.8 | 6e-17 | 39/48 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +8.8 | 6e-17 | 32/48 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +8.5 | 8e-16 | 30/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +8.4 | 1e-15 | 32/48 (SNU-423, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +7.9 | 2e-13 | 28/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +7.6 | 2e-12 | 26/48 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +7.0 | 9e-11 | 32/49 (NCI-H2347, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3922.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HepG2/C3A 0.351×, C32 0.478×, SW480 0.639×, LoVo 0.638×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SNU-1 0.167×, LoVo 0.438×, AN3 CA 0.155×, RKO 0.446×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.345×, RKO 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.801×** | -5.6 | 1e-05 | 23/48 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.882× | -4.5 | 0.002 | 15/48 (NCI-H1792, A-427, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.852× | -4.0 | 0.010 | 13/49 (NCI-H2122, Hs 766T, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.874× | -3.4 | 0.088 | 15/48 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.918× | -3.1 | 0.21 | 7/48 (PANC-1, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.918× | -3.1 | 0.21 | 7/49 (C32, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 116 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +28.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 50.0 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.78× (z +16.4) | — |
| [[HEC-1-A (line)]] | alt | 80.0 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +17.1) | — |
| [[LoVo (line)]] | wt | 105 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 84.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.73× (z +18.8) | — |
| [[A498 (line)]] | wt | 69.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +16.5) | — |
| [[AsPC-1 (line)]] | alt | 66.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +18.6) | — |
| [[CFPAC-1 (line)]] | alt | 48.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +23.0) | — |
| [[HOP62 (line)]] | alt | 35.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.43× (z +18.3) | — |
| [[HS-578T (line)]] | alt | 91.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.13× (z +21.1) | — |
| [[HT-29 (line)]] | alt | 163 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +18.6) | — |
| [[J82 (line)]] | alt | 61.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +18.5) | — |
| [[KATO III (line)]] | alt | 104 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.91× (z +21.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 64.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 46.5 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +20.8) | — |
| [[SW1417 (line)]] | alt | 74.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.2) | — |
| [[BT-474 (line)]] | alt | 48.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +13.1) | — |
| [[C32 (line)]] | wt | 121 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 65.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.01× (z +17.7) | — |
| [[hTERT-HPNE (line)]] | wt | 42.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.67× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 56.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 133 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 44.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 55.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +14.5) | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 61.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +17.8) | — |
| [[Panc 03.27 (line)]] | alt | 81.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.1) | — |
| [[SK-MEL-2 (line)]] | alt | 65.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 59.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.8) | — |
| [[SW48 (line)]] | wt | 93.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +11.0) | — |
| [[A-172 (line)]] | wt | 41.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +13.3) | — |
| [[A549 (line)]] | wt | 49.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 93.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +24.1) | — |
| [[H4 (line)]] | wt | 36.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.02× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 178 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 57.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +15.2) | — |
| [[RPMI-7951 (line)]] | alt | 58.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 83.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +10.5) | — |
| [[A-427 (line)]] | wt | 57.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +12.3) | — |
| [[AN3 CA (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 77.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 81.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 72.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3A2]] | +0.60 | +0.46 / +0.60 | both halves | 3e-05 | pathway: Class I peroxisomal membrane protein import; STRING 551 |
| [[SORT1]] | +0.57 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[ARHGEF12]] | +0.54 | +0.43 / +0.61 | both halves | 3e-05 | pathway: RHOA GTPase cycle |
| [[GDE1]] | +0.53 | +0.19 / +0.62 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SLC44A1]] | +0.52 | +0.22 / +0.53 | both halves | 6e-04 |  |
| [[LBR]] | +0.52 | +0.40 / +0.49 | both halves | 5e-05 | pathway: Metabolism of steroids |
| [[TACC1]] | +0.52 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[SESN3]] | +0.52 | +0.37 / +0.60 | both halves | 7e-05 |  |
| [[GALNT10]] | +0.52 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[GALNT1]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[STIM2]] | +0.52 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[DPY19L1]] | +0.51 | +0.27 / +0.50 | both halves | 3e-04 |  |
| [[EFR3A]] | +0.50 | +0.31 / +0.52 | both halves | 2e-04 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 27 of them with an alert (⚠; 27 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP36]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[EIF3J-DT]] | -0.56 | -0.15 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[RECQL5]] | -0.56 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[PCF11-AS1]] | -0.55 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[POLR1HASP]] | -0.54 | -0.24 / -0.43 | both halves | 5e-04 |  |
| [[RABL2A]] | -0.52 | -0.20 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[C14orf28]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TXNL4B]] | -0.52 | -0.25 / -0.31 | both halves | 4e-04 |  |
| [[SNIP1]] | -0.51 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[ANKRD42-DT]] | -0.51 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[ZNF263]] | -0.51 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PMS2P4-1]] | -0.51 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[ZNF785]] | -0.51 | -0.20 / -0.56 | both halves | 7e-04 |  |
| [[SUPV3L1]] | -0.50 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.5, 27.0); signed map (-3.8, 19.5). **Vector** length 99.0, 27.1% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | +4.4 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +10.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +7.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +6.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.1 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -7.3 | -4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -6.5 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.3 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +2.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily D member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:94,418,389-94,518,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PMP70, ZWS2; previously PXMP1 |
| Gene groups (HGNC) | ATP binding cassette subfamily D; GOLD domain containing |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 16 pathways, smallest: Synthesis of bile acids and bile salts via 24-hydroxycholesterol; ABC transporters in lipid homeostasis; Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [P28288](https://www.uniprot.org/uniprotkb/P28288) (ATP-binding cassette sub-family D member 3):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that catalyzes the transport of long- and very-long-chain fatty acyl-CoAs and probably bile acyl-CoAs from the cytosol to the peroxisome matrix for beta-oxydation. Appears to be specifically involved in the peroxisomal transport of branched-chain fatty acyl-CoAs (BCFA-CoAs) and dicarboxylic acyl CoAs (DCA-CoAs). Has fatty acyl-CoA thioesterase and ATPase activities. Probably hydrolyzes fatty acyl-CoAs into free fatty acids prior …

**Summary**, from NCBI Gene [5825](https://www.ncbi.nlm.nih.gov/gene/5825):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ALD subfamily, which is involved in peroxisomal import of fatty acids and/or fatty acyl-CoAs in the organelle. All known peroxisomal ABC transporters are half transporters …

**Accessions** — [HGNC:67](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:67) · Entrez [5825](https://www.ncbi.nlm.nih.gov/gene/5825) · UniProt [P28288](https://www.uniprot.org/uniprotkb/P28288) · Ensembl [ENSG00000117528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117528)

## Data

Gene col 3922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3922); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3922]; `tensor/DDL_lfc|DDL_z.npy` [3922]; `embed/gene_vectors.npy` [3922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3922 or target_col == 3922). Every well: [[ABCD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
