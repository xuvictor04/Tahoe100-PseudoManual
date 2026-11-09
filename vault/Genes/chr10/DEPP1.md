---
symbol: "DEPP1"
type: "gene"
col: 9135
ensembl_id: "ENSG00000165507"
name: "DEPP autophagy regulator 1"
location: "10q11.21"
module: 79
arm: "+"
pooled_cpm: 37.33
n_lines_expressing: 29
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 11
direction_downstream: 18
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# DEPP1

*DEPP autophagy regulator 1* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +5.9, q 2e-06, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.317× (z -10.7, q 6e-24, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADM]] (+0.71, fdr 7e-06), [[HILPDA]] (+0.66, fdr 7e-06), [[SAP30]] (+0.65, fdr 1e-05); moves opposite to [[EPM2A]] (-0.59, fdr 4e-05), [[PCBD2]] (-0.58, fdr 3e-05), [[MAPKAPK5]] (-0.57, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RASSF4]] → it (grade B ⚠); 18 go from it, the strongest it → [[VEGFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +5.9 | 2e-06 | 14/27 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 0.003 | 13/27 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +4.3 | 0.004 | 14/27 (AsPC-1, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.008 | 13/26 (A-172, Hs 766T, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.024 | 13/26 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.058 | 10/27 (Hs 766T, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.4 | 0.062 | 14/27 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.12 | 9/27 (A-172, HOP62, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.26× | +3.1 | 0.13 | 14/27 (PANC-1, CFPAC-1, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.13 | 9/26 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.317×** | -10.7 | 6e-24 | 23/26 (A-172, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.331×** | -9.9 | 1e-20 | 24/27 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.399×** | -8.2 | 3e-14 | 23/24 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -7.7 | 2e-12 | 19/21 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.426×** | -7.6 | 2e-12 | 23/27 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.463×** | -7.2 | 7e-11 | 23/26 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.483×** | -6.8 | 1e-09 | 21/27 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.501×** | -6.2 | 4e-08 | 20/25 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.627×** | -6.1 | 5e-08 | 19/27 (A-172, H4, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.508×** | -5.8 | 3e-07 | 19/24 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.596×** | -4.8 | 8e-05 | 20/27 (SW 1088, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.700×** | -4.7 | 1e-04 | 20/25 (A-172, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.615×** | -4.5 | 3e-04 | 17/27 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -4.4 | 4e-04 | 17/27 (A498, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -4.2 | 1e-03 | 19/27 (A-172, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.646×** | -3.8 | 0.004 | 15/27 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -3.7 | 0.006 | 16/27 (A-172, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.679×** | -3.6 | 0.010 | 18/27 (RPMI-7951, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.714×** | -3.1 | 0.050 | 8/26 (SNU-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.792×** | -3.0 | 0.062 | 17/27 (SHP-77, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.8 | 5 (4 ⚠) | 10 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.45× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -20.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -13.6) |
| [[A-172 (line)]] | wt | 135 | 2 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.11× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0114× (z -36.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -27.7) |
| [[RPMI-7951 (line)]] | alt | 89.9 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0436× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0856× (z -15.8) |
| [[SNU-423 (line)]] | alt | 153 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0528× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -15.8) |
| [[HOP62 (line)]] | alt | 112 | 2 (1 ⚠) | 8 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 7.57× (z +13.1) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.82× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0651× (z -16.9) |
| [[HS-578T (line)]] | alt | 109 | 0 | 10 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0174× (z -25.7) |
| [[A498 (line)]] | wt | 64.7 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 60.4 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 64.4 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -12.1) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -10.7) |
| [[H4 (line)]] | wt | 123 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -19.7) |
| [[Hs 766T (line)]] | wt | 55.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0680× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0796× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0840× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 63.5 | 2 (1 ⚠) | 2 | [[Harringtonine (drug)]] 0.5 µM 5.84× (z +10.5) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 5.48× (z +10.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0705× (z -15.3) |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -18.6) |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0455× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.4) |
| [[SW 1088 (line)]] | alt | 96.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.176× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.177× (z -8.6) |
| [[J82 (line)]] | alt | 11.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -16.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.7) |
| [[KATO III (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0288× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0204× (z -19.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADM]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SAP30]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RNF24]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[PLIN2]] | +0.60 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[RNASE4]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[THEMIS2]] | +0.60 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[RASSF4]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[EFNA3]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[DUSP1]] | +0.58 | +0.30 / +0.62 | both halves | 2e-04 |  |
| [[AVPI1]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[FAM13A]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | -0.59 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[PCBD2]] | -0.58 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.57 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMX3]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[DARS2]] | -0.56 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[IPO5]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ILF3]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MACROH2A1]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[NAA50]] | -0.53 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[DCTD]] | -0.53 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[RCC2]] | -0.52 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ALG8]] | -0.52 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF4]] | B | RASSF4 activity raises DEPP1's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 5.98× lower at baseline in the lines without RASSF4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers DEPP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity raises DEPP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[THEMIS2]] | B | THEMIS2 activity raises DEPP1's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without THEMIS2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[MAP2K2]] | B | MAP2K2 activity lowers DEPP1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SAA1]] | B | SAA1 activity raises DEPP1's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.51× lower at baseline in the lines without SAA1 | 0.085 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[CXXC5]] | B | CXXC5 activity raises DEPP1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 3.69× lower at baseline in the lines without CXXC5 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[CA9]] | B | CA9 activity raises DEPP1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without CA9 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[LOX]] | C | LOX activity raises DEPP1's level | lines that do not express LOX (31) vs lines expressing it (19) | 6.83× lower at baseline in the lines without LOX | 0.003 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[CA12]] | C | CA12 activity raises DEPP1's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.10× lower at baseline in the lines without CA12 | 0.006 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[TNS1]] | C | TNS1 activity raises DEPP1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 3.53× lower at baseline in the lines without TNS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEGFA]] | B | DEPP1 activity raises VEGFA's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without DEPP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[RASSF4]] | B | DEPP1 activity raises RASSF4's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without DEPP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[RAB40C]] | B | DEPP1 activity raises RAB40C's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.42× lower at baseline in the lines without DEPP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[FAM13A]] | B | DEPP1 activity raises FAM13A's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without DEPP1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[THEMIS2]] | B | DEPP1 activity raises THEMIS2's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without DEPP1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[PPP1R3B]] | B | DEPP1 activity raises PPP1R3B's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.53× lower at baseline in the lines without DEPP1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[NDRG1]] | B | DEPP1 activity raises NDRG1's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without DEPP1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[MCM9]] | B | DEPP1 activity lowers MCM9's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.42× higher at baseline in the lines without DEPP1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[CXXC5]] | B | DEPP1 activity raises CXXC5's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without DEPP1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[SSBP2]] | B | DEPP1 activity raises SSBP2's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.55× lower at baseline in the lines without DEPP1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[HPS3]] | B | DEPP1 activity raises HPS3's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without DEPP1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[ZNF395]] | B | DEPP1 activity raises ZNF395's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.80× lower at baseline in the lines without DEPP1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, -13.9); signed map (-32.8, 24.9). **Vector** length 97.0, 28.5% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.50 to 16); *hypoxia* (control, mean cos +0.51 to 5); *glycolysis* (hallmark, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.3 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -5.9 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DEPP autophagy regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:44,970,981-44,978,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEPP, FIG, Fseg; previously C10orf10 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTK1](https://www.uniprot.org/uniprotkb/Q9NTK1) (Protein DEPP1):

> Acts as a critical modulator of FOXO3-induced autophagy via increased cellular ROS.

**Summary**, from NCBI Gene [11067](https://www.ncbi.nlm.nih.gov/gene/11067):

> The expression of this gene is induced by fasting as well as by progesterone. The protein encoded by this gene contains a t-synaptosome-associated protein receptor (SNARE) coiled-coil homology domain and a peroxisomal targeting signal. Production of the encoded protein leads to phosphorylation and activation of the transcription factor ELK1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23355) · Entrez [11067](https://www.ncbi.nlm.nih.gov/gene/11067) · UniProt [Q9NTK1](https://www.uniprot.org/uniprotkb/Q9NTK1) · Ensembl [ENSG00000165507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165507)

## Data

Gene col 9135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9135); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9135]; `tensor/DDL_lfc|DDL_z.npy` [9135]; `embed/gene_vectors.npy` [9135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9135 or target_col == 9135). Every well: [[DEPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
