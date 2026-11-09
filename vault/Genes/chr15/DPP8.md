---
symbol: "DPP8"
type: "gene"
col: 1084
ensembl_id: "ENSG00000074603"
name: "dipeptidyl peptidase 8"
location: "15q22.31"
module: 194
arm: "+"
pooled_cpm: 63.8
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# DPP8

*dipeptidyl peptidase 8* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +17.4, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.767× (z -6.0, q 1e-06, down in 25 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.831× (z -4.3, q 0.003, down in 18 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (NCI-H1573 0.403×, J82 0.433×, NCI-H460 0.516×, LoVo 0.521×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.516×, NCI-H1573 0.469×, NCI-H460 0.505×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.449×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.313×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZIC]] (+0.71, fdr 1e-05), [[TAF2]] (+0.70, fdr 7e-06), [[DNAJC11]] (+0.69, fdr 7e-06); moves opposite to [[STK32C]] (-0.66, fdr 7e-06), [[EFNA4]] (-0.63, fdr 1e-05), [[MHENCR]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MLF1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BNIP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +17.4 | 0e+00 | 43/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +13.4 | 2e-38 | 42/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +8.6 | 1e-15 | 31/49 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.6 | 1e-15 | 30/43 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +8.6 | 1e-15 | 32/49 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +6.4 | 2e-08 | 30/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.3 | 3e-08 | 27/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.4 | 4e-06 | 27/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.9 | 7e-05 | 25/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.5 | 3e-04 | 22/48 (RKO, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.2 | 0.001 | 10/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 13/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 16/49 (Panc 03.27, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 12/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.12× | +3.7 | 0.007 | 14/48 (A498, HT-29, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.024 | 14/47 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.080 | 2/48 (NCI-H460, COLO 205) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.080 | 2/48 (PANC-1, LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1084.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (NCI-H1573 0.403×, J82 0.433×, NCI-H460 0.516×, LoVo 0.521×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.516×, NCI-H1573 0.469×, NCI-H460 0.505×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.449×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.313×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -6.0 | 1e-06 | 25/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.9 | 3e-04 | 1/49 (HepG2/C3A) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -4.3 | 0.003 | 18/49 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -3.4 | 0.090 | 15/49 (hTERT-HPNE, A498, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.764× | -3.2 | 0.14 | 17/45 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 64.4 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.51× (z +25.6) | — |
| [[NCI-H1573 (line)]] | alt | 86.9 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.403× (z -11.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 58.3 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.505× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 101 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.521× (z -8.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 75.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.449× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 81.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.0) | — |
| [[HOP62 (line)]] | alt | 54.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 51.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +23.5) | — |
| [[NCI-H23 (line)]] | alt | 65.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 49.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 48.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 70.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.94× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 58.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.2) | — |
| [[J82 (line)]] | alt | 68.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.433× (z -8.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 76.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 62.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 61.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.5) | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.313× (z -10.5) |
| [[RKO (line)]] | wt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.1) | — |
| [[A-172 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZIC]] | +0.71 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[TAF2]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[NDUFS1]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[DNAJC8]] | +0.68 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[SNX19]] | +0.67 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[NEK9]] | +0.67 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ZFP91]] | +0.66 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[JPX]] | +0.66 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[ST7L]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK32C]] | -0.66 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[EFNA4]] | -0.63 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MHENCR]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[PPP1R2]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[AFMID]] | -0.60 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[HDAC3]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[DPM1]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.59 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CARD19]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLF1]] | B | MLF1 activity raises DPP8's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without MLF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BNIP2]] | C | DPP8's natural level strengthens BNIP2's drug response | DPP8's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.21; direction not clear | 0.067 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-22.1, 10.3); signed map (14.3, -29.2). **Vector** length 114, 29.0% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +13.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -6.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,442,463-65,517,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DP8, DPRP1, MSTP141, FLJ14920, FLJ20283, MGC26191 |
| Gene groups (HGNC) | DASH family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6V1X1](https://www.uniprot.org/uniprotkb/Q6V1X1) (Dipeptidyl peptidase 8):

> Dipeptidyl peptidase that cleaves off N-terminal dipeptides from proteins having a Pro or Ala residue at position 2. Acts as a key inhibitor of caspase-1-dependent monocyte and macrophage pyroptosis in resting cells by preventing activation of NLRP1 and CARD8. Sequesters the cleaved C-terminal part of NLRP1 and CARD8, which respectively constitute the active part of the NLRP1 and CARD8 inflammasomes, in a ternary complex, thereby preventing their oligomerization and activation. The dipeptidyl …

**Summary**, from NCBI Gene [54878](https://www.ncbi.nlm.nih.gov/gene/54878):

> This gene encodes a member of the peptidase S9B family, a small family of dipeptidyl peptidases that are able to cleave peptide substrates at a prolyl bond. The encoded protein shares similarity with dipeptidyl peptidase IV in that it is ubiquitously expressed, and hydrolyzes the same substrates. These similarities suggest that, like dipeptidyl peptidase IV, this protein may play a role in T-cell activation and immune function. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:16490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16490) · Entrez [54878](https://www.ncbi.nlm.nih.gov/gene/54878) · UniProt [Q6V1X1](https://www.uniprot.org/uniprotkb/Q6V1X1) · Ensembl [ENSG00000074603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074603)

## Data

Gene col 1084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1084); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1084]; `tensor/DDL_lfc|DDL_z.npy` [1084]; `embed/gene_vectors.npy` [1084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1084 or target_col == 1084). Every well: [[DPP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
