---
symbol: "DLC1"
type: "gene"
col: 8997
ensembl_id: "ENSG00000164741"
name: "DLC1 Rho GTPase activating protein"
location: "8p22"
module: 120
arm: "+"
pooled_cpm: 154.23
n_lines_expressing: 36
n_dd_up: 9
n_dd_down: 40
n_dd_up_clean: 8
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# DLC1

*DLC1 Rho GTPase activating protein* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.97× (z +8.2, q 9e-14, up in 21 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.528× (z -21.0, q 0e+00, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMURF2]] (+0.69, fdr 7e-06), [[DDAH1]] (+0.68, fdr 7e-06), [[ELK3]] (+0.67, fdr 7e-06); moves opposite to [[BTN3A3]] (-0.47, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LAMA1]] → it (grade B ⚠); 4 go from it, the strongest it → [[DCBLD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +8.2 | 9e-14 | 21/35 (A-427, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.6 | 1e-08 | 17/34 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.21×** | +6.4 | 3e-08 | 16/35 (J82, A-172, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.30×** | +6.0 | 2e-07 | 20/34 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.23×** | +4.6 | 4e-04 | 15/32 (A-172, SW480, …) | rises with dose | composition shift |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 5e-04 | 14/34 (J82, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.20×** | +4.3 | 0.001 | 13/34 (J82, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.003 | 16/33 (A-172, HS-578T, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.010 | 15/34 (A-172, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.17× | +3.6 | 0.015 | 11/34 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +3.6 | 0.015 | 13/34 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.017 | 10/34 (SNU-423, SW1417, …) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 1.15× | +3.2 | 0.057 | 9/33 (KATO III, SW1417, …) | rises with dose |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.057 | 8/35 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.14× | +3.2 | 0.057 | 13/34 (HepG2/C3A, Panc 03.27, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.057 | 7/35 (A549, C32, …) | top dose only |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.059 | 6/34 (KATO III, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bexarotene (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.061 | 10/34 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Acetohexamide (drug)]] 5 µM |  | 1.09× | +3.0 | 0.075 | 2/34 (MIA PaCa-2, A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -21.0 | 0e+00 | 28/35 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -14.0 | 6e-42 | 27/34 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.587×** | -11.9 | 2e-30 | 31/33 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.635×** | -11.1 | 1e-26 | 21/36 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.627×** | -10.9 | 2e-25 | 27/33 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.707×** | -9.7 | 2e-20 | 23/34 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.664×** | -9.5 | 2e-19 | 24/35 (KATO III, HEC-1-A, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -8.7 | 2e-16 | 21/33 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.723×** | -8.6 | 7e-16 | 21/35 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.691×** | -8.3 | 8e-15 | 22/34 (HEC-1-A, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -8.2 | 1e-14 | 20/34 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -8.0 | 4e-14 | 21/34 (HepG2/C3A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.704×** | -7.5 | 2e-12 | 23/34 (HEC-1-A, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.723×** | -7.5 | 2e-12 | 22/34 (KATO III, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.725×** | -7.5 | 3e-12 | 18/33 (HEC-1-A, KATO III, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -7.4 | 4e-12 | 21/36 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 2,571 | 0 | 28 (16 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0804× (z -48.8) |
| [[HEC-1-A (line)]] | alt | 426 | 0 | 25 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -16.8) |
| [[KATO III (line)]] | alt | 173 | 0 | 22 (5 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.277× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 880 | 2 (2 ⚠) | 10 (7 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.23× (z +13.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -28.4) |
| [[LOX-IMVI (line)]] | wt | 301 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -21.1) |
| [[A-172 (line)]] | wt | 91.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.45× (z +8.5) | — |
| [[A-427 (line)]] | wt | 573 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.8) |
| [[J82 (line)]] | alt | 144 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -18.2) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 85.6 | 4 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.6) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.84× (z +8.6) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.360× (z -10.0) |
| [[CHP-212 (line)]] | wt | 286 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -10.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.5) |
| [[SW480 (line)]] | alt | 47.0 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.80× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -8.5) |
| [[A498 (line)]] | wt | 57.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.6) |
| [[LS 180 (line)]] | wt | 93.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -12.2) |
| [[SNU-423 (line)]] | alt | 106 | 1 | 2 | [[Budesonide (drug)]] 5 µM 2.37× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -13.6) |
| [[HCT15 (line)]] | alt | 143 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.1) |
| [[Hs 766T (line)]] | wt | 61.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +14.8) | — |
| [[hTERT-HPNE (line)]] | wt | 267 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 89.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 85.7 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.546× (z -14.8) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.205× (z -11.0) |
| [[SW1417 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.410× (z -8.6) |
| [[H4 (line)]] | wt | 99.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[HS-578T (line)]] | alt | 162 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.613× (z -11.0) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.346× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 222 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 227 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.6) |
| [[SW 900 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 34.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMURF2]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DDAH1]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ELK3]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CCN1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[ARHGAP18]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[CCN2]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[DOCK5]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[NF2]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[BCL2L1]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD1]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A3]] | -0.47 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA1]] | B | LAMA1 activity raises DLC1's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 2.47× lower at baseline in the lines without LAMA1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[SFTA1P]] | B | SFTA1P activity raises DLC1's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without SFTA1P | 0.013 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[MAP2K1]] | B | MAP2K1 activity raises DLC1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.6% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PALM2AKAP2]] | B | PALM2AKAP2 activity raises DLC1's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 4.04× lower at baseline in the lines without PALM2AKAP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L |
| [[LNCOG]] | B | LNCOG activity raises DLC1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without LNCOG | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[HMGA2]] | B | HMGA2 activity raises DLC1's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 3.05× lower at baseline in the lines without HMGA2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[CASC19]] | B | CASC19 activity raises DLC1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without CASC19 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[TMEM156]] | B | TMEM156 activity raises DLC1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.28× lower at baseline in the lines without TMEM156 | 0.098 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCBLD2]] | B | DLC1 activity raises DCBLD2's level | lines that do not express DLC1 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without DLC1 | 0.051 | ⚠ within organs, on part of the lines; also absent: AXL, LGALS1, VCAN |
| [[UBASH3B]] | B | DLC1 activity raises UBASH3B's level | lines that do not express DLC1 (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without DLC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: AXL, LGALS1, VCAN |
| [[ETV4]] | B | DLC1 activity raises ETV4's level | lines that do not express DLC1 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without DLC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: AXL, LGALS1, VCAN |
| [[UBASH3B]] | B | DLC1 activity strengthens UBASH3B's drug response | lines that do not express DLC1 (10) vs lines expressing it (33) | the lines without DLC1 respond 0.50× as strongly (z diff +2.33); strongest at Dinaciclib 5 µM: 1.11x vs 0.45x (z diff +5.6) | 0.093 | ⚠ within organs, on part of the lines; also absent: AXL, LGALS1, VCAN; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.6, 12.1); signed map (13.9, 41.0). **Vector** length 124, 33.3% of its response variance represented; |z| ≥ 3 in 1,529 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | +5.4 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.2 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +4.2 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -7.5 | -11.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.3 | -11.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -9.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.8 | -10.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.6 | -9.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.4 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | DLC1 Rho GTPase activating protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:13,083,361-13,604,610 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HP, ARHGAP7, STARD12, DLC-1, p122-RhoGAP |
| Gene groups (HGNC) | Rho GTPase activating proteins; StAR related lipid transfer domain containing |
| Hallmark sets | UV_RESPONSE_DN, ESTROGEN_RESPONSE_EARLY |
| Reactome | 9 pathways, smallest: RHOQ GTPase cycle; RHOB GTPase cycle; RHOC GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QB1](https://www.uniprot.org/uniprotkb/Q96QB1) (Rho GTPase-activating protein 7):

> Functions as a GTPase-activating protein for the small GTPases RHOA, RHOB, RHOC and CDC42, terminating their downstream signaling. This induces morphological changes and detachment through cytoskeletal reorganization, playing a critical role in biological processes such as cell migration and proliferation. Also functions in vivo as an activator of the phospholipase PLCD1. Active DLC1 increases cell migration velocity but reduces directionality. Required for growth factor-induced epithelial cell …

**Summary**, from NCBI Gene [10395](https://www.ncbi.nlm.nih.gov/gene/10395):

> This gene encodes a GTPase-activating protein (GAP) that is a member of the rhoGAP family of proteins which play a role in the regulation of small GTP-binding proteins. GAP family proteins participate in signaling pathways that regulate cell processes involved in cytoskeletal changes. This gene functions as a tumor suppressor gene in a number of common cancers, including prostate, lung, colorectal, and breast cancers. Multiple transcript variants due to alternative promoters and alternative …

**Accessions** — [HGNC:2897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2897) · Entrez [10395](https://www.ncbi.nlm.nih.gov/gene/10395) · UniProt [Q96QB1](https://www.uniprot.org/uniprotkb/Q96QB1) · Ensembl [ENSG00000164741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164741)

## Data

Gene col 8997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8997); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8997]; `tensor/DDL_lfc|DDL_z.npy` [8997]; `embed/gene_vectors.npy` [8997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8997 or target_col == 8997). Every well: [[DLC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
