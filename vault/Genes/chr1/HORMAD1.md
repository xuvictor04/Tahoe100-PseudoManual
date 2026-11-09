---
symbol: "HORMAD1"
type: "gene"
col: 6747
ensembl_id: "ENSG00000143452"
name: "HORMA domain containing 1"
location: "1q21.3"
module: 19
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 25
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# HORMAD1

*HORMA domain containing 1* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +11.0, q 2e-25, up in 7 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A549 0.166×, NCI-H1573 0.186×, NCI-H460 0.310×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.168×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.190×; ⚠ cell-cycle shift, explains ~76% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB4]] (+0.69, fdr 1e-05), [[LGSN]] (+0.66, fdr 1e-05), [[TARID]] (+0.63, fdr 1e-05); moves opposite to [[SPNS2]] (-0.48, fdr 7e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[SLC16A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +11.0 | 2e-25 | 7/13 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.62×** | +10.4 | 7e-23 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.68×** | +10.3 | 2e-22 | 2/7 (NCI-H1573, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.51×** | +9.2 | 8e-18 | 1/5 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.8 | 1e-09 | 9/19 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +6.0 | 2e-07 | 2/8 (A498, A549) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +5.7 | 1e-06 | 0/15 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +4.7 | 2e-04 | 1/14 (A549) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.6 | 3e-04 | 1/7 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +4.5 | 4e-04 | 4/19 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.70×** | +4.2 | 0.001 | 8/16 (A-427, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.2 | 0.001 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.004 | 3/18 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.007 | 0/14 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.007 | 4/10 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.045 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.060 | 2/13 (A-427, NCI-H2030) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A549 0.166×, NCI-H1573 0.186×, NCI-H460 0.310×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.168×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.190×; ⚠ cell-cycle shift, explains ~76% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.609× | -3.6 | 0.15 | 3/19 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.661× | -3.3 | 0.21 | 9/19 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.665× | -3.3 | 0.21 | 8/16 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~23% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -12.5) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -9.3) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A549 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.8) |
| [[A-172 (line)]] | wt | 0.951 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.432 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB4]] | +0.69 | +0.65 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[LGSN]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[TARID]] | +0.63 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RHOH]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[COL4A5]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[BASP1-AS1]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[EPGN]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SPDYE10]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[LINC02864]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CACNG6]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PDE1A]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[P3H2-AS1]] | +0.58 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPNS2]] | -0.48 | -0.50 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HORMAD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NCKAP5]] | B | NCKAP5 activity raises HORMAD1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without NCKAP5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[CSGALNACT1]] | B | CSGALNACT1 activity raises HORMAD1's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 1.87× lower at baseline in the lines without CSGALNACT1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[CPS1]] | B | CPS1 activity raises HORMAD1's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without CPS1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R |
| [[COL4A3]] | C | COL4A3 activity raises HORMAD1's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without COL4A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises HORMAD1's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.64× lower at baseline in the lines without GPR141 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[CDH19]] | C | CDH19 activity raises HORMAD1's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 2.94× lower at baseline in the lines without CDH19 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[LINC00278]] | C | LINC00278 activity raises HORMAD1's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.55× lower at baseline in the lines without LINC00278 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1; co-absent with the target |
| [[LRRK2]] | C | LRRK2 activity raises HORMAD1's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 1.91× lower at baseline in the lines without LRRK2 | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[TARID]] | C | TARID activity raises HORMAD1's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without TARID | 0.084 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | HORMAD1 activity raises SLC16A4's level | lines that do not express HORMAD1 (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without HORMAD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent |
| [[SLC16A4]] | B | HORMAD1 activity weakens SLC16A4's drug response | lines that do not express HORMAD1 (15) vs lines expressing it (18) | the lines without HORMAD1 respond 1.55× as strongly (z diff -0.61); strongest at Ouabain (Octahydrate) 5 µM: 2.13x vs 0.77x (z diff -4.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[RSPO3]] | C | HORMAD1 activity raises RSPO3's level | lines that do not express HORMAD1 (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without HORMAD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent; co-absent with the target |
| [[TARID]] | C | HORMAD1 activity raises TARID's level | lines that do not express HORMAD1 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without HORMAD1 | 0.053 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent; co-absent with the target |
| [[LINC02057]] | C | HORMAD1 activity raises LINC02057's level | lines that do not express HORMAD1 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without HORMAD1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LRRC63, CRLF2, ENTHD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, 37.6); signed map (39.9, 42.1). **Vector** length 35.2, 7.29% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -1.3 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.1 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | HORMA domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,698,060-150,720,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434A1315, CT46 |
| Gene groups (HGNC) | HORMA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X24](https://www.uniprot.org/uniprotkb/Q86X24) (HORMA domain-containing protein 1):

> Plays a key role in meiotic progression. Regulates 3 different functions during meiosis: ensures that sufficient numbers of processed DNA double-strand breaks (DSBs) are available for successful homology search by increasing the steady-state numbers of single-stranded DSB ends. Promotes synaptonemal-complex formation independently of its role in homology search. Plays a key role in the male mid-pachytene checkpoint and the female meiotic prophase checkpoint: required for efficient build-up of …

**Summary**, from NCBI Gene [84072](https://www.ncbi.nlm.nih.gov/gene/84072):

> This gene encodes a HORMA domain-containing protein. HORMA domains are involved in chromatin binding and play a role in cell cycle regulation. The encoded protein may play a role in meiosis, and expression of this gene is a potential marker for cancer. A pseudogene of this gene is located on the long arm of chromosome 6. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:25245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25245) · Entrez [84072](https://www.ncbi.nlm.nih.gov/gene/84072) · UniProt [Q86X24](https://www.uniprot.org/uniprotkb/Q86X24) · Ensembl [ENSG00000143452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143452)

## Data

Gene col 6747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6747); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6747]; `tensor/DDL_lfc|DDL_z.npy` [6747]; `embed/gene_vectors.npy` [6747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6747 or target_col == 6747). Every well: [[HORMAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HORMAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
