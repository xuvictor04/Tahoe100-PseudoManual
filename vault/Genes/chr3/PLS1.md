---
symbol: "PLS1"
type: "gene"
col: 4219
ensembl_id: "ENSG00000120756"
name: "plastin 1"
location: "3q23"
module: 55
arm: "+"
pooled_cpm: 60.71
n_lines_expressing: 36
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 44
direction_downstream: 15
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# PLS1

*plastin 1* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.53× (z +22.3, q 0e+00, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.731× (z -10.6, q 2e-23, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD22]] (+0.66, fdr 7e-06), [[CDH17]] (+0.61, fdr 1e-05), [[ILDR2]] (+0.61, fdr 9e-06); moves opposite to [[WDR81]] (-0.63, fdr 1e-05), [[LRRC41]] (-0.57, fdr 1e-04), [[ZNF785]] (-0.56, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[TJP3]] → it (grade B ⚠); 15 go from it, the strongest it → [[GDE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +22.3 | 0e+00 | 28/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +21.9 | 0e+00 | 28/34 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +21.6 | 0e+00 | 27/34 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +20.2 | 0e+00 | 28/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.20×** | +18.9 | 0e+00 | 26/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.14×** | +18.2 | 0e+00 | 24/32 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.85×** | +14.2 | 1e-43 | 18/27 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +13.3 | 2e-38 | 25/34 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.73×** | +12.2 | 3e-32 | 19/28 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.72×** | +11.6 | 2e-29 | 24/35 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +9.3 | 5e-19 | 21/34 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.6 | 2e-09 | 16/34 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +6.0 | 7e-08 | 16/34 (PANC-1, C-33 A, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.58×** | +5.3 | 4e-06 | 13/32 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +5.3 | 5e-06 | 15/33 (SW480, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +5.0 | 3e-05 | 12/35 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +4.9 | 3e-05 | 8/34 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.2 | 1e-03 | 7/34 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 4/33 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.001 | 10/34 (CFPAC-1, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -10.6 | 2e-23 | 20/33 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -7.8 | 2e-12 | 23/34 (SW480, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -4.3 | 0.003 | 14/34 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.1 | 0.006 | 10/34 (NCI-H2030, LoVo, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.826×** | -3.9 | 0.010 | 7/34 (RKO, NCI-H2030, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.716×** | -3.9 | 0.010 | 10/33 (KATO III, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.8 | 0.014 | 2/35 (NCI-H1792, SNU-1) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.7 | 0.015 | 13/34 (SW480, COLO 205, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.897× | -3.7 | 0.016 | 6/34 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.898× | -3.6 | 0.017 | 7/35 (PANC-1, SW 900, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.862× | -3.5 | 0.021 | 9/33 (HCT15, A549, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.865× | -3.4 | 0.027 | 9/34 (SW480, A-427, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.05 µM |  | 0.872× | -3.3 | 0.046 | 8/35 (Panc 03.27, NCI-H2122, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.053 | 6/35 (A-427, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.1 | 0.068 | 12/34 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.068 | 5/35 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.913× | -3.1 | 0.075 | 5/34 (RKO, NCI-H2030, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.883× | -3.0 | 0.094 | 8/34 (Panc 03.27, NCI-H661, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 67.0 | 8 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.46× (z +10.7) | — |
| [[A-427 (line)]] | wt | 47.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.43× (z +12.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.401× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 20.6 | 7 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.34× (z +12.8) | — |
| [[RKO (line)]] | wt | 28.1 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 6 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.22× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 51.4 | 6 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.98× (z +13.9) | — |
| [[HEC-1-A (line)]] | alt | 90.3 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 1.71× (z +10.3) | — |
| [[LoVo (line)]] | wt | 175 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -22.2) |
| [[NCI-H23 (line)]] | alt | 28.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 67.7 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.70× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 233 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -16.6) |
| [[Hs 766T (line)]] | wt | 44.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -13.6) |
| [[HT-29 (line)]] | alt | 111 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 17.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.95× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 28.2 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.95× (z +9.3) | — |
| [[SW480 (line)]] | alt | 101 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -15.7) |
| [[A549 (line)]] | wt | 41.8 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.05× (z +8.9) | — |
| [[KATO III (line)]] | alt | 289 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.0) |
| [[LS 180 (line)]] | wt | 272 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 71.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 81.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.1) |
| [[A-172 (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD22]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[CDH17]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ILDR2]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[AFAP1L2]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CYP2S1]] | +0.60 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[GCOM1]] | +0.59 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[PHF6]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[UGT8]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MAPRE2]] | +0.57 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[GDE1]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SSX2IP]] | +0.56 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[IQGAP2]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR81]] | -0.63 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[LRRC41]] | -0.57 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[ZNF785]] | -0.56 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[MRPL45P2]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.53 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[URM1]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MTG2]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[NOXRED1]] | -0.51 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[C1S]] | -0.51 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[COA6]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TRPV1]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZFHX2-AS1]] | -0.50 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 38, C 6. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP3]] | B | TJP3 activity raises PLS1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 4.26× lower at baseline in the lines without TJP3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises PLS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.53× lower at baseline in the lines without TMPRSS2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SULT2B1]] | B | SULT2B1 activity raises PLS1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 4.07× lower at baseline in the lines without SULT2B1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[GPX2]] | B | GPX2 activity raises PLS1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.21× lower at baseline in the lines without GPX2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[HOOK1]] | B | HOOK1 activity raises PLS1's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 3.25× lower at baseline in the lines without HOOK1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[SLC5A1]] | B | SLC5A1 activity raises PLS1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 4.75× lower at baseline in the lines without SLC5A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[RNF43]] | B | RNF43 activity raises PLS1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.15× lower at baseline in the lines without RNF43 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises PLS1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without PLEKHG6 | 0.005 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[MUC3A]] | B | MUC3A activity raises PLS1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 3.36× lower at baseline in the lines without MUC3A | 0.005 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[MPZL2]] | B | MPZL2 activity raises PLS1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.90× lower at baseline in the lines without MPZL2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[CKMT1A]] | B | CKMT1A activity raises PLS1's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 3.71× lower at baseline in the lines without CKMT1A | 0.010 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[FGFBP1]] | B | FGFBP1 activity raises PLS1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.76× lower at baseline in the lines without FGFBP1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 11, C 4. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDE1]] | B | PLS1 activity raises GDE1's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without PLS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[ABLIM1]] | B | PLS1 activity raises ABLIM1's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 3.69× lower at baseline in the lines without PLS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[LRRC41]] | B | PLS1 activity lowers LRRC41's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 1.25× higher at baseline in the lines without PLS1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[TNFRSF21]] | B | PLS1 activity raises TNFRSF21's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.83× lower at baseline in the lines without PLS1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[ITGA6]] | B | PLS1 activity raises ITGA6's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without PLS1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[ARHGAP26]] | B | PLS1 activity raises ARHGAP26's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.16× lower at baseline in the lines without PLS1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[C1S]] | B | PLS1 activity lowers C1S's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 1.79× higher at baseline in the lines without PLS1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[MUC3A]] | B | PLS1 activity raises MUC3A's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.40× lower at baseline in the lines without PLS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| cells under [[Erdafitinib (drug)]] 5 µM | B | PLS1 activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express PLS1 (14) vs lines expressing it (34) | the lines without PLS1: 0.85× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[DLG3]] | B | PLS1 activity raises DLG3's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.48× lower at baseline in the lines without PLS1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[RNF43]] | B | PLS1 activity raises RNF43's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 3.52× lower at baseline in the lines without PLS1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[SORL1]] | C | PLS1 activity raises SORL1's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 5.88× lower at baseline in the lines without PLS1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.4, 48.1); signed map (64.2, 9.5). **Vector** length 109, 28.9% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +21.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +8.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +8.5 | +18.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.0 | +12.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +4.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -10.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | plastin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:142,596,393-142,713,664 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing; Plastin family |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14651](https://www.uniprot.org/uniprotkb/Q14651) (Plastin-1):

> Actin-bundling protein. In the inner ear, it is required for stereocilia formation. Mediates liquid packing of actin filaments that is necessary for stereocilia to grow to their proper dimensions.

**Summary**, from NCBI Gene [5357](https://www.ncbi.nlm.nih.gov/gene/5357):

> Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. The protein encoded by this gene is a third distinct plastin isoform, which is specifically expressed at high levels in the small intestine. Alternatively spliced transcript variants varying in the 5' UTR, but encoding the same protein, have been found for this gene. A …

**Accessions** — [HGNC:9090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9090) · Entrez [5357](https://www.ncbi.nlm.nih.gov/gene/5357) · UniProt [Q14651](https://www.uniprot.org/uniprotkb/Q14651) · Ensembl [ENSG00000120756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120756)

## Data

Gene col 4219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4219); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4219]; `tensor/DDL_lfc|DDL_z.npy` [4219]; `embed/gene_vectors.npy` [4219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4219 or target_col == 4219). Every well: [[PLS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
