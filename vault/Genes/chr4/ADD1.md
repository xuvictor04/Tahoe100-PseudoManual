---
symbol: "ADD1"
type: "gene"
col: 1497
ensembl_id: "ENSG00000087274"
name: "adducin 1"
location: "4p16.3"
module: 171
arm: "+"
pooled_cpm: 128.3
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# ADD1

*adducin 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.24× (z +5.4, q 4e-05, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.590× (z -18.4, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDS2]] (+0.70, fdr 7e-06), [[CIZ1]] (+0.64, fdr 7e-06), [[NAP1L4]] (+0.62, fdr 7e-06); moves opposite to [[CAAP1]] (-0.57, fdr 1e-05), [[UTP14A]] (-0.57, fdr 1e-05), [[CEBPZ]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1497.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +5.4 | 4e-05 | 26/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +5.3 | 4e-05 | 31/48 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.0 | 1e-04 | 24/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +4.7 | 3e-04 | 27/49 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.088 | 12/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.15× | +3.3 | 0.088 | 13/47 (LOX-IMVI, HCT15, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.29× | +3.2 | 0.10 | 16/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.13 | 15/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.13 | 13/47 (H4, HCT15, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.590×** | -18.4 | 0e+00 | 36/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.646×** | -10.7 | 2e-24 | 41/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.654×** | -10.4 | 3e-23 | 43/48 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.655×** | -10.4 | 3e-23 | 40/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -9.2 | 4e-18 | 41/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.772×** | -9.0 | 2e-17 | 33/49 (HOP62, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -8.1 | 5e-14 | 41/47 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.722×** | -8.0 | 8e-14 | 29/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.715×** | -7.9 | 1e-13 | 31/48 (A-172, J82, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -6.3 | 2e-08 | 26/48 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.775×** | -6.3 | 2e-08 | 35/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.795×** | -5.6 | 8e-07 | 27/48 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.816×** | -5.0 | 2e-05 | 28/48 (J82, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -4.7 | 8e-05 | 17/48 (HOP62, J82, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.845× | -4.0 | 0.003 | 22/50 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.876× | -3.3 | 0.030 | 11/47 (SW480, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 189 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -18.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 194 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -13.0) |
| [[Hs 766T (line)]] | wt | 155 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -14.8) |
| [[A-172 (line)]] | wt | 189 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -25.4) |
| [[AsPC-1 (line)]] | alt | 137 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -15.3) |
| [[J82 (line)]] | alt | 205 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -22.2) |
| [[A549 (line)]] | wt | 113 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 139 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -12.2) |
| [[HCT15 (line)]] | alt | 232 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.7) |
| [[HS-578T (line)]] | alt | 108 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.3) |
| [[HT-29 (line)]] | alt | 146 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -12.6) |
| [[PANC-1 (line)]] | alt | 95.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.576× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 105 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 194 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 140 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -11.7) |
| [[A-427 (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -15.6) |
| [[AN3 CA (line)]] | alt | 180 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.234× (z -11.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.7) |
| [[H4 (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -17.7) |
| [[LoVo (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 94.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.549× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.579× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.9) |
| [[A498 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.67× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 93.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.2) |
| [[KATO III (line)]] | alt | 91.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.08× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 134 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -10.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.0951× (z -10.6) |
| [[SHP-77 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.511× (z -8.7) |
| [[SNU-423 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -15.7) |
| [[SW 1271 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -11.9) ⚠ transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW 900 (line)]] | alt | 87.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.6) |
| [[SW480 (line)]] | alt | 104 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 155 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDS2]] | +0.70 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[CIZ1]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NAP1L4]] | +0.62 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[RHOA]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 | STRING 440 |
| [[CD99]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.59 | +0.74 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[CAPN1]] | +0.58 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GET1]] | +0.57 | +0.77 / +0.43 | both halves | 3e-05 |  |
| [[USP33]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[SNX4]] | +0.57 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAAP1]] | -0.57 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[UTP14A]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.56 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[METTL1]] | -0.55 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[PPRC1]] | -0.55 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TRMT10C]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.54 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[NTMT1]] | -0.53 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RBMXL1]] | -0.53 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[EGR3]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 | pathway: HALLMARK_APOPTOSIS |
| [[FJX1]] | -0.53 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[NIFK]] | -0.53 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ADD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-10.3, -13.8); signed map (-38.2, -10.6). **Vector** length 97.3, 27.8% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.4 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.8 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +0.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -18.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.9 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Carbamazepine (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | adducin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,843,844-2,930,076 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adducin family |
| Hallmark sets | APOPTOSIS, HEME_METABOLISM |
| Reactome | 12 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Miscellaneous transport and binding events; Apoptotic cleavage of cellular proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P35611](https://www.uniprot.org/uniprotkb/P35611) (Alpha-adducin):

> Membrane-cytoskeleton-associated protein that promotes the assembly of the spectrin-actin network. Binds to calmodulin.

**Summary**, from NCBI Gene [118](https://www.ncbi.nlm.nih.gov/gene/118):

> Adducins are a family of cytoskeletal proteins encoded by three genes (alpha, beta, and gamma). Adducin acts as a heterodimer of the related alpha, beta, or gamma subunits. The protein encoded by this gene represents the alpha subunit. Alpha- and beta-adducin include a protease-resistant N-terminal region and a protease-sensitive, hydrophilic C-terminal region. Adducin binds with high affinity to Ca(2+)/calmodulin and is a substrate for protein kinases A and C. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:243) · Entrez [118](https://www.ncbi.nlm.nih.gov/gene/118) · UniProt [P35611](https://www.uniprot.org/uniprotkb/P35611) · Ensembl [ENSG00000087274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087274)

## Data

Gene col 1497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1497); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1497]; `tensor/DDL_lfc|DDL_z.npy` [1497]; `embed/gene_vectors.npy` [1497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1497 or target_col == 1497). Every well: [[ADD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
