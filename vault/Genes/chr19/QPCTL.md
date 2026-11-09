---
symbol: "QPCTL"
type: "gene"
col: 244
ensembl_id: "ENSG00000011478"
name: "glutaminyl-peptide cyclotransferase like"
location: "19q13.32"
module: 40
arm: "+"
pooled_cpm: 27.96
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# QPCTL

*glutaminyl-peptide cyclotransferase like* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +7.8, q 4e-12, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.380× (z -9.8, q 6e-20, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED26]] (+0.78, fdr 7e-06), [[DPM1]] (+0.78, fdr 7e-06), [[SLC35E1]] (+0.77, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.69, fdr 1e-05), [[VEZF1]] (-0.69, fdr 7e-06), [[NHLRC2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.8 | 4e-12 | 40/47 (NCI-H2030, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +7.3 | 7e-11 | 38/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +5.2 | 4e-05 | 26/48 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +3.4 | 0.072 | 22/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +3.4 | 0.072 | 19/48 (KATO III, LoVo, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +3.4 | 0.072 | 22/46 (HOP62, NCI-H23, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.086 | 17/45 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.099 | 17/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.10 | 14/48 (HOP62, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.380×** | -9.8 | 6e-20 | 41/48 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.404×** | -7.6 | 7e-12 | 33/42 (SW1417, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -7.4 | 2e-11 | 33/47 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -7.1 | 2e-10 | 25/32 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -5.9 | 3e-07 | 30/47 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.581×** | -5.5 | 4e-06 | 32/48 (NCI-H1573, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.705×** | -5.2 | 2e-05 | 32/48 (RPMI-7951, NCI-H2347, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.651×** | -4.5 | 5e-04 | 27/48 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.630×** | -4.5 | 5e-04 | 21/37 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -4.4 | 7e-04 | 24/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.714×** | -3.5 | 0.021 | 23/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -3.2 | 0.065 | 17/48 (A498, SNU-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.724×** | -3.1 | 0.077 | 18/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.738×** | -3.0 | 0.093 | 19/47 (SW 1271, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 58.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -11.8) |
| [[A549 (line)]] | wt | 23.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -8.9) |
| [[C32 (line)]] | wt | 56.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.272× (z -8.5) |
| [[HS-578T (line)]] | alt | 42.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -9.8) |
| [[LoVo (line)]] | wt | 21.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.79× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.185× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 34.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -9.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 52.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -10.7) |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -15.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0744× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.138× (z -8.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.5) | — |
| [[J82 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.252× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -8.7) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | +0.78 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[DPM1]] | +0.78 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[TBC1D20]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MPG]] | +0.73 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SS18L1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.69 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.69 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[NHLRC2]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[FAT1]] | -0.68 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.68 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.67 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[LIG4]] | -0.67 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[GMFB]] | -0.67 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[ZNF518B]] | -0.66 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[CFL2]] | -0.65 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.64 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CHTOP]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARAP2]] | B | ARAP2 activity lowers QPCTL's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.49× higher at baseline in the lines without ARAP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[TOP2A]] | B | TOP2A activity lowers QPCTL's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[AP1S3]] | C | AP1S3 activity lowers QPCTL's level | lines that do not express AP1S3 (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without AP1S3 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02842, ENSG00000236283, LRIF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.8, -19.9); signed map (-43.8, 12.3). **Vector** length 132, 38.4% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.2 | +3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.5 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.1 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | glutaminyl-peptide cyclotransferase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,692,403-45,703,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20084 |
| Gene groups (HGNC) | M28 metallopeptidases; Glutaminyl-peptide cyclotransferase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXS2](https://www.uniprot.org/uniprotkb/Q9NXS2) (Glutaminyl-peptide cyclotransferase-like protein):

> Responsible for the biosynthesis of pyroglutamyl peptides.

**Summary**, from NCBI Gene [54814](https://www.ncbi.nlm.nih.gov/gene/54814):

> Enables glutaminyl-peptide cyclotransferase activity and zinc ion binding activity. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25952) · Entrez [54814](https://www.ncbi.nlm.nih.gov/gene/54814) · UniProt [Q9NXS2](https://www.uniprot.org/uniprotkb/Q9NXS2) · Ensembl [ENSG00000011478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011478)

## Data

Gene col 244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 244); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 244]; `tensor/DDL_lfc|DDL_z.npy` [244]; `embed/gene_vectors.npy` [244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 244 or target_col == 244). Every well: [[QPCTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QPCTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
