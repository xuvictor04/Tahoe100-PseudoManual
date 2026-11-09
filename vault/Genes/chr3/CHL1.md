---
symbol: "CHL1"
type: "gene"
col: 5514
ensembl_id: "ENSG00000134121"
name: "cell adhesion molecule L1 like"
location: "3p26.3"
module: 19
arm: "+"
pooled_cpm: 26.01
n_lines_expressing: 8
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 28
direction_downstream: 32
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CHL1

*cell adhesion molecule L1 like* — 3p26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +7.9, q 1e-12, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +4.4, q 0.002, up in 2 of 5 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.401× (z -5.8, q 4e-06, down in 3 of 3 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARA5]] (+0.91, fdr 7e-06), [[LINC03000]] (+0.90, fdr 7e-06), [[GREM2]] (+0.86, fdr 7e-06); moves opposite to [[ADRA2C]] (-0.47, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 32 go from it, the strongest it → [[PLAC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +7.9 | 1e-12 | 2/4 (C32, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +7.5 | 1e-11 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +4.7 | 5e-04 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.4 | 0.002 | 2/5 (SK-MEL-2, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.66× | +3.1 | 0.21 | 2/5 (SK-MEL-2, C32) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -5.8 | 4e-06 | 3/3 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -4.1 | 0.011 | 3/5 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.531×** | -4.0 | 0.011 | 3/5 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.550×** | -3.8 | 0.021 | 3/5 (NCI-H460, C32, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.559×** | -3.7 | 0.026 | 3/5 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.558×** | -3.6 | 0.027 | 1/5 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.569×** | -3.6 | 0.027 | 2/4 (NCI-H460, C32) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.546×** | -3.5 | 0.027 | 0/5 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.576×** | -3.5 | 0.029 | 3/5 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.035 | 4/5 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.592× | -3.1 | 0.11 | 1/5 (AN3 CA) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.598× | -3.0 | 0.12 | 1/5 (AN3 CA) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 444 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0293× (z -28.3) |
| [[A-172 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARA5]] | +0.91 | +0.84 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.90 | +0.84 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.85 | +0.75 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.85 | +0.75 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.84 | +0.73 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A5]] | +0.83 | +0.84 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.83 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.83 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.82 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[LIN7A]] | +0.78 | +0.70 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADRA2C]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 1, C 27. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CHL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GSG1L2]] | C | GSG1L2 activity raises CHL1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 7.33× lower at baseline in the lines without GSG1L2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises CHL1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 4.94× lower at baseline in the lines without GTF2I-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises CHL1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.98× lower at baseline in the lines without MARCOL, SPINK13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC03000]] | C | LINC03000 activity raises CHL1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 5.73× lower at baseline in the lines without LINC03000 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises CHL1's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 5.10× lower at baseline in the lines without SLC15A5 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[GASK1B]] | C | GASK1B activity raises CHL1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without GASK1B | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises CHL1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.94× lower at baseline in the lines without GREM2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises CHL1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without TTTY10 | 0.021 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises CHL1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.66× lower at baseline in the lines without CTNND2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[SCG3]] | C | SCG3 activity raises CHL1's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 3.42× lower at baseline in the lines without SCG3 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[UTY]] | C | UTY activity raises CHL1's level | lines that do not express UTY (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without UTY | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 8, C 24. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | CHL1 activity raises PLAC4's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.93× lower at baseline in the lines without CHL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SOX6]] | B | CHL1 activity raises SOX6's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 5.09× lower at baseline in the lines without CHL1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[LMNTD1]] | B | CHL1 activity raises LMNTD1's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 1.71× lower at baseline in the lines without CHL1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[TNFRSF19]] | B | CHL1 activity raises TNFRSF19's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 4.71× lower at baseline in the lines without CHL1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SPDYE10]] | B | CHL1 activity raises SPDYE10's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 1.83× lower at baseline in the lines without CHL1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[PART1]] | B | CHL1 activity raises PART1's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 1.86× lower at baseline in the lines without CHL1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[RHOH]] | B | CHL1 activity raises RHOH's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.74× lower at baseline in the lines without CHL1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[PCDH15]] | B | CHL1 activity raises PCDH15's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 2.72× lower at baseline in the lines without CHL1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[CDH19]] | C | CHL1 activity raises CDH19's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 8.56× lower at baseline in the lines without CHL1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[LINC03000]] | C | CHL1 activity raises LINC03000's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 4.73× lower at baseline in the lines without CHL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[TTTY10]] | C | CHL1 activity raises TTTY10's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.20× lower at baseline in the lines without CHL1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[TBXT]] | C | CHL1 activity raises TBXT's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.90× lower at baseline in the lines without CHL1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 36.3); signed map (43.1, 43.9). **Vector** length 37.7, 27.2% of its response variance represented; |z| ≥ 3 in 114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.1 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +0.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.5 | +2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.5 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -0.6 | -3.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.6 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.6 | -3.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -3.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.5 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cell adhesion molecule L1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.3 — chr3:196,763-409,417 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CALL, L1CAM2, FLJ44930, MGC132578 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 4 pathways, smallest: CHL1 interactions; L1CAM interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O00533](https://www.uniprot.org/uniprotkb/O00533) (Neural cell adhesion molecule L1-like protein):

> Extracellular matrix and cell adhesion protein that plays a role in nervous system development and in synaptic plasticity. Both soluble and membranous forms promote neurite outgrowth of cerebellar and hippocampal neurons and suppress neuronal cell death. Plays a role in neuronal positioning of pyramidal neurons and in regulation of both the number of interneurons and the efficacy of GABAergic synapses. May play a role in regulating cell migration in nerve regeneration and cortical development. …

**Summary**, from NCBI Gene [10752](https://www.ncbi.nlm.nih.gov/gene/10752):

> The protein encoded by this gene is a member of the L1 gene family of neural cell adhesion molecules. It is a neural recognition molecule that may be involved in signal transduction pathways. The deletion of one copy of this gene may be responsible for mental defects in patients with 3p- syndrome. This protein may also play a role in the growth of certain cancers. Alternate splicing results in both coding and non-coding variants. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:1939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1939) · Entrez [10752](https://www.ncbi.nlm.nih.gov/gene/10752) · UniProt [O00533](https://www.uniprot.org/uniprotkb/O00533) · Ensembl [ENSG00000134121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134121)

## Data

Gene col 5514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5514); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5514]; `tensor/DDL_lfc|DDL_z.npy` [5514]; `embed/gene_vectors.npy` [5514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5514 or target_col == 5514). Every well: [[CHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
