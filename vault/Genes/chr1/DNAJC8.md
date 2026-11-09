---
symbol: "DNAJC8"
type: "gene"
col: 4751
ensembl_id: "ENSG00000126698"
name: "DnaJ heat shock protein family (Hsp40) member C8"
location: "1p35.3"
module: 51
arm: "+"
pooled_cpm: 69.11
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# DNAJC8

*DnaJ heat shock protein family (Hsp40) member C8* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.76× (z +18.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.51× (z +9.3, q 1e-18, up in 44 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP91]] (+0.69, fdr 7e-06), [[C11orf58]] (+0.69, fdr 7e-06), [[DPP8]] (+0.68, fdr 1e-05); moves opposite to [[STK32C]] (-0.70, fdr 7e-06), [[EEF1AKMT4]] (-0.64, fdr 1e-05), [[PDXP]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.76×** | +18.5 | 0e+00 | 49/49 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.14×** | +16.2 | 0e+00 | 43/43 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.59×** | +15.2 | 0e+00 | 47/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.18×** | +11.9 | 1e-30 | 43/44 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.72×** | +11.4 | 5e-28 | 46/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.51×** | +9.3 | 1e-18 | 44/49 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +8.4 | 4e-15 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +7.2 | 4e-11 | 43/48 (HT-29, LoVo, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +6.8 | 6e-10 | 42/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.68×** | +6.1 | 5e-08 | 37/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +5.8 | 3e-07 | 42/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.64×** | +5.8 | 3e-07 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.7 | 6e-07 | 33/48 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.63×** | +5.6 | 1e-06 | 40/47 (LoVo, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.54×** | +5.1 | 1e-05 | 39/48 (SNU-1, H4, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.8 | 6e-05 | 36/48 (A-172, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +3.9 | 0.002 | 29/48 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.007 | 26/48 (NCI-H1792, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.023 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.027 | 29/48 (RPMI-7951, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.051 | 27/47 (HOP62, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.052 | 19/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.1 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +20.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.48× (z +15.5) | — |
| [[LoVo (line)]] | wt | 31.4 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.36× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 82.0 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 49.1 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +21.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.17× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 97.8 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 78.9 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +20.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.74× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 83.1 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.31× (z +9.5) | — |
| [[A-172 (line)]] | wt | 46.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.74× (z +9.7) | — |
| [[A549 (line)]] | wt | 39.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.14× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 44.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +14.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +8.6) | — |
| [[J82 (line)]] | alt | 122 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 46.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.88× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 69.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.90× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 67.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 57.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 52.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[COLO 205 (line)]] | alt | 57.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +15.1) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 57.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.44× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HT-29 (line)]] | alt | 64.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.17× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.0) | — |
| [[KATO III (line)]] | alt | 72.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 57.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 81.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 82.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[H4 (line)]] | wt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.15× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 56.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 70.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW 900 (line)]] | alt | 58.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 62.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 78.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 97.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 85.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 77.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[LS 180 (line)]] | wt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 98.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SHP-77 (line)]] | alt | 72.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW48 (line)]] | wt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP91]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[C11orf58]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[DPP8]] | +0.68 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.67 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[USP40]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ATRX]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GATB]] | +0.65 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[TASOR]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.64 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ANKLE2]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[LZIC]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.64 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK32C]] | -0.70 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | -0.64 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[PDXP]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SLC37A3]] | -0.62 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[MPG]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[AFMID]] | -0.60 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CARD19]] | -0.59 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ELP2]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD37]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.58 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[TAF5]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[RGS10]] | -0.57 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAJC8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.5, 9.5); signed map (12.0, -27.7). **Vector** length 72.0, 24.0% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.2 | +15.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -2.6 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -2.6 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.4 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -2.4 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.6 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,199,456-28,233,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPF31 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O75937](https://www.uniprot.org/uniprotkb/O75937) (DnaJ homolog subfamily C member 8):

> Suppresses polyglutamine (polyQ) aggregation of ATXN3 in neuronal cells.

**Summary**, from NCBI Gene [22826](https://www.ncbi.nlm.nih.gov/gene/22826):

> Enables Hsp70 protein binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15470) · Entrez [22826](https://www.ncbi.nlm.nih.gov/gene/22826) · UniProt [O75937](https://www.uniprot.org/uniprotkb/O75937) · Ensembl [ENSG00000126698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126698)

## Data

Gene col 4751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4751); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4751]; `tensor/DDL_lfc|DDL_z.npy` [4751]; `embed/gene_vectors.npy` [4751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4751 or target_col == 4751). Every well: [[DNAJC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
