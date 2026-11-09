---
symbol: "OBSCN"
type: "gene"
col: 7801
ensembl_id: "ENSG00000154358"
name: "obscurin, cytoskeletal calmodulin and titin-interacting RhoGEF"
location: "1q42.13"
module: 136
arm: "+"
pooled_cpm: 48.33
n_lines_expressing: 41
n_dd_up: 0
n_dd_down: 43
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# OBSCN

*obscurin, cytoskeletal calmodulin and titin-interacting RhoGEF* — 1q42.13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 4.17×, BT-474 4.65×, LoVo 3.09×; ⚠ cell-cycle shift, explains ~21% of this change).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.317× (z -19.3, q 0e+00, down in 35 of 38 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.225× (z -12.8, q 4e-35, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTSR1]] (+0.56, fdr 3e-05), [[CACNA1B]] (+0.53, fdr 3e-05), [[UNC13A]] (+0.50, fdr 1e-04); moves opposite to [[RASSF6]] (-0.50, fdr 1e-05), [[SRI]] (-0.49, fdr 1e-04), [[PIP5K1B]] (-0.49, fdr 3e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PYURF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LS 180 4.17×, BT-474 4.65×, LoVo 3.09×; ⚠ cell-cycle shift, explains ~21% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Omeprazole (drug)]] 0.05 µM |  | 1.35× | +3.5 | 0.16 | 17/39 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.23× | +3.4 | 0.16 | 16/39 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.30× | +3.1 | 0.36 | 12/40 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.317×** | -19.3 | 0e+00 | 35/38 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.225×** | -12.8 | 4e-35 | 37/39 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.342×** | -12.7 | 6e-35 | 36/38 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.383×** | -11.4 | 5e-28 | 37/39 (H4, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.423×** | -10.2 | 2e-22 | 32/38 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.478×** | -8.8 | 2e-16 | 30/39 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.370×** | -8.5 | 1e-15 | 29/37 (NCI-H2030, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.495×** | -8.3 | 5e-15 | 30/39 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.505×** | -8.1 | 3e-14 | 30/39 (H4, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -8.0 | 1e-13 | 32/39 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.319×** | -7.1 | 6e-11 | 28/40 (CFPAC-1, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.556×** | -7.0 | 2e-10 | 27/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -6.9 | 2e-10 | 29/39 (CFPAC-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.572×** | -6.6 | 1e-09 | 26/39 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.454×** | -6.3 | 9e-09 | 29/39 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.612×** | -5.8 | 2e-07 | 30/39 (NCI-H1792, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.521×** | -5.6 | 6e-07 | 25/40 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.629×** | -5.5 | 1e-06 | 25/39 (LOX-IMVI, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -4.8 | 3e-05 | 25/39 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -4.5 | 2e-04 | 24/39 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.524×** | -4.0 | 0.001 | 24/39 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.740×** | -3.6 | 0.007 | 19/39 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.669×** | -3.2 | 0.023 | 14/39 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 94.2 | 0 | 12 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.308× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 70.5 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.233× (z -10.5) |
| [[A-172 (line)]] | wt | 154 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -24.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 144 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -30.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -16.0) |
| [[H4 (line)]] | wt | 77.7 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0771× (z -15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.184× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 78.8 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0931× (z -13.8) |
| [[PANC-1 (line)]] | alt | 28.5 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -13.6) |
| [[SNU-1 (line)]] | wt | 75.2 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -20.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.130× (z -9.4) |
| [[HCT15 (line)]] | alt | 138 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.165× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 56.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.155× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 85.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -11.2) |
| [[A-427 (line)]] | wt | 40.3 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 87.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0629× (z -27.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0778× (z -12.8) |
| [[BT-474 (line)]] | alt | 19.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +10.0) ⚠ cell-cycle shift, explains ~21% of this change | [[Digitoxin (drug)]] 0.5 µM 0.120× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 30.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -13.3) |
| [[SW 900 (line)]] | alt | 99.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -8.7) |
| [[SW480 (line)]] | alt | 27.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.135× (z -12.1) |
| [[A498 (line)]] | wt | 72.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 74.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -9.9) |
| [[J82 (line)]] | alt | 32.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.301× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 58.6 | 0 | 2 | — | [[Tazarotene (drug)]] 0.5 µM 0.0763× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0757× (z -23.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.108× (z -10.2) |
| [[CHP-212 (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 12.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.8) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[LS 180 (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.4) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -15.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW48 (line)]] | wt | 71.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -9.2) |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTSR1]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CACNA1B]] | +0.53 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[UNC13A]] | +0.50 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[PNKP]] | +0.50 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[LINC01237]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[PDE2A]] | +0.49 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[FAM85B]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[PAQR5]] | +0.49 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[EHBP1L1]] | +0.48 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SLCO4A1]] | +0.48 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[KNDC1]] | +0.48 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[CELF5]] | +0.48 | +0.34 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF6]] | -0.50 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SRI]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[PIP5K1B]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DHX29]] | -0.47 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ATP10B]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PLAAT4]] | -0.46 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[CEPT1]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MPPE1]] | -0.45 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[C4orf19]] | -0.45 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[UGT1A8]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[FRK]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 | same gene group |
| [[UGT1A6]] | -0.44 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYURF]] | B | OBSCN activity lowers PYURF's level | lines that do not express OBSCN (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without OBSCN | 0.035 | ⚠ within organs, on part of the lines; also absent: MAP3K21, C1orf115, CAMK1D; maybe low, not absent |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.9, 37.2); signed map (-9.0, 41.5). **Vector** length 88.6, 24.9% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +4.9 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +3.9 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | obscurin, cytoskeletal calmodulin and titin-interacting RhoGEF |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:228,208,044-228,378,876 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1556, UNC89, KIAA1639, ARHGEF30 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Dbl family Rho GEFs; Myosin light chain kinase family; SH3 domain containing |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; RHOQ GTPase cycle; G alpha (12/13) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VST9](https://www.uniprot.org/uniprotkb/Q5VST9) (Obscurin):

> Structural component of striated muscles which plays a role in myofibrillogenesis. Probably involved in the assembly of myosin into sarcomeric A bands in striated muscle. Has serine/threonine protein kinase activity and phosphorylates N-cadherin CDH2 and sodium/potassium-transporting ATPase subunit ATP1B1 (By similarity). Binds (via the PH domain) strongly to phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4)P2) and phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2), and to a lesser extent …

**Summary**, from NCBI Gene [84033](https://www.ncbi.nlm.nih.gov/gene/84033):

> The obscurin gene spans more than 150 kb, contains over 80 exons and encodes a protein of approximately 720 kDa. The encoded protein contains 68 Ig domains, 2 fibronectin domains, 1 calcium/calmodulin-binding domain, 1 RhoGEF domain with an associated PH domain, and 2 serine-threonine kinase domains. This protein belongs to the family of giant sacromeric signaling proteins that includes titin and nebulin, and may have a role in the organization of myofibrils during assembly and may mediate …

**Accessions** — [HGNC:15719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15719) · Entrez [84033](https://www.ncbi.nlm.nih.gov/gene/84033) · UniProt [Q5VST9](https://www.uniprot.org/uniprotkb/Q5VST9) · Ensembl [ENSG00000154358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154358)

## Data

Gene col 7801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7801); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7801]; `tensor/DDL_lfc|DDL_z.npy` [7801]; `embed/gene_vectors.npy` [7801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7801 or target_col == 7801). Every well: [[OBSCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OBSCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
