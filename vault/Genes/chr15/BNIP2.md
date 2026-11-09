---
symbol: "BNIP2"
type: "gene"
col: 6387
ensembl_id: "ENSG00000140299"
name: "BCL2 interacting protein 2"
location: "15q22.2"
module: 7
arm: "+"
pooled_cpm: 89.97
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# BNIP2

*BCL2 interacting protein 2* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.47× (z +16.7, q 0e+00, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.706× (z -17.5, q 0e+00, down in 40 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (A498 0.500×, LoVo 0.508×, SW480 0.626×, NCI-H460 0.604×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 5 lines (SW480 0.461×, H4 0.284×, A498 0.539×, LS 180 0.346×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.185×, H4 0.256×, SW480 0.484×, NCI-H1573 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THUMPD1]] (+0.56, fdr 1e-05), [[ATXN7L3]] (+0.52, fdr 8e-05), [[GTF3C3]] (+0.52, fdr 1e-04); moves opposite to [[ICAM5]] (-0.56, fdr 3e-05), [[OXR1]] (-0.53, fdr 1e-05), [[INTS6L]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +16.7 | 0e+00 | 38/49 (LoVo, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +12.3 | 2e-32 | 36/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +12.0 | 5e-31 | 0/50 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +9.3 | 2e-18 | 26/47 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +8.8 | 2e-16 | 32/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +8.3 | 1e-14 | 27/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.17× | +7.9 | 2e-13 | 20/48 (C32, SK-MEL-2, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +7.5 | 6e-12 | 26/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +7.2 | 3e-11 | 23/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | **1.22×** | +7.0 | 1e-10 | 24/48 (HEC-1-A, RKO, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.4 | 6e-09 | 21/38 (NCI-H1573, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +6.1 | 6e-08 | 22/48 (SW 900, COLO 205, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.0 | 9e-08 | 19/45 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change; position correction uncertain | 1.18× | +6.0 | 9e-08 | 21/48 (Hs 766T, SW48, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change; position correction uncertain | 1.19× | +5.6 | 9e-07 | 14/49 (NCI-H2030, NCI-H2347, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +4.9 | 3e-05 | 15/49 (BT-474, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +4.8 | 4e-05 | 13/48 (NCI-H2347, J82, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +4.8 | 5e-05 | 14/48 (NCI-H2030, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.20×** | +4.6 | 9e-05 | 16/48 (SW 900, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +4.3 | 5e-04 | 15/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.001 | 11/46 (RKO, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.07× | +3.4 | 0.015 | 0/49 | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.10× | +3.2 | 0.028 | 11/48 (RKO, SW 1271, …) | all doses, flat |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 1.10× | +3.0 | 0.048 | 3/49 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.09× | +2.9 | 0.059 | 6/48 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (A498 0.500×, LoVo 0.508×, SW480 0.626×, NCI-H460 0.604×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 5 lines (SW480 0.461×, H4 0.284×, A498 0.539×, LS 180 0.346×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.185×, H4 0.256×, SW480 0.484×, NCI-H1573 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -17.5 | 0e+00 | 40/49 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -12.4 | 4e-33 | 39/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.837× | -6.1 | 2e-07 | 23/50 (SW480, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.881× | -4.5 | 9e-04 | 15/48 (AsPC-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.918× | -4.4 | 0.001 | 7/48 (A498, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -4.0 | 0.006 | 12/49 (A498, SW 1271, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.899× | -3.8 | 0.011 | 17/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | 0.911× | -3.3 | 0.058 | 1/48 (LOX-IMVI) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.913× | -3.1 | 0.11 | 11/49 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.942× | -3.0 | 0.14 | 0/48 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 110 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -10.0) |
| [[LoVo (line)]] | wt | 203 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.47× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -16.8) |
| [[SW480 (line)]] | alt | 84.6 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.6) |
| [[H4 (line)]] | wt | 89.1 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.54× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.9) |
| [[A498 (line)]] | wt | 126 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -16.8) |
| [[A549 (line)]] | wt | 113 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.00× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -10.5) |
| [[LS 180 (line)]] | wt | 106 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 96.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 98.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.09× (z +10.9) | — |
| [[RKO (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.05× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 75.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.2) |
| [[A-427 (line)]] | wt | 56.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -12.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 70.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -8.9) |
| [[C32 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 98.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.94× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 91.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.52× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -10.5) |
| [[J82 (line)]] | alt | 96.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.40× (z +9.1) | — |
| [[KATO III (line)]] | alt | 92.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.87× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.30× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 83.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 91.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 107 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.04× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.468× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 89.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.1) |
| [[BT-474 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD1]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ATXN7L3]] | +0.52 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[GTF3C3]] | +0.52 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[ZNF426]] | +0.52 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[FAF2]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PLRG1]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[DDX23]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[MCRS1]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[NORAD]] | +0.50 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[POP4]] | +0.50 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ZNF510]] | +0.50 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[NRDE2]] | +0.49 | +0.37 / +0.54 | both halves | 8e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICAM5]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[OXR1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[INTS6L]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TBC1D12]] | -0.50 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[MTR]] | -0.49 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[NFKBID]] | -0.48 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[PIGX]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[KATNA1]] | -0.47 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ENY2]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[USP3]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[TAF5]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PIAS2]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BNIP2's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NMRAL2P]] | B | NMRAL2P activity raises BNIP2's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without NMRAL2P | 0.088 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[DPP8]] | C | DPP8's natural level strengthens BNIP2's drug response | DPP8's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.21; direction not clear | 0.067 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.427). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-24.2, -7.8); signed map (-9.8, -27.7). **Vector** length 96.1, 21.4% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +16.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +4.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -17.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -5.6 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | -2.9 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:59,659,146-59,689,339 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nip2, BNIP-2 |
| Gene groups (HGNC) | BCL2 family; BCH domain containing ; CRAL-TRIO lipid binding domain containing |
| Reactome | 1 pathways, smallest: Myogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12982](https://www.uniprot.org/uniprotkb/Q12982) (BCL2/adenovirus E1B 19 kDa protein-interacting protein 2):

> Implicated in the suppression of cell death. Interacts with the BCL-2 and adenovirus E1B 19 kDa proteins.

**Summary**, from NCBI Gene [663](https://www.ncbi.nlm.nih.gov/gene/663):

> This gene is a member of the BCL2/adenovirus E1B 19 kd-interacting protein (BNIP) family. It interacts with the E1B 19 kDa protein, which protects cells from virally-induced cell death. The encoded protein also interacts with E1B 19 kDa-like sequences of BCL2, another apoptotic protector. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:1083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1083) · Entrez [663](https://www.ncbi.nlm.nih.gov/gene/663) · UniProt [Q12982](https://www.uniprot.org/uniprotkb/Q12982) · Ensembl [ENSG00000140299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140299)

## Data

Gene col 6387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6387); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6387]; `tensor/DDL_lfc|DDL_z.npy` [6387]; `embed/gene_vectors.npy` [6387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6387 or target_col == 6387). Every well: [[BNIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
