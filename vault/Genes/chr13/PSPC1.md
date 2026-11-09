---
symbol: "PSPC1"
type: "gene"
col: 4270
ensembl_id: "ENSG00000121390"
name: "paraspeckle component 1"
location: "13q12.11"
module: 143
arm: "+"
pooled_cpm: 117.45
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# PSPC1

*paraspeckle component 1* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.34× (z +22.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.771× (z -4.6, q 0.002, down in 25 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.783× (z -4.5, q 0.002, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 0.161×, SNU-1 0.317×, NCI-H23 0.394×, Panc 03.27 0.449×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.228×, SW 1271 0.110×, NCI-H1573 0.453×, LOX-IMVI 0.410×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW 1271 0.135×, C32 0.434×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPH3]] (+0.62, fdr 1e-05), [[USP13]] (+0.61, fdr 1e-05), [[SATB2]] (+0.60, fdr 5e-05); moves opposite to [[PLCD1]] (-0.63, fdr 1e-05), [[ZNF526]] (-0.61, fdr 2e-05), [[RARS1]] (-0.60, fdr 5e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[POLE]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +22.1 | 0e+00 | 47/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.73×** | +18.4 | 0e+00 | 48/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +12.9 | 9e-36 | 44/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.00×** | +12.7 | 7e-35 | 47/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +12.5 | 8e-34 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +11.7 | 8e-30 | 47/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +8.3 | 1e-14 | 40/48 (COLO 205, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +7.0 | 2e-10 | 42/49 (COLO 205, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.8 | 9e-10 | 36/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.2 | 4e-08 | 35/48 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +6.1 | 7e-08 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +5.7 | 5e-07 | 38/48 (NCI-H1573, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +5.4 | 3e-06 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 31/50 (H4, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.18× | +4.3 | 7e-04 | 26/49 (AsPC-1, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.007 | 15/48 (RKO, C-33 A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.080 | 15/47 (HT-29, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4270.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 0.161×, SNU-1 0.317×, NCI-H23 0.394×, Panc 03.27 0.449×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.228×, SW 1271 0.110×, NCI-H1573 0.453×, LOX-IMVI 0.410×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (SW 1271 0.135×, C32 0.434×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.6 | 0.002 | 25/44 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -4.5 | 0.002 | 32/48 (SW 1271, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.801×** | -4.1 | 0.009 | 27/49 (SK-MEL-2, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.828×** | -3.5 | 0.067 | 22/48 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.818×** | -3.4 | 0.067 | 24/45 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | 0.842× | -3.2 | 0.14 | 20/48 (SW1417, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.848× | -3.0 | 0.19 | 12/48 (SW 1088, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 179 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +21.9) | — |
| [[CFPAC-1 (line)]] | alt | 58.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +20.0) | — |
| [[LoVo (line)]] | wt | 110 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +22.7) | — |
| [[NCI-H460 (line)]] | wt | 99.1 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +16.1) | — |
| [[SW480 (line)]] | alt | 133 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +17.6) | — |
| [[KATO III (line)]] | alt | 105 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +20.5) | — |
| [[NCI-H1573 (line)]] | alt | 150 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -22.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 115 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.91× (z +21.9) | — |
| [[BT-474 (line)]] | alt | 158 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 102 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 175 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +19.5) | [[Lonafarnib (drug)]] 5 µM 0.0957× (z -13.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 122 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 83.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 73.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +17.9) | — |
| [[C32 (line)]] | wt | 183 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +18.2) | [[Auranofin (drug)]] 5 µM 0.434× (z -9.9) |
| [[H4 (line)]] | wt | 48.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 153 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 53.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.6) | — |
| [[SW 900 (line)]] | alt | 109 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 123 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 110 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 268 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 76.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 167 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 84.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 94.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 80.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +18.2) | — |
| [[J82 (line)]] | alt | 206 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 50.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.6) | — |
| [[SHP-77 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 72.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 163 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.135× (z -10.0) |
| [[SW48 (line)]] | wt | 199 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +11.5) | — |
| [[A-172 (line)]] | wt | 88.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) | — |
| [[A498 (line)]] | wt | 86.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.5) | — |
| [[A549 (line)]] | wt | 72.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 209 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 111 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.0) | — |
| [[RKO (line)]] | wt | 165 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.9) | — |
| [[A-427 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH3]] | +0.62 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[USP13]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[SATB2]] | +0.60 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[ADGRA3]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TCF12]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[NR2C2]] | +0.59 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PKP4]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ATE1]] | +0.58 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[ARHGEF11]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[ZNF236]] | +0.57 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[HMGB3]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ATXN7]] | +0.57 | +0.51 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCD1]] | -0.63 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF526]] | -0.61 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[RARS1]] | -0.60 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[MED8]] | -0.59 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[ATOSB]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GNAI3]] | -0.58 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[SGTB]] | -0.58 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[CYB5R1]] | -0.57 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[GIPR]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[VIPAS39]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[SDE2]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[C1orf52]] | -0.56 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 1, B 0, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLE]] | A | the direction of POLE's effect on PSPC1's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of POLE in 8 lines vs 41 not recorded | the POLE-altered lines respond 0.60× as strongly (z diff +1.86); strongest at Digitoxin 5 µM: 1.46x vs 2.24x (z diff +3.1) | 0.009 | ⚠ within organs, on part of the lines; mechanism partly not recorded; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.1, 4.7); signed map (23.2, -32.7). **Vector** length 92.9, 29.4% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +12.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.5 | +12.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +18.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | +1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | paraspeckle component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:19,674,752-19,783,019 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSP1, FLJ10955 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXF1](https://www.uniprot.org/uniprotkb/Q8WXF1) (Paraspeckle component 1):

> RNA-binding protein required for the formation of nuclear paraspeckles. Binds to poly(A), poly(G) and poly(U) RNA homopolymers. Regulates, cooperatively with NONO and SFPQ, androgen receptor-mediated gene transcription activity in Sertoli cell line (By similarity). Regulates the circadian clock by repressing the transcriptional activator activity of the CLOCK-BMAL1 heterodimer (By similarity). Plays a role in the regulation of DNA virus-mediated innate immune response by assembling into the …

**Summary**, from NCBI Gene [55269](https://www.ncbi.nlm.nih.gov/gene/55269):

> This gene encodes a nucleolar protein that localizes to punctate subnuclear structures that occur close to splicing speckles, known as paraspeckles. These paraspeckles are composed of RNA-protein structures that include a non-coding RNA, NEAT1/Men epsilon/beta, and the Drosophila Behavior Human Splicing family of proteins, which include the product of this gene and the P54NRB/NONO and PSF/SFPQ proteins. Paraspeckles may function in the control of gene expression via an RNA nuclear retention …

**Accessions** — [HGNC:20320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20320) · Entrez [55269](https://www.ncbi.nlm.nih.gov/gene/55269) · UniProt [Q8WXF1](https://www.uniprot.org/uniprotkb/Q8WXF1) · Ensembl [ENSG00000121390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121390)

## Data

Gene col 4270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4270); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4270]; `tensor/DDL_lfc|DDL_z.npy` [4270]; `embed/gene_vectors.npy` [4270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4270 or target_col == 4270). Every well: [[PSPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
