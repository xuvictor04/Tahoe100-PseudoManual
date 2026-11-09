---
symbol: "RAI14"
type: "gene"
col: 463
ensembl_id: "ENSG00000039560"
name: "retinoic acid induced 14"
location: "5p13.2"
module: 81
arm: "+"
pooled_cpm: 303.08
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 22
direction_downstream: 18
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# RAI14

*retinoic acid induced 14* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.48× (z +7.7, q 1e-11, up in 15 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[BAY1125976 (drug)]] 5 µM: 1.46× (z +4.0, q 0.017, up in 22 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 3.67×, NCI-H23 3.30×, A-427 2.70×, NCI-H2030 2.27×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 3.18×, NCI-H23 2.92×, A-427 2.13×, HT-29 2.20×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (C32 2.52×, CHP-212 2.33×); [[Peretinoin (drug)]] 5 µM in 1 line (C32 3.29×); [[Peretinoin (drug)]] 0.5 µM in 1 line (C32 3.00×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.423× (z -24.6, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A51]] (+0.65, fdr 1e-05), [[VEGFC]] (+0.64, fdr 7e-06), [[ITGA2]] (+0.63, fdr 7e-06); moves opposite to [[ZBED3]] (-0.48, fdr 4e-05), [[EDN2]] (-0.48, fdr 3e-05), [[JDP2]] (-0.48, fdr 5e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[EDNRA]] → it (grade B ⚠); 18 go from it, the strongest it → [[OSMR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 463.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 3.67×, NCI-H23 3.30×, A-427 2.70×, NCI-H2030 2.27×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 3.18×, NCI-H23 2.92×, A-427 2.13×, HT-29 2.20×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (C32 2.52×, CHP-212 2.33×); [[Peretinoin (drug)]] 5 µM in 1 line (C32 3.29×); [[Peretinoin (drug)]] 0.5 µM in 1 line (C32 3.00×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +7.7 | 1e-11 | 15/34 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.017 | 22/37 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.8 | 0.030 | 12/37 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.13× | +3.6 | 0.039 | 15/38 (LOX-IMVI, CFPAC-1, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.039 | 17/37 (LOX-IMVI, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.047 | 15/38 (LoVo, NCI-H23, …) | rises with dose | composition shift |
| [[Clotrimazole (drug)]] 5 µM |  | 1.13× | +3.4 | 0.049 | 8/38 (BT-474, RPMI-7951, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.4 | 0.049 | 16/37 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.058 | 11/36 (J82, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.067 | 16/37 (LOX-IMVI, BT-474, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.14 | 14/37 (C32, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -24.6 | 0e+00 | 34/37 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -23.8 | 0e+00 | 32/38 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -21.6 | 0e+00 | 36/37 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.421×** | -17.5 | 0e+00 | 36/37 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.517×** | -13.3 | 2e-38 | 35/37 (Hs 766T, A549, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.513×** | -13.0 | 2e-36 | 27/36 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -9.5 | 2e-19 | 29/37 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -9.0 | 1e-17 | 29/37 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -8.8 | 6e-17 | 31/38 (A549, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -8.6 | 3e-16 | 28/37 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -8.5 | 1e-15 | 26/37 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.668×** | -8.1 | 2e-14 | 31/37 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.686×** | -7.3 | 1e-11 | 25/37 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.699×** | -7.2 | 2e-11 | 32/38 (SW 900, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -6.7 | 1e-09 | 24/37 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -6.2 | 2e-08 | 28/37 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -5.8 | 2e-07 | 21/37 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 217 | 0 | 24 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.145× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 438 | 0 | 16 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -23.1) |
| [[HOP62 (line)]] | alt | 803 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -26.5) |
| [[J82 (line)]] | alt | 895 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -29.6) |
| [[A549 (line)]] | wt | 558 | 0 | 15 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0937× (z -25.4) |
| [[AsPC-1 (line)]] | alt | 164 | 0 | 13 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -15.2) |
| [[SW 900 (line)]] | alt | 645 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -22.5) |
| [[hTERT-HPNE (line)]] | wt | 849 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 424 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -25.8) |
| [[A498 (line)]] | wt | 1,089 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -24.2) |
| [[CFPAC-1 (line)]] | alt | 384 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -25.7) |
| [[NCI-H460 (line)]] | wt | 145 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -22.8) |
| [[HS-578T (line)]] | alt | 260 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -21.8) |
| [[SNU-423 (line)]] | alt | 609 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -20.8) |
| [[Hs 766T (line)]] | wt | 892 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0846× (z -30.1) |
| [[NCI-H1792 (line)]] | alt | 744 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -28.3) |
| [[A-172 (line)]] | wt | 468 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -24.4) |
| [[NCI-H2347 (line)]] | alt | 396 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.4) |
| [[RKO (line)]] | wt | 167 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -17.9) |
| [[A-427 (line)]] | wt | 197 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +13.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.511× (z -9.4) |
| [[C32 (line)]] | wt | 98.8 | 5 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.52× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 301 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.3) |
| [[LoVo (line)]] | wt | 98.7 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.47× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 137 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 150 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -12.8) |
| [[CHP-212 (line)]] | wt | 207 | 1 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.33× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.3) |
| [[HT-29 (line)]] | alt | 127 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.455× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 192 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.9) |
| [[H4 (line)]] | wt | 243 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.305× (z -9.8) |
| [[SW 1271 (line)]] | alt | 271 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.0) |
| [[SW48 (line)]] | wt | 94.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.7) |
| [[C-33 A (line)]] | alt | 121 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.460× (z -9.6) |
| [[SW 1088 (line)]] | alt | 532 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.5) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 60.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 65.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 72.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 73.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A51]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[VEGFC]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ITGA2]] | +0.63 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[CD44]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[BZW1]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[LOXL2]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[GLIS3]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[AADACP1]] | +0.53 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[STK10]] | +0.53 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[AADAC]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED3]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[EDN2]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[JDP2]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PDPR]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[LINC01748]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[NEBL]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ANK3]] | -0.46 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[LINC01133]] | -0.45 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[IGFL2-AS1]] | -0.45 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[PUM2]] | -0.45 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[EPHX2]] | -0.45 | -0.48 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDNRA]] | B | EDNRA activity raises RAI14's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 3.79× lower at baseline in the lines without EDNRA | 0.003 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[FRMD6]] | B | FRMD6 activity raises RAI14's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.78× lower at baseline in the lines without FRMD6 | 0.005 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[LINC01748]] | B | LINC01748 activity lowers RAI14's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 2.97× higher at baseline in the lines without LINC01748 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |
| [[CD59]] | B | CD59 activity raises RAI14's level | lines that do not express CD59 (7) vs lines expressing it (43) | 3.05× lower at baseline in the lines without CD59 | 0.020 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[GFPT2]] | B | GFPT2 activity raises RAI14's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.86× lower at baseline in the lines without GFPT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[MIR100HG]] | B | MIR100HG activity raises RAI14's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 3.40× lower at baseline in the lines without MIR100HG | 0.036 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[VSTM4]] | B | VSTM4 activity raises RAI14's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without VSTM4 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[ARHGAP22]] | B | ARHGAP22 activity raises RAI14's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.92× lower at baseline in the lines without ARHGAP22 | 0.038 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[COL5A1]] | B | COL5A1 activity raises RAI14's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without COL5A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[OSMR]] | B | OSMR activity raises RAI14's level | lines that do not express OSMR (13) vs lines expressing it (37) | 3.50× lower at baseline in the lines without OSMR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1; its own permutation p |
| [[ADAMTS12]] | B | ADAMTS12 activity raises RAI14's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without ADAMTS12 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[ADAM12]] | B | ADAM12 activity raises RAI14's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 3.22× lower at baseline in the lines without ADAM12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSMR]] | B | RAI14 activity raises OSMR's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 4.57× lower at baseline in the lines without RAI14 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[ITGA2]] | B | RAI14 activity raises ITGA2's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without RAI14 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[CD59]] | B | RAI14 activity raises CD59's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without RAI14 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[HRH1]] | B | RAI14 activity raises HRH1's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without RAI14 | 0.016 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[LINC01748]] | B | RAI14 activity lowers LINC01748's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 5.72× higher at baseline in the lines without RAI14 | 0.023 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[TBILA]] | B | RAI14 activity raises TBILA's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without RAI14 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[STK10]] | B | RAI14 activity raises STK10's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without RAI14 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[BACH1]] | B | RAI14 activity raises BACH1's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without RAI14 | 0.042 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[RPSAP52]] | B | RAI14 activity raises RPSAP52's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 3.12× lower at baseline in the lines without RAI14 | 0.043 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[MOCS2-DT]] | B | RAI14 activity raises MOCS2-DT's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without RAI14 | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[BMAL2]] | B | RAI14 activity raises BMAL2's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without RAI14 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[F3]] | B | RAI14 activity raises F3's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without RAI14 | 0.049 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.0, 15.9); signed map (21.2, 50.2). **Vector** length 125, 43.6% of its response variance represented; |z| ≥ 3 in 1,663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | -13.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | -8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | -21.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -6.0 | -8.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.1 | -13.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | retinoic acid induced 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:34,656,328-34,832,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NORPEG, KIAA1334, RAI13, DKFZp564G013 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0K7](https://www.uniprot.org/uniprotkb/Q9P0K7) (Ankycorbin):

> Plays a role in actin regulation at the ectoplasmic specialization, a type of cell junction specific to testis. Important for establishment of sperm polarity and normal spermatid adhesion. May also promote integrity of Sertoli cell tight junctions at the blood-testis barrier.

**Summary**, from NCBI Gene [26064](https://www.ncbi.nlm.nih.gov/gene/26064):

> Predicted to enable actin binding activity. Predicted to be involved in cell differentiation and spermatogenesis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14873) · Entrez [26064](https://www.ncbi.nlm.nih.gov/gene/26064) · UniProt [Q9P0K7](https://www.uniprot.org/uniprotkb/Q9P0K7) · Ensembl [ENSG00000039560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039560)

## Data

Gene col 463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 463); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 463]; `tensor/DDL_lfc|DDL_z.npy` [463]; `embed/gene_vectors.npy` [463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 463 or target_col == 463). Every well: [[RAI14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAI14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
