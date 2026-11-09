---
symbol: "MIR1915HG"
type: "gene"
col: 12913
ensembl_id: "ENSG00000204682"
name: "MIR1915 host gene"
location: "10p12.31"
module: 10
arm: "+"
pooled_cpm: 3.48
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 14
direction_downstream: 36
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MIR1915HG

*MIR1915 host gene* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +11.7, q 7e-29, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.493× (z -6.2, q 3e-07, down in 20 of 30 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02026]] (+0.71, fdr 4e-05), [[PPEF1]] (+0.67, fdr 3e-05), [[FTCDNL1]] (+0.66, fdr 1e-05); moves opposite to [[TSC2]] (-0.54, fdr 6e-05), [[ZCCHC17]] (-0.54, fdr 4e-05), [[LCMT1]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LINC02643]] → it (grade B ⚠); 36 go from it, the strongest it → [[FTCDNL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +11.7 | 7e-29 | 14/23 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.23×** | +9.9 | 1e-20 | 2/4 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +7.7 | 3e-12 | 9/15 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +7.4 | 3e-11 | 3/6 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.9 | 5e-07 | 7/32 (A498, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.76×** | +5.0 | 6e-05 | 11/33 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.8 | 1e-04 | 4/18 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.5 | 6e-04 | 6/32 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +3.9 | 0.005 | 5/31 (LoVo, SW480, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.012 | 4/31 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.5 | 0.022 | 3/13 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.045 | 2/29 (C-33 A, SW1417) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.089 | 2/28 (J82, HEC-1-A) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -6.2 | 3e-07 | 20/30 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -5.4 | 2e-05 | 15/26 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.561×** | -5.1 | 8e-05 | 15/33 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -4.8 | 2e-04 | 17/23 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.587×** | -4.7 | 3e-04 | 14/33 (RKO, A-172, …) | inconsistent across doses |  |
| [[Indacaterol (maleate) (drug)]] 0.05 µM |  | **0.635×** | -4.0 | 0.006 | 9/32 (HepG2/C3A, CHP-212, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -4.0 | 0.006 | 11/29 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.649×** | -3.7 | 0.018 | 14/24 (MIA PaCa-2, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -3.5 | 0.034 | 11/28 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.686×** | -3.3 | 0.046 | 17/33 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.687×** | -3.3 | 0.046 | 11/33 (HOP62, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.591×** | -3.3 | 0.046 | 4/33 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.691×** | -3.2 | 0.051 | 3/31 (SW480, SW48, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -3.2 | 0.052 | 14/28 (PANC-1, SW480, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.687×** | -3.2 | 0.057 | 2/33 (AN3 CA, NCI-H2030) | top dose only | plate-row cell shift |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.080 | 8/31 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 43.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 3.84 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0541× (z -11.5) |
| [[A549 (line)]] | wt | 4.92 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0325× (z -11.8) |
| [[A-172 (line)]] | wt | 4.12 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0379× (z -10.9) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 4.27 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0659× (z -9.8) |
| [[SW480 (line)]] | alt | 3.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -9.2) |
| [[A498 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02026]] | +0.71 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[PPEF1]] | +0.67 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[FTCDNL1]] | +0.66 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[DENND5B-AS1]] | +0.66 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[LINC00466]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[C1QTNF6]] | +0.65 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[LINC01569]] | +0.64 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[FRG1-DT]] | +0.64 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[HHAT]] | +0.61 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CLDN16]] | +0.60 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[CYP1B1-AS1]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PRKG1-AS1]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC2]] | -0.54 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ZCCHC17]] | -0.54 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[LCMT1]] | -0.53 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[ORC3]] | -0.52 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[RARS2]] | -0.50 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[KANSL3]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[DHDDS]] | -0.49 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[HEATR5B]] | -0.49 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[PLD3]] | -0.49 | -0.49 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02643]] | B | LINC02643 activity raises MIR1915HG's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 3.17× lower at baseline in the lines without LINC02643 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530 |
| [[ELFN1]] | B | ELFN1 activity raises MIR1915HG's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without ELFN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[SSPOP]] | B | SSPOP activity raises MIR1915HG's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without SSPOP | 0.042 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises MIR1915HG's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without SYT9-AS1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MIR1915HG's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RFPL1S]] | B | RFPL1S activity raises MIR1915HG's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without RFPL1S | 0.059 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[JPH3]] | B | JPH3 activity raises MIR1915HG's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without JPH3 | 0.060 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[FTCDNL1]] | B | FTCDNL1 activity raises MIR1915HG's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without FTCDNL1 | 0.062 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises MIR1915HG's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without ABCA17P | 0.063 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises MIR1915HG's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 1.48× lower at baseline in the lines without DPY19L2P2-1 | 0.066 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[LINC00173]] | B | LINC00173 activity raises MIR1915HG's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without LINC00173 | 0.066 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[FAXC]] | B | FAXC activity raises MIR1915HG's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without FAXC | 0.072 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 35, C 1. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FTCDNL1]] | B | MIR1915HG activity raises FTCDNL1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without MIR1915HG | 0.001 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[SPTY2D1OS]] | B | MIR1915HG activity raises SPTY2D1OS's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without MIR1915HG | 0.002 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[CACHD1]] | B | MIR1915HG activity raises CACHD1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without MIR1915HG | 0.003 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[TMEM9B-AS1]] | B | MIR1915HG activity raises TMEM9B-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without MIR1915HG | 0.005 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[SYT9-AS1]] | B | MIR1915HG activity raises SYT9-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without MIR1915HG | 0.006 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[ATP6V1E2]] | B | MIR1915HG activity raises ATP6V1E2's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without MIR1915HG | 0.008 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[TMCC1-DT]] | B | MIR1915HG activity raises TMCC1-DT's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without MIR1915HG | 0.011 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[F8]] | B | MIR1915HG activity raises F8's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without MIR1915HG | 0.012 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[PJVK]] | B | MIR1915HG activity raises PJVK's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without MIR1915HG | 0.012 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[TMEM147-AS1]] | B | MIR1915HG activity raises TMEM147-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without MIR1915HG | 0.014 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[DENND5B-AS1]] | B | MIR1915HG activity raises DENND5B-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without MIR1915HG | 0.024 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[CHST14]] | B | MIR1915HG activity raises CHST14's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without MIR1915HG | 0.027 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.5, 29.2); signed map (35.3, -9.9). **Vector** length 49.0, 7.96% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.8 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | MIR1915 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p12.31 — chr10:21,490,272-21,497,260 (-) |
| Ensembl biotype | lncRNA |
| Also known as | bA418C1.3; previously C10orf114, CASC10 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

UniProt [Q5T4H9](https://www.uniprot.org/uniprotkb/Q5T4H9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31448) · Entrez [399726](https://www.ncbi.nlm.nih.gov/gene/399726) · UniProt [Q5T4H9](https://www.uniprot.org/uniprotkb/Q5T4H9) · Ensembl [ENSG00000204682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204682)

## Data

Gene col 12913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12913); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12913]; `tensor/DDL_lfc|DDL_z.npy` [12913]; `embed/gene_vectors.npy` [12913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12913 or target_col == 12913). Every well: [[MIR1915HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR1915HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
