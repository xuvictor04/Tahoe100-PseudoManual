---
symbol: "GTF3C2"
type: "gene"
col: 3633
ensembl_id: "ENSG00000115207"
name: "general transcription factor IIIC subunit 2"
location: "2p23.3"
module: 36
arm: "+"
pooled_cpm: 45.05
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# GTF3C2

*general transcription factor IIIC subunit 2* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 2.63× (z +11.2, q 3e-26, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 2 lines (PANC-1 5.71×, SW480 3.27×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.437× (z -17.5, q 0e+00, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.588× (z -16.5, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP1]] (+0.74, fdr 7e-06), [[MED9]] (+0.72, fdr 7e-06), [[NUP160]] (+0.72, fdr 7e-06); moves opposite to [[SDCBP]] (-0.61, fdr 1e-05), [[YWHAZ]] (-0.60, fdr 4e-05), [[GLS]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3633.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 2 lines (PANC-1 5.71×, SW480 3.27×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +11.2 | 3e-26 | 37/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +9.9 | 1e-20 | 36/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.7 | 0.038 | 0/49 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.27 | 11/48 (HCT15, NCI-H460, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -17.5 | 0e+00 | 36/42 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.588×** | -16.5 | 0e+00 | 40/48 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.482×** | -16.0 | 0e+00 | 39/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -13.6 | 3e-40 | 41/48 (SNU-1, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.523×** | -13.2 | 1e-37 | 34/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -11.3 | 1e-27 | 38/49 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.599×** | -10.8 | 2e-25 | 42/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -9.6 | 9e-20 | 41/48 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -9.5 | 2e-19 | 37/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -8.4 | 3e-15 | 35/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.691×** | -8.1 | 3e-14 | 43/48 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -7.9 | 2e-13 | 35/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.709×** | -7.5 | 2e-12 | 29/48 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.712×** | -7.5 | 3e-12 | 35/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.715×** | -7.4 | 6e-12 | 30/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.727×** | -7.0 | 9e-11 | 32/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -6.1 | 3e-08 | 24/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.811×** | -4.3 | 6e-04 | 19/47 (AN3 CA, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.741×** | -3.4 | 0.016 | 10/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.860× | -3.3 | 0.025 | 17/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -3.2 | 0.033 | 14/48 (A-172, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 58.9 | 1 | 8 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.27× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.8) |
| [[PANC-1 (line)]] | alt | 53.7 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.71× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.391× (z -11.1) |
| [[A-172 (line)]] | wt | 36.8 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 55.0 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.4) |
| [[SW1417 (line)]] | alt | 63.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 40.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 47.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.6) |
| [[SW 900 (line)]] | alt | 47.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.5) |
| [[A-427 (line)]] | wt | 78.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 34.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 45.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.9) |
| [[A498 (line)]] | wt | 46.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -9.4) |
| [[A549 (line)]] | wt | 50.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.2) |
| [[C32 (line)]] | wt | 34.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.6) |
| [[HOP62 (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -12.2) |
| [[KATO III (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0648× (z -26.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 33.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 37.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 70.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 40.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 54.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.4) |
| [[SHP-77 (line)]] | alt | 56.7 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.409× (z -9.2) |
| [[SNU-1 (line)]] | wt | 48.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -17.0) |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.1) |
| [[SW48 (line)]] | wt | 49.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -11.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.0) |
| [[LS 180 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -13.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP1]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[MED9]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[NUP160]] | +0.72 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[PARGP1]] | +0.72 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[DDX55]] | +0.72 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CCDC12]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ZNF16]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TYW1]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TAF6L]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TIMM23]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.60 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[GLS]] | -0.59 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[JUN]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[PEAK1]] | -0.56 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.2, -6.9); signed map (-16.4, -19.5). **Vector** length 102, 26.5% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.5 | +9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.8 | +11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.2 | +1.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -16.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIC subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,325,849-27,356,999 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0011, TFIIIC110 |
| Gene groups (HGNC) | WD repeat domain containing; General transcription factor IIIC complex subunits |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUA4](https://www.uniprot.org/uniprotkb/Q8WUA4) (General transcription factor 3C polypeptide 2):

> Required for RNA polymerase III-mediated transcription. Component of TFIIIC that initiates transcription complex assembly on tRNA and is required for transcription of 5S rRNA and other stable nuclear and cytoplasmic RNAs. May play a direct role in stabilizing interactions of TFIIIC2 with TFIIIC1.

**Summary**, from NCBI Gene [2976](https://www.ncbi.nlm.nih.gov/gene/2976):

> Enables RNA polymerase III general transcription initiation factor activity. Contributes to DNA binding activity. Involved in transcription initiation at RNA polymerase III promoter. Located in nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4665) · Entrez [2976](https://www.ncbi.nlm.nih.gov/gene/2976) · UniProt [Q8WUA4](https://www.uniprot.org/uniprotkb/Q8WUA4) · Ensembl [ENSG00000115207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115207)

## Data

Gene col 3633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3633); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3633]; `tensor/DDL_lfc|DDL_z.npy` [3633]; `embed/gene_vectors.npy` [3633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3633 or target_col == 3633). Every well: [[GTF3C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
