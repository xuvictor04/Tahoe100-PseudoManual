---
symbol: "RHBDD1"
type: "gene"
col: 6884
ensembl_id: "ENSG00000144468"
name: "rhomboid domain containing 1"
location: "2q36.3"
module: 18
arm: "+"
pooled_cpm: 101.35
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RHBDD1

*rhomboid domain containing 1* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.36× (z +5.1, q 2e-04, up in 30 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.32× (z +4.5, q 0.002, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.508× (z -10.3, q 4e-22, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.829× (z -4.4, q 7e-04, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD1L]] (+0.66, fdr 7e-06), [[PRMT3]] (+0.61, fdr 1e-05), [[HLCS]] (+0.59, fdr 1e-05); moves opposite to [[BPNT1]] (-0.46, fdr 4e-05), [[ATL1]] (-0.46, fdr 7e-05), [[ZNF44]] (-0.46, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BMF]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.1 | 2e-04 | 30/47 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +4.5 | 0.002 | 28/47 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +4.1 | 0.007 | 19/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +4.0 | 0.009 | 20/47 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.046 | 24/47 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.068 | 23/46 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +3.3 | 0.069 | 23/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.22×** | +3.2 | 0.084 | 20/47 (A-172, A498, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.084 | 23/47 (NCI-H2030, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.508×** | -10.3 | 4e-22 | 33/44 (A549, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.667×** | -9.5 | 1e-18 | 36/47 (SW1417, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -8.7 | 4e-16 | 34/43 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.581×** | -8.6 | 1e-15 | 39/47 (SW1417, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.5 | 5e-12 | 32/48 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -6.2 | 4e-08 | 32/46 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.735×** | -5.1 | 3e-05 | 29/47 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.829×** | -4.4 | 7e-04 | 19/47 (J82, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.624×** | -4.1 | 0.003 | 27/48 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.637×** | -3.9 | 0.006 | 25/46 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.013 | 23/49 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -3.6 | 0.014 | 21/47 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.818×** | -3.3 | 0.037 | 22/47 (SW1417, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.770×** | -3.3 | 0.040 | 25/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 127 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.473× (z -9.4) |
| [[HT-29 (line)]] | alt | 118 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[PANC-1 (line)]] | alt | 217 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -15.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 129 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -18.4) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A-427 (line)]] | wt | 174 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 148 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -26.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 77.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -17.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.169× (z -8.6) |
| [[LoVo (line)]] | wt | 171 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.453× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -14.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 79.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -16.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 123 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.344× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 97.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -14.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 95.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.5) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SHP-77 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A-172 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -14.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 92.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[C-33 A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0632× (z -12.2) ⚠ toxic |
| [[J82 (line)]] | alt | 33.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.482× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 89.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[LS 180 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +8.8) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.4) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SNU-1 (line)]] | wt | 237 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Larotrectinib sulfate (drug)]] 0.5 µM 0.0876× (z -8.6) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 125 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -8.6) |
| [[SW480 (line)]] | alt | 84.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 98.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD1L]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[HLCS]] | +0.59 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[MOCOS]] | +0.57 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MARS1]] | +0.57 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[EIF4G3]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[YARS1]] | +0.56 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[IARS1]] | +0.54 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[SLC7A1]] | +0.54 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[CAMKMT]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[FAM135A]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ATR]] | +0.53 | +0.55 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT1]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ATL1]] | -0.46 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[ZNF44]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZNF821]] | -0.45 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[GALT]] | -0.45 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MEX3B]] | -0.45 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[LINC00674]] | -0.43 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CCNG2]] | -0.43 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[SECISBP2L]] | -0.43 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[NOTCH2NLA]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[BMF]] | -0.42 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMF]] | C | BMF activity lowers RHBDD1's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.00× higher at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[MTHFD1L]] | C | MTHFD1L activity raises RHBDD1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.65× lower at baseline in the lines without MTHFD1L | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent |
| [[ZNF44]] | C | ZNF44's natural level weakens RHBDD1's drug response | ZNF44's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.06; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-3.8, -33.1); signed map (2.6, -51.8). **Vector** length 105, 29.8% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +5.7 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.2 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -4.3 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.7 | -8.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.9 | -3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:226,835,581-226,999,215 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547E052, RHBDL4 |
| Gene groups (HGNC) | Rhomboid family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEB9](https://www.uniprot.org/uniprotkb/Q8TEB9) (Rhomboid-related protein 4):

> Intramembrane-cleaving serine protease that cleaves single transmembrane or multi-pass membrane proteins in the hydrophobic plane of the membrane, luminal loops and juxtamembrane regions. Involved in regulated intramembrane proteolysis and the subsequent release of functional polypeptides from their membrane anchors. Functional component of endoplasmic reticulum-associated degradation (ERAD) for misfolded membrane proteins. Required for the degradation process of some specific misfolded …

**Summary**, from NCBI Gene [84236](https://www.ncbi.nlm.nih.gov/gene/84236):

> Enables serine-type endopeptidase activity. Involved in several processes, including cellular response to unfolded protein; membrane protein proteolysis; and positive regulation of protein catabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23081) · Entrez [84236](https://www.ncbi.nlm.nih.gov/gene/84236) · UniProt [Q8TEB9](https://www.uniprot.org/uniprotkb/Q8TEB9) · Ensembl [ENSG00000144468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144468)

## Data

Gene col 6884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6884); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6884]; `tensor/DDL_lfc|DDL_z.npy` [6884]; `embed/gene_vectors.npy` [6884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6884 or target_col == 6884). Every well: [[RHBDD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
