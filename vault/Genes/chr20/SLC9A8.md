---
symbol: "SLC9A8"
type: "gene"
col: 12470
ensembl_id: "ENSG00000197818"
name: "solute carrier family 9 member A8"
location: "20q13.13"
module: 68
arm: "+"
pooled_cpm: 58.64
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# SLC9A8

*solute carrier family 9 member A8* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.47× (z +23.3, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.490× (z -13.0, q 6e-36, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK1IP1L]] (+0.75, fdr 7e-06), [[PATL2]] (+0.74, fdr 1e-05), [[RAB30-DT]] (+0.74, fdr 1e-05); moves opposite to [[WASF3]] (-0.76, fdr 7e-06), [[POGLUT2]] (-0.71, fdr 1e-05), [[GMCL1]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC6A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +23.3 | 0e+00 | 45/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +12.5 | 3e-33 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +10.4 | 3e-23 | 41/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.60×** | +4.5 | 0.001 | 26/49 (Hs 766T, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +4.3 | 0.002 | 19/49 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 21/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +4.1 | 0.003 | 26/47 (NCI-H460, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.004 | 22/47 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.004 | 17/49 (AsPC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.005 | 16/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.7 | 0.012 | 21/47 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.6 | 0.016 | 17/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.042 | 19/47 (NCI-H460, RKO, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.2 | 0.045 | 14/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.045 | 20/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.490×** | -13.0 | 6e-36 | 45/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.498×** | -12.7 | 1e-34 | 46/48 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.525×** | -11.7 | 2e-29 | 44/48 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -11.5 | 3e-28 | 37/47 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.601×** | -9.3 | 2e-18 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.618×** | -8.8 | 2e-16 | 33/49 (RKO, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.615×** | -8.5 | 1e-15 | 29/39 (Hs 766T, NCI-H1792, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.659×** | -7.6 | 2e-12 | 34/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **0.761×** | -5.0 | 4e-05 | 27/46 (LS 180, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.634×** | -4.4 | 8e-04 | 23/49 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.649×** | -4.1 | 0.002 | 22/48 (Panc 03.27, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.691×** | -3.5 | 0.020 | 20/49 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.829×** | -3.3 | 0.042 | 21/49 (A-427, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.709×** | -3.3 | 0.042 | 17/42 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.838× | -3.2 | 0.049 | 17/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.2 | 9 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +31.7) | [[Belinostat (drug)]] 5 µM 0.378× (z -11.4) |
| [[PANC-1 (line)]] | alt | 43.9 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +25.7) | [[Panobinostat (drug)]] 5 µM 0.399× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 75.9 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.300× (z -11.5) |
| [[A-172 (line)]] | wt | 59.7 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 73.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -12.0) |
| [[SW480 (line)]] | alt | 62.5 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.420× (z -11.3) |
| [[COLO 205 (line)]] | alt | 164 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.242× (z -13.4) |
| [[HT-29 (line)]] | alt | 108 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -12.2) |
| [[J82 (line)]] | alt | 128 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.352× (z -11.0) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.442× (z -9.0) |
| [[A-427 (line)]] | wt | 33.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +14.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A498 (line)]] | wt | 46.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +20.7) | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +21.2) | [[Belinostat (drug)]] 5 µM 0.350× (z -8.9) |
| [[RKO (line)]] | wt | 83.7 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -12.7) |
| [[SNU-1 (line)]] | wt | 58.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SNU-423 (line)]] | alt | 61.5 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -9.2) |
| [[A549 (line)]] | wt | 68.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -11.5) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -9.1) |
| [[BT-474 (line)]] | alt | 94.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +21.7) | — |
| [[HepG2_C3A (line)]] | wt | 48.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[Hs 766T (line)]] | wt | 126 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.0747× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H23 (line)]] | alt | 58.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.399× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 30.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 67.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -9.0) |
| [[C-33 A (line)]] | alt | 43.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.8) | [[Belinostat (drug)]] 0.5 µM 0.283× (z -8.6) |
| [[HOP62 (line)]] | alt | 43.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 47.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +16.8) | — |
| [[LoVo (line)]] | wt | 38.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 72.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -13.0) |
| [[SW48 (line)]] | wt | 42.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 60.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 42.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK1IP1L]] | +0.75 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[PATL2]] | +0.74 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.74 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.73 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.71 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FKRP]] | +0.71 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.70 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.70 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.69 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.69 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[OCIAD1]] | +0.69 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | +0.69 | +0.69 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.76 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[POGLUT2]] | -0.71 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.71 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[PAPSS1]] | -0.70 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ATRN]] | -0.69 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[METAP1]] | -0.67 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[SETD3]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[HACE1]] | -0.66 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[GRB2]] | -0.66 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[GLG1]] | -0.66 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[KIAA1958]] | -0.64 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.64 | -0.61 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A7]] | B | SLC6A7 activity raises SLC9A8's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.31× lower at baseline in the lines without SLC6A7 | 0.090 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[ZDHHC1]] | C | ZDHHC1 activity lowers SLC9A8's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without ZDHHC1 | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.783). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.2, 7.1); signed map (18.0, -24.0). **Vector** length 128, 39.6% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +13.5 | +23.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.3 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.1 | +12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.9 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.1 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.9 | -9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.6 | -13.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.8 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,812,713-49,892,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0939, NHE8 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 4 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2E8](https://www.uniprot.org/uniprotkb/Q9Y2E8) (Sodium/hydrogen exchanger 8):

> Na(+)/H(+) antiporter. Mediates the electoneutral exchange of intracellular H(+) ions for extracellular Na(+) in 1:1 stoichiometry. Acts as an Na(+)/H(+) exchanger in the trans-Golgi. Contributes to the regulation of pH regulation of Golgi apparatus, and consequently, in protein trafficking and endosomal morphology. In germ cells, plays a crucial role in acrosome biogenesis and sperm development, probably by playing a role in the fusion of the Golgi-derived vesicles that form the acrosomal cap …

**Summary**, from NCBI Gene [23315](https://www.ncbi.nlm.nih.gov/gene/23315):

> Sodium-hydrogen exchangers (NHEs), such as SLC9A8, are integral transmembrane proteins that exchange extracellular Na+ for intracellular H+. NHEs have multiple functions, including intracellular pH homeostasis, cell volume regulation, and electroneutral NaCl absorption in epithelia (Xu et al., 2008 [PubMed 18209477]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:20728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20728) · Entrez [23315](https://www.ncbi.nlm.nih.gov/gene/23315) · UniProt [Q9Y2E8](https://www.uniprot.org/uniprotkb/Q9Y2E8) · Ensembl [ENSG00000197818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197818)

## Data

Gene col 12470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12470); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12470]; `tensor/DDL_lfc|DDL_z.npy` [12470]; `embed/gene_vectors.npy` [12470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12470 or target_col == 12470). Every well: [[SLC9A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
