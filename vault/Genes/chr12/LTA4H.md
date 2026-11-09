---
symbol: "LTA4H"
type: "gene"
col: 3195
ensembl_id: "ENSG00000111144"
name: "leukotriene A4 hydrolase"
location: "12q23.1"
module: 65
arm: "+"
pooled_cpm: 60.28
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# LTA4H

*leukotriene A4 hydrolase* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.58× (z +16.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.903× (z -6.1, q 6e-07, down in 5 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.735× (z -5.5, q 1e-05, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.286×, NCI-H23 0.485×, SNU-1 0.363×, HCT15 0.469×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.343×, NCI-H23 0.423×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H2347 0.423×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.120×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX7]] (+0.73, fdr 7e-06), [[BBS2]] (+0.72, fdr 7e-06), [[FIG4]] (+0.70, fdr 7e-06); moves opposite to [[SON]] (-0.65, fdr 1e-05), [[CDK11A]] (-0.64, fdr 1e-05), [[OPA3]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.58×** | +16.9 | 0e+00 | 47/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.49×** | +16.3 | 0e+00 | 46/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +12.5 | 1e-33 | 43/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +11.0 | 6e-26 | 40/48 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +9.7 | 4e-20 | 41/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.8 | 7e-13 | 30/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.8 | 7e-13 | 40/48 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 1e-07 | 37/49 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.9 | 2e-07 | 28/49 (MIA PaCa-2, A549, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 9e-07 | 32/48 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.6 | 1e-06 | 32/47 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 1e-06 | 28/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +5.2 | 8e-06 | 30/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.31×** | +4.6 | 2e-04 | 23/42 (C-33 A, LoVo, …) | two highest doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +4.5 | 2e-04 | 24/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.015 | 14/49 (HT-29, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.017 | 14/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.2 | 0.040 | 8/48 (hTERT-HPNE, A549, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.044 | 14/48 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3195.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.286×, NCI-H23 0.485×, SNU-1 0.363×, HCT15 0.469×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.343×, NCI-H23 0.423×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.258×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H2347 0.423×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H661 0.120×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -6.1 | 6e-07 | 5/49 (SW48, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -5.5 | 1e-05 | 26/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.848× | -4.2 | 0.006 | 18/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.831× | -3.3 | 0.14 | 11/48 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.838× | -3.2 | 0.18 | 14/47 (HepG2/C3A, A-172, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.838× | -3.0 | 0.20 | 15/49 (HEC-1-A, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.844× | -3.0 | 0.20 | 10/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 81.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 60.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 69.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 48.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 45.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.8) | — |
| [[LoVo (line)]] | wt | 68.1 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +11.5) | — |
| [[A-172 (line)]] | wt | 39.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 53.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.09× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 58.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 68.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.67× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 41.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 57.7 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +10.5) | — |
| [[A498 (line)]] | wt | 41.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.63× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 66.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.12× (z +8.9) | — |
| [[RKO (line)]] | wt | 71.8 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.30× (z +8.6) | — |
| [[A549 (line)]] | wt | 71.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.50× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 38.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 161 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.423× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.120× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[BBS2]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[FIG4]] | +0.70 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.69 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R2]] | +0.66 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ORC4]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.64 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[CAT]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MRS2]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ATP6V1B2]] | +0.63 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[IL17RD]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SON]] | -0.65 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[CDK11A]] | -0.64 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[OPA3]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[AGAP6]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ZC3H18]] | -0.63 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[SP2]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CDK11B]] | -0.62 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[AFG3L1P]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[DNAJB12]] | -0.62 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CRK]] | -0.60 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[RBBP6]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.0, -8.3); signed map (-32.9, -14.2). **Vector** length 113, 31.0% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.2 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +7.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.7 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +16.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.4 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.2 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -0.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | leukotriene A4 hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:96,000,753-96,043,520 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M1 metallopeptidases |
| Hallmark sets | COAGULATION, COMPLEMENT, MTORC1_SIGNALING |
| Reactome | 13 pathways, smallest: Biosynthesis of E-series 18(R)-resolvins; Biosynthesis of aspirin-triggered D-series resolvins; Biosynthesis of D-series resolvins |
| Matched by | ensembl_id |

**Function**, from UniProt [P09960](https://www.uniprot.org/uniprotkb/P09960) (Leukotriene A-4 hydrolase):

> Bifunctional zinc metalloenzyme that comprises both epoxide hydrolase (EH) and aminopeptidase activities. Acts as an epoxide hydrolase to catalyze the conversion of LTA4 to the pro-inflammatory mediator leukotriene B4 (LTB4). Can utilize LTA5 less effectively as a substrate than LTA4, and produce LTB5. Also has aminopeptidase activity, with high affinity for N-terminal arginines of various synthetic tripeptides. In addition to its pro-inflammatory EH activity, may also counteract inflammation …

**Summary**, from NCBI Gene [4048](https://www.ncbi.nlm.nih.gov/gene/4048):

> The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). Several transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:6710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6710) · Entrez [4048](https://www.ncbi.nlm.nih.gov/gene/4048) · UniProt [P09960](https://www.uniprot.org/uniprotkb/P09960) · Ensembl [ENSG00000111144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111144)

## Data

Gene col 3195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3195); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3195]; `tensor/DDL_lfc|DDL_z.npy` [3195]; `embed/gene_vectors.npy` [3195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3195 or target_col == 3195). Every well: [[LTA4H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTA4H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
