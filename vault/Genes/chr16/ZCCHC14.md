---
symbol: "ZCCHC14"
type: "gene"
col: 6468
ensembl_id: "ENSG00000140948"
name: "zinc finger CCHC-type containing 14"
location: "16q24.2"
module: 30
arm: "-"
pooled_cpm: 51.3
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ZCCHC14

*zinc finger CCHC-type containing 14* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.27× (z +21.8, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (C-33 A 0.189×, A-427 0.248×, NCI-H2030 0.411×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.221×, A-172 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.265×, A-427 0.276×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.307×, A-427 0.381×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.339×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASXL2]] (+0.49, fdr 1e-04), [[USP34]] (+0.49, fdr 5e-04), [[BPTF]] (+0.47, fdr 2e-04); moves opposite to [[RINT1]] (-0.54, fdr 4e-05), [[FRG1JP]] (-0.49, fdr 7e-04), [[DNAJC24]] (-0.49, fdr 2e-04).
> It sits in the **-** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.27×** | +21.8 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.72×** | +18.4 | 0e+00 | 46/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.68×** | +18.1 | 0e+00 | 46/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +17.5 | 0e+00 | 39/48 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +12.2 | 6e-32 | 37/48 (COLO 205, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.9 | 6e-21 | 36/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +9.5 | 1e-19 | 39/48 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +7.7 | 1e-12 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +7.1 | 6e-11 | 30/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.8 | 7e-10 | 28/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +6.5 | 6e-09 | 39/48 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-06 | 29/49 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 27/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.4 | 4e-04 | 21/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.3 | 5e-04 | 22/47 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.003 | 21/48 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6468.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (C-33 A 0.189×, A-427 0.248×, NCI-H2030 0.411×); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.221×, A-172 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.265×, A-427 0.276×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.307×, A-427 0.381×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.339×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.818× | -3.7 | 0.10 | 23/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.832× | -3.4 | 0.17 | 21/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.1 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +21.2) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 38.2 | 3 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +11.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 91.0 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 65.6 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +19.0) | — |
| [[COLO 205 (line)]] | alt | 43.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +17.7) | — |
| [[NCI-H460 (line)]] | wt | 28.3 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 4.85× (z +17.2) | — |
| [[A-427 (line)]] | wt | 41.7 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.44× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.248× (z -13.7) |
| [[A498 (line)]] | wt | 43.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +16.8) | — |
| [[C32 (line)]] | wt | 56.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.4) | — |
| [[HOP62 (line)]] | alt | 51.0 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +19.0) | — |
| [[NCI-H2030 (line)]] | alt | 80.2 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +11.0) | [[Harringtonine (drug)]] 5 µM 0.307× (z -12.4) |
| [[HT-29 (line)]] | alt | 55.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +11.0) | — |
| [[LoVo (line)]] | wt | 60.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 47.8 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 58.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +17.6) | — |
| [[A549 (line)]] | wt | 26.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 42.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.8) | — |
| [[J82 (line)]] | alt | 47.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 55.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.41× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 51.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.6) | [[Lonafarnib (drug)]] 5 µM 0.0581× (z -11.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 29.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 42.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.3) | — |
| [[H4 (line)]] | wt | 44.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.22× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 58.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 28.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 71.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 65.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.189× (z -13.9) |
| [[SW1417 (line)]] | alt | 68.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 57.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 111 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +9.6) | — |
| [[RKO (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.5) | — |
| [[SW48 (line)]] | wt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASXL2]] | +0.49 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[USP34]] | +0.49 | +0.23 / +0.41 | both halves | 5e-04 |  |
| [[BPTF]] | +0.47 | +0.64 / +0.30 | both halves | 2e-04 |  |
| [[WWC3]] | +0.47 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[NFIB]] | +0.47 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[IRS1]] | +0.46 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[FOXP1]] | +0.45 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[HNRNPF]] | +0.45 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[HIVEP2]] | +0.45 | +0.48 / +0.25 | both halves | 4e-04 |  |
| [[CPNE1]] | +0.44 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[WNK1]] | +0.43 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[HIVEP1]] | +0.43 | +0.52 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RINT1]] | -0.54 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[FRG1JP]] | -0.49 | -0.20 / -0.54 | both halves | 7e-04 |  |
| [[DNAJC24]] | -0.49 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[MKRN2]] | -0.48 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[ZNF708]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MIR29B2CHG]] | -0.47 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[NDUFAF7]] | -0.47 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[CDC23]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CERS5]] | -0.44 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[SCAI]] | -0.44 | -0.56 / -0.25 | both halves | 4e-04 |  |
| [[SCNM1]] | -0.44 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[ZFPL1]] | -0.44 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.361). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.6, 3.3); signed map (8.2, -10.8). **Vector** length 85.7, 21.1% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,406,246-87,493,024 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BDG29, MGC14139 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q8WYQ9](https://www.uniprot.org/uniprotkb/Q8WYQ9) carries no function annotation.

**Summary**, from NCBI Gene [23174](https://www.ncbi.nlm.nih.gov/gene/23174):

> Predicted to enable nucleic acid binding activity; phosphatidylinositol binding activity; and zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24134) · Entrez [23174](https://www.ncbi.nlm.nih.gov/gene/23174) · UniProt [Q8WYQ9](https://www.uniprot.org/uniprotkb/Q8WYQ9) · Ensembl [ENSG00000140948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140948)

## Data

Gene col 6468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6468); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6468]; `tensor/DDL_lfc|DDL_z.npy` [6468]; `embed/gene_vectors.npy` [6468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6468 or target_col == 6468). Every well: [[ZCCHC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
