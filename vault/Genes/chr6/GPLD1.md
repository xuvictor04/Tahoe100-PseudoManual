---
symbol: "GPLD1"
type: "gene"
col: 3348
ensembl_id: "ENSG00000112293"
name: "glycosylphosphatidylinositol specific phospholipase D1"
location: "6p22.3"
module: 10
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GPLD1

*glycosylphosphatidylinositol specific phospholipase D1* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +13.0, q 9e-36, up in 15 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.650× (z -4.6, q 0.003, down in 17 of 40 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.655× (z -4.2, q 0.007, down in 13 of 36 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAXC]] (+0.72, fdr 7e-06), [[DHRS4L2]] (+0.63, fdr 1e-05), [[PCDHA6]] (+0.62, fdr 7e-06); moves opposite to [[VRK3]] (-0.46, fdr 1e-04), [[FBH1]] (-0.45, fdr 5e-04), [[TRPT1]] (-0.44, fdr 6e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); 6 go from it, the strongest it → [[ADAM22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +13.0 | 9e-36 | 15/31 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +9.1 | 2e-17 | 2/3 (HOP62, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +8.7 | 7e-16 | 20/38 (HT-29, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.7 | 2e-12 | 3/6 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +6.7 | 2e-09 | 5/15 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.51×** | +6.2 | 4e-08 | 10/40 (A549, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.78×** | +6.1 | 7e-08 | 18/41 (A-427, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.3 | 8e-06 | 9/31 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +4.8 | 8e-05 | 3/31 (J82, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 1e-04 | 8/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 2e-04 | 6/27 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +4.5 | 4e-04 | 10/34 (NCI-H2030, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.008 | 7/35 (HT-29, SNU-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.009 | 3/38 (SW 900, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.013 | 8/38 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.094 | 1/42 (LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.650×** | -4.6 | 0.003 | 17/40 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -4.2 | 0.007 | 13/36 (SNU-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.690×** | -3.9 | 0.016 | 6/40 (C32, COLO 205, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.077 | 8/36 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.556× | -3.3 | 0.13 | 5/32 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.743× | -3.1 | 0.16 | 5/41 (NCI-H661, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.817× | -3.0 | 0.16 | 7/36 (HCT15, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | 0.752× | -3.0 | 0.16 | 10/28 (SNU-1, AN3 CA, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0485× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 3.09 | 0 | 2 | — | [[Penfluridol (drug)]] 0.05 µM 0.0634× (z -9.4) |
| [[LoVo (line)]] | wt | 3.34 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +13.2) | [[Menadione (drug)]] 0.5 µM 0.120× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.130× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -9.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[C32 (line)]] | wt | 2.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.4× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 1.62 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 51.1× (z +8.9) | — |
| [[J82 (line)]] | alt | 3.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 7.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 3.54 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.120× (z -8.5) |
| [[A-172 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.942 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAXC]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[DHRS4L2]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[PCDHA6]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LINC02026]] | +0.62 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CYP2U1]] | +0.60 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[FTCDNL1]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.57 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[STOX1]] | +0.56 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CC2D2A]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ALDH5A1]] | +0.55 | +0.47 / +0.64 | both halves | 2e-05 | STRING 549; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PALM]] | +0.52 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[JPH3]] | +0.52 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[CCDC102A]] | +0.52 | +0.61 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[FBH1]] | -0.45 | -0.41 / -0.24 | both halves | 5e-04 |  |
| [[TRPT1]] | -0.44 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[ZCCHC17]] | -0.44 | -0.51 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises GPLD1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without MIR1915HG | 0.030 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[EMID1]] | B | EMID1 activity raises GPLD1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without EMID1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises GPLD1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without SYT9-AS1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises GPLD1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without ABCA17P | 0.075 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[FAM184A]] | B | FAM184A activity raises GPLD1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without FAM184A | 0.084 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises GPLD1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without FAXC | 0.099 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ALDH5A1]] | C | ALDH5A1 activity raises GPLD1's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; co-absent with the target; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | GPLD1 activity raises ADAM22's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 2.57× lower at baseline in the lines without GPLD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[FAXC]] | B | GPLD1 activity raises FAXC's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 2.68× lower at baseline in the lines without GPLD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[PCDHA6]] | B | GPLD1 activity raises PCDHA6's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 3.20× lower at baseline in the lines without GPLD1 | 0.051 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[LINC00240]] | B | GPLD1 activity raises LINC00240's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without GPLD1 | 0.069 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[RNF157]] | B | GPLD1 activity raises RNF157's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without GPLD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[ALDH5A1]] | C | GPLD1 activity raises ALDH5A1's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 3.98× lower at baseline in the lines without GPLD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.0, 32.5); signed map (38.7, -10.8). **Vector** length 45.7, 5.93% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +6.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.4 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -0.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | glycosylphosphatidylinositol specific phospholipase D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,424,565-24,495,205 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P80108](https://www.uniprot.org/uniprotkb/P80108) (Phosphatidylinositol-glycan-specific phospholipase D):

> Hydrolyzes the inositol phosphate linkage of glycosylphosphatidylinositol (GPI)-anchored membrane proteins, thereby releasing them from the cell surface. Cleaves on the inositol side of the anchor, leaving the phosphate group attached to the membrane. This release of GPI-anchored proteins can modulate diverse biological processes, including the activation of signaling pathways.

**Summary**, from NCBI Gene [2822](https://www.ncbi.nlm.nih.gov/gene/2822):

> Many proteins are tethered to the extracellular face of eukaryotic plasma membranes by a glycosylphosphatidylinositol (GPI) anchor. The GPI-anchor is a glycolipid found on many blood cells. The protein encoded by this gene is a GPI degrading enzyme. Glycosylphosphatidylinositol specific phospholipase D1 hydrolyzes the inositol phosphate linkage in proteins anchored by phosphatidylinositol glycans, thereby releasing the attached protein from the plasma membrane. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4459) · Entrez [2822](https://www.ncbi.nlm.nih.gov/gene/2822) · UniProt [P80108](https://www.uniprot.org/uniprotkb/P80108) · Ensembl [ENSG00000112293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112293)

## Data

Gene col 3348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3348); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3348]; `tensor/DDL_lfc|DDL_z.npy` [3348]; `embed/gene_vectors.npy` [3348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3348 or target_col == 3348). Every well: [[GPLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
