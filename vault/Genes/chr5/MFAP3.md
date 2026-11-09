---
symbol: "MFAP3"
type: "gene"
col: 444
ensembl_id: "ENSG00000037749"
name: "microfibril associated protein 3"
location: "5q33.2"
module: 7
arm: "+"
pooled_cpm: 39.97
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MFAP3

*microfibril associated protein 3* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.39× (z +16.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.666× (z -7.9, q 2e-12, down in 33 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bendamustine (drug)]] 5 µM: 0.821× (z -3.7, q 0.030, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.190×, NCI-H2030 0.175×, NCI-H1573 0.181×, C32 0.242×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.238×, LS 180 0.292×, COLO 205 0.226×, HEC-1-A 0.414×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.244×, SW480 0.401×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF561]] (+0.61, fdr 3e-05), [[PYM1]] (+0.61, fdr 4e-05), [[PIGC]] (+0.55, fdr 1e-05); moves opposite to [[CSPP1]] (-0.61, fdr 2e-05), [[NAP1L1]] (-0.49, fdr 5e-05), [[DCUN1D4]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +16.9 | 0e+00 | 45/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +15.8 | 0e+00 | 45/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +12.9 | 5e-36 | 43/48 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +12.1 | 2e-31 | 36/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.4 | 2e-11 | 33/48 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +6.9 | 6e-10 | 26/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.8 | 1e-09 | 27/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.6 | 1e-06 | 26/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.34×** | +5.4 | 4e-06 | 27/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 8e-06 | 24/48 (hTERT-HPNE, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.4 | 5e-04 | 21/48 (A498, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +4.4 | 5e-04 | 21/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.25×** | +4.3 | 7e-04 | 19/48 (RKO, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.1 | 0.002 | 13/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.16× | +4.0 | 0.003 | 21/48 (NCI-H2347, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 16/48 (A498, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.017 | 15/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.2 | 0.036 | 8/48 (A498, HOP62, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +2.9 | 0.078 | 2/48 (RKO, CFPAC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 444.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 0.190×, NCI-H2030 0.175×, NCI-H1573 0.181×, C32 0.242×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.238×, LS 180 0.292×, COLO 205 0.226×, HEC-1-A 0.414×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.244×, SW480 0.401×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -7.9 | 2e-12 | 33/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -6.6 | 1e-08 | 21/40 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.749×** | -5.4 | 1e-05 | 27/47 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Bendamustine (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.030 | 18/48 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 0.836× | -3.5 | 0.054 | 21/48 (NCI-H460, SW480, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.732× | -3.2 | 0.14 | 7/47 (CFPAC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.781× | -3.1 | 0.18 | 11/47 (SW 1271, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 31.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 38.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.37× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 68.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 28.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 40.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 63.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +12.5) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.26× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 54.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.0) | [[Lonafarnib (drug)]] 5 µM 0.0928× (z -12.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 32.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.98× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 44.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 36.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.420× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 46.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.9) | — |
| [[A-172 (line)]] | wt | 51.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +11.2) | — |
| [[A-427 (line)]] | wt | 41.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 38.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +9.2) | — |
| [[LoVo (line)]] | wt | 58.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 32.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -15.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.109× (z -10.7) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 34.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[RKO (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 79.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 37.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF561]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[PYM1]] | +0.61 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[PIGC]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SZT2]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ASAH2B]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CHAMP1]] | +0.53 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[DGUOK]] | +0.50 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[TTPAL]] | +0.50 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[PGBD2]] | +0.49 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TIMM17A]] | +0.49 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ZNF408]] | +0.49 | +0.53 / +0.25 | both halves | 4e-04 |  |
| [[TMEM128]] | +0.48 | +0.64 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSPP1]] | -0.61 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NAP1L1]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[DCUN1D4]] | -0.47 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RPS6KA5]] | -0.47 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[PDE8A]] | -0.46 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NR6A1]] | -0.45 | -0.46 / -0.24 | both halves | 5e-04 |  |
| [[UBE4B]] | -0.45 | -0.50 / -0.37 | both halves | 9e-05 |  |
| [[VPS13A]] | -0.44 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[DLG1]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[WDR19]] | -0.43 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[TRIM37]] | -0.42 | -0.24 / -0.21 | both halves | 6e-04 |  |
| [[PRXL2A]] | -0.42 | -0.43 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.7, 22.0); signed map (3.5, -25.3). **Vector** length 65.4, 12.0% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +6.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.6 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.5 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.0 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.8 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | +0.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | microfibril associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,038,959-154,220,478 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | I-set domain containing |
| Reactome | 3 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55082](https://www.uniprot.org/uniprotkb/P55082) (Microfibril-associated glycoprotein 3):

> Component of the elastin-associated microfibrils.

**Summary**, from NCBI Gene [4238](https://www.ncbi.nlm.nih.gov/gene/4238):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7034) · Entrez [4238](https://www.ncbi.nlm.nih.gov/gene/4238) · UniProt [P55082](https://www.uniprot.org/uniprotkb/P55082) · Ensembl [ENSG00000037749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037749)

## Data

Gene col 444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 444); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 444]; `tensor/DDL_lfc|DDL_z.npy` [444]; `embed/gene_vectors.npy` [444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 444 or target_col == 444). Every well: [[MFAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
