---
symbol: "RBM47"
type: "gene"
col: 8756
ensembl_id: "ENSG00000163694"
name: "RNA binding motif protein 47"
location: "4p14"
module: 8
arm: "+"
pooled_cpm: 103.55
n_lines_expressing: 30
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 100
direction_downstream: 88
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RBM47

*RNA binding motif protein 47* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +10.8, q 1e-24, up in 12 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.692× (z -6.4, q 4e-08, down in 17 of 28 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.730× (z -5.7, q 2e-06, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM31]] (+0.76, fdr 7e-06), [[FRK]] (+0.75, fdr 7e-06), [[MUC4]] (+0.74, fdr 7e-06); moves opposite to [[SMYD2]] (-0.53, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 100 arrows point to it, the strongest [[ADGRF4]] → it (grade B ⚠); 88 go from it, the strongest it → [[MAP3K8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +10.8 | 1e-24 | 12/28 (A498, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 1e-14 | 13/29 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +6.2 | 9e-08 | 19/28 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +5.8 | 8e-07 | 20/28 (HEC-1-A, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +5.0 | 5e-05 | 17/29 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.36×** | +5.0 | 6e-05 | 17/28 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +4.8 | 1e-04 | 20/30 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.7 | 2e-04 | 4/26 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +4.2 | 0.001 | 14/28 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.006 | 17/29 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.011 | 9/28 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.018 | 19/28 (HEC-1-A, AsPC-1, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.018 | 7/28 (NCI-H2347, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.018 | 16/28 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.20×** | +3.4 | 0.023 | 7/28 (A498, SW1417, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.027 | 13/29 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.047 | 16/28 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.050 | 3/28 (AsPC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -6.4 | 4e-08 | 17/28 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.779×** | -6.4 | 4e-08 | 20/27 (LoVo, CFPAC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.730×** | -5.7 | 2e-06 | 22/28 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.731×** | -5.7 | 2e-06 | 18/28 (LoVo, LS 180, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.741×** | -5.2 | 2e-05 | 19/28 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.794×** | -4.2 | 0.003 | 14/28 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.797×** | -4.1 | 0.003 | 16/28 (BT-474, SW 900, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.804×** | -4.0 | 0.005 | 9/28 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.809×** | -3.9 | 0.007 | 18/28 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.862× | -3.8 | 0.008 | 19/29 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.812×** | -3.8 | 0.008 | 16/28 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.813×** | -3.8 | 0.008 | 15/28 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.678×** | -3.7 | 0.009 | 14/20 (SW1417, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.818×** | -3.7 | 0.010 | 18/28 (SW 900, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.013 | 12/28 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.696×** | -3.5 | 0.019 | 15/28 (CFPAC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.020 | 20/29 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.715×** | -3.2 | 0.035 | 13/28 (CFPAC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.041 | 17/28 (BT-474, A549, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.849× | -2.9 | 0.093 | 10/28 (BT-474, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 104 | 0 | 14 (13 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -15.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.268× (z -13.1) |
| [[LoVo (line)]] | wt | 252 | 0 | 13 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 378 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -14.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -11.8) |
| [[HT-29 (line)]] | alt | 417 | 0 | 10 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.262× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~57% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.356× (z -11.2) |
| [[BT-474 (line)]] | alt | 338 | 1 (1 ⚠) | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -19.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 118 | 7 (2 ⚠) | 1 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.31× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.519× (z -8.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[LS 180 (line)]] | wt | 289 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 458 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 290 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.4) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A498 (line)]] | wt | 66.4 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.84× (z +15.6) | — |
| [[Panc 03.27 (line)]] | alt | 202 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.331× (z -9.7) |
| [[SW480 (line)]] | alt | 36.6 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.03× (z +10.9) | [[Digitoxin (drug)]] 0.5 µM 0.351× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +9.9) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H1573 (line)]] | alt | 131 | 1 (1 ⚠) | 2 (2 ⚠) | [[Trametinib (drug)]] 5 µM 2.51× (z +8.9) ⚠ cell-cycle shift, explains ~22% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -12.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SW 900 (line)]] | alt | 201 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -14.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[KATO III (line)]] | alt | 295 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 105 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 2.83× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.98× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 28.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.02× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 66.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.182× (z -9.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM31]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[FRK]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HHLA2]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[FRMD4B]] | +0.70 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMC5]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.70 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[POF1B]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ELF3]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[MMP7]] | +0.68 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD2]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*100 arrows, 100 of them with an alert ⚠; grade A 0, B 42, C 58. Shown: the 12 strongest; 88 more arrows (88 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF4]] | B | ADGRF4 activity raises RBM47's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 4.27× lower at baseline in the lines without ADGRF4 | 0.001 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[PTPRB]] | B | PTPRB activity raises RBM47's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 3.27× lower at baseline in the lines without PTPRB | 0.002 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[RNF183]] | B | RNF183 activity raises RBM47's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 3.87× lower at baseline in the lines without RNF183 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[VNN1]] | B | VNN1 activity raises RBM47's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[RAB27B]] | B | RAB27B activity raises RBM47's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 3.71× lower at baseline in the lines without RAB27B | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[PLCH1]] | B | PLCH1 activity raises RBM47's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 4.18× lower at baseline in the lines without PLCH1 | 0.005 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TCN1]] | B | TCN1 activity raises RBM47's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 4.51× lower at baseline in the lines without TCN1 | 0.006 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[DUOX2]] | B | DUOX2 activity raises RBM47's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without DUOX2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[RASEF]] | B | RASEF activity raises RBM47's level | lines that do not express RASEF (20) vs lines expressing it (30) | 3.56× lower at baseline in the lines without RASEF | 0.007 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[TNFSF10]] | B | TNFSF10 activity raises RBM47's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 3.17× lower at baseline in the lines without TNFSF10 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[MUC4]] | B | MUC4 activity raises RBM47's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 5.12× lower at baseline in the lines without MUC4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[MMP7]] | B | MMP7 activity raises RBM47's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 4.23× lower at baseline in the lines without MMP7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |

### Downstream of this gene

*88 arrows, 88 of them with an alert ⚠; grade A 0, B 43, C 45. Shown: the 12 strongest; 76 more arrows (76 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K8]] | B | RBM47 activity raises MAP3K8's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without RBM47 | 0.003 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[EFNA1]] | B | RBM47 activity raises EFNA1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without RBM47 | 0.005 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[RDH10]] | B | RBM47 activity raises RDH10's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without RBM47 | 0.008 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[MTUS1]] | B | RBM47 activity raises MTUS1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 3.50× lower at baseline in the lines without RBM47 | 0.008 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[SLC37A1]] | B | RBM47 activity raises SLC37A1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without RBM47 | 0.011 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[NBPF15]] | B | RBM47 activity lowers NBPF15's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.66× higher at baseline in the lines without RBM47 | 0.011 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[LGALS9]] | B | RBM47 activity raises LGALS9's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.41× lower at baseline in the lines without RBM47 | 0.012 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[CTNND1]] | B | RBM47 activity raises CTNND1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.77× lower at baseline in the lines without RBM47 | 0.013 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[AKR1C3]] | B | RBM47 activity raises AKR1C3's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.92× lower at baseline in the lines without RBM47 | 0.013 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[PLCH1]] | B | RBM47 activity raises PLCH1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.95× lower at baseline in the lines without RBM47 | 0.013 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[ATP1B1]] | B | RBM47 activity raises ATP1B1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without RBM47 | 0.016 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[EPB41L1]] | B | RBM47 activity raises EPB41L1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.62× lower at baseline in the lines without RBM47 | 0.019 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, 54.6); signed map (59.4, 3.2). **Vector** length 117, 38.8% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.58 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +8.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +6.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | +3.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:40,423,267-40,630,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20273, NET18 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [A0AV96](https://www.uniprot.org/uniprotkb/A0AV96) (RNA-binding protein 47):

> Single-stranded RNA-binding protein that functions in a variety of RNA processes, including alternative splicing, RNA stabilization, and RNA editing. Functions as an enzyme-substrate adapter for the cytidine deaminase APOBEC1. With APOBEC1 forms an mRNA editing complex involved into cytidine to uridine editing of a variety of mRNA molecules. Through the binding of their 3'UTR, also stabilizes a variety of mRNAs and regulates the expression of genes such as the interferon alpha/beta receptor and …

**Summary**, from NCBI Gene [54502](https://www.ncbi.nlm.nih.gov/gene/54502):

> Enables enzyme binding activity; enzyme-substrate adaptor activity; and mRNA 3'-UTR binding activity. Involved in cytidine to uridine editing; positive regulation of type I interferon-mediated signaling pathway; and regulation of mRNA metabolic process. Located in cytoplasm and nucleus. Part of apolipoprotein B mRNA editing enzyme complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30358) · Entrez [54502](https://www.ncbi.nlm.nih.gov/gene/54502) · UniProt [A0AV96](https://www.uniprot.org/uniprotkb/A0AV96) · Ensembl [ENSG00000163694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163694)

## Data

Gene col 8756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8756); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8756]; `tensor/DDL_lfc|DDL_z.npy` [8756]; `embed/gene_vectors.npy` [8756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8756 or target_col == 8756). Every well: [[RBM47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
