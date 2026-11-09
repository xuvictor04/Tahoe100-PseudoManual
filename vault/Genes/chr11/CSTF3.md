---
symbol: "CSTF3"
type: "gene"
col: 10682
ensembl_id: "ENSG00000176102"
name: "cleavage stimulation factor subunit 3"
location: "11p13"
module: 83
arm: "+"
pooled_cpm: 92.76
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# CSTF3

*cleavage stimulation factor subunit 3* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +24.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.576× (z -6.2, q 4e-07, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.807× (z -4.6, q 8e-04, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.208×, AsPC-1 0.410×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (H4 0.268×, HepG2/C3A 0.368×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.361×, SHP-77 0.421×; ⚠ toxic; cell-cycle shift, explains ~27% of this change).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF10]] (+0.76, fdr 1e-05), [[PBLD]] (+0.75, fdr 2e-04), [[PCBP1-AS1]] (+0.73, fdr 9e-05); moves opposite to [[MAST3]] (-0.70, fdr 3e-04), [[SLC27A1]] (-0.69, fdr 2e-04), [[USP2]] (-0.69, fdr 2e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +24.9 | 0e+00 | 47/48 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +19.4 | 0e+00 | 46/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +17.1 | 0e+00 | 44/49 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +17.1 | 0e+00 | 46/50 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +14.1 | 7e-43 | 44/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +13.7 | 5e-41 | 46/48 (SW48, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +10.1 | 4e-22 | 43/48 (SHP-77, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +9.8 | 9e-21 | 36/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +8.5 | 1e-15 | 32/47 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.7 | 1e-09 | 30/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +5.8 | 3e-07 | 30/49 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 2e-05 | 26/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.7 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.6 | 2e-04 | 25/48 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +4.6 | 2e-04 | 24/48 (AsPC-1, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.008 | 17/49 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.008 | 18/47 (A498, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.024 | 13/48 (SW480, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.040 | 18/47 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.085 | 7/48 (A-427, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10682.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.208×, AsPC-1 0.410×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (H4 0.268×, HepG2/C3A 0.368×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.361×, SHP-77 0.421×; ⚠ toxic; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.576×** | -6.2 | 4e-07 | 35/47 (C32, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.779×** | -5.3 | 3e-05 | 26/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.807×** | -4.6 | 8e-04 | 25/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.005 | 23/48 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.9 | 0.011 | 22/48 (NCI-H23, Panc 03.27, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.8 | 0.012 | 22/48 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.842× | -3.7 | 0.018 | 21/48 (NCI-H23, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.6 | 0.022 | 20/48 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.766× | -3.1 | 0.12 | 10/48 (H4, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.769× | -3.1 | 0.12 | 13/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | 0.868× | -3.0 | 0.12 | 11/48 (CFPAC-1, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 77.0 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 95.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.4) | — |
| [[NCI-H2347 (line)]] | alt | 75.8 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +18.6) | — |
| [[HS-578T (line)]] | alt | 85.2 | 6 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +15.5) | — |
| [[NCI-H460 (line)]] | wt | 79.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 83.3 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +16.3) | — |
| [[A-172 (line)]] | wt | 123 | 5 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.39× (z +15.6) | — |
| [[AsPC-1 (line)]] | alt | 104 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 36.7 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +14.1) | — |
| [[Hs 766T (line)]] | wt | 93.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.5) | — |
| [[LoVo (line)]] | wt | 86.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 64.8 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +15.9) | — |
| [[SW1417 (line)]] | alt | 79.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +16.7) | — |
| [[SW48 (line)]] | wt | 86.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +15.5) | — |
| [[SW480 (line)]] | alt | 122 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +16.6) | — |
| [[C32 (line)]] | wt | 73.8 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 62.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +14.9) | — |
| [[H4 (line)]] | wt | 142 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 99.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.6) | — |
| [[NCI-H2030 (line)]] | alt | 57.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +19.7) | — |
| [[SW 900 (line)]] | alt | 39.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 92.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.6) | — |
| [[HepG2_C3A (line)]] | wt | 89.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 90.5 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.0) | — |
| [[J82 (line)]] | alt | 135 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 57.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 95.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.438× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 89.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 80.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 94.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +12.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.421× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 90.2 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.86× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 114 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.04× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 129 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 99.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 82.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.6) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 80.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.5) | — |
| [[A498 (line)]] | wt | 117 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.9) | — |
| [[A549 (line)]] | wt | 96.7 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.73× (z +8.6) | — |
| [[KATO III (line)]] | alt | 50.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.0) | — |
| [[RKO (line)]] | wt | 184 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 142 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF10]] | +0.76 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[PBLD]] | +0.75 | +0.73 / +0.32 | both halves | 2e-04 |  |
| [[PCBP1-AS1]] | +0.73 | +0.69 / +0.36 | both halves | 9e-05 |  |
| [[ZNF337-AS1]] | +0.73 | +0.73 / +0.35 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | +0.73 | +0.69 / +0.37 | both halves | 9e-05 |  |
| [[LINC01829]] | +0.72 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[MIRLET7IHG]] | +0.71 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.70 | +0.72 / +0.40 | both halves | 5e-05 |  |
| [[MSH4]] | +0.70 | +0.72 / +0.31 | both halves | 2e-04 |  |
| [[ST7L]] | +0.70 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[KLRA1P]] | +0.70 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.70 | +0.69 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.70 | -0.70 / -0.28 | both halves | 3e-04 |  |
| [[SLC27A1]] | -0.69 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[USP2]] | -0.69 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SUFU]] | -0.67 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TSPAN33]] | -0.67 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[CEP131]] | -0.67 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[DNAAF3]] | -0.66 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CFD]] | -0.66 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ALAD]] | -0.66 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[RAB40B]] | -0.65 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[EFNA4]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.64 | -0.51 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[PLEKHH3]] | -0.64 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSTF3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C2]] | B | NR3C2 activity strengthens CSTF3's drug response | lines that do not express NR3C2 (15) vs lines expressing it (35) | the lines without NR3C2 respond 0.91× as strongly (z diff +0.97); strongest at Idarubicin (hydrochloride) 5 µM: 1.51x vs 1.94x (z diff +2.1) | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.9, 7.4); signed map (23.3, -8.0). **Vector** length 135, 43.3% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +19.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +17.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.8 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.8 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.2 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -10.0 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.5 | -3.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.5 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | cleavage stimulation factor subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,077,188-33,162,371 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CstF-77 |
| Gene groups (HGNC) | Cleavage stimulation factor subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 10 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12996](https://www.uniprot.org/uniprotkb/Q12996) (Cleavage stimulation factor subunit 3):

> One of the multiple factors required for polyadenylation and 3'-end cleavage of mammalian pre-mRNAs.

**Summary**, from NCBI Gene [1479](https://www.ncbi.nlm.nih.gov/gene/1479):

> The protein encoded by this gene is one of three (including CSTF1 and CSTF2) cleavage stimulation factors that combine to form the cleavage stimulation factor complex (CSTF). This complex is involved in the polyadenylation and 3' end cleavage of pre-mRNAs. The encoded protein functions as a homodimer and interacts directly with both CSTF1 and CSTF2 in the CSTF complex. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2485) · Entrez [1479](https://www.ncbi.nlm.nih.gov/gene/1479) · UniProt [Q12996](https://www.uniprot.org/uniprotkb/Q12996) · Ensembl [ENSG00000176102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176102)

## Data

Gene col 10682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10682); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10682]; `tensor/DDL_lfc|DDL_z.npy` [10682]; `embed/gene_vectors.npy` [10682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10682 or target_col == 10682). Every well: [[CSTF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
