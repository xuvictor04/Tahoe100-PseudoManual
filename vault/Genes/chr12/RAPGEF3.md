---
symbol: "RAPGEF3"
type: "gene"
col: 1253
ensembl_id: "ENSG00000079337"
name: "Rap guanine nucleotide exchange factor 3"
location: "12q13.11"
module: 34
arm: "+"
pooled_cpm: 6.06
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 47
n_dd_up_clean: 3
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# RAPGEF3

*Rap guanine nucleotide exchange factor 3* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.59× (z +4.4, q 0.005, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM: 1.31× (z +3.8, q 0.022, up in 5 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.412× (z -8.5, q 1e-14, down in 21 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYEOV]] (+0.71, fdr 7e-06), [[ARHGEF1]] (+0.69, fdr 7e-06), [[C13orf46]] (+0.68, fdr 7e-06); moves opposite to [[ATG10]] (-0.56, fdr 1e-05), [[TET2]] (-0.54, fdr 3e-05), [[PAIP1]] (-0.53, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[FAM83A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.4 | 0.005 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.9 | 0.022 | 1/15 (LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.022 | 5/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.022 | 6/28 (NCI-H460, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.3 | 0.087 | 1/18 (LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.97×** | +3.3 | 0.087 | 4/22 (CFPAC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Naproxen (drug)]] 0.05 µM |  | 1.42× | +3.2 | 0.11 | 8/27 (A498, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.412×** | -8.5 | 1e-14 | 21/34 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.499×** | -6.9 | 1e-09 | 22/40 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.538×** | -6.7 | 3e-09 | 19/40 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.584×** | -6.6 | 5e-09 | 23/40 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.520×** | -6.5 | 1e-08 | 21/40 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -5.9 | 4e-07 | 22/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.552×** | -5.7 | 1e-06 | 18/35 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -5.5 | 3e-06 | 19/40 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.580×** | -5.4 | 4e-06 | 17/40 (HEC-1-A, AsPC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -5.4 | 5e-06 | 21/36 (A498, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.685×** | -5.2 | 8e-06 | 13/40 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -5.2 | 8e-06 | 15/25 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.591×** | -5.2 | 8e-06 | 16/40 (AsPC-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.584×** | -5.1 | 1e-05 | 18/38 (AsPC-1, KATO III, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.617×** | -4.8 | 6e-05 | 17/38 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.607×** | -4.6 | 2e-04 | 17/40 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.722×** | -4.6 | 2e-04 | 13/40 (Panc 03.27, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.727×** | -4.4 | 4e-04 | 11/40 (AsPC-1, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 29.2 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0789× (z -14.4) |
| [[SW480 (line)]] | alt | 10.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -9.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.218× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[KATO III (line)]] | alt | 3.65 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0478× (z -8.8) |
| [[LoVo (line)]] | wt | 6.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0851× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0450× (z -13.6) |
| [[PANC-1 (line)]] | alt | 3.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYEOV]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ARHGEF1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[C13orf46]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[KPNA2P3]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 | same gene group; STRING 431 |
| [[LINC00659]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NTSR1]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PTK6]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[TOR4A]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG10]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TET2]] | -0.54 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83A]] | B | FAM83A activity raises RAPGEF3's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without FAM83A | 0.005 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[MDFI]] | B | MDFI activity raises RAPGEF3's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without MDFI | 0.008 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[KIAA0040]] | B | KIAA0040 activity raises RAPGEF3's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.84× lower at baseline in the lines without KIAA0040 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[TNS4]] | B | TNS4 activity raises RAPGEF3's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without TNS4 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises RAPGEF3's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.80× lower at baseline in the lines without TNFRSF6B | 0.017 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |
| [[LAMA3]] | B | LAMA3 activity raises RAPGEF3's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without LAMA3 | 0.021 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[FAM110C]] | B | FAM110C activity raises RAPGEF3's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without FAM110C | 0.028 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[GJB3]] | B | GJB3 activity raises RAPGEF3's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without GJB3 | 0.028 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[SCEL]] | B | SCEL activity raises RAPGEF3's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.94× lower at baseline in the lines without SCEL | 0.035 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[CEACAM1]] | B | CEACAM1 activity raises RAPGEF3's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without CEACAM1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[MAP2K1]] | B | MAP2K1 activity raises RAPGEF3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.0% of all compounds | 0.048 | ⚠ off-target possible; 4 compounds |
| [[TNFRSF6B]] | B | TNFRSF6B activity strengthens RAPGEF3's drug response | lines that do not express TNFRSF6B (27) vs lines expressing it (13) | the lines without TNFRSF6B respond 0.59× as strongly (z diff +1.11); strongest at Panobinostat 5 µM: 0.64x vs 0.40x (z diff +2.0) | 0.063 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.2, 53.3); signed map (4.7, 40.4). **Vector** length 79.2, 15.4% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +1.9 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Naproxen (drug)]] 0.05 µM |  | +1.4 | +3.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.2 | -6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,734,363-47,771,040 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cAMP-GEFI, EPAC, bcm910 |
| Gene groups (HGNC) | DEP domain containing |
| Hallmark sets | COAGULATION |
| Reactome | 9 pathways, smallest: Rap1 signalling; Integrin signaling; Platelet Aggregation (Plug Formation) |
| Matched by | ensembl_id |

**Function**, from UniProt [O95398](https://www.uniprot.org/uniprotkb/O95398) (Rap guanine nucleotide exchange factor 3):

> Guanine nucleotide exchange factor (GEF) for RAP1A and RAP2A small GTPases that is activated by binding cAMP. Through simultaneous binding of PDE3B to RAPGEF3 and PIK3R6 is assembled in a signaling complex in which it activates the PI3K gamma complex and which is involved in angiogenesis. Plays a role in the modulation of the cAMP-induced dynamic control of endothelial barrier function through a pathway that is independent on Rho-mediated signaling. Required for the actin rearrangement at …

**Summary**, from NCBI Gene [10411](https://www.ncbi.nlm.nih.gov/gene/10411):

> Enables guanyl-nucleotide exchange factor activity and protein domain specific binding activity. Involved in several processes, including Rap protein signal transduction; cellular response to cAMP; and regulation of syncytium formation by plasma membrane fusion. Located in several cellular components, including filopodium; lamellipodium; and microvillus. Implicated in nicotine dependence. Biomarker of congestive heart failure. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16629) · Entrez [10411](https://www.ncbi.nlm.nih.gov/gene/10411) · UniProt [O95398](https://www.uniprot.org/uniprotkb/O95398) · Ensembl [ENSG00000079337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079337)

## Data

Gene col 1253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1253); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1253]; `tensor/DDL_lfc|DDL_z.npy` [1253]; `embed/gene_vectors.npy` [1253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1253 or target_col == 1253). Every well: [[RAPGEF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
