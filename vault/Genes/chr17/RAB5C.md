---
symbol: "RAB5C"
type: "gene"
col: 2992
ensembl_id: "ENSG00000108774"
name: "RAB5C, member RAS oncogene family"
location: "17q21.2"
module: 50
arm: "+"
pooled_cpm: 63.41
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# RAB5C

*RAB5C, member RAS oncogene family* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +17.6, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.64× (z +12.2, q 5e-32, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.563×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLPTM1]] (+0.68, fdr 1e-05), [[MAN2B2]] (+0.67, fdr 7e-06), [[MTPN]] (+0.67, fdr 7e-06); moves opposite to [[SEPSECS]] (-0.67, fdr 7e-06), [[NFYB]] (-0.63, fdr 1e-05), [[ZC3H6]] (-0.63, fdr 9e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.65×** | +17.6 | 0e+00 | 46/49 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.36×** | +14.9 | 0e+00 | 37/42 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.09×** | +13.2 | 1e-37 | 48/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.64×** | +12.2 | 5e-32 | 47/49 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.96×** | +12.1 | 1e-31 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.89×** | +11.4 | 3e-28 | 46/48 (LoVo, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +9.3 | 2e-18 | 43/48 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.64×** | +8.9 | 4e-17 | 39/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +8.5 | 1e-15 | 36/48 (LS 180, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.54×** | +7.7 | 6e-13 | 40/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.79×** | +7.6 | 2e-12 | 38/45 (HOP62, A498, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +6.7 | 1e-09 | 31/49 (A498, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +6.5 | 3e-09 | 39/48 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.43×** | +6.4 | 6e-09 | 33/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +5.7 | 6e-07 | 32/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 1e-06 | 38/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 1e-04 | 32/48 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.004 | 22/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.015 | 17/48 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.017 | 15/48 (RPMI-7951, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.034 | 15/48 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.041 | 15/48 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.076 | 14/47 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2992.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.563×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -4.3 | 0.008 | 17/48 (CHP-212, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.826× | -3.5 | 0.15 | 19/48 (hTERT-HPNE, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 58.8 | 9 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +11.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.74× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 53.8 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 51.9 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.57× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 94.1 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 45.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[A549 (line)]] | wt | 68.1 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 67.7 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +13.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 54.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.23× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 73.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 51.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 44.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 60.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.59× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 60.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.50× (z +8.6) | — |
| [[A498 (line)]] | wt | 82.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C32 (line)]] | wt | 55.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[COLO 205 (line)]] | alt | 68.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 81.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 74.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 45.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 59.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.24× (z +8.5) | — |
| [[A-172 (line)]] | wt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 70.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Hs 766T (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 63.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 84.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 59.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-1 (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 46.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPTM1]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MTPN]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[GNPTG]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NOMO1]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CAPZB]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ILRUN]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.63 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[EPN1]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 | pathway: Clathrin-mediated endocytosis |
| [[AP2A1]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 | pathway: Clathrin-mediated endocytosis; STRING 562 |
| [[GLB1]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPSECS]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NFYB]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.63 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[PBDC1]] | -0.60 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ARL14EP]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[APLF]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TMA16]] | -0.55 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[ZNF330]] | -0.54 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[GCFC2]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[WDR75]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PIM3]] | -0.52 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, -17.5); signed map (-49.6, -9.5). **Vector** length 90.8, 26.1% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +12.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.4 | +13.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.1 | +12.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.0 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +9.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +5.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.9 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB5C, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,124,978-42,155,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAB5CL; previously RABL |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 14 pathways, smallest: Respiratory syncytial virus (RSV) attachment and entry; TBC/RABGAPs; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P51148](https://www.uniprot.org/uniprotkb/P51148) (Ras-related protein Rab-5C):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. Involved in early endocytic trafficking. Required for EEA1 recruitment to early endosomes. Required for EGF and …

**Summary**, from NCBI Gene [5878](https://www.ncbi.nlm.nih.gov/gene/5878):

> Members of the Rab protein family are small GTPases of the Ras superfamily that are thought to ensure fidelity in the process of docking and/or fusion of vesicles with their correct acceptor compartment (Han et al., 1996 [PubMed 8646882]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:9785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9785) · Entrez [5878](https://www.ncbi.nlm.nih.gov/gene/5878) · UniProt [P51148](https://www.uniprot.org/uniprotkb/P51148) · Ensembl [ENSG00000108774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108774)

## Data

Gene col 2992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2992); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2992]; `tensor/DDL_lfc|DDL_z.npy` [2992]; `embed/gene_vectors.npy` [2992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2992 or target_col == 2992). Every well: [[RAB5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
