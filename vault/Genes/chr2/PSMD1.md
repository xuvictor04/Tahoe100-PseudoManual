---
symbol: "PSMD1"
type: "gene"
col: 10417
ensembl_id: "ENSG00000173692"
name: "proteasome 26S subunit, non-ATPase 1"
location: "2q37.1"
module: 36
arm: "+"
pooled_cpm: 128.54
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PSMD1

*proteasome 26S subunit, non-ATPase 1* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (19 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.57× (z +31.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 0.785× (z -5.1, q 2e-04, down in 33 of 49 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.749× (z -4.3, q 0.002, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (LS 180 0.614×, A-427 0.608×; ⚠ cell-cycle shift, explains ~79% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.326×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Estrone sulfate (potassium) (drug)]] 0.05 µM in 1 line (SW 1088 0.0921×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD11]] (+0.77, fdr 7e-06), [[VCP]] (+0.74, fdr 7e-06), [[HERC2]] (+0.71, fdr 7e-06); moves opposite to [[ABCA5]] (-0.67, fdr 7e-06), [[MINDY2]] (-0.66, fdr 7e-06), [[KLHL28]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GYPC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 24 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.57×** | +31.7 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.24×** | +30.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.53×** | +24.8 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.97×** | +17.5 | 0e+00 | 48/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +16.3 | 0e+00 | 47/48 (C32, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +16.2 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.40×** | +13.3 | 1e-38 | 46/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +13.0 | 5e-37 | 36/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.22×** | +12.7 | 2e-35 | 45/45 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.33×** | +12.6 | 2e-34 | 47/49 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.69×** | +10.9 | 5e-26 | 39/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.68×** | +10.8 | 2e-25 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +10.2 | 6e-23 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.60×** | +9.8 | 4e-21 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.61×** | +9.5 | 1e-19 | 41/47 (COLO 205, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 1e-03 | 23/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.001 | 14/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.006 | 21/48 (HS-578T, SW 900, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.010 | 20/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.4 | 0.013 | 18/48 (NCI-H1792, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10417.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (LS 180 0.614×, A-427 0.608×; ⚠ cell-cycle shift, explains ~79% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.326×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Estrone sulfate (potassium) (drug)]] 0.05 µM in 1 line (SW 1088 0.0921×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.785×** | -5.1 | 2e-04 | 33/49 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.793×** | -4.9 | 3e-04 | 27/49 (Panc 03.27, SHP-77, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.798×** | -4.7 | 4e-04 | 27/48 (A498, LS 180, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.749×** | -4.3 | 0.002 | 26/48 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.873× | -4.1 | 0.005 | 20/48 (LS 180, A-427, …) | all doses, flat | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.9 | 0.008 | 21/49 (LS 180, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.833×** | -3.9 | 0.009 | 24/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -3.6 | 0.024 | 12/48 (HS-578T, LS 180, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.041 | 18/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.066 | 16/48 (KATO III, A-427, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.860× | -3.2 | 0.070 | 10/48 (KATO III, NCI-H661, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.863× | -3.1 | 0.081 | 17/48 (KATO III, HOP62, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.093 | 15/48 (H4, NCI-H661, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 126 | 19 (10 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.77× (z +27.2) | — |
| [[LOX-IMVI (line)]] | wt | 114 | 14 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.14× (z +23.3) | — |
| [[PANC-1 (line)]] | alt | 141 | 14 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +21.1) | — |
| [[NCI-H460 (line)]] | wt | 170 | 13 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.73× (z +24.7) | — |
| [[LoVo (line)]] | wt | 136 | 12 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.26× (z +24.1) | — |
| [[NCI-H1792 (line)]] | alt | 87.2 | 12 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.36× (z +19.9) | — |
| [[SNU-423 (line)]] | alt | 88.3 | 11 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.99× (z +19.0) | — |
| [[COLO 205 (line)]] | alt | 62.3 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 16.3× (z +20.0) | — |
| [[LS 180 (line)]] | wt | 184 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.45× (z +20.3) | [[Selinexor (drug)]] 5 µM 0.614× (z -9.6) ⚠ cell-cycle shift, explains ~79% of this change |
| [[A498 (line)]] | wt | 116 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.93× (z +19.7) | — |
| [[HOP62 (line)]] | alt | 109 | 9 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.05× (z +22.5) | — |
| [[HT-29 (line)]] | alt | 113 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.86× (z +22.0) | — |
| [[SW 900 (line)]] | alt | 167 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.44× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.81× (z +18.9) | — |
| [[Panc 03.27 (line)]] | alt | 121 | 8 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.62× (z +19.4) | — |
| [[SNU-1 (line)]] | wt | 148 | 6 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.17× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 78.8 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.60× (z +18.3) | — |
| [[HEC-1-A (line)]] | alt | 114 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.15× (z +19.6) | — |
| [[KATO III (line)]] | alt | 106 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.81× (z +18.9) | — |
| [[RKO (line)]] | wt | 157 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.27× (z +15.4) | — |
| [[A549 (line)]] | wt | 125 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.53× (z +18.2) | — |
| [[AsPC-1 (line)]] | alt | 88.6 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.01× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 143 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.34× (z +22.7) | — |
| [[NCI-H23 (line)]] | alt | 201 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 170 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +15.8) | — |
| [[SW48 (line)]] | wt | 183 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.88× (z +14.8) | — |
| [[A-172 (line)]] | wt | 158 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +15.5) | — |
| [[BT-474 (line)]] | alt | 136 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.24× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 154 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 68.8 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.57× (z +18.7) | — |
| [[HS-578T (line)]] | alt | 115 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.18× (z +17.2) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.82× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.66× (z +16.5) | — |
| [[C32 (line)]] | wt | 61.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.06× (z +16.7) | — |
| [[H4 (line)]] | wt | 128 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.79× (z +15.2) | — |
| [[HCT15 (line)]] | alt | 89.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.47× (z +16.8) | — |
| [[HepG2_C3A (line)]] | wt | 170 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 160 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.08× (z +16.4) | — |
| [[SHP-77 (line)]] | alt | 143 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.33× (z +18.9) | — |
| [[A-427 (line)]] | wt | 182 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.608× (z -9.4) ⚠ cell-cycle shift, explains ~79% of this change |
| [[hTERT-HPNE (line)]] | wt | 87.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.50× (z +18.3) | — |
| [[J82 (line)]] | alt | 112 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 187 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.20× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 101 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.99× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0921× (z -9.1) |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 164 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD11]] | +0.77 | +0.76 / +0.83 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[VCP]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 778 |
| [[HERC2]] | +0.71 | +0.72 / +0.74 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[HERC2P9-1]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PSMB2]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[USP14]] | +0.70 | +0.65 / +0.77 | both halves | 7e-06 | pathway: Deubiquitination; STRING 999 |
| [[CCT5]] | +0.70 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 584 |
| [[PSMD2]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[STIP1]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[MACROH2A1]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CCT3]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 562 |
| [[TALDO1]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 | pathway: Cellular response to chemical stress |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA5]] | -0.67 | -0.63 / -0.61 | both halves | 7e-06 | pathway: ABC-family protein mediated transport |
| [[MINDY2]] | -0.66 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[KLHL28]] | -0.65 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.64 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[POLR1H]] | -0.63 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[RSRP1]] | -0.62 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.62 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[PIK3IP1]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.61 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[GAD1]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[OGA]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.60 | -0.60 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYPC]] | B | GYPC activity lowers PSMD1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.19× higher at baseline in the lines without GYPC | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[ME1]] | C | ME1 activity weakens PSMD1's drug response | lines that do not express ME1 (11) vs lines expressing it (38) | the lines without ME1 respond 0.92× as strongly (z diff -0.87); strongest at Ixazomib citrate 0.5 µM: 4.24x vs 4.34x (z diff -2.4) | 0.065 | ⚠ within organs, on part of the lines; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-21.1, -12.5); signed map (-13.3, -46.1). **Vector** length 120, 46.7% of its response variance represented; |z| ≥ 3 in 1,629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.1 | +31.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.7 | +30.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.1 | +24.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.8 | +5.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.7 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +4.4 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -6.6 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -5.9 | -4.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.2 | -5.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.1 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -0.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,056,845-231,173,116 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S1, P112, Rpn2 |
| Gene groups (HGNC) | Proteasome; Armadillo like helical domain containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99460](https://www.uniprot.org/uniprotkb/Q99460) (26S proteasome non-ATPase regulatory subunit 1):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [5707](https://www.ncbi.nlm.nih.gov/gene/5707):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9554) · Entrez [5707](https://www.ncbi.nlm.nih.gov/gene/5707) · UniProt [Q99460](https://www.uniprot.org/uniprotkb/Q99460) · Ensembl [ENSG00000173692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173692)

## Data

Gene col 10417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10417); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10417]; `tensor/DDL_lfc|DDL_z.npy` [10417]; `embed/gene_vectors.npy` [10417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10417 or target_col == 10417). Every well: [[PSMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
