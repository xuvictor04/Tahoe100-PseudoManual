---
symbol: "CACUL1"
type: "gene"
col: 7578
ensembl_id: "ENSG00000151893"
name: "CDK2 associated cullin domain 1"
location: "10q26.11"
module: 178
arm: "+"
pooled_cpm: 128.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# CACUL1

*CDK2 associated cullin domain 1* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.59× (z +10.9, q 7e-25, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.679× (z -9.1, q 4e-17, down in 30 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.757× (z -6.6, q 7e-09, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW 900 0.331×, C-33 A 0.329×, H4 0.330×, HEC-1-A 0.493×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.425×, KATO III 0.410×, SNU-423 0.440×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2347 0.535×, SW 900 0.418×, J82 0.495×; ⚠ toxic); [[Altretamine (drug)]] 0.05 µM in 1 line (SW 1088 0.0977×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC9C]] (+0.66, fdr 8e-06), [[MGST3]] (+0.64, fdr 7e-06), [[SLC25A23]] (+0.64, fdr 1e-05); moves opposite to [[GPATCH4]] (-0.60, fdr 1e-05), [[TTPAL]] (-0.60, fdr 1e-05), [[DDX5]] (-0.59, fdr 2e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +10.9 | 7e-25 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +9.9 | 1e-20 | 43/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.6 | 1e-15 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +8.4 | 7e-15 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.2 | 6e-11 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +7.0 | 2e-10 | 39/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +5.3 | 8e-06 | 28/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.3 | 8e-06 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +5.3 | 8e-06 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.007 | 17/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.007 | 15/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +3.8 | 0.007 | 18/48 (RPMI-7951, NCI-H1573, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.008 | 17/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.6 | 0.014 | 16/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.027 | 18/49 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7578.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW 900 0.331×, C-33 A 0.329×, H4 0.330×, HEC-1-A 0.493×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SK-MEL-2 0.425×, KATO III 0.410×, SNU-423 0.440×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2347 0.535×, SW 900 0.418×, J82 0.495×; ⚠ toxic); [[Altretamine (drug)]] 0.05 µM in 1 line (SW 1088 0.0977×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.679×** | -9.1 | 4e-17 | 30/49 (SW 900, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -8.3 | 2e-14 | 42/47 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.697×** | -8.2 | 6e-14 | 32/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.757×** | -6.6 | 7e-09 | 38/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.788×** | -5.2 | 2e-05 | 27/45 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.880× | -4.3 | 0.002 | 8/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.829×** | -4.2 | 0.002 | 24/48 (J82, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.854× | -3.6 | 0.023 | 20/50 (SNU-423, A-172, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.864× | -3.5 | 0.033 | 15/48 (A-172, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.865× | -3.4 | 0.033 | 16/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.870× | -3.3 | 0.052 | 15/49 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.075 | 10/48 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.877× | -3.1 | 0.084 | 6/48 (LoVo, KATO III, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.880× | -3.0 | 0.091 | 8/48 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.881× | -3.0 | 0.091 | 10/47 (NCI-H460, SW 900, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.882× | -3.0 | 0.091 | 4/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.882× | -3.0 | 0.091 | 6/48 (A-172, RKO, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.882× | -3.0 | 0.091 | 16/49 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 124 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.537× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 124 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 227 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 136 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.585× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 81.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.7) | — |
| [[LoVo (line)]] | wt | 125 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.04× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.495× (z -9.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 116 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.38× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 133 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 174 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -9.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.395× (z -9.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 123 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.66× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -9.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 92.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.504× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.535× (z -10.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.440× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.0977× (z -9.1) |
| [[A-172 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 176 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9C]] | +0.66 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[MGST3]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SLC25A23]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TMEM219]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.60 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ASB7]] | +0.60 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.59 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[PTOV1]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PJA2]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MAX]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | -0.60 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DDX5]] | -0.59 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[GRWD1]] | -0.54 | -0.49 / -0.54 | both halves | 2e-05 |  |
| [[NOP56]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.53 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ATXN7L2]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[RCBTB2]] | -0.52 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[UTP20]] | -0.52 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[ST7L]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.2, -12.9); signed map (-30.1, 15.7). **Vector** length 101, 29.1% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +5.4 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.4 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.6 | -6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -4.2 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | CDK2 associated cullin domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:118,674,167-118,755,249 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40409, MGC33215, CAC1; previously C10orf46 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y37](https://www.uniprot.org/uniprotkb/Q86Y37) (CDK2-associated and cullin domain-containing protein 1):

> Cell cycle associated protein capable of promoting cell proliferation through the activation of CDK2 at the G1/S phase transition.

**Summary**, from NCBI Gene [143384](https://www.ncbi.nlm.nih.gov/gene/143384):

> Enables protein kinase binding activity. Involved in G1/S transition of mitotic cell cycle; positive regulation of cell population proliferation; and positive regulation of protein kinase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23727) · Entrez [143384](https://www.ncbi.nlm.nih.gov/gene/143384) · UniProt [Q86Y37](https://www.uniprot.org/uniprotkb/Q86Y37) · Ensembl [ENSG00000151893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151893)

## Data

Gene col 7578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7578); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7578]; `tensor/DDL_lfc|DDL_z.npy` [7578]; `embed/gene_vectors.npy` [7578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7578 or target_col == 7578). Every well: [[CACUL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACUL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
