---
symbol: "GMEB1"
type: "gene"
col: 8515
ensembl_id: "ENSG00000162419"
name: "glucocorticoid modulatory element binding protein 1"
location: "1p35.3"
module: 156
arm: "+"
pooled_cpm: 33.83
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# GMEB1

*glucocorticoid modulatory element binding protein 1* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.61× (z +14.1, q 2e-42, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.510× (z -14.2, q 1e-42, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTG2]] (+0.66, fdr 1e-05), [[MTRES1]] (+0.66, fdr 1e-05), [[GMEB2]] (+0.66, fdr 7e-06); moves opposite to [[CRTAP]] (-0.52, fdr 3e-05), [[TPGS2]] (-0.52, fdr 1e-04), [[LAMP2]] (-0.52, fdr 8e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.61×** | +14.1 | 2e-42 | 42/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +10.9 | 4e-25 | 35/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +8.4 | 6e-15 | 30/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +8.2 | 3e-14 | 30/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.27×** | +7.2 | 9e-11 | 27/48 (C32, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.8 | 1e-09 | 23/47 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +6.6 | 4e-09 | 27/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.4 | 2e-08 | 29/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.7 | 2e-04 | 13/47 (SW480, LoVo, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +4.6 | 2e-04 | 17/47 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.2 | 0.002 | 19/45 (SW 900, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.22×** | +4.1 | 0.002 | 23/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.21×** | +4.1 | 0.002 | 18/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.018 | 10/47 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +3.0 | 0.087 | 15/48 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -14.2 | 1e-42 | 44/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.523×** | -13.6 | 6e-40 | 45/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.590×** | -11.1 | 2e-26 | 41/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -10.6 | 3e-24 | 35/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -10.3 | 6e-23 | 28/40 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -10.1 | 3e-22 | 32/47 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -10.1 | 7e-22 | 32/46 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -9.1 | 7e-18 | 30/48 (RPMI-7951, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.640×** | -8.7 | 2e-16 | 31/44 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.673×** | -8.3 | 5e-15 | 38/48 (PANC-1, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.770×** | -7.8 | 4e-13 | 27/47 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.609×** | -5.5 | 2e-06 | 20/48 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.778×** | -5.3 | 5e-06 | 25/47 (J82, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -5.1 | 2e-05 | 17/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.001 | 16/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -3.9 | 0.004 | 15/47 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.007 | 12/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.868× | -3.5 | 0.014 | 10/48 (MIA PaCa-2, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.891× | -2.9 | 0.096 | 9/48 (HEC-1-A, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.9 | 2 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.8) ⚠ cell-cycle shift, explains ~42% of this change | [[Dinaciclib (drug)]] 5 µM 0.259× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 54.1 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.347× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 62.0 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.7) ⚠ cell-cycle shift, explains ~42% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -13.0) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.8) |
| [[C-33 A (line)]] | alt | 80.7 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -10.7) |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -12.8) |
| [[RKO (line)]] | wt | 45.2 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -12.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.0 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.26× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 20.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -9.0) |
| [[A-427 (line)]] | wt | 42.7 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.4) ⚠ cell-cycle shift, explains ~42% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 32.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.8) ⚠ cell-cycle shift, explains ~42% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -8.6) |
| [[HS-578T (line)]] | alt | 36.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.4) |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -15.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 39.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -10.1) |
| [[KATO III (line)]] | alt | 23.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.2) ⚠ cell-cycle shift, explains ~42% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -8.9) |
| [[SW48 (line)]] | wt | 43.8 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -13.2) |
| [[A498 (line)]] | wt | 15.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A549 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -17.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[COLO 205 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HEC-1-A (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -20.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.206× (z -9.0) |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0822× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 44.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.5) |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.270× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTG2]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MTRES1]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GMEB2]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 | same gene group; STRING 860 |
| [[ZNF75A]] | +0.65 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TFCP2]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[GPATCH8]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[COIL]] | +0.63 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MRM2]] | +0.63 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZNF3]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LLPH]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MED18]] | +0.61 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TPGS2]] | -0.52 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[LAMP2]] | -0.52 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PGRMC1]] | -0.51 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TKT]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GMEB1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PPP3CB]] | C | PPP3CB's natural level strengthens GMEB1's drug response | PPP3CB's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.27; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.5, 3.8); signed map (-5.0, -16.4). **Vector** length 84.0, 18.3% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.3 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | -10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -10.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | glucocorticoid modulatory element binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,668,778-28,719,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P96PIF, PIF96 |
| Gene groups (HGNC) | SAND domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y692](https://www.uniprot.org/uniprotkb/Q9Y692) (Glucocorticoid modulatory element-binding protein 1):

> Acts as a DNA-binding transcriptional regulator involved in modulating the expression of genes responsive to glucocorticoid signaling. Specifically binds AT-rich DNA motifs known as glucocorticoid modulatory elements (GMEs), repressing or enhancing transcription depending on cellular context. Forms heterodimeric complexes with GMEB2, which enhances its DNA-binding specificity and transcriptional activity. This complex plays a critical role in the repression of glucocorticoid receptor (GR/NR3C1) …

**Summary**, from NCBI Gene [10691](https://www.ncbi.nlm.nih.gov/gene/10691):

> This gene encodes a member of KDWK gene family which associates with GMEB2 protein. The GMEB1-GMEB2 complex is essential for parvovirus DNA replication. Studies in rat for a similar gene suggest that this gene's role is to modulate the transactivation of the glucocorticoid receptor when it is bound to glucocorticoid response elements. Three alternative spliced transcript variants encoding different isoforms exist. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:4370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4370) · Entrez [10691](https://www.ncbi.nlm.nih.gov/gene/10691) · UniProt [Q9Y692](https://www.uniprot.org/uniprotkb/Q9Y692) · Ensembl [ENSG00000162419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162419)

## Data

Gene col 8515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8515); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8515]; `tensor/DDL_lfc|DDL_z.npy` [8515]; `embed/gene_vectors.npy` [8515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8515 or target_col == 8515). Every well: [[GMEB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMEB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
