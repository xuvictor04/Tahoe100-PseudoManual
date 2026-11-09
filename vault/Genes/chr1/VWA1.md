---
symbol: "VWA1"
type: "gene"
col: 11030
ensembl_id: "ENSG00000179403"
name: "von Willebrand factor A domain containing 1"
location: "1p36.33"
module: 83
arm: "-"
pooled_cpm: 10.84
n_lines_expressing: 40
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 14
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# VWA1

*von Willebrand factor A domain containing 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +5.9, q 2e-06, up in 9 of 14 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.269× (z -13.6, q 1e-39, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFD]] (+0.65, fdr 2e-05), [[ROGDI]] (+0.61, fdr 7e-05), [[ZDHHC12]] (+0.60, fdr 6e-05); moves opposite to [[ZNF621]] (-0.61, fdr 2e-04), [[TIRAP]] (-0.56, fdr 2e-04), [[DNAJA4]] (-0.55, fdr 1e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CRACR2B]] → it (grade B ⚠); 14 go from it, the strongest it → [[CLDN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +5.9 | 2e-06 | 9/14 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +4.5 | 0.002 | 13/25 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 1.63× | +3.5 | 0.10 | 16/36 (HepG2/C3A, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.57× | +3.3 | 0.13 | 15/37 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Binimetinib (drug)]] 5 µM |  | 1.57× | +3.2 | 0.13 | 12/37 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.55× | +3.2 | 0.13 | 14/37 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.269×** | -13.6 | 1e-39 | 33/34 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.213×** | -11.3 | 2e-27 | 35/35 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -6.8 | 1e-09 | 24/34 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.410×** | -6.6 | 8e-09 | 27/37 (SNU-423, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.442×** | -6.0 | 2e-07 | 29/36 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.408×** | -6.0 | 2e-07 | 26/36 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.447×** | -5.7 | 1e-06 | 26/36 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.455×** | -5.6 | 2e-06 | 25/36 (PANC-1, SHP-77, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.275×** | -5.0 | 5e-05 | 25/36 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.517×** | -4.8 | 7e-05 | 19/37 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -4.6 | 2e-04 | 22/36 (HT-29, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -4.3 | 9e-04 | 20/37 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.562×** | -4.2 | 1e-03 | 17/37 (C-33 A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.591×** | -3.9 | 0.005 | 19/37 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.614×** | -3.6 | 0.013 | 17/37 (NCI-H1573, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0710× (z -17.1) |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -14.4) |
| [[HOP62 (line)]] | alt | 5.84 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -12.7) |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -14.1) |
| [[C32 (line)]] | wt | 11.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0422× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.135× (z -9.3) |
| [[HS-578T (line)]] | alt | 4.04 | 0 | 2 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0497× (z -9.5) |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.3) |
| [[KATO III (line)]] | alt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 5.43 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0710× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 2.77 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0355× (z -11.0) |
| [[SNU-423 (line)]] | alt | 7.09 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0825× (z -11.7) |
| [[BT-474 (line)]] | alt | 6.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -12.1) |
| [[LoVo (line)]] | wt | 2.76 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0506× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 4.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 9.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 9.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0727× (z -11.1) |
| [[SW 900 (line)]] | alt | 6.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -9.8) |
| [[SW1417 (line)]] | alt | 5.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.8) |
| [[SW480 (line)]] | alt | 7.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.9) |
| [[A-172 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | +0.65 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ROGDI]] | +0.61 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[ZDHHC12]] | +0.60 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[GCHFR]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SLC35B2]] | +0.59 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | +0.59 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[RHPN2]] | +0.59 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[EFNA4]] | +0.57 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[LRG1]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CTXN1]] | +0.56 | +0.47 / +0.27 | both halves | 3e-04 |  |
| [[KCTD17]] | +0.55 | +0.41 / +0.31 | both halves | 2e-04 |  |
| [[ATAD3C]] | +0.55 | +0.48 / +0.41 | both halves | 4e-05 | ⚠ same locus (6.8 kb, same strand: neighbours can correlate without regulation) |
| [[TMEM276]] | +0.55 | +0.45 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF621]] | -0.61 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[TIRAP]] | -0.56 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[DNAJA4]] | -0.55 | -0.50 / -0.32 | both halves | 1e-04 |  |
| [[SMIM15-AS1]] | -0.54 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[N4BP2]] | -0.53 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[ANGEL2]] | -0.53 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ATE1OSP]] | -0.53 | -0.41 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[ZCWPW1]] | -0.52 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[GTF3C2-AS2]] | -0.52 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[ZNF425]] | -0.52 | -0.46 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[ZFHX2-AS1]] | -0.51 | -0.36 / -0.24 | both halves | 5e-04 |  |
| [[MSH4]] | -0.51 | -0.45 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[GLIPR1-AS1]] | -0.50 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[LINC01909]] | -0.50 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[KLRA1P]] | -0.50 | -0.36 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACR2B]] | B | CRACR2B activity raises VWA1's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without CRACR2B | 0.018 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[GCHFR]] | B | GCHFR activity raises VWA1's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without GCHFR | 0.023 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises VWA1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without TJP3 | 0.095 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[ATAD3C]] | C | ATAD3C activity raises VWA1's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.73× lower at baseline in the lines without ATAD3C | 7e-04 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN3]] | B | VWA1 activity raises CLDN3's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 3.89× lower at baseline in the lines without VWA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[SPAG5-AS1]] | B | VWA1 activity lowers SPAG5-AS1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.14× higher at baseline in the lines without VWA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[GALM]] | B | VWA1 activity raises GALM's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without VWA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[LMTK3]] | B | VWA1 activity raises LMTK3's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without VWA1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[CTNND1]] | B | VWA1 activity raises CTNND1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without VWA1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[GCHFR]] | B | VWA1 activity raises GCHFR's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without VWA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[ASB1]] | B | VWA1 activity lowers ASB1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without VWA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[ENDOD1]] | B | VWA1 activity raises ENDOD1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without VWA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[LINC00511]] | B | VWA1 activity raises LINC00511's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without VWA1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[PLAC8L1]] | B | VWA1 activity lowers PLAC8L1's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 1.31× higher at baseline in the lines without VWA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | B | VWA1 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express VWA1 (10) vs lines expressing it (38) | the lines without VWA1: 0.56× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[RHPN2]] | B | VWA1 activity raises RHPN2's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without VWA1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.5, -5.1); signed map (-37.7, 14.1). **Vector** length 71.7, 16.4% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -13.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -6.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | von Willebrand factor A domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,434,861-1,442,882 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22215, VWA-1, WARP |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCB0](https://www.uniprot.org/uniprotkb/Q6PCB0) (von Willebrand factor A domain-containing protein 1):

> Promotes matrix assembly (By similarity). Involved in the organization of skeletal muscles and in the formation of neuromuscular junctions (Probable).

**Summary**, from NCBI Gene [64856](https://www.ncbi.nlm.nih.gov/gene/64856):

> VWA1 belongs to the von Willebrand factor (VWF; MIM 613160) A (VWFA) domain superfamily of extracellular matrix proteins and appears to play a role in cartilage structure and function (Fitzgerald et al., 2002 [PubMed 12062410]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:30910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30910) · Entrez [64856](https://www.ncbi.nlm.nih.gov/gene/64856) · UniProt [Q6PCB0](https://www.uniprot.org/uniprotkb/Q6PCB0) · Ensembl [ENSG00000179403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179403)

## Data

Gene col 11030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11030); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11030]; `tensor/DDL_lfc|DDL_z.npy` [11030]; `embed/gene_vectors.npy` [11030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11030 or target_col == 11030). Every well: [[VWA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VWA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
