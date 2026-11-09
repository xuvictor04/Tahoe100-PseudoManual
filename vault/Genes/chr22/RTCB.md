---
symbol: "RTCB"
type: "gene"
col: 1894
ensembl_id: "ENSG00000100220"
name: "RNA 2',3'-cyclic phosphate and 5'-OH ligase"
location: "22q12.3"
module: 49
arm: "+"
pooled_cpm: 56.16
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RTCB

*RNA 2',3'-cyclic phosphate and 5'-OH ligase* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.45× (z +15.8, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.732× (z -7.8, q 4e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG3]] (+0.66, fdr 1e-05), [[OSBP]] (+0.65, fdr 1e-05), [[CINP]] (+0.63, fdr 2e-05); moves opposite to [[SRSF5]] (-0.53, fdr 9e-05), [[M6PR]] (-0.53, fdr 3e-05), [[ZNF124]] (-0.52, fdr 3e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.45×** | +15.8 | 0e+00 | 47/49 (LoVo, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.79×** | +14.5 | 7e-45 | 41/48 (A549, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.87×** | +10.8 | 1e-24 | 41/48 (LoVo, RKO, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +10.5 | 1e-23 | 41/48 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.60×** | +8.4 | 4e-15 | 36/48 (BT-474, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +8.4 | 4e-15 | 39/48 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.59×** | +8.3 | 7e-15 | 35/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +8.2 | 2e-14 | 38/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +7.6 | 2e-12 | 34/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +7.6 | 2e-12 | 31/48 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +7.1 | 8e-11 | 40/48 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.7 | 1e-09 | 35/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.42×** | +6.3 | 1e-08 | 30/48 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.40×** | +5.8 | 3e-07 | 27/47 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +5.6 | 1e-06 | 29/49 (LS 180, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 25/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 4e-04 | 25/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.032 | 7/49 (HCT15, C32, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.032 | 11/48 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.032 | 16/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.060 | 15/48 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +2.9 | 0.075 | 7/49 (SNU-423, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +2.8 | 0.099 | 16/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -7.8 | 4e-12 | 33/48 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.060 | 16/48 (HCT15, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.822×** | -3.5 | 0.060 | 16/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.060 | 15/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.824×** | -3.5 | 0.060 | 19/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.11 | 10/48 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.832× | -3.2 | 0.11 | 20/42 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.838× | -3.2 | 0.11 | 11/48 (RKO, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.1 | 0.14 | 13/48 (A498, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 44.6 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 8.64× (z +10.1) | — |
| [[LoVo (line)]] | wt | 65.3 | 5 (3 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -8.6) |
| [[A498 (line)]] | wt | 108 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -14.8) |
| [[PANC-1 (line)]] | alt | 40.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.42× (z +9.9) | — |
| [[RKO (line)]] | wt | 65.2 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +15.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.90× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 57.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +14.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 8.57× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 88.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 37.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.28× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 48.6 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.43× (z +11.1) | — |
| [[SW48 (line)]] | wt | 85.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +15.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +11.0) | — |
| [[SW480 (line)]] | alt | 84.1 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.97× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.0) |
| [[A-172 (line)]] | wt | 32.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.4) | — |
| [[A549 (line)]] | wt | 53.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +16.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 54.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 33.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.30× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 70.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.5) |
| [[HT-29 (line)]] | alt | 38.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.20× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 64.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.9× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 40.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.17× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 54.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.11× (z +8.8) | — |
| [[NCI-H596 (line)]] | alt | 59.7 | 1 (1 ⚠) | 1 | [[Trametinib (drug)]] 5 µM 3.06× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.288× (z -10.6) |
| [[SNU-1 (line)]] | wt | 74.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.79× (z +8.5) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.121× (z -8.7) ⚠ toxic |
| [[C32 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 55.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.135× (z -8.9) |
| [[HS-578T (line)]] | alt | 97.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.31× (z +10.5) | — |
| [[J82 (line)]] | alt | 44.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -8.8) |
| [[KATO III (line)]] | alt | 67.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2030 (line)]] | alt | 57.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H661 (line)]] | alt | 56.5 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.105× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG3]] | +0.66 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[OSBP]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[CINP]] | +0.63 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PRPF6]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 | STRING 565 |
| [[ARL1]] | +0.62 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[MED8]] | +0.61 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[YTHDF1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GORASP2]] | +0.61 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[MPHOSPH10]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ERLEC1]] | +0.60 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RARS1]] | +0.60 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[KLHL20]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF5]] | -0.53 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[M6PR]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ZNF124]] | -0.52 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[PRRC2B]] | -0.50 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[CERS2]] | -0.50 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.1, -54.9); signed map (-52.4, 13.7). **Vector** length 90.3, 24.5% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +15.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.0 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +8.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +2.8 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +10.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.3 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.8 | +8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA 2',3'-cyclic phosphate and 5'-OH ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:32,387,582-32,412,248 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSLIG5, HSPC117, FAAP; previously C22orf28 |
| Gene groups (HGNC) | tRNA splicing ligase complex; RNA ligases |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3I0](https://www.uniprot.org/uniprotkb/Q9Y3I0) (RNA-splicing ligase RTCB):

> 3'-5' RNA ligase, catalytic subunit of the tRNA-splicing ligase complex (tRNA-LC), which is involved in the enzyme-dependent maturation of intron-containing pre-tRNAs. Functions downstream of the tRNA-splicing endonuclease that removes introns, ligating the two generated halves via phosphodiester bond formation. The ligation reaction, which requires guanosine triphosphate (GTP) and Mn(2+), proceeds through three metal-dependent steps. The first step requires TSLIG1 and involves the …

**Summary**, from NCBI Gene [51493](https://www.ncbi.nlm.nih.gov/gene/51493):

> Enables vinculin binding activity. Contributes to RNA ligase (GTP) activity and protein guanylyltransferase activity. Involved in IRE1-mediated unfolded protein response; mRNA splicing, via endonucleolytic cleavage and ligation; and tRNA exon ligation. Located in cytosol and nucleoplasm. Part of tRNA-splicing ligase complex. Is active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26935) · Entrez [51493](https://www.ncbi.nlm.nih.gov/gene/51493) · UniProt [Q9Y3I0](https://www.uniprot.org/uniprotkb/Q9Y3I0) · Ensembl [ENSG00000100220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100220)

## Data

Gene col 1894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1894); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1894]; `tensor/DDL_lfc|DDL_z.npy` [1894]; `embed/gene_vectors.npy` [1894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1894 or target_col == 1894). Every well: [[RTCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
