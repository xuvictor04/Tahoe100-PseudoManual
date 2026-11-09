---
symbol: "SLAIN2"
type: "gene"
col: 3034
ensembl_id: "ENSG00000109171"
name: "SLAIN family member 2"
location: "4p11"
module: 25
arm: "+"
pooled_cpm: 87.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SLAIN2

*SLAIN family member 2* — 4p11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.73× (z +9.0, q 1e-16, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.651× (z -7.7, q 1e-11, down in 26 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.176×, NCI-H1573 0.356×, RKO 0.328×, SNU-1 0.273×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.149×, SNU-1 0.150×, SHP-77 0.171×, AsPC-1 0.270×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (Panc 03.27 0.313×, CHP-212 0.123×, C-33 A 0.322×, SW1417 0.381×; ⚠ toxic; transcription drop); [[Radotinib (drug)]] 0.5 µM in 1 line (Hs 766T 0.421×); [[Drospirenone (drug)]] 0.5 µM in 1 line (NCI-H661 0.145×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB23]] (+0.56, fdr 2e-05), [[UBP1]] (+0.51, fdr 4e-05), [[ACTR1A]] (+0.50, fdr 3e-05); moves opposite to [[MIR30DHG]] (-0.41, fdr 1e-04), [[TNFRSF1B]] (-0.39, fdr 1e-04), [[TMEM144]] (-0.38, fdr 6e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +9.0 | 1e-16 | 43/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.4 | 6e-08 | 32/48 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +6.2 | 1e-07 | 36/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +6.1 | 2e-07 | 24/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.9 | 8e-05 | 29/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 5e-04 | 27/48 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +4.5 | 5e-04 | 23/48 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.001 | 23/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.20× | +3.5 | 0.028 | 19/48 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.028 | 21/48 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.097 | 14/49 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.10 | 16/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3034.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.176×, NCI-H1573 0.356×, RKO 0.328×, SNU-1 0.273×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.149×, SNU-1 0.150×, SHP-77 0.171×, AsPC-1 0.270×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (Panc 03.27 0.313×, CHP-212 0.123×, C-33 A 0.322×, SW1417 0.381×; ⚠ toxic; transcription drop); [[Radotinib (drug)]] 0.5 µM in 1 line (Hs 766T 0.421×); [[Drospirenone (drug)]] 0.5 µM in 1 line (NCI-H661 0.145×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.651×** | -7.7 | 1e-11 | 26/45 (Panc 03.27, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.680×** | -7.5 | 2e-11 | 34/49 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -6.9 | 8e-10 | 31/44 (SK-MEL-2, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.817×** | -3.9 | 0.012 | 25/48 (HOP62, A498, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.871× | -3.8 | 0.017 | 9/48 (Hs 766T, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.832×** | -3.6 | 0.034 | 21/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.846× | -3.2 | 0.095 | 20/48 (SHP-77, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 90.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -23.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 99.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.5) | — |
| [[LS 180 (line)]] | wt | 93.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 99.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -16.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.8) | — |
| [[A549 (line)]] | wt | 66.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -10.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 78.7 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 91.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 91.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 75.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 80.4 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.421× (z -9.4) |
| [[HT-29 (line)]] | alt | 96.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.82× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.515× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 85.6 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.145× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -11.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.9) | — |
| [[RKO (line)]] | wt | 97.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -15.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -20.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 75.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.53× (z +10.0) | — |
| [[A-172 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB23]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[UBP1]] | +0.51 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ACTR1A]] | +0.50 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[SPAST]] | +0.49 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PPM1A]] | +0.49 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SACM1L]] | +0.49 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MTMR6]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[TMEM9B]] | +0.48 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[DR1]] | +0.46 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[SEC22C]] | +0.46 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[MAF1]] | +0.45 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[NRBP1]] | +0.45 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR30DHG]] | -0.41 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[TNFRSF1B]] | -0.39 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[TMEM144]] | -0.38 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[CASP8]] | -0.37 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MIR23AHG]] | -0.37 | -0.21 / -0.36 | both halves | 6e-04 |  |
| [[PFKFB3]] | -0.37 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[XACT]] | -0.37 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[CEP72]] | -0.36 | -0.22 / -0.27 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.289). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.0, -15.2); signed map (-41.0, -16.5). **Vector** length 69.2, 14.4% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.5 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | -7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | -6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.3 | +0.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | +4.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SLAIN family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p11 — chr4:48,341,529-48,426,201 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21611; previously KIAA1458 |
| Gene groups (HGNC) | SLAIN family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P270](https://www.uniprot.org/uniprotkb/Q9P270) (SLAIN motif-containing protein 2):

> Binds to the plus end of microtubules and regulates microtubule dynamics and microtubule organization. Promotes cytoplasmic microtubule nucleation and elongation. Required for normal structure of the microtubule cytoskeleton during interphase.

**Summary**, from NCBI Gene [57606](https://www.ncbi.nlm.nih.gov/gene/57606):

> Involved in cytoplasmic microtubule organization; microtubule nucleation; and positive regulation of microtubule polymerization. Located in ciliary tip; cytosol; and microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29282) · Entrez [57606](https://www.ncbi.nlm.nih.gov/gene/57606) · UniProt [Q9P270](https://www.uniprot.org/uniprotkb/Q9P270) · Ensembl [ENSG00000109171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109171)

## Data

Gene col 3034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3034); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3034]; `tensor/DDL_lfc|DDL_z.npy` [3034]; `embed/gene_vectors.npy` [3034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3034 or target_col == 3034). Every well: [[SLAIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLAIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
