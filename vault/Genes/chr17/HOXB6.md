---
symbol: "HOXB6"
type: "gene"
col: 2958
ensembl_id: "ENSG00000108511"
name: "homeobox B6"
location: "17q21.32"
module: 201
arm: "+"
pooled_cpm: 38.63
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXB6

*homeobox B6* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +13.2, q 7e-37, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.364× (z -25.0, q 0e+00, down in 33 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB5]] (+0.86, fdr 7e-06, ⚠ same locus), [[HOXB3]] (+0.85, fdr 7e-06, ⚠ same locus), [[HOXB-AS3]] (+0.75, fdr 7e-06, ⚠ same locus), [[HOXA3]] (+0.65, fdr 1e-05), [[ZNF224]] (+0.64, fdr 7e-06), [[AGAP3]] (+0.63, fdr 7e-06); moves opposite to [[SETX]] (-0.57, fdr 1e-05), [[TTPAL]] (-0.56, fdr 9e-06), [[NEK1]] (-0.55, fdr 3e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01232]] → it (grade B ⚠); 8 go from it, the strongest it → [[NDUFAF7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +13.2 | 7e-37 | 29/37 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +9.4 | 1e-18 | 24/37 (NCI-H2347, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +6.4 | 3e-08 | 26/37 (PANC-1, C32, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.9 | 5e-07 | 23/37 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 2e-06 | 19/37 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.2 | 2e-05 | 16/36 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.002 | 11/37 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.005 | 16/36 (SW1417, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.005 | 15/37 (AsPC-1, HT-29, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.005 | 12/37 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.005 | 12/37 (COLO 205, H4, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +3.7 | 0.011 | 10/37 (NCI-H2347, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.016 | 15/37 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.042 | 12/37 (PANC-1, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.042 | 7/37 (AsPC-1, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.2 | 0.045 | 15/37 (A-172, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.049 | 11/37 (NCI-H2347, J82, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.364×** | -25.0 | 0e+00 | 33/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.381×** | -16.9 | 0e+00 | 35/37 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -16.0 | 0e+00 | 35/37 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.354×** | -15.8 | 0e+00 | 32/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.501×** | -11.6 | 3e-29 | 30/37 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -9.5 | 3e-19 | 25/37 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.610×** | -8.6 | 4e-16 | 26/37 (SW480, PANC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -7.4 | 8e-12 | 9/37 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.672×** | -6.9 | 2e-10 | 22/37 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.727×** | -5.6 | 1e-06 | 19/37 (NCI-H460, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.552×** | -5.2 | 1e-05 | 18/37 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -4.9 | 5e-05 | 17/37 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.761×** | -4.8 | 8e-05 | 19/37 (HCT15, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.600×** | -4.5 | 3e-04 | 14/37 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.005 | 14/37 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.824×** | -3.4 | 0.021 | 14/37 (HCT15, HT-29, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.023 | 7/37 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.834× | -3.2 | 0.041 | 10/37 (SW480, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.842× | -3.0 | 0.070 | 16/37 (HCT15, HT-29, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.838× | -3.0 | 0.073 | 13/37 (MIA PaCa-2, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 105 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -27.3) |
| [[NCI-H460 (line)]] | wt | 28.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.6) |
| [[PANC-1 (line)]] | alt | 91.8 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.182× (z -21.4) |
| [[LoVo (line)]] | wt | 119 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.7) |
| [[A-172 (line)]] | wt | 49.6 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -23.0) |
| [[HT-29 (line)]] | alt | 112 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -17.9) |
| [[SW48 (line)]] | wt | 74.8 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.5) |
| [[C32 (line)]] | wt | 37.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -17.3) |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.8) |
| [[A498 (line)]] | wt | 17.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.5) |
| [[A549 (line)]] | wt | 19.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.9) |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -21.2) |
| [[HCT15 (line)]] | alt | 107 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.282× (z -9.8) |
| [[SW1417 (line)]] | alt | 151 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 22.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.9) |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 19.2 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.56× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.1) |
| [[H4 (line)]] | wt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0891× (z -9.3) |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.9) |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.8) |
| [[A-427 (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB5]] | +0.86 | +0.84 / +0.82 | both halves | 7e-06 | same gene group; STRING 982; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB3]] | +0.85 | +0.81 / +0.83 | both halves | 7e-06 | same gene group; STRING 836; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB-AS3]] | +0.75 | +0.63 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXB4]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 | same gene group; STRING 915; ⚠ same locus (17.4 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB8]] | +0.69 | +0.58 / +0.59 | both halves | 7e-06 | same gene group; STRING 887; ⚠ same locus (6.4 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA3]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 | same gene group; STRING 465 |
| [[ZNF224]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HOXB7]] | +0.63 | +0.52 / +0.55 | both halves | 1e-05 | same gene group; STRING 983; ⚠ same locus (2.2 kb, same strand: neighbours can correlate without regulation) |
| [[AGAP3]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TIAL1]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GPBP1L1]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[HOXC9]] | +0.59 | +0.35 / +0.57 | both halves | 1e-04 | same gene group; STRING 630 |
| [[BMPR1A]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MIRLET7BHG]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RSBN1L]] | +0.58 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.58 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[ASB7]] | +0.57 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[HOTAIR]] | +0.57 | +0.34 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.56 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[NEK1]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ETS1]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[HUS1]] | -0.52 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[EFL1]] | -0.50 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[DNAJB5]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ASAP1]] | -0.50 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NELFE]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TMEM185B]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01232]] | B | LINC01232 activity raises HOXB6's level | lines that do not express LINC01232 (11) vs lines expressing it (39) | 2.52× lower at baseline in the lines without LINC01232 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000286856, SERPINB1; maybe low, not absent |
| [[HOXB3]] | C | HOXB3 activity raises HOXB6's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 4.73× lower at baseline in the lines without HOXB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: HOXB6; co-absent with the target |
| [[HOXB8]] | C | HOXB8 activity raises HOXB6's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 3.51× lower at baseline in the lines without HOXB8 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFAF7]] | B | [[HOXB5]], HOXB6 activity lowers NDUFAF7's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.12× higher at baseline in the lines without HOXB5, HOXB6 | 0.060 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[SMAD5]] | B | [[HOXB5]], HOXB6 activity lowers SMAD5's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.31× higher at baseline in the lines without HOXB5, HOXB6 | 0.063 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[LAMTOR5-AS1]] | B | HOXB6 activity lowers LAMTOR5-AS1's level | lines that do not express HOXB6 (11) vs lines expressing it (39) | 1.44× higher at baseline in the lines without HOXB6 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HOXB3, HOXB8 |
| [[SLC16A4-AS1]] | B | HOXB6 activity lowers SLC16A4-AS1's level | lines that do not express HOXB6 (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without HOXB6 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; also absent: HOXB3, HOXB8 |
| [[HOXB-AS3]] | B | [[HOXB5]], HOXB6 activity raises HOXB-AS3's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.59× lower at baseline in the lines without HOXB5, HOXB6 | 0.093 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[TTPAL]] | B | [[HOXB5]], HOXB6 activity lowers TTPAL's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.24× higher at baseline in the lines without HOXB5, HOXB6 | 0.097 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[HOXB3]] | C | [[HOXB5]], HOXB6 activity raises HOXB3's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 4.32× lower at baseline in the lines without HOXB5, HOXB6 | 0.008 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent with the target; co-absent genes |
| [[HOXB8]] | C | [[HOXB5]], HOXB6 activity raises HOXB8's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 2.35× lower at baseline in the lines without HOXB5, HOXB6 | 0.021 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.817). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.0, 26.7); signed map (39.2, -4.1). **Vector** length 98.2, 24.6% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +13.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -15.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.2 | -16.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -16.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -25.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -11.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -6.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,595,751-48,604,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2B |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P17509](https://www.uniprot.org/uniprotkb/P17509) (Homeobox protein Hox-B6):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3216](https://www.ncbi.nlm.nih.gov/gene/3216):

> This gene is a member of the Antp homeobox family and encodes a protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded protein functions as a sequence-specific transcription factor that is involved in development, including that of lung and skin, and has been localized to both the nucleus and cytoplasm. Altered expression of this gene or a change in the subcellular localization of its protein is associated with some …

**Accessions** — [HGNC:5117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5117) · Entrez [3216](https://www.ncbi.nlm.nih.gov/gene/3216) · UniProt [P17509](https://www.uniprot.org/uniprotkb/P17509) · Ensembl [ENSG00000108511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108511)

## Data

Gene col 2958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2958); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2958]; `tensor/DDL_lfc|DDL_z.npy` [2958]; `embed/gene_vectors.npy` [2958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2958 or target_col == 2958). Every well: [[HOXB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
