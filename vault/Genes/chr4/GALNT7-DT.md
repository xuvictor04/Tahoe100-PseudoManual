---
symbol: "GALNT7-DT"
type: "gene"
col: 14423
ensembl_id: "ENSG00000245213"
name: "GALNT7 divergent transcript"
location: "4q34.1"
module: 23
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GALNT7-DT

*GALNT7 divergent transcript* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.93× (z +20.5, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.325× (z -11.9, q 8e-30, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (58 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 42 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAI4]] (+0.79, fdr 3e-05), [[TMEM202-AS1]] (+0.79, fdr 2e-04), [[OXA1L-DT]] (+0.78, fdr 1e-04); moves opposite to [[STUB1]] (-0.71, fdr 0.001, ⚠ not reproduced), [[YIF1B]] (-0.70, fdr 0.003, ⚠ one half only (not replicated)), [[PCMT1]] (-0.69, fdr 0.001, ⚠ one half only (not replicated)), [[AP2S1]] (-0.68, fdr 5e-04), [[KCTD17]] (-0.67, fdr 5e-05), [[NDUFA12]] (-0.67, fdr 5e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[IGF2BP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.93×** | +20.5 | 0e+00 | 39/40 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +10.7 | 2e-24 | 22/39 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +8.1 | 1e-13 | 21/37 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.1 | 1e-10 | 17/46 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 1e-05 | 3/9 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +5.3 | 1e-05 | 24/44 (PANC-1, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +4.8 | 1e-04 | 16/40 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.2 | 0.002 | 9/26 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.004 | 12/45 (SW480, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.008 | 7/45 (SW480, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.41×** | +3.6 | 0.014 | 13/45 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.014 | 6/46 (SW480, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.015 | 7/45 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.017 | 3/45 (A498, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.017 | 10/44 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.033 | 8/45 (SW480, A498, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.034 | 3/46 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.047 | 11/37 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.325×** | -11.9 | 8e-30 | 32/45 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.329×** | -11.7 | 2e-29 | 39/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.402×** | -9.6 | 1e-19 | 27/44 (SW480, PANC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.433×** | -8.8 | 1e-16 | 33/45 (SW480, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -6.9 | 5e-10 | 26/45 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.569×** | -6.0 | 2e-07 | 20/45 (SNU-1, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -5.5 | 2e-06 | 19/42 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.626×** | -5.0 | 5e-05 | 16/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.450×** | -4.4 | 6e-04 | 14/38 (Panc 03.27, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.700×** | -3.8 | 0.009 | 17/45 (SW480, SNU-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.718×** | -3.3 | 0.047 | 16/41 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.731×** | -3.2 | 0.063 | 12/30 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.564×** | -3.2 | 0.063 | 12/32 (KATO III, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.742×** | -3.2 | 0.063 | 15/44 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.4 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.0754× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0776× (z -16.9) |
| [[LoVo (line)]] | wt | 7.07 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +13.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0469× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.148× (z -9.0) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -13.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.6) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.114× (z -12.8) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.178× (z -10.1) |
| [[HOP62 (line)]] | alt | 5.24 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +10.4) | [[Decitabine (drug)]] 0.05 µM 0.0555× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 4.38 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.153× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0755× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[SNU-423 (line)]] | alt | 9.60 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -9.6) |
| [[C-33 A (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.145× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 6.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.46× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.158× (z -8.5) ⚠ cell-cycle shift, explains ~77% of this change |
| [[SNU-1 (line)]] | wt | 7.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0365× (z -10.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 36 of them with an alert (⚠; 36 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | +0.79 | +0.80 / +0.44 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.79 | +0.76 / +0.31 | both halves | 2e-04 |  |
| [[OXA1L-DT]] | +0.78 | +0.75 / +0.34 | both halves | 1e-04 | same gene group |
| [[MAILR]] | +0.76 | +0.75 / +0.23 | both halves | 5e-04 |  |
| [[PPP1R12A-AS2]] | +0.76 | +0.74 / +0.26 | both halves | 4e-04 |  |
| [[PPP1R3F]] | +0.74 | +0.69 / +0.34 | both halves | 1e-04 |  |
| [[AHI1-DT]] | +0.74 | +0.66 / +0.33 | both halves | 1e-04 | same gene group |
| [[IQCH-AS1]] | +0.74 | +0.75 / +0.31 | both halves | 2e-04 |  |
| [[SEPTIN7-DT]] | +0.73 | +0.70 / +0.27 | both halves | 3e-04 | same gene group |
| [[CCDC90B-AS1]] | +0.73 | +0.73 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[MYLK-AS1]] | +0.73 | +0.78 / +0.26 | both halves | 4e-04 |  |
| [[PCNX4-DT]] | +0.73 | +0.74 / +0.13 | ⚠ one half (not replicated) | 0.002 | same gene group |
| [[PKN2-AS1]] | +0.73 | +0.70 / +0.23 | both halves | 6e-04 |  |
| [[CASS4]] | +0.73 | +0.70 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.71 | -0.42 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[YIF1B]] | -0.70 | -0.59 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[PCMT1]] | -0.69 | -0.61 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[AP2S1]] | -0.68 | -0.63 / -0.24 | both halves | 5e-04 |  |
| [[SLC27A1]] | -0.67 | -0.59 / -0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[GNAI2]] | -0.67 | -0.56 / -0.07 | ⚠ one half (not replicated) | 0.004 |  |
| [[KCTD17]] | -0.67 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[NDUFA12]] | -0.67 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[MAST3]] | -0.66 | -0.45 / -0.23 | both halves | 5e-04 |  |
| [[CTNNBL1]] | -0.66 | -0.69 / -0.23 | both halves | 5e-04 |  |
| [[WRAP73]] | -0.66 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SPTLC2]] | -0.66 | -0.64 / -0.22 | both halves | 6e-04 |  |
| [[LRFN3]] | -0.65 | -0.56 / -0.24 | both halves | 4e-04 |  |
| [[FLNB]] | -0.65 | -0.63 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGF2BP1]] | B | IGF2BP1 activity raises GALNT7-DT's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 1.47× lower at baseline in the lines without IGF2BP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[TOP2A]] | B | TOP2A activity lowers GALNT7-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[JHY]] | B | JHY activity raises GALNT7-DT's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without JHY | 0.030 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises GALNT7-DT's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without SOCS2-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[GALNT7]] | C | GALNT7 activity raises GALNT7-DT's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 3.02× lower at baseline in the lines without GALNT7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; co-absent with the target |
| [[ZNF827]] | C | ZNF827 activity raises GALNT7-DT's level | lines that do not express ZNF827 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without ZNF827 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ITGA2-AS1, RND3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.4, 15.2); signed map (25.4, -11.5). **Vector** length 85.1, 16.6% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +20.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.2 | +4.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -11.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.3 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.2 | -11.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | GALNT7 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q34.1 — chr4:173,094,868-173,169,652 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55604) · Entrez [101930370](https://www.ncbi.nlm.nih.gov/gene/101930370) · Ensembl [ENSG00000245213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245213)

## Data

Gene col 14423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14423); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14423]; `tensor/DDL_lfc|DDL_z.npy` [14423]; `embed/gene_vectors.npy` [14423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14423 or target_col == 14423). Every well: [[GALNT7-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT7-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
