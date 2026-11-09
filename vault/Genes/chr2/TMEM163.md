---
symbol: "TMEM163"
type: "gene"
col: 7594
ensembl_id: "ENSG00000152128"
name: "transmembrane protein 163"
location: "2q21.3"
module: 196
arm: "+"
pooled_cpm: 28.0
n_lines_expressing: 15
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 22
direction_downstream: 21
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# TMEM163

*transmembrane protein 163* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +14.8, q 0e+00, up in 4 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.576× (z -5.4, q 3e-05, down in 3 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VSIG1]] (+0.72, fdr 1e-05), [[IL19]] (+0.65, fdr 1e-05), [[FGF19]] (+0.62, fdr 1e-05).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[MILR1]] → it (grade B ⚠); 21 go from it, the strongest it → [[YWHAEP7-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +14.8 | 0e+00 | 4/13 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +10.3 | 2e-22 | 7/13 (A-172, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +9.5 | 5e-19 | 2/9 (RPMI-7951, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.3 | 1e-14 | 1/11 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.1 | 4e-05 | 7/13 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.5 | 0.037 | 1/11 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.040 | 0/13 | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.040 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.062 | 1/13 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.33× | +3.0 | 0.14 | 3/13 (A-172, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.576×** | -5.4 | 3e-05 | 3/13 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.1 | 9e-05 | 8/12 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.624×** | -5.0 | 1e-04 | 6/13 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.625×** | -4.8 | 2e-04 | 7/13 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.673×** | -4.6 | 5e-04 | 5/13 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.651×** | -4.6 | 5e-04 | 6/13 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.712×** | -4.5 | 5e-04 | 8/13 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.748×** | -4.3 | 0.001 | 3/13 (SW480, BT-474, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.714×** | -4.2 | 0.002 | 4/13 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.772×** | -3.9 | 0.006 | 9/13 (A-172, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -3.8 | 0.007 | 8/13 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.015 | 5/13 (SW480, BT-474, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.028 | 4/13 (SW480, BT-474, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.049 | 8/13 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.049 | 3/13 (SW480, SHP-77, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.076 | 6/13 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 296 | 0 | 20 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -18.3) |
| [[SW1417 (line)]] | alt | 57.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.9) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.1) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -10.7) |
| [[SHP-77 (line)]] | alt | 56.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.1) |
| [[A-427 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -9.5) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A549 (line)]] | wt | 7.36 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0993× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0706× (z -9.0) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSIG1]] | +0.72 | +0.77 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[IL19]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[FGF19]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[FGD5]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ISM1]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[EPHB6]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[PROX1]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SCN5A]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[SPTSSB]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[CEMIP]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[MILR1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 2, C 20. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | MILR1 activity raises TMEM163's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without MILR1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises TMEM163's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[AFF2]] | C | AFF2 activity raises TMEM163's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without AFF2 | 0.004 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[LOXL4]] | C | LOXL4 activity raises TMEM163's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.51× lower at baseline in the lines without LOXL4 | 0.009 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[TRPV4]] | C | TRPV4 activity raises TMEM163's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without TRPV4 | 0.012 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises TMEM163's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.68× lower at baseline in the lines without KRT23 | 0.014 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[SERPINB4]] | C | SERPINB4 activity raises TMEM163's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 3.02× lower at baseline in the lines without SERPINB4 | 0.016 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises TMEM163's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.43× lower at baseline in the lines without PCSK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises TMEM163's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.26× lower at baseline in the lines without FKBP9P1-1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[SLC16A6]] | C | SLC16A6 activity raises TMEM163's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 2.17× lower at baseline in the lines without SLC16A6 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |
| [[SERPINB3]] | C | SERPINB3 activity raises TMEM163's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.78× lower at baseline in the lines without SERPINB3 | 0.035 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises TMEM163's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without SHROOM4 | 0.042 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 7, C 14. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YWHAEP7-1]] | B | TMEM163 activity raises YWHAEP7-1's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.65× lower at baseline in the lines without TMEM163 | 0.030 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[TESC]] | B | TMEM163 activity raises TESC's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without TMEM163 | 0.048 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[IQSEC1]] | B | TMEM163 activity raises IQSEC1's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without TMEM163 | 0.051 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[LINC03042]] | B | TMEM163 activity raises LINC03042's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.47× lower at baseline in the lines without TMEM163 | 0.051 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[ARSG]] | B | TMEM163 activity raises ARSG's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without TMEM163 | 0.053 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[IL19]] | B | TMEM163 activity raises IL19's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.66× lower at baseline in the lines without TMEM163 | 0.054 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[CLDN10]] | B | TMEM163 activity raises CLDN10's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.97× lower at baseline in the lines without TMEM163 | 0.084 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[KRT23]] | C | TMEM163 activity raises KRT23's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.10× lower at baseline in the lines without TMEM163 | 0.011 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[RIMBP2]] | C | TMEM163 activity raises RIMBP2's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.31× lower at baseline in the lines without TMEM163 | 0.019 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[APCDD1]] | C | TMEM163 activity raises APCDD1's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.09× lower at baseline in the lines without TMEM163 | 0.020 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[SCN5A]] | C | TMEM163 activity raises SCN5A's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.36× lower at baseline in the lines without TMEM163 | 0.021 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[SERPINB3]] | C | TMEM163 activity raises SERPINB3's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without TMEM163 | 0.031 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.7, 42.9); signed map (10.7, 53.3). **Vector** length 60.4, 22.2% of its response variance represented; |z| ≥ 3 in 421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -5.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 163 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:134,455,759-134,719,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566N034, SV31, SLC30A11 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC26](https://www.uniprot.org/uniprotkb/Q8TC26) (Transmembrane protein 163):

> Zinc ion transporter that mediates zinc efflux and plays a crucial role in intracellular zinc homeostasis. Binds the divalent cations Zn(2+), Ni(2+), and to a minor extent Cu(2+) (By similarity). Is a functional modulator of P2X purinoceptors, including P2RX1, P2RX3, P2RX4 and P2RX7. Plays a role in central nervous system development and is required for myelination, and survival and proliferation of oligodendrocytes.

**Summary**, from NCBI Gene [81615](https://www.ncbi.nlm.nih.gov/gene/81615):

> Predicted to enable zinc ion binding activity. Involved in intracellular zinc ion homeostasis; myelination; and zinc export across plasma membrane. Is active in late endosome; lysosome; and plasma membrane. Implicated in hypomyelinating leukodystrophy 25. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25380) · Entrez [81615](https://www.ncbi.nlm.nih.gov/gene/81615) · UniProt [Q8TC26](https://www.uniprot.org/uniprotkb/Q8TC26) · Ensembl [ENSG00000152128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152128)

## Data

Gene col 7594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7594); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7594]; `tensor/DDL_lfc|DDL_z.npy` [7594]; `embed/gene_vectors.npy` [7594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7594 or target_col == 7594). Every well: [[TMEM163 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM163.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
