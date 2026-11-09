---
symbol: "KAT2B"
type: "gene"
col: 3530
ensembl_id: "ENSG00000114166"
name: "lysine acetyltransferase 2B"
location: "3p24.3"
module: 5
arm: "-"
pooled_cpm: 37.25
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 25
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KAT2B

*lysine acetyltransferase 2B* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +10.6, q 1e-23, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.482× (z -15.1, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC16]] (+0.56, fdr 3e-05), [[PCM1]] (+0.55, fdr 3e-05), [[ATOSA]] (+0.52, fdr 1e-05); moves opposite to [[RRP7A]] (-0.58, fdr 2e-05), [[POP1]] (-0.58, fdr 1e-05), [[NEIL2]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLCD4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +10.6 | 1e-23 | 36/47 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +9.0 | 8e-17 | 28/46 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.4 | 7e-15 | 26/46 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +7.1 | 2e-10 | 24/47 (J82, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.1 | 1e-07 | 18/43 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 8e-06 | 22/46 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.1 | 3e-05 | 15/36 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 4e-04 | 16/47 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 0.001 | 19/47 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.004 | 10/47 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.011 | 9/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.018 | 5/47 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.024 | 15/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.024 | 9/47 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.032 | 6/47 (A498, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.089 | 5/46 (BT-474, RPMI-7951, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.089 | 3/47 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.482×** | -15.1 | 0e+00 | 39/46 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.491×** | -14.6 | 1e-45 | 41/47 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.527×** | -13.3 | 5e-38 | 34/47 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.528×** | -13.3 | 5e-38 | 39/47 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.545×** | -12.4 | 2e-33 | 38/47 (A-172, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.561×** | -11.3 | 9e-28 | 34/47 (A549, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.677×** | -8.1 | 5e-14 | 25/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.508×** | -7.3 | 1e-11 | 27/40 (SNU-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.708×** | -7.2 | 5e-11 | 29/46 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.555×** | -6.4 | 9e-09 | 26/45 (NCI-H1792, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.806×** | -6.3 | 2e-08 | 23/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.560×** | -6.3 | 2e-08 | 22/46 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.561×** | -6.3 | 2e-08 | 20/47 (NCI-H1792, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.770×** | -5.4 | 2e-06 | 24/46 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.780×** | -5.1 | 1e-05 | 25/46 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -5.0 | 2e-05 | 19/46 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.808×** | -4.2 | 7e-04 | 13/47 (MIA PaCa-2, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 58.4 | 0 | 7 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -12.3) |
| [[A549 (line)]] | wt | 58.4 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.242× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 59.2 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -15.5) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 29.7 | 0 | 6 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.308× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 45.9 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.272× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 47.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 60.2 | 2 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.56× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -14.8) |
| [[A-427 (line)]] | wt | 63.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -16.9) |
| [[HOP62 (line)]] | alt | 36.3 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -12.2) |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -11.5) |
| [[LoVo (line)]] | wt | 30.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.377× (z -9.3) |
| [[LS 180 (line)]] | wt | 25.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 32.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.365× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 23.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.6) | [[Ixazomib citrate (drug)]] 5 µM 0.286× (z -11.5) |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0912× (z -10.6) |
| [[C32 (line)]] | wt | 78.0 | 1 | 1 | [[Binimetinib (drug)]] 0.05 µM 2.22× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.329× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 22.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.6) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.103× (z -8.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 15.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 37.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.312× (z -9.0) |
| [[SW480 (line)]] | alt | 28.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.311× (z -8.7) |
| [[H4 (line)]] | wt | 12.3 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0740× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.0) | — |
| [[J82 (line)]] | alt | 31.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 45.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.247× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.190× (z -10.1) |
| [[A498 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | +0.56 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[PCM1]] | +0.55 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[ATOSA]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SPAG1]] | +0.52 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[RCOR3]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SKA2]] | +0.51 | +0.48 / +0.40 | both halves | 4e-05 | same gene group |
| [[GNAS]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[ZBTB25]] | +0.50 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[PPM1D]] | +0.50 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TMX4]] | +0.49 | +0.32 / +0.42 | both halves | 2e-04 |  |
| [[RDX]] | +0.49 | +0.41 / +0.34 | both halves | 1e-04 |  |
| [[ZNF821]] | +0.49 | +0.53 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7A]] | -0.58 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[POP1]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NEIL2]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[NOP16]] | -0.55 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[DPH2]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[FLAD1]] | -0.53 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[CANT1]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[RRP7BP]] | -0.53 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MRPS23]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PDCD11]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ZNF496]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[NOL10]] | -0.51 | -0.49 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD4]] | B | TLCD4 activity raises KAT2B's level | lines that do not express TLCD4 (11) vs lines expressing it (39) | 1.50× lower at baseline in the lines without TLCD4 | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.367). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.7, -39.8); signed map (11.4, -15.3). **Vector** length 116, 30.9% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.1 | +10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.4 | +5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.3 | +4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.1 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.6 | -11.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.4 | -15.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -12.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -13.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -13.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.2 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:20,040,446-20,154,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P/CAF, GCN5, GCN5L; previously PCAF |
| Gene groups (HGNC) | Lysine acetyltransferases; ATAC complex; SAGA complex; GCN5 related N-acetyltransferases; Bromodomain containing; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 49 pathways, smallest: Physiological factors; Regulation of FOXO transcriptional activity by acetylation; YAP1- and WWTR1 (TAZ)-stimulated gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92831](https://www.uniprot.org/uniprotkb/Q92831) (Histone acetyltransferase KAT2B):

> Functions as a histone acetyltransferase (HAT) to promote transcriptional activation. Has significant histone acetyltransferase activity with core histones (H3 and H4), and also with nucleosome core particles. Has a a strong preference for acetylation of H3 at 'Lys-9' (H3K9ac). Also acetylates non-histone proteins, such as ACLY, MAPRE1/EB1, PLK4, RRP9/U3-55K and TBX5. Inhibits cell-cycle progression and counteracts the mitogenic activity of the adenoviral oncoprotein E1A. Acts as a circadian …

**Summary**, from NCBI Gene [8850](https://www.ncbi.nlm.nih.gov/gene/8850):

> CBP and p300 are large nuclear proteins that bind to many sequence-specific factors involved in cell growth and/or differentiation, including c-jun and the adenoviral oncoprotein E1A. The protein encoded by this gene associates with p300/CBP. It has in vitro and in vivo binding activity with CBP and p300, and competes with E1A for binding sites in p300/CBP. It has histone acetyl transferase activity with core histones and nucleosome core particles, indicating that this protein plays a direct …

**Accessions** — [HGNC:8638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8638) · Entrez [8850](https://www.ncbi.nlm.nih.gov/gene/8850) · UniProt [Q92831](https://www.uniprot.org/uniprotkb/Q92831) · Ensembl [ENSG00000114166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114166)

## Data

Gene col 3530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3530); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3530]; `tensor/DDL_lfc|DDL_z.npy` [3530]; `embed/gene_vectors.npy` [3530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3530 or target_col == 3530). Every well: [[KAT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
