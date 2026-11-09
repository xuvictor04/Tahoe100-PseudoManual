---
symbol: "RRAGC"
type: "gene"
col: 3858
ensembl_id: "ENSG00000116954"
name: "Ras related GTP binding C"
location: "1p34.3"
module: 59
arm: "+"
pooled_cpm: 42.77
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# RRAGC

*Ras related GTP binding C* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.85× (z +17.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.564× (z -6.1, q 7e-07, down in 28 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.247×, HS-578T 0.248×, HOP62 0.202×, AN3 CA 0.112×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.158×, A-427 0.173×, SNU-423 0.282×, A549 0.261×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.259×, NCI-H1573 0.277×, MIA PaCa-2 0.302×; ⚠ toxic; transcription drop); [[Valdecoxib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0753×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLCN]] (+0.76, fdr 7e-06), [[SAT2]] (+0.70, fdr 7e-06), [[KMT2A]] (+0.69, fdr 7e-06); moves opposite to [[MACROH2A1]] (-0.67, fdr 7e-06), [[TFDP1]] (-0.66, fdr 7e-06), [[ARHGAP4]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +17.0 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.92×** | +12.3 | 3e-32 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +10.9 | 3e-25 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +10.1 | 5e-22 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +9.8 | 1e-20 | 47/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.16×** | +8.8 | 9e-17 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.74×** | +7.9 | 2e-13 | 42/49 (NCI-H1573, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.0 | 1e-10 | 33/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.2 | 5e-08 | 31/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +5.7 | 9e-07 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 2e-06 | 37/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.4 | 4e-06 | 34/47 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +5.3 | 4e-06 | 33/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.9 | 3e-05 | 33/48 (A-427, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +4.9 | 5e-05 | 31/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.002 | 29/46 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +3.8 | 0.005 | 26/48 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.247×, HS-578T 0.248×, HOP62 0.202×, AN3 CA 0.112×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.158×, A-427 0.173×, SNU-423 0.282×, A549 0.261×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.259×, NCI-H1573 0.277×, MIA PaCa-2 0.302×; ⚠ toxic; transcription drop); [[Valdecoxib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0753×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -6.1 | 7e-07 | 28/40 (A-172, A-427, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.636×** | -5.2 | 6e-05 | 26/46 (RKO, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -5.1 | 6e-05 | 25/37 (Panc 03.27, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.5 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +20.5) | — |
| [[PANC-1 (line)]] | alt | 46.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +19.8) | — |
| [[A-427 (line)]] | wt | 45.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 32.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +17.5) | — |
| [[COLO 205 (line)]] | alt | 30.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 93.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 50.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +14.5) | — |
| [[HEC-1-A (line)]] | alt | 43.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 38.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 45.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.2) | [[Lonafarnib (drug)]] 5 µM 0.101× (z -8.9) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 37.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -8.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 44.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 65.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -14.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 37.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 77.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 75.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +13.5) | — |
| [[LoVo (line)]] | wt | 22.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 20.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +16.7) | — |
| [[NCI-H2347 (line)]] | alt | 56.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 92.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.4) | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0753× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 61.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 33.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLCN]] | +0.76 | +0.79 / +0.73 | both halves | 7e-06 | pathway: Amino acids regulate mTORC1; STRING 999 |
| [[SAT2]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[KMT2A]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | +0.68 | +0.67 / +0.68 | both halves | 7e-06 | pathway: Autophagy; ⚠ in the vector space only through flagged drug-doses |
| [[RAB9A]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[HEIH]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[OPTN]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 | pathway: Autophagy |
| [[MITD1]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LACTB]] | +0.65 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[ZFYVE1]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PLEKHM2]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[WHAMM]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.67 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.66 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[ARHGAP4]] | -0.64 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[GCN1]] | -0.63 | -0.59 / -0.64 | both halves | 7e-06 | pathway: Cellular response to starvation |
| [[TXNDC5]] | -0.63 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[BANF1]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.61 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[NUP188]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.61 | -0.57 / -0.62 | both halves | 9e-06 | STRING 418 |
| [[PAICS]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-35.9, -28.9); signed map (-7.2, 0.4). **Vector** length 125, 42.6% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +2.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.5 | +1.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +4.5 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | +0.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[ML264 (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Ras related GTP binding C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:38,838,198-38,859,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GTR2, FLJ13311 |
| Gene groups (HGNC) | Ras related GTP binding proteins |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB90](https://www.uniprot.org/uniprotkb/Q9HB90) (Ras-related GTP-binding protein C):

> Guanine nucleotide-binding protein that plays a crucial role in the cellular response to amino acid availability through regulation of the mTORC1 signaling cascade. Forms heterodimeric Rag complexes with RagA/RRAGA or RagB/RRAGB and cycles between an inactive GTP-bound and an active GDP-bound form: RagC/RRAGC is in its active form when GDP-bound RagC/RRAGC forms a complex with GTP-bound RagA/RRAGA (or RagB/RRAGB) and in an inactive form when GTP-bound RagC/RRAGC heterodimerizes with GDP-bound …

**Summary**, from NCBI Gene [64121](https://www.ncbi.nlm.nih.gov/gene/64121):

> This gene encodes a member of the GTR/RAG GTP-binding protein family. The encoded protein is a monomeric guanine nucleotide-binding protein which forms a heterodimer with RRAGA and RRAGB and is primarily localized to the cytoplasm. The encoded protein promotes intracellular localization of the mTOR complex. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:19902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19902) · Entrez [64121](https://www.ncbi.nlm.nih.gov/gene/64121) · UniProt [Q9HB90](https://www.uniprot.org/uniprotkb/Q9HB90) · Ensembl [ENSG00000116954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116954)

## Data

Gene col 3858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3858); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3858]; `tensor/DDL_lfc|DDL_z.npy` [3858]; `embed/gene_vectors.npy` [3858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3858 or target_col == 3858). Every well: [[RRAGC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAGC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
