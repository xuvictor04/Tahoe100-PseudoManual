---
symbol: "PITPNA"
type: "gene"
col: 10478
ensembl_id: "ENSG00000174238"
name: "phosphatidylinositol transfer protein alpha"
location: "17p13.3"
module: 52
arm: "+"
pooled_cpm: 78.66
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PITPNA

*phosphatidylinositol transfer protein alpha* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +25.4, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.795× (z -8.6, q 4e-15, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.733× (z -8.2, q 5e-14, down in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (AsPC-1 0.542×, NCI-H1792 0.511×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.392×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HT-29 0.506×; ⚠ cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK1G2]] (+0.73, fdr 7e-06), [[PCSK7]] (+0.69, fdr 1e-05), [[USP20]] (+0.67, fdr 3e-05); moves opposite to [[CDC73]] (-0.64, fdr 1e-05), [[RBM7]] (-0.63, fdr 1e-05), [[RBBP9]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MAP4K5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +25.4 | 0e+00 | 47/49 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +21.3 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +18.7 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +17.6 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +11.3 | 1e-27 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +11.0 | 3e-26 | 39/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.50×** | +10.6 | 3e-24 | 39/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +10.5 | 7e-24 | 40/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +9.2 | 3e-18 | 33/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +9.0 | 1e-17 | 38/48 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +9.0 | 2e-17 | 36/50 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.28×** | +6.4 | 7e-09 | 28/48 (SW480, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.28×** | +6.2 | 2e-08 | 27/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +6.0 | 7e-08 | 26/48 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.18× | +6.0 | 9e-08 | 17/48 (NCI-H460, AsPC-1, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.8 | 2e-07 | 28/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 21/48 (LS 180, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.003 | 16/48 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.006 | 14/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.008 | 11/49 (MIA PaCa-2, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.011 | 10/49 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10478.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (AsPC-1 0.542×, NCI-H1792 0.511×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.392×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HT-29 0.506×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.795×** | -8.6 | 4e-15 | 30/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.733×** | -8.2 | 5e-14 | 35/49 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -6.0 | 3e-07 | 20/48 (KATO III, SHP-77, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.806×** | -5.7 | 1e-06 | 26/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.855× | -4.2 | 0.003 | 20/48 (HepG2/C3A, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.874× | -3.6 | 0.029 | 9/49 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.909× | -3.6 | 0.029 | 3/48 (RPMI-7951, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.883× | -3.5 | 0.029 | 9/50 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.879× | -3.5 | 0.031 | 11/48 (CFPAC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.879× | -3.5 | 0.031 | 15/47 (SW480, HepG2/C3A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.883× | -3.3 | 0.043 | 10/48 (A-172, RKO, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.895× | -3.2 | 0.063 | 8/49 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.922× | -3.1 | 0.082 | 1/48 (C32) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.892× | -3.1 | 0.092 | 7/48 (LoVo, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 126 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +16.0) | — |
| [[AsPC-1 (line)]] | alt | 65.7 | 7 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +16.6) | [[Selinexor (drug)]] 5 µM 0.542× (z -10.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 76.8 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +20.9) | — |
| [[LS 180 (line)]] | wt | 93.2 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 72.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +12.8) | — |
| [[LoVo (line)]] | wt | 104 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +16.9) | — |
| [[LOX-IMVI (line)]] | wt | 55.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +16.7) | — |
| [[A-172 (line)]] | wt | 95.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +12.7) | — |
| [[A549 (line)]] | wt | 92.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +19.3) | — |
| [[COLO 205 (line)]] | alt | 67.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 65.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +13.9) | — |
| [[KATO III (line)]] | alt | 114 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 65.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +11.2) | [[Selinexor (drug)]] 5 µM 0.511× (z -10.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[PANC-1 (line)]] | alt | 53.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 32.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 75.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.97× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 66.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -8.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 104 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.30× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 68.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 51.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 63.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.4) | — |
| [[A498 (line)]] | wt | 126 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 57.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 87.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +16.1) | — |
| [[Hs 766T (line)]] | wt | 56.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 83.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 69.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 65.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.6) | — |
| [[SW48 (line)]] | wt | 114 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 61.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -9.2) ⚠ cell-cycle shift, explains ~18% of this change |
| [[J82 (line)]] | alt | 86.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 56.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 99.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +14.3) | — |
| [[RKO (line)]] | wt | 107 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 56.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 77.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.5) | — |
| [[A-427 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G2]] | +0.73 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[PCSK7]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[USP20]] | +0.67 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[SENP5]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[AXIN1]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[MARK4]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SRGAP2D]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RAB43]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[MAPKAPK2]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FBH1]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HIRA]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC73]] | -0.64 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[RBM7]] | -0.63 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[RBBP9]] | -0.63 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[COMMD8]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CFL2]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[NBN]] | -0.59 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[ZBED8]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[C12orf29]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZNF711]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TRUB1]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[FUNDC1]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP4K5]] | C | PITPNA's natural level strengthens MAP4K5's drug response | PITPNA's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.01; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-15.2, -0.0); signed map (-45.9, 0.4). **Vector** length 109, 31.2% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +25.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +11.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.1 | +10.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.3 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -10.6 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -8.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.3 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol transfer protein alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,517,718-1,562,792 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VIB1A; previously PITPN |
| Gene groups (HGNC) | Phosphatidylinositol transfer proteins |
| Reactome | 9 pathways, smallest: Role of second messengers in netrin-1 signaling; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00169](https://www.uniprot.org/uniprotkb/Q00169) (Phosphatidylinositol transfer protein alpha isoform):

> Catalyzes the transfer of phosphatidylinositol (PI) and phosphatidylcholine (PC) between membranes. Shows a preference for PI and PC containing shorter saturated or monosaturated acyl chains at the sn-1 and sn-2 positions. Preference order for PC is C16:1 > C16:0 > C18:1 > C18:0 > C20:4 and for PI is C16:1 > C16:0 > C18:1 > C18:0 > C20:4 > C20:3.

**Summary**, from NCBI Gene [5306](https://www.ncbi.nlm.nih.gov/gene/5306):

> This gene encodes a member of a family of lipid-binding proteins that transfer molecules of phosphatidylinositol or phosphatidylcholine between membrane surfaces. The protein is implicated in phospholipase C signaling and in the production of phosphatidylinositol 3,4,5-trisphosphate (PIP3) by phosphoinositide-3-kinase.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:9001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9001) · Entrez [5306](https://www.ncbi.nlm.nih.gov/gene/5306) · UniProt [Q00169](https://www.uniprot.org/uniprotkb/Q00169) · Ensembl [ENSG00000174238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174238)

## Data

Gene col 10478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10478); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10478]; `tensor/DDL_lfc|DDL_z.npy` [10478]; `embed/gene_vectors.npy` [10478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10478 or target_col == 10478). Every well: [[PITPNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
