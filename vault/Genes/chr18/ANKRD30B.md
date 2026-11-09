---
symbol: "ANKRD30B"
type: "gene"
col: 11130
ensembl_id: "ENSG00000180777"
name: "ankyrin repeat domain 30B"
location: "18p11.21"
module: 125
arm: "+"
pooled_cpm: 5.88
n_lines_expressing: 15
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 15
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ANKRD30B

*ankyrin repeat domain 30B* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.04× (z +11.0, q 3e-25, up in 4 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (J82 0.160×; ⚠ cell-cycle shift, explains ~81% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (J82 0.190×; ⚠ cell-cycle shift, explains ~98% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.217×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLAMF7]] (+0.74, fdr 7e-06), [[PSG4]] (+0.69, fdr 1e-05), [[ROR1-AS1]] (+0.68, fdr 7e-06); moves opposite to [[SRPX]] (-0.53, fdr 4e-05), [[TRIB2]] (-0.52, fdr 3e-05), [[DAAM2]] (-0.51, fdr 6e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PHACTR1]] → it (grade C ⚠); 15 go from it, the strongest it → [[LINC01828]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +11.0 | 3e-25 | 4/11 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.96×** | +10.8 | 1e-24 | 2/7 (BT-474, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.92×** | +10.6 | 7e-24 | 7/11 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +9.5 | 3e-19 | 4/9 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +9.0 | 3e-17 | 3/7 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +7.5 | 7e-12 | 10/11 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.82×** | +7.2 | 4e-11 | 10/12 (C32, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +5.9 | 3e-07 | 2/10 (C32, SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.23×** | +5.6 | 1e-06 | 11/12 (A-172, C32, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.97×** | +4.7 | 1e-04 | 3/11 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.99×** | +4.5 | 3e-04 | 5/11 (BT-474, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[EX229 (drug)]] 5 µM |  | **3.42×** | +4.5 | 3e-04 | 9/10 (C32, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.56×** | +4.4 | 5e-04 | 10/12 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +4.3 | 8e-04 | 8/12 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.83×** | +4.2 | 9e-04 | 3/12 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.018 | 2/12 (HS-578T, C32) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.41×** | +3.2 | 0.034 | 6/10 (J82, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.034 | 8/11 (SK-MEL-2, C32, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.044 | 3/12 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.62×** | +3.1 | 0.044 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11130.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (J82 0.160×; ⚠ cell-cycle shift, explains ~81% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (J82 0.190×; ⚠ cell-cycle shift, explains ~98% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.217×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.588× | -3.7 | 0.11 | 2/12 (BT-474, HT-29) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.620× | -3.4 | 0.21 | 4/12 (SNU-423, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 65.0 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 8.99× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.2) |
| [[J82 (line)]] | alt | 49.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.01× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -10.3) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0867× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.666 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAMF7]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PSG4]] | +0.69 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[ROR1-AS1]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PSG9]] | +0.63 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[DISC1FP1]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[IGFN1]] | +0.62 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[KCP]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NR1H4]] | +0.61 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[LINC00536]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CPEB1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LINC01320]] | +0.59 | +0.58 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPX]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TRIB2]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 | same gene group |
| [[DAAM2]] | -0.51 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[ANGPTL4]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[FN1]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[LTBP3]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[COL13A1]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PIGS]] | -0.46 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[STAU1]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[INPP5F]] | -0.45 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[RPGR]] | -0.45 | -0.30 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHACTR1]] | C | PHACTR1 activity raises ANKRD30B's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 3.62× lower at baseline in the lines without PHACTR1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises ANKRD30B's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.38× lower at baseline in the lines without LINC01320 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises ANKRD30B's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 4.19× lower at baseline in the lines without PSG4 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[PNLIPRP3]] | C | PNLIPRP3 activity raises ANKRD30B's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.61× lower at baseline in the lines without PNLIPRP3 | 0.059 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |
| [[DAAM2]] | C | DAAM2 activity raises ANKRD30B's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without DAAM2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[SOX11]] | C | SOX11 activity raises ANKRD30B's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.11× lower at baseline in the lines without SOX11 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[TENM3-AS1]] | C | TENM3-AS1 activity raises ANKRD30B's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without TENM3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises ANKRD30B's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without NR1H4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[PSG9]] | C | PSG9 activity raises ANKRD30B's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 6.85× lower at baseline in the lines without PSG9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[DISC1FP1]] | C | DISC1FP1 activity raises ANKRD30B's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without DISC1FP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[SHISA9]] | C | SHISA9 activity raises ANKRD30B's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without SHISA9 | 0.098 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[ENTHD1]] | C | ENTHD1 activity raises ANKRD30B's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without ENTHD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01828]] | B | ANKRD30B activity raises LINC01828's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without ANKRD30B | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF |
| [[AMPD3]] | B | ANKRD30B activity raises AMPD3's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 2.37× lower at baseline in the lines without ANKRD30B | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF |
| [[C12orf50]] | B | ANKRD30B activity raises C12orf50's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without ANKRD30B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF |
| [[LINC00882]] | B | ANKRD30B activity raises LINC00882's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 4.15× lower at baseline in the lines without ANKRD30B | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF |
| [[SLC25A48]] | B | ANKRD30B activity raises SLC25A48's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without ANKRD30B | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF |
| [[DAAM2]] | C | ANKRD30B activity raises DAAM2's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.17× lower at baseline in the lines without ANKRD30B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[FN1]] | C | ANKRD30B activity raises FN1's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 8.59× lower at baseline in the lines without ANKRD30B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[LINC01320]] | C | ANKRD30B activity raises LINC01320's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.91× lower at baseline in the lines without ANKRD30B | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[ENTHD1]] | C | ANKRD30B activity raises ENTHD1's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.62× lower at baseline in the lines without ANKRD30B | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[LINC00504]] | C | ANKRD30B activity raises LINC00504's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without ANKRD30B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[PSG4]] | C | ANKRD30B activity raises PSG4's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without ANKRD30B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[SRPX]] | C | ANKRD30B activity raises SRPX's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 5.37× lower at baseline in the lines without ANKRD30B | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, 22.3); signed map (38.6, 23.4). **Vector** length 43.3, 14.0% of its response variance represented; |z| ≥ 3 in 331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.0 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 30B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:14,728,272-14,854,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-BR-1.1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; N-Ank proteins |
| Matched by | ensembl_id |

UniProt [Q9BXX2](https://www.uniprot.org/uniprotkb/Q9BXX2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24165) · Entrez [374860](https://www.ncbi.nlm.nih.gov/gene/374860) · UniProt [Q9BXX2](https://www.uniprot.org/uniprotkb/Q9BXX2) · Ensembl [ENSG00000180777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180777)

## Data

Gene col 11130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11130); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11130]; `tensor/DDL_lfc|DDL_z.npy` [11130]; `embed/gene_vectors.npy` [11130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11130 or target_col == 11130). Every well: [[ANKRD30B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD30B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
