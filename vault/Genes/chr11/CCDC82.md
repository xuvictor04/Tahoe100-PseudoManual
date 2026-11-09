---
symbol: "CCDC82"
type: "gene"
col: 7352
ensembl_id: "ENSG00000149231"
name: "coiled-coil domain containing 82"
location: "11q21"
module: 3
arm: "+"
pooled_cpm: 77.92
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CCDC82

*coiled-coil domain containing 82* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.23× (z +25.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.472× (z -12.3, q 5e-32, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.161×, SW480 0.459×, NCI-H23 0.334×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LOX-IMVI 0.274×, A-427 0.342×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 0.327×, NCI-H460 0.460×; ⚠ cell-cycle shift, explains ~6% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (AsPC-1 0.163×, HOP62 0.290×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.104×); [[PH-797804 (drug)]] 5 µM in 1 line (LOX-IMVI 0.236×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MORC3]] (+0.62, fdr 3e-05), [[WDR44]] (+0.61, fdr 1e-05), [[PPP1R21]] (+0.59, fdr 2e-05); moves opposite to [[HNRNPL]] (-0.56, fdr 6e-05), [[SSU72]] (-0.55, fdr 3e-05), [[HNRNPD]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +25.0 | 0e+00 | 46/47 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +24.7 | 0e+00 | 46/47 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +21.8 | 0e+00 | 37/48 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +21.4 | 0e+00 | 45/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +19.3 | 0e+00 | 43/49 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +18.8 | 0e+00 | 45/47 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +10.8 | 2e-25 | 31/47 (SW1417, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +10.3 | 3e-23 | 38/47 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +9.5 | 2e-19 | 27/47 (SW1417, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.34×** | +8.9 | 4e-17 | 30/46 (RKO, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +8.8 | 9e-17 | 32/47 (PANC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +7.5 | 4e-12 | 24/47 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +7.1 | 5e-11 | 27/47 (COLO 205, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +6.6 | 2e-09 | 20/47 (COLO 205, NCI-H1792, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +6.3 | 1e-08 | 22/47 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +5.0 | 2e-05 | 20/47 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +4.9 | 3e-05 | 22/48 (SW1417, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7352.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.161×, SW480 0.459×, NCI-H23 0.334×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LOX-IMVI 0.274×, A-427 0.342×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 0.327×, NCI-H460 0.460×; ⚠ cell-cycle shift, explains ~6% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (AsPC-1 0.163×, HOP62 0.290×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.104×); [[PH-797804 (drug)]] 5 µM in 1 line (LOX-IMVI 0.236×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -12.3 | 5e-32 | 39/48 (AsPC-1, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -10.1 | 1e-21 | 31/48 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.543×** | -10.0 | 2e-21 | 34/47 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.791×** | -7.1 | 2e-10 | 22/42 (LOX-IMVI, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.797×** | -6.6 | 5e-09 | 25/44 (LOX-IMVI, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.875× | -4.0 | 0.005 | 16/47 (NCI-H1792, SW480, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.893× | -3.6 | 0.029 | 4/47 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.908× | -3.1 | 0.16 | 9/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 116 | 5 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +14.2) | [[TAK-901 (drug)]] 5 µM 0.163× (z -12.3) |
| [[SW1417 (line)]] | alt | 93.0 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +19.7) | — |
| [[LOX-IMVI (line)]] | wt | 112 | 5 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.236× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 60.9 | 7 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +17.6) | [[TAK-901 (drug)]] 0.05 µM 0.504× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 50.9 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.401× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 187 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 74.9 | 5 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.5) | [[TAK-901 (drug)]] 5 µM 0.290× (z -9.3) |
| [[HS-578T (line)]] | alt | 107 | 5 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 57.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +16.0) | — |
| [[SW 900 (line)]] | alt | 89.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +14.0) | — |
| [[A-427 (line)]] | wt | 80.6 | 3 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 55.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +14.3) | — |
| [[KATO III (line)]] | alt | 98.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 45.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +13.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.436× (z -9.6) ⚠ cell-cycle shift, explains ~6% of this change |
| [[LS 180 (line)]] | wt | 71.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -12.6) ⚠ cell-cycle shift, explains ~6% of this change |
| [[PANC-1 (line)]] | alt | 110 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +17.2) | — |
| [[SNU-423 (line)]] | alt | 76.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 67.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +13.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 71.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 67.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +13.6) | — |
| [[RKO (line)]] | wt | 64.3 | 3 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 51.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 72.7 | 1 | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.319× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 98.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 83.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +20.0) | — |
| [[SW48 (line)]] | wt | 34.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +8.9) | — |
| [[A549 (line)]] | wt | 75.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.02× (z +9.1) | — |
| [[C32 (line)]] | wt | 26.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 112 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 72.9 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 79.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.104× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 81.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.88× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 86.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 58.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 87.3 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0689× (z -9.2) |
| [[AN3 CA (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORC3]] | +0.62 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[WDR44]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PPP1R21]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CERS5]] | +0.59 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ZC2HC1A]] | +0.56 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[KATNBL1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CNIH4]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[DHRS7]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[KCTD9]] | +0.54 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[DUSP18]] | +0.54 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[MED10]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | -0.56 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[SSU72]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[HNRNPD]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ZNF628]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[COG8]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[COA7]] | -0.50 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[ZNF644]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SFPQ]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[HNRNPH2]] | -0.50 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[SRSF3]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[EWSR1]] | -0.50 | -0.21 / -0.60 | both halves | 7e-04 |  |
| [[MRRF]] | -0.49 | -0.28 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC82's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.1, -1.0); signed map (-15.6, 17.7). **Vector** length 105, 27.9% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +21.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +19.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +10.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.7 | -12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.3 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.4 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | -10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 82 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:96,349,241-96,389,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23518 |
| Matched by | ensembl_id |

UniProt [Q8N4S0](https://www.uniprot.org/uniprotkb/Q8N4S0) carries no function annotation.

**Summary**, from NCBI Gene [79780](https://www.ncbi.nlm.nih.gov/gene/79780):

> Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26282) · Entrez [79780](https://www.ncbi.nlm.nih.gov/gene/79780) · UniProt [Q8N4S0](https://www.uniprot.org/uniprotkb/Q8N4S0) · Ensembl [ENSG00000149231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149231)

## Data

Gene col 7352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7352); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7352]; `tensor/DDL_lfc|DDL_z.npy` [7352]; `embed/gene_vectors.npy` [7352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7352 or target_col == 7352). Every well: [[CCDC82 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC82.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
