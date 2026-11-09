---
symbol: "CASP8AP2"
type: "gene"
col: 3987
ensembl_id: "ENSG00000118412"
name: "caspase 8 associated protein 2"
location: "6q15"
module: 6
arm: "+"
pooled_cpm: 55.53
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CASP8AP2

*caspase 8 associated protein 2* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.27× (z +15.8, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +15.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.761× (z -5.3, q 7e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCM]] (+0.71, fdr 7e-06), [[USP1]] (+0.67, fdr 1e-05), [[FEN1]] (+0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.27×** | +15.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.25×** | +15.6 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +15.2 | 0e+00 | 45/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.12×** | +14.4 | 4e-45 | 47/48 (SW480, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.07×** | +13.5 | 1e-39 | 41/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.86×** | +11.5 | 2e-28 | 40/49 (SW480, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +6.5 | 8e-09 | 30/48 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.41×** | +6.3 | 2e-08 | 30/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +6.0 | 1e-07 | 31/48 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.7 | 9e-07 | 26/48 (J82, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +5.3 | 5e-06 | 29/48 (J82, C-33 A, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 24/48 (HT-29, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 3e-05 | 24/48 (RKO, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **1.25×** | +4.2 | 9e-04 | 22/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.22×** | +3.9 | 0.004 | 23/48 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.011 | 17/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.13× | +3.4 | 0.020 | 7/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.067 | 9/48 (SNU-423, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -5.3 | 7e-05 | 27/48 (HT-29, A-427, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.799×** | -4.3 | 0.004 | 23/48 (Panc 03.27, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.808×** | -4.0 | 0.014 | 21/43 (LoVo, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.792×** | -3.7 | 0.025 | 19/45 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.707×** | -3.5 | 0.054 | 18/48 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.739× | -3.0 | 0.22 | 14/37 (HS-578T, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.8 | 7 (6 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.518× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 100 | 6 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 60.5 | 7 (6 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +14.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 57.5 | 4 (3 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.1) | [[Lonafarnib (drug)]] 5 µM 0.106× (z -12.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 69.6 | 6 (5 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +13.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 51.1 | 5 (5 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 73.1 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +12.5) | — |
| [[A549 (line)]] | wt | 35.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.6) | — |
| [[LoVo (line)]] | wt | 48.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 43.2 | 4 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +11.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 49.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.9) | — |
| [[A-172 (line)]] | wt | 77.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.44× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 50.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Lonafarnib (drug)]] 5 µM 0.0900× (z -12.4) ⚠ toxic |
| [[RKO (line)]] | wt | 55.5 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +9.0) | — |
| [[A-427 (line)]] | wt | 92.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | [[Selinexor (drug)]] 5 µM 0.584× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 48.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +8.7) ⚠ cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.22× (z +10.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C-33 A (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +8.9) | — |
| [[C32 (line)]] | wt | 41.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Lonafarnib (drug)]] 5 µM 0.136× (z -8.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 59.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +9.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 76.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0968× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 22.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 38.6 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.112× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 53.3 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +11.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 37.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 45.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCM]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[USP1]] | +0.67 | +0.52 / +0.77 | both halves | 1e-05 | STRING 442 |
| [[FEN1]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.64 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[NPAT]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 | STRING 892 |
| [[LIN9]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RMI1]] | +0.63 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SLF1]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[CHAF1A]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ORC6]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[ZNF367]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASP8AP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises CASP8AP2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without E2F2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CASP8AP2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without CDC25A | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises CASP8AP2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without DSCC1 | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises CASP8AP2's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CENPP | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens CASP8AP2's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 1.13× as strongly (z diff -0.81); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.33x vs 1.04x (z diff -3.2) | 0.852 over the table, 0.066 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.2, -48.0); signed map (-41.9, -46.3). **Vector** length 106, 29.6% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *CDC6 association with the ORC:origin complex* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.3 | +13.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.7 | +11.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.1 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.2 | +6.5 |
|  | [[Thymol (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.2 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.2 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | caspase 8 associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,829,894-89,874,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLASH, CED-4, RIP25, FLJ11208, KIAA1315 |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 3 pathways, smallest: SUMOylation of transcription cofactors; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKL3](https://www.uniprot.org/uniprotkb/Q9UKL3) (CASP8-associated protein 2):

> Participates in TNF-induced blockade of glucocorticoid receptor (GR) transactivation at the nuclear receptor coactivator level, upstream and independently of NF-kappa-B. Suppresses both NCOA2- and NCOA3-induced enhancement of GR transactivation. Involved in TNF-induced activation of NF-kappa-B via a TRAF2-dependent pathway (By similarity). Acts as a downstream mediator for CASP8-induced activation of NF-kappa-B. Required for the activation of CASP8 in FAS-mediated apoptosis. Involved for …

**Summary**, from NCBI Gene [9994](https://www.ncbi.nlm.nih.gov/gene/9994):

> This protein is highly similar to FLASH, a mouse apoptotic protein identified by its interaction with the death-effector domain (DED) of caspase 8. Studies of FLASH protein suggested that this protein may be a component of the death-inducing signaling complex that includes Fas receptor, Fas-binding adapter FADD, and caspase 8, and plays a regulatory role in Fas-mediated apoptosis. Alternative splicing results in multiple transcript variants encoding the same protein.[provided by RefSeq, Nov …

**Accessions** — [HGNC:1510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1510) · Entrez [9994](https://www.ncbi.nlm.nih.gov/gene/9994) · UniProt [Q9UKL3](https://www.uniprot.org/uniprotkb/Q9UKL3) · Ensembl [ENSG00000118412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118412)

## Data

Gene col 3987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3987); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3987]; `tensor/DDL_lfc|DDL_z.npy` [3987]; `embed/gene_vectors.npy` [3987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3987 or target_col == 3987). Every well: [[CASP8AP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP8AP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
