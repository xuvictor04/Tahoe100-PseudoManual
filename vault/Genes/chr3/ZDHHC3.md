---
symbol: "ZDHHC3"
type: "gene"
col: 8785
ensembl_id: "ENSG00000163812"
name: "zDHHC palmitoyltransferase 3"
location: "3p21.31"
module: 50
arm: "+"
pooled_cpm: 44.28
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ZDHHC3

*zDHHC palmitoyltransferase 3* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.06× (z +19.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.857× (z -5.9, q 2e-06, down in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~0% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (LoVo 0.396×, A-427 0.382×, LS 180 0.470×, C32 0.364×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LS 180 0.351×, C32 0.293×, LoVo 0.461×; ⚠ cell-cycle shift, explains ~18% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.517×, LoVo 0.576×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (LS 180 0.494×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM15]] (+0.68, fdr 7e-06), [[CDC42BPB]] (+0.64, fdr 9e-06), [[BLTP2]] (+0.62, fdr 1e-05); moves opposite to [[PLA2G4C]] (-0.61, fdr 1e-05), [[UPF3B]] (-0.58, fdr 3e-05), [[SEC62]] (-0.57, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +19.5 | 0e+00 | 46/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +19.4 | 0e+00 | 42/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +18.0 | 0e+00 | 42/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +16.8 | 0e+00 | 36/48 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +11.2 | 5e-27 | 35/47 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +9.9 | 4e-21 | 36/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +8.3 | 8e-15 | 31/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.34×** | +7.9 | 2e-13 | 27/45 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +7.3 | 2e-11 | 30/48 (AsPC-1, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.32×** | +7.2 | 4e-11 | 23/40 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.31×** | +7.1 | 9e-11 | 28/47 (HOP62, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +5.3 | 6e-06 | 18/48 (HOP62, SW480, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.21×** | +5.2 | 1e-05 | 17/48 (J82, A498, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.1 | 1e-05 | 18/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 19/48 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.017 | 6/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.018 | 7/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[OTS514 (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.041 | 9/45 (J82, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.12× | +3.1 | 0.052 | 13/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (LoVo 0.396×, A-427 0.382×, LS 180 0.470×, C32 0.364×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LS 180 0.351×, C32 0.293×, LoVo 0.461×; ⚠ cell-cycle shift, explains ~18% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.517×, LoVo 0.576×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (LS 180 0.494×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -5.9 | 2e-06 | 23/47 (LoVo, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.820×** | -5.3 | 2e-05 | 15/48 (C-33 A, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -4.7 | 4e-04 | 12/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.852× | -4.3 | 0.002 | 20/47 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.0 | 0.007 | 16/48 (C32, SW 1088, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.864× | -4.0 | 0.007 | 8/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 101 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.2) |
| [[C32 (line)]] | wt | 67.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 67.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 140 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.7) |
| [[HOP62 (line)]] | alt | 33.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 71.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 33.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[A-172 (line)]] | wt | 34.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +8.9) | — |
| [[A-427 (line)]] | wt | 40.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.13× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 31.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW480 (line)]] | alt | 51.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.98× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 36.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 27.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 33.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[A498 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM15]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CDC42BPB]] | +0.64 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[BLTP2]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ELAVL1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ITPK1]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ATG16L1]] | +0.57 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[IMPA2]] | +0.57 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[PYGB]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G4C]] | -0.61 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.58 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[SEC62]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[NFKBIB]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[LRCH3]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZNF226]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CRYM]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.55 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PBDC1]] | -0.55 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[RNF103-CHMP3]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ATF4]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[HDAC9]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, 1.2); signed map (-11.2, 36.8). **Vector** length 104, 25.2% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +6.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +5.9 | +7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +4.8 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +7.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -7.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:44,915,257-44,976,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF373, GODZ, DHHC3 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 6 pathways, smallest: Maturation of spike protein_9694548; Translation of Structural Proteins_9694635; Late SARS-CoV-2 Infection Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYG2](https://www.uniprot.org/uniprotkb/Q9NYG2) (Palmitoyltransferase ZDHHC3):

> Golgi-localized palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates. Has no stringent fatty acid selectivity and in addition to palmitate can also transfer onto target proteins myristate from tetradecanoyl-CoA and stearate from octadecanoyl-CoA (By similarity). Plays an important role in G protein-coupled receptor signaling pathways involving GNAQ and potentially other heterotrimeric G proteins by regulating their dynamic association with the plasma …

**Summary**, from NCBI Gene [51304](https://www.ncbi.nlm.nih.gov/gene/51304):

> Enables palmitoyltransferase activity. Involved in several processes, including TRAIL-activated apoptotic signaling pathway; protein localization to photoreceptor outer segment; and regulation of signal transduction. Located in membrane. Is active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18470) · Entrez [51304](https://www.ncbi.nlm.nih.gov/gene/51304) · UniProt [Q9NYG2](https://www.uniprot.org/uniprotkb/Q9NYG2) · Ensembl [ENSG00000163812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163812)

## Data

Gene col 8785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8785); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8785]; `tensor/DDL_lfc|DDL_z.npy` [8785]; `embed/gene_vectors.npy` [8785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8785 or target_col == 8785). Every well: [[ZDHHC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
