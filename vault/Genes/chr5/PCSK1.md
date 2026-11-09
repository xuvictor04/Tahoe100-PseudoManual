---
symbol: "PCSK1"
type: "gene"
col: 10609
ensembl_id: "ENSG00000175426"
name: "proprotein convertase subtilisin/kexin type 1"
location: "5q15"
module: 9
arm: "+"
pooled_cpm: 15.28
n_lines_expressing: 10
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 35
direction_downstream: 49
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PCSK1

*proprotein convertase subtilisin/kexin type 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.75× (z +11.8, q 2e-29, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +5.0, q 8e-05, up in 0 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.88×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.501× (z -5.2, q 1e-04, down in 7 of 8 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIT2]] (+0.82, fdr 7e-06), [[ASCL1]] (+0.81, fdr 7e-06), [[KCNB2]] (+0.80, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 49 go from it, the strongest it → [[KCNMB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10609.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.88×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.75×** | +11.8 | 2e-29 | 4/5 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +10.2 | 5e-22 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +7.8 | 1e-12 | 3/5 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.0 | 8e-05 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +4.7 | 2e-04 | 1/6 (SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.58×** | +3.8 | 0.016 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.096 | 4/8 (NCI-H460, SW 1088, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.52× | +3.2 | 0.11 | 0/8 | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.50× | +3.1 | 0.13 | 0/6 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.501×** | -5.2 | 1e-04 | 7/8 (SHP-77, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.556×** | -4.1 | 0.012 | 0/6 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.607×** | -3.8 | 0.031 | 4/8 (SHP-77, SW1417, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.613×** | -3.4 | 0.088 | 0/8 | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.633× | -3.3 | 0.12 | 0/7 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.665× | -3.1 | 0.19 | 4/7 (SHP-77, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 698 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 5.83 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Docetaxel (drug)]] 0.05 µM 0.0836× (z -11.3) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIT2]] | +0.82 | +0.82 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ASCL1]] | +0.81 | +0.81 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.80 | +0.78 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.80 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[LRFN2]] | +0.79 | +0.80 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SRRM4]] | +0.78 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[GRIK1]] | +0.78 | +0.76 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.77 | +0.77 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[CSMD3]] | +0.75 | +0.77 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.74 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[CGA]] | +0.74 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Peptide hormone biosynthesis |
| [[RMST]] | +0.73 | +0.73 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 1, C 34. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PCSK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CALCA]] | C | CALCA activity raises PCSK1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 11.34× lower at baseline in the lines without CALCA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises PCSK1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 7.45× lower at baseline in the lines without SYT4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[H19]] | C | H19 activity raises PCSK1's level | lines that do not express H19 (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without H19 | 0.004 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises PCSK1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without FKBP9P1-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises PCSK1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 7.40× lower at baseline in the lines without RIT2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[CGA]] | C | CGA activity raises PCSK1's level | lines that do not express CGA (44) vs lines expressing it (6) | 7.50× lower at baseline in the lines without CGA | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises PCSK1's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 4.09× lower at baseline in the lines without LINC01287 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises PCSK1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.77× lower at baseline in the lines without AK4P3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises PCSK1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 5.57× lower at baseline in the lines without KCNB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises PCSK1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.10× lower at baseline in the lines without ASCL1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises PCSK1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without MIR3667HG | 0.023 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 7, C 42. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2]] | B | PCSK1 activity raises KCNMB2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.54× lower at baseline in the lines without PCSK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[LINC02466]] | B | PCSK1 activity raises LINC02466's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 1.81× lower at baseline in the lines without PCSK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[GRIK2]] | B | PCSK1 activity raises GRIK2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.03× lower at baseline in the lines without PCSK1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[MIAT]] | B | PCSK1 activity raises MIAT's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.65× lower at baseline in the lines without PCSK1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[MYT1L]] | B | PCSK1 activity raises MYT1L's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without PCSK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[CHRM5]] | B | PCSK1 activity raises CHRM5's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 1.85× lower at baseline in the lines without PCSK1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[MTMR7]] | B | PCSK1 activity raises MTMR7's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.29× lower at baseline in the lines without PCSK1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[SCG2]] | C | PCSK1 activity raises SCG2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.59× lower at baseline in the lines without PCSK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[RMST]] | C | PCSK1 activity raises RMST's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.03× lower at baseline in the lines without PCSK1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[LINC01980]] | C | PCSK1 activity raises LINC01980's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.75× lower at baseline in the lines without PCSK1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[CPLX2]] | C | PCSK1 activity raises CPLX2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.72× lower at baseline in the lines without PCSK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[ST18]] | C | PCSK1 activity raises ST18's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.61× lower at baseline in the lines without PCSK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 37.0); signed map (45.2, 34.3). **Vector** length 29.9, 12.5% of its response variance represented; |z| ≥ 3 in 128 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.0 | +2.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:96,390,333-96,434,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PC1, PC3, SPC3, PC1/3; previously NEC1 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 11 pathways, smallest: Peptide hormone biosynthesis; Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and deacylation of Ghrelin |
| Matched by | ensembl_id |

**Function**, from UniProt [P29120](https://www.uniprot.org/uniprotkb/P29120) (Neuroendocrine convertase 1):

> Involved in the processing of hormone and other protein precursors at sites comprised of pairs of basic amino acid residues. Substrates include POMC, renin, oxytocin, vasopressin, enkephalin, dynorphin, somatostatin, insulin and AGRP.

**Summary**, from NCBI Gene [5122](https://www.ncbi.nlm.nih.gov/gene/5122):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. The encoded protein undergoes an initial autocatalytic processing event in the ER to generate a heterodimer which exits the ER and sorts to subcellular compartments where a second autocatalytic even takes place and the catalytic activity is acquired. The protease is …

**Accessions** — [HGNC:8743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8743) · Entrez [5122](https://www.ncbi.nlm.nih.gov/gene/5122) · UniProt [P29120](https://www.uniprot.org/uniprotkb/P29120) · Ensembl [ENSG00000175426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175426)

## Data

Gene col 10609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10609); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10609]; `tensor/DDL_lfc|DDL_z.npy` [10609]; `embed/gene_vectors.npy` [10609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10609 or target_col == 10609). Every well: [[PCSK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
