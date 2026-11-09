---
symbol: "STOX2"
type: "gene"
col: 10372
ensembl_id: "ENSG00000173320"
name: "storkhead box 2"
location: "4q35.1"
module: 82
arm: "+"
pooled_cpm: 37.96
n_lines_expressing: 28
n_dd_up: 13
n_dd_down: 26
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 24
direction_downstream: 15
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# STOX2

*storkhead box 2* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +16.8, q 0e+00, up in 21 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.419× (z -14.7, q 0e+00, down in 18 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.566× (z -10.1, q 1e-21, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAO1]] (+0.63, fdr 1e-05), [[RAB6B]] (+0.61, fdr 1e-05), [[SCN8A]] (+0.60, fdr 1e-05); moves opposite to [[SLC35B3]] (-0.49, fdr 7e-05), [[AMY2B]] (-0.45, fdr 3e-04), [[TMEM260]] (-0.45, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[MAPT]] → it (grade B ⚠); 15 go from it, the strongest it → [[SNX10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +16.8 | 0e+00 | 21/26 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +11.2 | 9e-27 | 22/26 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +11.2 | 9e-27 | 22/26 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +7.8 | 8e-13 | 15/26 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +7.2 | 6e-11 | 16/27 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.2 | 7e-11 | 14/26 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.41×** | +5.7 | 1e-06 | 10/26 (J82, NCI-H1792, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 1e-06 | 15/26 (HOP62, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +5.2 | 1e-05 | 12/26 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +4.8 | 9e-05 | 15/26 (PANC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.4 | 6e-04 | 10/26 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.011 | 8/26 (H4, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.028 | 5/26 (SW 900, HCT15, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.053 | 5/27 (HOP62, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.070 | 10/26 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.079 | 7/26 (NCI-H1573, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.419×** | -14.7 | 0e+00 | 18/23 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.481×** | -12.9 | 1e-35 | 22/26 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.483×** | -12.8 | 2e-35 | 21/26 (SK-MEL-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -10.1 | 1e-21 | 21/26 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -8.8 | 1e-16 | 21/26 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.609×** | -8.7 | 2e-16 | 16/26 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.614×** | -8.6 | 7e-16 | 22/26 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.626×** | -8.0 | 1e-13 | 14/26 (LoVo, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.634×** | -7.4 | 7e-12 | 20/24 (Panc 03.27, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.662×** | -7.3 | 2e-11 | 20/26 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.672×** | -7.0 | 1e-10 | 20/26 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -6.6 | 2e-09 | 18/27 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.690×** | -6.5 | 3e-09 | 15/26 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.684×** | -6.4 | 5e-09 | 19/25 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.713×** | -6.0 | 9e-08 | 17/26 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.688×** | -3.4 | 0.017 | 12/26 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.019 | 6/26 (HOP62, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.020 | 15/26 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.819×** | -3.3 | 0.029 | 12/26 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.713×** | -3.1 | 0.045 | 7/26 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.790×** | -3.0 | 0.069 | 6/26 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.797×** | -2.9 | 0.092 | 12/25 (C32, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 60.0 | 3 | 9 (8 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.439× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 46.1 | 1 (1 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.0773× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.0) |
| [[C32 (line)]] | wt | 77.3 | 1 (1 ⚠) | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 19.7× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.176× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 7 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 58.6 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0599× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 169 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -26.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0825× (z -25.3) |
| [[A498 (line)]] | wt | 172 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.373× (z -10.5) |
| [[HOP62 (line)]] | alt | 15.4 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.51× (z +13.9) | — |
| [[LoVo (line)]] | wt | 34.7 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0808× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 93.6 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 142 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -27.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -16.1) |
| [[SW480 (line)]] | alt | 43.1 | 1 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 32.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 47.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.5) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.191× (z -11.0) |
| [[J82 (line)]] | alt | 32.2 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.40× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.230× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 66.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 35.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -10.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 17.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.34× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.174× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 14.7 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.49× (z +11.1) | — |
| [[CHP-212 (line)]] | wt | 71.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.204× (z -8.8) |
| [[AN3 CA (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAO1]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SCN8A]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MAP6]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD6]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[KIF1A]] | +0.55 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[GRID1]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[JAKMIP1]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PRKD1]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35B3]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[AMY2B]] | -0.45 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[TMEM260]] | -0.45 | -0.32 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 10, C 14. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPT]] | B | MAPT activity raises STOX2's level | lines that do not express MAPT (10) vs lines expressing it (40) | 5.07× lower at baseline in the lines without MAPT | 0.023 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1 |
| [[SNX10]] | B | SNX10 activity raises STOX2's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 3.31× lower at baseline in the lines without SNX10 | 0.032 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[ARHGAP44]] | B | ARHGAP44 activity raises STOX2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without ARHGAP44 | 0.038 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[SLAIN1]] | B | SLAIN1 activity raises STOX2's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.74× lower at baseline in the lines without SLAIN1 | 0.039 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[CELSR1]] | B | CELSR1 activity raises STOX2's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 4.81× lower at baseline in the lines without CELSR1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[KIAA0319]] | B | KIAA0319 activity raises STOX2's level | lines that do not express KIAA0319 (19) vs lines expressing it (31) | 1.98× lower at baseline in the lines without KIAA0319 | 0.078 | ⚠ within organs, on part of the lines; also absent: ANKRD20A21P, DOCK3, ARHGAP8 |
| [[EBF2]] | B | EBF2 activity raises STOX2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without EBF2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[RIMS3]] | B | RIMS3 activity raises STOX2's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.69× lower at baseline in the lines without RIMS3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers STOX2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers STOX2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM124A]] | C | FAM124A activity raises STOX2's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 4.91× lower at baseline in the lines without FAM124A | 3e-04 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[RAB6B]] | C | RAB6B activity raises STOX2's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 5.95× lower at baseline in the lines without RAB6B | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX10]] | B | STOX2 activity raises SNX10's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without STOX2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[CELSR1]] | B | STOX2 activity raises CELSR1's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without STOX2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[MAPT]] | B | STOX2 activity raises MAPT's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without STOX2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[DBNDD1]] | B | STOX2 activity raises DBNDD1's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without STOX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[MCF2L2]] | B | STOX2 activity raises MCF2L2's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without STOX2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[RASGEF1C]] | C | STOX2 activity raises RASGEF1C's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.29× lower at baseline in the lines without STOX2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[FAM124A]] | C | STOX2 activity raises FAM124A's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without STOX2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[TCF7L1]] | C | STOX2 activity raises TCF7L1's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.98× lower at baseline in the lines without STOX2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[RAB6B]] | C | STOX2 activity raises RAB6B's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without STOX2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[WIPF3]] | C | STOX2 activity raises WIPF3's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without STOX2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[MAP3K15]] | C | STOX2 activity raises MAP3K15's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.42× lower at baseline in the lines without STOX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[ANKRD6]] | C | STOX2 activity raises ANKRD6's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 3.18× lower at baseline in the lines without STOX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.8, 39.9); signed map (26.7, 29.1). **Vector** length 86.7, 24.7% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +16.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +11.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +5.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +5.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -10.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.8 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.6 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | storkhead box 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:183,797,692-184,023,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762K222 |
| Gene groups (HGNC) | Storkhead boxes |
| Matched by | ensembl_id |

UniProt [Q9P2F5](https://www.uniprot.org/uniprotkb/Q9P2F5) carries no function annotation.

**Summary**, from NCBI Gene [56977](https://www.ncbi.nlm.nih.gov/gene/56977):

> This gene encodes a Storkhead-box_winged-helix domain containing protein. This protein is differentially expressed in decidual tissue and may be involved in the susceptibility to pre-eclampsia with fetal growth restriction. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:25450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25450) · Entrez [56977](https://www.ncbi.nlm.nih.gov/gene/56977) · UniProt [Q9P2F5](https://www.uniprot.org/uniprotkb/Q9P2F5) · Ensembl [ENSG00000173320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173320)

## Data

Gene col 10372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10372); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10372]; `tensor/DDL_lfc|DDL_z.npy` [10372]; `embed/gene_vectors.npy` [10372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10372 or target_col == 10372). Every well: [[STOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
