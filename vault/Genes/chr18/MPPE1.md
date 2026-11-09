---
symbol: "MPPE1"
type: "gene"
col: 7850
ensembl_id: "ENSG00000154889"
name: "metallophosphoesterase 1"
location: "18p11.21"
module: 39
arm: "+"
pooled_cpm: 9.44
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MPPE1

*metallophosphoesterase 1* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.15× (z +8.8, q 4e-16, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.578× (z -10.1, q 4e-21, down in 31 of 45 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.474× (z -9.7, q 8e-20, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PXMP4]] (+0.61, fdr 1e-05), [[CROT]] (+0.59, fdr 1e-05), [[SLC9A6]] (+0.58, fdr 2e-05); moves opposite to [[TRIM59]] (-0.61, fdr 2e-05), [[CPNE9]] (-0.60, fdr 1e-05), [[TRIM72]] (-0.60, fdr 2e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +8.8 | 4e-16 | 31/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +8.8 | 4e-16 | 31/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +7.3 | 7e-11 | 26/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +6.6 | 5e-09 | 26/46 (LoVo, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.7 | 2e-06 | 18/47 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +5.2 | 2e-05 | 21/45 (A498, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.46×** | +4.8 | 2e-04 | 19/37 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.40×** | +4.4 | 7e-04 | 15/47 (SW480, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 9e-04 | 9/45 (SW480, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 9/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 12/48 (A498, SW480, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +3.8 | 0.006 | 13/46 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.7 | 0.008 | 9/26 (AsPC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.011 | 15/45 (A498, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.011 | 12/47 (AsPC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.015 | 11/48 (AsPC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.023 | 7/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.028 | 5/47 (NCI-H2030, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.578×** | -10.1 | 4e-21 | 31/45 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.474×** | -9.7 | 8e-20 | 34/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.576×** | -6.9 | 1e-09 | 21/45 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -6.4 | 2e-08 | 22/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.632×** | -6.0 | 3e-07 | 23/45 (SW480, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.650×** | -5.6 | 2e-06 | 19/43 (A-172, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -5.1 | 3e-05 | 21/39 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -4.8 | 8e-05 | 21/46 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.657×** | -4.8 | 8e-05 | 17/47 (SW480, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -4.7 | 1e-04 | 17/46 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -3.6 | 0.014 | 13/42 (Panc 03.27, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.732×** | -3.6 | 0.016 | 17/46 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.3 | 0.043 | 7/47 (HOP62, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.632×** | -3.1 | 0.074 | 8/44 (hTERT-HPNE, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -8.7) |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 9.66 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.201× (z -9.7) |
| [[C32 (line)]] | wt | 9.32 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LoVo (line)]] | wt | 14.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -9.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.110× (z -11.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0634× (z -13.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A498 (line)]] | wt | 8.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HepG2_C3A (line)]] | wt | 9.59 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0806× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 9.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RKO (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0747× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0934× (z -8.5) |
| [[A549 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*28 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXMP4]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CROT]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[NDUFAF5]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[C5orf22]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[NDUFS2]] | +0.54 | +0.46 / +0.40 | both halves | 4e-05 |  |
| [[SNX4]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[FBXO3]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[STX18]] | +0.52 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[PPP4R1]] | +0.51 | +0.49 / +0.32 | both halves | 2e-04 |  |
| [[REPS1]] | +0.51 | +0.40 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*72 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM59]] | -0.61 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CPNE9]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[TRIM72]] | -0.60 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[LINC01619]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[TXK]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[USP50]] | -0.59 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SELPLG]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[FGF18]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[LINC01934]] | -0.58 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[DPYS]] | -0.57 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[MIR9-1HG]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SLC22A1]] | -0.56 | -0.37 / -0.59 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MPPE1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction -0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.3, -12.2); signed map (-29.3, -15.2). **Vector** length 63.3, 9.97% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +3.4 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.3 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -4.3 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.6 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.4 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | metallophosphoesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:11,882,622-11,908,366 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGAP5, Cdc1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53F39](https://www.uniprot.org/uniprotkb/Q53F39) (Metallophosphoesterase 1):

> Metallophosphoesterase that catalyzes the removal of a side-chain ethanolamine-phosphate (EtNP) from the second mannose of the GPI-anchor protein intermediate. Participates in the glycan remodeling steps of GPI-anchor maturation to allow an efficient transport of GPI-anchor proteins from the endoplasmic reticulum to the Golgi.

**Summary**, from NCBI Gene [65258](https://www.ncbi.nlm.nih.gov/gene/65258):

> Predicted to enable GPI-mannose ethanolamine phosphate phosphodiesterase activity and manganese ion binding activity. Involved in GPI anchor biosynthetic process. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15988) · Entrez [65258](https://www.ncbi.nlm.nih.gov/gene/65258) · UniProt [Q53F39](https://www.uniprot.org/uniprotkb/Q53F39) · Ensembl [ENSG00000154889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154889)

## Data

Gene col 7850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7850); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7850]; `tensor/DDL_lfc|DDL_z.npy` [7850]; `embed/gene_vectors.npy` [7850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7850 or target_col == 7850). Every well: [[MPPE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPPE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
