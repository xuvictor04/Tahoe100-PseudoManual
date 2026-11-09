---
symbol: "PDZD7"
type: "gene"
col: 11863
ensembl_id: "ENSG00000186862"
name: "PDZ domain containing 7"
location: "10q24.31"
module: 100
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# PDZD7

*PDZ domain containing 7* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 4.28× (z +14.7, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.329× (z -11.3, q 7e-27, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC29A4]] (+0.71, fdr 7e-06), [[MAPT]] (+0.71, fdr 1e-05), [[PEDS1]] (+0.70, fdr 7e-06); moves opposite to [[WARS2-AS1]] (-0.69, fdr 1e-05), [[ST7L]] (-0.68, fdr 2e-05), [[DPH5-DT]] (-0.67, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAN1C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **4.28×** | +14.7 | 0e+00 | 40/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.21×** | +14.6 | 1e-45 | 41/42 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.08×** | +14.3 | 8e-44 | 42/46 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.01×** | +14.1 | 8e-43 | 40/47 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.38×** | +12.4 | 2e-33 | 40/45 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +11.4 | 5e-28 | 8/9 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +11.3 | 6e-28 | 23/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.79×** | +10.4 | 2e-23 | 29/33 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +8.7 | 2e-16 | 13/21 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.28×** | +8.4 | 4e-15 | 24/38 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.34×** | +7.8 | 4e-13 | 29/40 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.56×** | +4.3 | 7e-04 | 5/21 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +4.3 | 9e-04 | 7/32 (LS 180, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 0.001 | 11/40 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.1 | 0.002 | 2/12 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Brivudine (drug)]] 0.5 µM |  | **1.74×** | +4.0 | 0.002 | 4/41 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.004 | 6/43 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 8/46 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.010 | 8/36 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.020 | 3/29 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.329×** | -11.3 | 7e-27 | 30/47 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.333×** | -11.2 | 2e-26 | 24/32 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.513×** | -9.6 | 1e-19 | 25/34 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.400×** | -9.3 | 2e-18 | 28/42 (C32, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.432×** | -8.5 | 1e-15 | 27/40 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.418×** | -8.5 | 1e-15 | 25/40 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.503×** | -7.0 | 2e-10 | 24/43 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.595×** | -5.3 | 9e-06 | 17/40 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -5.0 | 3e-05 | 17/46 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.632×** | -4.7 | 2e-04 | 16/41 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.633×** | -4.7 | 2e-04 | 14/45 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.639×** | -4.3 | 8e-04 | 13/39 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -4.0 | 0.002 | 9/38 (C32, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.474×** | -4.0 | 0.003 | 8/31 (C32, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -3.4 | 0.028 | 15/30 (C32, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.740×** | -3.1 | 0.074 | 13/45 (NCI-H460, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 16.8 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0381× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.114× (z -14.5) |
| [[HT-29 (line)]] | alt | 6.53 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0661× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 8.31 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0513× (z -10.5) |
| [[A-172 (line)]] | wt | 9.98 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0502× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -8.9) |
| [[HOP62 (line)]] | alt | 5.46 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0216× (z -15.1) |
| [[J82 (line)]] | alt | 6.05 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -15.7) |
| [[PANC-1 (line)]] | alt | 3.57 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -10.1) |
| [[SW480 (line)]] | alt | 3.73 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 6.60 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0632× (z -9.0) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.0613× (z -8.7) |
| [[SNU-423 (line)]] | alt | 8.33 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0167× (z -16.8) |
| [[A498 (line)]] | wt | 3.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0972× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 3.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0565× (z -10.0) |
| [[A-427 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC29A4]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[MAPT]] | +0.71 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.70 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.70 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[CDON]] | +0.68 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CIB2]] | +0.68 | +0.50 / +0.61 | both halves | 1e-05 | STRING 777 |
| [[MGST3]] | +0.67 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[GPR155]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.67 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[UBTD1]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | -0.69 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ST7L]] | -0.68 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[DPH5-DT]] | -0.67 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ATXN7L1]] | -0.66 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RGS5]] | -0.66 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[INTS14]] | -0.65 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.64 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.64 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ENOX2]] | -0.64 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.63 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RFX3-DT]] | -0.63 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAN1C1]] | B | MAN1C1 activity raises PDZD7's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without MAN1C1 | 0.061 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[FYN]] | B | FYN activity raises PDZD7's level | lines that do not express FYN (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without FYN | 0.064 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[TIMP2]] | C | TIMP2 activity raises PDZD7's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without TIMP2 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |
| [[SFXN3]] | C | SFXN3 activity raises PDZD7's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without SFXN3 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.3, -2.1); signed map (-28.9, 22.0). **Vector** length 74.0, 13.5% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +14.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PDZ domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:101,007,679-101,032,295 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23209, bA108L7.8; previously PDZK7, DFNB57 |
| Gene groups (HGNC) | PDZ domain containing; USH2 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5P4](https://www.uniprot.org/uniprotkb/Q9H5P4) (PDZ domain-containing protein 7):

> In cochlear developing hair cells, essential in organizing the USH2 complex at stereocilia ankle links. Blocks inhibition of adenylate cyclase activity mediated by ADGRV1.

**Summary**, from NCBI Gene [79955](https://www.ncbi.nlm.nih.gov/gene/79955):

> This gene encodes a ciliary protein homologous to proteins which are mutated in Usher syndrome patients, and mutations and translocations involving this gene have been associated with two types of Usher syndrome. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:26257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26257) · Entrez [79955](https://www.ncbi.nlm.nih.gov/gene/79955) · UniProt [Q9H5P4](https://www.uniprot.org/uniprotkb/Q9H5P4) · Ensembl [ENSG00000186862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186862)

## Data

Gene col 11863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11863); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11863]; `tensor/DDL_lfc|DDL_z.npy` [11863]; `embed/gene_vectors.npy` [11863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11863 or target_col == 11863). Every well: [[PDZD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
