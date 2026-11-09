---
symbol: "PRDM2"
type: "gene"
col: 3830
ensembl_id: "ENSG00000116731"
name: "PR/SET domain 2"
location: "1p36.21"
module: 46
arm: "+"
pooled_cpm: 94.04
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PRDM2

*PR/SET domain 2* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +31.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.785× (z -5.5, q 2e-05, down in 27 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SHP-77 0.226×, HepG2/C3A 0.369×, LOX-IMVI 0.433×, NCI-H2030 0.480×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.356×, NCI-H2030 0.353×, HepG2/C3A 0.421×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.187×, NCI-H2030 0.457×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (56 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 44 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD5]] (+0.65, fdr 1e-05), [[NCOA2]] (+0.62, fdr 7e-05), [[AP4S1]] (+0.62, fdr 1e-04); moves opposite to [[TXNL4A]] (-0.59, fdr 2e-04), [[NAA40]] (-0.58, fdr 2e-04), [[MRPL14]] (-0.58, fdr 7e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +31.3 | 0e+00 | 46/48 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +25.2 | 0e+00 | 47/49 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +17.1 | 0e+00 | 46/48 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +13.8 | 4e-41 | 43/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +11.7 | 9e-30 | 46/48 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +11.3 | 2e-27 | 41/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +10.5 | 1e-23 | 37/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +9.7 | 2e-20 | 38/50 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +8.5 | 9e-16 | 42/48 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +8.0 | 6e-14 | 40/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +7.7 | 8e-13 | 37/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +7.0 | 1e-10 | 30/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +6.6 | 2e-09 | 29/48 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.6 | 7e-07 | 28/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.6 | 9e-07 | 32/48 (C32, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.6 | 1e-04 | 16/48 (BT-474, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 1e-04 | 25/47 (SW48, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SHP-77 0.226×, HepG2/C3A 0.369×, LOX-IMVI 0.433×, NCI-H2030 0.480×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H23 0.356×, NCI-H2030 0.353×, HepG2/C3A 0.421×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.187×, NCI-H2030 0.457×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.785×** | -5.5 | 2e-05 | 27/49 (NCI-H23, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.824×** | -4.2 | 0.007 | 22/44 (SHP-77, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.891× | -3.7 | 0.043 | 7/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.859× | -3.5 | 0.079 | 13/47 (CFPAC-1, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 88.2 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +29.5) | — |
| [[NCI-H460 (line)]] | wt | 82.1 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +23.2) | — |
| [[KATO III (line)]] | alt | 81.8 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +21.9) | — |
| [[SW480 (line)]] | alt | 104 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +20.6) | — |
| [[HT-29 (line)]] | alt | 79.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +21.6) | — |
| [[BT-474 (line)]] | alt | 95.9 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +15.5) | — |
| [[C32 (line)]] | wt | 88.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +25.4) | — |
| [[COLO 205 (line)]] | alt | 107 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +20.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 84.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +21.4) | — |
| [[HEC-1-A (line)]] | alt | 87.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +19.2) | — |
| [[HOP62 (line)]] | alt | 110 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +22.5) | — |
| [[LOX-IMVI (line)]] | wt | 78.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 128 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +15.8) | — |
| [[NCI-H2030 (line)]] | alt | 98.1 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 112 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +16.7) | — |
| [[SW1417 (line)]] | alt | 101 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +20.8) | — |
| [[CFPAC-1 (line)]] | alt | 106 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +27.9) | — |
| [[Hs 766T (line)]] | wt | 82.4 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 118 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 60.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +18.1) | — |
| [[NCI-H1573 (line)]] | alt | 106 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +21.2) | — |
| [[Panc 03.27 (line)]] | alt | 84.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.0) | — |
| [[RKO (line)]] | wt | 98.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +15.3) | — |
| [[A-172 (line)]] | wt | 45.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +18.2) | — |
| [[AsPC-1 (line)]] | alt | 94.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +16.9) | — |
| [[H4 (line)]] | wt | 96.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 151 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 94.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +16.8) | — |
| [[NCI-H1792 (line)]] | alt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +23.3) | — |
| [[NCI-H2347 (line)]] | alt | 94.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +19.8) | — |
| [[RPMI-7951 (line)]] | alt | 121 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.9) | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +20.9) | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 65.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.7) | — |
| [[SW 900 (line)]] | alt | 82.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +16.5) | — |
| [[SW48 (line)]] | wt | 68.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +11.6) | — |
| [[A549 (line)]] | wt | 81.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 132 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.9) | — |
| [[SHP-77 (line)]] | alt | 106 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -17.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 91.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 65.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.235× (z -11.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.4) | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 0.5 µM 0.102× (z -9.0) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 38 of them with an alert (⚠; 38 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD5]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[NCOA2]] | +0.62 | +0.52 / +0.37 | both halves | 7e-05 |  |
| [[AP4S1]] | +0.62 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[ATP11C]] | +0.61 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[RBMX]] | +0.61 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CSRNP2]] | +0.60 | +0.62 / +0.32 | both halves | 2e-04 |  |
| [[PXDNL]] | +0.59 | +0.54 / +0.24 | both halves | 4e-04 |  |
| [[SEC24B-AS1]] | +0.59 | +0.47 / +0.25 | both halves | 4e-04 |  |
| [[ICA1L]] | +0.59 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[RNF217-AS1]] | +0.59 | +0.43 / +0.24 | both halves | 5e-04 |  |
| [[PBLD]] | +0.58 | +0.45 / +0.16 | ⚠ not reproduced | 0.001 |  |
| [[WDFY3]] | +0.58 | +0.30 / +0.44 | both halves | 2e-04 |  |
| [[C2orf76]] | +0.56 | +0.43 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4A]] | -0.59 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[NAA40]] | -0.58 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[MRPL14]] | -0.58 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[MAGEF1]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[GUSBP18]] | -0.56 | -0.53 / -0.21 | both halves | 6e-04 |  |
| [[DDX55]] | -0.55 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[NME7]] | -0.54 | -0.55 / -0.23 | both halves | 5e-04 |  |
| [[RRP1B]] | -0.54 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[INIP]] | -0.54 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[WRAP73]] | -0.53 | -0.30 / -0.24 | both halves | 4e-04 |  |
| [[PELP1]] | -0.53 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[HMGXB3]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (7.2, 9.7); signed map (22.2, -8.1). **Vector** length 80.7, 21.2% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +25.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +13.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -5.3 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | +3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:13,700,188-13,825,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIZ, RIZ1, RIZ2, KMT8, MTB-ZF, HUMHOXY1, KMT8A |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13029](https://www.uniprot.org/uniprotkb/Q13029) (PR domain zinc finger protein 2):

> S-adenosyl-L-methionine-dependent histone methyltransferase that specifically methylates 'Lys-9' of histone H3. May function as a DNA-binding transcription factor. Binds to the macrophage-specific TPA-responsive element (MTE) of the HMOX1 (heme oxygenase 1) gene and may act as a transcriptional activator of this gene.

**Summary**, from NCBI Gene [7799](https://www.ncbi.nlm.nih.gov/gene/7799):

> This tumor suppressor gene is a member of a nuclear histone/protein methyltransferase superfamily. It encodes a zinc finger protein that can bind to retinoblastoma protein, estrogen receptor, and the TPA-responsive element (MTE) of the heme-oxygenase-1 gene. Although the functions of this protein have not been fully characterized, it may (1) play a role in transcriptional regulation during neuronal differentiation and pathogenesis of retinoblastoma, (2) act as a transcriptional activator of the …

**Accessions** — [HGNC:9347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9347) · Entrez [7799](https://www.ncbi.nlm.nih.gov/gene/7799) · UniProt [Q13029](https://www.uniprot.org/uniprotkb/Q13029) · Ensembl [ENSG00000116731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116731)

## Data

Gene col 3830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3830); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3830]; `tensor/DDL_lfc|DDL_z.npy` [3830]; `embed/gene_vectors.npy` [3830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3830 or target_col == 3830). Every well: [[PRDM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
