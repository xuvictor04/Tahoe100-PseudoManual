---
symbol: "RPAP3"
type: "gene"
col: 70
ensembl_id: "ENSG00000005175"
name: "RNA polymerase II associated protein 3"
location: "12q13.11"
module: 17
arm: "+"
pooled_cpm: 52.12
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RPAP3

*RNA polymerase II associated protein 3* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +30.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.711× (z -11.8, q 2e-29, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (SNU-1 0.202×, RKO 0.468×, SW1417 0.522×, LoVo 0.557×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.175×, A-427 0.305×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.314×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOCS2]] (+0.76, fdr 7e-06), [[BMS1]] (+0.66, fdr 7e-06), [[MAP9]] (+0.66, fdr 1e-05); moves opposite to [[CA5BP1]] (-0.64, fdr 8e-06), [[WDR20]] (-0.63, fdr 1e-05), [[LEMD3]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 70.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +30.3 | 0e+00 | 47/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +21.9 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +21.8 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +20.2 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +17.4 | 0e+00 | 45/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +15.7 | 0e+00 | 46/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.82×** | +14.6 | 0e+00 | 39/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.80×** | +13.8 | 2e-41 | 31/42 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +13.8 | 2e-41 | 44/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +13.3 | 2e-38 | 44/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +12.2 | 2e-32 | 41/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +11.8 | 2e-30 | 40/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +10.3 | 2e-23 | 38/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.53×** | +9.5 | 6e-20 | 30/45 (A-427, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +9.5 | 1e-19 | 37/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +7.0 | 8e-11 | 32/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +6.1 | 3e-08 | 32/48 (AsPC-1, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +6.0 | 8e-08 | 26/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 70.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (SNU-1 0.202×, RKO 0.468×, SW1417 0.522×, LoVo 0.557×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.175×, A-427 0.305×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (Hs 766T 0.314×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -11.8 | 2e-29 | 38/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 0.868× | -3.4 | 0.18 | 15/47 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.867× | -3.2 | 0.22 | 11/47 (BT-474, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.838× | -3.1 | 0.22 | 14/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.880× | -3.1 | 0.22 | 10/48 (hTERT-HPNE, SW 1088, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.790× | -3.0 | 0.22 | 10/48 (CHP-212, AN3 CA, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.22 | 10/47 (HOP62, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 70. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.0 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -11.2) |
| [[PANC-1 (line)]] | alt | 56.6 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -9.6) |
| [[LoVo (line)]] | wt | 74.7 | 8 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -12.1) |
| [[SW480 (line)]] | alt | 93.4 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +15.1) | — |
| [[A549 (line)]] | wt | 58.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +20.2) | — |
| [[LOX-IMVI (line)]] | wt | 40.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 85.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +22.5) | — |
| [[J82 (line)]] | alt | 49.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +16.3) | — |
| [[RKO (line)]] | wt | 80.2 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.9) |
| [[A-172 (line)]] | wt | 33.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 34.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.53× (z +14.0) | — |
| [[C32 (line)]] | wt | 42.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 62.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.4) | — |
| [[Hs 766T (line)]] | wt | 40.8 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.0) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.314× (z -9.4) |
| [[HT-29 (line)]] | alt | 55.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 49.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 38.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 86.4 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -20.3) |
| [[SW1417 (line)]] | alt | 61.9 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 33.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +20.3) | — |
| [[HS-578T (line)]] | alt | 36.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.0) | — |
| [[KATO III (line)]] | alt | 62.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 49.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 38.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.9) | — |
| [[SW48 (line)]] | wt | 55.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.2) | — |
| [[A-427 (line)]] | wt | 84.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 36.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.7) | — |
| [[A498 (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.2) | — |
| [[H4 (line)]] | wt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 53.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 45.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 70), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS2]] | +0.76 | +0.61 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[BMS1]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[MAP9]] | +0.66 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[CEP290]] | +0.65 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.64 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[DDX1]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TTC1]] | +0.63 | +0.50 / +0.67 | both halves | 1e-05 | same gene group; STRING 487 |
| [[CCNC]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[QDPR]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TBC1D19]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[NSFL1C]] | +0.60 | +0.39 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA5BP1]] | -0.64 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[WDR20]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[LEMD3]] | -0.62 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[TMEM187]] | -0.60 | -0.14 / -0.65 | ⚠ one half (not replicated) | 0.002 |  |
| [[PHC2-AS1]] | -0.60 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[KIAA2026]] | -0.60 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[GUCD1]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[MSL1]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[POC1B-AS1]] | -0.57 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[TTC28-AS1]] | -0.55 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[ENDOG]] | -0.55 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[SAP30L-AS1]] | -0.55 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[GATD1-DT]] | -0.55 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.5, -0.3); signed map (-22.6, -19.7). **Vector** length 99.8, 27.6% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +6.0 | +14.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +21.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.7 | -11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.6 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +3.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,661,249-47,706,030 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21908, spag, hSpagh, Tah1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; R2TP complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6T3](https://www.uniprot.org/uniprotkb/Q9H6T3) (RNA polymerase II-associated protein 3):

> Forms an interface between the RNA polymerase II enzyme and chaperone/scaffolding protein, suggesting that it is required to connect RNA polymerase II to regulators of protein complex formation.

**Summary**, from NCBI Gene [79657](https://www.ncbi.nlm.nih.gov/gene/79657):

> This gene encodes an RNA polymerase II-associated protein. The encoded protein may function in transcriptional regulation and may also regulate apoptosis. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:26151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26151) · Entrez [79657](https://www.ncbi.nlm.nih.gov/gene/79657) · UniProt [Q9H6T3](https://www.uniprot.org/uniprotkb/Q9H6T3) · Ensembl [ENSG00000005175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005175)

## Data

Gene col 70: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 70); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 70, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 70]; `tensor/DDL_lfc|DDL_z.npy` [70]; `embed/gene_vectors.npy` [70]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 70 or target_col == 70). Every well: [[RPAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
