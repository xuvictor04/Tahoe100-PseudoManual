---
symbol: "DUSP14"
type: "gene"
col: 15864
ensembl_id: "ENSG00000276023"
name: "dual specificity phosphatase 14"
location: "17q12"
module: 224
arm: "+"
pooled_cpm: 20.82
n_lines_expressing: 49
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# DUSP14

*dual specificity phosphatase 14* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.61× (z +30.1, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 5 µM: 0.776× (z -4.2, q 0.013, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.209×, LoVo 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.354×; ⚠ cell-cycle shift, explains ~24% of this change); [[Sulfisoxazole (drug)]] 0.5 µM in 1 line (Hs 766T 0.0921×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.115×); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.127×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLK2]] (+0.64, fdr 7e-06), [[SERTAD1]] (+0.62, fdr 7e-06), [[RAP2B]] (+0.61, fdr 1e-05); moves opposite to [[RPUSD4]] (-0.50, fdr 1e-05), [[ADPGK]] (-0.49, fdr 4e-05), [[PIGN]] (-0.49, fdr 3e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM40]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.61×** | +30.1 | 0e+00 | 44/46 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.21×** | +23.8 | 0e+00 | 43/46 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.39×** | +18.5 | 0e+00 | 43/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +11.8 | 6e-30 | 38/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +11.5 | 1e-28 | 36/44 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.99×** | +11.3 | 8e-28 | 38/47 (BT-474, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.39×** | +10.6 | 4e-24 | 39/47 (A498, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.87×** | +10.4 | 2e-23 | 35/47 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.82×** | +9.9 | 4e-21 | 34/46 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.72×** | +9.0 | 2e-17 | 38/47 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.54×** | +7.1 | 5e-11 | 27/45 (BT-474, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +7.1 | 8e-11 | 25/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +7.0 | 8e-11 | 27/47 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.50×** | +6.7 | 7e-10 | 23/46 (BT-474, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +6.1 | 4e-08 | 23/45 (HT-29, SW480, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +5.3 | 4e-06 | 20/44 (A-172, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 2e-05 | 19/46 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 17/47 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +4.2 | 6e-04 | 17/46 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.2 | 6e-04 | 16/47 (HT-29, A-427, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.002 | 14/47 (A498, A549, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.006 | 7/44 (A-427, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15864.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.209×, LoVo 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.354×; ⚠ cell-cycle shift, explains ~24% of this change); [[Sulfisoxazole (drug)]] 0.5 µM in 1 line (Hs 766T 0.0921×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.115×); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.127×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 5 µM |  | **0.776×** | -4.2 | 0.013 | 14/46 (LOX-IMVI, CHP-212, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.807× | -3.6 | 0.10 | 10/46 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.821× | -3.3 | 0.19 | 14/46 (J82, HOP62, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.1 | 0.25 | 2/47 (NCI-H23, H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 79.8 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.06× (z +12.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.3) | — |
| [[A498 (line)]] | wt | 24.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +22.1) | — |
| [[A549 (line)]] | wt | 18.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 18.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +17.1) | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +16.3) | — |
| [[HT-29 (line)]] | alt | 23.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +14.3) | — |
| [[LoVo (line)]] | wt | 12.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 36.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 10.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +15.5) | — |
| [[J82 (line)]] | alt | 19.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 8.76 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 7.20× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +16.3) | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 25.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.2) | — |
| [[A-172 (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.115× (z -9.2) |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0921× (z -10.7) |
| [[KATO III (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[RKO (line)]] | wt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[SW480 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.5) | — |
| [[A-427 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLK2]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SERTAD1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RAP2B]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SERTAD2]] | +0.58 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[C21orf91]] | +0.57 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SYTL2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[AMOTL2]] | +0.57 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.56 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[RAB30]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[BIK]] | +0.54 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ABL2]] | +0.53 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD4]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.49 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[PIGN]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.49 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[GDAP2]] | -0.49 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[NTAQ1]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.47 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[METTL9]] | -0.47 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SAP130]] | -0.47 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SNRNP40]] | -0.46 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[TRAPPC10]] | -0.46 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[NIPA2]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM40]] | B | TMEM40 activity raises DUSP14's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.30× lower at baseline in the lines without TMEM40 | 0.095 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.6, 8.3); signed map (3.9, 23.5). **Vector** length 86.4, 19.4% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +23.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +30.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +11.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +7.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +1.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:37,489,891-37,513,501 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MKP-L, MKP6 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Hallmark sets | COAGULATION |
| Matched by | ensembl_id |

**Function**, from UniProt [O95147](https://www.uniprot.org/uniprotkb/O95147) (Dual specificity protein phosphatase 14):

> Involved in the inactivation of MAP kinases. Dephosphorylates ERK, JNK and p38 MAP-kinases. Plays a negative role in TCR signaling by dephosphorylating MAP3K7 adapter TAB1 leading to its inactivation.

**Summary**, from NCBI Gene [11072](https://www.ncbi.nlm.nih.gov/gene/11072):

> Dual-specificity phosphatases (DUSPs) constitute a large heterogeneous subgroup of the type I cysteine-based protein-tyrosine phosphatase superfamily. DUSPs are characterized by their ability to dephosphorylate both tyrosine and serine/threonine residues. They have been implicated as major modulators of critical signaling pathways. DUSP14 contains the consensus DUSP C-terminal catalytic domain but lacks the N-terminal CH2 domain found in the MKP (mitogen-activated protein kinase phosphatase) …

**Accessions** — [HGNC:17007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17007) · Entrez [11072](https://www.ncbi.nlm.nih.gov/gene/11072) · UniProt [O95147](https://www.uniprot.org/uniprotkb/O95147) · Ensembl [ENSG00000276023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276023)

## Data

Gene col 15864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15864); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15864]; `tensor/DDL_lfc|DDL_z.npy` [15864]; `embed/gene_vectors.npy` [15864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15864 or target_col == 15864). Every well: [[DUSP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
