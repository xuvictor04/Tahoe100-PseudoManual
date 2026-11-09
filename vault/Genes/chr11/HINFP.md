---
symbol: "HINFP"
type: "gene"
col: 10234
ensembl_id: "ENSG00000172273"
name: "histone H4 transcription factor"
location: "11q23.3"
module: 76
arm: "+"
pooled_cpm: 12.99
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# HINFP

*histone H4 transcription factor* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.57× (z +16.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.531× (z -10.9, q 4e-25, down in 40 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.554× (z -5.3, q 1e-05, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMBR1L]] (+0.74, fdr 7e-06), [[ECT2L]] (+0.73, fdr 7e-06), [[NUDT2]] (+0.71, fdr 7e-06); moves opposite to [[CEP41]] (-0.64, fdr 7e-06), [[DCLRE1A]] (-0.62, fdr 1e-05), [[NAA15]] (-0.62, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +16.2 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +13.5 | 4e-39 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +12.8 | 3e-35 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +12.4 | 2e-33 | 38/45 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +12.3 | 1e-32 | 43/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +11.9 | 1e-30 | 30/45 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +8.7 | 2e-16 | 32/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.4 | 7e-12 | 23/40 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.6 | 2e-09 | 22/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 2e-06 | 20/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 23/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.0 | 2e-05 | 17/43 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.0 | 3e-05 | 15/47 (LOX-IMVI, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +4.8 | 6e-05 | 17/48 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.22×** | +4.4 | 4e-04 | 15/48 (SW1417, SHP-77, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.001 | 16/45 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.002 | 11/47 (NCI-H23, J82, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.006 | 13/48 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.015 | 7/47 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.531×** | -10.9 | 4e-25 | 40/47 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.578×** | -9.5 | 8e-19 | 25/36 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -8.3 | 1e-14 | 15/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -6.7 | 3e-09 | 19/32 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.554×** | -5.3 | 1e-05 | 17/46 (Hs 766T, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.575×** | -5.0 | 5e-05 | 17/45 (HCT15, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.629×** | -4.2 | 0.002 | 18/45 (SK-MEL-2, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.629×** | -4.2 | 0.002 | 18/42 (C-33 A, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.641×** | -4.0 | 0.004 | 11/46 (SW1417, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.801×** | -3.8 | 0.007 | 11/48 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.751×** | -3.5 | 0.022 | 3/47 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.045 | 11/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.828×** | -3.1 | 0.079 | 10/47 (AN3 CA, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.831×** | -3.1 | 0.079 | 14/46 (NCI-H1573, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.079 | 6/48 (AsPC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.840× | -3.0 | 0.087 | 8/48 (NCI-H1573, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 16.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 23.8 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.80× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 8.20 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -11.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0912× (z -11.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0675× (z -11.2) |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 1 | — | [[ULK-101 (drug)]] 0.5 µM 0.0696× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -15.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 9.77 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0607× (z -11.0) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -8.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0876× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 9.65 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0719× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1L]] | +0.74 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[NUDT2]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ATXN3]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[TSC22D4]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[NARF]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ZNHIT1]] | +0.69 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[APTR]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MAX]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP41]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.62 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[NAA15]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.61 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RBBP8]] | -0.60 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[TRIM44]] | -0.59 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[TMEM185B]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[CEP83]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[FKTN]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NBN]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.0, -42.4); signed map (-16.9, 11.5). **Vector** length 80.5, 15.1% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.2 | +12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.2 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -10.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | histone H4 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,121,580-119,136,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434F162, HiNF-P, ZNF743; previously MIZF |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQA5](https://www.uniprot.org/uniprotkb/Q9BQA5) (Histone H4 transcription factor):

> Transcriptional repressor that binds to the consensus sequence 5'-CGGACGTT-3' and to the RB1 promoter. Transcriptional activator that promotes histone H4 gene transcription at the G1/S phase transition in conjunction with NPAT. Also activates transcription of the ATM and PRKDC genes. Autoregulates its expression by associating with its own promoter.

**Summary**, from NCBI Gene [25988](https://www.ncbi.nlm.nih.gov/gene/25988):

> This gene encodes a transcription factor that interacts with methyl-CpG-binding protein-2 (MBD2), a component of the MeCP1 histone deacetylase (HDAC) complex, and plays a role in DNA methylation and transcription repression. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17850) · Entrez [25988](https://www.ncbi.nlm.nih.gov/gene/25988) · UniProt [Q9BQA5](https://www.uniprot.org/uniprotkb/Q9BQA5) · Ensembl [ENSG00000172273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172273)

## Data

Gene col 10234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10234); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10234]; `tensor/DDL_lfc|DDL_z.npy` [10234]; `embed/gene_vectors.npy` [10234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10234 or target_col == 10234). Every well: [[HINFP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HINFP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
