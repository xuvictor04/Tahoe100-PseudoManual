---
symbol: "ADGRG5"
type: "gene"
col: 8265
ensembl_id: "ENSG00000159618"
name: "adhesion G protein-coupled receptor G5"
location: "16q21"
module: 55
arm: "+"
pooled_cpm: 2.99
n_lines_expressing: 15
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 21
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# ADGRG5

*adhesion G protein-coupled receptor G5* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.41× (z +12.1, q 8e-31, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.35× (z +11.5, q 3e-28, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.530× (z -4.3, q 0.008, down in 7 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SW480 0.0942×, LoVo 0.125×, COLO 205 0.0536×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.0623×, LoVo 0.103×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.176×, LoVo 0.171×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.161×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA2]] (+0.80, fdr 7e-06), [[LINC01819]] (+0.76, fdr 7e-06), [[SKAP1]] (+0.76, fdr 7e-06); moves opposite to [[HOXA9]] (-0.50, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[PSG1]] → it (grade C ⚠); 21 go from it, the strongest it → [[TNFRSF14-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.41×** | +12.1 | 8e-31 | 3/4 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.35×** | +11.5 | 3e-28 | 0/9 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +9.5 | 2e-19 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +8.1 | 7e-14 | 1/10 (HCT15) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +5.5 | 4e-06 | 3/10 (SW480, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +5.5 | 4e-06 | 1/4 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +5.4 | 5e-06 | 1/9 (Panc 03.27) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +5.0 | 5e-05 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +4.4 | 6e-04 | 6/10 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.4 | 7e-04 | 1/10 (HT-29) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.7 | 0.009 | 0/9 | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.009 | 0/10 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.13×** | +3.6 | 0.012 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.051 | 0/10 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.1 | 0.062 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.61×** | +3.1 | 0.066 | 1/9 (RKO) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8265.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SW480 0.0942×, LoVo 0.125×, COLO 205 0.0536×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.0623×, LoVo 0.103×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 0.176×, LoVo 0.171×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.161×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -4.3 | 0.008 | 7/10 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.722× | -3.1 | 0.46 | 1/10 (LS 180) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.8 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0623× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -16.0) |
| [[LoVo (line)]] | wt | 16.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -11.3) |
| [[COLO 205 (line)]] | alt | 6.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0536× (z -8.7) |
| [[RKO (line)]] | wt | 8.17 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0420× (z -11.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.710 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA2]] | +0.80 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[SKAP1]] | +0.76 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.71 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[EDAR]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PROX1-AS1]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FGF19]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.67 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[SLC52A3]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[BMP4]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[KCNH8]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA9]] | -0.50 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSG1]] | C | PSG1 activity raises ADGRG5's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.21× lower at baseline in the lines without PSG1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[FGF19]] | C | FGF19 activity raises ADGRG5's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.99× lower at baseline in the lines without FGF19 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises ADGRG5's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without HSD17B2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[SHISA9]] | C | SHISA9 activity raises ADGRG5's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.22× lower at baseline in the lines without SHISA9 | 0.021 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises ADGRG5's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without TMEM139 | 0.024 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[PIK3AP1]] | C | PIK3AP1 activity raises ADGRG5's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without PIK3AP1 | 0.024 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises ADGRG5's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without TNFRSF14-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises ADGRG5's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without SLC5A1 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |
| [[FAM83F]] | C | FAM83F activity raises ADGRG5's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 2.52× lower at baseline in the lines without FAM83F | 0.040 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises ADGRG5's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without LINC03040 | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[LINC02058]] | C | LINC02058 activity raises ADGRG5's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without LINC02058 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; co-absent with the target |
| [[LEMD1]] | C | LEMD1 activity raises ADGRG5's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.85× lower at baseline in the lines without LEMD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | C | ADGRG5 activity raises TNFRSF14-AS1's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 2.55× lower at baseline in the lines without ADGRG5 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[FAM83F]] | C | ADGRG5 activity raises FAM83F's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 4.65× lower at baseline in the lines without ADGRG5 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[LINC01559]] | C | ADGRG5 activity raises LINC01559's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without ADGRG5 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[INPP5D]] | C | ADGRG5 activity raises INPP5D's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 3.15× lower at baseline in the lines without ADGRG5 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[LCK]] | C | ADGRG5 activity raises LCK's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 2.13× lower at baseline in the lines without ADGRG5 | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | ADGRG5 activity raises GPX2's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 3.03× lower at baseline in the lines without ADGRG5 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[EPS8L3]] | C | ADGRG5 activity raises EPS8L3's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 4.38× lower at baseline in the lines without ADGRG5 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[IL20RA]] | C | ADGRG5 activity raises IL20RA's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 4.33× lower at baseline in the lines without ADGRG5 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[GJB1]] | C | ADGRG5 activity raises GJB1's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 1.62× lower at baseline in the lines without ADGRG5 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[B3GNT3]] | C | ADGRG5 activity raises B3GNT3's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 4.31× lower at baseline in the lines without ADGRG5 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[TFF3]] | C | ADGRG5 activity raises TFF3's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 2.57× lower at baseline in the lines without ADGRG5 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[FGF19]] | C | ADGRG5 activity raises FGF19's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without ADGRG5 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 46.3); signed map (63.9, 12.3). **Vector** length 38.2, 12.6% of its response variance represented; |z| ≥ 3 in 296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor G5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,542,643-57,591,681 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGR27; previously GPR114 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily G |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZF4](https://www.uniprot.org/uniprotkb/Q8IZF4) (Adhesion G protein-coupled receptor G5):

> Orphan adhesion G protein-coupled receptor (aGPCR). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. ADGRG5 is specifically coupled to G(s) G proteins and mediates activation of adenylate cyclase activity.

**Summary**, from NCBI Gene [221188](https://www.ncbi.nlm.nih.gov/gene/221188):

> This gene encodes a member of the adhesion family of G-protein coupled receptors. Members of this family are characterized by long N-termini and multiple functional domains. They may play a role in the immune system as well as in the central nervous system. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:19010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19010) · Entrez [221188](https://www.ncbi.nlm.nih.gov/gene/221188) · UniProt [Q8IZF4](https://www.uniprot.org/uniprotkb/Q8IZF4) · Ensembl [ENSG00000159618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159618)

## Data

Gene col 8265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8265); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8265]; `tensor/DDL_lfc|DDL_z.npy` [8265]; `embed/gene_vectors.npy` [8265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8265 or target_col == 8265). Every well: [[ADGRG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
