---
symbol: "SPRY3"
type: "gene"
col: 9728
ensembl_id: "ENSG00000168939"
name: "sprouty RTK signaling antagonist 3"
location: "Xq28 and Yq12"
module: 137
arm: "+"
pooled_cpm: 16.36
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 24
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# SPRY3

*sprouty RTK signaling antagonist 3* — Xq28 and Yq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +10.7, q 8e-24, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.249× (z -15.6, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB2]] (+0.80, fdr 1e-05), [[PBLD]] (+0.77, fdr 2e-05), [[MMADHC-DT]] (+0.74, fdr 2e-04); moves opposite to [[FCHO1]] (-0.71, fdr 1e-05), [[CDON]] (-0.70, fdr 3e-05), [[ARRB2]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +10.7 | 8e-24 | 29/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.7 | 6e-20 | 41/47 (HEC-1-A, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.39×** | +5.2 | 5e-05 | 22/47 (SW480, A498, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.7 | 4e-04 | 21/45 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.011 | 20/46 (NCI-H2030, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.041 | 17/46 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.045 | 9/46 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +3.4 | 0.045 | 17/45 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.087 | 14/46 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.087 | 12/47 (RKO, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.092 | 9/47 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.092 | 13/46 (SW480, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.249×** | -15.6 | 0e+00 | 41/46 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.257×** | -15.2 | 0e+00 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.267×** | -14.8 | 0e+00 | 39/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.350×** | -11.8 | 5e-30 | 40/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.392×** | -10.5 | 7e-24 | 33/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.507×** | -7.6 | 2e-12 | 30/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.304×** | -7.0 | 2e-10 | 34/47 (PANC-1, SNU-423, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.544×** | -6.9 | 5e-10 | 28/46 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.316×** | -6.8 | 8e-10 | 36/47 (SNU-423, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.556×** | -6.6 | 2e-09 | 28/45 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.673×** | -6.3 | 1e-08 | 31/47 (C-33 A, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.350×** | -6.2 | 3e-08 | 25/45 (SW 900, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.576×** | -6.0 | 1e-07 | 24/46 (PANC-1, SW 900, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.622×** | -5.1 | 1e-05 | 23/40 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.683×** | -4.3 | 6e-04 | 22/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.716×** | -3.8 | 0.005 | 21/45 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.017 | 17/47 (RKO, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -3.3 | 0.026 | 14/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.7 | 0 | 17 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0784× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0921× (z -18.5) |
| [[A-427 (line)]] | wt | 22.7 | 0 | 8 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0886× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.133× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 19.1 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.7) | [[Digitoxin (drug)]] 0.5 µM 0.140× (z -15.1) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.309× (z -9.0) |
| [[SW480 (line)]] | alt | 13.9 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.106× (z -15.3) |
| [[HT-29 (line)]] | alt | 27.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -12.6) |
| [[J82 (line)]] | alt | 40.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.244× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0713× (z -16.2) |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0427× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 22.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.263× (z -9.8) |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -9.2) |
| [[KATO III (line)]] | alt | 8.94 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.127× (z -9.2) |
| [[LoVo (line)]] | wt | 12.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.143× (z -10.9) |
| [[RKO (line)]] | wt | 16.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -13.4) |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0501× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0677× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 10.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +8.6) | [[Bendamustine (drug)]] 5 µM 0.153× (z -8.6) |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0343× (z -12.4) |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0658× (z -13.3) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.163× (z -9.4) |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0961× (z -8.7) |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.132× (z -9.3) |
| [[HS-578T (line)]] | alt | 5.51 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0589× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.110× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0364× (z -8.9) |
| [[A498 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | +0.80 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[PBLD]] | +0.77 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | +0.74 | +0.65 / +0.29 | both halves | 2e-04 |  |
| [[AVEN]] | +0.74 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RNPC3-DT]] | +0.73 | +0.72 / +0.24 | both halves | 5e-04 |  |
| [[CRPPA]] | +0.72 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[LINC01829]] | +0.72 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[PPP3CB-AS1]] | +0.71 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[PCBP1-AS1]] | +0.71 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[SLC25A21]] | +0.71 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[LINC01004]] | +0.70 | +0.62 / +0.28 | both halves | 3e-04 |  |
| [[ATXN1L]] | +0.70 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.71 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CDON]] | -0.70 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[ARRB2]] | -0.69 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.68 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[SLC27A1]] | -0.67 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[MAST1]] | -0.66 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.66 | -0.53 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[TPD52]] | -0.66 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.66 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RADX]] | -0.65 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CDK18]] | -0.65 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[SH3PXD2B]] | -0.65 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[MAST3]] | -0.65 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPRY3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HECW2]] | B | HECW2 activity raises SPRY3's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 1.25× lower at baseline in the lines without HECW2 | 0.078 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.811). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (7.0, 10.7); signed map (24.3, -25.6). **Vector** length 96.3, 23.3% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.5 | +9.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.5 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.9 | -10.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.9 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -15.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -14.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.5 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | sprouty RTK signaling antagonist 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 and Yq12 — chrX:155,612,572-155,782,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPRY3 |
| Gene groups (HGNC) | Pseudoautosomal region 2; Sprouty RTK signaling antagonist family |
| Matched by | ensembl_id |

**Function**, from UniProt [O43610](https://www.uniprot.org/uniprotkb/O43610) (Protein sprouty homolog 3):

> Inhibits neurite branching, arbor length and neurite complexity (By similarity). Inhibits EGF-mediated p42/44 ERK signaling (By similarity). Negatively regulates the MAPK cascade, resulting in a reduction of extracellular matrix protein accumulation. May function as an antagonist of fibroblast growth factor (FGF) pathways and may negatively modulate respiratory organogenesis.

**Summary**, from NCBI Gene [10251](https://www.ncbi.nlm.nih.gov/gene/10251):

> Predicted to enable protein kinase inhibitor activity. Involved in negative regulation of MAPK cascade. Predicted to be located in cytoplasm and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11271) · Entrez [10251](https://www.ncbi.nlm.nih.gov/gene/10251) · UniProt [O43610](https://www.uniprot.org/uniprotkb/O43610) · Ensembl [ENSG00000168939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168939)

## Data

Gene col 9728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9728); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9728]; `tensor/DDL_lfc|DDL_z.npy` [9728]; `embed/gene_vectors.npy` [9728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9728 or target_col == 9728). Every well: [[SPRY3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRY3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
