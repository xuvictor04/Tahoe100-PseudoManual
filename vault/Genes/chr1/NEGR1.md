---
symbol: "NEGR1"
type: "gene"
col: 10229
ensembl_id: "ENSG00000172260"
name: "neuronal growth regulator 1"
location: "1p31.1"
module: 9
arm: "+"
pooled_cpm: 51.24
n_lines_expressing: 26
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 21
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 16
direction_downstream: 16
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NEGR1

*neuronal growth regulator 1* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +19.3, q 0e+00, up in 14 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.648× (z -6.5, q 4e-08, down in 17 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH18]] (+0.64, fdr 7e-06), [[NREP]] (+0.63, fdr 7e-06), [[FMN2]] (+0.63, fdr 1e-05); moves opposite to [[ZNF133]] (-0.47, fdr 5e-05), [[SLC30A6]] (-0.46, fdr 7e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[NREP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +19.3 | 0e+00 | 14/24 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +13.0 | 6e-36 | 10/23 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +12.7 | 7e-35 | 21/24 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.0 | 3e-17 | 10/22 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +9.0 | 3e-17 | 12/24 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +7.9 | 3e-13 | 7/24 (Panc 03.27, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +7.6 | 2e-12 | 22/24 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +7.4 | 8e-12 | 9/22 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +7.2 | 3e-11 | 17/24 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.5 | 4e-09 | 14/24 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.9 | 1e-07 | 14/24 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.7 | 6e-07 | 11/24 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 4e-06 | 18/24 (NCI-H460, SHP-77, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +5.3 | 6e-06 | 16/24 (A498, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.0 | 2e-05 | 7/24 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.0 | 2e-05 | 8/24 (SHP-77, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 13/24 (PANC-1, SNU-423, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.008 | 14/24 (PANC-1, A-427, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.017 | 13/25 (A-427, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.648×** | -6.5 | 4e-08 | 17/24 (J82, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -4.8 | 4e-04 | 7/24 (NCI-H2030, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.778×** | -3.9 | 0.011 | 19/24 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.838× | -3.9 | 0.011 | 6/24 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.616×** | -3.9 | 0.011 | 16/24 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.716×** | -3.7 | 0.019 | 12/24 (PANC-1, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.791×** | -3.7 | 0.021 | 5/24 (HOP62, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.647×** | -3.5 | 0.033 | 11/25 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.855× | -3.5 | 0.034 | 11/24 (HS-578T, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.794×** | -3.4 | 0.039 | 19/24 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.806×** | -3.4 | 0.039 | 13/24 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -3.3 | 0.046 | 18/24 (A-427, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.666×** | -3.3 | 0.049 | 9/24 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.049 | 17/24 (LOX-IMVI, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.050 | 11/24 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -3.1 | 0.075 | 17/24 (PANC-1, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 157 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~4% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.326× (z -9.2) |
| [[A498 (line)]] | wt | 15.9 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +11.6) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.00× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 6 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.155× (z -13.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 55.7 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -11.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.284× (z -9.7) |
| [[A-427 (line)]] | wt | 292 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.216× (z -13.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.337× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 471 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.194× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.4) |
| [[C-33 A (line)]] | alt | 75.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 244 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0615× (z -17.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.217× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 14.2 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.92× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 24.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 76.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0813× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 46.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.12× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0722× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +13.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[RPMI-7951 (line)]] | alt | 34.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 54.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.228× (z -9.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW 900 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.96 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.34 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH18]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NREP]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FMN2]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 | same gene group |
| [[LRRC7]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 | STRING 429 |
| [[UNC5C]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 | same gene group |
| [[ADAMTS3]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[DPY19L2P1]] | +0.57 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[NLGN1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 | STRING 407 |
| [[DPY19L2]] | +0.57 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[ATRNL1]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF133]] | -0.47 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[SLC30A6]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 5, C 11. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NEGR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLIT2]] | B | SLIT2 activity strengthens NEGR1's drug response | lines that do not express SLIT2 (5) vs lines expressing it (19) | the lines without SLIT2 respond the other way (z diff +4.01); strongest at Epirubicin (hydrochloride) 5 µM: 0.50x vs 1.50x (z diff +5.8) | 0.051 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; target measured in part of the lines; artifact flags |
| [[FAM184A]] | B | FAM184A activity raises NEGR1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without FAM184A | 0.074 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[PCDH7]] | B | PCDH7 activity raises NEGR1's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 2.62× lower at baseline in the lines without PCDH7 | 0.085 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[PANTR1]] | B | PANTR1 activity raises NEGR1's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 1.76× lower at baseline in the lines without PANTR1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4 |
| [[B3GALT1]] | C | B3GALT1 activity raises NEGR1's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 4.01× lower at baseline in the lines without B3GALT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises NEGR1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 4.19× lower at baseline in the lines without NLGN1 | 0.009 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises NEGR1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 4.65× lower at baseline in the lines without DPY19L2 | 0.014 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises NEGR1's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 3.71× lower at baseline in the lines without ATRNL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[MPDZ]] | C | MPDZ activity raises NEGR1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 4.83× lower at baseline in the lines without MPDZ | 0.033 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[DMD]] | C | DMD activity raises NEGR1's level | lines that do not express DMD (18) vs lines expressing it (32) | 4.31× lower at baseline in the lines without DMD | 0.039 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises NEGR1's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 2.50× lower at baseline in the lines without ODAD2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | NEGR1 activity raises NREP's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.80× lower at baseline in the lines without NEGR1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1 |
| [[MMP16]] | C | NEGR1 activity raises MMP16's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 5.67× lower at baseline in the lines without NEGR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[ATRNL1]] | C | NEGR1 activity raises ATRNL1's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 4.10× lower at baseline in the lines without NEGR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[MPDZ]] | C | NEGR1 activity raises MPDZ's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 7.16× lower at baseline in the lines without NEGR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[CAMK4]] | C | NEGR1 activity raises CAMK4's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 5.22× lower at baseline in the lines without NEGR1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[NLGN1]] | C | NEGR1 activity raises NLGN1's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 6.17× lower at baseline in the lines without NEGR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[B3GALT1]] | C | NEGR1 activity raises B3GALT1's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without NEGR1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[DPY19L2]] | C | NEGR1 activity raises DPY19L2's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.95× lower at baseline in the lines without NEGR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[EGFEM1P]] | C | NEGR1 activity raises EGFEM1P's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.05× lower at baseline in the lines without NEGR1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[TMEM108]] | C | NEGR1 activity raises TMEM108's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.16× lower at baseline in the lines without NEGR1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[FAT4]] | C | NEGR1 activity raises FAT4's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 4.44× lower at baseline in the lines without NEGR1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[TRHDE]] | C | NEGR1 activity raises TRHDE's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without NEGR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 30.2); signed map (37.2, 33.8). **Vector** length 87.3, 26.6% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.7 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.5 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | neuronal growth regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:71,395,943-72,282,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KILON, MGC46680, Ntra, IGLON4 |
| Gene groups (HGNC) | I-set domain containing; IgLON cell adhesion molecules |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3B1](https://www.uniprot.org/uniprotkb/Q7Z3B1) (Neuronal growth regulator 1):

> May be involved in cell-adhesion. May function as a trans-neural growth-promoting factor in regenerative axon sprouting in the mammalian brain (By similarity).

**Summary**, from NCBI Gene [257194](https://www.ncbi.nlm.nih.gov/gene/257194):

> Enables transmembrane transporter binding activity. Acts upstream of or within several processes, including cholesterol homeostasis; protein localization to plasma membrane raft; and regulation of protein stability. Located in late endosome and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17302) · Entrez [257194](https://www.ncbi.nlm.nih.gov/gene/257194) · UniProt [Q7Z3B1](https://www.uniprot.org/uniprotkb/Q7Z3B1) · Ensembl [ENSG00000172260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172260)

## Data

Gene col 10229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10229); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10229]; `tensor/DDL_lfc|DDL_z.npy` [10229]; `embed/gene_vectors.npy` [10229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10229 or target_col == 10229). Every well: [[NEGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
