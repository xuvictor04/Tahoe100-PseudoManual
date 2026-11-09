---
symbol: "SPAG1"
type: "gene"
col: 2464
ensembl_id: "ENSG00000104450"
name: "sperm associated antigen 1"
location: "8q22.2"
module: 68
arm: "+"
pooled_cpm: 37.22
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# SPAG1

*sperm associated antigen 1* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.67× (z +54.3, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.163×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.106×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.124×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRAM1]] (+0.61, fdr 1e-05), [[LGALSL-DT]] (+0.61, fdr 3e-05), [[HIVEP1]] (+0.60, fdr 1e-04); moves opposite to [[PHKA2]] (-0.59, fdr 4e-05), [[ST6GALNAC6]] (-0.56, fdr 2e-04), [[TBC1D16]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.67×** | +54.3 | 0e+00 | 47/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.44×** | +31.7 | 0e+00 | 47/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.99×** | +30.6 | 0e+00 | 47/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +24.5 | 0e+00 | 42/47 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.30×** | +18.4 | 0e+00 | 40/48 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +16.9 | 0e+00 | 39/47 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +16.4 | 0e+00 | 41/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.02×** | +15.5 | 0e+00 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.96×** | +14.9 | 0e+00 | 38/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.92×** | +14.4 | 3e-45 | 34/43 (AsPC-1, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +14.1 | 3e-43 | 37/46 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.87×** | +13.9 | 3e-42 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.89×** | +13.6 | 2e-40 | 40/47 (A498, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +12.9 | 2e-36 | 36/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +12.6 | 1e-34 | 36/47 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +12.5 | 3e-34 | 35/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.93×** | +12.4 | 5e-34 | 35/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +12.1 | 3e-32 | 34/47 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.3 | 3e-23 | 34/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +9.4 | 1e-19 | 34/47 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +9.3 | 5e-19 | 33/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +8.7 | 5e-17 | 31/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2464.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 1 line (C-33 A 0.163×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.106×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -5.3 | 6e-05 | 3/48 (SW 1271, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.842× | -3.8 | 0.038 | 10/47 (NCI-H1792, A498, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.855× | -3.5 | 0.098 | 5/48 (SW 1088, SNU-423, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.29 | 12/47 (Panc 03.27, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.6 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +33.7) | — |
| [[PANC-1 (line)]] | alt | 32.5 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +32.6) | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +23.0) | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +21.7) | — |
| [[RKO (line)]] | wt | 67.1 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 51.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +19.8) | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +28.6) | — |
| [[KATO III (line)]] | alt | 17.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +19.8) | — |
| [[LS 180 (line)]] | wt | 31.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +21.3) | — |
| [[SW480 (line)]] | alt | 41.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +18.4) | — |
| [[A498 (line)]] | wt | 64.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +23.6) | — |
| [[NCI-H2347 (line)]] | alt | 46.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +29.2) | — |
| [[A-172 (line)]] | wt | 49.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +21.8) | — |
| [[HS-578T (line)]] | alt | 39.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +17.9) | — |
| [[NCI-H460 (line)]] | wt | 37.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +17.4) | — |
| [[A549 (line)]] | wt | 60.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +23.1) | — |
| [[C32 (line)]] | wt | 18.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 36.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +29.8) | — |
| [[LoVo (line)]] | wt | 45.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +20.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +17.1) | — |
| [[SNU-423 (line)]] | alt | 24.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +23.1) | — |
| [[SW 900 (line)]] | alt | 25.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +18.7) | — |
| [[SW1417 (line)]] | alt | 60.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +22.8) | — |
| [[SW48 (line)]] | wt | 18.8 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +14.8) | [[Roxadustat (drug)]] 0.05 µM 0.106× (z -9.2) |
| [[A-427 (line)]] | wt | 29.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 15.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +16.7) | — |
| [[H4 (line)]] | wt | 14.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +14.3) | [[Temsirolimus (drug)]] 0.5 µM 0.124× (z -8.8) |
| [[HCT15 (line)]] | alt | 36.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 51.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +23.5) | — |
| [[J82 (line)]] | alt | 50.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +30.0) | — |
| [[Panc 03.27 (line)]] | alt | 72.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +23.1) | — |
| [[C-33 A (line)]] | alt | 25.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.1) | [[Harringtonine (drug)]] 0.05 µM 0.163× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.11× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 82.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +23.6) | — |
| [[SHP-77 (line)]] | alt | 47.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.2) | [[LJI308 (drug)]] 5 µM 0.127× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 24.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +10.7) | — |
| [[CHP-212 (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +16.1) | — |
| [[NCI-H661 (line)]] | alt | 62.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM1]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.61 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[HIVEP1]] | +0.60 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[ZNF702P]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SERTAD4]] | +0.58 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[LINC00944]] | +0.57 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[ARAP2]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[S100A4]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TSGA10]] | +0.57 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[RASGRF1]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[LINC02605]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA2]] | -0.59 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ST6GALNAC6]] | -0.56 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[TBC1D16]] | -0.55 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[ST6GALNAC4]] | -0.54 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[NFRKB]] | -0.53 | -0.55 / -0.25 | both halves | 4e-04 |  |
| [[MKRN2]] | -0.53 | -0.58 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TOMM70]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 | same gene group |
| [[HERC2P2]] | -0.53 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[GEMIN5]] | -0.53 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[SLC30A6]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SPATC1L]] | -0.52 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[WRN]] | -0.52 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[MRPL55]] | -0.52 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPAG1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.4, 11.0); signed map (44.4, -5.3). **Vector** length 90.9, 24.0% of its response variance represented; |z| ≥ 3 in 1,554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +7.2 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +7.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +6.9 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.6 | +13.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.6 | +15.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.3 | +14.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | +0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:100,157,906-100,259,278 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SP75, FLJ32920, HSD-3.8, TPIS, CT140, CILD28, DNAAF13 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Axonemal dynein assembly factors; R2SP complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07617](https://www.uniprot.org/uniprotkb/Q07617) (Sperm-associated antigen 1):

> May play a role in the cytoplasmic assembly of the ciliary dynein arms (By similarity). May play a role in fertilization. Binds GTP and has GTPase activity.

**Summary**, from NCBI Gene [6674](https://www.ncbi.nlm.nih.gov/gene/6674):

> The correlation of anti-sperm antibodies with cases of unexplained infertility implicates a role for these antibodies in blocking fertilization. Improved diagnosis and treatment of immunologic infertility, as well as identification of proteins for targeted contraception, are dependent on the identification and characterization of relevant sperm antigens. The protein expressed by this gene is recognized by anti-sperm agglutinating antibodies from an infertile woman. Furthermore, immunization of …

**Accessions** — [HGNC:11212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11212) · Entrez [6674](https://www.ncbi.nlm.nih.gov/gene/6674) · UniProt [Q07617](https://www.uniprot.org/uniprotkb/Q07617) · Ensembl [ENSG00000104450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104450)

## Data

Gene col 2464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2464); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2464]; `tensor/DDL_lfc|DDL_z.npy` [2464]; `embed/gene_vectors.npy` [2464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2464 or target_col == 2464). Every well: [[SPAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
