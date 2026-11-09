---
symbol: "KCTD14"
type: "gene"
col: 7512
ensembl_id: "ENSG00000151364"
name: "potassium channel tetramerization domain containing 14"
location: "11q14.1"
module: 55
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# KCTD14

*potassium channel tetramerization domain containing 14* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.12× (z +11.7, q 1e-28, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.88× (z +9.9, q 9e-21, up in 12 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.586× (z -5.9, q 2e-06, down in 12 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SULT1C2]] (+0.65, fdr 7e-06), [[LPAR5]] (+0.62, fdr 4e-05), [[TPRXL]] (+0.62, fdr 4e-05); moves opposite to [[SRGAP2C]] (-0.55, fdr 2e-04), [[SRGAP2B]] (-0.54, fdr 4e-05), [[SRGAP2]] (-0.53, fdr 7e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC03040]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +11.7 | 1e-28 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.88×** | +9.9 | 9e-21 | 12/37 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +8.8 | 2e-16 | 2/10 (CFPAC-1, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.3 | 1e-14 | 1/3 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.0 | 3e-07 | 3/12 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 3e-04 | 4/30 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +4.1 | 0.004 | 0/3 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.8 | 0.010 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.017 | 6/28 (HS-578T, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.032 | 2/19 (SHP-77, SW1417) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.2 | 0.070 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.073 | 2/28 (CFPAC-1, HEC-1-A) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.11 | 1/16 (HOP62) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -5.9 | 2e-06 | 12/32 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.699×** | -3.9 | 0.014 | 6/28 (HepG2/C3A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -3.9 | 0.014 | 10/19 (SHP-77, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -3.8 | 0.014 | 11/39 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.705×** | -3.8 | 0.014 | 13/28 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.093 | 1/37 (HOP62) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.749× | -3.2 | 0.11 | 7/39 (COLO 205, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Cepharanthine (drug)]] 0.05 µM |  | 0.750× | -3.2 | 0.11 | 2/37 (LOX-IMVI, HEC-1-A) | inconsistent across doses | position effect removed |
| [[Olanzapine (drug)]] 0.05 µM |  | 0.753× | -3.1 | 0.11 | 3/37 (NCI-H2030, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 11.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0948× (z -11.8) |
| [[SHP-77 (line)]] | alt | 7.95 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0787× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[palbociclib (drug)]] 0.05 µM 0.0755× (z -10.2) |
| [[LS 180 (line)]] | wt | 6.80 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.09 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.791 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.765 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.856 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.697 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SULT1C2]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LPAR5]] | +0.62 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TPRXL]] | +0.62 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[ANKEF1]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.59 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[EPHX4]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[C9orf152]] | +0.58 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[ABO]] | +0.58 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[FUT2]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[LINC02058]] | +0.57 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[FAM221A]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[FGD3]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2C]] | -0.55 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[SRGAP2B]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SRGAP2]] | -0.53 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[SFI1]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[LRP11]] | -0.49 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[YPEL1]] | -0.49 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[MYADM]] | -0.49 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[STX2]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[DNAAF9]] | -0.48 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[TMEM50A]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MYO9A]] | -0.47 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[PACS2]] | -0.46 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03040]] | B | LINC03040 activity raises KCTD14's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without LINC03040 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[TPRXL]] | B | TPRXL activity raises KCTD14's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without TPRXL | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises KCTD14's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without ZNF503-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises KCTD14's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.54× lower at baseline in the lines without RASSF6 | 0.060 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[LINC02253]] | B | LINC02253 activity raises KCTD14's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.61× lower at baseline in the lines without LINC02253 | 0.063 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349 |
| [[LINC01559]] | B | LINC01559 activity raises KCTD14's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 1.88× lower at baseline in the lines without LINC01559 | 0.084 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[ANKEF1]] | B | ANKEF1 activity raises KCTD14's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without ANKEF1 | 0.098 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[TMPRSS3]] | B | TMPRSS3 activity raises KCTD14's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without TMPRSS3 | 0.0995 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[MIR4713HG]] | B | MIR4713HG activity raises KCTD14's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without MIR4713HG | 0.0996 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.5, 45.7); signed map (59.6, 12.3). **Vector** length 37.6, 4.41% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | -0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -3.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,015,715-78,046,191 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2376 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

UniProt [Q9BQ13](https://www.uniprot.org/uniprotkb/Q9BQ13) carries no function annotation.

**Summary**, from NCBI Gene [65987](https://www.ncbi.nlm.nih.gov/gene/65987):

> Predicted to be involved in protein homooligomerization. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23295) · Entrez [65987](https://www.ncbi.nlm.nih.gov/gene/65987) · UniProt [Q9BQ13](https://www.uniprot.org/uniprotkb/Q9BQ13) · Ensembl [ENSG00000151364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151364)

## Data

Gene col 7512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7512); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7512]; `tensor/DDL_lfc|DDL_z.npy` [7512]; `embed/gene_vectors.npy` [7512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7512 or target_col == 7512). Every well: [[KCTD14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
