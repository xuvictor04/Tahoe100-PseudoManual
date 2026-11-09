---
symbol: "PDZD8"
type: "gene"
col: 9157
ensembl_id: "ENSG00000165650"
name: "PDZ domain containing 8"
location: "10q25.3-q26.11"
module: 29
arm: "+"
pooled_cpm: 152.98
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PDZD8

*PDZ domain containing 8* — 10q25.3-q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.57× (z +13.8, q 2e-40, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.753× (z -4.2, q 0.012, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A549 0.312×, HT-29 0.361×, CFPAC-1 0.416×, COLO 205 0.439×, …; ⚠ cell-cycle shift, explains ~12% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.244×, HepG2/C3A 0.349×, NCI-H2030 0.521×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.411×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STT3B]] (+0.59, fdr 2e-05), [[ERMP1]] (+0.53, fdr 2e-05), [[GOLM1]] (+0.53, fdr 1e-05); moves opposite to [[CROCCP2-1]] (-0.52, fdr 6e-05), [[ZRSR2]] (-0.51, fdr 3e-05), [[NKAP]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ITIH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.57×** | +13.8 | 2e-40 | 46/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +10.7 | 4e-24 | 35/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +10.3 | 1e-22 | 36/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +10.1 | 6e-22 | 35/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +9.2 | 5e-18 | 45/48 (Hs 766T, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +8.5 | 2e-15 | 28/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +7.3 | 2e-11 | 33/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.9 | 4e-10 | 32/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.25×** | +6.8 | 7e-10 | 28/49 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 2e-09 | 29/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +6.3 | 2e-08 | 32/48 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 2e-06 | 25/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 6e-06 | 28/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +4.6 | 1e-04 | 24/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.5 | 2e-04 | 19/48 (A498, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.4 | 3e-04 | 24/49 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 23/48 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.011 | 23/48 (Hs 766T, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9157.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A549 0.312×, HT-29 0.361×, CFPAC-1 0.416×, COLO 205 0.439×, …; ⚠ cell-cycle shift, explains ~12% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.244×, HepG2/C3A 0.349×, NCI-H2030 0.521×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.753×** | -4.2 | 0.012 | 27/48 (SNU-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.877× | -4.0 | 0.015 | 4/49 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.829×** | -3.9 | 0.016 | 22/47 (HT-29, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.775×** | -3.8 | 0.019 | 24/49 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.890× | -3.6 | 0.037 | 15/48 (NCI-H1792, A498, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.864× | -3.2 | 0.14 | 15/49 (SW480, BT-474, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | 0.869× | -3.1 | 0.18 | 6/48 (COLO 205, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 106 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +16.2) | — |
| [[A549 (line)]] | wt | 331 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -19.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[MIA PaCa-2 (line)]] | alt | 83.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +12.9) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 108 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +14.3) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.99× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 123 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 5.34× (z +13.9) | — |
| [[KATO III (line)]] | alt | 104 | 4 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.32× (z +10.2) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.8) | — |
| [[SW480 (line)]] | alt | 181 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +13.9) | — |
| [[A-172 (line)]] | wt | 130 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.15× (z +10.0) | — |
| [[C32 (line)]] | wt | 98.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 118 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 349 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 122 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.84× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H2030 (line)]] | alt | 156 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.521× (z -8.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 180 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 10.4× (z +12.3) | — |
| [[A-427 (line)]] | wt | 137 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.69× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 113 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.39× (z +16.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 9.27× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 579 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[LoVo (line)]] | wt | 289 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H1792 (line)]] | alt | 109 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.23× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 81.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.4) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[Panc 03.27 (line)]] | alt | 95.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.39× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 149 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.95× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 374 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[COLO 205 (line)]] | alt | 306 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[H4 (line)]] | wt | 93.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.86× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 174 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.68× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -9.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 64.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 80.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.56× (z +8.6) | — |
| [[RKO (line)]] | wt | 136 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.06× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 173 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.84× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 133 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.80× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.26× (z +9.4) ⚠ unreliable plate only | — |
| [[SW1417 (line)]] | alt | 194 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 179 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | +0.59 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[ERMP1]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GOLM1]] | +0.53 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CPD]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[LBR]] | +0.51 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[FAM120A]] | +0.51 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[TMEM123]] | +0.51 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[PPA1]] | +0.50 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[GSPT1]] | +0.49 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[SCARB2]] | +0.49 | +0.43 / +0.49 | both halves | 4e-05 |  |
| [[DPP4]] | +0.48 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[MAL2]] | +0.48 | +0.44 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.52 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[ZRSR2]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NKAP]] | -0.49 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[TMEM101]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TMEM106A]] | -0.48 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[ZSWIM3]] | -0.47 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[RBX1]] | -0.46 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[GARRE1]] | -0.46 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[YJU2B]] | -0.46 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[IL23A]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[KDM2B]] | -0.45 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[BSDC1]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITIH2]] | B | ITIH2 activity raises PDZD8's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 1.68× lower at baseline in the lines without ITIH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[ITIH2]] | B | ITIH2 activity weakens PDZD8's drug response | lines that do not express ITIH2 (42) vs lines expressing it (7) | the lines without ITIH2 respond 16.14× as strongly (z diff -3.21); strongest at Homoharringtonine 5 µM: 1.25x vs 0.88x (z diff -6.1) | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; target measured in part of the lines; artifact flags |
| [[PAQR7]] | B | PAQR7 activity lowers PDZD8's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.90× higher at baseline in the lines without PAQR7 | 0.040 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |
| [[POF1B]] | B | POF1B activity raises PDZD8's level | lines that do not express POF1B (34) vs lines expressing it (16) | 1.67× lower at baseline in the lines without POF1B | 0.062 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-32.4, -28.7); signed map (18.4, 24.9). **Vector** length 115, 34.2% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +7.4 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.8 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +10.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.3 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -3.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | -3.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PDZ domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3-q26.11 — chr10:117,277,274-117,375,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LYVAC, bA129M16.2, FLJ34427; previously PDZK8 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEN9](https://www.uniprot.org/uniprotkb/Q8NEN9) (PDZ domain-containing protein 8):

> Lipid transfer and molecular tethering protein, which plays a key role in the formation of membrane contact sites between the endoplasmic reticulum and other organelles, such as late endosomes/lysosomes and mitochondria. Facilitates the exchange of lipids at membrane contact sites between the endoplasmic reticulum and organelles by mediating the transport of lipids, such as ceramide, cholesterol and phosphatidylserine. Also acts as a molecular glue by undergoing liquid-liquid phase separation, …

**Summary**, from NCBI Gene [118987](https://www.ncbi.nlm.nih.gov/gene/118987):

> Predicted to enable lipid binding activity and zinc ion binding activity. Involved in mitochondrial calcium ion homeostasis and mitochondrion-endoplasmic reticulum membrane tethering. Located in endoplasmic reticulum membrane and mitochondria-associated endoplasmic reticulum membrane contact site. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26974) · Entrez [118987](https://www.ncbi.nlm.nih.gov/gene/118987) · UniProt [Q8NEN9](https://www.uniprot.org/uniprotkb/Q8NEN9) · Ensembl [ENSG00000165650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165650)

## Data

Gene col 9157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9157); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9157]; `tensor/DDL_lfc|DDL_z.npy` [9157]; `embed/gene_vectors.npy` [9157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9157 or target_col == 9157). Every well: [[PDZD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
