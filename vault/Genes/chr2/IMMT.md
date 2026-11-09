---
symbol: "IMMT"
type: "gene"
col: 5295
ensembl_id: "ENSG00000132305"
name: "inner membrane mitochondrial protein"
location: "2p11.2"
module: 6
arm: "+"
pooled_cpm: 127.29
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# IMMT

*inner membrane mitochondrial protein* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.39× (z +7.5, q 2e-11, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.678× (z -12.4, q 2e-32, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.715× (z -10.7, q 5e-24, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC150]] (+0.61, fdr 9e-06), [[MPHOSPH9]] (+0.57, fdr 2e-05), [[KPNB1]] (+0.55, fdr 2e-05); moves opposite to [[RNF103]] (-0.57, fdr 1e-05), [[RNF103-CHMP3]] (-0.55, fdr 3e-05), [[TRIM8]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00944]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +7.5 | 2e-11 | 38/48 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +7.5 | 2e-11 | 36/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.38×** | +7.3 | 6e-11 | 34/49 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.39×** | +7.2 | 7e-11 | 30/44 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.5 | 1e-08 | 33/48 (SNU-423, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.21×** | +4.4 | 0.001 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.20×** | +4.2 | 0.002 | 23/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.088 | 21/48 (SW1417, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.12 | 12/49 (NCI-H1573, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.678×** | -12.4 | 2e-32 | 43/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -10.7 | 5e-24 | 36/49 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -8.9 | 7e-17 | 2/50 (MIA PaCa-2, SW 1088) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.697×** | -8.1 | 7e-14 | 39/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.741×** | -6.7 | 2e-09 | 34/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -6.6 | 5e-09 | 30/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -6.3 | 2e-08 | 34/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.756×** | -6.3 | 2e-08 | 28/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -5.6 | 2e-06 | 34/48 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -5.3 | 8e-06 | 29/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -5.2 | 9e-06 | 21/48 (A-427, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.812×** | -4.7 | 1e-04 | 23/48 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -4.6 | 2e-04 | 22/48 (NCI-H23, PANC-1, …) | inconsistent across doses | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 0.839× | -3.8 | 0.006 | 20/47 (A-427, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.850× | -3.6 | 0.011 | 13/48 (SW48, A-427, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.761×** | -3.2 | 0.038 | 17/50 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.862× | -3.2 | 0.038 | 16/48 (A549, hTERT-HPNE, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.869× | -3.2 | 0.038 | 12/49 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.056 | 12/48 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.893× | -3.0 | 0.065 | 7/48 (A-427, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 205 | 5 (5 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.3) ⚠ cell-cycle shift, explains ~90% of this change | [[Panobinostat (drug)]] 5 µM 0.500× (z -11.5) |
| [[A498 (line)]] | wt | 145 | 0 | 7 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.585× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.524× (z -10.4) |
| [[LoVo (line)]] | wt | 91.8 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.35× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Selinexor (drug)]] 5 µM 0.610× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 128 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +12.3) ⚠ cell-cycle shift, explains ~90% of this change | [[Selinexor (drug)]] 5 µM 0.631× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 214 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.609× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.5) |
| [[HOP62 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -11.8) |
| [[KATO III (line)]] | alt | 127 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.524× (z -8.5) |
| [[LS 180 (line)]] | wt | 97.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Selinexor (drug)]] 5 µM 0.584× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 176 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.41× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.453× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 228 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -13.2) |
| [[SW480 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[A-172 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.615× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 80.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 95.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.593× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.486× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.0) |
| [[J82 (line)]] | alt | 92.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.583× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.579× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 148 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 121 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.498× (z -8.7) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SNU-423 (line)]] | alt | 92.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW 900 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.572× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.531× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC150]] | +0.61 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[MPHOSPH9]] | +0.57 | +0.49 / +0.58 | both halves | 2e-05 |  |
| [[KPNB1]] | +0.55 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[NCAPD3]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[HSD17B4]] | +0.55 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[TUBGCP3]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LHPP]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CSE1L]] | +0.54 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PRIM1]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[BLMH]] | +0.53 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[R3HDM1]] | +0.53 | +0.24 / +0.68 | both halves | 5e-04 | same gene group |
| [[POT1]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF103]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[TRIM8]] | -0.53 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CHMP4B]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SMIM4]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RRAGC-DT]] | -0.51 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[CD63]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZNF580]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[KLHL21]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[OTUD7B]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LYST]] | -0.49 | -0.57 / -0.39 | both halves | 5e-05 | same gene group |
| [[FAM117A]] | -0.49 | -0.48 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00944]] | B | LINC00944 activity lowers IMMT's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.17× higher at baseline in the lines without LINC00944 | 0.029 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[PSMB5]] | B | PSMB5 activity lowers IMMT's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.0, -42.4); signed map (-33.9, -41.4). **Vector** length 103, 30.1% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.8 | -12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -5.3 | -4.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | -4.8 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -10.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.8 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | inner membrane mitochondrial protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,143,932-86,195,472 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P87, P89, HMP, MINOS2, Mic60, MICOS60 |
| Gene groups (HGNC) | Mitochondrial contact site and cristae organizing system subunits; MicroRNA protein coding host genes |
| Hallmark sets | ADIPOGENESIS, MTORC1_SIGNALING, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16891](https://www.uniprot.org/uniprotkb/Q16891) (MICOS complex subunit MIC60):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane. Plays an important role in the maintenance of the MICOS complex stability and the mitochondrial cristae morphology.

**Summary**, from NCBI Gene [10989](https://www.ncbi.nlm.nih.gov/gene/10989):

> Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6047) · Entrez [10989](https://www.ncbi.nlm.nih.gov/gene/10989) · UniProt [Q16891](https://www.uniprot.org/uniprotkb/Q16891) · Ensembl [ENSG00000132305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132305)

## Data

Gene col 5295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5295); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5295]; `tensor/DDL_lfc|DDL_z.npy` [5295]; `embed/gene_vectors.npy` [5295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5295 or target_col == 5295). Every well: [[IMMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
