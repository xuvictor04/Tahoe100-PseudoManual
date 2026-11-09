---
symbol: "MIR548XHG"
type: "gene"
col: 13381
ensembl_id: "ENSG00000224141"
name: "MIR548X host gene"
location: "21q21.1"
module: 108
arm: "+"
pooled_cpm: 15.81
n_lines_expressing: 12
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 22
direction_downstream: 21
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MIR548XHG

*MIR548X host gene* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +10.2, q 8e-22, up in 0 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.458× (z -7.7, q 7e-12, down in 9 of 10 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00383]] (+0.74, fdr 1e-05), [[LINC01687]] (+0.71, fdr 1e-05), [[LINC02267]] (+0.70, fdr 7e-06).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 21 go from it, the strongest it → [[CALCRL-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.2 | 8e-22 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.6 | 2e-19 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.2 | 5e-18 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.8 | 1e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +5.7 | 1e-06 | 3/10 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.5 | 5e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.4 | 5e-06 | 3/10 (A-172, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.5 | 5e-04 | 4/10 (H4, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.004 | 7/10 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.8 | 0.009 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.4 | 0.030 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.056 | 5/10 (A-172, hTERT-HPNE, …) | two highest doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.095 | 0/9 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.095 | 0/10 | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.0 | 0.095 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.095 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.458×** | -7.7 | 7e-12 | 9/10 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.626×** | -4.6 | 0.001 | 10/10 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.645×** | -4.3 | 0.003 | 10/10 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.672×** | -3.9 | 0.012 | 0/10 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.678×** | -3.6 | 0.043 | 0/10 | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.695×** | -3.5 | 0.052 | 0/10 | top dose only | plate-row cell shift |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.712×** | -3.4 | 0.062 | 0/10 | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.2 | 0.090 | 2/10 (H4, NCI-H661) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -3.2 | 0.096 | 2/10 (SK-MEL-2, LOX-IMVI) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.730× | -3.1 | 0.10 | 0/10 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.714× | -3.1 | 0.10 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 268 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0814× (z -18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.105× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 59.5 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -13.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.204× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0711× (z -15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.101× (z -13.8) |
| [[SNU-423 (line)]] | alt | 147 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -9.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0303× (z -12.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00383]] | +0.74 | +0.71 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LINC01687]] | +0.71 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LINC02267]] | +0.70 | +0.59 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ZIC1]] | +0.68 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MIR3171HG]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 | same gene group |
| [[MAGI2]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LINC00879]] | +0.66 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[FAP]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[LINC01905]] | +0.65 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[MAGI2-AS3]] | +0.63 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[KC6]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 2, C 20. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIR548XHG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MIR548XHG's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02616]] | C | LINC02616 activity raises MIR548XHG's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 5.27× lower at baseline in the lines without LINC02616 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[FAM95A]] | C | FAM95A activity raises MIR548XHG's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 5.39× lower at baseline in the lines without FAM95A | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises MIR548XHG's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without GABRA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises MIR548XHG's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 4.40× lower at baseline in the lines without LINC01687 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[COX7B2]] | C | COX7B2 activity raises MIR548XHG's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 7.56× lower at baseline in the lines without COX7B2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[MSC]] | C | MSC activity raises MIR548XHG's level | lines that do not express MSC (34) vs lines expressing it (16) | 4.69× lower at baseline in the lines without MSC | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[LIN28B]] | C | LIN28B activity raises MIR548XHG's level | lines that do not express LIN28B (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without LIN28B | 0.025 | ⚠ within organs, on part of the lines; also absent: LRFN5, BARX1, KCNH7; co-absent with the target |
| [[LINC00383]] | C | LINC00383 activity raises MIR548XHG's level | lines that do not express LINC00383 (39) vs lines expressing it (11) | 4.31× lower at baseline in the lines without LINC00383 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259639, LINC01425, ENSG00000285751; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises MIR548XHG's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 3.91× lower at baseline in the lines without LINC00648 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[MIR3171HG]] | C | MIR3171HG activity raises MIR548XHG's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 4.10× lower at baseline in the lines without MIR3171HG | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 1, C 20. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCRL-AS1]] | B | MIR548XHG activity raises CALCRL-AS1's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 2.27× lower at baseline in the lines without MIR548XHG | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2 |
| [[GABRA3]] | C | MIR548XHG activity raises GABRA3's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 5.13× lower at baseline in the lines without MIR548XHG | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC01446]] | C | MIR548XHG activity raises LINC01446's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 6.62× lower at baseline in the lines without MIR548XHG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC01687]] | C | MIR548XHG activity raises LINC01687's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 5.28× lower at baseline in the lines without MIR548XHG | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC00470]] | C | MIR548XHG activity raises LINC00470's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 5.52× lower at baseline in the lines without MIR548XHG | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[ADGRG7]] | C | MIR548XHG activity raises ADGRG7's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 3.17× lower at baseline in the lines without MIR548XHG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC02616]] | C | MIR548XHG activity raises LINC02616's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 3.95× lower at baseline in the lines without MIR548XHG | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC02476]] | C | MIR548XHG activity raises LINC02476's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 8.74× lower at baseline in the lines without MIR548XHG | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[TPTE]] | C | MIR548XHG activity raises TPTE's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 4.68× lower at baseline in the lines without MIR548XHG | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[LINC02882]] | C | MIR548XHG activity raises LINC02882's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 6.07× lower at baseline in the lines without MIR548XHG | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[GLI3]] | C | MIR548XHG activity raises GLI3's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 3.70× lower at baseline in the lines without MIR548XHG | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |
| [[GABRG2]] | C | MIR548XHG activity raises GABRG2's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without MIR548XHG | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.1, 25.7); signed map (33.8, 41.8). **Vector** length 40.8, 14.9% of its response variance represented; |z| ≥ 3 in 256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +0.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.8 | +1.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.2 | -7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MIR548X host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q21.1 — chr21:18,561,265-18,760,320 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52006) · Entrez [101927797](https://www.ncbi.nlm.nih.gov/gene/101927797) · Ensembl [ENSG00000224141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224141)

## Data

Gene col 13381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13381); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13381]; `tensor/DDL_lfc|DDL_z.npy` [13381]; `embed/gene_vectors.npy` [13381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13381 or target_col == 13381). Every well: [[MIR548XHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR548XHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
