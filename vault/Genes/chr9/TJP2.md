---
symbol: "TJP2"
type: "gene"
col: 4042
ensembl_id: "ENSG00000119139"
name: "tight junction protein 2"
location: "9q21.11"
module: 31
arm: "+"
pooled_cpm: 125.61
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 63
direction_downstream: 50
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TJP2

*tight junction protein 2* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.43× (z +13.4, q 3e-38, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.445× (z -23.3, q 0e+00, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB4]] (+0.69, fdr 7e-06), [[B3GNT3]] (+0.69, fdr 7e-06), [[MST1R]] (+0.67, fdr 7e-06); moves opposite to [[BRSK1]] (-0.54, fdr 4e-05), [[ST3GAL3]] (-0.51, fdr 1e-05), [[CNRIP1]] (-0.49, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); 50 go from it, the strongest it → [[BMP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.43×** | +13.4 | 3e-38 | 29/39 (PANC-1, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +12.2 | 1e-31 | 27/38 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +10.9 | 3e-25 | 24/37 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +10.3 | 1e-22 | 21/38 (HS-578T, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +7.0 | 4e-10 | 22/38 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +6.9 | 7e-10 | 16/38 (C32, CHP-212, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +6.8 | 1e-09 | 20/38 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.22×** | +5.5 | 2e-06 | 14/39 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.16× | +4.4 | 7e-04 | 18/38 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.13× | +3.6 | 0.018 | 10/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.018 | 14/38 (A498, C32, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.024 | 8/38 (SW 1088, SNU-1, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.038 | 17/38 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.041 | 7/38 (HS-578T, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.068 | 5/38 (HepG2/C3A, A498, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.069 | 5/38 (NCI-H460, CHP-212, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.445×** | -23.3 | 0e+00 | 32/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.464×** | -22.1 | 0e+00 | 30/38 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.523×** | -18.7 | 0e+00 | 23/38 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -16.3 | 0e+00 | 27/39 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -15.4 | 0e+00 | 28/37 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -12.5 | 5e-34 | 30/38 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.677×** | -11.2 | 2e-27 | 21/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -10.7 | 1e-24 | 21/33 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.587×** | -8.0 | 7e-14 | 23/38 (NCI-H2347, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.599×** | -7.7 | 7e-13 | 22/35 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.767×** | -7.6 | 2e-12 | 22/39 (SW480, HEC-1-A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.613×** | -7.4 | 9e-12 | 22/38 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.619×** | -7.2 | 2e-11 | 21/38 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.768×** | -7.2 | 3e-11 | 21/38 (NCI-H2347, HT-29, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.653×** | -6.4 | 6e-09 | 24/38 (LoVo, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.667×** | -6.1 | 4e-08 | 21/38 (Hs 766T, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.829×** | -5.4 | 2e-06 | 17/38 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -4.7 | 6e-05 | 13/38 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.743×** | -4.5 | 2e-04 | 14/38 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -4.3 | 3e-04 | 19/38 (AsPC-1, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 176 | 0 | 24 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -37.8) |
| [[LoVo (line)]] | wt | 205 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -31.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0963× (z -30.0) |
| [[HEC-1-A (line)]] | alt | 290 | 1 (1 ⚠) | 15 (7 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.68× (z +9.4) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -40.2) |
| [[HT-29 (line)]] | alt | 320 | 0 | 15 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.105× (z -21.8) |
| [[LS 180 (line)]] | wt | 243 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -26.6) |
| [[NCI-H2347 (line)]] | alt | 357 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0859× (z -31.4) |
| [[Panc 03.27 (line)]] | alt | 314 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -29.3) |
| [[SW1417 (line)]] | alt | 251 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -28.5) |
| [[AsPC-1 (line)]] | alt | 221 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -27.1) |
| [[C32 (line)]] | wt | 73.0 | 10 (4 ⚠) | 0 | [[Binimetinib (drug)]] 0.5 µM 3.30× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 337 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -26.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.166× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 95.4 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -24.0) |
| [[A-172 (line)]] | wt | 85.1 | 7 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +21.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.87× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HCT15 (line)]] | alt | 186 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -20.3) |
| [[KATO III (line)]] | alt | 269 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -24.1) |
| [[PANC-1 (line)]] | alt | 69.4 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +27.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.00× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 94.2 | 5 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +27.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.60× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.6) |
| [[Hs 766T (line)]] | wt | 80.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -14.5) |
| [[A498 (line)]] | wt | 133 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +18.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 137 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -10.2) |
| [[H4 (line)]] | wt | 73.7 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +15.2) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.6) |
| [[SW48 (line)]] | wt | 140 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 80.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.20× (z +20.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 53.4 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.47× (z +15.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +17.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +16.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 118 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +23.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.35× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 85.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 129 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -9.7) |
| [[J82 (line)]] | alt | 46.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -8.9) |
| [[SW 1271 (line)]] | alt | 160 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -12.0) |
| [[SW 900 (line)]] | alt | 83.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 65.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 81.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.6) |
| [[SNU-1 (line)]] | wt | 35.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.191× (z -9.7) |
| [[A-427 (line)]] | wt | 20.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB4]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[MST1R]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 | same gene group |
| [[GRB7]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ARHGEF16]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 | same gene group |
| [[INAVA]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ARHGEF3]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[SPINT1]] | +0.62 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[USP6NL]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[TCF7L2]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK1]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ST3GAL3]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CNRIP1]] | -0.49 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[APBA2]] | -0.48 | -0.31 / -0.43 | both halves | 2e-04 | same gene group |
| [[ZNF286A]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 63, C 0. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises TJP2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.10× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[MPZL2]] | B | MPZL2 activity raises TJP2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without MPZL2 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[C1orf116]] | B | C1orf116 activity raises TJP2's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.07× lower at baseline in the lines without C1orf116 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[ST14]] | B | ST14 activity raises TJP2's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.22× lower at baseline in the lines without ST14 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ITGB6]] | B | ITGB6 activity raises TJP2's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.10× lower at baseline in the lines without ITGB6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[HS3ST1]] | B | HS3ST1 activity raises TJP2's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.29× lower at baseline in the lines without HS3ST1 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[CLIC5]] | B | CLIC5 activity raises TJP2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.77× lower at baseline in the lines without CLIC5 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[INAVA]] | B | INAVA activity raises TJP2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without INAVA | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises TJP2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.80× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[B3GNT3]] | B | B3GNT3 activity raises TJP2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.42× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[C6orf132]] | B | C6orf132 activity raises TJP2's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.54× lower at baseline in the lines without C6orf132 | 0.003 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[KLK10]] | B | KLK10 activity raises TJP2's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.58× lower at baseline in the lines without KLK10 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 50, C 0. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP4]] | B | TJP2 activity raises BMP4's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.20× lower at baseline in the lines without TJP2 | 0.002 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ANXA11]] | B | TJP2 activity raises ANXA11's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without TJP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[C1orf116]] | B | TJP2 activity raises C1orf116's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.56× lower at baseline in the lines without TJP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[MPZL2]] | B | TJP2 activity raises MPZL2's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 4.29× lower at baseline in the lines without TJP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ANO9]] | B | TJP2 activity raises ANO9's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.87× lower at baseline in the lines without TJP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[SORL1]] | B | TJP2 activity raises SORL1's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.57× lower at baseline in the lines without TJP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[KLF3]] | B | TJP2 activity raises KLF3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without TJP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[JUP]] | B | TJP2 activity raises JUP's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TJP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ANXA3]] | B | TJP2 activity raises ANXA3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 4.01× lower at baseline in the lines without TJP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ST14]] | B | TJP2 activity raises ST14's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 4.48× lower at baseline in the lines without TJP2 | 0.014 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[TMC4]] | B | TJP2 activity raises TMC4's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TJP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[TC2N]] | B | TJP2 activity raises TC2N's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TJP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.1, 57.5); signed map (55.8, 9.7). **Vector** length 122, 36.9% of its response variance represented; |z| ≥ 3 in 1,471 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.5 | +10.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +3.2 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -12.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -7.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -4.4 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | tight junction protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:69,121,264-69,274,615 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZO-2, X104, ZO2; previously DFNA51 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Reactome | 12 pathways, smallest: Apoptotic cleavage of cell adhesion  proteins; Signaling by Hippo; Apoptotic cleavage of cellular proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDY2](https://www.uniprot.org/uniprotkb/Q9UDY2) (Tight junction protein 2):

> Plays a role in tight junctions and adherens junctions (By similarity). Acts as a positive regulator of RANKL-induced osteoclast differentiation, potentially via mediating downstream transcriptional activity (By similarity).

**Summary**, from NCBI Gene [9414](https://www.ncbi.nlm.nih.gov/gene/9414):

> This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb region including this gene causes autosomal dominant deafness-51. Alternatively spliced transcripts …

**Accessions** — [HGNC:11828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11828) · Entrez [9414](https://www.ncbi.nlm.nih.gov/gene/9414) · UniProt [Q9UDY2](https://www.uniprot.org/uniprotkb/Q9UDY2) · Ensembl [ENSG00000119139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119139)

## Data

Gene col 4042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4042); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4042]; `tensor/DDL_lfc|DDL_z.npy` [4042]; `embed/gene_vectors.npy` [4042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4042 or target_col == 4042). Every well: [[TJP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TJP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
