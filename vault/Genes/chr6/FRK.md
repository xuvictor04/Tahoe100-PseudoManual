---
symbol: "FRK"
type: "gene"
col: 3286
ensembl_id: "ENSG00000111816"
name: "fyn related Src family tyrosine kinase"
location: "6q22.1"
module: 8
arm: "+"
pooled_cpm: 41.45
n_lines_expressing: 28
n_dd_up: 21
n_dd_down: 23
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 84
direction_downstream: 94
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FRK

*fyn related Src family tyrosine kinase* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.60× (z +9.7, q 1e-19, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.426× (z -11.6, q 4e-28, down in 20 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.668× (z -5.7, q 1e-06, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM47]] (+0.75, fdr 7e-06), [[POF1B]] (+0.70, fdr 7e-06), [[TOX3]] (+0.69, fdr 7e-06); moves opposite to [[CAPRIN2]] (-0.54, fdr 1e-05), [[HMGA2]] (-0.52, fdr 2e-05), [[NT5E]] (-0.52, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[HNF4G]] → it (grade B ⚠); 94 go from it, the strongest it → [[EFNA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +9.7 | 1e-19 | 13/26 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.83×** | +8.5 | 4e-15 | 25/26 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +8.3 | 2e-14 | 16/27 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +6.8 | 1e-09 | 20/26 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 1e-08 | 20/26 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.57×** | +6.3 | 3e-08 | 15/26 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +6.2 | 4e-08 | 21/27 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +6.1 | 8e-08 | 16/26 (HT-29, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +6.0 | 1e-07 | 18/27 (HEC-1-A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +5.8 | 5e-07 | 19/26 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +5.7 | 5e-07 | 16/26 (A549, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +5.4 | 4e-06 | 16/26 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.48×** | +5.3 | 4e-06 | 17/26 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +5.0 | 2e-05 | 12/27 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 4e-05 | 14/26 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 4e-04 | 14/27 (HEC-1-A, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.426×** | -11.6 | 4e-28 | 20/23 (HepG2/C3A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.591×** | -7.7 | 4e-12 | 18/26 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.620×** | -7.0 | 5e-10 | 21/26 (SW480, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.633×** | -6.7 | 3e-09 | 18/26 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.634×** | -6.4 | 2e-08 | 18/22 (LoVo, Panc 03.27, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.656×** | -6.2 | 6e-08 | 21/26 (SW480, KATO III, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.668×** | -5.7 | 1e-06 | 16/26 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.689×** | -5.5 | 4e-06 | 14/26 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.688×** | -5.3 | 9e-06 | 20/26 (COLO 205, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.777×** | -5.2 | 1e-05 | 15/26 (KATO III, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.701×** | -5.2 | 1e-05 | 12/26 (SW480, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -4.3 | 1e-03 | 15/27 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.003 | 19/26 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.759×** | -3.9 | 0.004 | 7/26 (NCI-H460, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.772×** | -3.8 | 0.005 | 13/26 (SNU-423, HEC-1-A, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.005 | 11/26 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.016 | 14/26 (A498, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.795×** | -3.2 | 0.038 | 11/26 (SW 900, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.600×** | -3.2 | 0.041 | 9/26 (COLO 205, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.068 | 8/26 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 60.0 | 7 | 5 (5 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.59× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 200 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 89.6 | 0 | 10 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0917× (z -20.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 177 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0455× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -18.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.242× (z -10.9) |
| [[SW1417 (line)]] | alt | 53.0 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -9.0) |
| [[LoVo (line)]] | wt | 108 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0969× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[AsPC-1 (line)]] | alt | 58.8 | 1 | 5 (5 ⚠) | [[Trametinib (drug)]] 0.5 µM 2.95× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[CFPAC-1 (line)]] | alt | 83.7 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.227× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0884× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[Panc 03.27 (line)]] | alt | 82.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.245× (z -11.6) |
| [[SW48 (line)]] | wt | 16.6 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.101× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Orlistat (drug)]] 0.05 µM 0.0981× (z -8.6) |
| [[BT-474 (line)]] | alt | 41.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +12.6) ⚠ cell-cycle shift, explains ~75% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 68.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.325× (z -9.2) ⚠ cell-cycle shift, explains ~74% of this change |
| [[NCI-H2030 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.72 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM47]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[TOX3]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MMP7]] | +0.67 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[OCLN]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[RASSF6]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 | same gene group |
| [[HHLA2]] | +0.66 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[ITGB6]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[MACC1]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | same gene group |
| [[ADGRF1]] | +0.65 | +0.62 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN2]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[HMGA2]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[NT5E]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CLMP]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ITGB1BP1]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 23, C 61. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF4G]] | B | HNF4G activity raises FRK's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without HNF4G | 0.005 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[EFNA1]] | B | EFNA1 activity raises FRK's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 3.60× lower at baseline in the lines without EFNA1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises FRK's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.84× lower at baseline in the lines without SHROOM3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[SLC44A3]] | B | SLC44A3 activity raises FRK's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 4.33× lower at baseline in the lines without SLC44A3 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises FRK's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without SLC44A3-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity raises FRK's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 4.60× lower at baseline in the lines without ATP1B1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[PLCH1]] | B | PLCH1 activity raises FRK's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 3.12× lower at baseline in the lines without PLCH1 | 0.031 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises FRK's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.98× lower at baseline in the lines without SPATA6L | 0.032 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[HNMT]] | B | HNMT activity raises FRK's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without HNMT | 0.032 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[HGD]] | B | HGD activity raises FRK's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without HGD | 0.033 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[MGST2]] | B | MGST2 activity raises FRK's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without MGST2 | 0.037 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[RORC]] | B | RORC activity raises FRK's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without RORC | 0.043 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |

### Downstream of this gene

*94 arrows, 94 of them with an alert ⚠; grade A 0, B 44, C 50. Shown: the 12 strongest; 82 more arrows (82 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA1]] | B | FRK activity raises EFNA1's level | lines that do not express FRK (22) vs lines expressing it (28) | 3.00× lower at baseline in the lines without FRK | 0.002 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[CASP10]] | B | FRK activity raises CASP10's level | lines that do not express FRK (22) vs lines expressing it (28) | 3.32× lower at baseline in the lines without FRK | 0.004 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[CTNND1]] | B | FRK activity raises CTNND1's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without FRK | 0.005 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[EPS8]] | B | FRK activity raises EPS8's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without FRK | 0.005 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[ST3GAL3]] | B | FRK activity weakens ST3GAL3's drug response | lines that do not express FRK (21) vs lines expressing it (26) | the lines without FRK respond 1.56× as strongly (z diff -2.63); strongest at Panobinostat 0.5 µM: 0.61x vs 1.04x (z diff -4.7) | 0.006 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP; target measured in part of the lines; artifact flags |
| [[FMO5]] | B | FRK activity raises FMO5's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without FRK | 0.007 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[LGALS9]] | B | FRK activity raises LGALS9's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without FRK | 0.011 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[ST3GAL3]] | B | FRK activity lowers ST3GAL3's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.93× higher at baseline in the lines without FRK | 0.014 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[ARHGAP42]] | B | FRK activity raises ARHGAP42's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without FRK | 0.016 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[DAPK2]] | B | FRK activity raises DAPK2's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without FRK | 0.017 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[TNFRSF21]] | B | FRK activity raises TNFRSF21's level | lines that do not express FRK (22) vs lines expressing it (28) | 3.02× lower at baseline in the lines without FRK | 0.017 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[SLC44A3]] | B | FRK activity raises SLC44A3's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.82× lower at baseline in the lines without FRK | 0.018 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 54.0); signed map (58.6, 3.4). **Vector** length 101, 35.1% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +8.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +8.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.4 | +6.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.0 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.6 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -1.9 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | fyn related Src family tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:115,931,149-116,060,891 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAK, GTK; previously PTK5 |
| Gene groups (HGNC) | SH2 domain containing; Src family tyrosine kinases; SH3 domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 6 pathways, smallest: Regulation of PTEN stability and activity; PTEN Regulation; PIP3 activates AKT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42685](https://www.uniprot.org/uniprotkb/P42685) (Tyrosine-protein kinase FRK):

> Non-receptor tyrosine-protein kinase that negatively regulates cell proliferation. Positively regulates PTEN protein stability through phosphorylation of PTEN on 'Tyr-336', which in turn prevents its ubiquitination and degradation, possibly by reducing its binding to NEDD4. May function as a tumor suppressor.

**Summary**, from NCBI Gene [2444](https://www.ncbi.nlm.nih.gov/gene/2444):

> The protein encoded by this gene belongs to the TYR family of protein kinases. This tyrosine kinase is a nuclear protein and may function during G1 and S phase of the cell cycle and suppress growth. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3955) · Entrez [2444](https://www.ncbi.nlm.nih.gov/gene/2444) · UniProt [P42685](https://www.uniprot.org/uniprotkb/P42685) · Ensembl [ENSG00000111816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111816)

## Data

Gene col 3286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3286); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3286]; `tensor/DDL_lfc|DDL_z.npy` [3286]; `embed/gene_vectors.npy` [3286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3286 or target_col == 3286). Every well: [[FRK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
