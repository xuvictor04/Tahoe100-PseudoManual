---
symbol: "BECN1"
type: "gene"
col: 4746
ensembl_id: "ENSG00000126581"
name: "beclin 1"
location: "17q21.31"
module: 35
arm: "+"
pooled_cpm: 39.23
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# BECN1

*beclin 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +17.4, q 0e+00, up in 42 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +12.4, q 3e-33, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (CHP-212 0.0657×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.343×; ⚠ toxic; transcription drop); [[LJI308 (drug)]] 0.05 µM in 1 line (CHP-212 0.148×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC7]] (+0.61, fdr 3e-05), [[C11orf58]] (+0.60, fdr 1e-05), [[CFLAR]] (+0.59, fdr 3e-05); moves opposite to [[CCDC85B]] (-0.63, fdr 1e-05), [[LSM2]] (-0.57, fdr 4e-05), [[YIF1B]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +17.4 | 0e+00 | 42/45 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +13.3 | 7e-38 | 37/41 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +12.4 | 3e-33 | 44/48 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +12.4 | 3e-33 | 39/43 (KATO III, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.5 | 2e-15 | 41/48 (HEC-1-A, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +8.2 | 3e-14 | 41/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.4 | 6e-06 | 30/48 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 1e-05 | 29/46 (SW1417, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 6e-04 | 22/48 (HOP62, LoVo, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 6e-04 | 24/48 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 9e-04 | 21/47 (A498, A-172, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.3 | 9e-04 | 21/47 (KATO III, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 9e-04 | 18/48 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 9e-04 | 26/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.003 | 20/48 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.006 | 17/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.007 | 19/48 (HOP62, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.009 | 19/46 (SW480, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.013 | 21/47 (HOP62, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.019 | 20/48 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4746.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (CHP-212 0.0657×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.343×; ⚠ toxic; transcription drop); [[LJI308 (drug)]] 0.05 µM in 1 line (CHP-212 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -4.0 | 0.041 | 14/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.828× | -3.3 | 0.30 | 15/48 (NCI-H460, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.0) | — |
| [[SW480 (line)]] | alt | 43.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.28× (z +9.8) | — |
| [[A549 (line)]] | wt | 39.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 43.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 25.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 60.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.31× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 42.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.6) | — |
| [[A-427 (line)]] | wt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 54.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 42.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 49.7 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.0657× (z -13.0) |
| [[HS-578T (line)]] | alt | 32.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.5) | — |
| [[LoVo (line)]] | wt | 33.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +8.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 75.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC7]] | +0.61 | +0.45 / +0.59 | both halves | 3e-05 | same gene group |
| [[C11orf58]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CFLAR]] | +0.59 | +0.52 / +0.44 | both halves | 3e-05 | STRING 687 |
| [[RBM42]] | +0.59 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[STXBP2]] | +0.59 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[VPS52]] | +0.59 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[ATXN1L]] | +0.59 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TMEM199]] | +0.58 | +0.57 / +0.44 | both halves | 3e-05 | same gene group |
| [[RNF6]] | +0.58 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[WDR45]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 | pathway: Autophagy; STRING 599 |
| [[PSME3IP1]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[FBXL19-AS1]] | +0.57 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 8 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC85B]] | -0.63 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[LSM2]] | -0.57 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[YIF1B]] | -0.57 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[PAXX]] ⚠ | -0.54 | -0.29 / -0.41 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NPM3]] | -0.54 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ANAPC11]] | -0.53 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[ATP5F1D]] ⚠ | -0.53 | -0.14 / -0.42 | ⚠ not reproduced | 0.002 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM191A-1]] | -0.53 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[RPL22L1]] ⚠ | -0.52 | -0.20 / -0.56 | ⚠ one half (not replicated) | 8e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PBX4]] | -0.52 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.52 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[FAM13B]] | -0.51 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[ARL3]] | -0.51 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[ETHE1]] | -0.51 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[PPP1R14B]] | -0.51 | -0.58 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BECN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-8.2, 3.4); signed map (18.0, -21.3). **Vector** length 84.8, 19.0% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +5.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | +3.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.9 | -1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | beclin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,810,134-42,833,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATG6, VPS30 |
| Gene groups (HGNC) | Autophagy related; PIK3C3 complex subunits; MicroRNA protein coding host genes; Beclin family |
| Reactome | 25 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Dengue virus modulates apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14457](https://www.uniprot.org/uniprotkb/Q14457) (Beclin-1):

> Plays a central role in autophagy. Acts as a core subunit of the PI3K complex that mediates formation of phosphatidylinositol 3-phosphate; different complex forms are believed to play a role in multiple membrane trafficking pathways: PI3KC3-C1 is involved in initiation of autophagosomes and PI3KC3-C2 in maturation of autophagosomes and endocytosis. Involved in regulation of degradative endocytic trafficking and required for the abscission step in cytokinesis, probably in the context of …

**Summary**, from NCBI Gene [8678](https://www.ncbi.nlm.nih.gov/gene/8678):

> This gene encodes a protein that regulates autophagy, a catabolic process of degradation induced by starvation. The encoded protein is a component of the phosphatidylinositol-3-kinase (PI3K) complex which mediates vesicle-trafficking processes. This protein is thought to play a role in multiple cellular processes, including tumorigenesis, neurodegeneration and apoptosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:1034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1034) · Entrez [8678](https://www.ncbi.nlm.nih.gov/gene/8678) · UniProt [Q14457](https://www.uniprot.org/uniprotkb/Q14457) · Ensembl [ENSG00000126581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126581)

## Data

Gene col 4746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4746); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4746]; `tensor/DDL_lfc|DDL_z.npy` [4746]; `embed/gene_vectors.npy` [4746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4746 or target_col == 4746). Every well: [[BECN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BECN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
