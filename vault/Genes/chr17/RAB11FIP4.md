---
symbol: "RAB11FIP4"
type: "gene"
col: 5189
ensembl_id: "ENSG00000131242"
name: "RAB11 family interacting protein 4"
location: "17q11.2"
module: 8
arm: "+"
pooled_cpm: 18.72
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RAB11FIP4

*RAB11 family interacting protein 4* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +20.6, q 0e+00, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.334× (z -10.5, q 3e-23, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP1LC3A]] (+0.58, fdr 3e-05), [[PPFIBP2]] (+0.54, fdr 2e-05), [[ASS1]] (+0.51, fdr 2e-05); moves opposite to [[PARGP1]] (-0.47, fdr 1e-04), [[MRPS11]] (-0.46, fdr 1e-04), [[NUDT5]] (-0.43, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CLDN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +20.6 | 0e+00 | 33/44 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +12.7 | 2e-34 | 34/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +11.8 | 4e-30 | 30/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +7.1 | 1e-10 | 26/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.9 | 7e-10 | 19/44 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.2 | 7e-08 | 22/45 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.2 | 1e-05 | 18/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.005 | 22/44 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +4.0 | 0.005 | 17/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.23×** | +3.8 | 0.007 | 7/46 (HEC-1-A, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.015 | 11/45 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.5 | 0.018 | 15/46 (HS-578T, A-172, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.20×** | +3.5 | 0.018 | 6/46 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.018 | 10/46 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.20×** | +3.4 | 0.028 | 11/40 (NCI-H460, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.041 | 3/45 (LS 180, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.2 | 0.045 | 8/43 (HT-29, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.045 | 7/45 (SW480, AsPC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.13× | +3.2 | 0.045 | 8/46 (CFPAC-1, C-33 A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.055 | 9/46 (AsPC-1, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5189.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -10.5 | 3e-23 | 32/45 (SW480, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.668×** | -7.4 | 4e-11 | 24/42 (A498, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -7.0 | 6e-10 | 23/42 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.716×** | -6.1 | 1e-07 | 18/39 (SK-MEL-2, SW48, …) | inconsistent across doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.729×** | -5.8 | 8e-07 | 21/45 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.750×** | -5.3 | 1e-05 | 19/44 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.789×** | -4.3 | 0.001 | 13/44 (SNU-423, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.789×** | -4.2 | 0.002 | 19/40 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.803×** | -4.0 | 0.004 | 16/45 (COLO 205, SK-MEL-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.808×** | -3.9 | 0.005 | 14/46 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.031 | 19/45 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.840× | -3.2 | 0.066 | 9/43 (HEC-1-A, AN3 CA, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -3.1 | 0.092 | 15/45 (HT-29, SW480, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.092 | 11/45 (AsPC-1, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 66.5 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.354× (z -10.2) |
| [[PANC-1 (line)]] | alt | 7.93 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0852× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 36.0 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.378× (z -9.3) |
| [[HS-578T (line)]] | alt | 7.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.1) |
| [[A549 (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 45.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.133× (z -8.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[HOP62 (line)]] | alt | 6.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +14.2) | — |
| [[J82 (line)]] | alt | 4.91 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0990× (z -9.1) |
| [[KATO III (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 7.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0894× (z -13.7) |
| [[SNU-423 (line)]] | alt | 8.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.146× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A-172 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 41.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1LC3A]] | +0.58 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[PPFIBP2]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ASS1]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[RAP1GAP]] | +0.50 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[TP53INP2]] | +0.49 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[MYO7A]] | +0.48 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[HS6ST1]] | +0.48 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[MUC20]] | +0.48 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TUFT1]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 | same gene group |
| [[LBH]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[PNPLA2]] | +0.47 | +0.50 / +0.40 | both halves | 4e-05 |  |
| [[ST14]] | +0.47 | +0.32 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARGP1]] | -0.47 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[MRPS11]] | -0.46 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[NUDT5]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[SNRNP40]] | -0.43 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[DZIP1L]] | -0.42 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[TIMM23B]] | -0.42 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[L3HYPDH]] | -0.42 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[RBM45]] | -0.42 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[GSTCD]] | -0.42 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[TIMM23]] | -0.41 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[ITGB3BP]] | -0.41 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[KCTD1]] | -0.40 | -0.41 / -0.33 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN3]] | B | CLDN3 activity raises RAB11FIP4's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without CLDN3 | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ERBB3]] | B | ERBB3 activity raises RAB11FIP4's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.71× lower at baseline in the lines without ERBB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[LINC03040]] | B | LINC03040 activity raises RAB11FIP4's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without LINC03040 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[ST14]] | B | ST14 activity raises RAB11FIP4's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without ST14 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[SLC44A4]] | B | SLC44A4 activity raises RAB11FIP4's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without SLC44A4 | 0.033 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises RAB11FIP4's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.24× lower at baseline in the lines without TMPRSS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[IL17RE]] | B | IL17RE activity raises RAB11FIP4's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without IL17RE | 0.035 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[CDH1]] | B | CDH1 activity raises RAB11FIP4's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without CDH1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[BTBD16]] | B | BTBD16 activity lowers RAB11FIP4's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.02× higher at baseline in the lines without BTBD16 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OCLN]] | B | OCLN activity raises RAB11FIP4's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without OCLN | 0.071 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[CLIC5]] | B | CLIC5 activity raises RAB11FIP4's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.09× lower at baseline in the lines without CLIC5 | 0.083 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[TOX3]] | B | TOX3 activity raises RAB11FIP4's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without TOX3 | 0.090 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.435). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.0, 46.5); signed map (51.4, 3.1). **Vector** length 80.6, 15.1% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +20.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.6 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | +0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.4 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.2 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB11 family interacting protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,391,675-31,538,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAB11-FIP4, KIAA1821, MGC11316, FLJ00131 |
| Gene groups (HGNC) | EF-hand domain containing; RAB11 binding domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YS3](https://www.uniprot.org/uniprotkb/Q86YS3) (Rab11 family-interacting protein 4):

> Acts as a regulator of endocytic traffic by participating in membrane delivery. Required for the abscission step in cytokinesis, possibly by acting as an 'address tag' delivering recycling endosome membranes to the cleavage furrow during late cytokinesis. In case of infection by HCMV (human cytomegalovirus), may participate in egress of the virus out of nucleus; this function is independent of ARF6.

**Summary**, from NCBI Gene [84440](https://www.ncbi.nlm.nih.gov/gene/84440):

> The protein encoded by this gene interacts with RAB11 and is thought to be involved in bringing recycling endosome membranes to the cleavage furrow in late cytokinesis. Hypoxic conditions can lead to an upregulation of the encoded protein and enhance the metastatic potential of hepatocellular carcinoma. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:30267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30267) · Entrez [84440](https://www.ncbi.nlm.nih.gov/gene/84440) · UniProt [Q86YS3](https://www.uniprot.org/uniprotkb/Q86YS3) · Ensembl [ENSG00000131242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131242)

## Data

Gene col 5189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5189); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5189]; `tensor/DDL_lfc|DDL_z.npy` [5189]; `embed/gene_vectors.npy` [5189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5189 or target_col == 5189). Every well: [[RAB11FIP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11FIP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
