---
symbol: "NLGN4Y"
type: "gene"
col: 9094
ensembl_id: "ENSG00000165246"
name: "neuroligin 4 Y-linked"
location: "Yq11.221"
module: 19
arm: "+"
pooled_cpm: 17.44
n_lines_expressing: 13
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 28
direction_downstream: 36
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NLGN4Y

*neuroligin 4 Y-linked* — Yq11.221

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +11.2, q 2e-26, up in 10 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.588× (z -4.9, q 7e-04, down in 9 of 11 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC9]] (+0.69, fdr 7e-06), [[ZEB2]] (+0.68, fdr 7e-06), [[ZFY]] (+0.67, fdr 7e-06); moves opposite to [[CASP9]] (-0.51, fdr 4e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 36 go from it, the strongest it → [[TBX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +11.2 | 2e-26 | 10/11 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.6 | 3e-19 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +9.5 | 4e-19 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +7.6 | 5e-12 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +6.7 | 2e-09 | 11/11 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 4/11 (SNU-1, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.008 | 1/11 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.011 | 2/11 (hTERT-HPNE, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.021 | 1/11 (A-172) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.094 | 3/11 (A549, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.10 | 1/11 (SNU-1) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.58× | +3.0 | 0.12 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -4.9 | 7e-04 | 9/11 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.618×** | -4.4 | 0.003 | 9/11 (A-172, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -4.0 | 0.010 | 7/11 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.648×** | -4.0 | 0.010 | 10/11 (A-172, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Pimozide (drug)]] 5 µM |  | **0.689×** | -3.4 | 0.076 | 1/11 (SW 1088) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.699× | -3.2 | 0.12 | 0/11 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.694× | -3.2 | 0.12 | 0/11 | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.711× | -3.1 | 0.12 | 0/11 | inconsistent across doses |  |
| [[MK-8353 (drug)]] 0.5 µM |  | 0.622× | -3.1 | 0.12 | 0/11 | inconsistent across doses | noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.695× | -3.1 | 0.12 | 1/11 (SW 1088) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.700× | -3.0 | 0.14 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 192 | 5 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.0462× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0853× (z -17.4) |
| [[J82 (line)]] | alt | 73.4 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +19.2) | [[Belinostat (drug)]] 5 µM 0.206× (z -10.4) |
| [[SNU-1 (line)]] | wt | 102 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.0460× (z -17.7) |
| [[hTERT-HPNE (line)]] | wt | 56.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.9 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.117× (z -12.2) |
| [[A549 (line)]] | wt | 16.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.148× (z -9.3) |
| [[CHP-212 (line)]] | wt | 66.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0679× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 38.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.125× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +12.9) | — |
| [[A-427 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC9]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[ZEB2]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ZFY]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 | STRING 945 |
| [[UTY]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 | STRING 894 |
| [[GASK1B-AS1]] | +0.62 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[RBMS3]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.61 | +0.65 / +0.40 | both halves | 5e-05 | pathway: Neuronal System |
| [[SHISAL1]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CPED1]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CDH11]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP9]] | -0.51 | -0.53 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 4, C 24. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NLGN4Y's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises NLGN4Y's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without TENM3-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises NLGN4Y's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers NLGN4Y's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[UTY]] | C | UTY activity raises NLGN4Y's level | lines that do not express UTY (31) vs lines expressing it (19) | 6.62× lower at baseline in the lines without UTY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises NLGN4Y's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.68× lower at baseline in the lines without ALPK2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises NLGN4Y's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 8.60× lower at baseline in the lines without GREM2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises NLGN4Y's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 6.41× lower at baseline in the lines without TTTY10 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[USP9Y]] | C | USP9Y activity raises NLGN4Y's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 7.17× lower at baseline in the lines without USP9Y | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises NLGN4Y's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 4.02× lower at baseline in the lines without PDE1A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises NLGN4Y's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 6.08× lower at baseline in the lines without MARCOL, SPINK13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[ZFY]] | C | ZFY activity raises NLGN4Y's level | lines that do not express ZFY (29) vs lines expressing it (21) | 6.51× lower at baseline in the lines without ZFY | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 3, C 33. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX2]] | B | NLGN4Y activity raises TBX2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 2.39× lower at baseline in the lines without NLGN4Y | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9 |
| [[BMPER]] | B | NLGN4Y activity raises BMPER's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without NLGN4Y | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9 |
| [[FSTL4]] | B | NLGN4Y activity raises FSTL4's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.60× lower at baseline in the lines without NLGN4Y | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9 |
| [[ALPK2]] | C | NLGN4Y activity raises ALPK2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 5.80× lower at baseline in the lines without NLGN4Y | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[UTY]] | C | NLGN4Y activity raises UTY's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 12.02× lower at baseline in the lines without NLGN4Y | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[TTTY10]] | C | NLGN4Y activity raises TTTY10's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 4.32× lower at baseline in the lines without NLGN4Y | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[GREM2]] | C | NLGN4Y activity raises GREM2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 4.08× lower at baseline in the lines without NLGN4Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[USP9Y]] | C | NLGN4Y activity raises USP9Y's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 16.75× lower at baseline in the lines without NLGN4Y | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[DGKI]] | C | NLGN4Y activity raises DGKI's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without NLGN4Y | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[ABI3BP]] | C | NLGN4Y activity raises ABI3BP's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 4.42× lower at baseline in the lines without NLGN4Y | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[EDA2R]] | C | NLGN4Y activity raises EDA2R's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.28× lower at baseline in the lines without NLGN4Y | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[SPINK13]] | C | NLGN4Y activity raises SPINK13's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.45× lower at baseline in the lines without NLGN4Y | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.6, 25.1); signed map (41.8, 26.3). **Vector** length 52.1, 19.6% of its response variance represented; |z| ≥ 3 in 308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | neuroligin 4 Y-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yq11.221 — chrY:14,522,573-14,845,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0951 |
| Gene groups (HGNC) | Neuroligins |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFZ3](https://www.uniprot.org/uniprotkb/Q8NFZ3) (Neuroligin-4, Y-linked):

> Cell surface protein involved in cell-cell-interactions via its interactions with neurexin family members.

**Summary**, from NCBI Gene [22829](https://www.ncbi.nlm.nih.gov/gene/22829):

> This gene encodes a type I membrane protein that belongs to the family of neuroligins, which are cell adhesion molecules present at the postsynaptic side of the synapse, and may be essential for the formation of functional synapses. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:15529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15529) · Entrez [22829](https://www.ncbi.nlm.nih.gov/gene/22829) · UniProt [Q8NFZ3](https://www.uniprot.org/uniprotkb/Q8NFZ3) · Ensembl [ENSG00000165246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165246)

## Data

Gene col 9094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9094); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9094]; `tensor/DDL_lfc|DDL_z.npy` [9094]; `embed/gene_vectors.npy` [9094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9094 or target_col == 9094). Every well: [[NLGN4Y — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLGN4Y.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
