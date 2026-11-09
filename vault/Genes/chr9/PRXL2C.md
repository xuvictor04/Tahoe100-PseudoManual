---
symbol: "PRXL2C"
type: "gene"
col: 8134
ensembl_id: "ENSG00000158122"
name: "peroxiredoxin like 2C"
location: "9q22.33"
module: 17
arm: "+"
pooled_cpm: 18.27
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PRXL2C

*peroxiredoxin like 2C* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.65× (z +7.4, q 6e-11, up in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Terfenadine (drug)]] 0.5 µM: 1.28× (z +3.7, q 0.024, up in 14 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.431× (z -17.6, q 0e+00, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC112]] (+0.68, fdr 1e-05), [[SNX15]] (+0.65, fdr 1e-05), [[FSD1L]] (+0.61, fdr 9e-06); moves opposite to [[NIPBL-DT]] (-0.51, fdr 1e-04), [[SPAG4]] (-0.50, fdr 2e-04), [[ZNF75D]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.4 | 6e-11 | 20/35 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.8 | 1e-06 | 15/27 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.1 | 7e-05 | 15/30 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.024 | 14/45 (A498, SNU-1, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.024 | 10/42 (J82, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.25×** | +3.4 | 0.073 | 13/41 (KATO III, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.084 | 5/46 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.084 | 10/45 (J82, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.24× | +3.1 | 0.12 | 15/41 (SW48, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.431×** | -17.6 | 0e+00 | 40/45 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -10.7 | 2e-24 | 33/45 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.583×** | -8.0 | 3e-13 | 35/45 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -7.7 | 2e-12 | 27/44 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -6.8 | 9e-10 | 29/46 (MIA PaCa-2, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -6.5 | 7e-09 | 28/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.730×** | -4.6 | 3e-04 | 16/46 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.561×** | -4.5 | 6e-04 | 17/36 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -4.2 | 0.001 | 17/45 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.004 | 16/45 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.774×** | -3.6 | 0.014 | 16/45 (CFPAC-1, J82, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.044 | 13/46 (A-172, HOP62, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.659×** | -3.2 | 0.055 | 14/43 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.0 | 0.099 | 3/46 (H4, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.3 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 22.9 | 0 | 5 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0490× (z -10.8) |
| [[RKO (line)]] | wt | 26.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -13.1) |
| [[C32 (line)]] | wt | 13.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0605× (z -13.2) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.4) |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -17.2) |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -9.8) |
| [[J82 (line)]] | alt | 39.2 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -18.0) |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.6) |
| [[SW480 (line)]] | alt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 42.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0489× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -9.2) |
| [[LoVo (line)]] | wt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.262× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.5) |
| [[SHP-77 (line)]] | alt | 9.97 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -10.2) |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.6) |
| [[SW48 (line)]] | wt | 16.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.7) |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC112]] | +0.68 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SNX15]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[FSD1L]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[MCUR1]] ⚠ | +0.61 | +0.57 / +0.46 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ESD]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SLC25A43]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KLF11]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.57 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MOSPD2]] | +0.57 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[NEK1]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[HS1BP3]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TTBK2]] | +0.55 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[CEP290]] | +0.55 | +0.42 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPBL-DT]] | -0.51 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[SPAG4]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[ZNF75D]] | -0.49 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[XNDC1N]] | -0.49 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ZNF876P]] | -0.48 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.48 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | -0.48 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[TMEM11-DT]] | -0.47 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[PHC2-AS1]] | -0.47 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[PDCD6]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DARS1-AS1]] | -0.46 | -0.36 / -0.24 | both halves | 5e-04 |  |
| [[TNRC18]] | -0.46 | -0.36 / -0.38 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises PRXL2C's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without KATNAL1 | 0.047 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[TGFB1I1]] | B | TGFB1I1 activity raises PRXL2C's level | lines that do not express TGFB1I1 (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without TGFB1I1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, ENSG00000234405, TMOD1 |
| [[TOP2A]] | B | TOP2A activity raises PRXL2C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FSD1L]] | C | FSD1L activity raises PRXL2C's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.52× lower at baseline in the lines without FSD1L | 0.033 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-5.0, -2.3); signed map (-21.9, -7.0). **Vector** length 84.9, 17.8% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.5 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -17.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.4 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin like 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:96,639,577-96,655,317 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C9orf21, AAED1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7RTV5](https://www.uniprot.org/uniprotkb/Q7RTV5) (Peroxiredoxin-like 2C):

> May positively regulate ERK1/2 signaling and AKT1 activation leading to HIF1A up-regulation with an increased expression of glycolysis genes and enhanced glycolysis.

**Summary**, from NCBI Gene [195827](https://www.ncbi.nlm.nih.gov/gene/195827):

> Involved in positive regulation of ERK1 and ERK2 cascade and positive regulation of glycolytic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16881) · Entrez [195827](https://www.ncbi.nlm.nih.gov/gene/195827) · UniProt [Q7RTV5](https://www.uniprot.org/uniprotkb/Q7RTV5) · Ensembl [ENSG00000158122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158122)

## Data

Gene col 8134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8134); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8134]; `tensor/DDL_lfc|DDL_z.npy` [8134]; `embed/gene_vectors.npy` [8134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8134 or target_col == 8134). Every well: [[PRXL2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRXL2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
