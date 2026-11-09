---
symbol: "AXIN1"
type: "gene"
col: 2322
ensembl_id: "ENSG00000103126"
name: "axin 1"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 52.31
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# AXIN1

*axin 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +7.4, q 9e-11, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.501× (z -15.5, q 0e+00, down in 28 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.597× (z -11.6, q 1e-28, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO7]] (+0.69, fdr 7e-06), [[ZMYND19]] (+0.67, fdr 7e-06), [[ESRRA]] (+0.67, fdr 1e-05); moves opposite to [[NDUFA5]] (-0.68, fdr 7e-06), [[CFL2]] (-0.68, fdr 7e-06), [[ATP6V1A]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF816-ZNF321P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +7.4 | 9e-11 | 23/48 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.9 | 3e-04 | 15/49 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.20×** | +4.3 | 0.004 | 18/47 (NCI-H1573, C32, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.010 | 18/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.017 | 17/48 (AsPC-1, SW480, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.7 | 0.020 | 13/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.7 | 0.020 | 14/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.029 | 18/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.066 | 5/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +3.2 | 0.066 | 4/48 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.066 | 13/48 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.074 | 16/48 (AsPC-1, SW480, …) | two highest doses | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.074 | 4/47 (A-427, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.098 | 7/48 (SW 1088, HEC-1-A, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -15.5 | 0e+00 | 28/41 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.552×** | -13.8 | 5e-41 | 32/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -13.5 | 2e-39 | 33/44 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.597×** | -11.6 | 1e-28 | 37/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.763×** | -8.9 | 7e-17 | 30/48 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.767×** | -8.7 | 3e-16 | 29/48 (RKO, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -7.8 | 5e-13 | 31/48 (Panc 03.27, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.744×** | -6.6 | 3e-09 | 30/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.796×** | -5.3 | 7e-06 | 22/48 (AN3 CA, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.796×** | -5.3 | 7e-06 | 27/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.797×** | -5.3 | 8e-06 | 22/48 (A-172, RKO, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.799×** | -5.2 | 8e-06 | 21/49 (SW480, HT-29, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.786×** | -5.2 | 1e-05 | 20/48 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.855× | -5.1 | 2e-05 | 17/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.814×** | -4.8 | 7e-05 | 22/47 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.816×** | -4.7 | 9e-05 | 22/48 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.815×** | -4.6 | 1e-04 | 20/48 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.834× | -4.6 | 2e-04 | 22/48 (SHP-77, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.824×** | -4.5 | 2e-04 | 20/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 72.1 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 106 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.609× (z -8.7) |
| [[A549 (line)]] | wt | 59.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.2) |
| [[RKO (line)]] | wt | 64.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -11.0) |
| [[A-427 (line)]] | wt | 63.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.286× (z -17.8) |
| [[C-33 A (line)]] | alt | 77.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -15.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 53.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.386× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 64.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 52.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.426× (z -9.0) |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.328× (z -8.8) |
| [[LS 180 (line)]] | wt | 66.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.416× (z -9.2) |
| [[PANC-1 (line)]] | alt | 51.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 37.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -15.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0741× (z -23.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0421× (z -24.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 53.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0843× (z -17.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[Hs 766T (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 83.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 42.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -10.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 50.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.3) | — |
| [[SW480 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -13.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO7]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ESRRA]] | +0.67 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[KLF13]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[PITPNA]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[IL9RP3]] | +0.64 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[ZBED4]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CAPN10]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A19]] | +0.62 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[FBRSL1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[RAB11FIP3]] | +0.61 | +0.40 / +0.69 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.68 | -0.60 / -0.72 | both halves | 7e-06 |  |
| [[CFL2]] | -0.68 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ATP6V1A]] | -0.60 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[ZNF280D]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TAB2]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SYNJ2BP]] | -0.56 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[IFT81]] | -0.55 | -0.43 / -0.58 | both halves | 4e-05 | STRING 537 |
| [[FUBP1]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[BRINP3]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SH3BGRL]] | -0.55 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[MBTPS2]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[TSPAN6]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF816-ZNF321P]] | B | ZNF816-ZNF321P activity lowers AXIN1's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without ZNF816-ZNF321P | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[MAP2K1]] | B | MAP2K1 activity raises AXIN1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ATP10D]] | B | ATP10D activity lowers AXIN1's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 1.58× higher at baseline in the lines without ATP10D | 0.088 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.1, 1.8); signed map (-45.1, -1.4). **Vector** length 116, 30.7% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.6 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.5 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -11.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -8.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.4 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | axin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:287,440-352,723 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R49 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 28 pathways, smallest: RUNX1 regulates transcription of genes involved in WNT signaling; RUNX1 regulates estrogen receptor mediated transcription; APC truncation mutants have impaired AXIN binding |
| Matched by | ensembl_id |

**Function**, from UniProt [O15169](https://www.uniprot.org/uniprotkb/O15169) (Axin-1):

> Component of the beta-catenin destruction complex required for regulating CTNNB1 levels through phosphorylation and ubiquitination, and modulating Wnt-signaling. Controls dorsoventral patterning via two opposing effects; down-regulates CTNNB1 to inhibit the Wnt signaling pathway and ventralize embryos, but also dorsalizes embryos by activating a Wnt-independent JNK signaling pathway. In Wnt signaling, probably facilitates the phosphorylation of CTNNB1 and APC by GSK3B. Enhances TGF-beta …

**Summary**, from NCBI Gene [8312](https://www.ncbi.nlm.nih.gov/gene/8312):

> This gene encodes a cytoplasmic protein which contains a regulation of G-protein signaling (RGS) domain and a dishevelled and axin (DIX) domain. The encoded protein interacts with adenomatosis polyposis coli, catenin beta-1, glycogen synthase kinase 3 beta, protein phosphate 2, and itself. This protein functions as a negative regulator of the wingless-type MMTV integration site family, member 1 (WNT) signaling pathway and can induce apoptosis. The crystal structure of a portion of this protein, …

**Accessions** — [HGNC:903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:903) · Entrez [8312](https://www.ncbi.nlm.nih.gov/gene/8312) · UniProt [O15169](https://www.uniprot.org/uniprotkb/O15169) · Ensembl [ENSG00000103126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103126)

## Data

Gene col 2322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2322); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2322]; `tensor/DDL_lfc|DDL_z.npy` [2322]; `embed/gene_vectors.npy` [2322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2322 or target_col == 2322). Every well: [[AXIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AXIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
