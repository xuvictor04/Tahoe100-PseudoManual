---
symbol: "ZMYM5"
type: "gene"
col: 5393
ensembl_id: "ENSG00000132950"
name: "zinc finger MYM-type containing 5"
location: "13q12.11"
module: 20
arm: "-"
pooled_cpm: 63.55
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ZMYM5

*zinc finger MYM-type containing 5* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +26.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.632× (z -7.8, q 4e-12, down in 28 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.790× (z -4.0, q 0.006, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 0.0626×, A498 0.342×, A549 0.276×, NCI-H661 0.0824×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1573 0.225×, A-427 0.212×, HT-29 0.387×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.163×, SNU-1 0.141×; ⚠ toxic; transcription drop); [[Futibatinib (drug)]] 5 µM in 1 line (SNU-1 0.0629×); [[Pimozide (drug)]] 0.05 µM in 1 line (SW 1271 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TERF2IP]] (+0.85, fdr 7e-06), [[MPHOSPH8]] (+0.73, fdr 7e-06), [[GGNBP2]] (+0.73, fdr 7e-06); moves opposite to [[PRKDC]] (-0.78, fdr 7e-06), [[MAT2A]] (-0.73, fdr 7e-06), [[EFTUD2]] (-0.73, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MPHOSPH8]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +26.4 | 0e+00 | 46/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +14.5 | 6e-45 | 46/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +12.4 | 3e-33 | 45/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +11.9 | 1e-30 | 43/48 (PANC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.9 | 9e-05 | 27/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.5 | 5e-04 | 28/47 (SW480, LS 180, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.7 | 0.016 | 24/46 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.043 | 21/47 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.051 | 20/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.064 | 10/47 (A-427, COLO 205, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.20×** | +3.2 | 0.068 | 16/47 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.20× | +3.2 | 0.068 | 19/47 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.071 | 10/48 (NCI-H2347, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5393.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 0.0626×, A498 0.342×, A549 0.276×, NCI-H661 0.0824×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1573 0.225×, A-427 0.212×, HT-29 0.387×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.163×, SNU-1 0.141×; ⚠ toxic; transcription drop); [[Futibatinib (drug)]] 5 µM in 1 line (SNU-1 0.0629×); [[Pimozide (drug)]] 0.05 µM in 1 line (SW 1271 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -7.8 | 4e-12 | 28/40 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.669×** | -6.6 | 1e-08 | 28/44 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -6.4 | 3e-08 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -5.8 | 1e-06 | 35/47 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.682×** | -5.3 | 2e-05 | 29/48 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -4.0 | 0.006 | 23/47 (LoVo, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 150 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 47.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +23.4) | — |
| [[COLO 205 (line)]] | alt | 170 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +22.8) | — |
| [[LOX-IMVI (line)]] | wt | 63.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 65.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +24.0) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -13.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 44.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.8) | — |
| [[RKO (line)]] | wt | 65.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 84.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +21.2) | — |
| [[A-427 (line)]] | wt | 36.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 80.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +19.5) | — |
| [[HEC-1-A (line)]] | alt | 70.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +19.2) | — |
| [[LoVo (line)]] | wt | 76.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +22.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 66.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.1) | — |
| [[SNU-1 (line)]] | wt | 63.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Futibatinib (drug)]] 5 µM 0.0629× (z -11.0) |
| [[A-172 (line)]] | wt | 75.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.7) | — |
| [[A498 (line)]] | wt | 76.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 72.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.5) | — |
| [[BT-474 (line)]] | alt | 76.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 51.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 61.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.8) | — |
| [[hTERT-HPNE (line)]] | wt | 57.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.0) | — |
| [[J82 (line)]] | alt | 70.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +18.6) | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 40.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 93.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.0626× (z -31.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 56.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.9) | — |
| [[SW48 (line)]] | wt | 45.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 50.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.8) | — |
| [[H4 (line)]] | wt | 42.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 87.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 50.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 82.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.3) | — |
| [[NCI-H661 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0824× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 69.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.4) | — |
| [[SW 1271 (line)]] | alt | 66.6 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[AN3 CA (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 88.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | +0.73 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[GGNBP2]] | +0.73 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[ZNF821]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ING2]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[NKAP]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[MED19]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ARID4B]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 | STRING 410 |
| [[ARID4A]] | +0.69 | +0.70 / +0.71 | both halves | 7e-06 | STRING 467 |
| [[NDUFC1]] | +0.69 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[EAPP]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[RSF1]] | +0.67 | +0.71 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.78 | -0.74 / -0.73 | both halves | 7e-06 |  |
| [[MAT2A]] | -0.73 | -0.71 / -0.72 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.73 | -0.71 / -0.71 | both halves | 7e-06 |  |
| [[RPSA]] | -0.73 | -0.69 / -0.71 | both halves | 7e-06 |  |
| [[VMA21]] | -0.72 | -0.60 / -0.78 | both halves | 7e-06 |  |
| [[RPE]] | -0.71 | -0.63 / -0.73 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.71 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.71 | -0.71 / -0.68 | both halves | 7e-06 |  |
| [[PRPS1]] | -0.69 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[CHID1]] | -0.69 | -0.74 / -0.59 | both halves | 7e-06 |  |
| [[ICMT]] | -0.69 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[TMX1]] | -0.69 | -0.63 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPHOSPH8]] | C | ZMYM5's natural level strengthens MPHOSPH8's drug response | ZMYM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.44; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.6, -30.0); signed map (-7.6, 4.9). **Vector** length 123, 35.7% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +26.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +14.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYM-type containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:19,823,482-19,863,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF198L1, MYM; previously ZNF237 |
| Gene groups (HGNC) | Zinc fingers MYM-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ78](https://www.uniprot.org/uniprotkb/Q9UJ78) (Zinc finger MYM-type protein 5):

> Functions as a transcriptional regulator.

**Summary**, from NCBI Gene [9205](https://www.ncbi.nlm.nih.gov/gene/9205):

> Predicted to enable zinc ion binding activity. Involved in negative regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13029) · Entrez [9205](https://www.ncbi.nlm.nih.gov/gene/9205) · UniProt [Q9UJ78](https://www.uniprot.org/uniprotkb/Q9UJ78) · Ensembl [ENSG00000132950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132950)

## Data

Gene col 5393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5393); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5393]; `tensor/DDL_lfc|DDL_z.npy` [5393]; `embed/gene_vectors.npy` [5393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5393 or target_col == 5393). Every well: [[ZMYM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
