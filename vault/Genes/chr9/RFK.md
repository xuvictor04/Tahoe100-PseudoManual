---
symbol: "RFK"
type: "gene"
col: 5635
ensembl_id: "ENSG00000135002"
name: "riboflavin kinase"
location: "9q21.13"
module: 216
arm: "+"
pooled_cpm: 21.04
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# RFK

*riboflavin kinase* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.48× (z +20.6, q 0e+00, up in 39 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.21× (z +9.6, q 6e-20, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (SW48 0.0625×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFR3A]] (+0.67, fdr 8e-06), [[VEZF1]] (+0.61, fdr 1e-05), [[COMMD8]] (+0.60, fdr 7e-06); moves opposite to [[UBOX5]] (-0.63, fdr 1e-05), [[DRD4]] (-0.63, fdr 9e-06), [[RNF121]] (-0.63, fdr 7e-06).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.48×** | +20.6 | 0e+00 | 39/40 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.59×** | +17.8 | 0e+00 | 26/27 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.39×** | +13.7 | 3e-40 | 31/34 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.09×** | +12.7 | 1e-34 | 35/46 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.45×** | +10.5 | 2e-23 | 40/46 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.24×** | +9.8 | 1e-20 | 40/47 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.21×** | +9.6 | 6e-20 | 41/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +9.4 | 4e-19 | 36/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +8.8 | 1e-16 | 36/44 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **2.07×** | +8.5 | 9e-16 | 36/44 (A549, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.95×** | +8.1 | 2e-14 | 37/47 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.85×** | +7.5 | 4e-12 | 35/48 (PANC-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.84×** | +7.4 | 6e-12 | 37/46 (LoVo, BT-474, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.81×** | +7.2 | 2e-11 | 36/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.6 | 2e-09 | 33/48 (A498, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 3e-05 | 27/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.2 | 6e-04 | 22/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.002 | 21/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.006 | 18/46 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.019 | 18/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.038 | 14/47 (J82, HOP62, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.049 | 16/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.061 | 8/43 (A498, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +2.8 | 0.075 | 6/48 (A-172, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +2.8 | 0.079 | 19/48 (A498, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5635.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (SW48 0.0625×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.578× | -3.5 | 0.32 | 14/46 (SW 1271, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 28.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.88× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.07× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.23× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 14.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 11.3 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 36.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.56× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 7.02 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.81× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 32.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 19.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.27× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 30.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 26.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.3× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.16× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.2) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0625× (z -9.2) |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3A]] | +0.67 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[VEZF1]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.60 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CHRAC1]] | +0.59 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[GMFB]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TIGD2]] | +0.57 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[VPS13C]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB33]] | +0.56 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ISOC1]] | +0.56 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[AKAP11]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GCFC2]] | +0.55 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBOX5]] | -0.63 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[DRD4]] | -0.63 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[RNF121]] | -0.63 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[FAM156A]] | -0.62 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[WDR37]] | -0.62 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[RARS2]] | -0.61 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.60 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SMPD4BP]] | -0.59 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[MED26]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB49]] | -0.58 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SDHAP4-1]] | -0.57 | -0.65 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.7, -2.6); signed map (6.2, -35.3). **Vector** length 64.7, 12.8% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.4 | +20.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.2 | +17.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.2 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -1.4 | +8.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -1.2 | +7.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | riboflavin kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:76,385,526-76,394,517 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11149, RIFK |
| Gene groups (HGNC) | Flavoproteins; Vitamin/cofactor kinases |
| Reactome | 3 pathways, smallest: Vitamin B2 (riboflavin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969G6](https://www.uniprot.org/uniprotkb/Q969G6) (Riboflavin kinase):

> Catalyzes the phosphorylation of riboflavin (vitamin B2) to form flavin-mononucleotide (FMN), hence rate-limiting enzyme in the synthesis of FAD. Essential for TNF-induced reactive oxygen species (ROS) production. Through its interaction with both TNFRSF1A and CYBA, physically and functionally couples TNFRSF1A to NADPH oxidase. TNF-activation of RFK may enhance the incorporation of FAD in NADPH oxidase, a critical step for the assembly and activation of NADPH oxidase.

**Summary**, from NCBI Gene [55312](https://www.ncbi.nlm.nih.gov/gene/55312):

> Riboflavin kinase (RFK; EC 2.7.1.26) is an essential enzyme that catalyzes the phosphorylation of riboflavin (vitamin B2) to form flavin mononucleotide (FMN), an obligatory step in vitamin B2 utilization and flavin cofactor synthesis (Karthikeyan et al., 2003 [PubMed 12623014]).[supplied by OMIM, Nov 2009]

**Accessions** — [HGNC:30324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30324) · Entrez [55312](https://www.ncbi.nlm.nih.gov/gene/55312) · UniProt [Q969G6](https://www.uniprot.org/uniprotkb/Q969G6) · Ensembl [ENSG00000135002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135002)

## Data

Gene col 5635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5635); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5635]; `tensor/DDL_lfc|DDL_z.npy` [5635]; `embed/gene_vectors.npy` [5635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5635 or target_col == 5635). Every well: [[RFK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
