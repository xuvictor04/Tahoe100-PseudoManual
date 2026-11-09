---
symbol: "TLE5"
type: "gene"
col: 2531
ensembl_id: "ENSG00000104964"
name: "TLE family member 5, transcriptional modulator"
location: "19p13.3"
module: 50
arm: "+"
pooled_cpm: 41.09
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# TLE5

*TLE family member 5, transcriptional modulator* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.87× (z +17.3, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1573 9.07×, PANC-1 5.31×, HOP62 5.60×, A498 4.59×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 5.79×, PANC-1 4.67×, LoVo 5.68×, A-427 4.65×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.376× (z -17.7, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC10]] (+0.69, fdr 1e-05), [[LAMB2]] (+0.64, fdr 7e-06), [[SELENON]] (+0.64, fdr 3e-05); moves opposite to [[DNTTIP2]] (-0.60, fdr 2e-05), [[NIFK]] (-0.56, fdr 2e-05), [[MRPL46]] (-0.55, fdr 7e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2531.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H1573 9.07×, PANC-1 5.31×, HOP62 5.60×, A498 4.59×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 5.79×, PANC-1 4.67×, LoVo 5.68×, A-427 4.65×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.87×** | +17.3 | 0e+00 | 47/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +14.7 | 0e+00 | 39/39 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +11.9 | 1e-30 | 42/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +6.4 | 2e-08 | 41/47 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.2 | 2e-05 | 3/49 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.19 | 18/48 (SHP-77, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.26× | +3.0 | 0.21 | 21/47 (NCI-H460, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.376×** | -17.7 | 0e+00 | 46/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.375×** | -12.5 | 1e-33 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.398×** | -11.8 | 1e-29 | 45/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.407×** | -11.5 | 2e-28 | 45/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.424×** | -10.9 | 8e-26 | 43/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.531×** | -8.1 | 6e-14 | 43/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.555×** | -7.2 | 4e-11 | 40/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -6.1 | 6e-08 | 29/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.593×** | -6.1 | 8e-08 | 39/48 (A549, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -5.9 | 2e-07 | 36/48 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.466×** | -4.8 | 9e-05 | 36/48 (Panc 03.27, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.717×** | -4.2 | 0.001 | 25/48 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -4.1 | 0.002 | 26/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.534×** | -3.9 | 0.004 | 24/43 (Hs 766T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -3.8 | 0.006 | 22/48 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.575×** | -3.5 | 0.017 | 27/48 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.776×** | -3.1 | 0.055 | 19/48 (BT-474, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 56.8 | 2 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.3) |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.3) |
| [[LoVo (line)]] | wt | 33.9 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 5.68× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.238× (z -11.0) |
| [[A-172 (line)]] | wt | 113 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 46.1 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 35.8 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 9.07× (z +16.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 26.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -14.9) |
| [[SW480 (line)]] | alt | 39.1 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.225× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 50.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.1) |
| [[A-427 (line)]] | wt | 58.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.0) |
| [[A549 (line)]] | wt | 27.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 57.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -8.9) |
| [[HOP62 (line)]] | alt | 33.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.0) |
| [[J82 (line)]] | alt | 45.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.7) |
| [[LS 180 (line)]] | wt | 49.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 52.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.2) |
| [[PANC-1 (line)]] | alt | 36.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.5) |
| [[RKO (line)]] | wt | 42.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0589× (z -20.2) |
| [[RPMI-7951 (line)]] | alt | 33.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.4) |
| [[A498 (line)]] | wt | 34.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +13.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 41.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.7) |
| [[Hs 766T (line)]] | wt | 55.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 45.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.2) |
| [[KATO III (line)]] | alt | 38.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 23.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 40.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.237× (z -9.0) |
| [[SNU-1 (line)]] | wt | 58.1 | 0 | 3 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.303× (z -10.9) |
| [[SNU-423 (line)]] | alt | 29.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.1) |
| [[SW 900 (line)]] | alt | 41.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.9) |
| [[BT-474 (line)]] | alt | 33.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 32.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.8) |
| [[HS-578T (line)]] | alt | 29.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.4) |
| [[HT-29 (line)]] | alt | 33.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 58.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -12.5) |
| [[C-33 A (line)]] | alt | 38.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -8.5) |
| [[HCT15 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.9) |
| [[AN3 CA (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC10]] | +0.69 | +0.52 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[LAMB2]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SELENON]] | +0.64 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[CLSTN1]] | +0.60 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[LENG8]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GANAB]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.59 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[GRK2]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[USF2]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PTMS]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PRKCSH]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNTTIP2]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[NIFK]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MRPL46]] | -0.55 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[PWP2]] | -0.55 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[GEMIN6]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CEBPZ]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[FADD]] | -0.52 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[MRPL2]] | -0.51 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[NSRP1]] | -0.51 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[C1orf131]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[CEP290]] | -0.49 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, -48.2); signed map (-25.9, -36.6). **Vector** length 65.2, 16.3% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +17.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | TLE family member 5, transcriptional modulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,052,910-3,063,107 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRG5; previously AES |
| Gene groups (HGNC) | TLE family |
| Reactome | 3 pathways, smallest: Repression of WNT target genes; Degradation of beta-catenin by the destruction complex; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08117](https://www.uniprot.org/uniprotkb/Q08117) (TLE family member 5):

> Transcriptional corepressor. Acts as a dominant repressor towards other family members. Inhibits NF-kappa-B-regulated gene expression. May be required for the initiation and maintenance of the differentiated state. Essential for the transcriptional repressor activity of SIX3 during retina and lens development.

**Summary**, from NCBI Gene [166](https://www.ncbi.nlm.nih.gov/gene/166):

> The protein encoded by this gene is similar in sequence to the amino terminus of Drosophila enhancer of split groucho, a protein involved in neurogenesis during embryonic development. The encoded protein, which belongs to the groucho/TLE family of proteins, can function as a homooligomer or as a heteroologimer with other family members to dominantly repress the expression of other family member genes. Three transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:307) · Entrez [166](https://www.ncbi.nlm.nih.gov/gene/166) · UniProt [Q08117](https://www.uniprot.org/uniprotkb/Q08117) · Ensembl [ENSG00000104964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104964)

## Data

Gene col 2531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2531); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2531]; `tensor/DDL_lfc|DDL_z.npy` [2531]; `embed/gene_vectors.npy` [2531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2531 or target_col == 2531). Every well: [[TLE5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLE5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
