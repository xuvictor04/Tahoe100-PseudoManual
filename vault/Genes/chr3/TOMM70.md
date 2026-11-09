---
symbol: "TOMM70"
type: "gene"
col: 7781
ensembl_id: "ENSG00000154174"
name: "translocase of outer mitochondrial membrane 70"
location: "3q12.2"
module: 40
arm: "+"
pooled_cpm: 82.55
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# TOMM70

*translocase of outer mitochondrial membrane 70* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.55× (z +13.7, q 5e-40, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.638× (z -12.1, q 6e-31, down in 29 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.883× (z -4.9, q 1e-04, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (Panc 03.27 0.0725×, SHP-77 0.217×, A-427 0.261×, HS-578T 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.0498×, PANC-1 0.290×, RPMI-7951 0.285×, A-172 0.345×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.537×; ⚠ cell-cycle shift, explains ~0% of this change); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.110×); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0737×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM11]] (+0.72, fdr 7e-06), [[ALG3]] (+0.69, fdr 7e-06), [[NAA20]] (+0.66, fdr 1e-05); moves opposite to [[PLA2G4C]] (-0.57, fdr 1e-05), [[P2RX4]] (-0.57, fdr 2e-05), [[SPAG1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +13.7 | 5e-40 | 44/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +10.4 | 8e-23 | 36/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +9.7 | 4e-20 | 38/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +8.6 | 7e-16 | 34/48 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +8.5 | 2e-15 | 31/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.35×** | +8.5 | 2e-15 | 34/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +8.1 | 7e-14 | 31/48 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +8.0 | 8e-14 | 33/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +7.8 | 3e-13 | 39/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +7.1 | 8e-11 | 34/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +6.3 | 1e-08 | 27/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.26×** | +6.1 | 4e-08 | 24/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +5.3 | 4e-06 | 28/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +5.0 | 3e-05 | 23/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.34×** | +4.3 | 6e-04 | 20/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.34×** | +4.2 | 8e-04 | 22/48 (NCI-H460, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +4.2 | 9e-04 | 15/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.010 | 13/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.013 | 13/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Hesperidin (drug)]] 5 µM |  | 1.13× | +3.3 | 0.028 | 5/48 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.031 | 13/48 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.12× | +3.1 | 0.052 | 7/48 (SNU-423, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7781.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (Panc 03.27 0.0725×, SHP-77 0.217×, A-427 0.261×, HS-578T 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.0498×, PANC-1 0.290×, RPMI-7951 0.285×, A-172 0.345×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.537×; ⚠ cell-cycle shift, explains ~0% of this change); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.110×); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0737×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -12.1 | 6e-31 | 29/44 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.703×** | -9.9 | 1e-20 | 30/49 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.834× | -5.1 | 7e-05 | 20/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -4.9 | 1e-04 | 14/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.854× | -4.2 | 0.002 | 15/47 (COLO 205, A549, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.751×** | -4.2 | 0.003 | 20/48 (CFPAC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.854× | -4.1 | 0.003 | 20/47 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.874× | -3.6 | 0.020 | 13/47 (HOP62, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.885× | -3.4 | 0.039 | 19/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.891× | -3.2 | 0.067 | 12/47 (A-172, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 0.926× | -3.1 | 0.11 | 1/48 (AsPC-1) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 106 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.51× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -20.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 73.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.9 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.00× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -15.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -18.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 72.2 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.55× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.479× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 61.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.84× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0498× (z -43.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 84.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 85.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -17.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 92.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.37× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 73.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.7) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.17× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 75.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -31.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 84.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.18× (z +10.2) | — |
| [[A498 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.331× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -16.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 93.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.486× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +10.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H596 (line)]] | alt | 77.1 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.110× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -15.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -19.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.545× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 86.8 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0737× (z -9.7) |
| [[SW 1271 (line)]] | alt | 75.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.110× (z -9.2) |
| [[A549 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ALG3]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NAA20]] | +0.66 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FTO]] | +0.66 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[ZW10]] | +0.64 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[GORASP2]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[POLR3A]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[WDR3]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[COASY]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RARS1]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4C]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[P2RX4]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[SPAG1]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 | same gene group |
| [[MAFK]] | -0.53 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.53 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[AGRN]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-10.1, -30.4); signed map (-14.9, -56.3). **Vector** length 115, 30.4% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +10.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +13.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +9.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.3 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +8.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +4.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,363,431-100,401,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0719, Tom70; previously TOMM70A |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Translocase of outer mitochondrial membrane complex |
| Hallmark sets | MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 19 pathways, smallest: PINK1-PRKN Mediated Mitophagy; SARS-CoV-1 activates/modulates innate immune responses; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [O94826](https://www.uniprot.org/uniprotkb/O94826) (Mitochondrial import receptor subunit TOM70):

> Acts as a receptor of the preprotein translocase complex of the outer mitochondrial membrane (TOM complex). Recognizes and mediates the translocation of mitochondrial preproteins from the cytosol into the mitochondria in a chaperone dependent manner. Mediates TBK1 and IRF3 activation induced by MAVS in response to Sendai virus infection and promotes host antiviral responses during virus infection. Upon Sendai virus infection, recruits HSP90AA1:IRF3:BAX in mitochondrion and the complex induces …

**Summary**, from NCBI Gene [9868](https://www.ncbi.nlm.nih.gov/gene/9868):

> This gene encodes an import receptor of the outer mitochondrial membrane that is part of the translocase of the outer membrane complex. This protein is involved in the import of mitochondrial precursor proteins. The protein interacts with the SARS-CoV and SARS-Cov-2 ORF9b proteins. [provided by RefSeq, Dec 2021]

**Accessions** — [HGNC:11985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11985) · Entrez [9868](https://www.ncbi.nlm.nih.gov/gene/9868) · UniProt [O94826](https://www.uniprot.org/uniprotkb/O94826) · Ensembl [ENSG00000154174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154174)

## Data

Gene col 7781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7781); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7781]; `tensor/DDL_lfc|DDL_z.npy` [7781]; `embed/gene_vectors.npy` [7781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7781 or target_col == 7781). Every well: [[TOMM70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
