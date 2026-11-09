---
symbol: "ALG2"
type: "gene"
col: 4076
ensembl_id: "ENSG00000119523"
name: "ALG2 alpha-1,3/1,6-mannosyltransferase"
location: "9q22.33"
module: 12
arm: "+"
pooled_cpm: 26.94
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ALG2

*ALG2 alpha-1,3/1,6-mannosyltransferase* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.69× (z +23.7, q 0e+00, up in 48 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.64× (z +6.5, q 1e-08, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.643× (z -5.4, q 3e-05, down in 24 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Berberine (chloride hydrate) (drug)]] 5 µM: 0.825× (z -3.6, q 0.039, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 0.0657×, RPMI-7951 0.0748×, NCI-H1792 0.101×, SW 900 0.140×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.147×, H4 0.108×, HT-29 0.134×, NCI-H460 0.219×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.0552×, MIA PaCa-2 0.215×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.05 µM in 1 line (SHP-77 0.129×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FICD]] (+0.77, fdr 7e-06), [[SELENOS]] (+0.68, fdr 7e-06), [[SEC61B]] (+0.67, fdr 7e-06, ⚠ same locus), [[NRBF2]] (+0.67, fdr 2e-05); moves opposite to [[YWHAQ]] (-0.71, fdr 7e-06), [[RBBP7]] (-0.67, fdr 7e-06), [[MAPK9]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.69×** | +23.7 | 0e+00 | 48/48 (A498, J82, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +8.2 | 8e-14 | 40/46 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.65×** | +6.6 | 1e-08 | 39/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +6.5 | 1e-08 | 35/48 (SNU-423, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +6.0 | 2e-07 | 30/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +6.0 | 2e-07 | 34/48 (C-33 A, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 3e-07 | 29/46 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +5.8 | 5e-07 | 29/48 (SNU-423, A-172, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.7 | 6e-07 | 29/47 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +5.5 | 2e-06 | 29/45 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 3e-06 | 30/48 (NCI-H460, RKO, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +5.0 | 3e-05 | 28/48 (NCI-H2347, HOP62, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +4.6 | 2e-04 | 25/47 (HOP62, COLO 205, …) | two highest doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.91×** | +4.4 | 4e-04 | 26/47 (HOP62, A498, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.23×** | +3.8 | 0.005 | 21/47 (HOP62, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.020 | 14/46 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4076.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (KATO III 0.0657×, RPMI-7951 0.0748×, NCI-H1792 0.101×, SW 900 0.140×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.147×, H4 0.108×, HT-29 0.134×, NCI-H460 0.219×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.0552×, MIA PaCa-2 0.215×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.05 µM in 1 line (SHP-77 0.129×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -5.4 | 3e-05 | 24/42 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.675×** | -4.8 | 4e-04 | 24/36 (KATO III, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.825×** | -3.6 | 0.039 | 17/48 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.039 | 18/47 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -3.6 | 0.039 | 20/45 (SNU-423, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.789× | -3.0 | 0.22 | 16/33 (KATO III, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 51.5 | 1 (1 ⚠) | 3 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +13.3) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.05 µM 0.0552× (z -18.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 37.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +10.7) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.28× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.2 | 3 (3 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +13.5) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 24.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +11.6) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +15.2) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.321× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +19.0) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 24.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +12.6) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 36.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +12.1) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +10.9) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 21.1 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.75× (z +13.4) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.80× (z +15.2) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 37.6 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +11.6) ⚠ position not correctable | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +12.2) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -16.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 19.6 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +10.1) ⚠ position not correctable | [[Saquinavir (drug)]] 0.05 µM 0.129× (z -11.9) |
| [[SW 900 (line)]] | alt | 28.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +10.6) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.140× (z -12.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +14.5) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +9.2) ⚠ position not correctable | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.76× (z +12.9) ⚠ position not correctable | — |
| [[BT-474 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.79× (z +9.6) ⚠ position not correctable | — |
| [[C32 (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +9.5) ⚠ position not correctable | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +10.2) ⚠ position not correctable | — |
| [[COLO 205 (line)]] | alt | 37.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +10.4) ⚠ position not correctable | — |
| [[HCT15 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +9.8) ⚠ position not correctable | — |
| [[HEC-1-A (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +13.4) ⚠ position not correctable | — |
| [[Hs 766T (line)]] | wt | 38.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.80× (z +14.2) ⚠ position not correctable | — |
| [[HS-578T (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.75× (z +14.1) ⚠ position not correctable | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.65× (z +10.0) ⚠ position not correctable | — |
| [[J82 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +16.0) ⚠ position not correctable | — |
| [[LoVo (line)]] | wt | 37.1 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +14.4) ⚠ position not correctable | — |
| [[LOX-IMVI (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +11.4) ⚠ position not correctable | — |
| [[LS 180 (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.68× (z +12.8) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +8.6) ⚠ position not correctable | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +9.5) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +11.4) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +13.0) ⚠ position not correctable | — |
| [[PANC-1 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +13.0) ⚠ position not correctable | — |
| [[SNU-423 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.65× (z +10.8) ⚠ position not correctable | — |
| [[SW1417 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.67× (z +13.3) ⚠ position not correctable | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FICD]] | +0.77 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[SELENOS]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[NRBF2]] | +0.67 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[YIF1A]] | +0.67 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[SRP19]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ZCCHC9]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ZNF766]] | +0.64 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ADPRS]] | +0.64 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SSR2]] | +0.63 | +0.37 / +0.77 | both halves | 8e-05 |  |
| [[HM13]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[C14orf119]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAQ]] | -0.71 | -0.67 / -0.72 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.67 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[DHFR]] | -0.62 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[MRE11]] | -0.60 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[APP]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[GNG12]] | -0.60 | -0.40 / -0.69 | both halves | 5e-05 |  |
| [[CRTAP]] | -0.59 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[NONO]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ACTR3]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[PFKM]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.1, -11.3); signed map (-10.4, -7.7). **Vector** length 100, 25.6% of its response variance represented; |z| ≥ 3 in 709 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ALG2 alpha-1,3/1,6-mannosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:99,216,425-99,221,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDGIi, FLJ14511, hALPG2, NET38, CDG1I |
| Gene groups (HGNC) | Glycosyl transferases group 1 domain containing |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H553](https://www.uniprot.org/uniprotkb/Q9H553) (Alpha-1,3/1,6-mannosyltransferase ALG2):

> Mannosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two GlcNAcs, nine mannoses and three …

**Summary**, from NCBI Gene [85365](https://www.ncbi.nlm.nih.gov/gene/85365):

> This gene encodes a member of the glycosyltransferase 1 family. The encoded protein acts as an alpha 1,3 mannosyltransferase, mannosylating Man(2)GlcNAc(2)-dolichol diphosphate and Man(1)GlcNAc(2)-dolichol diphosphate to form Man(3)GlcNAc(2)-dolichol diphosphate. Defects in this gene have been associated with congenital disorder of glycosylation type Ih (CDG-Ii). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:23159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23159) · Entrez [85365](https://www.ncbi.nlm.nih.gov/gene/85365) · UniProt [Q9H553](https://www.uniprot.org/uniprotkb/Q9H553) · Ensembl [ENSG00000119523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119523)

## Data

Gene col 4076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4076); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4076]; `tensor/DDL_lfc|DDL_z.npy` [4076]; `embed/gene_vectors.npy` [4076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4076 or target_col == 4076). Every well: [[ALG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
