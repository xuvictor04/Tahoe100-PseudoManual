---
symbol: "WDR1"
type: "gene"
col: 977
ensembl_id: "ENSG00000071127"
name: "WD repeat domain 1"
location: "4p16.1"
module: 111
arm: "+"
pooled_cpm: 121.53
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# WDR1

*WD repeat domain 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +12.1, q 1e-30, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 3.11×, NCI-H1792 5.16×, A549 2.99×, SNU-423 4.27×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A498 3.02×, NCI-H1792 5.35×, SNU-423 3.98×, PANC-1 3.08×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A549 2.38×, A498 1.87×, RKO 2.01×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A498 2.04×, A549 2.14×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.680× (z -8.1, q 3e-13, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR3]] (+0.78, fdr 8e-06), [[ARPC4]] (+0.76, fdr 7e-06), [[MYH9]] (+0.75, fdr 7e-06); moves opposite to [[MALSU1]] (-0.71, fdr 1e-05), [[CAMLG]] (-0.70, fdr 7e-06), [[SMIM26]] (-0.67, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[TOMM7]] (-0.66, fdr 7e-06).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[F2RL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 977.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 3.11×, NCI-H1792 5.16×, A549 2.99×, SNU-423 4.27×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A498 3.02×, NCI-H1792 5.35×, SNU-423 3.98×, PANC-1 3.08×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A549 2.38×, A498 1.87×, RKO 2.01×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (A498 2.04×, A549 2.14×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +12.1 | 1e-30 | 45/49 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +10.8 | 1e-24 | 39/44 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +8.9 | 8e-17 | 35/45 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Folic acid (drug)]] 5 µM |  | 1.19× | +3.7 | 0.037 | 19/48 (COLO 205, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.27 | 20/48 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 977.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -8.1 | 3e-13 | 32/49 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -7.6 | 1e-11 | 42/48 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.629×** | -6.9 | 1e-09 | 40/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -6.6 | 8e-09 | 39/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -5.8 | 8e-07 | 31/47 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -4.6 | 4e-04 | 32/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.813×** | -4.3 | 0.001 | 29/48 (A549, J82, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.747×** | -4.2 | 0.002 | 36/49 (HepG2/C3A, SNU-423, …) | top dose only | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | 0.835× | -3.8 | 0.011 | 20/48 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.011 | 30/48 (NCI-H23, LS 180, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.780×** | -3.7 | 0.012 | 25/48 (J82, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.849× | -3.4 | 0.030 | 21/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.646×** | -3.4 | 0.031 | 27/45 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.805×** | -3.2 | 0.054 | 26/48 (SW480, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | **0.810×** | -3.1 | 0.067 | 21/48 (J82, LoVo, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.072 | 19/48 (KATO III, LS 180, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.089 | 21/48 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.819×** | -3.0 | 0.091 | 20/48 (HepG2/C3A, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 122 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.14× (z +8.8) | — |
| [[LoVo (line)]] | wt | 126 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -10.2) |
| [[A498 (line)]] | wt | 150 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.04× (z +9.5) | — |
| [[A-172 (line)]] | wt | 96.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 84.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +13.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +10.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +11.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 187 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.2) |
| [[PANC-1 (line)]] | alt | 103 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.398× (z -9.5) |
| [[SNU-423 (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 94.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 174 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.388× (z -8.5) |
| [[HS-578T (line)]] | alt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 88.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 200 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 80.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 51.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 93.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 138 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -9.2) |
| [[C-33 A (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 81.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -8.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -10.2) ⚠ toxic |
| [[RKO (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.3) |
| [[SW 1088 (line)]] | alt | 88.5 | 0 | 1 | — | [[Econazole (drug)]] 5 µM 0.0659× (z -9.1) |
| [[BT-474 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 143 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR3]] | +0.78 | +0.58 / +0.83 | both halves | 8e-06 | STRING 826 |
| [[ARPC4]] | +0.76 | +0.66 / +0.78 | both halves | 7e-06 | STRING 582 |
| [[MYH9]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | same gene group; STRING 770 |
| [[MAPRE1]] | +0.74 | +0.63 / +0.77 | both halves | 7e-06 | STRING 457 |
| [[ZYX]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 | same gene group |
| [[FLNA]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 874 |
| [[CDC42]] | +0.70 | +0.53 / +0.77 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 417 |
| [[DBNL]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 | same gene group; STRING 478 |
| [[TPM4]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 | STRING 548 |
| [[CSRP1]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION |
| [[UBA1]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[PIEZO1]] | +0.66 | +0.52 / +0.71 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*65 of its nearest partners move opposite, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALSU1]] | -0.71 | -0.54 / -0.78 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.70 | -0.59 / -0.75 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.52 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | -0.66 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[LAMTOR5]] | -0.66 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[FAM182B]] | -0.65 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.65 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[WDR83OS]] ⚠ | -0.65 | -0.53 / -0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.65 | -0.49 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS36]] ⚠ | -0.65 | -0.54 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD1]] | -0.64 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ELP2]] | -0.64 | -0.50 / -0.65 | both halves | 1e-05 | same gene group |
| [[ASB7]] | -0.64 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ATP5MC2]] | -0.63 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ATP5MJ]] | -0.63 | -0.52 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2RL1]] | B | F2RL1 activity raises WDR1's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.19× lower at baseline in the lines without F2RL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.806). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -19.8); signed map (-7.8, 34.5). **Vector** length 144, 48.1% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cell-extracellular matrix interactions* (reactome, mean cos +0.50 to 5); *RHO GTPase Effectors* (reactome, mean cos +0.61 to 10); *EPHB-mediated forward signaling* (reactome, mean cos +0.59 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.3 | +2.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Folic acid (drug)]] 5 µM |  | +3.1 | +3.7 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -5.0 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | -4.1 | -3.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.5 | -3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:10,068,089-10,116,972 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AIP1 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Hallmark sets | COAGULATION |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75083](https://www.uniprot.org/uniprotkb/O75083) (WD repeat-containing protein 1):

> Induces disassembly of actin filaments in conjunction with ADF/cofilin family proteins. Enhances cofilin-mediated actin severing (By similarity). Involved in cytokinesis. Involved in chemotactic cell migration by restricting lamellipodial membrane protrusions. Involved in myocardium sarcomere organization. Required for cardiomyocyte growth and maintenance (By similarity). Involved in megakaryocyte maturation and platelet shedding. Required for the establishment of planar cell polarity (PCP) …

**Summary**, from NCBI Gene [9948](https://www.ncbi.nlm.nih.gov/gene/9948):

> This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12754) · Entrez [9948](https://www.ncbi.nlm.nih.gov/gene/9948) · UniProt [O75083](https://www.uniprot.org/uniprotkb/O75083) · Ensembl [ENSG00000071127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071127)

## Data

Gene col 977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 977); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 977]; `tensor/DDL_lfc|DDL_z.npy` [977]; `embed/gene_vectors.npy` [977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 977 or target_col == 977). Every well: [[WDR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
