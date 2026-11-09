---
symbol: "MRPL30"
type: "gene"
col: 11673
ensembl_id: "ENSG00000185414"
name: "mitochondrial ribosomal protein L30"
location: "2q11.2"
module: 148
arm: "+"
pooled_cpm: 24.92
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# MRPL30

*mitochondrial ribosomal protein L30* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +25.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.811× (z -4.4, q 0.006, down in 18 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.0985×); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.444×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (SW 900 0.0692×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX18]] (+0.68, fdr 7e-06), [[INTS2]] (+0.66, fdr 3e-05), [[C17orf75]] (+0.65, fdr 1e-04); moves opposite to [[FRMD8]] (-0.58, fdr 1e-05), [[GATAD2B]] (-0.57, fdr 6e-05), [[SNN]] (-0.56, fdr 3e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +25.5 | 0e+00 | 47/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.52×** | +19.4 | 0e+00 | 39/43 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +19.1 | 0e+00 | 40/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.13×** | +14.7 | 0e+00 | 31/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.75×** | +11.8 | 6e-30 | 39/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.81×** | +11.5 | 1e-28 | 31/39 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.70×** | +11.2 | 4e-27 | 41/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +10.7 | 7e-25 | 30/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.6 | 4e-20 | 29/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.64×** | +9.6 | 4e-20 | 31/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.4 | 4e-19 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +9.3 | 5e-19 | 34/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.49×** | +8.4 | 2e-15 | 33/48 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +7.7 | 4e-13 | 21/48 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +7.5 | 3e-12 | 30/47 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.2 | 2e-11 | 24/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +7.1 | 6e-11 | 25/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.003 | 13/48 (HEC-1-A, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.003 | 3/48 (Panc 03.27, HOP62, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.004 | 11/47 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.006 | 11/48 (HOP62, HEC-1-A, …) | two highest doses |  |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.011 | 8/47 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11673.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.0985×); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.444×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 0.484×; ⚠ cell-cycle shift, explains ~0% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (SW 900 0.0692×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.811×** | -4.4 | 0.006 | 18/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.805×** | -4.2 | 0.006 | 18/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.834× | -3.8 | 0.020 | 17/47 (SNU-423, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.8 | 0.020 | 12/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.2 | 0.13 | 13/47 (SW480, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 8 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +21.4) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +16.6) | — |
| [[SNU-423 (line)]] | alt | 19.7 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +12.1) | — |
| [[SW480 (line)]] | alt | 39.2 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.67× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Digitoxin (drug)]] 5 µM 0.444× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.1 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.0) | — |
| [[LoVo (line)]] | wt | 22.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 34.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.5) | — |
| [[A-172 (line)]] | wt | 21.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +16.8) | — |
| [[HOP62 (line)]] | alt | 22.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 18.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.9) | — |
| [[J82 (line)]] | alt | 24.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 25.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +16.8) | — |
| [[SW 900 (line)]] | alt | 19.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.9) | [[Sonidegib (drug)]] 5 µM 0.0692× (z -8.6) |
| [[A549 (line)]] | wt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +10.3) | — |
| [[C32 (line)]] | wt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0985× (z -12.9) |
| [[HT-29 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.9) | — |
| [[KATO III (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.1) | — |
| [[NCI-H23 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +16.3) | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 33.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.0) | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX18]] | +0.68 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[INTS2]] | +0.66 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[C17orf75]] | +0.65 | +0.73 / +0.33 | both halves | 1e-04 |  |
| [[C8orf33]] | +0.62 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[RIMOC1]] | +0.61 | +0.72 / +0.37 | both halves | 7e-05 |  |
| [[RWDD2B]] | +0.61 | +0.74 / +0.34 | both halves | 1e-04 |  |
| [[GUF1]] | +0.61 | +0.73 / +0.46 | both halves | 2e-05 |  |
| [[ATP5PB]] | +0.61 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[SLC30A9]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CFAP97]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[POLDIP2]] | +0.60 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[PHYH]] | +0.60 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMD8]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[GATAD2B]] | -0.57 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[SNN]] | -0.56 | -0.59 / -0.29 | both halves | 3e-04 |  |
| [[COX6A1]] | -0.56 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[C4orf48]] | -0.55 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[ELOB]] | -0.54 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[KANK2]] | -0.53 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[CENPW]] | -0.53 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TRIR]] ⚠ | -0.53 | -0.42 / -0.53 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CABLES2]] | -0.53 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[RPL36AL]] ⚠ | -0.52 | -0.43 / -0.48 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC34]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PEDS1]] | -0.51 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[CYTH3]] | -0.51 | -0.63 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPL30's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NNT]] | B | NNT activity lowers MRPL30's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without NNT | 0.081 | ⚠ within organs, on part of the lines; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-18.8, 7.7); signed map (10.0, -29.2). **Vector** length 64.2, 11.2% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.0 | +19.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +25.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.4 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +7.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +0.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,181,152-99,199,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L28, RPML28, uL30m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q8TCC3](https://www.uniprot.org/uniprotkb/Q8TCC3) carries no function annotation.

**Summary**, from NCBI Gene [51263](https://www.ncbi.nlm.nih.gov/gene/51263):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14036) · Entrez [51263](https://www.ncbi.nlm.nih.gov/gene/51263) · UniProt [Q8TCC3](https://www.uniprot.org/uniprotkb/Q8TCC3) · Ensembl [ENSG00000185414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185414)

## Data

Gene col 11673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11673); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11673]; `tensor/DDL_lfc|DDL_z.npy` [11673]; `embed/gene_vectors.npy` [11673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11673 or target_col == 11673). Every well: [[MRPL30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
