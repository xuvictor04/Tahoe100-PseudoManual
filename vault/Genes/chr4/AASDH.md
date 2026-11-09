---
symbol: "AASDH"
type: "gene"
col: 8069
ensembl_id: "ENSG00000157426"
name: "aminoadipate-semialdehyde dehydrogenase"
location: "4q12"
module: 11
arm: "+"
pooled_cpm: 24.93
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# AASDH

*aminoadipate-semialdehyde dehydrogenase* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.80× (z +13.3, q 7e-38, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.501× (z -15.8, q 0e+00, down in 29 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.375× (z -11.7, q 2e-29, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP23]] (+0.62, fdr 9e-06), [[CEBPZ]] (+0.61, fdr 8e-06), [[MRPL2]] (+0.61, fdr 7e-06); moves opposite to [[PABIR2]] (-0.58, fdr 3e-05), [[ARF3]] (-0.55, fdr 1e-05), [[RHOA]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +13.3 | 7e-38 | 41/48 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +10.8 | 7e-25 | 33/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +10.5 | 1e-23 | 36/48 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +9.3 | 2e-18 | 30/48 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +8.5 | 1e-15 | 26/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +8.5 | 2e-15 | 25/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +7.0 | 2e-10 | 24/48 (LS 180, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +6.5 | 5e-09 | 23/47 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +6.2 | 3e-08 | 23/47 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.2 | 3e-08 | 17/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +6.0 | 1e-07 | 19/47 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +6.0 | 1e-07 | 24/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.4 | 3e-06 | 17/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 1e-04 | 17/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 3e-04 | 13/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.003 | 8/47 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.007 | 8/47 (SW480, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.6 | 0.010 | 7/48 (SNU-423, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -15.8 | 0e+00 | 29/44 (LoVo, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.527×** | -14.1 | 2e-42 | 37/46 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -11.7 | 2e-29 | 38/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -11.2 | 5e-27 | 37/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.623×** | -10.7 | 1e-24 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -9.6 | 1e-19 | 26/41 (A-427, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -8.3 | 1e-14 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -8.2 | 2e-14 | 19/37 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -7.3 | 1e-11 | 25/47 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.721×** | -6.5 | 6e-09 | 21/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.9 | 5e-05 | 2/48 (AN3 CA, SW 1088) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.869× | -4.5 | 3e-04 | 13/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.837× | -4.1 | 0.002 | 10/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -4.0 | 0.002 | 15/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.837× | -3.9 | 0.003 | 12/48 (NCI-H1573, SW 1271, …) | top dose only | plate-row cell shift |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.061 | 4/48 (CHP-212, CFPAC-1, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.873× | -3.0 | 0.083 | 8/48 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.0 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -11.9) |
| [[PANC-1 (line)]] | alt | 22.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -13.9) |
| [[SW480 (line)]] | alt | 30.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -14.5) |
| [[A-427 (line)]] | wt | 36.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.9) |
| [[A498 (line)]] | wt | 29.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -12.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 33.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -19.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -13.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0795× (z -12.8) |
| [[HCT15 (line)]] | alt | 41.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -12.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 26.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 55.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.208× (z -15.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -9.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0659× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -11.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -12.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP23]] | +0.62 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[CEBPZ]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[MRPL2]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RPAP1]] | +0.61 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[MRPS31]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[GOSR1]] | +0.60 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[ZNF146]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LEO1]] | +0.59 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MRPL46]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PSMD5]] | +0.58 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[FBXO45]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ABRAXAS2]] | +0.57 | +0.70 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABIR2]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ARF3]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RHOA]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[LAMP1]] | -0.53 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[PPM1A]] | -0.53 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ILRUN]] | -0.53 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[PRKACA]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[HMG20B]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[KIF1C]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MAPK1]] | -0.51 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ACTR3]] | -0.51 | -0.50 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.5, 0.8); signed map (-13.4, -6.9). **Vector** length 69.8, 12.5% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +6.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -8.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -14.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -7.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | aminoadipate-semialdehyde dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,338,287-56,387,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRPS998, LYS2, ACSF4 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4L235](https://www.uniprot.org/uniprotkb/Q4L235) (Beta-alanine-activating enzyme):

> Covalently binds beta-alanine in an ATP-dependent manner to form a thioester bond with its phosphopantetheine group and transfers it to an, as yet, unknown acceptor. May be required for a post-translational protein modification or for post-transcriptional modification of an RNA.

**Summary**, from NCBI Gene [132949](https://www.ncbi.nlm.nih.gov/gene/132949):

> This gene encodes a member of the non-ribosome peptide syntesase (NRPS) enzyme family. The encoded protein contains an AMP-binding domain, PP-binding (phosphopantetheine, or pantetheine 4'phosphate-binding) domain and the Pyrrolo-quinoline quinon (PQQ) binding domain. The protein is expressed in several adult tissues. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:23993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23993) · Entrez [132949](https://www.ncbi.nlm.nih.gov/gene/132949) · UniProt [Q4L235](https://www.uniprot.org/uniprotkb/Q4L235) · Ensembl [ENSG00000157426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157426)

## Data

Gene col 8069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8069); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8069]; `tensor/DDL_lfc|DDL_z.npy` [8069]; `embed/gene_vectors.npy` [8069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8069 or target_col == 8069). Every well: [[AASDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AASDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
