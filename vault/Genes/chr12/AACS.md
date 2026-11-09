---
symbol: "AACS"
type: "gene"
col: 1323
ensembl_id: "ENSG00000081760"
name: "acetoacetyl-CoA synthetase"
location: "12q24.31"
module: 25
arm: "-"
pooled_cpm: 39.09
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AACS

*acetoacetyl-CoA synthetase* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +20.7, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.654× (z -9.7, q 2e-19, down in 33 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (C32 0.0778×, BT-474 0.134×, HCT15 0.229×, SNU-1 0.212×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.187×, HCT15 0.248×, SNU-423 0.379×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.124×, LOX-IMVI 0.311×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKI]] (+0.55, fdr 1e-05), [[PDXK]] (+0.52, fdr 8e-05), [[RAB11FIP3]] (+0.49, fdr 5e-05); moves opposite to [[MRPL42]] (-0.51, fdr 3e-05), [[MRPL19]] (-0.47, fdr 4e-05), [[FAM98B]] (-0.47, fdr 5e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +20.7 | 0e+00 | 36/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +15.5 | 0e+00 | 47/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +14.6 | 1e-45 | 38/48 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +11.2 | 5e-27 | 40/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +9.5 | 3e-19 | 35/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 7e-16 | 28/47 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +7.8 | 6e-13 | 29/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +7.3 | 3e-11 | 24/48 (SW1417, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.2 | 5e-11 | 29/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.35×** | +6.9 | 3e-10 | 29/48 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.7 | 1e-09 | 26/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.4 | 9e-09 | 27/49 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 5e-08 | 24/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +5.4 | 2e-06 | 21/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.3 | 4e-06 | 24/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.13× | +4.0 | 0.002 | 17/48 (A549, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 8/47 (HCT15, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1323.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (C32 0.0778×, BT-474 0.134×, HCT15 0.229×, SNU-1 0.212×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.187×, HCT15 0.248×, SNU-423 0.379×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.124×, LOX-IMVI 0.311×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.654×** | -9.7 | 2e-19 | 33/47 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -8.3 | 2e-14 | 29/44 (C32, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.8 | 3e-04 | 18/39 (SHP-77, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.833×** | -4.0 | 0.009 | 16/46 (RKO, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | 0.904× | -3.3 | 0.12 | 9/48 (H4, PANC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.863× | -3.2 | 0.12 | 18/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.875× | -3.0 | 0.20 | 8/48 (H4, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.0) | — |
| [[NCI-H460 (line)]] | wt | 54.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 41.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 30.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 43.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.1) | — |
| [[A498 (line)]] | wt | 31.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +12.2) | — |
| [[A549 (line)]] | wt | 29.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.7) | — |
| [[C32 (line)]] | wt | 41.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0778× (z -19.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 38.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +13.8) | — |
| [[RKO (line)]] | wt | 53.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -14.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.0) | — |
| [[A-427 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.357× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 37.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.7) | — |
| [[J82 (line)]] | alt | 44.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 31.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 42.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -18.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.6) | — |
| [[A-172 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKI]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PDXK]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[RAB11FIP3]] | +0.49 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[PKD1]] | +0.47 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[TOB2]] | +0.47 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[BAIAP2]] | +0.47 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R13L]] | +0.46 | +0.33 / +0.40 | both halves | 1e-04 |  |
| [[NPHP3]] | +0.46 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[POLG]] | +0.46 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[PPP1R13B]] | +0.45 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[NPIPP1]] | +0.45 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CATSPERG]] | +0.44 | +0.50 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL42]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MRPL19]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FAM98B]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[RPP30]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[DYRK2]] | -0.44 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[APOO]] | -0.43 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[LEPROTL1]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[SMG7]] | -0.41 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[AAGAB]] | -0.41 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[SUMO1]] | -0.40 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[PAFAH1B2]] | -0.40 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[C5orf22]] | -0.40 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.349). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.6, -13.8); signed map (-24.1, 41.6). **Vector** length 81.3, 16.4% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +20.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.7 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | acetoacetyl-CoA synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:125,065,434-125,143,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12389, SUR-5, ACSF1 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Reactome | 3 pathways, smallest: Synthesis of Ketone Bodies; Ketone body metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V21](https://www.uniprot.org/uniprotkb/Q86V21) (Acetoacetyl-CoA synthetase):

> Converts acetoacetate to acetoacetyl-CoA in the cytosol (By similarity). Ketone body-utilizing enzyme, responsible for the synthesis of cholesterol and fatty acids (By similarity).

**Summary**, from NCBI Gene [65985](https://www.ncbi.nlm.nih.gov/gene/65985):

> Predicted to enable acetoacetate-CoA ligase activity. Predicted to be involved in positive regulation of insulin secretion. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21298) · Entrez [65985](https://www.ncbi.nlm.nih.gov/gene/65985) · UniProt [Q86V21](https://www.uniprot.org/uniprotkb/Q86V21) · Ensembl [ENSG00000081760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081760)

## Data

Gene col 1323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1323); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1323]; `tensor/DDL_lfc|DDL_z.npy` [1323]; `embed/gene_vectors.npy` [1323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1323 or target_col == 1323). Every well: [[AACS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AACS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
