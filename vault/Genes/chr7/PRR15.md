---
symbol: "PRR15"
type: "gene"
col: 10727
ensembl_id: "ENSG00000176532"
name: "proline rich 15"
location: "7p14.3"
module: 44
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 22
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 130
direction_downstream: 148
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PRR15

*proline rich 15* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.85× (z +8.9, q 4e-16, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +4.2, q 0.005, up in 1 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.435× (z -5.7, q 6e-06, down in 16 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15L]] (+0.84, fdr 7e-06), [[FXYD3]] (+0.81, fdr 7e-06), [[UGT1A1]] (+0.80, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 130 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 148 go from it, the strongest it → [[TOB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.85×** | +8.9 | 4e-16 | 2/6 (SW1417, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +6.0 | 4e-07 | 2/12 (SW1417, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +4.3 | 0.003 | 2/11 (HEC-1-A, SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.005 | 1/18 (AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.79×** | +4.0 | 0.008 | 8/19 (LS 180, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.015 | 2/19 (KATO III, HEC-1-A) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.6 | 0.029 | 2/12 (HEC-1-A, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +3.5 | 0.030 | 1/9 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.4 | 0.049 | 2/13 (SW480, COLO 205) | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.094 | 5/19 (LS 180, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.435×** | -5.7 | 6e-06 | 16/20 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -5.3 | 3e-05 | 17/20 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.508×** | -4.7 | 6e-04 | 16/20 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -3.5 | 0.061 | 9/20 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.629× | -3.2 | 0.16 | 11/20 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0481× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0777× (z -12.2) |
| [[KATO III (line)]] | alt | 39.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -11.9) |
| [[LoVo (line)]] | wt | 19.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0746× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 2.41 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.0583× (z -9.6) |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0805× (z -9.8) |
| [[Hs 766T (line)]] | wt | 8.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0864× (z -8.8) |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0994× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[Panc 03.27 (line)]] | alt | 6.00 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0638× (z -8.7) |
| [[A-172 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15L]] | +0.84 | +0.82 / +0.80 | both halves | 7e-06 | STRING 580 |
| [[FXYD3]] | +0.81 | +0.80 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[POF1B]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PRR15-DT]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[MUC13]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.77 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A9]] | +0.77 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CLDN3]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[GPX2]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[CFTR]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*130 arrows, 130 of them with an alert ⚠; grade A 0, B 7, C 123. Shown: the 12 strongest; 118 more arrows (118 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises PRR15's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without PLAAT4 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[PLEKHS1]] | B | PLEKHS1 activity raises PRR15's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without PLEKHS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[FAM3B]] | B | FAM3B activity raises PRR15's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without FAM3B | 0.050 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises PRR15's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.18× lower at baseline in the lines without ATP8B1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[PLA2R1]] | B | PLA2R1 activity raises PRR15's level | lines that do not express PLA2R1 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without PLA2R1 | 0.052 | ⚠ within organs, on part of the lines; also absent: CYP2S1, RARRES1, IL18 |
| [[MANSC1]] | B | MANSC1 activity raises PRR15's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without MANSC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[GNA14]] | B | GNA14 activity raises PRR15's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without GNA14 | 0.069 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[PHGR1]] | C | PHGR1 activity raises PRR15's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 5.82× lower at baseline in the lines without PHGR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[PRR15-DT]] | C | PRR15-DT activity raises PRR15's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 4.05× lower at baseline in the lines without PRR15-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises PRR15's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.91× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[CYP4F12]] | C | CYP4F12 activity raises PRR15's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.85× lower at baseline in the lines without CYP4F12 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises PRR15's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 5.53× lower at baseline in the lines without PLA2G2A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |

### Downstream of this gene

*148 arrows, 148 of them with an alert ⚠; grade A 0, B 36, C 112. Shown: the 12 strongest; 136 more arrows (136 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOB1]] | B | PRR15 activity raises TOB1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without PRR15 | 0.003 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[TST]] | B | PRR15 activity raises TST's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without PRR15 | 0.006 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[TNFRSF21]] | B | PRR15 activity raises TNFRSF21's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 3.78× lower at baseline in the lines without PRR15 | 0.007 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[IL22RA1]] | B | PRR15 activity raises IL22RA1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without PRR15 | 0.007 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[MGST2]] | B | PRR15 activity raises MGST2's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.79× lower at baseline in the lines without PRR15 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[MAP3K8]] | B | PRR15 activity raises MAP3K8's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without PRR15 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[MANSC1]] | B | PRR15 activity raises MANSC1's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without PRR15 | 0.013 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[C4orf19]] | B | PRR15 activity raises C4orf19's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without PRR15 | 0.014 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[SLC12A2]] | B | PRR15 activity raises SLC12A2's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without PRR15 | 0.017 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[ABHD11]] | B | PRR15 activity raises ABHD11's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without PRR15 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[FUT2]] | B | PRR15 activity raises FUT2's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without PRR15 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[ZNF703]] | B | PRR15 activity raises ZNF703's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without PRR15 | 0.021 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.863). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.4, 51.9); signed map (62.6, 4.7). **Vector** length 64.3, 21.5% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.60 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.60 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +8.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -5.7 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:29,563,835-29,567,293 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV56](https://www.uniprot.org/uniprotkb/Q8IV56) (Proline-rich protein 15):

> May have a role in proliferation and/or differentiation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:22310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22310) · Entrez [222171](https://www.ncbi.nlm.nih.gov/gene/222171) · UniProt [Q8IV56](https://www.uniprot.org/uniprotkb/Q8IV56) · Ensembl [ENSG00000176532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176532)

## Data

Gene col 10727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10727); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10727]; `tensor/DDL_lfc|DDL_z.npy` [10727]; `embed/gene_vectors.npy` [10727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10727 or target_col == 10727). Every well: [[PRR15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
