---
symbol: "UCHL3"
type: "gene"
col: 4027
ensembl_id: "ENSG00000118939"
name: "ubiquitin C-terminal hydrolase L3"
location: "13q22.2"
module: 184
arm: "+"
pooled_cpm: 61.97
n_lines_expressing: 49
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# UCHL3

*ubiquitin C-terminal hydrolase L3* — 13q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +21.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.834× (z -5.3, q 7e-05, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.837× (z -3.9, q 0.031, down in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.426×, NCI-H1573 0.412×, HepG2/C3A 0.394×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.361×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (HOP62 0.443×; ⚠ cell-cycle shift, explains ~19% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP29]] (+0.61, fdr 1e-05), [[EHD4]] (+0.61, fdr 3e-05), [[S100A16]] (+0.59, fdr 5e-05); moves opposite to [[JADE2]] (-0.61, fdr 2e-05), [[RPRD2]] (-0.59, fdr 2e-05), [[XPO1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[S100A16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +21.0 | 0e+00 | 46/47 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +19.1 | 0e+00 | 46/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +18.7 | 0e+00 | 46/47 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +12.3 | 1e-32 | 43/47 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +9.6 | 1e-19 | 36/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +8.8 | 1e-16 | 34/46 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +8.6 | 5e-16 | 36/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +7.7 | 1e-12 | 27/46 (RKO, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +7.5 | 6e-12 | 32/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 9e-11 | 31/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.8 | 6e-10 | 28/46 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +6.5 | 3e-09 | 24/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.5 | 5e-09 | 28/47 (C32, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +6.0 | 7e-08 | 25/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +6.0 | 9e-08 | 23/47 (SNU-1, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +5.7 | 5e-07 | 28/48 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 8e-06 | 24/46 (HT-29, RKO, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 1e-05 | 22/47 (HT-29, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 5e-05 | 21/47 (HT-29, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.426×, NCI-H1573 0.412×, HepG2/C3A 0.394×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.361×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (HOP62 0.443×; ⚠ cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.834× | -5.3 | 7e-05 | 22/47 (HOP62, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.837× | -3.9 | 0.031 | 14/47 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.7 | 0.039 | 10/47 (A498, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.850× | -3.5 | 0.048 | 18/47 (A498, J82, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.956× | -3.5 | 0.048 | 3/49 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.072 | 15/46 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.858× | -3.3 | 0.072 | 13/47 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.866× | -3.1 | 0.11 | 11/47 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.867× | -3.1 | 0.11 | 8/47 (H4, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.867× | -3.1 | 0.11 | 12/48 (RKO, HS-578T, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.12 | 11/48 (BT-474, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.890× | -3.0 | 0.12 | 13/47 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 50.2 | 14 (8 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.48× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 43.1 | 8 (4 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.42× (z +11.7) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.24× (z +9.6) | [[Selinexor (drug)]] 5 µM 0.443× (z -8.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[C32 (line)]] | wt | 33.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 120 | 4 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.72× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 24.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +12.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.13× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 35.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 40.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +12.1) | — |
| [[SW480 (line)]] | alt | 197 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 25.4 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.78× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 69.3 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 68.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 58.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 44.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +9.2) | — |
| [[J82 (line)]] | alt | 70.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +11.2) | — |
| [[LoVo (line)]] | wt | 57.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 58.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 67.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 31.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 73.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 50.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 138 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +11.8) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.80× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 58.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +10.1) | — |
| [[A-427 (line)]] | wt | 27.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.8) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[COLO 205 (line)]] | alt | 165 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +12.2) | — |
| [[NCI-H460 (line)]] | wt | 45.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +8.5) | — |
| [[RKO (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW48 (line)]] | wt | 99.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A498 (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP29]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[EHD4]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[S100A16]] | +0.59 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[HMOX2]] | +0.59 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[CAPN2]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[GPAT3]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.57 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[LRRFIP1]] | +0.57 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[RTN4]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.56 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[C3orf52]] | +0.56 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[CORO2B]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JADE2]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[RPRD2]] | -0.59 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[XPO1]] | -0.55 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[KDM3B]] | -0.55 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[HMGN2]] | -0.55 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[EIF1B-AS1]] | -0.54 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CREB3L4]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SAFB]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[BRD8]] | -0.52 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[HMGB2]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[HDGF]] | -0.51 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[NUCKS1]] | -0.51 | -0.43 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | S100A16 activity raises UCHL3's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without S100A16 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[FAM241A]] | B | FAM241A activity raises UCHL3's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without FAM241A | 0.070 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |
| [[B9D2]] | C | B9D2's natural level weakens UCHL3's drug response | B9D2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.10; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (15.7, 4.6); signed map (-2.7, 46.6). **Vector** length 102, 27.3% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.2 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +12.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +19.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.8 | +7.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +5.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.3 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.8 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.3 | +1.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin C-terminal hydrolase L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.2 — chr13:75,549,483-75,606,020 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin C-terminal hydrolases |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; UCH proteinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P15374](https://www.uniprot.org/uniprotkb/P15374) (Ubiquitin carboxyl-terminal hydrolase isozyme L3):

> Deubiquitinating enzyme (DUB) that controls levels of cellular ubiquitin through processing of ubiquitin precursors and ubiquitinated proteins. Thiol protease that recognizes and hydrolyzes a peptide bond at the C-terminal glycine of either ubiquitin or NEDD8. Has a 10-fold preference for Arg and Lys at position P3'', and exhibits a preference towards 'Lys-48'-linked ubiquitin chains. Can hydrolyze UBB(+1), a mutated form of ubiquitin which is not effectively degraded by the proteasome and is …

**Summary**, from NCBI Gene [7347](https://www.ncbi.nlm.nih.gov/gene/7347):

> The protein encoded by this gene is a member of the deubiquitinating enzyme family. Members of this family are proteases that catalyze the removal of ubiquitin from polypeptides and are divided into five classes, depending on the mechanism of catalysis. This protein may hydrolyze the ubiquitinyl-N-epsilon amide bond of ubiquitinated proteins to regenerate ubiquitin for another catalytic cycle. Alternative splicing results in multiple transcript variants that encode different protein isoforms. …

**Accessions** — [HGNC:12515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12515) · Entrez [7347](https://www.ncbi.nlm.nih.gov/gene/7347) · UniProt [P15374](https://www.uniprot.org/uniprotkb/P15374) · Ensembl [ENSG00000118939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118939)

## Data

Gene col 4027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4027); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4027]; `tensor/DDL_lfc|DDL_z.npy` [4027]; `embed/gene_vectors.npy` [4027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4027 or target_col == 4027). Every well: [[UCHL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCHL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
