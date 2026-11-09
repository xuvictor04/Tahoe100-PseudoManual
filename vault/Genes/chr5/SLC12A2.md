---
symbol: "SLC12A2"
type: "gene"
col: 752
ensembl_id: "ENSG00000064651"
name: "solute carrier family 12 member 2"
location: "5q23.3"
module: 44
arm: "+"
pooled_cpm: 181.42
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 32
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# SLC12A2

*solute carrier family 12 member 2* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +18.5, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.795× (z -6.0, q 1e-06, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFSF15]] (+0.69, fdr 8e-06), [[TNFRSF21]] (+0.62, fdr 7e-06), [[MYB]] (+0.61, fdr 1e-05); moves opposite to [[LSP1P4]] (-0.56, fdr 3e-05), [[FLYWCH1]] (-0.56, fdr 3e-05), [[AP3S2]] (-0.55, fdr 3e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[ARHGEF38]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +18.5 | 0e+00 | 38/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +15.4 | 0e+00 | 32/46 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.05×** | +13.3 | 5e-38 | 41/47 (NCI-H460, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.83×** | +10.7 | 2e-24 | 34/41 (NCI-H1573, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.85×** | +10.5 | 6e-24 | 37/43 (HS-578T, NCI-H1573, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.6 | 9e-16 | 32/46 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.61×** | +8.4 | 3e-15 | 32/46 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.52×** | +7.8 | 5e-13 | 30/46 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.48×** | +7.2 | 4e-11 | 26/46 (A498, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.45×** | +6.9 | 3e-10 | 30/46 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +6.6 | 2e-09 | 30/46 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.5 | 4e-09 | 26/46 (A498, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.1 | 5e-08 | 26/46 (hTERT-HPNE, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.1 | 5e-08 | 25/46 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.39×** | +5.9 | 1e-07 | 26/48 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 7e-06 | 24/46 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 7e-05 | 25/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.8 | 0.005 | 13/47 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.005 | 21/46 (BT-474, Panc 03.27, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.007 | 18/46 (NCI-H23, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.014 | 14/46 (A549, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.015 | 17/47 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.032 | 13/46 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.17× | +2.9 | 0.068 | 11/46 (NCI-H1573, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -6.0 | 1e-06 | 24/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -5.8 | 2e-06 | 31/46 (COLO 205, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -5.4 | 1e-05 | 25/46 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.076 | 19/46 (SW48, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.826×** | -3.3 | 0.091 | 19/46 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.091 | 21/46 (LS 180, COLO 205, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.713×** | -3.3 | 0.091 | 15/44 (HS-578T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 1,485 | 0 | 14 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.127× (z -15.3) |
| [[COLO 205 (line)]] | alt | 567 | 0 | 13 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0795× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 72.0 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +21.4) | — |
| [[HOP62 (line)]] | alt | 79.2 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +24.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 62.3 | 9 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +26.9) | — |
| [[A498 (line)]] | wt | 47.6 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.0) | — |
| [[C32 (line)]] | wt | 118 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +23.6) | [[Bortezomib (drug)]] 0.05 µM 0.421× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 54.9 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +19.7) | — |
| [[HS-578T (line)]] | alt | 93.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +16.3) | — |
| [[HT-29 (line)]] | alt | 945 | 0 | 6 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.181× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.356× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 98.6 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 82.4 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +17.1) | — |
| [[A-427 (line)]] | wt | 112 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.6) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[HEC-1-A (line)]] | alt | 102 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +21.1) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +20.7) | — |
| [[NCI-H1573 (line)]] | alt | 144 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.9) | — |
| [[A-172 (line)]] | wt | 49.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +18.2) | — |
| [[RKO (line)]] | wt | 90.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.8) | — |
| [[AsPC-1 (line)]] | alt | 53.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +17.9) | — |
| [[NCI-H2347 (line)]] | alt | 65.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 344 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.322× (z -11.1) |
| [[A549 (line)]] | wt | 95.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[CFPAC-1 (line)]] | alt | 234 | 2 | 0 | [[Tofacitinib (drug)]] 5 µM 2.53× (z +9.7) | — |
| [[H4 (line)]] | wt | 75.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 55.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 132 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.1) | — |
| [[LoVo (line)]] | wt | 453 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.268× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 95.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 95.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 96.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 418 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.421× (z -8.6) |
| [[SW48 (line)]] | wt | 294 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -12.4) |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 172 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFSF15]] | +0.69 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[TNFRSF21]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MYB]] | +0.61 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[KCNH8]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CFTR]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_SPERMATOGENESIS; STRING 816 |
| [[LINC02331]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ARL5B]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[BCAR3-AS1]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CEMIP2]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CDH17]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ATP1B1]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 | STRING 445 |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSP1P4]] | -0.56 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[FLYWCH1]] | -0.56 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[AP3S2]] | -0.55 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[MED10]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TAB1]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CIAO3]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SHARPIN]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MKRN2]] | -0.53 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[RUFY2]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TRIP4]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PSMF1]] | -0.52 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RTCA]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 31, C 1. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF38]] | B | ARHGEF38 activity raises SLC12A2's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.22× lower at baseline in the lines without ARHGEF38 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises SLC12A2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.69× lower at baseline in the lines without ST6GALNAC1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[KCNH8]] | B | KCNH8 activity raises SLC12A2's level | lines that do not express KCNH8 (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without KCNH8 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[SLC6A14]] | B | SLC6A14 activity raises SLC12A2's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.22× lower at baseline in the lines without SLC6A14 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[MACC1]] | B | MACC1 activity raises SLC12A2's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.89× lower at baseline in the lines without MACC1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[MUC5B]] | B | MUC5B activity raises SLC12A2's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.13× lower at baseline in the lines without MUC5B | 0.012 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[CFTR]] | B | CFTR activity raises SLC12A2's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.24× lower at baseline in the lines without CFTR | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent |
| [[GPX2]] | B | GPX2 activity raises SLC12A2's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 2.65× lower at baseline in the lines without GPX2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[TOX3]] | B | TOX3 activity raises SLC12A2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without TOX3 | 0.016 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[PRR15]] | B | PRR15 activity raises SLC12A2's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without PRR15 | 0.017 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[TMPRSS2]] | B | TMPRSS2 activity raises SLC12A2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.73× lower at baseline in the lines without TMPRSS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[COL17A1]] | B | COL17A1 activity raises SLC12A2's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without COL17A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 47.0); signed map (55.8, 12.3). **Vector** length 134, 41.6% of its response variance represented; |z| ≥ 3 in 1,520 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +6.5 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.4 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.3 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +15.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.7 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +8.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.8 | +2.9 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.4 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.2 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 12 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:128,083,766-128,189,677 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NKCC1, BSC2, BSC-2, PPP1R141, CCC1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Solute carrier family 12 |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: Cation-coupled Chloride cotransporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P55011](https://www.uniprot.org/uniprotkb/P55011) (Solute carrier family 12 member 2):

> Cation-chloride cotransporter which mediates the electroneutral transport of chloride, potassium and/or sodium ions across the membrane. Plays a vital role in the regulation of ionic balance and cell volume.

**Summary**, from NCBI Gene [6558](https://www.ncbi.nlm.nih.gov/gene/6558):

> The protein encoded by this gene mediates sodium and chloride transport and reabsorption. The encoded protein is a membrane protein and is important in maintaining proper ionic balance and cell volume. This protein is phosphorylated in response to DNA damage. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:10911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10911) · Entrez [6558](https://www.ncbi.nlm.nih.gov/gene/6558) · UniProt [P55011](https://www.uniprot.org/uniprotkb/P55011) · Ensembl [ENSG00000064651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064651)

## Data

Gene col 752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 752); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 752]; `tensor/DDL_lfc|DDL_z.npy` [752]; `embed/gene_vectors.npy` [752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 752 or target_col == 752). Every well: [[SLC12A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
