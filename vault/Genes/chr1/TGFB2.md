---
symbol: "TGFB2"
type: "gene"
col: 1715
ensembl_id: "ENSG00000092969"
name: "transforming growth factor beta 2"
location: "1q41"
module: 66
arm: "+"
pooled_cpm: 72.53
n_lines_expressing: 35
n_dd_up: 40
n_dd_down: 12
n_dd_up_clean: 32
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TGFB2

*transforming growth factor beta 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +19.1, q 0e+00, up in 21 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.644× (z -7.9, q 1e-12, down in 21 of 33 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.717× (z -6.0, q 3e-07, down in 17 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDB2]] (+0.72, fdr 7e-06), [[ROS1]] (+0.71, fdr 7e-06), [[ALPK2]] (+0.68, fdr 7e-06); moves opposite to [[PGF]] (-0.54, fdr 3e-05), [[FXYD5]] (-0.53, fdr 2e-05), [[EIF4EBP1]] (-0.51, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[EFEMP1]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[crizotinib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +19.1 | 0e+00 | 21/33 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +11.4 | 1e-27 | 21/33 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +10.9 | 3e-25 | 15/27 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +10.6 | 6e-24 | 19/31 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +10.2 | 3e-22 | 16/29 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +8.9 | 8e-17 | 16/33 (PANC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +8.5 | 2e-15 | 21/34 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +8.4 | 2e-15 | 17/33 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +8.1 | 4e-14 | 17/33 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.8 | 5e-10 | 17/33 (Hs 766T, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.44×** | +6.7 | 1e-09 | 18/33 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 2e-09 | 19/32 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +6.1 | 4e-08 | 20/33 (HOP62, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +6.0 | 1e-07 | 20/31 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 8e-07 | 18/33 (HOP62, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +5.5 | 1e-06 | 14/32 (A-172, HS-578T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +5.0 | 2e-05 | 17/33 (HOP62, C32, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +4.8 | 5e-05 | 10/33 (A-172, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.644×** | -7.9 | 1e-12 | 21/33 (SW48, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.647×** | -7.8 | 1e-12 | 20/33 (SW48, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.717×** | -6.0 | 3e-07 | 17/32 (NCI-H2030, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.791×** | -6.0 | 3e-07 | 20/33 (NCI-H2030, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.718×** | -6.0 | 3e-07 | 17/33 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.751×** | -5.0 | 6e-05 | 15/32 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **0.770×** | -4.4 | 0.001 | 10/32 (NCI-H2030, A498, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.801×** | -4.0 | 0.004 | 16/32 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.818×** | -3.6 | 0.016 | 11/32 (A549, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.812×** | -3.6 | 0.016 | 13/30 (J82, SW48, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.884× | -3.2 | 0.075 | 11/33 (J82, SW 900, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **0.698×** | -3.1 | 0.078 | 4/33 (HEC-1-A, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.700×** | -3.1 | 0.078 | 8/32 (CFPAC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.838× | -3.1 | 0.078 | 10/31 (SNU-423, NCI-H661, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.887× | -3.1 | 0.078 | 14/34 (PANC-1, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 187 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -15.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.8) |
| [[HOP62 (line)]] | alt | 94.0 | 9 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.11× (z +15.1) ⚠ position not correctable · without an alert: [[Tucidinostat (drug)]] 5 µM 3.66× (z +10.3) | — |
| [[A-172 (line)]] | wt | 58.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +14.7) | — |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -14.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.168× (z -13.8) |
| [[PANC-1 (line)]] | alt | 71.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +24.8) | — |
| [[A498 (line)]] | wt | 221 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 66.9 | 5 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.64× (z +13.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.8) | — |
| [[C32 (line)]] | wt | 26.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 123 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.302× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 310 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -10.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -11.6) |
| [[SNU-423 (line)]] | alt | 132 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.9) | — |
| [[A549 (line)]] | wt | 86.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.163× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 127 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.283× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.176× (z -12.3) ⚠ cell-cycle shift, explains ~86% of this change |
| [[SW 900 (line)]] | alt | 238 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.9) | — |
| [[A-427 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDB2]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ROS1]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ALPK2]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SEMA3C]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[NFIB]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[LATS2]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FIGN]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BDNF]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 | STRING 424 |
| [[EFEMP1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 | pathway: Elastic fibre formation; STRING 471 |
| [[COL12A1]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[RHOBTB3]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DIO2]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGF]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 | STRING 558 |
| [[FXYD5]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[EIF4EBP1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SH2B3]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RAC2]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 | pathway: Platelet activation, signaling and aggregation |
| [[SHANK1]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SH3PXD2A]] | -0.48 | -0.50 / -0.39 | both halves | 6e-05 | pathway: Extracellular matrix organization |
| [[CARD19]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[STX1A]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TM4SF19]] | -0.47 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[CIB1]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFEMP1]] | B | EFEMP1 activity raises TGFB2's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 4.42× lower at baseline in the lines without EFEMP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[TNS3]] | B | TNS3 activity raises TGFB2's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without TNS3 | 0.046 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[LINC02057]] | B | LINC02057 activity raises TGFB2's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 3.85× lower at baseline in the lines without LINC02057 | 0.048 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[CPS1]] | B | CPS1 activity raises TGFB2's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 1.71× lower at baseline in the lines without CPS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R |
| [[ARID5B]] | B | ARID5B activity raises TGFB2's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 3.23× lower at baseline in the lines without ARID5B | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[CCBE1]] | B | CCBE1 activity raises TGFB2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without CCBE1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[LINC00472]] | B | LINC00472 activity raises TGFB2's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 3.44× lower at baseline in the lines without LINC00472 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT |
| [[CDH2]] | B | CDH2 activity strengthens TGFB2's drug response | lines that do not express CDH2 (9) vs lines expressing it (25) | the lines without CDH2 respond 0.12× as strongly (z diff +3.38); strongest at Homoharringtonine 5 µM: 0.86x vs 2.30x (z diff +7.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; target measured in part of the lines; artifact flags |
| [[ARHGAP42]] | B | ARHGAP42 activity raises TGFB2's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without ARHGAP42 | 0.094 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[PALLD]] | B | PALLD activity raises TGFB2's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without PALLD | 0.098 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[NALCN]] | C | NALCN activity raises TGFB2's level | lines that do not express NALCN (22) vs lines expressing it (28) | 3.62× lower at baseline in the lines without NALCN | 0.078 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises TGFB2's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 3.96× lower at baseline in the lines without FAT4 | 0.082 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[crizotinib (drug)]] 5 µM | B | TGFB2 activity raises the cells' numbers under crizotinib 5 µM (protects the cells) | lines that do not express TGFB2 (15) vs lines expressing it (33) | the lines without TGFB2: 0.90× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| [[DIO2]] | B | TGFB2 activity raises DIO2's level | lines that do not express TGFB2 (15) vs lines expressing it (35) | 2.71× lower at baseline in the lines without TGFB2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| [[ARID5B]] | B | TGFB2 activity raises ARID5B's level | lines that do not express TGFB2 (15) vs lines expressing it (35) | 1.33× lower at baseline in the lines without TGFB2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| cells under [[Carbamazepine (drug)]] 0.5 µM | B | TGFB2 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express TGFB2 (15) vs lines expressing it (33) | the lines without TGFB2: 1.15× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |
| [[NEXN]] | B | TGFB2 activity raises NEXN's level | lines that do not express TGFB2 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without TGFB2 | 0.097 | ⚠ within organs, on part of the lines; also absent: CTSF, EHD3, MAP9 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.9, 21.3); signed map (47.1, 20.4). **Vector** length 130, 36.8% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +10.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.1 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | +4.8 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +6.0 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.9 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -7.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -6.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.0 | -6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:218,345,336-218,444,619 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Transforming growth factor beta family |
| Hallmark sets | KRAS_SIGNALING_DN, ALLOGRAFT_REJECTION, APOPTOSIS, XENOBIOTIC_METABOLISM |
| Reactome | 13 pathways, smallest: TGFBR3 regulates TGF-beta signaling; Molecules associated with elastic fibres; Elastic fibre formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P61812](https://www.uniprot.org/uniprotkb/P61812) (Transforming growth factor beta-2 proprotein):

> [Transforming growth factor beta-2 proprotein]: Precursor of the Latency-associated peptide (LAP) and Transforming growth factor beta-2 (TGF-beta-2) chains, which constitute the regulatory and active subunit of TGF-beta-2, respectively.; [Latency-associated peptide]: Required to maintain the Transforming growth factor beta-2 (TGF-beta-2) chain in a latent state during storage in extracellular matrix (By similarity). Associates non-covalently with TGF-beta-2 and regulates its activation via …

**Summary**, from NCBI Gene [7042](https://www.ncbi.nlm.nih.gov/gene/7042):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate a latency-associated peptide (LAP) and a mature peptide, and is found in either a latent form composed of a mature peptide homodimer, a LAP homodimer, and a …

**Accessions** — [HGNC:11768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11768) · Entrez [7042](https://www.ncbi.nlm.nih.gov/gene/7042) · UniProt [P61812](https://www.uniprot.org/uniprotkb/P61812) · Ensembl [ENSG00000092969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092969)

## Data

Gene col 1715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1715); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1715]; `tensor/DDL_lfc|DDL_z.npy` [1715]; `embed/gene_vectors.npy` [1715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1715 or target_col == 1715). Every well: [[TGFB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
