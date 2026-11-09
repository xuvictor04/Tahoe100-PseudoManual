---
symbol: "FAM83G"
type: "gene"
col: 12019
ensembl_id: "ENSG00000188522"
name: "scaffolding CK1 anchoring protein G"
location: "17p11.2"
module: 101
arm: "+"
pooled_cpm: 15.69
n_lines_expressing: 44
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# FAM83G

*scaffolding CK1 anchoring protein G* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.99× (z +22.9, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.559× (z -6.6, q 3e-08, down in 14 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.650× (z -4.9, q 2e-04, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KHNYN]] (+0.70, fdr 7e-06), [[SOWAHC]] (+0.67, fdr 7e-06), [[ZNF562]] (+0.64, fdr 7e-06); moves opposite to [[RCN2]] (-0.60, fdr 7e-06), [[PPP2R5E]] (-0.60, fdr 1e-05), [[PEBP1]] (-0.59, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Docetaxel (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.99×** | +22.9 | 0e+00 | 37/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.00×** | +12.9 | 2e-35 | 37/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.86×** | +7.3 | 6e-11 | 36/41 (SW 900, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +7.1 | 1e-10 | 25/41 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +6.1 | 1e-07 | 24/41 (KATO III, SW480, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +4.8 | 2e-04 | 23/41 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +4.6 | 3e-04 | 20/41 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.3 | 0.001 | 20/41 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.002 | 19/41 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.008 | 14/40 (SNU-423, SW48, …) | two highest doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.008 | 18/40 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.029 | 15/41 (LS 180, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.029 | 17/41 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.059 | 9/40 (HOP62, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +3.2 | 0.060 | 11/41 (KATO III, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.062 | 12/41 (KATO III, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.097 | 16/41 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -6.6 | 3e-08 | 14/25 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.608×** | -5.9 | 1e-06 | 22/36 (KATO III, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.650×** | -4.9 | 2e-04 | 25/41 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.675×** | -4.8 | 2e-04 | 24/42 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.668×** | -4.7 | 2e-04 | 19/41 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.672×** | -4.4 | 1e-03 | 19/40 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.731×** | -4.3 | 0.001 | 21/41 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.740×** | -4.1 | 0.003 | 17/42 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.513×** | -4.1 | 0.003 | 18/38 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.533×** | -3.9 | 0.006 | 11/24 (NCI-H1573, A549, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.722×** | -3.8 | 0.006 | 16/41 (H4, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.713×** | -3.8 | 0.006 | 12/40 (HOP62, J82, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.797×** | -3.6 | 0.011 | 16/41 (NCI-H23, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.734×** | -3.6 | 0.011 | 21/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.750×** | -3.6 | 0.011 | 15/41 (NCI-H23, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.736×** | -3.3 | 0.030 | 10/41 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | **0.754×** | -3.2 | 0.045 | 13/40 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.827×** | -3.2 | 0.050 | 16/41 (AsPC-1, HT-29, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +22.7) | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +19.8) | — |
| [[A549 (line)]] | wt | 24.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 15.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +15.8) | [[AZD-7648 (drug)]] 0.5 µM 0.0430× (z -9.3) |
| [[KATO III (line)]] | alt | 30.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0974× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 23.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +14.4) | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -9.0) ⚠ position not correctable |
| [[AsPC-1 (line)]] | alt | 16.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +17.1) | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 0.5 µM 0.0848× (z -8.5) |
| [[HOP62 (line)]] | alt | 27.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -12.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 18.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 19.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +12.5) | [[Adagrasib (drug)]] 0.05 µM 0.622× (z -10.8) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 15.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 11.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +14.8) | — |
| [[A-172 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -9.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -8.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 9.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +14.4) | — |
| [[HepG2_C3A (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +14.9) | — |
| [[Hs 766T (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 9.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +8.9) | — |
| [[RKO (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.234× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +15.9) | — |
| [[SW480 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.4) | — |
| [[A-427 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHNYN]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SOWAHC]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ZNF562]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZYX]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SERPINB8]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZNF222]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[AGO2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZNF274]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ABR]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ALOXE3]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | -0.60 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[PPP2R5E]] | -0.60 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PEBP1]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ARL6IP5]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[LGR4]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CTDSPL2]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[USP33]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RSBN1L]] | -0.54 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[CBX1]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CNOT6L]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[STK38]] | -0.53 | -0.68 / -0.36 | both halves | 9e-05 |  |
| [[CDC42SE2]] | -0.53 | -0.63 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises FAM83G's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Docetaxel (drug)]] 0.05 µM | C | FAM83G activity lowers the cells' numbers under Docetaxel 0.05 µM (makes them more sensitive) | lines that do not express FAM83G (6) vs lines expressing it (42) | the lines without FAM83G: 1.67× the cells of the other lines | 0.090 | ⚠ tissue-confounded; across organs; also absent: FBLIM1, PSD4, LINC02977 |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, -2.9); signed map (4.2, 33.2). **Vector** length 98.2, 23.9% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +22.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.9 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +0.4 |
|  | [[NG25 (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,968,789-19,004,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41564, PAWS1; previously FAM83G |
| Gene groups (HGNC) | Scaffolding anchor of CK1 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A6ND36](https://www.uniprot.org/uniprotkb/A6ND36) (Scaffolding CK1 anchoring protein G):

> Substrate for type I BMP receptor kinase involved in regulation of some target genes of the BMP signaling pathway. Also regulates the expression of several non-BMP target genes, suggesting a role in other signaling pathways.

**Summary**, from NCBI Gene [644815](https://www.ncbi.nlm.nih.gov/gene/644815):

> Predicted to enable protein kinase binding activity. Involved in BMP signaling pathway. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32554) · Entrez [644815](https://www.ncbi.nlm.nih.gov/gene/644815) · UniProt [A6ND36](https://www.uniprot.org/uniprotkb/A6ND36) · Ensembl [ENSG00000188522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188522)

## Data

Gene col 12019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12019); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12019]; `tensor/DDL_lfc|DDL_z.npy` [12019]; `embed/gene_vectors.npy` [12019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12019 or target_col == 12019). Every well: [[FAM83G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
