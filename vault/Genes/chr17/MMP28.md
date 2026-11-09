---
symbol: "MMP28"
type: "gene"
col: 15684
ensembl_id: "ENSG00000271447"
name: "matrix metallopeptidase 28"
location: "17q12"
module: 73
arm: "+"
pooled_cpm: 3.89
n_lines_expressing: 23
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 47
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# MMP28

*matrix metallopeptidase 28* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +12.5, q 8e-33, up in 6 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.514× (z -4.8, q 8e-04, down in 11 of 16 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.607× (z -3.6, q 0.087, down in 9 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.108×, Hs 766T 0.225×, LS 180 0.137×); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0956×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.235×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSE]] (+0.64, fdr 1e-05), [[ERG]] (+0.63, fdr 3e-05), [[CALB1]] (+0.62, fdr 3e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[C4BPB]] → it (grade B ⚠); 47 go from it, the strongest it → [[NOSTRIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +12.5 | 8e-33 | 6/13 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.95×** | +11.1 | 5e-26 | 1/2 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.81×** | +8.9 | 1e-16 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.36×** | +8.7 | 4e-16 | 3/6 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +8.1 | 4e-14 | 6/16 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +5.7 | 1e-06 | 7/15 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +4.8 | 1e-04 | 2/17 (NCI-H460, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +4.4 | 7e-04 | 2/13 (NCI-H460, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.06×** | +3.7 | 0.013 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.04×** | +3.7 | 0.014 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.044 | 2/15 (NCI-H23, CFPAC-1) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +3.3 | 0.051 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +3.2 | 0.061 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.074 | 1/15 (LS 180) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.108×, Hs 766T 0.225×, LS 180 0.137×); [[Panobinostat (drug)]] 5 µM in 1 line (Hs 766T 0.0956×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.235×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.514×** | -4.8 | 8e-04 | 11/16 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -3.6 | 0.087 | 9/15 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.633× | -3.2 | 0.28 | 7/14 (KATO III, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 102 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0956× (z -14.4) |
| [[LoVo (line)]] | wt | 9.12 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.8) |
| [[LS 180 (line)]] | wt | 4.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -8.5) |
| [[A-172 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.897 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSE]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ERG]] | +0.63 | +0.69 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[CALB1]] | +0.62 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[GPA33]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[REG4]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[FAM3D]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[DSG4]] | +0.59 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[TPTEP1-1]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LINC02582]] | +0.58 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[UGT1A1]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SEPTIN9-DT]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4BPB]] | B | C4BPB activity raises MMP28's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.08× lower at baseline in the lines without C4BPB | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[FXYD3]] | B | FXYD3 activity raises MMP28's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without FXYD3 | 0.083 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[LINC02582]] | C | LINC02582 activity raises MMP28's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.66× lower at baseline in the lines without LINC02582 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[CALB1]] | C | CALB1 activity raises MMP28's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.45× lower at baseline in the lines without CALB1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises MMP28's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 1.66× lower at baseline in the lines without TPTEP1-1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises MMP28's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.03× lower at baseline in the lines without LINC01133 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises MMP28's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 2.53× lower at baseline in the lines without KRT14 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises MMP28's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 1.96× lower at baseline in the lines without UGT1A6 | 0.047 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises MMP28's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.24× lower at baseline in the lines without KRT6A | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises MMP28's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without SPON1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises MMP28's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.98× lower at baseline in the lines without CYP4F12 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises MMP28's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.12× lower at baseline in the lines without UGT1A1 | 0.054 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 20, C 27. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | MMP28 activity raises NOSTRIN's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.97× lower at baseline in the lines without MMP28 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[PLAC8]] | B | MMP28 activity raises PLAC8's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without MMP28 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[PITPNM3]] | B | MMP28 activity raises PITPNM3's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without MMP28 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[PIK3AP1]] | B | MMP28 activity raises PIK3AP1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without MMP28 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[TRABD2A]] | B | MMP28 activity raises TRABD2A's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without MMP28 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[MUC12]] | B | MMP28 activity raises MUC12's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without MMP28 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[IGFL2]] | B | MMP28 activity raises IGFL2's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without MMP28 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[ITPK1]] | B | MMP28 activity raises ITPK1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without MMP28 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[FXYD3]] | B | MMP28 activity raises FXYD3's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.49× lower at baseline in the lines without MMP28 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[C4BPB]] | B | MMP28 activity raises C4BPB's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without MMP28 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[ABHD12B]] | B | MMP28 activity raises ABHD12B's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without MMP28 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[MUC3A]] | B | MMP28 activity raises MUC3A's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without MMP28 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.1, 49.7); signed map (66.1, 6.8). **Vector** length 44.1, 12.3% of its response variance represented; |z| ≥ 3 in 396 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +8.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.9 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.2 | -0.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | +0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,756,249-35,795,707 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MMP-25, MM28, EPILYSIN, MMP-28 |
| Gene groups (HGNC) | M10 matrix metallopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H239](https://www.uniprot.org/uniprotkb/Q9H239) (Matrix metalloproteinase-28):

> Can degrade casein. Could play a role in tissues homeostasis and repair.

**Summary**, from NCBI Gene [79148](https://www.ncbi.nlm.nih.gov/gene/79148):

> Proteins of the matrix metalloproteinase (MMP) family are involved in the breakdown of extracellular matrix for both normal physiological processes, such as embryonic development, reproduction and tissue remodeling, and disease processes, such as asthma and metastasis. This gene encodes a secreted enzyme that degrades casein. Its expression pattern suggests that it plays a role in tissue homeostasis and in wound repair. Alternative splicing of this gene results in multiple transcript variants. …

**Accessions** — [HGNC:14366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14366) · Entrez [79148](https://www.ncbi.nlm.nih.gov/gene/79148) · UniProt [Q9H239](https://www.uniprot.org/uniprotkb/Q9H239) · Ensembl [ENSG00000271447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271447)

## Data

Gene col 15684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15684); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15684]; `tensor/DDL_lfc|DDL_z.npy` [15684]; `embed/gene_vectors.npy` [15684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15684 or target_col == 15684). Every well: [[MMP28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
