---
symbol: "TTC13"
type: "gene"
col: 6786
ensembl_id: "ENSG00000143643"
name: "tetratricopeptide repeat domain 13"
location: "1q42.2"
module: 18
arm: "+"
pooled_cpm: 15.8
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TTC13

*tetratricopeptide repeat domain 13* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.13× (z +11.7, q 1e-28, up in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.04× (z +11.0, q 1e-25, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.517× (z -14.4, q 2e-44, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.453× (z -12.2, q 7e-32, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS1]] (+0.71, fdr 7e-06), [[XPO5]] (+0.66, fdr 7e-06), [[HEATR3]] (+0.64, fdr 7e-06); moves opposite to [[SLC31A2]] (-0.60, fdr 2e-05), [[FMO4]] (-0.59, fdr 6e-05), [[RBMXL1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF506]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.13×** | +11.7 | 1e-28 | 40/47 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +11.0 | 1e-25 | 39/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +9.5 | 2e-19 | 34/47 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.86×** | +9.5 | 2e-19 | 35/47 (SW 900, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.75×** | +8.3 | 1e-14 | 30/46 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.75×** | +8.1 | 4e-14 | 34/48 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +6.9 | 6e-10 | 30/45 (LS 180, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +6.8 | 8e-10 | 23/46 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.56×** | +6.6 | 2e-09 | 17/26 (HOP62, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 3e-06 | 23/46 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +4.4 | 4e-04 | 17/47 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +4.4 | 6e-04 | 11/47 (HEC-1-A, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.32×** | +4.3 | 7e-04 | 11/47 (LS 180, CFPAC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 15/48 (A498, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.006 | 16/48 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.058 | 8/48 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.078 | 8/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.517×** | -14.4 | 2e-44 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.453×** | -12.2 | 7e-32 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -9.8 | 2e-20 | 32/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.594×** | -8.1 | 1e-13 | 30/47 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -7.9 | 4e-13 | 30/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.618×** | -7.2 | 7e-11 | 26/47 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.676×** | -6.1 | 1e-07 | 26/46 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.760×** | -4.2 | 0.001 | 14/47 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -4.2 | 0.001 | 23/47 (C32, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.2 | 0.002 | 19/48 (PANC-1, RKO, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.778×** | -3.9 | 0.005 | 20/46 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -3.8 | 0.008 | 15/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.015 | 9/47 (A-172, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.786×** | -3.5 | 0.018 | 13/46 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.025 | 15/47 (J82, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.806×** | -3.4 | 0.028 | 9/48 (SK-MEL-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.686×** | -3.0 | 0.072 | 18/44 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.762×** | -3.0 | 0.079 | 16/44 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -9.7) |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -17.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -12.6) |
| [[A498 (line)]] | wt | 13.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 20.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 11.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0906× (z -12.2) |
| [[J82 (line)]] | alt | 18.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -8.7) |
| [[LoVo (line)]] | wt | 13.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -13.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.5) |
| [[A-172 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -8.5) |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.105× (z -12.8) |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.09 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 1 | — | [[4EGI-1 (drug)]] 5 µM 0.0454× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -13.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -10.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0594× (z -12.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS1]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[XPO5]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ABCB10]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PCCB]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[R3HDM1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NUP93]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[FAM120A]] | +0.59 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[WRNIP1]] | +0.59 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[GMPS]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TMTC4]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 | same gene group |
| [[BLTP2]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC31A2]] | -0.60 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[FMO4]] | -0.59 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[RBMXL1]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ZNF506]] | -0.57 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ELF1]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[NECAP2]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ARMCX1]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[STAT6]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | -0.55 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[AP5Z1]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CDK3]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RFTN2]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF506]] | B | ZNF506 activity lowers TTC13's level | lines that do not express ZNF506 (18) vs lines expressing it (32) | 1.28× higher at baseline in the lines without ZNF506 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000267581, ZNF486, ENSG00000291130 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.5, -38.7); signed map (-5.3, -52.9). **Vector** length 79.6, 16.0% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.6 | +8.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.3 | +6.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +8.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.7 | -14.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.7 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.2 | -7.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.0 | -4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:230,906,243-230,978,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22584 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8NBP0](https://www.uniprot.org/uniprotkb/Q8NBP0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26204) · Entrez [79573](https://www.ncbi.nlm.nih.gov/gene/79573) · UniProt [Q8NBP0](https://www.uniprot.org/uniprotkb/Q8NBP0) · Ensembl [ENSG00000143643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143643)

## Data

Gene col 6786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6786); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6786]; `tensor/DDL_lfc|DDL_z.npy` [6786]; `embed/gene_vectors.npy` [6786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6786 or target_col == 6786). Every well: [[TTC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
