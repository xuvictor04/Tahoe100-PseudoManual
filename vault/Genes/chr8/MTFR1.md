---
symbol: "MTFR1"
type: "gene"
col: 841
ensembl_id: "ENSG00000066855"
name: "mitochondrial fission regulator 1"
location: "8q13.1"
module: 16
arm: "-"
pooled_cpm: 69.28
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MTFR1

*mitochondrial fission regulator 1* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.56× (z +11.4, q 3e-27, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.680× (z -9.6, q 6e-19, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.298×, A498 0.475×, HS-578T 0.401×, PANC-1 0.593×, …; ⚠ cell-cycle shift, explains ~59% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (HS-578T 0.209×, A498 0.402×, A-427 0.362×, LOX-IMVI 0.426×; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.539×, HS-578T 0.446×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HS-578T 0.479×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCUN1D2]] (+0.70, fdr 7e-06), [[FAM20B]] (+0.65, fdr 7e-06), [[MTHFD2]] (+0.64, fdr 7e-06); moves opposite to [[METTL18]] (-0.64, fdr 9e-06), [[FAM200A]] (-0.63, fdr 8e-06), [[ZFHX2]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIP6]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Lactate (calcium) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +11.4 | 3e-27 | 42/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +10.7 | 4e-24 | 28/40 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +10.4 | 7e-23 | 38/48 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +9.5 | 2e-19 | 38/48 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +9.5 | 3e-19 | 30/48 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +9.3 | 9e-19 | 32/48 (AsPC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.9 | 4e-17 | 30/49 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +8.5 | 1e-15 | 29/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +8.2 | 2e-14 | 25/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +8.1 | 4e-14 | 31/43 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.7 | 8e-13 | 33/48 (MIA PaCa-2, C32, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +6.9 | 2e-10 | 30/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.5 | 3e-09 | 26/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +5.6 | 1e-06 | 23/49 (SW480, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +5.5 | 1e-06 | 25/49 (HOP62, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +5.2 | 7e-06 | 19/48 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +4.8 | 5e-05 | 16/49 (HOP62, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +4.7 | 8e-05 | 19/48 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.39×** | +4.4 | 3e-04 | 20/48 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.007 | 16/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 841.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.298×, A498 0.475×, HS-578T 0.401×, PANC-1 0.593×, …; ⚠ cell-cycle shift, explains ~59% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (HS-578T 0.209×, A498 0.402×, A-427 0.362×, LOX-IMVI 0.426×; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.539×, HS-578T 0.446×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (HS-578T 0.479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.680×** | -9.6 | 6e-19 | 29/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.820×** | -6.3 | 7e-08 | 27/48 (A-427, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -6.3 | 7e-08 | 28/48 (HS-578T, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.790×** | -6.1 | 1e-07 | 26/48 (HS-578T, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.852× | -4.2 | 0.004 | 20/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Allantoin (drug)]] 5 µM |  | 0.895× | -3.7 | 0.025 | 6/48 (Hs 766T, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.906× | -3.4 | 0.063 | 10/48 (H4, J82, …) | top dose only | low cells (technical?) |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.877× | -3.2 | 0.11 | 8/48 (SNU-423, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 38.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 126 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -18.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.446× (z -9.3) |
| [[A498 (line)]] | wt | 163 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -15.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.539× (z -9.5) |
| [[A-427 (line)]] | wt | 72.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[C32 (line)]] | wt | 42.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 62.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.13× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.01× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 73.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 97.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[CFPAC-1 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -8.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[J82 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -9.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[MIA PaCa-2 (line)]] | alt | 49.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 99.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[RPMI-7951 (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.103× (z -10.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 107 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SSR3]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SETD3]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[HYOU1]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SEC63]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[NOMO2]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TMED3]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MFN1]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TXNDC12]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | -0.64 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[FAM200A]] | -0.63 | -0.64 / -0.57 | both halves | 8e-06 |  |
| [[ZFHX2]] | -0.62 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[TBCC]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[KAT5]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SDSL]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.61 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[EPC1]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TIGD6]] | -0.60 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZNF429]] | -0.59 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[EID2]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity strengthens MTFR1's drug response | lines that do not express TRIP6 (12) vs lines expressing it (37) | the lines without TRIP6 respond 0.72× as strongly (z diff +0.90); strongest at Panobinostat 0.5 µM: 1.18x vs 1.52x (z diff +1.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | C | MTFR1's natural level raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | MTFR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.281 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Menadione (drug)]] 0.5 µM | C | MTFR1's natural level lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | MTFR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.421 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | MTFR1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | MTFR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.6, 12.9); signed map (-55.9, 3.8). **Vector** length 113, 29.1% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -10.5 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.3 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -5.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial fission regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:65,644,734-65,771,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHPPR, KIAA0009, FAM54A2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15390](https://www.uniprot.org/uniprotkb/Q15390) (Mitochondrial fission regulator 1):

> May play a role in mitochondrial aerobic respiration. May also regulate mitochondrial organization and fission (By similarity).

**Summary**, from NCBI Gene [9650](https://www.ncbi.nlm.nih.gov/gene/9650):

> This gene encodes a mitochondrial protein that is characterized by a poly-proline rich region. A chicken homolog of this protein promotes mitochondrial fission and the mouse homolog protects cells from oxidative stress. A related pseudogene of this gene is found on chromosome X. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:29510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29510) · Entrez [9650](https://www.ncbi.nlm.nih.gov/gene/9650) · UniProt [Q15390](https://www.uniprot.org/uniprotkb/Q15390) · Ensembl [ENSG00000066855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066855)

## Data

Gene col 841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 841); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 841]; `tensor/DDL_lfc|DDL_z.npy` [841]; `embed/gene_vectors.npy` [841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 841 or target_col == 841). Every well: [[MTFR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTFR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
