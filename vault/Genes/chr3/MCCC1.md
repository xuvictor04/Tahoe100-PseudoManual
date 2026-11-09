---
symbol: "MCCC1"
type: "gene"
col: 1206
ensembl_id: "ENSG00000078070"
name: "methylcrotonyl-CoA carboxylase subunit 1"
location: "3q27.1"
module: 122
arm: "+"
pooled_cpm: 47.75
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# MCCC1

*methylcrotonyl-CoA carboxylase subunit 1* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +18.0, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.739× (z -8.7, q 1e-15, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPALPP1]] (+0.70, fdr 7e-06), [[TSC1]] (+0.64, fdr 1e-05), [[PPP1R3E]] (+0.64, fdr 1e-05); moves opposite to [[EHD4]] (-0.55, fdr 1e-05), [[GALNT10]] (-0.55, fdr 1e-04), [[GFOD1]] (-0.52, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TIAM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +18.0 | 0e+00 | 41/46 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +13.1 | 7e-37 | 40/47 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +9.5 | 3e-19 | 31/47 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +9.0 | 5e-17 | 33/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.4 | 1e-11 | 25/47 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +6.7 | 2e-09 | 28/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.0 | 1e-07 | 26/46 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.8 | 5e-07 | 21/47 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.8 | 5e-07 | 25/48 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 2e-05 | 23/46 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.18× | +4.8 | 1e-04 | 19/47 (NCI-H2347, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.6 | 2e-04 | 20/48 (BT-474, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.53×** | +4.5 | 3e-04 | 16/46 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.25×** | +4.5 | 3e-04 | 22/47 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.4 | 4e-04 | 23/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.009 | 18/47 (NCI-H1573, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.4 | 0.018 | 13/47 (HOP62, H4, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.022 | 14/46 (SW480, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.739×** | -8.7 | 1e-15 | 40/47 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.752×** | -5.8 | 2e-06 | 23/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.770×** | -5.3 | 2e-05 | 24/47 (C32, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.766×** | -5.2 | 2e-05 | 20/40 (SNU-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.817×** | -4.1 | 0.004 | 19/44 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.762×** | -4.0 | 0.007 | 17/47 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.019 | 17/47 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.837× | -3.6 | 0.019 | 11/47 (HT-29, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.826×** | -3.6 | 0.019 | 18/46 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.842× | -3.5 | 0.024 | 13/47 (NCI-H1573, HCT15, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.854× | -3.2 | 0.065 | 13/47 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.859× | -3.1 | 0.091 | 11/48 (NCI-H2347, H4, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.901× | -3.0 | 0.11 | 7/47 (NCI-H23, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 61.0 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 58.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +15.9) | — |
| [[HS-578T (line)]] | alt | 41.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +16.1) | — |
| [[HT-29 (line)]] | alt | 56.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.4) | — |
| [[A-172 (line)]] | wt | 49.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +19.0) | — |
| [[A498 (line)]] | wt | 30.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.5) | — |
| [[J82 (line)]] | alt | 51.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +20.6) | — |
| [[KATO III (line)]] | alt | 77.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.4) | — |
| [[LoVo (line)]] | wt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 52.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[PANC-1 (line)]] | alt | 41.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.8) | — |
| [[RKO (line)]] | wt | 46.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 73.1 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.225× (z -12.0) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0709× (z -10.4) |
| [[C32 (line)]] | wt | 65.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 52.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.122× (z -10.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[H4 (line)]] | wt | 65.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 45.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 43.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 69.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SNU-423 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SW 900 (line)]] | alt | 58.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 54.6 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.541× (z -9.0) |
| [[SW480 (line)]] | alt | 64.4 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.563× (z -10.4) |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPALPP1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TSC1]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R3E]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[HEXA]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[TRPM7]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[WASHC2C]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MYL6B]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[HPS4]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TMEM192]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[LRRC37B]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ARFGEF2]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[RRAGB]] | +0.56 | +0.63 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.55 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[GALNT10]] | -0.55 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[GFOD1]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[GPRIN1]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ELOVL1]] | -0.52 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TAF1B]] | -0.51 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CDYL2]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 | STRING 410 |
| [[POLR3B]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[VANGL1]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TUBG1]] | -0.49 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[TIAM1]] | -0.49 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ATP8B5P-1]] | -0.49 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIAM1]] | B | TIAM1 activity raises MCCC1's level | lines that do not express TIAM1 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without TIAM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: RASSF2, SPATC1L, DNAH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.9, 15.3); signed map (-1.1, -4.7). **Vector** length 107, 27.4% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.8 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +18.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.4 | +4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.9 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | methylcrotonyl-CoA carboxylase subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,015,218-183,116,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCCA, MCCCα |
| Gene groups (HGNC) | Methylcrotonyl-CoA carboxylase subunits; ATP-grasp fold containing |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 10 pathways, smallest: Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism; Biotin transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RQ3](https://www.uniprot.org/uniprotkb/Q96RQ3) (Methylcrotonoyl-CoA carboxylase subunit alpha, mitochondrial):

> Biotin-attachment subunit of the 3-methylcrotonyl-CoA carboxylase, an enzyme that catalyzes the conversion of 3-methylcrotonyl-CoA to 3-methylglutaconyl-CoA, a critical step for leucine and isovaleric acid catabolism.

**Summary**, from NCBI Gene [56922](https://www.ncbi.nlm.nih.gov/gene/56922):

> This gene encodes the large subunit of 3-methylcrotonyl-CoA carboxylase. This enzyme functions as a heterodimer and catalyzes the carboxylation of 3-methylcrotonyl-CoA to form 3-methylglutaconyl-CoA. Mutations in this gene are associated with 3-Methylcrotonylglycinuria, an autosomal recessive disorder of leucine catabolism. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6936) · Entrez [56922](https://www.ncbi.nlm.nih.gov/gene/56922) · UniProt [Q96RQ3](https://www.uniprot.org/uniprotkb/Q96RQ3) · Ensembl [ENSG00000078070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078070)

## Data

Gene col 1206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1206); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1206]; `tensor/DDL_lfc|DDL_z.npy` [1206]; `embed/gene_vectors.npy` [1206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1206 or target_col == 1206). Every well: [[MCCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
