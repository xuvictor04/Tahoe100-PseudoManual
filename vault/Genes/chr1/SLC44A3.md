---
symbol: "SLC44A3"
type: "gene"
col: 6672
ensembl_id: "ENSG00000143036"
name: "solute carrier family 44 member 3"
location: "1p21.3"
module: 8
arm: "+"
pooled_cpm: 16.22
n_lines_expressing: 37
n_dd_up: 22
n_dd_down: 24
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 81
direction_downstream: 62
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC44A3

*solute carrier family 44 member 3* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.63× (z +7.0, q 2e-09, up in 6 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 1.53× (z +6.4, q 4e-08, up in 17 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.491× (z -10.6, q 2e-23, down in 29 of 34 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.532× (z -9.4, q 2e-18, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A3-AS1]] (+0.72, fdr 7e-06), [[SYK]] (+0.71, fdr 7e-06), [[PROM1]] (+0.69, fdr 7e-06); moves opposite to [[EPOR]] (-0.56, fdr 4e-05), [[FIBCD1]] (-0.53, fdr 4e-05), [[ZNF275]] (-0.52, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 81 arrows point to it, the strongest [[KDF1]] → it (grade B ⚠); 62 go from it, the strongest it → [[SHROOM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.0 | 2e-09 | 6/19 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.53×** | +6.4 | 4e-08 | 17/35 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.4 | 4e-08 | 11/26 (HS-578T, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.2 | 6e-08 | 13/32 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +6.1 | 1e-07 | 23/32 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +6.1 | 1e-07 | 11/25 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +5.8 | 6e-07 | 16/32 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +5.6 | 2e-06 | 12/34 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.4 | 5e-06 | 12/34 (KATO III, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 5e-06 | 14/33 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 2e-05 | 15/32 (KATO III, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 2e-05 | 17/34 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 2e-05 | 14/34 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 10/34 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 5e-05 | 11/34 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 4e-04 | 13/33 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 9e-04 | 12/32 (SW480, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.027 | 8/34 (LS 180, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.028 | 2/32 (NCI-H460, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.491×** | -10.6 | 2e-23 | 29/34 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -9.4 | 2e-18 | 26/32 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -9.1 | 1e-17 | 22/32 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.563×** | -8.5 | 2e-15 | 20/31 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -7.8 | 7e-13 | 22/34 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.615×** | -7.2 | 5e-11 | 22/32 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.631×** | -6.8 | 6e-10 | 18/34 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.729×** | -6.6 | 2e-09 | 21/33 (LoVo, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.647×** | -6.5 | 6e-09 | 20/34 (LoVo, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -6.0 | 1e-07 | 21/33 (HT-29, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.695×** | -5.4 | 3e-06 | 9/33 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.685×** | -5.4 | 3e-06 | 17/30 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.689×** | -5.3 | 5e-06 | 20/34 (Panc 03.27, HEC-1-A, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.706×** | -5.2 | 9e-06 | 16/33 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -5.1 | 1e-05 | 19/32 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -5.0 | 2e-05 | 17/33 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.009 | 11/34 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.009 | 10/34 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.848× | -3.5 | 0.013 | 13/33 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.819×** | -3.0 | 0.068 | 15/34 (LoVo, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 46.6 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -20.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.215× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -8.7) |
| [[SW480 (line)]] | alt | 21.5 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.138× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.159× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 60.1 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H1573 (line)]] | alt | 80.5 | 1 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +8.7) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.4 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.220× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 14.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +19.6) ⚠ cell-cycle shift, explains ~61% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 6.73 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.83× (z +11.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 7.63× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -16.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[C32 (line)]] | wt | 13.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.127× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Hs 766T (line)]] | wt | 6.32 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0902× (z -9.1) |
| [[KATO III (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H2347 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 8.49 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.116× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 8.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -10.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SYK]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TMC4]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[TOX3]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ABO]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ERBB3]] | +0.64 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.63 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[FAAH2]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LINC01814]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPOR]] | -0.56 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[FIBCD1]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZNF275]] | -0.52 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[STEAP3]] | -0.51 | -0.61 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 78, C 3. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDF1]] | B | KDF1 activity raises SLC44A3's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 3.79× lower at baseline in the lines without KDF1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[RNF43]] | B | RNF43 activity raises SLC44A3's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.18× lower at baseline in the lines without RNF43 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[INAVA]] | B | INAVA activity raises SLC44A3's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.49× lower at baseline in the lines without INAVA | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ST14]] | B | ST14 activity raises SLC44A3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.74× lower at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[CLDN3]] | B | CLDN3 activity raises SLC44A3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.41× lower at baseline in the lines without CLDN3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ESRP1]] | B | ESRP1 activity raises SLC44A3's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.69× lower at baseline in the lines without ESRP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ERBB3]] | B | ERBB3 activity raises SLC44A3's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.71× lower at baseline in the lines without ERBB3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[TJP3]] | B | TJP3 activity raises SLC44A3's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.68× lower at baseline in the lines without TJP3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[HSH2D]] | B | HSH2D activity raises SLC44A3's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 3.77× lower at baseline in the lines without HSH2D | 3e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity raises SLC44A3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.34× lower at baseline in the lines without TMPRSS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TMEM125]] | B | TMEM125 activity raises SLC44A3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.68× lower at baseline in the lines without TMEM125 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises SLC44A3's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 3.55× lower at baseline in the lines without SPINT1-AS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |

### Downstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 59, C 3. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHROOM3]] | B | SLC44A3 activity raises SHROOM3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.98× lower at baseline in the lines without SLC44A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[ERBB3]] | B | SLC44A3 activity raises ERBB3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 4.64× lower at baseline in the lines without SLC44A3 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[FAAH2]] | B | SLC44A3 activity raises FAAH2's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.16× lower at baseline in the lines without SLC44A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TJP3]] | B | SLC44A3 activity raises TJP3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.51× lower at baseline in the lines without SLC44A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[ANXA3]] | B | SLC44A3 activity raises ANXA3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.48× lower at baseline in the lines without SLC44A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[FRK]] | B | SLC44A3 activity raises FRK's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 4.33× lower at baseline in the lines without SLC44A3 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[INAVA]] | B | SLC44A3 activity raises INAVA's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.92× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[LINC00857]] | B | SLC44A3 activity raises LINC00857's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[PLEKHG1]] | B | SLC44A3 activity raises PLEKHG1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TMC4]] | B | SLC44A3 activity raises TMC4's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[CLDN3]] | B | SLC44A3 activity raises CLDN3's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.39× lower at baseline in the lines without SLC44A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[RNF43]] | B | SLC44A3 activity raises RNF43's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without SLC44A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 49.0); signed map (57.3, 4.9). **Vector** length 81.5, 19.0% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +5.5 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +5.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.2 | -9.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.1 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 44 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:94,820,342-94,895,246 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45474, CTL3 |
| Gene groups (HGNC) | Solute carrier family 44 |
| Reactome | 8 pathways, smallest: SLC-mediated bile acid transport; SLC-mediated transport of organic anions; Synthesis of PC |
| Matched by | ensembl_id |

UniProt [Q8N4M1](https://www.uniprot.org/uniprotkb/Q8N4M1) carries no function annotation.

**Summary**, from NCBI Gene [126969](https://www.ncbi.nlm.nih.gov/gene/126969):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28689) · Entrez [126969](https://www.ncbi.nlm.nih.gov/gene/126969) · UniProt [Q8N4M1](https://www.uniprot.org/uniprotkb/Q8N4M1) · Ensembl [ENSG00000143036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143036)

## Data

Gene col 6672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6672); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6672]; `tensor/DDL_lfc|DDL_z.npy` [6672]; `embed/gene_vectors.npy` [6672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6672 or target_col == 6672). Every well: [[SLC44A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC44A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
