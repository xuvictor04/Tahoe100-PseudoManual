---
symbol: "EPB41L2"
type: "gene"
col: 1266
ensembl_id: "ENSG00000079819"
name: "erythrocyte membrane protein band 4.1 like 2"
location: "6q23.1-q23.2"
module: 172
arm: "+"
pooled_cpm: 237.07
n_lines_expressing: 44
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 14
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# EPB41L2

*erythrocyte membrane protein band 4.1 like 2* — 6q23.1-q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +25.0, q 0e+00, up in 40 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.721× (z -6.2, q 3e-07, down in 32 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.807× (z -4.3, q 0.003, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBL1]] (+0.66, fdr 7e-06), [[SEPTIN11]] (+0.62, fdr 9e-06), [[ACTN1]] (+0.59, fdr 1e-05); moves opposite to [[CIAO3]] (-0.72, fdr 7e-06), [[RBSN]] (-0.68, fdr 7e-06), [[ZNF766]] (-0.63, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C12orf75]] → it (grade B ⚠); 14 go from it, the strongest it → [[C19orf12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +25.0 | 0e+00 | 40/42 (SW1417, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +22.7 | 0e+00 | 37/43 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.33×** | +16.1 | 0e+00 | 40/42 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +14.0 | 4e-42 | 40/44 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.08×** | +13.9 | 6e-42 | 39/42 (A-172, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.94×** | +13.1 | 3e-37 | 33/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.88×** | +12.4 | 2e-33 | 29/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +11.2 | 2e-27 | 38/42 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.73×** | +10.8 | 3e-25 | 41/42 (SW1417, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.74×** | +10.5 | 4e-24 | 35/41 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.64×** | +9.8 | 9e-21 | 37/42 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.70×** | +9.6 | 3e-20 | 32/40 (PANC-1, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +9.5 | 1e-19 | 34/43 (SW48, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.51×** | +8.1 | 2e-14 | 31/42 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +8.0 | 4e-14 | 30/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.5 | 2e-12 | 28/42 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.7 | 3e-07 | 25/43 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.3 | 3e-06 | 36/43 (A549, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.5 | 1e-04 | 21/42 (SW48, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.5 | 2e-04 | 17/42 (MIA PaCa-2, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -6.2 | 3e-07 | 32/41 (SNU-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.787×** | -4.6 | 0.001 | 28/41 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.807×** | -4.3 | 0.003 | 24/42 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.808×** | -4.3 | 0.003 | 22/41 (SK-MEL-2, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **0.826×** | -3.8 | 0.017 | 22/42 (SNU-1, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.845× | -3.7 | 0.020 | 19/42 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.023 | 22/42 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.836× | -3.6 | 0.024 | 18/42 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.779×** | -3.6 | 0.024 | 24/41 (LoVo, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.839× | -3.4 | 0.040 | 18/42 (LoVo, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.040 | 15/43 (LoVo, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.846× | -3.3 | 0.051 | 14/44 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.060 | 16/41 (C-33 A, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.072 | 20/42 (HEC-1-A, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.858× | -3.1 | 0.086 | 12/42 (RKO, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.4 | 21 (15 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +27.9) | — |
| [[A-172 (line)]] | wt | 165 | 16 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +24.8) | — |
| [[HS-578T (line)]] | alt | 201 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +23.3) | — |
| [[SW1417 (line)]] | alt | 229 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +28.8) | — |
| [[hTERT-HPNE (line)]] | wt | 192 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +27.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 136 | 10 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +26.8) | — |
| [[NCI-H1792 (line)]] | alt | 121 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +25.7) | — |
| [[A549 (line)]] | wt | 202 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +20.0) | — |
| [[KATO III (line)]] | alt | 261 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +17.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.4) | — |
| [[SW48 (line)]] | wt | 257 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 387 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 430 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +22.1) | — |
| [[SW 900 (line)]] | alt | 102 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +16.7) | — |
| [[C32 (line)]] | wt | 277 | 7 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 199 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +20.3) | — |
| [[Hs 766T (line)]] | wt | 136 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +22.2) | — |
| [[RPMI-7951 (line)]] | alt | 262 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +26.0) | — |
| [[J82 (line)]] | alt | 336 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.8) | — |
| [[Panc 03.27 (line)]] | alt | 285 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +23.4) | — |
| [[SK-MEL-2 (line)]] | alt | 444 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 157 | 5 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +13.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -13.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 202 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +20.0) | — |
| [[H4 (line)]] | wt | 148 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +14.0) | — |
| [[HEC-1-A (line)]] | alt | 429 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.560× (z -8.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 193 | 4 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 186 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +22.8) | — |
| [[HepG2_C3A (line)]] | wt | 262 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +24.8) | — |
| [[A-427 (line)]] | wt | 188 | 3 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.9) | — |
| [[A498 (line)]] | wt | 248 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 343 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +12.1) | — |
| [[LoVo (line)]] | wt | 281 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +16.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.516× (z -8.8) |
| [[LS 180 (line)]] | wt | 330 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 414 | 3 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +13.8) | — |
| [[CHP-212 (line)]] | wt | 109 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.0) | [[Pyridoxine (drug)]] 0.5 µM 0.184× (z -9.8) |
| [[HCT15 (line)]] | alt | 242 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 1,024 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.419× (z -9.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 265 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 137 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +16.7) | — |
| [[AN3 CA (line)]] | alt | 380 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 40.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 49.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 254 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*28 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBL1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SEPTIN11]] | +0.62 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[ACTN1]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CALM2]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CMTM6]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[COTL1]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[EXTL2]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PKM]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[RASSF3]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[GLS]] | +0.57 | +0.39 / +0.68 | both halves | 6e-05 | pathway: Neuronal System |
| [[ARL5B]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RBFOX2]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*72 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO3]] | -0.72 | -0.73 / -0.66 | both halves | 7e-06 |  |
| [[RBSN]] | -0.68 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[ZNF766]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[PEX16]] | -0.62 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[PHYKPL]] | -0.61 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[TEFM]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | -0.61 | -0.49 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NMT1]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SLC25A17]] | -0.60 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[MAP2K7]] | -0.60 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[GPATCH3]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[SETDB1]] | -0.59 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[TOM1]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf75]] | B | C12orf75 activity raises EPB41L2's level | lines that do not express C12orf75 (5) vs lines expressing it (45) | 3.39× lower at baseline in the lines without C12orf75 | 0.012 | ⚠ within organs, on part of the lines; also absent: FKBP7, VAT1, KCNC4 |
| [[VIM-AS1]] | B | VIM-AS1 activity raises EPB41L2's level | lines that do not express VIM-AS1 (6) vs lines expressing it (44) | 2.48× lower at baseline in the lines without VIM-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000290876, SCHIP1, BLVRA; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises EPB41L2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without MYBL1 | 0.077 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C19orf12]] | B | EPB41L2 activity raises C19orf12's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without EPB41L2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[CRIM1]] | B | EPB41L2 activity raises CRIM1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 2.54× lower at baseline in the lines without EPB41L2 | 0.029 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[RASSF3]] | B | EPB41L2 activity lowers RASSF3's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without EPB41L2 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[NFE2L3]] | B | EPB41L2 activity raises NFE2L3's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without EPB41L2 | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[METTL16]] | B | EPB41L2 activity raises METTL16's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.30× lower at baseline in the lines without EPB41L2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[NMT1]] | B | EPB41L2 activity raises NMT1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without EPB41L2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[MPHOSPH10]] | B | EPB41L2 activity raises MPHOSPH10's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without EPB41L2 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[TEAD1]] | B | EPB41L2 activity raises TEAD1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without EPB41L2 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[SAT2]] | B | EPB41L2 activity raises SAT2's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.45× lower at baseline in the lines without EPB41L2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[MYBL1]] | B | EPB41L2 activity raises MYBL1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 2.32× lower at baseline in the lines without EPB41L2 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[LSM7]] | B | EPB41L2 activity raises LSM7's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.30× lower at baseline in the lines without EPB41L2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[ELMOD3]] | B | EPB41L2 activity raises ELMOD3's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without EPB41L2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction -0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.9, -5.0); signed map (-5.8, 35.0). **Vector** length 120, 42.2% of its response variance represented; |z| ≥ 3 in 1,482 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +14.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.6 | +13.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.3 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.7 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.4 | -3.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -3.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | erythrocyte membrane protein band 4.1 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.1-q23.2 — chr6:130,839,347-131,063,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 4.1-G, 4.1G |
| Gene groups (HGNC) | Erythrocyte membrane protein band 4.1; FERM domain containing |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O43491](https://www.uniprot.org/uniprotkb/O43491) (Band 4.1-like protein 2):

> Required for dynein-dynactin complex and NUMA1 recruitment at the mitotic cell cortex during anaphase.

**Summary**, from NCBI Gene [2037](https://www.ncbi.nlm.nih.gov/gene/2037):

> Predicted to enable PH domain binding activity; cytoskeletal protein binding activity; and structural molecule activity. Involved in positive regulation of protein localization to cell cortex. Located in several cellular components, including cell cortex; cell junction; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3379) · Entrez [2037](https://www.ncbi.nlm.nih.gov/gene/2037) · UniProt [O43491](https://www.uniprot.org/uniprotkb/O43491) · Ensembl [ENSG00000079819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079819)

## Data

Gene col 1266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1266); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1266]; `tensor/DDL_lfc|DDL_z.npy` [1266]; `embed/gene_vectors.npy` [1266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1266 or target_col == 1266). Every well: [[EPB41L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
