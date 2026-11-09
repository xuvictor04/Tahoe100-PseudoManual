---
symbol: "SNX4"
type: "gene"
col: 3561
ensembl_id: "ENSG00000114520"
name: "sorting nexin 4"
location: "3q21.2"
module: 171
arm: "+"
pooled_cpm: 95.8
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# SNX4

*sorting nexin 4* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.73× (z +10.3, q 6e-22, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.652× (z -11.6, q 2e-28, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.641× (z -8.7, q 1e-15, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS35]] (+0.78, fdr 7e-06), [[RTCA]] (+0.77, fdr 7e-06), [[ALG9]] (+0.74, fdr 7e-06); moves opposite to [[KDM6B]] (-0.64, fdr 1e-05), [[SSUH2]] (-0.63, fdr 7e-06), [[TUT7]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +10.3 | 6e-22 | 44/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +8.5 | 6e-15 | 38/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +6.7 | 6e-09 | 37/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.23×** | +5.7 | 1e-06 | 24/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +5.4 | 7e-06 | 35/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.1 | 3e-05 | 28/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +5.0 | 6e-05 | 32/48 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.040 | 18/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.046 | 22/47 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.17× | +3.1 | 0.097 | 14/49 (hTERT-HPNE, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.11 | 17/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.652×** | -11.6 | 2e-28 | 31/48 (SNU-423, RPMI-7951, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.641×** | -8.7 | 1e-15 | 39/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -7.7 | 4e-12 | 30/49 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -7.3 | 6e-11 | 39/48 (SNU-423, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.706×** | -6.8 | 1e-09 | 29/49 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.701×** | -6.7 | 3e-09 | 28/44 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.714×** | -6.6 | 4e-09 | 30/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -5.6 | 2e-06 | 0/50 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.736×** | -5.5 | 2e-06 | 25/45 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -5.3 | 6e-06 | 26/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.762×** | -5.1 | 2e-05 | 25/50 (A-172, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -4.1 | 0.002 | 27/49 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.808×** | -4.1 | 0.002 | 24/48 (PANC-1, HOP62, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.828×** | -3.7 | 0.010 | 19/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.026 | 17/48 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.027 | 15/48 (CHP-212, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.034 | 13/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.853× | -3.1 | 0.056 | 20/48 (SW 1271, Hs 766T, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.892× | -3.1 | 0.056 | 5/48 (NCI-H23, A498, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.808×** | -3.0 | 0.073 | 18/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.863× | -2.9 | 0.095 | 12/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.864× | -2.8 | 0.095 | 12/48 (A-427, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 160 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -18.3) |
| [[SW480 (line)]] | alt | 92.9 | 4 (2 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 157 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -13.2) |
| [[RKO (line)]] | wt | 82.2 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.77× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.2) |
| [[A-427 (line)]] | wt | 110 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.56× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 79.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 90.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 185 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.60× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -12.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.461× (z -8.7) |
| [[PANC-1 (line)]] | alt | 71.5 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.94× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.626× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -13.0) |
| [[SNU-423 (line)]] | alt | 81.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -10.4) |
| [[SW1417 (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[AsPC-1 (line)]] | alt | 53.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.5) |
| [[HS-578T (line)]] | alt | 118 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 63.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 89.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[LoVo (line)]] | wt | 64.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.05× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 79.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.36× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 67.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 85.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 84.7 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.143× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[Hs 766T (line)]] | wt | 68.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 57.2 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.01× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 68.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 96.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0956× (z -8.7) |
| [[SW 900 (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 98.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS35]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[RTCA]] | +0.77 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[ALG9]] | +0.74 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MBD2]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.70 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SEC24B]] | +0.69 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[NDFIP1]] | +0.69 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CDADC1]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ASB7]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.68 | +0.80 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM6B]] | -0.64 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TUT7]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[PPP1R10]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[MCL1]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[EGR1]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[THOC6]] | -0.60 | -0.67 / -0.40 | both halves | 4e-05 |  |
| [[EGR3]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[AGO2]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGR2]] | B | EGR2 activity lowers SNX4's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without EGR2 | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF738]] | B | ZNF738 activity raises SNX4's level | lines that do not express ZNF738 (9) vs lines expressing it (41) | 1.21× lower at baseline in the lines without ZNF738 | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF493, ENSG00000269237, ZNF66 |
| [[PSMB5]] | B | PSMB5 activity lowers SNX4's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-4.3, -11.8); signed map (-32.5, -11.4). **Vector** length 115, 35.9% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +10.5 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.6 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +10.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -8.3 | -11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -6.3 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -5.4 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.6 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:125,446,650-125,520,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATG24B |
| Gene groups (HGNC) | Sorting nexins; Autophagy related; PX-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95219](https://www.uniprot.org/uniprotkb/O95219) (Sorting nexin-4):

> Involved in the regulation of endocytosis and in several stages of intracellular trafficking. Plays a role in recycling endocytosed transferrin receptor and prevent its degradation. Involved in autophagosome assembly by regulating trafficking and recycling of phospholipid scramblase ATG9A.

**Summary**, from NCBI Gene [8723](https://www.ncbi.nlm.nih.gov/gene/8723):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein associated with the long isoform of the leptin receptor and with receptor tyrosine kinases for platelet-derived growth factor, insulin, and epidermal growth factor in cell cultures, but its function is unknown. This protein may form oligomeric complexes with family members. Two …

**Accessions** — [HGNC:11175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11175) · Entrez [8723](https://www.ncbi.nlm.nih.gov/gene/8723) · UniProt [O95219](https://www.uniprot.org/uniprotkb/O95219) · Ensembl [ENSG00000114520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114520)

## Data

Gene col 3561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3561); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3561]; `tensor/DDL_lfc|DDL_z.npy` [3561]; `embed/gene_vectors.npy` [3561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3561 or target_col == 3561). Every well: [[SNX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
