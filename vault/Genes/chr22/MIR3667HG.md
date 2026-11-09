---
symbol: "MIR3667HG"
type: "gene"
col: 12017
ensembl_id: "ENSG00000188511"
name: "MIR3667 host gene"
location: "22q13.33"
module: 27
arm: "+"
pooled_cpm: 33.38
n_lines_expressing: 12
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 30
direction_downstream: 34
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MIR3667HG

*MIR3667 host gene* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.80× (z +19.4, q 0e+00, up in 5 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.618× (z -4.6, q 0.003, down in 0 of 9 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST18]] (+0.66, fdr 7e-06), [[RMST]] (+0.64, fdr 7e-06), [[RIMBP2]] (+0.64, fdr 1e-05); moves opposite to [[CDIPT]] (-0.47, fdr 2e-04), [[KCTD1]] (-0.46, fdr 4e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[NKD2]] → it (grade B ⚠); 34 go from it, the strongest it → [[GRIK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.80×** | +19.4 | 0e+00 | 5/10 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +10.7 | 3e-24 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +9.1 | 2e-17 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.1 | 6e-14 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +7.6 | 5e-12 | 2/9 (SNU-1, HS-578T) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.3 | 3e-11 | 1/9 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +7.0 | 3e-10 | 3/9 (SNU-423, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.8 | 9e-10 | 6/10 (KATO III, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +4.6 | 3e-04 | 9/9 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 5e-04 | 5/9 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.9 | 0.004 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.8 | 0.007 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.007 | 1/9 (SNU-423) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.019 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.025 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.085 | 0/9 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.090 | 0/9 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.618×** | -4.6 | 0.003 | 0/9 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.673×** | -4.0 | 0.015 | 1/10 (SW 1088) | two highest doses |  |
| [[Methotrexate (drug)]] 5 µM |  | **0.699×** | -3.7 | 0.045 | 0/10 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -3.6 | 0.045 | 6/9 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.703× | -3.3 | 0.10 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 116 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.1) |
| [[SW480 (line)]] | alt | 114 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -17.9) |
| [[SNU-1 (line)]] | wt | 308 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -10.4) |
| [[SHP-77 (line)]] | alt | 697 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.6) |
| [[HS-578T (line)]] | alt | 222 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST18]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[RMST]] | +0.64 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[RIMBP2]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[SMOC2]] | +0.63 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[NKD1]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[PROX1]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CSMD3]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[JAKMIP2-AS1]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PROX1-AS1]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[VWA2]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LINC00923]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIPT]] | -0.47 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[KCTD1]] | -0.46 | -0.40 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 2, C 28. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKD2]] | B | NKD2 activity lowers MIR3667HG's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 1.58× higher at baseline in the lines without NKD2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1 |
| [[PCDH9]] | B | PCDH9 activity raises MIR3667HG's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without PCDH9 | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5 |
| [[GTSF1]] | C | GTSF1 activity raises MIR3667HG's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 7.69× lower at baseline in the lines without GTSF1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises MIR3667HG's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without JAKMIP2-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises MIR3667HG's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 5.47× lower at baseline in the lines without RNF17 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[ST18]] | C | ST18 activity raises MIR3667HG's level | lines that do not express ST18 (39) vs lines expressing it (11) | 3.66× lower at baseline in the lines without ST18 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | RIMBP2 activity raises MIR3667HG's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without RIMBP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises MIR3667HG's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 3.07× lower at baseline in the lines without FKBP9P1-1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises MIR3667HG's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without POU3F2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises MIR3667HG's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.31× lower at baseline in the lines without PCSK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises MIR3667HG's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 4.39× lower at baseline in the lines without KCNB2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises MIR3667HG's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.54× lower at baseline in the lines without PSG1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 4, C 30. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK2]] | B | MIR3667HG activity raises GRIK2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without MIR3667HG | 0.036 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA |
| [[FKBP9P1]] | B | MIR3667HG activity raises FKBP9P1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.93× lower at baseline in the lines without MIR3667HG | 0.061 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA |
| [[LINC02254]] | B | MIR3667HG activity raises LINC02254's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.46× lower at baseline in the lines without MIR3667HG | 0.091 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA |
| [[NCALD]] | B | MIR3667HG activity raises NCALD's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.26× lower at baseline in the lines without MIR3667HG | 0.096 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA |
| [[ST18]] | C | MIR3667HG activity raises ST18's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without MIR3667HG | 0.003 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[RMST]] | C | MIR3667HG activity raises RMST's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without MIR3667HG | 0.005 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[ARHGAP25]] | C | MIR3667HG activity raises ARHGAP25's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without MIR3667HG | 0.005 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[RIMBP2]] | C | MIR3667HG activity raises RIMBP2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without MIR3667HG | 0.007 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[LINC01980]] | C | MIR3667HG activity raises LINC01980's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.19× lower at baseline in the lines without MIR3667HG | 0.008 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[CLRN3]] | C | MIR3667HG activity raises CLRN3's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.09× lower at baseline in the lines without MIR3667HG | 0.011 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[JAKMIP2-AS1]] | C | MIR3667HG activity raises JAKMIP2-AS1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without MIR3667HG | 0.013 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[SMOC2]] | C | MIR3667HG activity raises SMOC2's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.98× lower at baseline in the lines without MIR3667HG | 0.013 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 44.0); signed map (63.5, 15.2). **Vector** length 37.8, 14.0% of its response variance represented; |z| ≥ 3 in 196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +19.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -4.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | MIR3667 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.33 — chr22:49,414,524-49,657,542 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C22orf34 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28010) · Entrez [348645](https://www.ncbi.nlm.nih.gov/gene/348645) · Ensembl [ENSG00000188511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188511)

## Data

Gene col 12017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12017); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12017]; `tensor/DDL_lfc|DDL_z.npy` [12017]; `embed/gene_vectors.npy` [12017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12017 or target_col == 12017). Every well: [[MIR3667HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR3667HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
