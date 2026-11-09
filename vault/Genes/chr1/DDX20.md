---
symbol: "DDX20"
type: "gene"
col: 758
ensembl_id: "ENSG00000064703"
name: "DEAD-box helicase 20"
location: "1p13.2"
module: 16
arm: "+"
pooled_cpm: 11.32
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DDX20

*DEAD-box helicase 20* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.90× (z +23.4, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.564× (z -8.6, q 4e-15, down in 15 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.657× (z -4.7, q 5e-04, down in 17 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LS 180 0.142×, SW480 0.313×, A549 0.134×, HEC-1-A 0.253×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.175×, NCI-H2030 0.147×, A498 0.226×, J82 0.247×; ⚠ toxic; transcription drop); [[LJI308 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf25]] (+0.79, fdr 7e-06), [[TRMT5]] (+0.76, fdr 7e-06), [[ADO]] (+0.76, fdr 7e-06); moves opposite to [[CBFA2T2]] (-0.67, fdr 7e-06), [[TMEM50B]] (-0.64, fdr 7e-06), [[PIK3C2A]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.90×** | +23.4 | 0e+00 | 44/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **11.4×** | +19.8 | 0e+00 | 46/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **3.68×** | +19.5 | 0e+00 | 45/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.04×** | +17.3 | 0e+00 | 43/45 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.88×** | +16.5 | 0e+00 | 45/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.88×** | +12.9 | 4e-36 | 38/45 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.91×** | +10.0 | 1e-21 | 31/47 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.3 | 1e-18 | 31/46 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.79×** | +9.0 | 1e-17 | 31/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.68×** | +8.0 | 5e-14 | 26/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +7.7 | 8e-13 | 28/47 (A498, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +7.5 | 3e-12 | 25/41 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.60×** | +7.3 | 1e-11 | 24/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +7.0 | 9e-11 | 25/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +7.0 | 1e-10 | 30/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.0 | 1e-05 | 12/45 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.7 | 5e-05 | 13/48 (CFPAC-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.7 | 6e-05 | 12/44 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.3 | 5e-04 | 19/47 (J82, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 7e-04 | 19/47 (HEC-1-A, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 758.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LS 180 0.142×, SW480 0.313×, A549 0.134×, HEC-1-A 0.253×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (HEC-1-A 0.175×, NCI-H2030 0.147×, A498 0.226×, J82 0.247×; ⚠ toxic; transcription drop); [[LJI308 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -8.6 | 4e-15 | 15/19 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.641×** | -7.0 | 9e-10 | 25/39 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.657×** | -4.7 | 5e-04 | 17/42 (KATO III, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.764× | -3.0 | 0.32 | 10/46 (C32, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.7 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.2 | 6 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.8× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 10.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 8.19 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +15.9) | — |
| [[A549 (line)]] | wt | 8.72 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 8.63 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.4 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 4.36× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 38.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.3) | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0772× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 8.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +8.8) | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 9.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.87× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 9.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 8.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.8) | — |
| [[RKO (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.2) | — |
| [[A-172 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf25]] | +0.79 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.76 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ADO]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[NOL11]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 | STRING 429 |
| [[DCLRE1A]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.72 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[UTP15]] | +0.72 | +0.77 / +0.65 | both halves | 7e-06 | STRING 419 |
| [[ZNF507]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.67 | -0.73 / -0.62 | both halves | 7e-06 |  |
| [[TMEM50B]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[F11R]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[PDXK]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[TMEM41B]] | -0.62 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[QSOX1]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.62 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TTC3]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PHF1]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.61 | -0.68 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRIP1]] | B | NRIP1 activity lowers DDX20's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.58× higher at baseline in the lines without NRIP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[DLX1]] | B | DLX1 activity raises DDX20's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.32× lower at baseline in the lines without DLX1 | 0.099 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.4, 12.9); signed map (2.9, -36.9). **Vector** length 75.3, 14.7% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +16.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +19.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +19.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +12.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -2.4 | +5.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.2 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -1.9 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -4.7 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,754,832-111,775,602 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DP103, GEMIN3 |
| Gene groups (HGNC) | DEAD-box helicases; Gemins |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHI6](https://www.uniprot.org/uniprotkb/Q9UHI6) (Probable ATP-dependent RNA helicase DDX20):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [11218](https://www.ncbi.nlm.nih.gov/gene/11218):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2743) · Entrez [11218](https://www.ncbi.nlm.nih.gov/gene/11218) · UniProt [Q9UHI6](https://www.uniprot.org/uniprotkb/Q9UHI6) · Ensembl [ENSG00000064703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064703)

## Data

Gene col 758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 758); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 758]; `tensor/DDL_lfc|DDL_z.npy` [758]; `embed/gene_vectors.npy` [758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 758 or target_col == 758). Every well: [[DDX20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
