---
symbol: "DSP"
type: "gene"
col: 1769
ensembl_id: "ENSG00000096696"
name: "desmoplakin"
location: "6p24.3"
module: 54
arm: "-"
pooled_cpm: 349.5
n_lines_expressing: 33
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# DSP

*desmoplakin* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +10.8, q 2e-24, up in 25 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.29× (z +4.6, q 5e-04, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.490× (z -12.9, q 3e-35, down in 28 of 31 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.643× (z -5.7, q 1e-06, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROCK2]] (+0.58, fdr 1e-05), [[AHNAK]] (+0.57, fdr 3e-05), [[SPTBN1]] (+0.55, fdr 7e-05); moves opposite to [[POLR2F]] (-0.53, fdr 1e-05), [[TOMM5]] (-0.53, fdr 3e-05), [[SNU13]] (-0.52, fdr 8e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSG2]] → it (grade B ⚠); 6 go from it, the strongest it → [[ASB16-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +10.8 | 2e-24 | 25/29 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +10.5 | 3e-23 | 26/32 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +7.5 | 9e-12 | 21/29 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 5e-04 | 19/31 (KATO III, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.015 | 18/31 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.015 | 20/31 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.029 | 15/31 (HOP62, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.069 | 15/31 (KATO III, HOP62, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.12 | 14/31 (Panc 03.27, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.490×** | -12.9 | 3e-35 | 28/31 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.548×** | -10.9 | 5e-25 | 29/31 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.572×** | -10.1 | 1e-21 | 28/31 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -9.6 | 8e-20 | 29/31 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.715×** | -5.8 | 7e-07 | 26/31 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.643×** | -5.7 | 1e-06 | 26/31 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -5.6 | 2e-06 | 24/31 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.744×** | -5.3 | 7e-06 | 22/31 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.747×** | -5.3 | 1e-05 | 21/31 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.760×** | -4.9 | 4e-05 | 25/31 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.824×** | -4.9 | 5e-05 | 19/32 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.786×** | -4.3 | 7e-04 | 21/31 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -4.2 | 0.001 | 20/31 (HepG2/C3A, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.800×** | -4.0 | 0.002 | 18/31 (HEC-1-A, A498, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.656×** | -4.0 | 0.003 | 21/32 (A-172, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.804×** | -3.9 | 0.003 | 18/31 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.013 | 19/31 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.041 | 13/31 (A498, A-172, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.781×** | -3.2 | 0.041 | 20/31 (LoVo, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 722 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 0.05 µM 2.35× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 1,825 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.266× (z -12.9) |
| [[BT-474 (line)]] | alt | 541 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -14.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.430× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 601 | 2 (2 ⚠) | 6 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.228× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 273 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -11.4) |
| [[SW1417 (line)]] | alt | 629 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.96× (z +9.3) | — |
| [[A-172 (line)]] | wt | 342 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 565 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.314× (z -12.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.341× (z -10.8) |
| [[LoVo (line)]] | wt | 1,079 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 934 | 1 | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.24× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.418× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 645 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 275 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 292 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.89× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 212 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 642 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Phenylephrine (hydrochloride) (drug)]] 5 µM 1.83× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 445 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.441× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 479 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 931 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 682 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.08× (z +9.5) | — |
| [[A-427 (line)]] | wt | 267 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.90× (z +8.6) | — |
| [[A498 (line)]] | wt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 782 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.17× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.463× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 97.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.404× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 199 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 96.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0694× (z -10.8) |
| [[AN3 CA (line)]] | alt | 65.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 61.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 34.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 43.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 487 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 329 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 41.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 471 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 68.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 79.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 74.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 34.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 37.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.3 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 60.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROCK2]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[AHNAK]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[SPTBN1]] | +0.55 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[SPTAN1]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 | same gene group; pathway: Apoptosis |
| [[SBDS]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[YWHAZ]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 | pathway: Apoptosis |
| [[BMI1]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[NCOA4]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DNAJA2]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[WNK1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[DSG2]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 | pathway: Apoptosis; STRING 998 |
| [[SF3B1]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2F]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TOMM5]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SNU13]] | -0.52 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ASB16-AS1]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ANKRD13D]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[LSM7]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[STARD3]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[SNRPD2]] | -0.48 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[NDUFA3]] | -0.48 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[CDK5RAP1]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ATP5MG]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSG2]] | B | DSG2 activity raises DSP's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 4.47× lower at baseline in the lines without DSG2 | 0.068 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |
| [[TRIM29]] | C | TRIM29 activity raises DSP's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 6.08× lower at baseline in the lines without TRIM29 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASB16-AS1]] | B | DSP activity raises ASB16-AS1's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without DSP | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[STARD3]] | B | DSP activity raises STARD3's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without DSP | 0.040 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[MORF4L1P1]] | B | DSP activity raises MORF4L1P1's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.11× lower at baseline in the lines without DSP | 0.057 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| cells under [[Digitoxin (drug)]] 0.5 µM | B | DSP activity raises the cells' numbers under Digitoxin 0.5 µM (protects the cells) | lines that do not express DSP (17) vs lines expressing it (31) | the lines without DSP: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[B3GAT3]] | B | DSP activity raises B3GAT3's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.13× lower at baseline in the lines without DSP | 0.079 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[TRIM29]] | C | DSP activity raises TRIM29's level | lines that do not express DSP (17) vs lines expressing it (33) | 2.80× lower at baseline in the lines without DSP | 0.038 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.2, 2.7); signed map (11.8, -8.9). **Vector** length 125, 38.7% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.3 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | -3.3 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.9 | -3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.8 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | desmoplakin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,541,326-7,586,717 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KPPS2, PPKS2, DPI, DPII, DP |
| Gene groups (HGNC) | Plakins; Spectrin repeat containing; SH3 domain containing |
| Reactome | 14 pathways, smallest: Apoptotic cleavage of cell adhesion  proteins; Apoptotic cleavage of cellular proteins; Formation of the cornified envelope |
| Matched by | ensembl_id |

**Function**, from UniProt [P15924](https://www.uniprot.org/uniprotkb/P15924) (Desmoplakin):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Critical for cell-cell adhesion in early stage blastocysts and progression through proamniotic cavity formation (By similarity). Not required for preimplantation morphogenic process in blastocysts (By similarity). Required for keratin filament anchoring at the desmosome junction and subsequent organization of the keratin intermediate filament network within the cytoplasm (By …

**Summary**, from NCBI Gene [1832](https://www.ncbi.nlm.nih.gov/gene/1832):

> This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:3052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3052) · Entrez [1832](https://www.ncbi.nlm.nih.gov/gene/1832) · UniProt [P15924](https://www.uniprot.org/uniprotkb/P15924) · Ensembl [ENSG00000096696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096696)

## Data

Gene col 1769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1769); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1769]; `tensor/DDL_lfc|DDL_z.npy` [1769]; `embed/gene_vectors.npy` [1769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1769 or target_col == 1769). Every well: [[DSP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
