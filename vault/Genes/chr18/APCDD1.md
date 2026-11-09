---
symbol: "APCDD1"
type: "gene"
col: 7847
ensembl_id: "ENSG00000154856"
name: "APC down-regulated 1"
location: "18p11.22"
module: 27
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 10
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 25
direction_downstream: 31
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# APCDD1

*APC down-regulated 1* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.96× (z +8.6, q 3e-15, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 2.20× (z +4.7, q 4e-04, up in 0 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.550× (z -3.8, q 0.088, down in 4 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.120×, SW1417 0.147×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.124×, SW1417 0.247×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW1417 0.0620×, SW480 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.0780×, SW1417 0.136×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.0903×, SW1417 0.102×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA2]] (+0.87, fdr 7e-06), [[JAKMIP2-AS1]] (+0.87, fdr 7e-06), [[FGF20]] (+0.81, fdr 7e-06); moves opposite to [[PASD1]] (-0.52, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[LINC02466]] → it (grade B ⚠); 31 go from it, the strongest it → [[HUNK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +8.6 | 3e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.74×** | +8.0 | 5e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +5.6 | 4e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.20×** | +4.7 | 4e-04 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +3.3 | 0.097 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.097 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.66× | +3.2 | 0.11 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.36× | +3.1 | 0.13 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7847.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.120×, SW1417 0.147×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.124×, SW1417 0.247×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW1417 0.0620×, SW480 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.0780×, SW1417 0.136×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.0903×, SW1417 0.102×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.550×** | -3.8 | 0.088 | 4/8 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.561× | -3.5 | 0.11 | 6/8 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.584× | -3.4 | 0.11 | 4/8 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.594× | -3.3 | 0.11 | 8/8 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.600× | -3.2 | 0.11 | 6/7 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.575× | -3.2 | 0.11 | 1/8 (SK-MEL-2) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.707× | -3.1 | 0.15 | 4/8 (SW480, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 72.7 | 0 | 23 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0406× (z -17.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -16.6) |
| [[SW1417 (line)]] | alt | 85.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0620× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -11.9) |
| [[LS 180 (line)]] | wt | 6.60 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0403× (z -9.3) |
| [[A-172 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.865 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.876 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA2]] | +0.87 | +0.83 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.87 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[FGF20]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ST18]] | +0.81 | +0.72 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[NKD1]] | +0.80 | +0.71 / +0.84 | both halves | 7e-06 | STRING 612 |
| [[SLC30A10]] | +0.77 | +0.76 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[B3GAT1-DT]] | +0.77 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PROX1-AS1]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IGFL4]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[F10]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[LINC01622]] | +0.75 | +0.78 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASD1]] | -0.52 | -0.50 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 1, C 24. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02466]] | B | LINC02466 activity raises APCDD1's level | lines that do not express LINC02466 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without LINC02466 | 0.089 | ⚠ within organs, on part of the lines; also absent: MME, ENSG00000227088, GABRA3; maybe low, not absent |
| [[PTPRZ1]] | C | PTPRZ1 activity raises APCDD1's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 3.28× lower at baseline in the lines without PTPRZ1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises APCDD1's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.81× lower at baseline in the lines without PCSK1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises APCDD1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without CSMD3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises APCDD1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.18× lower at baseline in the lines without JAKMIP2-AS1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[CPLX2]] | C | CPLX2 activity raises APCDD1's level | lines that do not express CPLX2 (41) vs lines expressing it (9) | 3.01× lower at baseline in the lines without CPLX2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, TBXT, F5; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises APCDD1's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.09× lower at baseline in the lines without TMEM163 | 0.020 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises APCDD1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.94× lower at baseline in the lines without KRT23 | 0.031 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises APCDD1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.94× lower at baseline in the lines without GJB1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises APCDD1's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.92× lower at baseline in the lines without PSG1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[KLK7]] | C | KLK7 activity raises APCDD1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without KLK7 | 0.042 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises APCDD1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 4.13× lower at baseline in the lines without KRT5 | 0.044 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 6, C 25. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HUNK]] | B | APCDD1 activity raises HUNK's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 3.61× lower at baseline in the lines without APCDD1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[CHDH]] | B | APCDD1 activity raises CHDH's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.66× lower at baseline in the lines without APCDD1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[PDK4-AS1]] | B | APCDD1 activity raises PDK4-AS1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.00× lower at baseline in the lines without APCDD1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[GPR143]] | B | APCDD1 activity raises GPR143's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.24× lower at baseline in the lines without APCDD1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[NMNAT3]] | B | APCDD1 activity raises NMNAT3's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.98× lower at baseline in the lines without APCDD1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[ZNRF3]] | B | APCDD1 activity raises ZNRF3's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without APCDD1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[TMEM139]] | C | APCDD1 activity raises TMEM139's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.24× lower at baseline in the lines without APCDD1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[NKD1]] | C | APCDD1 activity raises NKD1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 5.12× lower at baseline in the lines without APCDD1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[TRPV4]] | C | APCDD1 activity raises TRPV4's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.47× lower at baseline in the lines without APCDD1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[AZGP1]] | C | APCDD1 activity raises AZGP1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 4.20× lower at baseline in the lines without APCDD1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[AXIN2]] | C | APCDD1 activity raises AXIN2's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 4.66× lower at baseline in the lines without APCDD1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[GJB1]] | C | APCDD1 activity raises GJB1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.60× lower at baseline in the lines without APCDD1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, 43.6); signed map (62.8, 15.7). **Vector** length 43.7, 21.2% of its response variance represented; |z| ≥ 3 in 215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | -0.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | APC down-regulated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:10,454,635-10,489,949 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B7323 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8J025](https://www.uniprot.org/uniprotkb/Q8J025) (Protein APCDD1):

> Negative regulator of the Wnt signaling pathway. Inhibits Wnt signaling in a cell-autonomous manner and functions upstream of beta-catenin. May act via its interaction with Wnt and LRP proteins. May play a role in colorectal tumorigenesis.

**Summary**, from NCBI Gene [147495](https://www.ncbi.nlm.nih.gov/gene/147495):

> This locus encodes an inhibitor of the Wnt signaling pathway. Mutations at this locus have been associated with hereditary hypotrichosis simplex. Increased expression of this gene may also be associated with colorectal carcinogenesis.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:15718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15718) · Entrez [147495](https://www.ncbi.nlm.nih.gov/gene/147495) · UniProt [Q8J025](https://www.uniprot.org/uniprotkb/Q8J025) · Ensembl [ENSG00000154856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154856)

## Data

Gene col 7847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7847); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7847]; `tensor/DDL_lfc|DDL_z.npy` [7847]; `embed/gene_vectors.npy` [7847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7847 or target_col == 7847). Every well: [[APCDD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APCDD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
