---
symbol: "ATP8B1"
type: "gene"
col: 1330
ensembl_id: "ENSG00000081923"
name: "ATPase phospholipid transporting 8B1"
location: "18q21.31"
module: 44
arm: "+"
pooled_cpm: 102.59
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 42
direction_downstream: 45
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# ATP8B1

*ATPase phospholipid transporting 8B1* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 1.27× (z +8.9, q 4e-16, up in 20 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.448× (z -29.2, q 0e+00, down in 32 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELF3]] (+0.70, fdr 7e-06), [[TJP3]] (+0.68, fdr 7e-06), [[PLEKHG6]] (+0.68, fdr 8e-06); moves opposite to [[ZNF558]] (-0.56, fdr 1e-05), [[RBM19]] (-0.55, fdr 2e-05), [[PDK1-AS1]] (-0.52, fdr 5e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); 45 go from it, the strongest it → [[KIAA1522]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +8.9 | 4e-16 | 20/34 (AsPC-1, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +7.1 | 4e-10 | 17/34 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +5.0 | 9e-05 | 13/35 (HEC-1-A, A-172, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.37×** | +4.2 | 0.003 | 16/34 (J82, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.11× | +3.9 | 0.009 | 5/35 (BT-474, J82, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.11× | +3.9 | 0.009 | 2/35 (BT-474, CFPAC-1) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.16× | +3.9 | 0.009 | 9/34 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.009 | 10/34 (A-427, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.017 | 10/35 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.14× | +3.3 | 0.054 | 12/36 (AsPC-1, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.094 | 6/34 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.100 | 4/34 (J82, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.10 | 8/35 (BT-474, SNU-423, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.448×** | -29.2 | 0e+00 | 32/35 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.409×** | -23.0 | 0e+00 | 29/34 (LS 180, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.467×** | -19.6 | 0e+00 | 29/34 (LoVo, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -16.8 | 0e+00 | 23/34 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.530×** | -16.3 | 0e+00 | 31/34 (SHP-77, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.607×** | -12.3 | 7e-33 | 24/33 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.630×** | -11.9 | 1e-30 | 24/34 (SHP-77, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -9.9 | 3e-21 | 27/34 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -9.8 | 8e-21 | 27/34 (BT-474, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.691×** | -9.5 | 1e-19 | 22/34 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.777×** | -9.1 | 4e-18 | 20/34 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -9.1 | 4e-18 | 21/34 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.684×** | -9.0 | 1e-17 | 24/31 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.711×** | -8.7 | 1e-16 | 23/34 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.709×** | -8.5 | 8e-16 | 25/34 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -7.8 | 2e-13 | 21/34 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.740×** | -7.7 | 4e-13 | 23/34 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.735×** | -7.4 | 3e-12 | 20/34 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.740×** | -7.4 | 4e-12 | 15/34 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -7.1 | 4e-11 | 20/34 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.759×** | -7.0 | 5e-11 | 20/34 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.659×** | -5.6 | 5e-07 | 19/34 (BT-474, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.9 | 2e-05 | 16/34 (HS-578T, LS 180, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.701×** | -4.8 | 4e-05 | 19/34 (NCI-H2347, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 155 | 0 | 23 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -25.4) |
| [[SHP-77 (line)]] | alt | 333 | 0 | 18 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -31.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -21.3) |
| [[LoVo (line)]] | wt | 192 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -30.1) |
| [[COLO 205 (line)]] | alt | 226 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.7) |
| [[LS 180 (line)]] | wt | 394 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -28.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 85.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 218 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -20.2) |
| [[BT-474 (line)]] | alt | 485 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -17.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -16.7) |
| [[HS-578T (line)]] | alt | 124 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -21.6) |
| [[HT-29 (line)]] | alt | 185 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -21.9) |
| [[KATO III (line)]] | alt | 294 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -23.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -16.9) |
| [[SW48 (line)]] | wt | 124 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -18.3) |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -15.6) |
| [[SW1417 (line)]] | alt | 143 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -22.0) |
| [[hTERT-HPNE (line)]] | wt | 233 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -15.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.5) |
| [[A-427 (line)]] | wt | 42.5 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.517× (z -8.6) |
| [[SNU-423 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -10.7) |
| [[A-172 (line)]] | wt | 109 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -9.1) |
| [[A498 (line)]] | wt | 141 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.360× (z -12.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 65.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 104 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 74.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.5) |
| [[J82 (line)]] | alt | 77.7 | 1 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.07× (z +8.6) ⚠ cell-cycle shift, explains ~16% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 63.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.9) |
| [[SW 1271 (line)]] | alt | 57.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -9.1) |
| [[SW480 (line)]] | alt | 30.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.348× (z -9.9) |
| [[AN3 CA (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF3]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TJP3]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[PLEKHG6]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[NR3C2]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GALM]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CGN]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TOX3]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PIK3C2B]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[RNF43]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PLAAT3]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[IKZF2]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF558]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[RBM19]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PDK1-AS1]] | -0.52 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[EMG1]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[GHRLOS]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 40, C 2. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises ATP8B1's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 3.58× lower at baseline in the lines without NR3C2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[LNX1]] | B | LNX1 activity raises ATP8B1's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without LNX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[SHROOM3]] | B | SHROOM3 activity raises ATP8B1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without SHROOM3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[ATP1B1]] | B | ATP1B1 activity raises ATP8B1's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.80× lower at baseline in the lines without ATP1B1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[PTPRB]] | B | PTPRB activity raises ATP8B1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without PTPRB | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[ST14]] | B | ST14 activity raises ATP8B1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.53× lower at baseline in the lines without ST14 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[CLDN3]] | B | CLDN3 activity raises ATP8B1's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.15× lower at baseline in the lines without CLDN3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[FAAH2]] | B | FAAH2 activity raises ATP8B1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.69× lower at baseline in the lines without FAAH2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[PRR15L]] | B | PRR15L activity raises ATP8B1's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 3.92× lower at baseline in the lines without PRR15L | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[CDS1]] | B | CDS1 activity raises ATP8B1's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 3.24× lower at baseline in the lines without CDS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[ALOX5]] | B | ALOX5 activity raises ATP8B1's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 3.34× lower at baseline in the lines without ALOX5 | 0.021 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[MPP7]] | B | MPP7 activity raises ATP8B1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without MPP7 | 0.023 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 43, C 2. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | ATP8B1 activity raises KIAA1522's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.76× lower at baseline in the lines without ATP8B1 | 0.003 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ELF3-AS1]] | B | ATP8B1 activity raises ELF3-AS1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.88× lower at baseline in the lines without ATP8B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ST3GAL3]] | B | ATP8B1 activity lowers ST3GAL3's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.03× higher at baseline in the lines without ATP8B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TUFT1]] | B | ATP8B1 activity raises TUFT1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without ATP8B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ATP1B1]] | B | ATP8B1 activity raises ATP1B1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without ATP8B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[VIPR1]] | B | ATP8B1 activity raises VIPR1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without ATP8B1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TSPAN15]] | B | ATP8B1 activity raises TSPAN15's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without ATP8B1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TC2N]] | B | ATP8B1 activity raises TC2N's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 4.22× lower at baseline in the lines without ATP8B1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[CYP2S1]] | B | ATP8B1 activity raises CYP2S1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.44× lower at baseline in the lines without ATP8B1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[ST14]] | B | ATP8B1 activity raises ST14's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 4.88× lower at baseline in the lines without ATP8B1 | 0.017 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[MTUS1]] | B | ATP8B1 activity raises MTUS1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.55× lower at baseline in the lines without ATP8B1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[CDS1]] | B | ATP8B1 activity raises CDS1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without ATP8B1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 54.1); signed map (50.9, 4.1). **Vector** length 119, 34.8% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.53 to 4); *Aspirin ADME* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | -9.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.4 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -5.9 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -9.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -16.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 8B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:57,646,426-57,803,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIC, PFIC; previously FIC1, BRIC, PFIC1 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O43520](https://www.uniprot.org/uniprotkb/O43520) (Phospholipid-transporting ATPase IC):

> Catalytic component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of phospholipids, in particular phosphatidylcholines (PC), from the outer to the inner leaflet of the plasma membrane. May participate in the establishment of the canalicular membrane integrity by ensuring asymmetric distribution of phospholipids in the canicular membrane (By similarity). Thus may have a role in the regulation of bile acids transport into the canaliculus, uptake of …

**Summary**, from NCBI Gene [5205](https://www.ncbi.nlm.nih.gov/gene/5205):

> This gene encodes a member of the P-type cation transport ATPase family, which belongs to the subfamily of aminophospholipid-transporting ATPases. The aminophospholipid translocases transport phosphatidylserine and phosphatidylethanolamine from one side of a bilayer to another. Mutations in this gene may result in progressive familial intrahepatic cholestasis type 1 and in benign recurrent intrahepatic cholestasis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3706) · Entrez [5205](https://www.ncbi.nlm.nih.gov/gene/5205) · UniProt [O43520](https://www.uniprot.org/uniprotkb/O43520) · Ensembl [ENSG00000081923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081923)

## Data

Gene col 1330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1330); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1330]; `tensor/DDL_lfc|DDL_z.npy` [1330]; `embed/gene_vectors.npy` [1330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1330 or target_col == 1330). Every well: [[ATP8B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
