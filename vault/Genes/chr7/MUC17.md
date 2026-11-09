---
symbol: "MUC17"
type: "gene"
col: 9865
ensembl_id: "ENSG00000169876"
name: "mucin 17, cell surface associated"
location: "7q22.1"
module: 73
arm: "+"
pooled_cpm: 25.83
n_lines_expressing: 6
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 63
direction_downstream: 84
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# MUC17

*mucin 17, cell surface associated* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.41× (z +10.3, q 5e-22, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +8.3, q 1e-14, up in 1 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Pimozide (drug)]] 5 µM: 0.509× (z -4.7, q 0.002, down in 0 of 4 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.84, fdr 7e-06), [[HEPH]] (+0.83, fdr 7e-06), [[CALB1]] (+0.82, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 63 arrows point to it, the strongest [[NPSR1]] → it (grade C ⚠); 84 go from it, the strongest it → [[MUC12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +10.3 | 5e-22 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.45×** | +8.8 | 5e-16 | 0/4 | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +8.3 | 1e-14 | 1/4 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +7.0 | 3e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.59×** | +5.5 | 4e-06 | 1/1 (AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +5.4 | 7e-06 | 3/4 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +5.3 | 1e-05 | 0/4 | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +5.1 | 2e-05 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +4.0 | 0.004 | 2/4 (HT-29, AsPC-1) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.015 | 0/4 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.72×** | +3.6 | 0.015 | 2/4 (KATO III, HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.60×** | +3.3 | 0.051 | 0/4 | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.072 | 2/4 (HT-29, KATO III) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pimozide (drug)]] 5 µM |  | **0.509×** | -4.7 | 0.002 | 0/4 | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.539×** | -4.3 | 0.006 | 4/4 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.558×** | -3.9 | 0.013 | 0/4 | rises with dose | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.548×** | -3.8 | 0.013 | 0/4 | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.576×** | -3.8 | 0.013 | 4/4 (LS 180, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -3.8 | 0.013 | 4/4 (LS 180, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.561×** | -3.8 | 0.013 | 0/4 | inconsistent across doses | position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.587×** | -3.7 | 0.017 | 0/4 | inconsistent across doses | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.610×** | -3.4 | 0.040 | 0/4 | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.615×** | -3.4 | 0.045 | 0/4 | rises with dose | low cells (technical?); position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | **0.618×** | -3.3 | 0.046 | 0/4 | inconsistent across doses |  |
| [[Dabrafenib (drug)]] 0.05 µM |  | **0.613×** | -3.2 | 0.068 | 0/4 | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.643× | -3.0 | 0.10 | 4/4 (LS 180, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 194 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -15.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 709 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.84 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.83 | +0.75 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.82 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.79 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TMEM30B]] | +0.78 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.78 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | pathway: O-linked glycosylation; STRING 571 |
| [[LINC02474]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[C4BPB]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[TPTEP1-1]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 0, C 63. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPSR1]] | C | NPSR1 activity raises MUC17's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 11.51× lower at baseline in the lines without NPSR1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[REG4]] | C | REG4 activity raises MUC17's level | lines that do not express REG4 (43) vs lines expressing it (7) | 16.52× lower at baseline in the lines without REG4 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises MUC17's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 7.85× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises MUC17's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 5.19× lower at baseline in the lines without GPA33 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises MUC17's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.80× lower at baseline in the lines without MYO7B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises MUC17's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 6.01× lower at baseline in the lines without CEACAM5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises MUC17's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 3.61× lower at baseline in the lines without MUC6 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises MUC17's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 7.27× lower at baseline in the lines without MUC13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises MUC17's level | lines that do not express LYZ (40) vs lines expressing it (10) | 7.15× lower at baseline in the lines without LYZ | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[TM4SF4]] | C | TM4SF4 activity raises MUC17's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 5.58× lower at baseline in the lines without TM4SF4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises MUC17's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 4.41× lower at baseline in the lines without PPP1R1B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises MUC17's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 7.03× lower at baseline in the lines without LINC02582 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 15, C 69. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC12]] | B | MUC17 activity raises MUC12's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 3.91× lower at baseline in the lines without MUC17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[NOSTRIN]] | B | MUC17 activity raises NOSTRIN's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 5.86× lower at baseline in the lines without MUC17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[SDCBP2]] | B | MUC17 activity raises SDCBP2's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 9.07× lower at baseline in the lines without MUC17 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[MYH14]] | B | MUC17 activity raises MYH14's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 7.09× lower at baseline in the lines without MUC17 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[MYO18A]] | B | MUC17 activity raises MYO18A's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.03× lower at baseline in the lines without MUC17 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[EPS8L1]] | B | MUC17 activity raises EPS8L1's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 5.04× lower at baseline in the lines without MUC17 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[SLC37A1]] | B | MUC17 activity raises SLC37A1's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 3.60× lower at baseline in the lines without MUC17 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[HTR1D]] | B | MUC17 activity raises HTR1D's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.23× lower at baseline in the lines without MUC17 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[PLEKHA6]] | B | MUC17 activity raises PLEKHA6's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 3.49× lower at baseline in the lines without MUC17 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[SEPTIN9-DT]] | B | MUC17 activity raises SEPTIN9-DT's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.63× lower at baseline in the lines without MUC17 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[PITX1]] | B | MUC17 activity raises PITX1's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.73× lower at baseline in the lines without MUC17 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[LINC02580]] | B | MUC17 activity raises LINC02580's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.61× lower at baseline in the lines without MUC17 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.4, 50.9); signed map (64.9, 7.8). **Vector** length 22.2, 13.0% of its response variance represented; |z| ≥ 3 in 62 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.6 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.5 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | +0.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.4 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.4 | -2.6 |
|  | [[Futibatinib (drug)]] 0.05 µM |  | -0.4 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | mucin 17, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,020,072-101,058,859 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mucins; SEA domain containing |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q685J3](https://www.uniprot.org/uniprotkb/Q685J3) (Mucin-17):

> Probably plays a role in maintaining homeostasis on mucosal surfaces.

**Summary**, from NCBI Gene [140453](https://www.ncbi.nlm.nih.gov/gene/140453):

> The protein encoded by this gene is a membrane-bound mucin that provides protection to gut epithelial cells. The encoded protein contains about 60 tandem repeats, with each repeat being around 60 aa. N-glycosylation enables the encoded protein to localize on the cell surface, while the C-terminus interacts with the scaffold protein PDZ domain containing 1 (PDZK1). Two transcript variants, one protein-coding and the other non-protein coding, have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:16800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16800) · Entrez [140453](https://www.ncbi.nlm.nih.gov/gene/140453) · UniProt [Q685J3](https://www.uniprot.org/uniprotkb/Q685J3) · Ensembl [ENSG00000169876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169876)

## Data

Gene col 9865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9865); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9865]; `tensor/DDL_lfc|DDL_z.npy` [9865]; `embed/gene_vectors.npy` [9865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9865 or target_col == 9865). Every well: [[MUC17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
