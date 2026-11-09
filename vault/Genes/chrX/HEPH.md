---
symbol: "HEPH"
type: "gene"
col: 1588
ensembl_id: "ENSG00000089472"
name: "hephaestin"
location: "Xq12"
module: 73
arm: "+"
pooled_cpm: 10.98
n_lines_expressing: 9
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 75
direction_downstream: 71
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# HEPH

*hephaestin* — Xq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.04× (z +11.7, q 8e-29, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +7.5, q 2e-11, up in 0 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.120×, LS 180 0.168×, HT-29 0.127×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.117×, LS 180 0.228×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.154×, HT-29 0.122×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.209×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.89, fdr 7e-06), [[GCNT3]] (+0.86, fdr 7e-06), [[FAM3D]] (+0.85, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[REG4]] → it (grade C ⚠); 71 go from it, the strongest it → [[MUC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +11.7 | 8e-29 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.47×** | +10.8 | 6e-25 | 1/5 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +7.5 | 2e-11 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +6.5 | 1e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +6.4 | 1e-08 | 4/7 (SW1417, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.4 | 0.001 | 3/7 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.2 | 0.002 | 0/5 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.025 | 0/7 | top dose only | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **1.55×** | +3.5 | 0.028 | 2/6 (H4, LoVo) | inconsistent across doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.65×** | +3.4 | 0.033 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.4 | 0.033 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.034 | 2/6 (SW1417, H4) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.2 | 0.068 | 0/5 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.078 | 0/7 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1588.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 0.120×, LS 180 0.168×, HT-29 0.127×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.117×, LS 180 0.228×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.154×, HT-29 0.122×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.209×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | 0.468× | -3.5 | 0.13 | 0/7 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.676× | -3.4 | 0.13 | 1/7 (LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.760× | -3.4 | 0.13 | 3/7 (KATO III, SW48, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.700× | -3.1 | 0.19 | 0/7 | two highest doses | position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.704× | -3.1 | 0.19 | 0/7 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.684× | -3.1 | 0.19 | 0/7 | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.699× | -3.0 | 0.19 | 1/7 (LoVo) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.785× | -3.0 | 0.19 | 0/7 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 143 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -19.5) |
| [[LS 180 (line)]] | wt | 178 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -17.8) |
| [[HT-29 (line)]] | alt | 33.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -13.3) |
| [[A-172 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.858 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.89 | +0.88 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.86 | +0.86 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.85 | +0.88 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.85 | +0.81 / +0.81 | both halves | 7e-06 | pathway: Disorders of transmembrane transporters |
| [[CDH17]] | +0.84 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MUC17]] | +0.83 | +0.75 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[DSG4]] | +0.82 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.82 | +0.81 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TPTEP1-1]] | +0.80 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[CFTR]] | +0.79 | +0.87 / +0.69 | both halves | 7e-06 | pathway: Disorders of transmembrane transporters |
| [[LINC02474]] | +0.79 | +0.79 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 0, C 75. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REG4]] | C | REG4 activity raises HEPH's level | lines that do not express REG4 (43) vs lines expressing it (7) | 10.01× lower at baseline in the lines without REG4 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises HEPH's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without PTPRR | 0.001 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises HEPH's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 5.26× lower at baseline in the lines without MUC2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises HEPH's level | lines that do not express CFTR (39) vs lines expressing it (11) | 4.19× lower at baseline in the lines without CFTR | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises HEPH's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 7.41× lower at baseline in the lines without NPSR1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises HEPH's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 5.81× lower at baseline in the lines without CDH17 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[FGFR2]] | C | FGFR2 activity raises HEPH's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 6.87× lower at baseline in the lines without FGFR2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises HEPH's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 6.65× lower at baseline in the lines without MUC17 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises HEPH's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without LINC01133 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises HEPH's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.75× lower at baseline in the lines without TPTEP1-1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises HEPH's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.40× lower at baseline in the lines without CEACAM5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises HEPH's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.90× lower at baseline in the lines without LINC02582 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |

### Downstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 12, C 59. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC12]] | B | HEPH activity raises MUC12's level | lines that do not express HEPH (41) vs lines expressing it (9) | 3.24× lower at baseline in the lines without HEPH | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[MYH14]] | B | HEPH activity raises MYH14's level | lines that do not express HEPH (41) vs lines expressing it (9) | 6.88× lower at baseline in the lines without HEPH | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[SLC12A2]] | B | HEPH activity raises SLC12A2's level | lines that do not express HEPH (41) vs lines expressing it (9) | 3.00× lower at baseline in the lines without HEPH | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[EPS8L1]] | B | HEPH activity raises EPS8L1's level | lines that do not express HEPH (41) vs lines expressing it (9) | 4.83× lower at baseline in the lines without HEPH | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[BAG1]] | B | HEPH activity raises BAG1's level | lines that do not express HEPH (41) vs lines expressing it (9) | 1.86× lower at baseline in the lines without HEPH | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[NOSTRIN]] | B | HEPH activity raises NOSTRIN's level | lines that do not express HEPH (41) vs lines expressing it (9) | 3.64× lower at baseline in the lines without HEPH | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[ADAP1]] | B | HEPH activity raises ADAP1's level | lines that do not express HEPH (41) vs lines expressing it (9) | 3.67× lower at baseline in the lines without HEPH | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[IGSF9]] | B | HEPH activity raises IGSF9's level | lines that do not express HEPH (41) vs lines expressing it (9) | 2.25× lower at baseline in the lines without HEPH | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[GAREM1]] | B | HEPH activity raises GAREM1's level | lines that do not express HEPH (41) vs lines expressing it (9) | 2.77× lower at baseline in the lines without HEPH | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[B4GALNT3]] | B | HEPH activity raises B4GALNT3's level | lines that do not express HEPH (41) vs lines expressing it (9) | 4.30× lower at baseline in the lines without HEPH | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[GSKIP]] | B | HEPH activity raises GSKIP's level | lines that do not express HEPH (41) vs lines expressing it (9) | 1.63× lower at baseline in the lines without HEPH | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |
| [[LINC02580]] | B | HEPH activity raises LINC02580's level | lines that do not express HEPH (41) vs lines expressing it (9) | 2.42× lower at baseline in the lines without HEPH | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.5, 50.7); signed map (64.8, 7.7). **Vector** length 41.8, 22.7% of its response variance represented; |z| ≥ 3 in 185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +11.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.7 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.7 | +0.7 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.8 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | hephaestin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12 — chrX:66,162,671-66,268,867 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0698, CPL |
| Gene groups (HGNC) | Multicopper ferroxidase family |
| Reactome | 6 pathways, smallest: Metal ion SLC transporters; Iron uptake and transport; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQS7](https://www.uniprot.org/uniprotkb/Q9BQS7) (Hephaestin):

> Plasma membrane ferroxidase that mediates the extracellular conversion of ferrous/Fe(2+) iron into its ferric/Fe(3+) form. Couples ferroportin which specifically exports ferrous/Fe(2+) iron from cells to transferrin that only binds and shuttles extracellular ferric/Fe(3+) iron throughout the body. By helping iron transfer from cells to blood mainly contributes to dietary iron absorption by the intestinal epithelium and more generally regulates iron levels in the body (By similarity).

**Summary**, from NCBI Gene [9843](https://www.ncbi.nlm.nih.gov/gene/9843):

> This gene encodes a member of the multicopper oxidase protein family. The encoded protein is involved in the transport of dietary iron from epithelial cells of the intestinal lumen into the circulatory system, and may be involved in copper transport and homeostasis. In mouse, defects in this gene can lead to severe microcytic anemia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:4866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4866) · Entrez [9843](https://www.ncbi.nlm.nih.gov/gene/9843) · UniProt [Q9BQS7](https://www.uniprot.org/uniprotkb/Q9BQS7) · Ensembl [ENSG00000089472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089472)

## Data

Gene col 1588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1588); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1588]; `tensor/DDL_lfc|DDL_z.npy` [1588]; `embed/gene_vectors.npy` [1588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1588 or target_col == 1588). Every well: [[HEPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
