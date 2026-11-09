---
symbol: "NFRKB"
type: "gene"
col: 9935
ensembl_id: "ENSG00000170322"
name: "nuclear factor related to kappaB binding protein"
location: "11q24.3"
module: 30
arm: "+"
pooled_cpm: 51.3
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NFRKB

*nuclear factor related to kappaB binding protein* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.20× (z +17.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.532× (z -13.9, q 3e-41, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.831× (z -4.1, q 0.005, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C32 0.0440×, A-427 0.132×, KATO III 0.298×, AsPC-1 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.0857×, HEC-1-A 0.225×, NCI-H1573 0.306×, A-427 0.223×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.207×, SW48 0.104×, MIA PaCa-2 0.239×, NCI-H2347 0.298×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0982×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYPOP]] (+0.74, fdr 7e-06), [[VDAC3]] (+0.73, fdr 7e-06), [[SLC9A6]] (+0.71, fdr 1e-05); moves opposite to [[SDCBP2-AS1]] (-0.68, fdr 1e-05), [[PPP3CB-AS1]] (-0.68, fdr 1e-05), [[ST7L]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZNF511]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +17.4 | 0e+00 | 46/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +16.1 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +13.4 | 1e-38 | 45/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +7.5 | 8e-12 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +6.5 | 7e-09 | 31/48 (H4, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +6.4 | 2e-08 | 29/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.2 | 5e-08 | 22/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.1 | 9e-08 | 25/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.9 | 2e-07 | 26/43 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +5.7 | 9e-07 | 29/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +4.4 | 5e-04 | 19/47 (KATO III, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.003 | 15/48 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.010 | 12/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 14/48 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.017 | 10/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 1.11× | +3.2 | 0.035 | 6/49 (SHP-77, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.035 | 12/48 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9935.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C32 0.0440×, A-427 0.132×, KATO III 0.298×, AsPC-1 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.0857×, HEC-1-A 0.225×, NCI-H1573 0.306×, A-427 0.223×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.207×, SW48 0.104×, MIA PaCa-2 0.239×, NCI-H2347 0.298×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.532×** | -13.9 | 3e-41 | 39/49 (C32, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -11.6 | 2e-28 | 31/44 (KATO III, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -7.7 | 3e-12 | 26/41 (AsPC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.822×** | -4.3 | 0.002 | 18/48 (C32, NCI-H1573, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.831×** | -4.1 | 0.005 | 17/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.860× | -3.3 | 0.077 | 8/48 (SW480, SW48, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.863× | -3.3 | 0.084 | 13/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.864× | -3.2 | 0.084 | 16/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.1 | 0.13 | 17/48 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.871× | -3.0 | 0.13 | 9/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 74.4 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -13.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 102 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.08× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -19.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 77.3 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 81.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -24.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 58.0 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 65.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.525× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 70.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -10.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 30.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +9.9) | — |
| [[C32 (line)]] | wt | 39.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0440× (z -24.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -18.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 33.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 23.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 44.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 52.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 63.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0982× (z -9.8) |
| [[RKO (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 75.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +8.7) | — |
| [[SW48 (line)]] | wt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -14.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYPOP]] | +0.74 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 | pathway: Deubiquitination |
| [[SLC9A6]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[MFSD9]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RNF149]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[NBPF3]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.68 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ATG4C]] | +0.67 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SUFU]] | +0.67 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[MAST3]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2-AS1]] | -0.68 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.68 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ST7L]] | -0.68 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.67 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[TSTD2]] | -0.67 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[MIS12]] | -0.67 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | -0.66 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.66 | -0.68 / -0.36 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.66 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.65 | -0.64 / -0.37 | both halves | 9e-05 |  |
| [[FKRP]] | -0.64 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H4]] | -0.64 | -0.66 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF511]] | C | NFRKB's natural level strengthens ZNF511's drug response | NFRKB's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.38; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.4, -6.7); signed map (-35.1, -5.2). **Vector** length 97.8, 23.3% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +17.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +16.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +13.4 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -6.8 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.4 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +3.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor related to kappaB binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:129,863,636-129,895,590 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp547B2013, INO80G |
| Gene groups (HGNC) | INO80 complex subunits |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4R8](https://www.uniprot.org/uniprotkb/Q6P4R8) (Nuclear factor related to kappa-B-binding protein):

> Binds to the DNA consensus sequence 5'-GGGGAATCTCC-3'.; Putative regulatory component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair. Modulates the deubiquitinase activity of UCHL5 in the INO80 complex.

**Summary**, from NCBI Gene [4798](https://www.ncbi.nlm.nih.gov/gene/4798):

> Enables protease binding activity. Involved in several processes, including positive regulation of DNA-templated transcription; regulation of DNA metabolic process; and regulation of chromosome organization. Located in Ino80 complex and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7802) · Entrez [4798](https://www.ncbi.nlm.nih.gov/gene/4798) · UniProt [Q6P4R8](https://www.uniprot.org/uniprotkb/Q6P4R8) · Ensembl [ENSG00000170322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170322)

## Data

Gene col 9935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9935); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9935]; `tensor/DDL_lfc|DDL_z.npy` [9935]; `embed/gene_vectors.npy` [9935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9935 or target_col == 9935). Every well: [[NFRKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFRKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
