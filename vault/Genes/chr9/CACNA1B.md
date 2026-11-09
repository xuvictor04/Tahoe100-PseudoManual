---
symbol: "CACNA1B"
type: "gene"
col: 7280
ensembl_id: "ENSG00000148408"
name: "calcium voltage-gated channel subunit alpha1 B"
location: "9q34.3"
module: 128
arm: "+"
pooled_cpm: 7.1
n_lines_expressing: 35
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# CACNA1B

*calcium voltage-gated channel subunit alpha1 B* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +17.9, q 0e+00, up in 15 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.384× (z -11.4, q 3e-27, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC36]] (+0.77, fdr 7e-06), [[JPH3]] (+0.71, fdr 7e-06), [[RFPL1S]] (+0.66, fdr 7e-06); moves opposite to [[TMED8]] (-0.45, fdr 3e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYT1]] → it (grade B ⚠); 10 go from it, the strongest it → [[ERICH6-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +17.9 | 0e+00 | 15/27 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.62×** | +17.5 | 0e+00 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.37×** | +14.5 | 4e-45 | 22/32 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +14.0 | 2e-42 | 16/29 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +12.2 | 6e-32 | 1/10 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.65×** | +11.6 | 5e-29 | 16/29 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +10.1 | 5e-22 | 6/16 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +9.3 | 1e-18 | 20/31 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +8.0 | 8e-14 | 17/32 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +6.4 | 7e-09 | 17/32 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.8 | 4e-07 | 12/27 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.4 | 3e-06 | 11/32 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.8 | 0.006 | 0/10 | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.010 | 3/28 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.010 | 6/26 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.012 | 2/32 (HEC-1-A, SW1417) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.026 | 1/31 (HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.384×** | -11.4 | 3e-27 | 19/30 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -5.0 | 2e-04 | 17/32 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -4.6 | 7e-04 | 11/22 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.682×** | -4.4 | 0.002 | 10/28 (J82, SHP-77, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.712×** | -4.0 | 0.006 | 14/32 (C-33 A, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.732×** | -3.7 | 0.020 | 6/32 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.768× | -3.1 | 0.14 | 13/31 (C-33 A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 72.1 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -15.2) |
| [[A549 (line)]] | wt | 27.5 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0184× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.2) |
| [[A-427 (line)]] | wt | 57.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.2) |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 5.40 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 10.0× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 7.32 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -9.9) |
| [[H4 (line)]] | wt | 10.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0453× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 2.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.56× (z +9.3) | — |
| [[LoVo (line)]] | wt | 1.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC36]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[JPH3]] | +0.71 | +0.68 / +0.59 | both halves | 7e-06 | STRING 491 |
| [[RFPL1S]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CELF5]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CDH23]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NR5A2]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[LINC00466]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DPYSL5]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[APC2]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.57 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[RBFOX3]] | +0.57 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[FBXO27]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED8]] | -0.45 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYT1]] | B | MYT1 activity raises CACNA1B's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without MYT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[PAX2]] | B | PAX2 activity raises CACNA1B's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without PAX2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERICH6-AS1]] | B | CACNA1B activity raises ERICH6-AS1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.52× lower at baseline in the lines without CACNA1B | 0.024 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[RYR1]] | B | CACNA1B activity raises RYR1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without CACNA1B | 0.032 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[ANKS1B]] | B | CACNA1B activity raises ANKS1B's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without CACNA1B | 0.035 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[EFHD1]] | B | CACNA1B activity raises EFHD1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without CACNA1B | 0.047 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[DNAI1]] | B | CACNA1B activity raises DNAI1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without CACNA1B | 0.050 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[TMEM150C]] | B | CACNA1B activity raises TMEM150C's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 2.27× lower at baseline in the lines without CACNA1B | 0.059 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[CELF5]] | B | CACNA1B activity raises CELF5's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without CACNA1B | 0.071 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[FAM184A]] | B | CACNA1B activity raises FAM184A's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without CACNA1B | 0.089 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[LINC03036]] | B | CACNA1B activity raises LINC03036's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.21× lower at baseline in the lines without CACNA1B | 0.091 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[LINC00466]] | B | CACNA1B activity raises LINC00466's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without CACNA1B | 0.097 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.1, 37.2); signed map (25.0, 25.4). **Vector** length 59.1, 10.9% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +17.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +3.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | +0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -11.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.4 | -4.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel subunit alpha1 B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,877,782-138,124,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cav2.2, CACNN; previously CACNL1A5 |
| Gene groups (HGNC) | EF-hand domain containing; Calcium voltage-gated channel alpha1 subunits |
| Hallmark sets | PEROXISOME |
| Reactome | 3 pathways, smallest: Presynaptic depolarization and calcium channel opening; Transmission across Chemical Synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00975](https://www.uniprot.org/uniprotkb/Q00975) (Voltage-dependent N-type calcium channel subunit alpha-1B):

> Voltage-sensitive calcium channels (VSCC) mediate the entry of calcium ions into excitable cells and are also involved in a variety of calcium-dependent processes, including muscle contraction, hormone or neurotransmitter release, gene expression, cell motility, cell division and cell death. This alpha-1B subunit gives rise to N-type calcium currents. N-type calcium channels belong to the 'high-voltage activated' (HVA) group. They are involved in pain signaling. Calcium channels containing …

**Summary**, from NCBI Gene [774](https://www.ncbi.nlm.nih.gov/gene/774):

> The protein encoded by this gene is the pore-forming subunit of an N-type voltage-dependent calcium channel, which controls neurotransmitter release from neurons. The encoded protein forms a complex with alpha-2, beta, and delta subunits to form the high-voltage activated channel. This channel is sensitive to omega-conotoxin-GVIA and omega-agatoxin-IIIA but insensitive to dihydropyridines. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:1389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1389) · Entrez [774](https://www.ncbi.nlm.nih.gov/gene/774) · UniProt [Q00975](https://www.uniprot.org/uniprotkb/Q00975) · Ensembl [ENSG00000148408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148408)

## Data

Gene col 7280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7280); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7280]; `tensor/DDL_lfc|DDL_z.npy` [7280]; `embed/gene_vectors.npy` [7280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7280 or target_col == 7280). Every well: [[CACNA1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
