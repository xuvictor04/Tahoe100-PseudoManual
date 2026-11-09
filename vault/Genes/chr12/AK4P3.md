---
symbol: "AK4P3"
type: "gene"
col: 13900
ensembl_id: "ENSG00000233381"
name: "adenylate kinase 4 pseudogene 3"
location: "12p11.21"
module: 9
arm: "+"
pooled_cpm: 6.75
n_lines_expressing: 14
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 24
direction_downstream: 40
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# AK4P3

*adenylate kinase 4 pseudogene 3* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.22× (z +15.6, q 0e+00, up in 1 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.635× (z -4.3, q 0.009, down in 8 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0955×, Hs 766T 0.172×, RPMI-7951 0.162×, KATO III 0.276×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0617×, KATO III 0.130×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 0.105×, SHP-77 0.217×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.274×, RPMI-7951 0.199×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AN3 CA 0.0745×, SK-MEL-2 0.339×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGA]] (+0.62, fdr 1e-05), [[LRFN2]] (+0.58, fdr 4e-05), [[RIT2]] (+0.57, fdr 5e-05); moves opposite to [[ELFN2]] (-0.35, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[UNC80]] → it (grade B ⚠); 40 go from it, the strongest it → [[UNC80]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.22×** | +15.6 | 0e+00 | 1/11 (KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.8 | 4e-20 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +9.7 | 4e-20 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.80×** | +9.7 | 4e-20 | 3/12 (SHP-77, NCI-H661, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +6.8 | 1e-09 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +5.7 | 1e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.2 | 2e-05 | 4/12 (AN3 CA, SHP-77, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.3 | 0.001 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.3 | 0.001 | 1/3 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.0 | 0.004 | 1/10 (HepG2/C3A) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.005 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.49×** | +3.8 | 0.007 | 1/8 (Hs 766T) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.7 | 0.009 | 2/8 (SK-MEL-2, C-33 A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.4 | 0.028 | 0/11 | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.1 | 0.070 | 0/9 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13900.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0955×, Hs 766T 0.172×, RPMI-7951 0.162×, KATO III 0.276×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0617×, KATO III 0.130×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 0.105×, SHP-77 0.217×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.274×, RPMI-7951 0.199×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AN3 CA 0.0745×, SK-MEL-2 0.339×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -4.3 | 0.009 | 8/12 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.697× | -3.4 | 0.17 | 5/12 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.685× | -3.3 | 0.17 | 1/12 (SK-MEL-2) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.707× | -3.0 | 0.33 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 90.8 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -27.9) |
| [[KATO III (line)]] | alt | 69.3 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0257× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.162× (z -14.3) |
| [[AN3 CA (line)]] | alt | 28.8 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0745× (z -8.9) |
| [[Hs 766T (line)]] | wt | 43.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -15.0) |
| [[SHP-77 (line)]] | alt | 61.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.3) |
| [[A-172 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.778 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGA]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LRFN2]] | +0.58 | +0.52 / +0.43 | both halves | 4e-05 |  |
| [[RIT2]] | +0.57 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NELL1]] | +0.57 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[SYT4]] | +0.57 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[LINC01287]] | +0.56 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CALCA]] | +0.56 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[ASCL1]] | +0.55 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[SRRM4]] | +0.55 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[KCTD8]] | +0.55 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[GRIK1]] | +0.54 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[KHDRBS2]] | +0.52 | +0.37 / +0.40 | both halves | 8e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELFN2]] | -0.35 | -0.40 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 1, C 23. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC80]] | B | UNC80 activity raises AK4P3's level | lines that do not express UNC80 (16) vs lines expressing it (34) | 2.92× lower at baseline in the lines without UNC80 | 0.090 | ⚠ within organs, on part of the lines; also absent: PPFIA2, GAS7, COP1-DT; maybe low, not absent |
| [[ASCL1]] | C | ASCL1 activity raises AK4P3's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 6.57× lower at baseline in the lines without ASCL1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises AK4P3's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 5.30× lower at baseline in the lines without SRRM4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises AK4P3's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 6.39× lower at baseline in the lines without GTSF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises AK4P3's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 6.07× lower at baseline in the lines without SYT4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises AK4P3's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.32× lower at baseline in the lines without PCSK1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises AK4P3's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without RUNX1T1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises AK4P3's level | lines that do not express CALCA (45) vs lines expressing it (5) | 6.80× lower at baseline in the lines without CALCA | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[ZNF727]] | C | ZNF727 activity raises AK4P3's level | lines that do not express ZNF727 (35) vs lines expressing it (15) | 3.27× lower at baseline in the lines without ZNF727 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF732, CCK, LINC02899; co-absent with the target |
| [[CGA]] | C | CGA activity raises AK4P3's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.58× lower at baseline in the lines without CGA | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises AK4P3's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.59× lower at baseline in the lines without LINC01446 | 0.040 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[KHDRBS2]] | C | KHDRBS2 activity raises AK4P3's level | lines that do not express KHDRBS2 (37) vs lines expressing it (13) | 3.25× lower at baseline in the lines without KHDRBS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 9, C 31. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC80]] | B | AK4P3 activity raises UNC80's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.21× lower at baseline in the lines without AK4P3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[RALYL]] | B | AK4P3 activity raises RALYL's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.71× lower at baseline in the lines without AK4P3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[MTCP1]] | B | AK4P3 activity raises MTCP1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without AK4P3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[PECAM1]] | B | AK4P3 activity raises PECAM1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.00× lower at baseline in the lines without AK4P3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[MYT1L]] | B | AK4P3 activity raises MYT1L's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without AK4P3 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[DIRC3]] | B | AK4P3 activity raises DIRC3's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.79× lower at baseline in the lines without AK4P3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[PECAM1]] | B | AK4P3 activity weakens PECAM1's drug response | lines that do not express AK4P3 (35) vs lines expressing it (11) | the lines without AK4P3 respond 32.85× as strongly (z diff -1.96); strongest at Idarubicin (hydrochloride) 5 µM: 5.99x vs 1.53x (z diff -5.9) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; target measured in part of the lines; artifact flags |
| [[GLRA3]] | B | AK4P3 activity raises GLRA3's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.48× lower at baseline in the lines without AK4P3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[CHRM5]] | B | AK4P3 activity raises CHRM5's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.57× lower at baseline in the lines without AK4P3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[RUNX1T1]] | C | AK4P3 activity raises RUNX1T1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 3.94× lower at baseline in the lines without AK4P3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[PCSK1]] | C | AK4P3 activity raises PCSK1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.77× lower at baseline in the lines without AK4P3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[KHDRBS2]] | C | AK4P3 activity raises KHDRBS2's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.50× lower at baseline in the lines without AK4P3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.385). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 37.1); signed map (44.4, 34.4). **Vector** length 35.3, 8.83% of its response variance represented; |z| ≥ 3 in 354 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +9.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.7 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 4 pseudogene 3 |
| Locus type | pseudogene |
| Location | 12p11.21 — chr12:31,615,023-31,652,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AK3L2P; previously AK3L2 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [645619](https://www.ncbi.nlm.nih.gov/gene/645619):

> Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in AMP metabolic process and nucleoside triphosphate biosynthetic process. Predicted to be located in mitochondrion. Predicted to be active in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21596) · Entrez [645619](https://www.ncbi.nlm.nih.gov/gene/645619) · Ensembl [ENSG00000233381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233381)

## Data

Gene col 13900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13900); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13900]; `tensor/DDL_lfc|DDL_z.npy` [13900]; `embed/gene_vectors.npy` [13900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13900 or target_col == 13900). Every well: [[AK4P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK4P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
