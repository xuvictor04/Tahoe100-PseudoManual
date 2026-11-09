---
symbol: "PCTP"
type: "gene"
col: 6492
ensembl_id: "ENSG00000141179"
name: "phosphatidylcholine transfer protein"
location: "17q22"
module: 30
arm: "+"
pooled_cpm: 18.49
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 28
n_dd_up_clean: 12
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PCTP

*phosphatidylcholine transfer protein* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +11.2, q 4e-26, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -20.9, q 0e+00, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.439× (z -14.3, q 5e-44, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF3]] (+0.71, fdr 7e-06), [[PRUNE1]] (+0.69, fdr 1e-05), [[DPY30]] (+0.68, fdr 8e-06); moves opposite to [[PCBP1-AS1]] (-0.65, fdr 2e-05), [[GPR137]] (-0.65, fdr 6e-05), [[MZF1-AS1]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +11.2 | 4e-26 | 39/47 (LS 180, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +7.2 | 1e-10 | 26/46 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.34×** | +7.2 | 1e-10 | 22/47 (A498, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.4 | 2e-08 | 26/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 3e-07 | 25/47 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +4.6 | 4e-04 | 20/47 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 9e-04 | 14/47 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 9e-04 | 14/47 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.003 | 10/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +3.4 | 0.034 | 5/47 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.061 | 7/47 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.062 | 4/46 (Hs 766T, J82, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.080 | 3/47 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.083 | 3/47 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.088 | 12/46 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.428×** | -20.9 | 0e+00 | 41/46 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.439×** | -14.3 | 5e-44 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -12.9 | 1e-35 | 34/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -11.9 | 2e-30 | 31/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.522×** | -10.9 | 2e-25 | 30/43 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -10.5 | 1e-23 | 32/45 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.324×** | -10.3 | 9e-23 | 38/47 (NCI-H460, CHP-212, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -9.9 | 2e-21 | 33/46 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.566×** | -8.9 | 3e-17 | 30/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -8.2 | 2e-14 | 31/43 (BT-474, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -8.0 | 6e-14 | 23/46 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -7.4 | 5e-12 | 25/46 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -7.4 | 7e-12 | 27/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -6.9 | 2e-10 | 22/41 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -6.4 | 5e-09 | 23/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -5.1 | 1e-05 | 22/47 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.001 | 15/46 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.814×** | -3.4 | 0.017 | 8/46 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.4 | 0.018 | 13/47 (NCI-H460, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.7 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -25.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -18.5) |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.182× (z -10.1) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -15.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.231× (z -10.1) |
| [[A498 (line)]] | wt | 29.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.320× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -9.8) |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[4EGI-1 (drug)]] 5 µM 0.0595× (z -8.8) |
| [[CHP-212 (line)]] | wt | 93.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0409× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0950× (z -10.1) |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0316× (z -15.5) |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -9.8) |
| [[A549 (line)]] | wt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.149× (z -9.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 8.55 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0861× (z -8.5) |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 8.46 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | +0.71 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PRUNE1]] | +0.69 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[DPY30]] | +0.68 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[NCK1]] | +0.67 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ARNT]] | +0.67 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[MALSU1]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.65 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PIGH]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MAST3]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SLC35A1]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[YIF1B]] | +0.63 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP1-AS1]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[GPR137]] | -0.65 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[MZF1-AS1]] | -0.64 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[LINC00571]] | -0.62 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZC3H4]] | -0.62 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[DNAJB12]] | -0.62 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZCWPW1]] | -0.62 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[CRPPA]] | -0.61 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DDX5]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.61 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[ST7L]] | -0.61 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[HIVEP2-DT]] | -0.60 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity raises PCTP's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without PLEKHA6 | 0.055 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[NR2F1-AS1]] | B | NR2F1-AS1 activity lowers PCTP's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 1.57× higher at baseline in the lines without NR2F1-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.4, -6.6); signed map (-34.8, -4.5). **Vector** length 80.5, 16.9% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.6 | +7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.7 | -20.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.9 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -12.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -7.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylcholine transfer protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:55,751,051-55,842,830 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STARD2 |
| Gene groups (HGNC) | StAR related lipid transfer domain containing |
| Reactome | 6 pathways, smallest: Synthesis of PC; Mitochondrial Fatty Acid Beta-Oxidation; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKL6](https://www.uniprot.org/uniprotkb/Q9UKL6) (Phosphatidylcholine transfer protein):

> Catalyzes the transfer of phosphatidylcholine between membranes. Binds a single lipid molecule.

**Summary**, from NCBI Gene [58488](https://www.ncbi.nlm.nih.gov/gene/58488):

> Enables phosphatidylcholine binding activity and phosphatidylcholine intramembrane carrier activity. Involved in phospholipid transport. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8752) · Entrez [58488](https://www.ncbi.nlm.nih.gov/gene/58488) · UniProt [Q9UKL6](https://www.uniprot.org/uniprotkb/Q9UKL6) · Ensembl [ENSG00000141179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141179)

## Data

Gene col 6492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6492); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6492]; `tensor/DDL_lfc|DDL_z.npy` [6492]; `embed/gene_vectors.npy` [6492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6492 or target_col == 6492). Every well: [[PCTP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCTP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
