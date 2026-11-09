---
symbol: "TMEM30A"
type: "gene"
col: 3396
ensembl_id: "ENSG00000112697"
name: "cell division cycle 50 P4-ATPase accessory subunit A"
location: "6q14.1"
module: 29
arm: "+"
pooled_cpm: 108.06
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TMEM30A

*cell division cycle 50 P4-ATPase accessory subunit A* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +14.3, q 8e-44, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.85× (z +9.7, q 6e-20, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.738× (z -4.8, q 9e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED7]] (+0.76, fdr 7e-06), [[DDOST]] (+0.74, fdr 7e-06), [[BPNT2]] (+0.74, fdr 7e-06); moves opposite to [[ZNF593]] (-0.76, fdr 7e-06), [[NT5C]] (-0.73, fdr 7e-06), [[ATF4]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRFN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3396.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +14.3 | 8e-44 | 46/49 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +13.9 | 2e-41 | 43/44 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +11.1 | 2e-26 | 43/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +9.7 | 6e-20 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +7.1 | 1e-10 | 45/49 (C32, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.49×** | +6.3 | 3e-08 | 38/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +6.0 | 1e-07 | 35/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 2e-07 | 39/48 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.7 | 8e-07 | 35/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +5.3 | 8e-06 | 28/48 (LS 180, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +5.1 | 2e-05 | 32/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.007 | 27/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.7 | 0.011 | 28/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.24×** | +3.2 | 0.053 | 23/47 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.053 | 20/38 (HOP62, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.088 | 22/47 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.088 | 22/48 (A-172, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3396.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.738×** | -4.8 | 9e-04 | 27/48 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -4.3 | 0.006 | 27/48 (A-172, C32, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.762×** | -4.1 | 0.007 | 29/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.010 | 36/48 (hTERT-HPNE, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.011 | 28/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.7 | 0.018 | 25/48 (NCI-H2030, H4, …) | all doses, flat | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.798×** | -3.6 | 0.025 | 26/48 (BT-474, SW 1088, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.728×** | -3.6 | 0.025 | 30/47 (HCT15, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.738×** | -3.4 | 0.038 | 26/49 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **0.820×** | -3.1 | 0.085 | 27/48 (SNU-423, HepG2/C3A, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.821×** | -3.1 | 0.085 | 21/48 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.821×** | -3.1 | 0.085 | 23/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3396. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 54.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +11.4) | — |
| [[A-172 (line)]] | wt | 105 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +14.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.452× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 107 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 115 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[SW480 (line)]] | alt | 73.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +10.2) | — |
| [[C32 (line)]] | wt | 110 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +13.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 92.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 92.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +14.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 119 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +16.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +12.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 86.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 62.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 63.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 70.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 201 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 94.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.59× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 67.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 76.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 98.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 112 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 144 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 174 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 232 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -9.0) |
| [[RKO (line)]] | wt | 98.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.52× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3396), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED7]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 | STRING 450 |
| [[DDOST]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[RPN1]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[TMX1]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[AGPAT1]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TGOLN2]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[FAM91A1]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.76 | -0.62 / -0.80 | both halves | 7e-06 |  |
| [[NT5C]] | -0.73 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[ATF4]] | -0.68 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[SURF6]] | -0.67 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.66 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[NIFK]] | -0.66 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[ESF1]] | -0.66 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.65 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[AK6]] | -0.65 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[FBXL6]] | -0.65 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.65 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.63 | -0.56 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN4]] | B | LRFN4 activity raises TMEM30A's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without LRFN4 | 0.067 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.6, -21.8); signed map (-24.1, -39.0). **Vector** length 146, 49.3% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.4 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +14.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.9 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +3.1 | +2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +3.0 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -1.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 50 P4-ATPase accessory subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:75,252,924-75,284,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10856; previously C6orf67, TMEM30A |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV96](https://www.uniprot.org/uniprotkb/Q9NV96) (Cell cycle control protein 50A):

> Accessory component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids from the outer to the inner leaflet of various membranes and ensures the maintenance of asymmetric distribution of phospholipids. Phospholipid translocation also seems to be implicated in vesicle formation and in uptake of lipid signaling molecules. The beta subunit may assist in binding of the phospholipid substrate. Required for the proper folding, assembly …

**Summary**, from NCBI Gene [55754](https://www.ncbi.nlm.nih.gov/gene/55754):

> Enables aminophospholipid flippase activity and structural molecule activity. Involved in several processes, including phospholipid transport; positive regulation of transport; and xenobiotic transmembrane transport. Located in endoplasmic reticulum; endosome membrane; and plasma membrane. Part of phospholipid-translocating ATPase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16667) · Entrez [55754](https://www.ncbi.nlm.nih.gov/gene/55754) · UniProt [Q9NV96](https://www.uniprot.org/uniprotkb/Q9NV96) · Ensembl [ENSG00000112697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112697)

## Data

Gene col 3396: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3396); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3396, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3396]; `tensor/DDL_lfc|DDL_z.npy` [3396]; `embed/gene_vectors.npy` [3396]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3396 or target_col == 3396). Every well: [[TMEM30A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM30A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
