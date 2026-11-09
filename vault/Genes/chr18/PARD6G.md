---
symbol: "PARD6G"
type: "gene"
col: 10905
ensembl_id: "ENSG00000178184"
name: "par-6 family cell polarity regulator gamma"
location: "18q23"
module: 115
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 40
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 17
direction_downstream: 12
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# PARD6G

*par-6 family cell polarity regulator gamma* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.86× (z +14.9, q 0e+00, up in 30 of 37 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.57× (z +13.4, q 3e-38, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.613× (z -9.8, q 5e-20, down in 18 of 34 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.521× (z -9.3, q 4e-18, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCD5]] (+0.66, fdr 7e-06), [[PTK7]] (+0.66, fdr 9e-06), [[SHANK3]] (+0.65, fdr 1e-05); moves opposite to [[METTL6]] (-0.52, fdr 4e-05), [[GGPS1]] (-0.52, fdr 4e-05), [[LINC01252]] (-0.49, fdr 7e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[SLC16A10]] → it (grade B ⚠); 12 go from it, the strongest it → [[FBXO44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.86×** | +14.9 | 0e+00 | 30/37 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.57×** | +13.4 | 3e-38 | 32/37 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.49×** | +12.9 | 5e-36 | 27/37 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.27×** | +11.6 | 4e-29 | 29/37 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.86×** | +8.8 | 2e-16 | 21/34 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.65×** | +7.1 | 1e-10 | 18/37 (NCI-H460, LoVo, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.0 | 2e-10 | 16/37 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.41×** | +6.9 | 3e-10 | 10/37 (NCI-H460, A549, …) | top dose only | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **2.53×** | +6.9 | 4e-10 | 16/37 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.36×** | +6.2 | 4e-08 | 14/34 (NCI-H460, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.55×** | +6.0 | 1e-07 | 11/25 (LS 180, NCI-H460, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.47×** | +5.3 | 7e-06 | 11/35 (LS 180, LoVo, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.010 | 5/37 (A549, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.017 | 7/37 (NCI-H2030, C32, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.017 | 6/37 (NCI-H460, C32, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.017 | 9/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.066 | 2/37 (LS 180, C32) | top dose only | plate-row cell shift |
| [[Vismodegib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.087 | 1/37 (A-427) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.092 | 2/37 (BT-474, A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.613×** | -9.8 | 5e-20 | 18/34 (C32, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.515×** | -9.4 | 2e-18 | 20/34 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.521×** | -9.3 | 4e-18 | 23/36 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.524×** | -9.2 | 7e-18 | 21/37 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -6.5 | 1e-08 | 20/37 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -5.9 | 3e-07 | 17/36 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Clotrimazole (drug)]] 5 µM |  | **0.800×** | -4.5 | 6e-04 | 7/37 (PANC-1, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.731×** | -4.4 | 6e-04 | 6/37 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -4.2 | 0.001 | 16/37 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.735×** | -4.2 | 0.002 | 17/36 (LoVo, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.731×** | -4.1 | 0.002 | 12/33 (AN3 CA, RKO, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.783×** | -3.5 | 0.025 | 15/34 (NCI-H23, LS 180, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.847× | -3.3 | 0.035 | 6/37 (LS 180, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.777×** | -3.3 | 0.037 | 10/17 (C-33 A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.038 | 12/35 (A-172, HEC-1-A, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.801×** | -3.0 | 0.087 | 5/37 (A-427, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 17.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.5) ⚠ cell-cycle shift, explains ~76% of this change |
| [[PANC-1 (line)]] | alt | 3.43 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 14.6× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -13.2) ⚠ cell-cycle shift, explains ~76% of this change |
| [[LoVo (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0870× (z -14.8) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.195× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 8.23 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0578× (z -12.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -9.0) |
| [[A-172 (line)]] | wt | 8.28 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -9.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[C32 (line)]] | wt | 16.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -17.3) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A498 (line)]] | wt | 2.33 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 4.70 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0902× (z -8.5) |
| [[HCT15 (line)]] | alt | 8.42 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -9.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[Hs 766T (line)]] | wt | 3.43 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0562× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 7.41 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0680× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 7.44 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.2) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0312× (z -17.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 5.34 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0291× (z -13.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 4.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -8.8) ⚠ cell-cycle shift, explains ~76% of this change |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCD5]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PTK7]] | +0.66 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[SHANK3]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 | same gene group |
| [[SBK1]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[EPHB4]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D2B]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.60 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[SLC29A4]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[PACSIN3]] | +0.58 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[SLC47A1]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL6]] | -0.52 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[GGPS1]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[LINC01252]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[LARP7]] | -0.48 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[FSIP2-AS1]] | -0.48 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[TRMT13]] | -0.48 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[FCF1]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[MIR583HG]] | -0.48 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[BPTF]] | -0.48 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[RIPK2-DT]] | -0.47 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[RFX3-DT]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[TAF1]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A10]] | B | SLC16A10 activity raises PARD6G's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without SLC16A10 | 0.009 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[AIF1L]] | B | AIF1L activity raises PARD6G's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 2.38× lower at baseline in the lines without AIF1L | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises PARD6G's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without JAG2 | 0.014 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[MSI1]] | B | MSI1 activity raises PARD6G's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without MSI1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[WNK2]] | B | WNK2 activity raises PARD6G's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without WNK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[SLC47A1]] | B | SLC47A1 activity raises PARD6G's level | lines that do not express SLC47A1 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without SLC47A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: DUSP9, STOX2, NOVA2; maybe low, not absent |
| [[CRACD]] | B | CRACD activity raises PARD6G's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without CRACD | 0.029 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[LAMC3]] | B | LAMC3 activity raises PARD6G's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without LAMC3 | 0.030 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[RET]] | B | RET activity raises PARD6G's level | lines that do not express RET (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without RET | 0.031 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[TOP1]] | B | TOP1 activity lowers PARD6G's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02643]] | B | LINC02643 activity raises PARD6G's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without LINC02643 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530 |
| [[NCS1]] | B | NCS1 activity raises PARD6G's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.82× lower at baseline in the lines without NCS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO44]] | B | PARD6G activity raises FBXO44's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without PARD6G | 0.020 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[TCFL5]] | B | PARD6G activity raises TCFL5's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without PARD6G | 0.022 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[SRPK2]] | B | PARD6G activity raises SRPK2's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PARD6G | 0.036 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[C2orf72]] | B | PARD6G activity strengthens C2orf72's drug response | lines that do not express PARD6G (8) vs lines expressing it (33) | the lines without PARD6G respond 0.54× as strongly (z diff +2.27); strongest at Niclosamide (olamine) 5 µM: 0.65x vs 0.25x (z diff +3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SEMA6B]] | B | PARD6G activity raises SEMA6B's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.96× lower at baseline in the lines without PARD6G | 0.041 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[SLC16A10]] | B | PARD6G activity raises SLC16A10's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 3.29× lower at baseline in the lines without PARD6G | 0.041 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[NCS1]] | B | PARD6G activity raises NCS1's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without PARD6G | 0.047 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[SHANK3]] | B | PARD6G activity raises SHANK3's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.08× lower at baseline in the lines without PARD6G | 0.051 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[LAMC3]] | B | PARD6G activity raises LAMC3's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.34× lower at baseline in the lines without PARD6G | 0.059 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[SLC47A1]] | B | PARD6G activity raises SLC47A1's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without PARD6G | 0.073 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[SLC29A4]] | B | PARD6G activity raises SLC29A4's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without PARD6G | 0.081 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[RASGEF1C]] | C | PARD6G activity raises RASGEF1C's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.67× lower at baseline in the lines without PARD6G | 0.064 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.8, 38.1); signed map (-22.6, 36.1). **Vector** length 69.7, 13.0% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +8.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.8 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | +2.8 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +7.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +6.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.1 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -3.1 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -2.4 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | par-6 family cell polarity regulator gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:80,157,232-80,247,514 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAR-6G, PAR6gamma |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Tight junction interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYG4](https://www.uniprot.org/uniprotkb/Q9BYG4) (Partitioning defective 6 homolog gamma):

> Adapter protein involved in asymmetrical cell division and cell polarization processes. May play a role in the formation of epithelial tight junctions. The PARD6-PARD3 complex links GTP-bound Rho small GTPases to atypical protein kinase C proteins (By similarity).

**Summary**, from NCBI Gene [84552](https://www.ncbi.nlm.nih.gov/gene/84552):

> Predicted to be involved in centrosome cycle; establishment or maintenance of cell polarity; and regulation of cellular localization. Predicted to be located in cytosol; plasma membrane; and tight junction. Predicted to be active in apical plasma membrane; cell cortex; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16076) · Entrez [84552](https://www.ncbi.nlm.nih.gov/gene/84552) · UniProt [Q9BYG4](https://www.uniprot.org/uniprotkb/Q9BYG4) · Ensembl [ENSG00000178184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178184)

## Data

Gene col 10905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10905); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10905]; `tensor/DDL_lfc|DDL_z.npy` [10905]; `embed/gene_vectors.npy` [10905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10905 or target_col == 10905). Every well: [[PARD6G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARD6G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
