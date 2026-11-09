---
symbol: "TM2D1"
type: "gene"
col: 8540
ensembl_id: "ENSG00000162604"
name: "TM2 domain containing 1"
location: "1p31.3"
module: 89
arm: "+"
pooled_cpm: 81.83
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TM2D1

*TM2 domain containing 1* — 1p31.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 1.93×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.702× (z -15.6, q 0e+00, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC32]] (+0.65, fdr 7e-06), [[TAF11]] (+0.64, fdr 7e-06), [[ZBTB8OS]] (+0.62, fdr 2e-05); moves opposite to [[BAHCC1]] (-0.59, fdr 8e-06), [[PSMG1]] (-0.55, fdr 1e-05), [[NAB1]] (-0.54, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8540.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 1.93×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.13× | +5.4 | 3e-05 | 11/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.20× | +5.3 | 3e-05 | 24/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.6 | 7e-04 | 15/48 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.13× | +3.9 | 0.013 | 7/48 (C-33 A, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.9 | 0.013 | 16/48 (NCI-H1573, KATO III, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +3.6 | 0.029 | 4/48 (SW1417, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.11× | +3.4 | 0.063 | 17/48 (NCI-H23, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.702×** | -15.6 | 0e+00 | 34/48 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -14.6 | 1e-45 | 41/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.701×** | -11.0 | 5e-26 | 39/48 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.721×** | -10.2 | 4e-22 | 35/48 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -10.0 | 3e-21 | 34/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -9.5 | 2e-19 | 27/49 (A549, SNU-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.753×** | -8.8 | 8e-17 | 31/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.754×** | -8.8 | 1e-16 | 31/49 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.757×** | -8.7 | 3e-16 | 32/48 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.772×** | -8.0 | 5e-14 | 29/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.765×** | -8.0 | 6e-14 | 27/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.761×** | -7.8 | 2e-13 | 28/45 (SW480, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.781×** | -7.4 | 7e-12 | 25/44 (NCI-H1573, SHP-77, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.824×** | -6.0 | 7e-08 | 23/48 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.715×** | -5.5 | 2e-06 | 23/49 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.844× | -5.1 | 1e-05 | 19/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.006 | 20/48 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 0.890× | -3.5 | 0.016 | 8/47 (A-427, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.898× | -3.3 | 0.023 | 11/48 (A-172, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -12.2) |
| [[HOP62 (line)]] | alt | 75.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 96.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.581× (z -10.6) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.648× (z -8.5) |
| [[A549 (line)]] | wt | 54.5 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.5) |
| [[H4 (line)]] | wt | 121 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.354× (z -10.0) |
| [[A-427 (line)]] | wt | 76.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.467× (z -10.0) |
| [[J82 (line)]] | alt | 74.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -15.2) |
| [[LoVo (line)]] | wt | 77.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -11.9) |
| [[LS 180 (line)]] | wt | 85.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.429× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 82.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -16.0) |
| [[A-172 (line)]] | wt | 65.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -15.0) |
| [[A498 (line)]] | wt | 67.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 68.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -13.5) |
| [[HS-578T (line)]] | alt | 73.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.442× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 96.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.473× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 94.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0782× (z -33.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 91.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.392× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 68.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 89.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -17.7) |
| [[SNU-1 (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.0) |
| [[SNU-423 (line)]] | alt | 68.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -10.1) |
| [[SW480 (line)]] | alt | 90.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[AsPC-1 (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C-33 A (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.380× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[COLO 205 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 80.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.470× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 89.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 81.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.527× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H596 (line)]] | alt | 83.8 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.112× (z -10.6) |
| [[RKO (line)]] | wt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.4) |
| [[SHP-77 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.146× (z -8.5) |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC32]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TAF11]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ZBTB8OS]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RNPC3]] | +0.62 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NDUFA4]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[INTS9]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[UXT]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A17]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[EMC3]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[MED31]] | +0.59 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NDUFA13]] ⚠ | +0.59 | +0.46 / +0.59 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SEM1]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAHCC1]] | -0.59 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[PSMG1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NAB1]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.54 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ZNF664]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[HGH1]] | -0.54 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[AKAP11]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZNF816]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SEPTIN11]] | -0.52 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ZBTB14]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CSRP1]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, 23.7); signed map (-0.8, -2.3). **Vector** length 105, 25.9% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.9 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.5 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.5 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.3 | -11.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | -6.3 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | -4.9 | -7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.3 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TM2 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:61,681,046-61,725,423 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BBP |
| Gene groups (HGNC) | TM2 domain containing family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX74](https://www.uniprot.org/uniprotkb/Q9BX74) (TM2 domain-containing protein 1):

> May participate in amyloid-beta-induced apoptosis via its interaction with beta-APP42.

**Summary**, from NCBI Gene [83941](https://www.ncbi.nlm.nih.gov/gene/83941):

> The protein encoded by this gene is a beta-amyloid peptide-binding protein. It contains a structural module related to that of the seven transmembrane domain G protein-coupled receptor superfamily and known to be important in heterotrimeric G protein activation. Beta-amyloid peptide has been established to be a causative factor in neuron death and the consequent diminution of cognitive abilities observed in Alzheimer's disease. This protein may be a target of neurotoxic beta-amyloid peptide, …

**Accessions** — [HGNC:24142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24142) · Entrez [83941](https://www.ncbi.nlm.nih.gov/gene/83941) · UniProt [Q9BX74](https://www.uniprot.org/uniprotkb/Q9BX74) · Ensembl [ENSG00000162604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162604)

## Data

Gene col 8540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8540); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8540]; `tensor/DDL_lfc|DDL_z.npy` [8540]; `embed/gene_vectors.npy` [8540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8540 or target_col == 8540). Every well: [[TM2D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM2D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
