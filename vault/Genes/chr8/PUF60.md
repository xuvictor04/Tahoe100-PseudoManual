---
symbol: "PUF60"
type: "gene"
col: 11069
ensembl_id: "ENSG00000179950"
name: "poly(U) binding splicing factor 60"
location: "8q24.3"
module: 16
arm: "+"
pooled_cpm: 21.14
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PUF60

*poly(U) binding splicing factor 60* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +13.3, q 2e-37, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.20× (z +10.3, q 3e-22, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.768× (z -4.9, q 6e-04, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRWD1]] (+0.78, fdr 7e-06), [[SRCAP]] (+0.78, fdr 7e-06), [[TMEM185B]] (+0.75, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.73, fdr 7e-06), [[RAB6A]] (-0.69, fdr 7e-06), [[DPM1]] (-0.65, fdr 8e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF518B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.06×** | +13.3 | 2e-37 | 36/47 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +10.3 | 3e-22 | 39/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.18×** | +9.7 | 5e-20 | 39/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +9.4 | 1e-18 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.90×** | +8.4 | 7e-15 | 41/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.99×** | +7.4 | 1e-11 | 38/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.58×** | +5.9 | 3e-07 | 26/43 (A-427, SK-MEL-2, …) | all doses, flat | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.9 | 3e-07 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.8 | 3e-07 | 33/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 3e-07 | 35/47 (HOP62, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.50×** | +5.3 | 6e-06 | 32/47 (SW480, NCI-H460, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +5.1 | 2e-05 | 24/47 (J82, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +5.1 | 2e-05 | 25/46 (A498, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.52×** | +5.1 | 2e-05 | 21/39 (PANC-1, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.48×** | +4.9 | 4e-05 | 26/44 (C32, LoVo, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +4.6 | 1e-04 | 25/45 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.6 | 1e-04 | 23/47 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.005 | 20/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +3.7 | 0.006 | 19/47 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.010 | 14/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.010 | 16/45 (PANC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +3.1 | 0.043 | 7/44 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.9 | 6e-04 | 29/47 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -4.7 | 7e-04 | 23/46 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.804×** | -4.0 | 0.011 | 22/48 (PANC-1, BT-474, …) | top dose only | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.046 | 15/47 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.762×** | -3.5 | 0.046 | 18/47 (H4, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.771×** | -3.4 | 0.068 | 18/47 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.782× | -3.2 | 0.11 | 17/48 (A498, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -3.1 | 0.16 | 16/48 (A-172, NCI-H1792, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +10.3) | — |
| [[C32 (line)]] | wt | 20.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.23× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 11.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.63× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 30.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +8.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 47.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.5) |
| [[SNU-423 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRWD1]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.71 | +0.63 / +0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RTL6]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.71 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[EIF2B5]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[PRRC2A]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RBM12]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 | same gene group |
| [[CSTF2T]] | +0.70 | +0.62 / +0.74 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions |
| [[ZKSCAN2]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.73 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.69 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[DPM1]] | -0.65 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[APTR]] | -0.65 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.64 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[ABHD18]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[KLHL7]] | -0.64 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[SGK3]] | -0.63 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[MAX]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[IFI27L1]] | -0.61 | -0.52 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF518B]] | B | ZNF518B activity lowers PUF60's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.20× higher at baseline in the lines without ZNF518B | 0.072 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-17.8, -2.0); signed map (1.3, -32.7). **Vector** length 90.2, 20.6% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.4 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +10.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | +4.7 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.7 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.3 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.1 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | poly(U) binding splicing factor 60 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,816,344-143,830,709 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FIR, SIAHBP1, RoBPI |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal A complex |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHX1](https://www.uniprot.org/uniprotkb/Q9UHX1) (Poly(U)-binding-splicing factor PUF60):

> DNA- and RNA-binding protein, involved in several nuclear processes such as pre-mRNA splicing, apoptosis and transcription regulation. In association with FUBP1 regulates MYC transcription at the P2 promoter through the core-TFIIH basal transcription factor. Acts as a transcriptional repressor through the core-TFIIH basal transcription factor. Represses FUBP1-induced transcriptional activation but not basal transcription. Decreases ERCC3 helicase activity. Does not repress TFIIH-mediated …

**Summary**, from NCBI Gene [22827](https://www.ncbi.nlm.nih.gov/gene/22827):

> This gene encodes a nucleic acid-binding protein that plays a role in a variety of nuclear processes, including pre-mRNA splicing and transcriptional regulation. The encoded protein forms a complex with the far upstream DNA element (FUSE) and FUSE-binding protein at the myelocytomatosis oncogene (MYC) promoter. This complex represses MYC transcription through the core-TFIIH basal transcription factor. Alternatively spliced transcript variants encoding multiple isoforms have been observed for …

**Accessions** — [HGNC:17042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17042) · Entrez [22827](https://www.ncbi.nlm.nih.gov/gene/22827) · UniProt [Q9UHX1](https://www.uniprot.org/uniprotkb/Q9UHX1) · Ensembl [ENSG00000179950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179950)

## Data

Gene col 11069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11069); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11069]; `tensor/DDL_lfc|DDL_z.npy` [11069]; `embed/gene_vectors.npy` [11069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11069 or target_col == 11069). Every well: [[PUF60 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUF60.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
