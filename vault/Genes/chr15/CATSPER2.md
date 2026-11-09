---
symbol: "CATSPER2"
type: "gene"
col: 9352
ensembl_id: "ENSG00000166762"
name: "cation channel sperm associated 2"
location: "15q15.3"
module: 25
arm: "-"
pooled_cpm: 23.4
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# CATSPER2

*cation channel sperm associated 2* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +9.9, q 2e-20, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.538× (z -10.6, q 2e-23, down in 30 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.615× (z -8.7, q 1e-15, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIP5K1]] (+0.82, fdr 7e-06, ⚠ same locus), [[ACAP1]] (+0.52, fdr 6e-05), [[MYO1D]] (+0.50, fdr 2e-04), [[COX17]] (+0.49, fdr 3e-05); moves opposite to [[TMX1]] (-0.54, fdr 3e-05), [[STX16]] (-0.53, fdr 2e-04), [[CAPRIN1]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BSPRY]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +9.9 | 2e-20 | 30/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +8.9 | 2e-16 | 38/48 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +8.1 | 9e-14 | 33/48 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +8.0 | 1e-13 | 35/48 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 8e-12 | 30/46 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +7.2 | 6e-11 | 27/48 (BT-474, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +7.0 | 2e-10 | 27/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.4 | 6e-06 | 2/48 (NCI-H23, NCI-H2030) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 4e-04 | 20/46 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.4 | 6e-04 | 16/48 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.014 | 11/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.054 | 9/44 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.073 | 12/44 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.083 | 7/48 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.091 | 11/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -10.6 | 2e-23 | 30/43 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -8.7 | 1e-15 | 31/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -8.3 | 2e-14 | 36/48 (LoVo, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -7.6 | 5e-12 | 26/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -7.5 | 6e-12 | 32/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -7.4 | 2e-11 | 20/34 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -7.0 | 2e-10 | 27/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -6.8 | 8e-10 | 29/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.777×** | -6.3 | 1e-08 | 23/48 (PANC-1, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.739×** | -5.4 | 4e-06 | 20/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -5.1 | 1e-05 | 21/45 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.774×** | -4.5 | 3e-04 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.782×** | -4.4 | 6e-04 | 23/47 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.820×** | -3.5 | 0.018 | 10/47 (NCI-H1792, CHP-212, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.699×** | -3.3 | 0.033 | 12/27 (HOP62, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.835× | -3.2 | 0.046 | 5/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.2 | 1 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -14.9) |
| [[COLO 205 (line)]] | alt | 70.3 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -11.2) |
| [[KATO III (line)]] | alt | 34.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H1573 (line)]] | alt | 31.0 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.337× (z -9.4) |
| [[LS 180 (line)]] | wt | 28.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.215× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 16.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.05 µM 0.282× (z -10.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 26.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -9.7) |
| [[SW48 (line)]] | wt | 32.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Menadione (drug)]] 0.05 µM 0.146× (z -10.1) |
| [[A-427 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[HEC-1-A (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.113× (z -9.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -13.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 21.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -11.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.477× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0833× (z -16.6) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.263× (z -9.4) |
| [[SW480 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 9 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIP5K1]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 | STRING 930; ⚠ same locus (38.3 kb, same strand: neighbours can correlate without regulation) |
| [[ACAP1]] | +0.52 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[MYO1D]] | +0.50 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[COX17]] | +0.49 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZBTB46]] | +0.49 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[TUBB2B]] | +0.49 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[KLF2]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[POLD4]] | +0.48 | +0.26 / +0.45 | both halves | 3e-04 |  |
| [[RPL18]] ⚠ | +0.48 | +0.26 / +0.55 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CLIP2]] | +0.48 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[RPL36AL]] ⚠ | +0.47 | +0.25 / +0.52 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMB2P1]] | +0.47 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[IL10RB]] | +0.47 | +0.43 / +0.43 | both halves | 4e-05 |  |
| [[GABARAPL2]] | +0.47 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[JUND]] | +0.47 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX1]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[STX16]] | -0.53 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[CAPRIN1]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[EMC1]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.52 | -0.29 / -0.61 | both halves | 3e-04 |  |
| [[ADI1]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ZMPSTE24]] | -0.50 | -0.22 / -0.56 | both halves | 6e-04 |  |
| [[AP2M1]] | -0.50 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ARL5A]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[FKBP9]] | -0.50 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[NAXD]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[COX11]] | -0.50 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSPRY]] | B | BSPRY activity raises CATSPER2's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.68× lower at baseline in the lines without BSPRY | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CATSPER2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CATSPER2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.1, -22.1); signed map (-5.8, 11.6). **Vector** length 76.4, 14.6% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.7 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cation channel sperm associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,628,503-43,668,118 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cation channels sperm associated; CatSpermasome complex |
| Reactome | 3 pathways, smallest: Sperm Motility And Taxes; Fertilization; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P56](https://www.uniprot.org/uniprotkb/Q96P56) (Cation channel sperm-associated protein 2):

> Pore-forming subunit of the CatSper complex, a sperm-specific voltage-gated calcium channel, that plays a central role in calcium-dependent physiological responses essential for successful fertilization, such as sperm hyperactivation, acrosome reaction and chemotaxis towards the oocyte.

**Summary**, from NCBI Gene [117155](https://www.ncbi.nlm.nih.gov/gene/117155):

> This gene encodes a member of a family of cation channel proteins that localize to the flagellum of spermatozoa. Defects at this locus causes male infertility. Alternatively spliced transcript variants have been observed at this locus. Readthrough transcription originates upstream of this locus in diphosphoinositol pentakisphosphate kinase 1 pseudogene 1 and is represented by GeneID:110006325. Related pseudogenes are found next to this locus on chromosome 15 and on chromosome 5. [provided by …

**Accessions** — [HGNC:18810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18810) · Entrez [117155](https://www.ncbi.nlm.nih.gov/gene/117155) · UniProt [Q96P56](https://www.uniprot.org/uniprotkb/Q96P56) · Ensembl [ENSG00000166762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166762)

## Data

Gene col 9352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9352); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9352]; `tensor/DDL_lfc|DDL_z.npy` [9352]; `embed/gene_vectors.npy` [9352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9352 or target_col == 9352). Every well: [[CATSPER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
