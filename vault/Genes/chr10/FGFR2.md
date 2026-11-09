---
symbol: "FGFR2"
type: "gene"
col: 830
ensembl_id: "ENSG00000066468"
name: "fibroblast growth factor receptor 2"
location: "10q26.13"
module: 44
arm: "+"
pooled_cpm: 168.63
n_lines_expressing: 6
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 48
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# FGFR2

*fibroblast growth factor receptor 2* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.76× (z +14.0, q 1e-41, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +7.4, q 2e-11, up in 1 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.654× (z -4.5, q 0.002, down in 4 of 4 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15L]] (+0.77, fdr 7e-06), [[VIPR1]] (+0.75, fdr 1e-05), [[ATP10B]] (+0.73, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PHGR1]] → it (grade C ⚠); 48 go from it, the strongest it → [[KCNQ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +14.0 | 1e-41 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +10.7 | 2e-24 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +8.3 | 2e-14 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.4 | 2e-11 | 1/4 (AN3 CA) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +6.1 | 1e-07 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +5.6 | 2e-06 | 2/4 (HT-29, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.6 | 2e-06 | 1/4 (LS 180) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.9 | 7e-05 | 1/6 (LS 180) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.002 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.004 | 1/4 (HT-29) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.005 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.010 | 0/4 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.031 | 0/4 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.055 | 3/4 (LS 180, KATO III, …) | two highest doses | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.070 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -4.5 | 0.002 | 4/4 (KATO III, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.657×** | -4.5 | 0.002 | 4/4 (AN3 CA, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.758×** | -4.2 | 0.006 | 4/4 (KATO III, AN3 CA, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **0.721×** | -3.5 | 0.065 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -3.4 | 0.065 | 2/4 (LS 180, AN3 CA) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.708×** | -3.4 | 0.065 | 0/4 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 6,600 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -8.8) |
| [[AN3 CA (line)]] | alt | 422 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.6) |
| [[A-172 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 35.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 34.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 32.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 16.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15L]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[VIPR1]] | +0.75 | +0.49 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[ATP10B]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.70 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CYP4F12]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PRR15]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ILDR2]] | +0.67 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ST6GALNAC1]] | +0.67 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHGR1]] | C | PHGR1 activity raises FGFR2's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 1.87× lower at baseline in the lines without PHGR1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises FGFR2's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 1.55× lower at baseline in the lines without GPA33 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[CADPS]] | C | CADPS activity raises FGFR2's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.08× lower at baseline in the lines without CADPS | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises FGFR2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.10× lower at baseline in the lines without MYO7B | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises FGFR2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.28× lower at baseline in the lines without CLIC5 | 0.094 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 4, C 44. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNQ1]] | B | FGFR2 activity raises KCNQ1's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 3.30× lower at baseline in the lines without FGFR2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2 |
| [[MUC12]] | B | FGFR2 activity raises MUC12's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 2.79× lower at baseline in the lines without FGFR2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2 |
| [[CALML4]] | B | FGFR2 activity raises CALML4's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 2.04× lower at baseline in the lines without FGFR2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2 |
| [[FUT2]] | B | FGFR2 activity raises FUT2's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 2.65× lower at baseline in the lines without FGFR2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2 |
| [[MUC5B]] | C | FGFR2 activity raises MUC5B's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 7.55× lower at baseline in the lines without FGFR2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[CFTR]] | C | FGFR2 activity raises CFTR's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 6.55× lower at baseline in the lines without FGFR2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[HEPH]] | C | FGFR2 activity raises HEPH's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 6.87× lower at baseline in the lines without FGFR2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[AGR3]] | C | FGFR2 activity raises AGR3's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 7.21× lower at baseline in the lines without FGFR2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[LGALS4]] | C | FGFR2 activity raises LGALS4's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 8.30× lower at baseline in the lines without FGFR2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[APOH]] | C | FGFR2 activity raises APOH's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 2.48× lower at baseline in the lines without FGFR2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[PIP5K1B]] | C | FGFR2 activity raises PIP5K1B's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 8.28× lower at baseline in the lines without FGFR2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[BCAS1]] | C | FGFR2 activity raises BCAS1's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 4.88× lower at baseline in the lines without FGFR2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.6, 52.0); signed map (63.0, 5.6). **Vector** length 21.9, 10.4% of its response variance represented; |z| ≥ 3 in 116 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.53 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.53 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +0.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +7.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +4.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.5 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.5 | -0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -0.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:121,478,332-121,598,458 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEK3, TK14, TK25, ECT1, K-SAM, CD332; previously KGFR, BEK, CFD1, JWS |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Fibroblast growth factor receptor family |
| Reactome | 34 pathways, smallest: FGFR2b ligand binding and activation; Activated point mutants of FGFR2; FGFR2c ligand binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P21802](https://www.uniprot.org/uniprotkb/P21802) (Fibroblast growth factor receptor 2):

> Tyrosine-protein kinase that acts as a cell-surface receptor for fibroblast growth factors and plays an essential role in the regulation of cell proliferation, differentiation, migration and apoptosis, and in the regulation of embryonic development. Required for normal embryonic patterning, trophoblast function, limb bud development, lung morphogenesis, osteogenesis and skin development. Plays an essential role in the regulation of osteoblast differentiation, proliferation and apoptosis, and is …

**Summary**, from NCBI Gene [2263](https://www.ncbi.nlm.nih.gov/gene/2263):

> The protein encoded by this gene is a member of the fibroblast growth factor receptor family, where amino acid sequence is highly conserved between members and throughout evolution. FGFR family members differ from one another in their ligand affinities and tissue distribution. A full-length representative protein consists of an extracellular region, composed of three immunoglobulin-like domains, a single hydrophobic membrane-spanning segment and a cytoplasmic tyrosine kinase domain. The …

**Accessions** — [HGNC:3689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3689) · Entrez [2263](https://www.ncbi.nlm.nih.gov/gene/2263) · UniProt [P21802](https://www.uniprot.org/uniprotkb/P21802) · Ensembl [ENSG00000066468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066468)

## Data

Gene col 830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 830); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 830]; `tensor/DDL_lfc|DDL_z.npy` [830]; `embed/gene_vectors.npy` [830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 830 or target_col == 830). Every well: [[FGFR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
