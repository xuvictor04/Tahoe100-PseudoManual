---
symbol: "FBXO22"
type: "gene"
col: 9434
ensembl_id: "ENSG00000167196"
name: "F-box protein 22"
location: "15q24.2"
module: 62
arm: "+"
pooled_cpm: 65.98
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 1
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# FBXO22

*F-box protein 22* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +24.3, q 0e+00, up in 45 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.111×, A-172 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.336×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.535×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIGAR]] (+0.71, fdr 7e-06), [[TMEM68]] (+0.68, fdr 7e-06), [[ACTA2]] (+0.64, fdr 1e-05); moves opposite to [[KLF2]] (-0.58, fdr 4e-05), [[DHRS2]] (-0.57, fdr 4e-05), [[EZR]] (-0.53, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ASCC3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +24.3 | 0e+00 | 45/49 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +15.6 | 0e+00 | 43/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +15.5 | 0e+00 | 44/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +13.3 | 4e-38 | 40/50 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +8.6 | 8e-16 | 27/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +6.9 | 4e-10 | 24/48 (NCI-H460, SNU-1, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.7 | 1e-09 | 30/49 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.33×** | +6.3 | 3e-08 | 31/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 2e-06 | 26/48 (A-172, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +5.3 | 6e-06 | 27/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +4.8 | 8e-05 | 22/48 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.15× | +4.2 | 0.001 | 18/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.20×** | +4.0 | 0.002 | 22/49 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 18/48 (A-172, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | **1.21×** | +3.9 | 0.003 | 20/47 (C-33 A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.005 | 20/48 (A498, A549, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.007 | 18/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.011 | 18/48 (NCI-H460, A498, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.015 | 20/48 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.017 | 16/48 (LoVo, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.024 | 19/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.033 | 18/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.111×, A-172 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.336×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.535×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.798× | -3.5 | 0.25 | 18/48 (H4, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.900× | -3.2 | 0.34 | 11/48 (LS 180, SW1417, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.868× | -3.1 | 0.40 | 3/48 (LoVo, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.2 | 13 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +23.2) | — |
| [[A-172 (line)]] | wt | 79.6 | 10 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A498 (line)]] | wt | 98.1 | 10 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +20.1) | — |
| [[A549 (line)]] | wt | 148 | 8 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 82.3 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +17.2) | — |
| [[RKO (line)]] | wt | 91.6 | 6 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +20.5) | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[LoVo (line)]] | wt | 107 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +16.4) | — |
| [[LOX-IMVI (line)]] | wt | 79.6 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +21.0) | — |
| [[HepG2_C3A (line)]] | wt | 75.3 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +17.8) | — |
| [[SNU-1 (line)]] | wt | 81.0 | 5 (3 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.12× (z +13.3) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.7) | — |
| [[H4 (line)]] | wt | 64.9 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 47.3 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +14.0) | — |
| [[SW480 (line)]] | alt | 65.4 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.23× (z +10.6) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.3) | — |
| [[A-427 (line)]] | wt | 79.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 30.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 41.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 59.0 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.68× (z +11.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 45.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 74.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 70.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 71.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SNU-423 (line)]] | alt | 28.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.4) | — |
| [[SW48 (line)]] | wt | 83.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +17.0) | — |
| [[AsPC-1 (line)]] | alt | 37.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.25× (z +9.1) ⚠ toxic | — |
| [[KATO III (line)]] | alt | 47.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.58× (z +11.2) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 65.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.64× (z +10.0) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.361× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~92% of this change |
| [[SW 900 (line)]] | alt | 42.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 61.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGAR]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TMEM68]] | +0.68 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SESN1]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PANK1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.63 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[EI24]] | +0.62 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[NOPCHAP1]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.62 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[ZMAT3]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ZNF79]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PINCR]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF2]] | -0.58 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[DHRS2]] | -0.57 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[EZR]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[DNAJB1]] | -0.52 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[LMCD1]] | -0.50 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[ATP1A3]] | -0.48 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[CCDC110]] | -0.47 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[ARL4A]] | -0.46 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[TCN2]] | -0.46 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 6, C 8. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity raises FBXO22's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without PINCR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises FBXO22's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.33× lower at baseline in the lines without EDA2R | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[TOP2A]] | B | TOP2A activity lowers FBXO22's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens FBXO22's drug response | lines that do not express PINCR (29) vs lines expressing it (21) | the lines without PINCR respond 0.57× as strongly (z diff +2.77); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.18x vs 2.12x (z diff +4.4) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; artifact flags |
| [[TP53]] | B | TP53 activity strengthens FBXO22's drug response | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | the TP53-altered lines respond 0.46× as strongly (z diff +3.23); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.15x vs 2.38x (z diff +5.6) | 0.065 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; artifact flags |
| [[EDA2R]] | B | EDA2R activity strengthens FBXO22's drug response | lines that do not express EDA2R (28) vs lines expressing it (22) | the lines without EDA2R respond 0.86× as strongly (z diff +1.26); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.25x vs 1.47x (z diff +2.4) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3; artifact flags |
| [[MDM2]] | C | MDM2's natural level strengthens FBXO22's drug response | MDM2's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.55; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[FDXR]] | C | FDXR's natural level strengthens FBXO22's drug response | FDXR's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.42; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[AEN]] | C | AEN's natural level strengthens FBXO22's drug response | AEN's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.54; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NOPCHAP1]] | C | NOPCHAP1's natural level strengthens FBXO22's drug response | NOPCHAP1's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.13; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZMAT3]] | C | ZMAT3's natural level strengthens FBXO22's drug response | ZMAT3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.73, reverse -0.34; direction not clear | 0.010 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RRM2B]] | C | RRM2B's natural level strengthens FBXO22's drug response | RRM2B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.05; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCC3]] | C | FBXO22's natural level strengthens ASCC3's drug response | FBXO22's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.44; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.4, 34.8); signed map (42.4, -26.0). **Vector** length 124, 35.6% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +15.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +15.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +24.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +13.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.9 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +8.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +3.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | +1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -4.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +0.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,903,876-75,942,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX22, FISTC1 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEZ5](https://www.uniprot.org/uniprotkb/Q8NEZ5) (F-box only protein 22):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex that is implicated in the control of various cellular processes such as cell cycle control, transcriptional regulation, DNA damage repair, and apoptosis. Promotes the proteasome-dependent degradation of key sarcomeric proteins, such as alpha-actinin (ACTN2) and filamin-C (FLNC), essential for maintenance of normal contractile function. Acts as a key regulator of histone methylation marks namely …

**Summary**, from NCBI Gene [26263](https://www.ncbi.nlm.nih.gov/gene/26263):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13593) · Entrez [26263](https://www.ncbi.nlm.nih.gov/gene/26263) · UniProt [Q8NEZ5](https://www.uniprot.org/uniprotkb/Q8NEZ5) · Ensembl [ENSG00000167196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167196)

## Data

Gene col 9434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9434); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9434]; `tensor/DDL_lfc|DDL_z.npy` [9434]; `embed/gene_vectors.npy` [9434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9434 or target_col == 9434). Every well: [[FBXO22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
