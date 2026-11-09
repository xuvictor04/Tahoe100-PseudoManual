---
symbol: "OXSR1"
type: "gene"
col: 10319
ensembl_id: "ENSG00000172939"
name: "oxidative stress responsive kinase 1"
location: "3p22.2"
module: 31
arm: "+"
pooled_cpm: 228.9
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 28
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# OXSR1

*oxidative stress responsive kinase 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.24× (z +8.2, q 1e-13, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.625× (z -13.0, q 1e-35, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRC5A]] (+0.66, fdr 7e-06), [[FA2H]] (+0.58, fdr 2e-05), [[EZR]] (+0.55, fdr 3e-05); moves opposite to [[ZNF253]] (-0.48, fdr 8e-05), [[EIF2B5]] (-0.47, fdr 2e-04), [[CCDC102A]] (-0.46, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +8.2 | 1e-13 | 43/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +6.2 | 1e-07 | 35/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +5.7 | 3e-06 | 38/48 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.1 | 0.005 | 24/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +4.1 | 0.005 | 25/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.0 | 0.005 | 26/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.006 | 27/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.015 | 23/48 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.060 | 20/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | 1.19× | +3.3 | 0.060 | 19/48 (A-427, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.073 | 22/49 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.1 | 0.086 | 11/49 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -13.0 | 1e-35 | 39/49 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.585×** | -10.5 | 4e-23 | 44/48 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.606×** | -9.8 | 3e-20 | 40/49 (AsPC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.621×** | -9.3 | 2e-18 | 46/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.621×** | -8.9 | 4e-17 | 37/44 (HT-29, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.638×** | -8.1 | 5e-14 | 32/45 (CHP-212, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.758×** | -7.6 | 2e-12 | 29/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.699×** | -7.0 | 2e-10 | 37/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.751×** | -5.6 | 1e-06 | 32/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.756×** | -5.4 | 3e-06 | 32/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.782×** | -4.6 | 2e-04 | 25/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.850× | -4.5 | 3e-04 | 22/48 (NCI-H1573, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.802×** | -4.3 | 7e-04 | 31/48 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.812×** | -4.1 | 0.002 | 23/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.868× | -3.9 | 0.003 | 10/48 (A549, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.819×** | -3.9 | 0.003 | 24/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.848× | -3.2 | 0.033 | 20/49 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.065 | 16/47 (KATO III, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 380 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.89× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -15.5) |
| [[HT-29 (line)]] | alt | 218 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 260 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 501 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -18.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 198 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 285 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -16.0) |
| [[Hs 766T (line)]] | wt | 233 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 418 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -16.3) |
| [[A549 (line)]] | wt | 226 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 277 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.07× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -14.5) |
| [[LoVo (line)]] | wt | 555 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -17.4) |
| [[A-172 (line)]] | wt | 235 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 291 | 1 (1 ⚠) | 2 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.65× (z +9.1) ⚠ cell-cycle shift, explains ~18% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 266 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.474× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.2) |
| [[C32 (line)]] | wt | 194 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 234 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 1.83× (z +9.3) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -9.8) |
| [[KATO III (line)]] | alt | 243 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 256 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.7) |
| [[RKO (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 361 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -17.0) |
| [[SW48 (line)]] | wt | 378 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 172 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.95× (z +10.8) | — |
| [[A-427 (line)]] | wt | 109 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.65× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0710× (z -10.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -12.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 176 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.6) |
| [[HS-578T (line)]] | alt | 198 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.5) |
| [[LS 180 (line)]] | wt | 278 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 114 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.48× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 203 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.3) |
| [[A498 (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 213 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5A]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FA2H]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[EZR]] | +0.55 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[CAPG]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[KRT19]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[TSC22D2]] | +0.54 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[CD55]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[JUP]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DSG3]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RDH13]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CDA]] | +0.52 | +0.58 / +0.32 | both halves | 2e-04 |  |
| [[CYTH1]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF253]] | -0.48 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[EIF2B5]] | -0.47 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[CCDC102A]] | -0.46 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[USP19]] | -0.46 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[TMEM80]] | -0.45 | -0.57 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LSM1]] | -0.45 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[DTX3]] | -0.45 | -0.45 / -0.24 | both halves | 5e-04 |  |
| [[BBS1]] | -0.45 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[CASD1]] | -0.45 | -0.46 / -0.22 | both halves | 6e-04 |  |
| [[L3MBTL2]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[MED24]] | -0.44 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[PPWD1]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[C12orf4]] | -0.44 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 28, C 0. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity strengthens OXSR1's drug response | lines that do not express SERPINB5 (34) vs lines expressing it (15) | the lines without SERPINB5 respond 0.69× as strongly (z diff +1.76); strongest at Homoharringtonine 5 µM: 0.88x vs 0.48x (z diff +7.0) | 0.003 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; target measured in part of the lines; artifact flags |
| [[SERPINB1]] | B | SERPINB1 activity raises OXSR1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without SERPINB1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[SERPINB5]] | B | SERPINB5 activity raises OXSR1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 1.54× lower at baseline in the lines without SERPINB5 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[PKP1]] | B | PKP1 activity raises OXSR1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.51× lower at baseline in the lines without PKP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[GPRC5A]] | B | GPRC5A activity raises OXSR1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without GPRC5A | 0.008 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[MYO1E]] | B | MYO1E activity raises OXSR1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without MYO1E | 0.011 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[FA2H]] | B | FA2H activity strengthens OXSR1's drug response | lines that do not express FA2H (27) vs lines expressing it (22) | the lines without FA2H respond 0.69× as strongly (z diff +1.68); strongest at Homoharringtonine 5 µM: 0.92x vs 0.55x (z diff +6.3) | 0.016 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2; target measured in part of the lines; artifact flags |
| [[KLK10]] | B | KLK10 activity raises OXSR1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 1.52× lower at baseline in the lines without KLK10 | 0.017 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[C1orf116]] | B | C1orf116 activity raises OXSR1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.42× lower at baseline in the lines without C1orf116 | 0.021 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CEACAM6]] | B | CEACAM6 activity strengthens OXSR1's drug response | lines that do not express CEACAM6 (37) vs lines expressing it (12) | the lines without CEACAM6 respond 0.69× as strongly (z diff +1.92); strongest at Homoharringtonine 5 µM: 0.81x vs 0.53x (z diff +5.7) | 0.023 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; target measured in part of the lines; artifact flags |
| [[FA2H]] | B | FA2H activity raises OXSR1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without FA2H | 0.023 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[CD55]] | B | CD55 activity raises OXSR1's level | lines that do not express CD55 (16) vs lines expressing it (34) | 1.39× lower at baseline in the lines without CD55 | 0.026 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, 56.8); signed map (-1.8, 38.1). **Vector** length 99.6, 31.8% of its response variance represented; |z| ≥ 3 in 1,403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.5 | -9.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +5.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | oxidative stress responsive kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,165,089-38,255,484 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1101; previously OSR1 |
| Gene groups (HGNC) | OXSR1/STK39 kinase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O95747](https://www.uniprot.org/uniprotkb/O95747) (Serine/threonine-protein kinase OSR1):

> Effector serine/threonine-protein kinase component of the WNK-SPAK/OSR1 kinase cascade, which is involved in various processes, such as ion transport, response to hypertonic stress and blood pressure. Specifically recognizes and binds proteins with a RFXV motif. Acts downstream of WNK kinases (WNK1, WNK2, WNK3 or WNK4): following activation by WNK kinases, catalyzes phosphorylation of ion cotransporters, such as SLC12A1/NKCC2, SLC12A2/NKCC1, SLC12A3/NCC, SLC12A5/KCC2 or SLC12A6/KCC3, regulating …

**Summary**, from NCBI Gene [9943](https://www.ncbi.nlm.nih.gov/gene/9943):

> The product of this gene belongs to the Ser/Thr protein kinase family of proteins. It regulates downstream kinases in response to environmental stress, and may play a role in regulating the actin cytoskeleton. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8508) · Entrez [9943](https://www.ncbi.nlm.nih.gov/gene/9943) · UniProt [O95747](https://www.uniprot.org/uniprotkb/O95747) · Ensembl [ENSG00000172939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172939)

## Data

Gene col 10319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10319); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10319]; `tensor/DDL_lfc|DDL_z.npy` [10319]; `embed/gene_vectors.npy` [10319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10319 or target_col == 10319). Every well: [[OXSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
