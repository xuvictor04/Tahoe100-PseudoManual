---
symbol: "SETD3"
type: "gene"
col: 11418
ensembl_id: "ENSG00000183576"
name: "SET domain containing 3, actin N3(tau)-histidine methyltransferase"
location: "14q32.2"
module: 16
arm: "-"
pooled_cpm: 78.71
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SETD3

*SET domain containing 3, actin N3(tau)-histidine methyltransferase* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.51× (z +20.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.677× (z -8.6, q 4e-15, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.72, fdr 7e-06), [[PIGN]] (+0.71, fdr 1e-05), [[PPP2R5D]] (+0.68, fdr 7e-06); moves opposite to [[MRFAP1L1]] (-0.70, fdr 7e-06), [[ZC3HC1]] (-0.70, fdr 7e-06), [[ZNF155]] (-0.70, fdr 7e-06).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +20.3 | 0e+00 | 48/48 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +18.5 | 0e+00 | 45/49 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +17.5 | 0e+00 | 48/48 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +16.9 | 0e+00 | 48/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +11.5 | 1e-28 | 43/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +9.1 | 6e-18 | 2/50 (NCI-H2030, SW 1088) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +8.9 | 5e-17 | 44/48 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +8.2 | 2e-14 | 32/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +7.3 | 2e-11 | 45/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.38×** | +7.2 | 4e-11 | 29/49 (A-427, SW480, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.7 | 1e-09 | 35/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +6.6 | 3e-09 | 34/50 (NCI-H460, RKO, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +4.5 | 3e-04 | 25/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +4.5 | 3e-04 | 23/48 (SW480, PANC-1, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.22×** | +4.1 | 0.002 | 21/45 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.009 | 14/47 (SW48, NCI-H23, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.060 | 11/47 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.0 | 0.082 | 9/48 (NCI-H2347, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -8.6 | 4e-15 | 35/48 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -8.4 | 1e-14 | 33/47 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.825×** | -6.0 | 3e-07 | 23/48 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.792×** | -5.0 | 1e-04 | 24/48 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.7 | 0.022 | 17/48 (Hs 766T, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.849× | -3.6 | 0.027 | 20/48 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.061 | 15/48 (SW1417, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 0.766× | -3.1 | 0.13 | 17/47 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.13 | 16/47 (MIA PaCa-2, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | 0.825× | -3.0 | 0.13 | 12/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.873× | -3.0 | 0.14 | 17/48 (A498, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 90.0 | 8 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 172 | 2 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.353× (z -12.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.495× (z -8.6) |
| [[RKO (line)]] | wt | 58.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 52.5 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +20.8) | — |
| [[PANC-1 (line)]] | alt | 76.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.4) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.00× (z +9.9) | — |
| [[J82 (line)]] | alt | 85.4 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -9.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.488× (z -9.0) |
| [[KATO III (line)]] | alt | 78.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 91.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[Panc 03.27 (line)]] | alt | 109 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.88× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.447× (z -9.6) |
| [[SW48 (line)]] | wt | 90.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.7) | — |
| [[A-172 (line)]] | wt | 44.1 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 61.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 86.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 64.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 73.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 72.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 60.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 71.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +11.2) | — |
| [[LoVo (line)]] | wt | 72.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 65.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 89.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 54.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 65.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 89.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 77.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 97.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.0) | — |
| [[A498 (line)]] | wt | 58.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.4) | — |
| [[C32 (line)]] | wt | 63.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.9) | — |
| [[H4 (line)]] | wt | 57.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HepG2_C3A (line)]] | wt | 68.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 70.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.3) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SK-MEL-2 (line)]] | alt | 71.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 75.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 102 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 73.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 72.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 120 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 46.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.457× (z -8.8) |
| [[SW 900 (line)]] | alt | 97.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[PIGN]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[PPP2R5D]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MLEC]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ABHD12]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[WRNIP1]] | +0.66 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[SRD5A1]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.66 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[TBCD]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1L1]] | -0.70 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[ZC3HC1]] | -0.70 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[ZNF155]] | -0.70 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[ZNF594]] | -0.68 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[YJU2]] | -0.68 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[METTL18]] | -0.67 | -0.69 / -0.57 | both halves | 1e-05 | same gene group; STRING 577 |
| [[FAM200A]] | -0.67 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[SLC9A8]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[CWC22]] | -0.67 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[GSPT2]] | -0.66 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | -0.66 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[ZNF829]] | -0.66 | -0.64 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SETD3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[P3H1]] | C | P3H1 activity lowers SETD3's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.35× higher at baseline in the lines without P3H1 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.8, 11.8); signed map (-48.5, -5.9). **Vector** length 122, 37.1% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +18.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.7 | +6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +16.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.3 | +7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +7.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Tomivosertib (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -10.5 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -9.7 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.0 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 3, actin N3(tau)-histidine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,397,748-99,480,889 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23027; previously C14orf154 |
| Gene groups (HGNC) | SET domain containing; Histidine methyltransferases |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TU7](https://www.uniprot.org/uniprotkb/Q86TU7) (Actin-histidine N-methyltransferase):

> Protein-histidine N-methyltransferase that specifically mediates 3-methylhistidine (tele-methylhistidine) methylation of actin at 'His-73'. Histidine methylation of actin is required for smooth muscle contraction of the laboring uterus during delivery. Does not have protein-lysine N-methyltransferase activity and probably only catalyzes histidine methylation of actin.

**Summary**, from NCBI Gene [84193](https://www.ncbi.nlm.nih.gov/gene/84193):

> Enables protein-L-histidine N-tele-methyltransferase activity. Involved in actin modification and peptidyl-histidine methylation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20493) · Entrez [84193](https://www.ncbi.nlm.nih.gov/gene/84193) · UniProt [Q86TU7](https://www.uniprot.org/uniprotkb/Q86TU7) · Ensembl [ENSG00000183576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183576)

## Data

Gene col 11418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11418); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11418]; `tensor/DDL_lfc|DDL_z.npy` [11418]; `embed/gene_vectors.npy` [11418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11418 or target_col == 11418). Every well: [[SETD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
