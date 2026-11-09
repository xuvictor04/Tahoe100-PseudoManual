---
symbol: "FIP1L1"
type: "gene"
col: 6964
ensembl_id: "ENSG00000145216"
name: "factor interacting with PAPOLA and CPSF1"
location: "4q12"
module: 65
arm: "+"
pooled_cpm: 107.95
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# FIP1L1

*factor interacting with PAPOLA and CPSF1* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.44× (z +7.7, q 7e-12, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.664× (z -8.6, q 3e-15, down in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.755× (z -8.4, q 1e-14, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTX2]] (+0.74, fdr 7e-06), [[PRMT9]] (+0.67, fdr 7e-06), [[PRPF39]] (+0.67, fdr 7e-06); moves opposite to [[RAB7A]] (-0.60, fdr 1e-05), [[THUMPD3-AS1]] (-0.55, fdr 1e-05), [[CYTH2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.7 | 7e-12 | 34/48 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.6 | 7e-12 | 37/47 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +6.1 | 2e-07 | 31/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.7 | 1e-06 | 31/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.3 | 1e-05 | 30/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +4.8 | 2e-04 | 26/47 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 3e-04 | 24/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.4 | 9e-04 | 24/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 1e-03 | 25/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 21/48 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.004 | 23/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.9 | 0.006 | 21/48 (SW1417, SW 1088, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.012 | 17/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.023 | 16/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | 1.16× | +3.0 | 0.10 | 11/48 (SNU-423, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6964.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.664×** | -8.6 | 3e-15 | 36/49 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -8.4 | 1e-14 | 32/49 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -8.2 | 6e-14 | 33/44 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **0.806×** | -4.2 | 0.004 | 24/45 (NCI-H2347, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.821×** | -4.2 | 0.004 | 23/48 (C32, A549, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.824×** | -4.1 | 0.004 | 23/49 (NCI-H2030, SW48, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.826×** | -4.0 | 0.004 | 23/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.834× | -3.8 | 0.009 | 20/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.842× | -3.6 | 0.017 | 18/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.845× | -3.6 | 0.019 | 21/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.845× | -3.6 | 0.019 | 18/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.056 | 18/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.859× | -3.2 | 0.058 | 12/48 (HOP62, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 225 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.5) |
| [[LoVo (line)]] | wt | 94.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +10.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.535× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 181 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.2) |
| [[PANC-1 (line)]] | alt | 68.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.0) | — |
| [[A-427 (line)]] | wt | 93.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.5) ⚠ cell-cycle shift, explains ~19% of this change | [[Dinaciclib (drug)]] 5 µM 0.258× (z -16.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 120 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.70× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -15.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 86.9 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.20× (z +10.3) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -9.7) |
| [[A498 (line)]] | wt | 157 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.7) |
| [[HCT15 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.407× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -21.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 122 | 0 | 2 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0761× (z -10.9) |
| [[SW 900 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 82.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.1) |
| [[C-33 A (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -13.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 92.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.73× (z +10.2) ⚠ toxic | — |
| [[H4 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -13.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -18.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 97.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[KATO III (line)]] | alt | 87.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Lonafarnib (drug)]] 5 µM 3.60× (z +9.3) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 148 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.00× (z +10.6) | — |
| [[RKO (line)]] | wt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.8) |
| [[SNU-1 (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A549 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX2]] | +0.74 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PRPF39]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TADA1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[UBA5]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[REV1]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NDUFV2]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[RYK]] | +0.61 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SNX4]] | +0.59 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[LRIG2]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB7A]] | -0.60 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | -0.55 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[CYTH2]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TMBIM6]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ATP6V1D]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[CSNK1A1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NOP14-AS1]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.51 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SECISBP2]] | -0.50 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[TUBA1C]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[OTUD5]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.7, -9.7); signed map (-29.3, -13.2). **Vector** length 97.8, 27.7% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +7.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +2.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.4 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | factor interacting with PAPOLA and CPSF1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:53,377,569-53,464,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586K0717, FIP1, hFip1 |
| Gene groups (HGNC) | Cleavage and polyadenylation specific factor subunits |
| Reactome | 16 pathways, smallest: Signaling by cytosolic PDGFRA and PDGFRB fusion proteins; Signaling by PDGFR in disease; Processing of Intronless Pre-mRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UN15](https://www.uniprot.org/uniprotkb/Q6UN15) (Pre-mRNA 3'-end-processing factor FIP1):

> Component of the cleavage and polyadenylation specificity factor (CPSF) complex that plays a key role in pre-mRNA 3'-end formation, recognizing the AAUAAA signal sequence and interacting with poly(A) polymerase and other factors to bring about cleavage and poly(A) addition. FIP1L1 contributes to poly(A) site recognition and stimulates poly(A) addition. Binds to U-rich RNA sequence elements surrounding the poly(A) site. May act to tether poly(A) polymerase to the CPSF complex.

**Summary**, from NCBI Gene [81608](https://www.ncbi.nlm.nih.gov/gene/81608):

> This gene encodes a subunit of the CPSF (cleavage and polyadenylation specificity factor) complex that polyadenylates the 3' end of mRNA precursors. This gene, the homolog of yeast Fip1 (factor interacting with PAP), binds to U-rich sequences of pre-mRNA and stimulates poly(A) polymerase activity. Its N-terminus contains a PAP-binding site and its C-terminus an RNA-binding domain. An interstitial chromosomal deletion on 4q12 creates an in-frame fusion of human genes FIP1L1 and PDGFRA …

**Accessions** — [HGNC:19124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19124) · Entrez [81608](https://www.ncbi.nlm.nih.gov/gene/81608) · UniProt [Q6UN15](https://www.uniprot.org/uniprotkb/Q6UN15) · Ensembl [ENSG00000145216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145216)

## Data

Gene col 6964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6964); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6964]; `tensor/DDL_lfc|DDL_z.npy` [6964]; `embed/gene_vectors.npy` [6964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6964 or target_col == 6964). Every well: [[FIP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
