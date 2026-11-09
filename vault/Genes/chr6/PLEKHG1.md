---
symbol: "PLEKHG1"
type: "gene"
col: 4174
ensembl_id: "ENSG00000120278"
name: "pleckstrin homology and RhoGEF domain containing G1"
location: "6q25.1"
module: 8
arm: "+"
pooled_cpm: 42.11
n_lines_expressing: 33
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 25
direction_downstream: 48
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PLEKHG1

*pleckstrin homology and RhoGEF domain containing G1* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +11.8, q 4e-29, up in 16 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.438× (z -16.6, q 0e+00, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INAVA]] (+0.59, fdr 1e-05), [[FAM149A]] (+0.59, fdr 3e-05), [[ALDH1L1]] (+0.57, fdr 1e-05); moves opposite to [[IFT122]] (-0.44, fdr 6e-05), [[GLIS3]] (-0.44, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[SLC44A3-AS1]] → it (grade B ⚠); 48 go from it, the strongest it → [[OCLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +11.8 | 4e-29 | 16/31 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +9.9 | 7e-21 | 17/31 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +6.1 | 2e-07 | 18/29 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.8 | 1e-06 | 18/31 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +5.6 | 2e-06 | 16/31 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.32×** | +5.6 | 2e-06 | 14/29 (HCT15, A-427, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 7e-05 | 16/30 (COLO 205, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +4.6 | 3e-04 | 8/30 (C32, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 5e-04 | 11/31 (A-427, AsPC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.16× | +4.2 | 0.002 | 12/31 (KATO III, HCT15, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.002 | 4/30 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 7/30 (HCT15, A-427, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 4/31 (A498, A-427, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.6 | 0.015 | 2/31 (AsPC-1, SK-MEL-2) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.020 | 4/31 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.044 | 3/31 (Panc 03.27, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.067 | 8/31 (A498, KATO III, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.067 | 4/31 (SW480, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.438×** | -16.6 | 0e+00 | 26/31 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.441×** | -16.4 | 0e+00 | 26/31 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.572×** | -15.9 | 0e+00 | 26/31 (KATO III, LoVo, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.468×** | -15.3 | 0e+00 | 27/31 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.589×** | -10.6 | 2e-24 | 23/29 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.589×** | -10.6 | 2e-24 | 22/31 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.600×** | -10.3 | 9e-23 | 24/31 (KATO III, HT-29, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.617×** | -9.7 | 2e-20 | 20/30 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -9.4 | 2e-19 | 22/31 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.636×** | -9.1 | 6e-18 | 22/30 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.669×** | -7.8 | 4e-13 | 24/31 (KATO III, SK-MEL-2, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.725×** | -6.2 | 2e-08 | 18/29 (COLO 205, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.738×** | -6.1 | 5e-08 | 18/27 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.751×** | -5.3 | 4e-06 | 17/26 (KATO III, C-33 A, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.775×** | -5.1 | 1e-05 | 16/29 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.631×** | -4.8 | 4e-05 | 12/30 (SW1417, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -4.7 | 8e-05 | 16/31 (C32, SW48, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.3 | 0.027 | 16/31 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.741×** | -3.1 | 0.042 | 10/31 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 115 | 0 | 16 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.186× (z -15.7) |
| [[KATO III (line)]] | alt | 121 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -41.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.117× (z -24.6) |
| [[LoVo (line)]] | wt | 407 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0565× (z -32.8) |
| [[SW1417 (line)]] | alt | 70.7 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.208× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 63.2 | 1 (1 ⚠) | 10 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.84× (z +8.6) ⚠ unreliable plate only | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -16.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -15.4) |
| [[HCT15 (line)]] | alt | 76.5 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -17.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.174× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 43.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -19.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 56.0 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.174× (z -14.6) |
| [[SW48 (line)]] | wt | 187 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.185× (z -13.4) |
| [[A-427 (line)]] | wt | 58.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.9) |
| [[A498 (line)]] | wt | 46.9 | 1 (1 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.88× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.180× (z -17.1) |
| [[LS 180 (line)]] | wt | 37.4 | 2 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.85× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -17.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 38.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -26.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -12.6) |
| [[C-33 A (line)]] | alt | 102 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.213× (z -10.5) |
| [[COLO 205 (line)]] | alt | 54.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -20.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.169× (z -13.4) |
| [[A-172 (line)]] | wt | 23.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -11.5) |
| [[PANC-1 (line)]] | alt | 10.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.79× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 18.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.228× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 307 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0800× (z -10.5) |
| [[SW480 (line)]] | alt | 11.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.54× (z +11.8) | — |
| [[C32 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[AN3 CA (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAVA]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FAM149A]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ALDH1L1]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[WIPF3]] | +0.54 | +0.46 / +0.49 | both halves | 2e-05 | pathway: CDC42 GTPase cycle |
| [[FUT2]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ESRP1]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GCNT3]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GDF15]] | +0.53 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CLIC5]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT122]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[GLIS3]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 20, C 5. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises PLEKHG1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.28× lower at baseline in the lines without SLC44A3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises PLEKHG1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without SLC44A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[ST14]] | B | ST14 activity raises PLEKHG1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.17× lower at baseline in the lines without ST14 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[MYO5B]] | B | MYO5B activity raises PLEKHG1's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.83× lower at baseline in the lines without MYO5B | 0.018 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[GRHL3]] | B | GRHL3 activity raises PLEKHG1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.04× lower at baseline in the lines without GRHL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[TMPRSS4]] | B | TMPRSS4 activity raises PLEKHG1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.45× lower at baseline in the lines without TMPRSS4 | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[PCAT1]] | B | PCAT1 activity raises PLEKHG1's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.25× lower at baseline in the lines without PCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[OCLN]] | B | OCLN activity raises PLEKHG1's level | lines that do not express OCLN (19) vs lines expressing it (31) | 2.64× lower at baseline in the lines without OCLN | 0.037 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises PLEKHG1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without PLEKHG6 | 0.044 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[FAM83B]] | B | FAM83B activity raises PLEKHG1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.06× lower at baseline in the lines without FAM83B | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[CDH1]] | B | CDH1 activity raises PLEKHG1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without CDH1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[PRSS12]] | B | PRSS12 activity raises PLEKHG1's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without PRSS12 | 0.060 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 42, C 6. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCLN]] | B | PLEKHG1 activity raises OCLN's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.76× lower at baseline in the lines without PLEKHG1 | 0.001 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[IGSF3]] | B | PLEKHG1 activity raises IGSF3's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.67× lower at baseline in the lines without PLEKHG1 | 0.002 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SLC44A3-AS1]] | B | PLEKHG1 activity raises SLC44A3-AS1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.76× lower at baseline in the lines without PLEKHG1 | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SLC44A3]] | B | PLEKHG1 activity raises SLC44A3's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.56× lower at baseline in the lines without PLEKHG1 | 0.006 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[MYO5B]] | B | PLEKHG1 activity raises MYO5B's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.70× lower at baseline in the lines without PLEKHG1 | 0.008 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[CDH1]] | B | PLEKHG1 activity raises CDH1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.87× lower at baseline in the lines without PLEKHG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[GPR35]] | B | PLEKHG1 activity raises GPR35's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without PLEKHG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[EPS8L1]] | B | PLEKHG1 activity raises EPS8L1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without PLEKHG1 | 0.014 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[BEX2]] | B | PLEKHG1 activity raises BEX2's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without PLEKHG1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[ST14]] | B | PLEKHG1 activity raises ST14's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 4.38× lower at baseline in the lines without PLEKHG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[CDS1]] | B | PLEKHG1 activity raises CDS1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.76× lower at baseline in the lines without PLEKHG1 | 0.019 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[LIPH]] | B | PLEKHG1 activity raises LIPH's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.34× lower at baseline in the lines without PLEKHG1 | 0.019 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.3, 54.3); signed map (54.4, 4.7). **Vector** length 95.2, 23.4% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.1 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.7 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +5.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +4.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.3 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.9 | -10.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -0.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:150,599,883-150,843,665 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1209, ARHGEF41 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 5 pathways, smallest: CDC42 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULL1](https://www.uniprot.org/uniprotkb/Q9ULL1) (Pleckstrin homology domain-containing family G member 1):

> Acts as a guanine nucleotide exchange factor (GEF) for RAC1 and CDC42.

**Summary**, from NCBI Gene [57480](https://www.ncbi.nlm.nih.gov/gene/57480):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in regulation of small GTPase mediated signal transduction. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20884) · Entrez [57480](https://www.ncbi.nlm.nih.gov/gene/57480) · UniProt [Q9ULL1](https://www.uniprot.org/uniprotkb/Q9ULL1) · Ensembl [ENSG00000120278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120278)

## Data

Gene col 4174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4174); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4174]; `tensor/DDL_lfc|DDL_z.npy` [4174]; `embed/gene_vectors.npy` [4174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4174 or target_col == 4174). Every well: [[PLEKHG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
