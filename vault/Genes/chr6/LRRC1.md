---
symbol: "LRRC1"
type: "gene"
col: 5994
ensembl_id: "ENSG00000137269"
name: "leucine rich repeat containing 1"
location: "6p12.1"
module: 163
arm: "+"
pooled_cpm: 76.05
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# LRRC1

*leucine rich repeat containing 1* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.77× (z +10.9, q 5e-25, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.426× (z -15.6, q 0e+00, down in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.688× (z -7.1, q 2e-10, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5A]] (+0.65, fdr 7e-06), [[ORC4]] (+0.64, fdr 7e-06), [[TANC1]] (+0.64, fdr 9e-06); moves opposite to [[VAC14]] (-0.56, fdr 1e-05), [[CC2D1B]] (-0.55, fdr 5e-05), [[GPATCH2L]] (-0.54, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ATP8B1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RBMS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +10.9 | 5e-25 | 36/45 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +10.9 | 5e-25 | 32/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +9.4 | 9e-19 | 29/46 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +9.2 | 4e-18 | 32/45 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +8.9 | 7e-17 | 28/45 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +8.6 | 8e-16 | 28/45 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +8.5 | 2e-15 | 27/45 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +8.2 | 2e-14 | 27/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +7.8 | 3e-13 | 35/46 (PANC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +6.6 | 2e-09 | 28/44 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 3e-08 | 29/45 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 18/45 (C32, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 19/45 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.006 | 11/47 (PANC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.8 | 0.006 | 11/45 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.010 | 10/45 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.4 | 0.027 | 13/45 (AsPC-1, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.426×** | -15.6 | 0e+00 | 32/40 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.535×** | -11.9 | 4e-30 | 30/45 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.592×** | -9.2 | 7e-18 | 31/42 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -7.1 | 2e-10 | 34/45 (LoVo, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -6.6 | 6e-09 | 25/43 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -5.9 | 3e-07 | 29/45 (LoVo, A498, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.667×** | -5.5 | 3e-06 | 23/43 (C32, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -5.2 | 2e-05 | 24/45 (A498, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -4.7 | 1e-04 | 21/45 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.794×** | -4.4 | 7e-04 | 21/45 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **0.811×** | -4.0 | 0.004 | 19/43 (LS 180, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.9 | 0.005 | 19/44 (HOP62, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -3.8 | 0.005 | 19/45 (NCI-H2347, NCI-H661, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.828×** | -3.6 | 0.014 | 17/45 (SNU-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.829×** | -3.6 | 0.014 | 15/45 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.885× | -3.3 | 0.037 | 8/45 (RKO, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 205 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0911× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.400× (z -10.6) |
| [[PANC-1 (line)]] | alt | 36.6 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 82.5 | 2 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.86× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 25.1 | 5 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.80× (z +10.6) | — |
| [[J82 (line)]] | alt | 30.8 | 5 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.07× (z +12.0) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 3.80× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 121 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.5× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 233 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0652× (z -28.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 155 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.00× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 67.1 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -14.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -15.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 240 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -15.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 45.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 72.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -17.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.263× (z -10.1) |
| [[SW1417 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -13.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 134 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 13.1× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0703× (z -18.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 41.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.1 | 2 | 0 | [[Ponatinib (drug)]] 5 µM 3.86× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 49.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 106 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 41.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 32.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 47.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -13.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.5 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 3.16× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0539× (z -15.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5A]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ORC4]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TANC1]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[PIK3C2B]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RANBP9]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[PRKAR2B]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[NOS1AP]] | +0.61 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[EPB41L4B]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CNOT6L]] | +0.60 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CDC42SE2]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TBC1D2B]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[TMEM131L]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAC14]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CC2D1B]] | -0.55 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[GPATCH2L]] | -0.54 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TAF2]] | -0.53 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[CRYM]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PEPD]] | -0.52 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[RABL3]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[IBA57]] | -0.51 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ATXN10]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CHM]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ANKLE2]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP8B1]] | B | ATP8B1 activity raises LRRC1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without ATP8B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TJP2]] | B | TJP2 activity raises LRRC1's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without TJP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity weakens LRRC1's drug response | lines that do not express ATP8B1 (12) vs lines expressing it (34) | the lines without ATP8B1 respond 1.15× as strongly (z diff -0.67); strongest at Panobinostat 0.5 µM: 2.14x vs 1.27x (z diff -4.0) | 0.090 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86; target measured in part of the lines; both ways; artifact flags |
| [[ADGRB2]] | B | ADGRB2 activity lowers LRRC1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.48× higher at baseline in the lines without ADGRB2 | 0.095 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBMS2]] | C | LRRC1 activity strengthens RBMS2's drug response | lines that do not express LRRC1 (3) vs lines expressing it (44) | the lines without LRRC1 respond 0.41× as strongly (z diff +2.98); strongest at Auranofin 5 µM: 0.74x vs 0.51x (z diff +4.7) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: CYP2E1; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.3, -5.5); signed map (-19.8, 18.7). **Vector** length 123, 36.0% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.6 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +8.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.0 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:53,794,497-53,924,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ523E19.1, LANO, FLJ10775, FLJ11834 |
| Reactome | 4 pathways, smallest: RND2 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

UniProt [Q9BTT6](https://www.uniprot.org/uniprotkb/Q9BTT6) carries no function annotation.

**Summary**, from NCBI Gene [55227](https://www.ncbi.nlm.nih.gov/gene/55227):

> Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14307) · Entrez [55227](https://www.ncbi.nlm.nih.gov/gene/55227) · UniProt [Q9BTT6](https://www.uniprot.org/uniprotkb/Q9BTT6) · Ensembl [ENSG00000137269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137269)

## Data

Gene col 5994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5994); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5994]; `tensor/DDL_lfc|DDL_z.npy` [5994]; `embed/gene_vectors.npy` [5994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5994 or target_col == 5994). Every well: [[LRRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
