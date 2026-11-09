---
symbol: "HTATSF1"
type: "gene"
col: 2230
ensembl_id: "ENSG00000102241"
name: "HIV-1 Tat specific factor 1"
location: "Xq26.3"
module: 25
arm: "+"
pooled_cpm: 49.39
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# HTATSF1

*HIV-1 Tat specific factor 1* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.36× (z +20.6, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.32× (z +3.8, q 0.007, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 5.24×, SNU-423 7.54×, NCI-H460 4.82×, HOP62 6.58×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 5.57×, NCI-H23 5.69×, NCI-H460 5.00×, SNU-423 7.03×, …; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.384×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (CHP-212 0.102×; ⚠ transcription drop); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0922×; ⚠ transcription drop; unreliable plate only); [[Verteporfin (drug)]] 5 µM in 1 line (SNU-423 0.328×); [[Decitabine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.175×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSX2IP]] (+0.63, fdr 1e-05), [[SSRP1]] (+0.61, fdr 1e-05), [[HNRNPR]] (+0.60, fdr 1e-05); moves opposite to [[ELL]] (-0.54, fdr 1e-05), [[TRNAU1AP]] (-0.54, fdr 4e-05), [[COPS9]] (-0.53, fdr 9e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2230.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 5.24×, SNU-423 7.54×, NCI-H460 4.82×, HOP62 6.58×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 5.57×, NCI-H23 5.69×, NCI-H460 5.00×, SNU-423 7.03×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.36×** | +20.6 | 0e+00 | 47/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +19.5 | 0e+00 | 42/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +14.4 | 2e-44 | 44/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.89×** | +8.9 | 8e-17 | 42/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.84×** | +8.5 | 2e-15 | 45/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.82×** | +8.4 | 5e-15 | 43/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +7.6 | 2e-12 | 40/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.61×** | +6.4 | 1e-08 | 36/47 (SNU-423, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.47×** | +5.4 | 5e-06 | 37/47 (Hs 766T, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.24×** | +4.0 | 0.004 | 29/48 (PANC-1, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.007 | 23/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +3.8 | 0.008 | 26/48 (J82, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.068 | 20/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.25×** | +3.1 | 0.068 | 19/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +3.0 | 0.090 | 19/48 (HOP62, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2230.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.384×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (CHP-212 0.102×; ⚠ transcription drop); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0922×; ⚠ transcription drop; unreliable plate only); [[Verteporfin (drug)]] 5 µM in 1 line (SNU-423 0.328×); [[Decitabine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.175×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.785× | -3.4 | 0.21 | 18/48 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.833× | -3.4 | 0.21 | 18/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.793× | -3.3 | 0.21 | 17/48 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.806× | -3.0 | 0.35 | 21/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 50.3 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 50.2 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +17.0) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.328× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 47.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +16.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 40.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +15.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 42.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.43× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 36.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 52.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +13.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 45.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +14.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 53.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 36.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +14.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.98× (z +13.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 96.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +18.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 64.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 20.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 91.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +10.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 51.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +12.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 68.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +15.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 92.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.69× (z +16.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 44.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 75.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +15.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 73.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +13.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.102× (z -9.6) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.175× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +10.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0922× (z -9.4) ⚠ transcription drop; unreliable plate only |
| [[SW 900 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SSRP1]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[HNRNPR]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PDHA1]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SMARCA5]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[LRRCC1]] | +0.56 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[NONO]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 | same gene group |
| [[IPO8]] | +0.55 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SYNJ2BP]] | +0.54 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[DLD]] | +0.54 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[DCTN1]] | +0.54 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PHF6]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELL]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | -0.54 | -0.41 / -0.49 | both halves | 4e-05 | same gene group |
| [[COPS9]] | -0.53 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[SPDYE5]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SMIM27]] | -0.53 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[DNLZ]] | -0.52 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[URM1]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[FAU]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CCDC142]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[HMGCL]] | -0.50 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[NAA60]] | -0.50 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[SPATC1]] | -0.49 | -0.12 / -0.45 | ⚠ not reproduced | 0.002 |  |
| [[SIRT6]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.9, -36.1); signed map (-18.4, -45.4). **Vector** length 65.7, 13.9% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +20.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.1 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +1.9 | +8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +19.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.6 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +0.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.0 | +0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.7 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | HIV-1 Tat specific factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:136,497,079-136,512,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAT-SF1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O43719](https://www.uniprot.org/uniprotkb/O43719) (17S U2 SnRNP complex component HTATSF1):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, HTATSF1 is required to stabilize the …

**Summary**, from NCBI Gene [27336](https://www.ncbi.nlm.nih.gov/gene/27336):

> The protein encoded by this gene functions as a cofactor for the stimulation of transcriptional elongation by HIV-1 Tat, which binds to the HIV-1 promoter through Tat-TAR interaction. This protein may also serve as a dual-function factor to couple transcription and splicing and to facilitate their reciprocal activation. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:5276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5276) · Entrez [27336](https://www.ncbi.nlm.nih.gov/gene/27336) · UniProt [O43719](https://www.uniprot.org/uniprotkb/O43719) · Ensembl [ENSG00000102241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102241)

## Data

Gene col 2230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2230); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2230]; `tensor/DDL_lfc|DDL_z.npy` [2230]; `embed/gene_vectors.npy` [2230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2230 or target_col == 2230). Every well: [[HTATSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTATSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
