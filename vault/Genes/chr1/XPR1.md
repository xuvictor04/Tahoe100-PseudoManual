---
symbol: "XPR1"
type: "gene"
col: 6715
ensembl_id: "ENSG00000143324"
name: "xenotropic and polytropic retrovirus receptor 1"
location: "1q25.3"
module: 23
arm: "-"
pooled_cpm: 127.03
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# XPR1

*xenotropic and polytropic retrovirus receptor 1* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +22.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.726× (z -6.2, q 4e-07, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.777× (z -5.3, q 4e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (Panc 03.27 0.123×, A-427 0.344×, SK-MEL-2 0.336×, C-33 A 0.319×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.457×, NCI-H2347 0.515×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.225×, HepG2/C3A 0.274×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.598×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXT2]] (+0.69, fdr 1e-05), [[SRPK2]] (+0.68, fdr 8e-06), [[INPP4A]] (+0.65, fdr 1e-05); moves opposite to [[GOSR1]] (-0.63, fdr 1e-05), [[MSANTD3-TMEFF1]] (-0.60, fdr 4e-05), [[THAP2]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +22.9 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.58×** | +19.6 | 0e+00 | 48/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +19.1 | 0e+00 | 48/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +12.4 | 3e-33 | 39/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +12.0 | 3e-31 | 43/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +11.9 | 2e-30 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +9.1 | 9e-18 | 39/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.7 | 2e-16 | 35/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.1 | 2e-14 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +8.0 | 8e-14 | 46/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.9 | 2e-10 | 37/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +6.5 | 4e-09 | 35/49 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.2 | 3e-08 | 32/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +6.1 | 3e-08 | 35/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +6.0 | 7e-08 | 28/49 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.1 | 1e-05 | 27/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.56×** | +4.8 | 5e-05 | 27/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 1e-04 | 26/48 (HT-29, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6715.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (Panc 03.27 0.123×, A-427 0.344×, SK-MEL-2 0.336×, C-33 A 0.319×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.457×, NCI-H2347 0.515×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.225×, HepG2/C3A 0.274×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.598×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.726×** | -6.2 | 4e-07 | 30/45 (Panc 03.27, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.777×** | -5.3 | 4e-05 | 28/48 (SW480, SW 1271, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.781×** | -5.2 | 5e-05 | 26/49 (SW1417, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.801×** | -4.5 | 0.001 | 23/44 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.815×** | -4.1 | 0.004 | 25/47 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.852× | -3.4 | 0.067 | 15/47 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | 0.853× | -3.3 | 0.067 | 22/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 128 | 9 | 1 | [[Panobinostat (drug)]] 5 µM 2.85× (z +17.2) | [[Auranofin (drug)]] 5 µM 0.598× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 157 | 6 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 90.3 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 134 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 125 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +17.8) | — |
| [[A-172 (line)]] | wt | 107 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 85.9 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 56.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +15.7) | — |
| [[LoVo (line)]] | wt | 98.7 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 85.4 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.63× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -19.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 207 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -14.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 96.6 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 94.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 119 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.57× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 153 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 77.0 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 15.0× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 86.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.47× (z +14.8) | — |
| [[COLO 205 (line)]] | alt | 137 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +12.6) | — |
| [[H4 (line)]] | wt | 72.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 65.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 162 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -13.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 124 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 117 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 214 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 117 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -15.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 154 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -12.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 102 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +10.5) | — |
| [[A549 (line)]] | wt | 180 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 79.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 92.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 146 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.68× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 195 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 66.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 91.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 101 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 161 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 146 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 263 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -12.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 163 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 216 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXT2]] | +0.69 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.68 | +0.70 / +0.57 | both halves | 8e-06 |  |
| [[INPP4A]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[METAP1]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CCNY]] | +0.63 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[FDX1]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[CYRIB]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[STRN]] | +0.61 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[CARMIL1]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[STK3]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[EPS15]] | +0.60 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[PPP4R1]] | +0.60 | +0.72 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOSR1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[MSANTD3-TMEFF1]] | -0.60 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[THAP2]] | -0.60 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[CDKL3]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.58 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[ZNF547]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZNF621]] | -0.56 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB1]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[HELQ]] | -0.55 | -0.62 / -0.24 | both halves | 5e-04 |  |
| [[GOLGA1]] | -0.55 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[CFAP53]] | -0.55 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TRIM39]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-9.6, -7.3); signed map (-44.5, -6.9). **Vector** length 114, 38.5% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +11.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.8 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +8.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.5 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -12.9 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.8 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | xenotropic and polytropic retrovirus receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:180,632,022-180,890,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYG1, X3, SLC53A1 |
| Gene groups (HGNC) | Solute carrier family 53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBH6](https://www.uniprot.org/uniprotkb/Q9UBH6) (Solute carrier family 53 member 1):

> Inorganic ion transporter that mediates phosphate ion export across the plasma membrane. Plays a major role in phosphate homeostasis, preventing intracellular phosphate accumulation and possible calcium phosphate precipitation, ultimately preserving calcium signaling. Binds inositol hexakisphosphate (Ins6P) and similar inositol polyphosphates, such as 5-diphospho-inositol pentakisphosphate (5-InsP7), which are important intracellular signaling molecules involved in regulation of phosphate flux.

**Summary**, from NCBI Gene [9213](https://www.ncbi.nlm.nih.gov/gene/9213):

> The protein encoded by this gene is a receptor for the xenotropic and polytropic classes of murine leukemia viruses. The encoded protein is involved in phosphate homeostasis by mediating phosphate export from the cell. Defects in this gene have been associated with idiopathic basal ganglia calcification-6. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:12827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12827) · Entrez [9213](https://www.ncbi.nlm.nih.gov/gene/9213) · UniProt [Q9UBH6](https://www.uniprot.org/uniprotkb/Q9UBH6) · Ensembl [ENSG00000143324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143324)

## Data

Gene col 6715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6715); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6715]; `tensor/DDL_lfc|DDL_z.npy` [6715]; `embed/gene_vectors.npy` [6715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6715 or target_col == 6715). Every well: [[XPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
