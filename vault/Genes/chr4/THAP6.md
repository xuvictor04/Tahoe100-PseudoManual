---
symbol: "THAP6"
type: "gene"
col: 10527
ensembl_id: "ENSG00000174796"
name: "THAP domain containing 6"
location: "4q21.1"
module: 11
arm: "+"
pooled_cpm: 19.77
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# THAP6

*THAP domain containing 6* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.44× (z +9.7, q 1e-19, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.41× (z +9.2, q 8e-18, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.517× (z -12.0, q 2e-30, down in 36 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.703× (z -6.7, q 5e-09, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF226]] (+0.76, fdr 7e-06), [[THAP1]] (+0.72, fdr 1e-05), [[MED18]] (+0.71, fdr 7e-06); moves opposite to [[PLXND1]] (-0.63, fdr 4e-05), [[VAV2]] (-0.62, fdr 1e-05), [[ACOT7]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC28A2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.44×** | +9.7 | 1e-19 | 33/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.2 | 8e-18 | 27/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 1e-08 | 24/47 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +6.3 | 4e-08 | 23/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.9 | 3e-07 | 22/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +5.4 | 5e-06 | 17/48 (KATO III, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.32×** | +5.3 | 9e-06 | 21/48 (SW480, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +5.2 | 1e-05 | 22/48 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +5.1 | 3e-05 | 16/48 (A498, C-33 A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.7 | 1e-04 | 15/48 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.6 | 2e-04 | 19/44 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +4.3 | 9e-04 | 16/48 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.009 | 13/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.011 | 8/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.013 | 7/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.017 | 5/48 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.035 | 9/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.039 | 9/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.064 | 9/48 (H4, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.517×** | -12.0 | 2e-30 | 36/46 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.663×** | -7.8 | 2e-12 | 26/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -6.7 | 5e-09 | 24/48 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.705×** | -6.6 | 6e-09 | 24/42 (SHP-77, RPMI-7951, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -6.3 | 2e-08 | 25/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.753×** | -5.3 | 8e-06 | 23/48 (PANC-1, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.746×** | -5.1 | 3e-05 | 17/37 (Panc 03.27, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.760×** | -5.0 | 5e-05 | 18/32 (NCI-H1573, LoVo, …) | all doses, flat | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.618×** | -4.8 | 1e-04 | 21/46 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.784×** | -4.6 | 3e-04 | 19/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -4.6 | 3e-04 | 16/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.646×** | -4.3 | 8e-04 | 18/41 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.795×** | -4.1 | 0.002 | 16/48 (MIA PaCa-2, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.761×** | -3.7 | 0.010 | 10/48 (NCI-H460, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.014 | 12/46 (RPMI-7951, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.015 | 11/46 (HS-578T, J82, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.016 | 14/45 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 0.894× | -3.0 | 0.079 | 6/48 (SW 1088, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 27.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.6) |
| [[PANC-1 (line)]] | alt | 19.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[C32 (line)]] | wt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW480 (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0338× (z -11.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H2347 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.18× (z +8.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.176× (z -9.1) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF226]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[THAP1]] | +0.72 | +0.73 / +0.57 | both halves | 1e-05 | same gene group |
| [[MED18]] | +0.71 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[GIN1]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[YAE1]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[C3orf38]] | +0.68 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.67 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.67 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[METTL6]] | +0.67 | +0.77 / +0.38 | both halves | 6e-05 |  |
| [[ZNF397]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[KRT10-AS1]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ZNF264]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXND1]] | -0.63 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[VAV2]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.60 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TBCD]] | -0.57 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[CTBP2]] | -0.56 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[ARHGAP8]] | -0.56 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[WNK2]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[LRP8]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TCF3]] | -0.56 | -0.63 / -0.40 | both halves | 4e-05 |  |
| [[PSME4]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC28A2-AS1]] | B | SLC28A2-AS1 activity raises THAP6's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without SLC28A2-AS1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF419]] | C | ZNF419 activity raises THAP6's level | lines that do not express ZNF419 (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without ZNF419 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: UBA6-DT, ENSG00000251379, ZNF264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-27.2, 16.9); signed map (5.1, -19.2). **Vector** length 69.0, 11.7% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.6 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.4 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -3.1 | -6.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -2.8 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +2.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,513,946-75,550,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC30052 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

UniProt [Q8TBB0](https://www.uniprot.org/uniprotkb/Q8TBB0) carries no function annotation.

**Summary**, from NCBI Gene [152815](https://www.ncbi.nlm.nih.gov/gene/152815):

> Predicted to enable DNA-binding transcription factor activity; sequence-specific DNA binding activity; and zinc ion binding activity. Predicted to be involved in DNA-templated transcription; endothelial cell proliferation; and regulation of DNA-templated transcription. Located in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23189) · Entrez [152815](https://www.ncbi.nlm.nih.gov/gene/152815) · UniProt [Q8TBB0](https://www.uniprot.org/uniprotkb/Q8TBB0) · Ensembl [ENSG00000174796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174796)

## Data

Gene col 10527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10527); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10527]; `tensor/DDL_lfc|DDL_z.npy` [10527]; `embed/gene_vectors.npy` [10527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10527 or target_col == 10527). Every well: [[THAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
