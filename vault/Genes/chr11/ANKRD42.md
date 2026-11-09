---
symbol: "ANKRD42"
type: "gene"
col: 6022
ensembl_id: "ENSG00000137494"
name: "ankyrin repeat domain 42"
location: "11q14.1"
module: 205
arm: "+"
pooled_cpm: 24.41
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# ANKRD42

*ankyrin repeat domain 42* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.73× (z +24.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.636× (z -8.6, q 6e-15, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (SW48 0.0813×); [[Furosemide (drug)]] 0.5 µM in 1 line (H4 0.125×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM174A]] (+0.69, fdr 1e-05), [[ZNF487]] (+0.66, fdr 1e-05), [[CFAP69]] (+0.66, fdr 7e-06); moves opposite to [[POGK]] (-0.56, fdr 2e-05), [[TMEM185B]] (-0.50, fdr 4e-05), [[UBE2D4]] (-0.49, fdr 9e-05).
> It is in [[Module 205]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +24.8 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +18.8 | 0e+00 | 47/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.24×** | +15.7 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.06×** | +14.9 | 0e+00 | 47/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.92×** | +14.3 | 4e-44 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +14.1 | 5e-43 | 45/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.41×** | +11.7 | 7e-30 | 46/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.23×** | +10.7 | 1e-24 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.17×** | +9.9 | 2e-21 | 38/47 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.02×** | +9.4 | 4e-19 | 42/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +9.1 | 4e-18 | 38/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.01×** | +9.0 | 1e-17 | 38/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +8.5 | 1e-15 | 36/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.5 | 3e-12 | 35/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +7.1 | 5e-11 | 37/48 (J82, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 2e-10 | 28/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 9e-10 | 34/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +6.2 | 1e-08 | 34/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.56×** | +5.9 | 8e-08 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +5.8 | 2e-07 | 28/48 (A498, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6022.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (SW48 0.0813×); [[Furosemide (drug)]] 0.5 µM in 1 line (H4 0.125×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.636×** | -8.6 | 6e-15 | 39/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.564×** | -7.7 | 5e-12 | 40/48 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.775× | -3.3 | 0.15 | 18/47 (A-172, NCI-H460, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.784× | -3.3 | 0.15 | 15/48 (PANC-1, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.2 | 15 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +20.0) | — |
| [[SW480 (line)]] | alt | 29.1 | 13 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 28.8 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +14.9) | — |
| [[LoVo (line)]] | wt | 16.9 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +15.1) | — |
| [[SW1417 (line)]] | alt | 36.6 | 6 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.6 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 18.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 40.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.9) | — |
| [[KATO III (line)]] | alt | 32.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 22.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +15.2) | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.0) | — |
| [[RKO (line)]] | wt | 22.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +11.6) | — |
| [[A-427 (line)]] | wt | 20.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.18× (z +9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +9.3) | — |
| [[A549 (line)]] | wt | 20.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 33.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +17.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 27.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.5) | — |
| [[C32 (line)]] | wt | 27.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +14.2) | — |
| [[H4 (line)]] | wt | 29.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +9.0) | [[Furosemide (drug)]] 0.5 µM 0.125× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 18.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 24.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.1) | — |
| [[SW48 (line)]] | wt | 18.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +10.2) | [[Orlistat (drug)]] 0.05 µM 0.0813× (z -10.1) |
| [[A498 (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.82× (z +15.1) | — |
| [[BT-474 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 9.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +11.7) | — |
| [[J82 (line)]] | alt | 22.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +13.7) | — |
| [[RPMI-7951 (line)]] | alt | 36.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 47.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM174A]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[ZNF487]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[CFAP69]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[ZNHIT1]] | +0.59 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MORN2]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CFAP210]] | +0.57 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[COG7]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TMEM67]] | +0.57 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[CCDC40]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CCDC157]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[DZANK1]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[UBE2D4]] | -0.49 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[DNAH14]] | -0.49 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[PSEN2]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RASGEF1C]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TMEM177]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SACS]] | -0.47 | -0.45 / -0.47 | both halves | 3e-05 | same gene group |
| [[PDCD2]] | -0.47 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[RIOX2]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNF365]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[GLIPR2]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD42's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.1, 21.5); signed map (-19.3, 4.7). **Vector** length 87.3, 23.8% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +24.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.0 | +14.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.6 | +4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +7.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.9 | -8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.4 | -7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:83,193,712-83,260,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37874, SARP, PPP1R79 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

UniProt [Q8N9B4](https://www.uniprot.org/uniprotkb/Q8N9B4) carries no function annotation.

**Summary**, from NCBI Gene [338699](https://www.ncbi.nlm.nih.gov/gene/338699):

> Predicted to enable NF-kappaB binding activity and cyclin-dependent protein serine/threonine kinase inhibitor activity. Predicted to act upstream of or within obsolete positive regulation of NF-kappaB transcription factor activity and positive regulation of cytokine production involved in inflammatory response. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26752) · Entrez [338699](https://www.ncbi.nlm.nih.gov/gene/338699) · UniProt [Q8N9B4](https://www.uniprot.org/uniprotkb/Q8N9B4) · Ensembl [ENSG00000137494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137494)

## Data

Gene col 6022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6022); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6022]; `tensor/DDL_lfc|DDL_z.npy` [6022]; `embed/gene_vectors.npy` [6022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6022 or target_col == 6022). Every well: [[ANKRD42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
