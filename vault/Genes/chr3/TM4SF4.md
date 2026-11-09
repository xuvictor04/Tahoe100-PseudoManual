---
symbol: "TM4SF4"
type: "gene"
col: 9870
ensembl_id: "ENSG00000169903"
name: "transmembrane 4 L six family member 4"
location: "3q25.1"
module: 44
arm: "+"
pooled_cpm: 8.01
n_lines_expressing: 8
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 30
direction_downstream: 56
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TM4SF4

*transmembrane 4 L six family member 4* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.56× (z +12.2, q 2e-31, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.59× (z +9.0, q 2e-17, up in 2 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.536× (z -3.9, q 0.050, down in 0 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.0629×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.158×; ⚠ cell-cycle shift, explains ~47% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HT-29 0.0959×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.116×); [[Belinostat (drug)]] 5 µM in 1 line (HT-29 0.127×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.305×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPNT]] (+0.78, fdr 7e-06), [[TSPAN8]] (+0.77, fdr 7e-06), [[BCL2L15]] (+0.74, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[AKR1B10]] → it (grade C ⚠); 56 go from it, the strongest it → [[MUC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.56×** | +12.2 | 2e-31 | 2/2 (CFPAC-1, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.05×** | +10.9 | 2e-25 | 4/5 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.92×** | +9.9 | 5e-21 | 3/5 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +9.0 | 2e-17 | 2/6 (AsPC-1, A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.13×** | +5.1 | 4e-05 | 1/4 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +4.8 | 1e-04 | 0/6 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.2 | 0.002 | 2/5 (CFPAC-1, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.1 | 0.002 | 0/6 | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.52×** | +4.0 | 0.005 | 2/6 (AsPC-1, A549) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.89×** | +3.7 | 0.010 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +3.5 | 0.027 | 1/6 (AsPC-1) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.3 | 0.042 | 4/6 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.1 | 0.073 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.87× | +3.0 | 0.11 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9870.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.0629×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.158×; ⚠ cell-cycle shift, explains ~47% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HT-29 0.0959×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.116×); [[Belinostat (drug)]] 5 µM in 1 line (HT-29 0.127×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.305×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.536×** | -3.9 | 0.050 | 0/6 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.639× | -3.1 | 0.30 | 5/6 (HT-29, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 235 | 0 | 9 (6 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0629× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.116× (z -11.8) |
| [[A-172 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.637 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPNT]] | +0.78 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 | STRING 433 |
| [[BCL2L15]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[KRT20]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MGAM2]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN1]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 | STRING 426 |
| [[MMP7]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A6]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 | STRING 444 |
| [[CDH17]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[BCAS1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 0, C 30. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1B10]] | C | AKR1B10 activity raises TM4SF4's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 3.71× lower at baseline in the lines without AKR1B10 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises TM4SF4's level | lines that do not express GABRP (44) vs lines expressing it (6) | 5.28× lower at baseline in the lines without GABRP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises TM4SF4's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.84× lower at baseline in the lines without AGR3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[HHLA2]] | C | HHLA2 activity raises TM4SF4's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 3.52× lower at baseline in the lines without HHLA2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises TM4SF4's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.24× lower at baseline in the lines without MMP7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises TM4SF4's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.87× lower at baseline in the lines without MUC5B | 0.013 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises TM4SF4's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without HNF1A-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises TM4SF4's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.15× lower at baseline in the lines without GCNT3 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[KRT20]] | C | KRT20 activity raises TM4SF4's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.84× lower at baseline in the lines without KRT20 | 0.020 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises TM4SF4's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 3.50× lower at baseline in the lines without TRIM31 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises TM4SF4's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.59× lower at baseline in the lines without SMIM2-AS1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises TM4SF4's level | lines that do not express LYZ (40) vs lines expressing it (10) | 3.34× lower at baseline in the lines without LYZ | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 10, C 46. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC12]] | B | TM4SF4 activity raises MUC12's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.59× lower at baseline in the lines without TM4SF4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[GNA14]] | B | TM4SF4 activity raises GNA14's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.26× lower at baseline in the lines without TM4SF4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[HGD]] | B | TM4SF4 activity raises HGD's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.32× lower at baseline in the lines without TM4SF4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[MYH14]] | B | TM4SF4 activity raises MYH14's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 4.19× lower at baseline in the lines without TM4SF4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[PLCH1]] | B | TM4SF4 activity raises PLCH1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.66× lower at baseline in the lines without TM4SF4 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[RSPH1]] | B | TM4SF4 activity raises RSPH1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.10× lower at baseline in the lines without TM4SF4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[ALDH3B1]] | B | TM4SF4 activity raises ALDH3B1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.31× lower at baseline in the lines without TM4SF4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[PBX1]] | B | TM4SF4 activity raises PBX1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.60× lower at baseline in the lines without TM4SF4 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[SORL1]] | B | TM4SF4 activity raises SORL1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 3.57× lower at baseline in the lines without TM4SF4 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[RBM47]] | B | TM4SF4 activity raises RBM47's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 4.48× lower at baseline in the lines without TM4SF4 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[HHLA2]] | C | TM4SF4 activity raises HHLA2's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 7.28× lower at baseline in the lines without TM4SF4 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[MUC5B]] | C | TM4SF4 activity raises MUC5B's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 4.27× lower at baseline in the lines without TM4SF4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, 52.8); signed map (61.4, 2.5). **Vector** length 30.8, 14.4% of its response variance represented; |z| ≥ 3 in 143 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.51 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.51 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.6 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 4 L six family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,474,697-149,503,394 (+) |
| Ensembl biotype | protein_coding |
| Also known as | il-TMP |
| Gene groups (HGNC) | Transmembrane 4 L six family |
| Matched by | ensembl_id |

**Function**, from UniProt [P48230](https://www.uniprot.org/uniprotkb/P48230) (Transmembrane 4 L6 family member 4):

> Regulates the adhesive and proliferative status of intestinal epithelial cells. Can mediate density-dependent cell proliferation.

**Summary**, from NCBI Gene [7104](https://www.ncbi.nlm.nih.gov/gene/7104):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is a cell surface glycoprotein that can regulate cell proliferation.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:11856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11856) · Entrez [7104](https://www.ncbi.nlm.nih.gov/gene/7104) · UniProt [P48230](https://www.uniprot.org/uniprotkb/P48230) · Ensembl [ENSG00000169903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169903)

## Data

Gene col 9870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9870); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9870]; `tensor/DDL_lfc|DDL_z.npy` [9870]; `embed/gene_vectors.npy` [9870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9870 or target_col == 9870). Every well: [[TM4SF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM4SF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
