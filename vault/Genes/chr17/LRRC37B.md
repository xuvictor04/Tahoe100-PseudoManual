---
symbol: "LRRC37B"
type: "gene"
col: 11632
ensembl_id: "ENSG00000185158"
name: "leucine rich repeat containing 37B"
location: "17q11.2"
module: 59
arm: "+"
pooled_cpm: 20.52
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# LRRC37B

*leucine rich repeat containing 37B* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +12.1, q 1e-30, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.463× (z -12.4, q 9e-33, down in 29 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.782× (z -5.9, q 2e-07, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRSAM1]] (+0.68, fdr 7e-06), [[TRNAU1AP]] (+0.65, fdr 7e-06), [[TRPM7]] (+0.64, fdr 1e-05); moves opposite to [[CORO1C]] (-0.64, fdr 1e-05), [[APEH]] (-0.63, fdr 2e-05), [[RUVBL1]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +12.1 | 1e-30 | 38/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +9.7 | 8e-20 | 32/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.3 | 2e-18 | 29/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +6.9 | 9e-10 | 26/48 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +6.8 | 1e-09 | 31/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.6 | 5e-09 | 22/46 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 25/48 (KATO III, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 2e-05 | 22/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.004 | 16/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.007 | 13/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 16/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.009 | 18/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.017 | 14/46 (J82, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.018 | 8/48 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.5 | 0.018 | 13/48 (RKO, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.039 | 12/48 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.463×** | -12.4 | 9e-33 | 29/35 (A-172, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.505×** | -11.5 | 5e-28 | 22/32 (HEC-1-A, HS-578T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.524×** | -11.3 | 2e-27 | 27/41 (A-172, SNU-423, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.570×** | -9.8 | 1e-20 | 40/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.573×** | -9.7 | 3e-20 | 33/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.683×** | -6.7 | 3e-09 | 26/47 (A-172, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -6.4 | 2e-08 | 25/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -5.9 | 2e-07 | 24/48 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.603×** | -4.6 | 2e-04 | 17/45 (RPMI-7951, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.790×** | -4.1 | 0.002 | 17/47 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.872× | -3.3 | 0.048 | 7/48 (SW 1271, BT-474, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.048 | 11/48 (MIA PaCa-2, SW 1088, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.817×** | -3.1 | 0.069 | 5/48 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.819×** | -3.1 | 0.069 | 9/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.819×** | -3.1 | 0.069 | 8/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -3.1 | 0.069 | 12/48 (HS-578T, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 40.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0998× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.238× (z -8.5) |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 17.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +19.2) | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 2 | — | [[Monocrotaline (drug)]] 0.05 µM 0.101× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[PANC-1 (line)]] | alt | 22.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRSAM1]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TRNAU1AP]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TRPM7]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[FLCN]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ZCCHC8]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[THAP3]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZNF821]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[DYRK1B]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SLC26A11]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TSC1]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EIF3J-DT]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[APEH]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[RUVBL1]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[FKBP1A]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TTLL12]] | -0.57 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ACTB]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RSU1]] | -0.56 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ITGB1]] | -0.56 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SPCS3]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-38.0, -17.5); signed map (-4.7, 0.9). **Vector** length 104, 24.2% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +5.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.6 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.2 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.1 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -3.2 | -12.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 37B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,007,383-32,053,504 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q96QE4](https://www.uniprot.org/uniprotkb/Q96QE4) carries no function annotation.

**Summary**, from NCBI Gene [114659](https://www.ncbi.nlm.nih.gov/gene/114659):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29070) · Entrez [114659](https://www.ncbi.nlm.nih.gov/gene/114659) · UniProt [Q96QE4](https://www.uniprot.org/uniprotkb/Q96QE4) · Ensembl [ENSG00000185158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185158)

## Data

Gene col 11632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11632); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11632]; `tensor/DDL_lfc|DDL_z.npy` [11632]; `embed/gene_vectors.npy` [11632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11632 or target_col == 11632). Every well: [[LRRC37B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC37B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
