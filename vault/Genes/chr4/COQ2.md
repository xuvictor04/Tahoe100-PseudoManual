---
symbol: "COQ2"
type: "gene"
col: 10339
ensembl_id: "ENSG00000173085"
name: "coenzyme Q2, polyprenyltransferase"
location: "4q21.23"
module: 51
arm: "+"
pooled_cpm: 9.89
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# COQ2

*coenzyme Q2, polyprenyltransferase* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.52× (z +17.7, q 0e+00, up in 34 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.48× (z +4.4, q 7e-04, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.599× (z -5.7, q 7e-06, down in 22 of 45 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.658× (z -4.9, q 3e-04, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROS]] (+0.62, fdr 1e-05), [[UQCC2]] (+0.62, fdr 2e-05), [[SCAF8]] (+0.60, fdr 2e-05); moves opposite to [[NOXRED1]] (-0.57, fdr 2e-04), [[ISY1-RAB43]] (-0.56, fdr 5e-05), [[RABGEF1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.52×** | +17.7 | 0e+00 | 34/36 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.40×** | +16.7 | 0e+00 | 16/16 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +11.9 | 1e-30 | 22/23 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.62×** | +5.5 | 6e-06 | 25/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.58×** | +5.4 | 8e-06 | 21/36 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.50×** | +4.8 | 2e-04 | 22/47 (A-172, SW480, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.7 | 2e-04 | 15/38 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +4.4 | 7e-04 | 18/47 (SW480, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.4 | 7e-04 | 11/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +4.2 | 0.001 | 13/39 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.96×** | +4.1 | 0.002 | 10/38 (NCI-H1573, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.41×** | +4.0 | 0.003 | 18/47 (HT-29, SW480, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.34×** | +3.4 | 0.026 | 14/47 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.026 | 7/47 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.038 | 7/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.044 | 10/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.045 | 8/41 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.045 | 7/46 (SW1417, A549, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.067 | 8/43 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.067 | 9/47 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.091 | 7/44 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.599×** | -5.7 | 7e-06 | 22/45 (SNU-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -4.9 | 3e-04 | 22/47 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -4.4 | 0.002 | 21/47 (LoVo, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.717×** | -3.9 | 0.013 | 16/46 (SNU-1, HT-29, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.546×** | -3.7 | 0.023 | 13/30 (LoVo, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -3.4 | 0.072 | 13/41 (HepG2/C3A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.582×** | -3.3 | 0.073 | 9/48 (SHP-77, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.597× | -3.2 | 0.10 | 5/48 (LS 180, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.828× | -3.1 | 0.10 | 7/47 (C-33 A, SNU-1, …) | top dose only |  |
| [[Ivermectin (drug)]] 5 µM |  | 0.766× | -3.1 | 0.10 | 3/47 (A-427, SW480, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.834× | -3.0 | 0.14 | 15/47 (A-172, NCI-H460, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.90× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 7.81 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.64 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 13.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0475× (z -10.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 8.15 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.50 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.05 µM 0.0631× (z -9.7) |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 7.99 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0808× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HT-29 (line)]] | alt | 7.63 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.69× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.94 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 8.65 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.107× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 1 | — | [[NVP-BHG712 (drug)]] 0.5 µM 0.0652× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROS]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 | STRING 465 |
| [[UQCC2]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SCAF8]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[NCAPH]] | +0.60 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[C2CD5]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PTBP2]] | +0.59 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[YEATS4]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NHLRC2]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SREK1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[POGZ]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[H2AZ2]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CENPS]] | +0.56 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOXRED1]] | -0.57 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ISY1-RAB43]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[RABGEF1]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZNF778]] | -0.54 | -0.17 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[NPIPB11]] | -0.54 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[TTLL3]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MROH1]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[RAB43]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZFC3H1]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ST6GALNAC6-1]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[DRD4]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CCDC32]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[BAHD1]] | -0.51 | -0.58 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises COQ2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.0, -46.2); signed map (6.9, -38.2). **Vector** length 68.4, 11.8% of its response variance represented; |z| ≥ 3 in 813 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.6 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.1 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.7 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -3.1 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q2, polyprenyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:83,261,536-83,284,914 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CL640, FLJ26072 |
| Reactome | 5 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96H96](https://www.uniprot.org/uniprotkb/Q96H96) (4-hydroxybenzoate polyprenyltransferase, mitochondrial):

> Mediates the second step in the final reaction sequence of coenzyme Q (CoQ) biosynthesis. Catalyzes the prenylation of para-hydroxybenzoate (PHB) with an all-trans polyprenyl donor (such as all-trans-decaprenyl diphosphate). The length of the polyprenyl side chain varies depending on the species, in humans, the side chain is comprised of 10 isoprenyls (decaprenyl) producing CoQ10 (also known as ubiquinone), whereas rodents predominantly generate CoQ9. However, this specificity is not complete, …

**Summary**, from NCBI Gene [27235](https://www.ncbi.nlm.nih.gov/gene/27235):

> This gene encodes an enzyme that functions in the final steps in the biosynthesis of CoQ (ubiquinone), a redox carrier in the mitochondrial respiratory chain and a lipid-soluble antioxidant. This enzyme, which is part of the coenzyme Q10 pathway, catalyzes the prenylation of parahydroxybenzoate with an all-trans polyprenyl group. Mutations in this gene cause coenzyme Q10 deficiency, a mitochondrial encephalomyopathy, and also COQ2 nephropathy, an inherited form of mitochondriopathy with primary …

**Accessions** — [HGNC:25223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25223) · Entrez [27235](https://www.ncbi.nlm.nih.gov/gene/27235) · UniProt [Q96H96](https://www.uniprot.org/uniprotkb/Q96H96) · Ensembl [ENSG00000173085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173085)

## Data

Gene col 10339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10339); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10339]; `tensor/DDL_lfc|DDL_z.npy` [10339]; `embed/gene_vectors.npy` [10339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10339 or target_col == 10339). Every well: [[COQ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
