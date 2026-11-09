---
symbol: "GTF3C4"
type: "gene"
col: 4623
ensembl_id: "ENSG00000125484"
name: "general transcription factor IIIC subunit 4"
location: "9q34.13"
module: 7
arm: "+"
pooled_cpm: 40.25
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# GTF3C4

*general transcription factor IIIC subunit 4* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.42× (z +21.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.634× (z -10.2, q 1e-21, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.876× (z -4.2, q 0.005, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SHP-77 0.204×, MIA PaCa-2 0.241×, HEC-1-A 0.290×, RKO 0.385×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 0.132×, SW 900 0.129×, NCI-H1792 0.296×, A498 0.472×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.0851×, HOP62 0.106×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBLL1]] (+0.83, fdr 7e-06), [[ZBTB6]] (+0.79, fdr 7e-06), [[SMG8]] (+0.79, fdr 7e-06); moves opposite to [[CBFA2T2]] (-0.64, fdr 2e-05), [[C1QL1]] (-0.61, fdr 1e-04), [[TMEM50B]] (-0.60, fdr 8e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AKT1]], [[AKT2]], [[AKT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.42×** | +21.7 | 0e+00 | 48/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +20.1 | 0e+00 | 40/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +17.2 | 0e+00 | 44/48 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +14.7 | 0e+00 | 45/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +14.4 | 8e-45 | 39/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +12.6 | 2e-34 | 43/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +11.3 | 1e-27 | 37/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +11.2 | 3e-27 | 38/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +10.6 | 2e-24 | 44/48 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +10.2 | 1e-22 | 40/48 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +9.8 | 9e-21 | 35/48 (SW480, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +8.6 | 5e-16 | 36/48 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +7.9 | 1e-13 | 31/48 (BT-474, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +7.2 | 2e-11 | 30/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 2e-08 | 27/48 (HT-29, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.1 | 1e-05 | 21/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +4.2 | 8e-04 | 13/48 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4623.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SHP-77 0.204×, MIA PaCa-2 0.241×, HEC-1-A 0.290×, RKO 0.385×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 0.132×, SW 900 0.129×, NCI-H1792 0.296×, A498 0.472×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 2 lines (HEC-1-A 0.0851×, HOP62 0.106×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.634×** | -10.2 | 1e-21 | 37/48 (SHP-77, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -9.2 | 7e-18 | 26/40 (A549, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.2 | 0.005 | 15/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.837× | -3.8 | 0.017 | 14/47 (RKO, NCI-H1573, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.803×** | -3.5 | 0.051 | 16/48 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.076 | 12/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 49.2 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.3) | [[Lonafarnib (drug)]] 5 µM 0.0851× (z -14.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 36.6 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.92× (z +10.5) | — |
| [[A549 (line)]] | wt | 35.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +22.2) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 46.1 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 30.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.0) | [[Lonafarnib (drug)]] 5 µM 0.106× (z -11.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 28.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.16× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.6 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.84× (z +13.8) | — |
| [[A-172 (line)]] | wt | 51.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +17.7) | — |
| [[A498 (line)]] | wt | 58.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.472× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 35.4 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 38.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 60.8 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.10× (z +12.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.379× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.68× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -14.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 101 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.58× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 37.5 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.79× (z +9.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.2) | — |
| [[J82 (line)]] | alt | 63.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.89× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 59.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.31× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 46.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 33.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.75× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 56.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.5) | — |
| [[LoVo (line)]] | wt | 35.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.76× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.41× (z +8.7) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLL1]] | +0.83 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[SMG8]] | +0.79 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[DDX20]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.75 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.73 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[TACO1]] | +0.72 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.72 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FEM1A]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[METTL13]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MRM3]] | +0.70 | +0.59 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.64 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[C1QL1]] | -0.61 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[TMEM50B]] | -0.60 | -0.58 / -0.61 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT1]], [[AKT2]], [[AKT3]] | B | AKT1, AKT2, AKT3 activity raises GTF3C4's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.1, 11.0); signed map (-1.5, -26.6). **Vector** length 107, 27.2% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +21.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +12.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.6 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +17.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +3.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.3 | -10.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -9.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | +0.7 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIC subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,670,035-132,694,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIIC90, KAT12 |
| Gene groups (HGNC) | Lysine acetyltransferases; General transcription factor IIIC complex subunits |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKN8](https://www.uniprot.org/uniprotkb/Q9UKN8) (General transcription factor 3C polypeptide 4):

> Essential for RNA polymerase III to make a number of small nuclear and cytoplasmic RNAs, including 5S RNA, tRNA, and adenovirus-associated (VA) RNA of both cellular and viral origin. Has histone acetyltransferase activity (HAT) with unique specificity for free and nucleosomal H3. May cooperate with GTF3C5 in facilitating the recruitment of TFIIIB and RNA polymerase through direct interactions with BRF1, POLR3C and POLR3F. May be localized close to the A box.

**Summary**, from NCBI Gene [9329](https://www.ncbi.nlm.nih.gov/gene/9329):

> Enables RNA polymerase III general transcription initiation factor activity and histone H3K14 acetyltransferase activity. Involved in transcription initiation at RNA polymerase III promoter. Located in nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4667) · Entrez [9329](https://www.ncbi.nlm.nih.gov/gene/9329) · UniProt [Q9UKN8](https://www.uniprot.org/uniprotkb/Q9UKN8) · Ensembl [ENSG00000125484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125484)

## Data

Gene col 4623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4623); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4623]; `tensor/DDL_lfc|DDL_z.npy` [4623]; `embed/gene_vectors.npy` [4623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4623 or target_col == 4623). Every well: [[GTF3C4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
