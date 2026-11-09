---
symbol: "CACNA2D4"
type: "gene"
col: 7480
ensembl_id: "ENSG00000151062"
name: "calcium voltage-gated channel auxiliary subunit alpha2delta 4"
location: "12p13.33"
module: 196
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 28
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 11
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# CACNA2D4

*calcium voltage-gated channel auxiliary subunit alpha2delta 4* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.09× (z +16.8, q 0e+00, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.54× (z +15.0, q 0e+00, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.563× (z -4.8, q 8e-04, down in 14 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF19]] (+0.67, fdr 7e-06), [[LCK]] (+0.65, fdr 7e-06), [[MIR4280HG]] (+0.64, fdr 7e-06).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LINC03042]] → it (grade B ⚠); 11 go from it, the strongest it → [[KIF21B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.09×** | +16.8 | 0e+00 | 2/4 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.32×** | +15.4 | 0e+00 | 6/8 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.54×** | +15.0 | 0e+00 | 8/20 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.10×** | +12.6 | 2e-34 | 2/5 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +8.4 | 6e-15 | 2/20 (LoVo, SNU-423) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +5.2 | 2e-05 | 11/23 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.5 | 5e-04 | 5/23 (KATO III, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.78×** | +4.5 | 5e-04 | 1/8 (COLO 205) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +4.3 | 9e-04 | 2/7 (COLO 205, HepG2/C3A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.63×** | +4.2 | 0.001 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.003 | 3/22 (LoVo, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.005 | 10/22 (BT-474, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.8 | 0.006 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.017 | 2/20 (J82, HS-578T) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.2 | 0.045 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.045 | 1/11 (KATO III) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.060 | 2/14 (SW1417, KATO III) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -4.8 | 8e-04 | 14/20 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.676×** | -4.6 | 0.001 | 12/23 (HepG2/C3A, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.625×** | -4.1 | 0.008 | 10/23 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.686×** | -4.0 | 0.011 | 10/23 (SW480, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.605×** | -3.9 | 0.011 | 9/23 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.468×** | -3.3 | 0.070 | 5/23 (HOP62, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.070 | 9/23 (SW480, HepG2/C3A, …) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.696× | -3.1 | 0.15 | 10/23 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 5 µM |  | 0.775× | -3.0 | 0.15 | 2/23 (hTERT-HPNE, LoVo) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0592× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -11.4) |
| [[HOP62 (line)]] | alt | 17.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 8.11× (z +10.9) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.114× (z -11.2) |
| [[KATO III (line)]] | alt | 5.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0561× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 5.68 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0414× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0993× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.868 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.763 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF19]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MIR4280HG]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[IL19]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[LAPTM5]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[IGFL4]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC02964]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 | **novel candidate** |
| [[FKBP9P1-1]] | +0.57 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SCN5A]] | +0.55 | +0.46 / +0.50 | both halves | 3e-05 | STRING 414 |
| [[DIO3OS]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EPHB6]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ETV4]] | +0.55 | +0.47 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03042]] | B | LINC03042 activity raises CACNA2D4's level | lines that do not express LINC03042 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without LINC03042 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC00960, CORO2B, DNAH17; maybe low, not absent |
| [[FGF19]] | B | FGF19 activity raises CACNA2D4's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 2.05× lower at baseline in the lines without FGF19 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5 |
| [[MILR1]] | B | MILR1 activity raises CACNA2D4's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without MILR1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[GPSM3]] | B | GPSM3 activity raises CACNA2D4's level | lines that do not express GPSM3 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without GPSM3 | 0.043 | ⚠ within organs, on part of the lines; also absent: NAV1, CDK15, PAMR1 |
| [[LINC00659]] | B | LINC00659 activity raises CACNA2D4's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without LINC00659 | 0.045 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[PAEP]] | B | PAEP activity raises CACNA2D4's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.52× lower at baseline in the lines without PAEP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[MIR4280HG]] | B | MIR4280HG activity raises CACNA2D4's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.97× lower at baseline in the lines without MIR4280HG | 0.054 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises CACNA2D4's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SCAT1]] | B | SCAT1 activity raises CACNA2D4's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without SCAT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[IL19]] | B | IL19 activity raises CACNA2D4's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without IL19 | 0.0997 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises CACNA2D4's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.28× lower at baseline in the lines without FKBP9P1-1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[LCK]] | C | LCK activity raises CACNA2D4's level | lines that do not express LCK (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without LCK | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF21B]] | B | CACNA2D4 activity raises KIF21B's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without CACNA2D4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[EPHB6]] | B | CACNA2D4 activity raises EPHB6's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without CACNA2D4 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[SCN5A]] | B | CACNA2D4 activity raises SCN5A's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without CACNA2D4 | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[RAC2]] | B | CACNA2D4 activity raises RAC2's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without CACNA2D4 | 0.048 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[ANO4]] | B | CACNA2D4 activity raises ANO4's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without CACNA2D4 | 0.076 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[FGF19]] | B | CACNA2D4 activity raises FGF19's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without CACNA2D4 | 0.085 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[IGFL4]] | B | CACNA2D4 activity raises IGFL4's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.51× lower at baseline in the lines without CACNA2D4 | 0.095 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[PIWIL1]] | C | CACNA2D4 activity raises PIWIL1's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without CACNA2D4 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent; co-absent with the target |
| [[MANCR]] | C | CACNA2D4 activity raises MANCR's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 2.45× lower at baseline in the lines without CACNA2D4 | 0.061 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent; co-absent with the target |
| [[PADI1]] | C | CACNA2D4 activity raises PADI1's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without CACNA2D4 | 0.072 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent; co-absent with the target |
| [[LCK]] | C | CACNA2D4 activity raises LCK's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without CACNA2D4 | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.5, 8.2); signed map (9.8, 52.6). **Vector** length 49.1, 11.0% of its response variance represented; |z| ≥ 3 in 528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +5.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | -0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit alpha2delta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:1,791,963-1,918,666 (-) |
| Ensembl biotype | protein_coding |
| Also known as | alpha2delta-4 |
| Gene groups (HGNC) | Calcium voltage-gated channel auxiliary alpha2delta subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3S7](https://www.uniprot.org/uniprotkb/Q7Z3S7) (Voltage-dependent calcium channel subunit alpha-2/delta-4):

> The alpha-2/delta subunit of voltage-dependent calcium channels regulates calcium current density and activation/inactivation kinetics of the calcium channel.

**Summary**, from NCBI Gene [93589](https://www.ncbi.nlm.nih.gov/gene/93589):

> This gene encodes a member of the alpha-2/delta subunit family, a protein in the voltage-dependent calcium channel complex. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization and consist of a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. Various versions of each of these subunits exist, either expressed from similar genes or the result of alternative splicing. Research on a highly similar protein in rabbit suggests the …

**Accessions** — [HGNC:20202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20202) · Entrez [93589](https://www.ncbi.nlm.nih.gov/gene/93589) · UniProt [Q7Z3S7](https://www.uniprot.org/uniprotkb/Q7Z3S7) · Ensembl [ENSG00000151062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151062)

## Data

Gene col 7480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7480); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7480]; `tensor/DDL_lfc|DDL_z.npy` [7480]; `embed/gene_vectors.npy` [7480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7480 or target_col == 7480). Every well: [[CACNA2D4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA2D4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
