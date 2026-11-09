---
symbol: "TGFBRAP1"
type: "gene"
col: 5791
ensembl_id: "ENSG00000135966"
name: "transforming growth factor beta receptor associated protein 1"
location: "2q12.1-q12.2"
module: 1
arm: "+"
pooled_cpm: 24.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TGFBRAP1

*transforming growth factor beta receptor associated protein 1* — 2q12.1-q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.11× (z +10.9, q 9e-25, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.443× (z -15.0, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTPAP]] (+0.70, fdr 7e-06), [[ZZZ3]] (+0.70, fdr 7e-06), [[ZNF507]] (+0.68, fdr 1e-05); moves opposite to [[PNPLA8]] (-0.67, fdr 7e-06), [[SPAG9]] (-0.65, fdr 1e-05), [[CDKL5]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +10.9 | 9e-25 | 40/48 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +8.8 | 4e-16 | 34/47 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +8.0 | 3e-13 | 32/48 (A-427, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.0 | 3e-07 | 27/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 3e-06 | 24/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 3e-05 | 17/47 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.8 | 1e-04 | 11/26 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 2e-04 | 23/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.6 | 2e-04 | 19/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 16/47 (A-427, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 13/47 (NCI-H2347, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.6 | 0.016 | 12/47 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +3.4 | 0.032 | 19/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.20×** | +3.3 | 0.035 | 13/48 (SNU-1, A549, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.047 | 12/45 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.066 | 11/48 (HOP62, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.443×** | -15.0 | 0e+00 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -14.9 | 0e+00 | 40/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -14.5 | 3e-45 | 38/47 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.539×** | -11.4 | 1e-27 | 36/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.666×** | -7.5 | 8e-12 | 22/43 (A-427, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -6.8 | 1e-09 | 24/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.722×** | -6.0 | 2e-07 | 25/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.767×** | -4.7 | 2e-04 | 17/35 (NCI-H2030, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.753×** | -4.6 | 2e-04 | 16/39 (SNU-423, HEC-1-A, …) | all doses, flat | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -4.3 | 8e-04 | 18/46 (MIA PaCa-2, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.0 | 0.003 | 19/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.003 | 18/47 (COLO 205, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.799×** | -4.0 | 0.003 | 18/47 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.744×** | -3.9 | 0.004 | 12/48 (Panc 03.27, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.014 | 21/47 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.791×** | -3.1 | 0.060 | 13/45 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **0.830×** | -3.1 | 0.064 | 13/47 (NCI-H661, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.3 | 6 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 53.4 | 1 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.48× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 27.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.2) |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.8) |
| [[A549 (line)]] | wt | 25.7 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0457× (z -28.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.2) |
| [[A-427 (line)]] | wt | 23.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -8.8) |
| [[C32 (line)]] | wt | 22.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.7) |
| [[LS 180 (line)]] | wt | 31.9 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 8.13× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -11.7) |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -13.1) |
| [[A-172 (line)]] | wt | 24.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.5× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.212× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -9.4) |
| [[A498 (line)]] | wt | 16.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.98× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 1 | — | [[Ralimetinib dimesylate (drug)]] 0.5 µM 0.0492× (z -9.3) |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0851× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0509× (z -12.9) |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -9.0) |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.9) |
| [[KATO III (line)]] | alt | 13.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -9.9) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -12.4) |
| [[RKO (line)]] | wt | 35.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0483× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -12.9) |
| [[SNU-1 (line)]] | wt | 34.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.9) |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0846× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ZZZ3]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.68 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[METAP1D]] | +0.68 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ACBD6]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[BYSL]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LTV1]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PATZ1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A13]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MRRF]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA8]] | -0.67 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[SPAG9]] | -0.65 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[CDKL5]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[MXD1]] | -0.60 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[NDRG1]] | -0.59 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[NBEAL1]] | -0.58 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[KCNQ1OT1]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ARFGAP3]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PTPRH]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SWI5]] | -0.55 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SELENOK]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TGFBRAP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CNTNAP3B]] | B | CNTNAP3B activity raises TGFBRAP1's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 1.06× lower at baseline in the lines without CNTNAP3B | 0.097 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C |
| [[LRRC8D]] | C | LRRC8D activity raises TGFBRAP1's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.4, 3.2); signed map (5.0, -40.2). **Vector** length 95.5, 21.2% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.1 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.0 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.8 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +0.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -15.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -14.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -6.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta receptor associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1-q12.2 — chr2:105,264,391-105,329,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAP-1, TRAP1, VPS3 |
| Gene groups (HGNC) | CORVET complex |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUH2](https://www.uniprot.org/uniprotkb/Q8WUH2) (Transforming growth factor-beta receptor-associated protein 1):

> Plays a role in the TGF-beta/activin signaling pathway. It associates with inactive heteromeric TGF-beta and activin receptor complexes, mainly through the type II receptor, and is released upon activation of signaling. May recruit SMAD4 to the vicinity of the receptor complex and facilitate its interaction with receptor-regulated Smads, such as SMAD2.; Plays a role in vesicle-mediated protein trafficking of the endocytic membrane transport pathway. Believed to act as a component of the …

**Summary**, from NCBI Gene [9392](https://www.ncbi.nlm.nih.gov/gene/9392):

> This gene encodes a protein that binds to transforming growth factor-beta (TGF-beta) receptors and plays a role in TGF-beta signaling. The encoded protein acts as a chaprone in signaling downstream of TGF-beta. It is involved in signal-dependent association with SMAD4. The protein is also a component of mammalian CORVET, a multisubunit tethering protein complex that is involved in fusion of early endosomes. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:16836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16836) · Entrez [9392](https://www.ncbi.nlm.nih.gov/gene/9392) · UniProt [Q8WUH2](https://www.uniprot.org/uniprotkb/Q8WUH2) · Ensembl [ENSG00000135966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135966)

## Data

Gene col 5791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5791); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5791]; `tensor/DDL_lfc|DDL_z.npy` [5791]; `embed/gene_vectors.npy` [5791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5791 or target_col == 5791). Every well: [[TGFBRAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFBRAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
