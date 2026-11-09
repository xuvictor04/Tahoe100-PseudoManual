---
symbol: "TMEM65"
type: "gene"
col: 9050
ensembl_id: "ENSG00000164983"
name: "transmembrane protein 65"
location: "8q24.13"
module: 99
arm: "+"
pooled_cpm: 118.71
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# TMEM65

*transmembrane protein 65* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +5.7, q 8e-06, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 2.12×; ⚠ cell-cycle shift, explains ~26% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 2.12×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.33×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.532× (z -11.1, q 8e-26, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.657× (z -7.7, q 2e-12, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEBP1]] (+0.70, fdr 1e-05), [[CDS1]] (+0.65, fdr 7e-06), [[RAP2A]] (+0.61, fdr 1e-05); moves opposite to [[FBXO38]] (-0.66, fdr 1e-05), [[ZNF268]] (-0.63, fdr 1e-05), [[DNAJC11]] (-0.63, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 2.12×; ⚠ cell-cycle shift, explains ~26% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 2.12×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.33×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.7 | 8e-06 | 28/47 (RKO, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.29×** | +4.4 | 0.003 | 28/46 (NCI-H2030, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.026 | 25/46 (NCI-H2030, LoVo, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.15 | 11/47 (AsPC-1, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.16 | 17/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.37× | +3.0 | 0.24 | 14/48 (LoVo, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.532×** | -11.1 | 8e-26 | 33/47 (SNU-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.553×** | -10.4 | 6e-23 | 34/42 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.693×** | -9.5 | 6e-19 | 29/47 (SNU-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.615×** | -8.2 | 3e-14 | 31/44 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.651×** | -7.9 | 4e-13 | 36/48 (SNU-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -7.7 | 2e-12 | 34/47 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -7.3 | 2e-11 | 30/47 (SNU-1, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.718×** | -6.1 | 9e-08 | 29/47 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.744×** | -5.4 | 4e-06 | 30/47 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -5.3 | 7e-06 | 29/48 (SNU-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.815×** | -3.7 | 0.009 | 22/47 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.865× | -3.7 | 0.009 | 11/47 (NCI-H460, SW1417, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.817×** | -3.7 | 0.010 | 24/47 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.875× | -3.4 | 0.023 | 18/48 (SNU-1, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.023 | 21/47 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.3 | 0.029 | 20/47 (C32, HOP62, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.042 | 21/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.1 | 0.052 | 12/47 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.843× | -3.1 | 0.053 | 15/47 (SW1417, A-172, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.844× | -3.1 | 0.055 | 18/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.075 | 17/48 (SW480, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 639 | 0 | 18 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -25.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 83.3 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -8.8) |
| [[SW 900 (line)]] | alt | 169 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -16.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -12.9) |
| [[HS-578T (line)]] | alt | 203 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -11.6) |
| [[HT-29 (line)]] | alt | 621 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 134 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.473× (z -8.7) |
| [[A-172 (line)]] | wt | 94.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.391× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.494× (z -9.2) |
| [[Hs 766T (line)]] | wt | 163 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 98.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -9.3) |
| [[RKO (line)]] | wt | 86.7 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.12× (z +10.5) | [[PH-797804 (drug)]] 5 µM 0.187× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -13.4) |
| [[BT-474 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.459× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 87.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -9.2) |
| [[SW1417 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[J82 (line)]] | alt | 87.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 99.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.07× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[Panc 03.27 (line)]] | alt | 95.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[PANC-1 (line)]] | alt | 84.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.481× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.532× (z -8.6) |
| [[SW 1271 (line)]] | alt | 75.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0575× (z -11.2) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0762× (z -10.5) |
| [[A-427 (line)]] | wt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -9.8) |
| [[CHP-212 (line)]] | wt | 67.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.95× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 68.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.05 µM 2.11× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.1000× (z -9.7) ⚠ transcription drop |
| [[A498 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEBP1]] | +0.70 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CDS1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RAP2A]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SLC17A7]] | +0.60 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[F11R]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MGST3]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GNB2]] | +0.59 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[PPP2R5A]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[STX7]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[KCTD9]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO38]] | -0.66 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.63 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ALG8]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[INTS14]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[DNAJB12]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TASOR]] | -0.61 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[PYM1]] | -0.61 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[FIZ1]] | -0.60 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TAF2]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.59 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ZC3H4]] | -0.59 | -0.62 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.0, 4.5); signed map (-32.9, 19.6). **Vector** length 114, 33.9% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -8.0 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.2 | -11.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 65 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:124,306,189-124,372,701 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PI78](https://www.uniprot.org/uniprotkb/Q6PI78) (Transmembrane protein 65):

> Mitochondrial protein that plays a critical role in the sodium-dependent calcium efflux from mitochondrion. The precise role of TMEM65 in mitochondrial sodium/calcium exchange is however unclear: TMEM65 associates with the SLC8B1/NCLX antiporter and probably promotes the sodium/calcium exchange mediated by SLC8B1/NCLX. According to another report, TMEM65 functions as the mitochondrial sodium/calcium antiporter itself: homodimerization drives formation of a pocket capable of binding calcium. …

**Summary**, from NCBI Gene [157378](https://www.ncbi.nlm.nih.gov/gene/157378):

> Enables calcium:sodium antiporter activity. Involved in calcium export from the mitochondrion. Located in intercalated disc and plasma membrane. Is active in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25203) · Entrez [157378](https://www.ncbi.nlm.nih.gov/gene/157378) · UniProt [Q6PI78](https://www.uniprot.org/uniprotkb/Q6PI78) · Ensembl [ENSG00000164983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164983)

## Data

Gene col 9050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9050); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9050]; `tensor/DDL_lfc|DDL_z.npy` [9050]; `embed/gene_vectors.npy` [9050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9050 or target_col == 9050). Every well: [[TMEM65 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM65.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
