---
symbol: "USP13"
type: "gene"
col: 654
ensembl_id: "ENSG00000058056"
name: "ubiquitin specific peptidase 13"
location: "3q26.33"
module: 143
arm: "+"
pooled_cpm: 39.78
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# USP13

*ubiquitin specific peptidase 13* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +9.7, q 2e-19, up in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +7.8, q 1e-12, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.289× (z -22.3, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPO]] (+0.70, fdr 7e-06), [[OXCT1]] (+0.69, fdr 1e-05), [[SNX5]] (+0.66, fdr 3e-05); moves opposite to [[PLD3]] (-0.63, fdr 2e-05), [[PIGH]] (-0.63, fdr 5e-05), [[GIPR]] (-0.61, fdr 2e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +9.7 | 2e-19 | 31/46 (HOP62, J82, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.8 | 1e-12 | 27/46 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.45×** | +6.6 | 7e-09 | 25/45 (SNU-423, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.2 | 1e-07 | 24/44 (A-172, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +5.9 | 3e-07 | 24/46 (HS-578T, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 5e-05 | 21/45 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.8 | 2e-04 | 21/46 (HOP62, J82, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.5 | 4e-04 | 18/46 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 21/46 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 8e-04 | 10/46 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +4.2 | 0.002 | 16/45 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.9 | 0.004 | 16/38 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.007 | 18/45 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +3.7 | 0.009 | 19/46 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.22×** | +3.5 | 0.018 | 13/44 (CFPAC-1, Panc 03.27, …) | all doses, flat | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.029 | 6/46 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.14× | +3.3 | 0.029 | 7/46 (HT-29, HCT15, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.040 | 9/46 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.061 | 13/45 (HOP62, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.289×** | -22.3 | 0e+00 | 45/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.315×** | -20.7 | 0e+00 | 42/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.386×** | -17.1 | 0e+00 | 40/46 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.583×** | -5.1 | 6e-05 | 22/45 (H4, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -4.8 | 2e-04 | 22/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -4.8 | 2e-04 | 24/45 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.803×** | -3.9 | 0.007 | 20/46 (H4, A-427, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.871× | -3.5 | 0.032 | 7/46 (LOX-IMVI, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.836× | -3.2 | 0.080 | 18/46 (MIA PaCa-2, SK-MEL-2, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.886× | -3.1 | 0.12 | 16/46 (CHP-212, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 114 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -18.2) |
| [[A498 (line)]] | wt | 46.5 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +11.7) ⚠ cell-cycle shift, explains ~23% of this change | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -16.0) |
| [[C-33 A (line)]] | alt | 102 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -16.3) |
| [[HOP62 (line)]] | alt | 50.2 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +19.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.169× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 44.1 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +14.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.199× (z -11.1) |
| [[J82 (line)]] | alt | 59.1 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +16.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.262× (z -11.9) |
| [[A549 (line)]] | wt | 27.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -11.5) |
| [[AN3 CA (line)]] | alt | 131 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.214× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 56.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -15.1) |
| [[HS-578T (line)]] | alt | 33.6 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 6.04× (z +13.1) ⚠ cell-cycle shift, explains ~23% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 53.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 59.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 41.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 40.0 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 47.5 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -9.7) |
| [[SHP-77 (line)]] | alt | 56.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -14.4) |
| [[SNU-423 (line)]] | alt | 41.7 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.226× (z -11.4) |
| [[SW48 (line)]] | wt | 69.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -12.1) |
| [[SW480 (line)]] | alt | 45.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -19.3) |
| [[BT-474 (line)]] | alt | 22.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -9.4) |
| [[H4 (line)]] | wt | 52.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.175× (z -12.6) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.318× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 17.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.341× (z -9.1) |
| [[PANC-1 (line)]] | alt | 46.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -11.7) |
| [[SNU-1 (line)]] | wt | 82.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -11.5) |
| [[SW 900 (line)]] | alt | 52.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -13.2) |
| [[A-172 (line)]] | wt | 45.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +14.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.220× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 31.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -10.2) |
| [[LS 180 (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[RKO (line)]] | wt | 50.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPO]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[OXCT1]] | +0.69 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[SNX5]] | +0.66 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[NFIB]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.66 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[CNTLN]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[HYLS1]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.63 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[HDGF]] | +0.62 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[ZMYND11]] | +0.62 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLD3]] | -0.63 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PIGH]] | -0.63 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[GIPR]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CIB1]] | -0.60 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ATG4B]] | -0.60 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[GP6-AS1]] | -0.60 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[EDF1]] | -0.60 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[ARPC1A]] | -0.60 | -0.63 / -0.36 | both halves | 9e-05 |  |
| [[GUK1]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.59 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[LCMT1]] | -0.59 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[MPG]] | -0.59 | -0.57 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity weakens USP13's drug response | lines that do not express NFIA (11) vs lines expressing it (35) | the lines without NFIA respond 1.35× as strongly (z diff -1.14); strongest at Homoharringtonine 5 µM: 2.73x vs 1.29x (z diff -4.9) | 0.039 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZNF618]] | B | ZNF618 activity raises USP13's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without ZNF618 | 0.046 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[HDAC6]] | B | HDAC6 activity raises USP13's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF618]] | B | ZNF618 activity strengthens USP13's drug response | lines that do not express ZNF618 (7) vs lines expressing it (39) | the lines without ZNF618 respond 0.75× as strongly (z diff +1.13); strongest at Belinostat 5 µM: 0.58x vs 0.38x (z diff +3.4) | 0.063 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63; target measured in part of the lines; artifact flags |
| [[TMEM92]] | B | TMEM92 activity lowers USP13's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.70× higher at baseline in the lines without TMEM92 | 0.072 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[ANKRD18B]] | B | ANKRD18B activity raises USP13's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without ANKRD18B | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity lowers USP13's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.71× higher at baseline in the lines without TMEM92-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[SPDL1]] | C | SPDL1 activity raises USP13's level | lines that do not express SPDL1 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.8, 5.0); signed map (21.1, -33.8). **Vector** length 137, 40.6% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.2 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.4 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.2 | +5.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +4.5 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.9 | -22.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.9 | -20.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -17.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:179,653,032-179,804,366 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IsoT-3 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 6 pathways, smallest: Regulation of PTEN stability and activity; PTEN Regulation; Ub-specific processing proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92995](https://www.uniprot.org/uniprotkb/Q92995) (Ubiquitin carboxyl-terminal hydrolase 13):

> Deubiquitinase that mediates deubiquitination of target proteins such as BECN1, MITF, SKP2 and USP10 and is involved in various processes such as autophagy, endoplasmic reticulum-associated degradation (ERAD), cell cycle progression or DNA damage response. Component of a regulatory loop that controls autophagy and p53/TP53 levels: mediates deubiquitination of BECN1, a key regulator of autophagy, leading to stabilize the PIK3C3/VPS34-containing complexes. Alternatively, forms with NEDD4 a …

**Summary**, from NCBI Gene [8975](https://www.ncbi.nlm.nih.gov/gene/8975):

> Enables several functions, including BAT3 complex binding activity; peptidase activity; and proteasome binding activity. Involved in several processes, including maintenance of unfolded protein; positive regulation of ERAD pathway; and regulation of autophagy. Acts upstream of or within protein deubiquitination and protein stabilization. Predicted to be located in nucleoplasm. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12611) · Entrez [8975](https://www.ncbi.nlm.nih.gov/gene/8975) · UniProt [Q92995](https://www.uniprot.org/uniprotkb/Q92995) · Ensembl [ENSG00000058056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058056)

## Data

Gene col 654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 654); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 654]; `tensor/DDL_lfc|DDL_z.npy` [654]; `embed/gene_vectors.npy` [654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 654 or target_col == 654). Every well: [[USP13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
