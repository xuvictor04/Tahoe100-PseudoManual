---
symbol: "UGT1A1"
type: "gene"
col: 14281
ensembl_id: "ENSG00000241635"
name: "UDP glucuronosyltransferase family 1 member A1"
location: "2q37.1"
module: 44
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 14
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 59
direction_downstream: 91
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# UGT1A1

*UDP glucuronosyltransferase family 1 member A1* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.70× (z +10.6, q 1e-23, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.70× (z +4.2, q 0.002, up in 0 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.489× (z -4.0, q 0.026, down in 9 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A6]] (+0.92, fdr 7e-06, ⚠ same locus), [[UGT1A9]] (+0.86, fdr 7e-06, ⚠ same locus), [[LGALS4]] (+0.85, fdr 7e-06), [[GPA33]] (+0.81, fdr 7e-06), [[ST6GALNAC1]] (+0.81, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[PPM1E]] → it (grade B ⚠); 91 go from it, the strongest it → [[MECOM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.70×** | +10.6 | 1e-23 | 3/6 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.92×** | +9.6 | 2e-19 | 2/4 (KATO III, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.72×** | +8.0 | 2e-13 | 1/6 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.44×** | +5.0 | 1e-04 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.30×** | +4.6 | 4e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.48×** | +4.5 | 6e-04 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.4 | 9e-04 | 0/8 | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.002 | 0/11 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.82×** | +4.0 | 0.004 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.9 | 0.006 | 3/8 (AsPC-1, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.8 | 0.006 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.014 | 0/9 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.39×** | +3.6 | 0.016 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.86×** | +3.4 | 0.025 | 1/8 (KATO III) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.034 | 1/11 (Hs 766T) | rises with dose | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **1.82×** | +3.1 | 0.059 | 0/8 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.489×** | -4.0 | 0.026 | 9/11 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.026 | 2/11 (AsPC-1, Panc 03.27) | rises with dose | plate-row cell shift |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.389×** | -3.7 | 0.038 | 2/11 (LS 180, SNU-423) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.540× | -3.2 | 0.17 | 0/11 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.549× | -3.0 | 0.26 | 9/11 (HT-29, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 16.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -19.4) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0634× (z -17.8) |
| [[LoVo (line)]] | wt | 22.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0224× (z -19.5) |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0316× (z -13.5) |
| [[Hs 766T (line)]] | wt | 4.61 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -10.0) |
| [[KATO III (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -8.9) ⚠ cell-cycle shift, explains ~76% of this change |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -12.3) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A-172 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.166 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.405 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A6]] | +0.92 | +0.93 / +0.88 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 998; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A9]] | +0.86 | +0.87 / +0.80 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 998; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LGALS4]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A8]] | +0.81 | +0.81 / +0.74 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 996; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GPA33]] | +0.81 | +0.81 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.81 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PRR15]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.79 | +0.79 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.79 | +0.81 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[FXYD3]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[CFTR]] | +0.78 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.78 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[NPSR1]] | +0.76 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 2, C 57. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1E]] | B | PPM1E activity lowers UGT1A1's level | lines that do not express PPM1E (16) vs lines expressing it (34) | 3.03× higher at baseline in the lines without PPM1E | 0.031 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises UGT1A1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without HTR1D | 0.086 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[UGT1A6]] | C | UGT1A6 activity raises UGT1A1's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 4.95× lower at baseline in the lines without UGT1A6 | 5e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[UGT1A8]], [[UGT1A9]] | C | UGT1A8, UGT1A9 activity raises UGT1A1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 4.02× lower at baseline in the lines without UGT1A8, UGT1A9 | 3e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[NPSR1]] | C | NPSR1 activity raises UGT1A1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 8.11× lower at baseline in the lines without NPSR1 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[CREB3L1]] | C | CREB3L1 activity raises UGT1A1's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without CREB3L1 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises UGT1A1's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 4.94× lower at baseline in the lines without PLA2G2A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises UGT1A1's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without PTPRR | 0.005 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises UGT1A1's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 4.34× lower at baseline in the lines without MUC2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises UGT1A1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 5.87× lower at baseline in the lines without FAM3D | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises UGT1A1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 5.11× lower at baseline in the lines without CDH17 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises UGT1A1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.47× lower at baseline in the lines without CEACAM5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*91 arrows, 91 of them with an alert ⚠; grade A 0, B 30, C 61. Shown: the 12 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MECOM]] | B | UGT1A1 activity raises MECOM's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 4.45× lower at baseline in the lines without UGT1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[SEPTIN9-DT]] | B | UGT1A1 activity raises SEPTIN9-DT's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.17× lower at baseline in the lines without UGT1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[PLA2R1]] | B | UGT1A1 activity raises PLA2R1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without UGT1A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[HTR1D]] | B | UGT1A1 activity raises HTR1D's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without UGT1A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[SEPTIN9-DT]] | B | UGT1A1 activity strengthens SEPTIN9-DT's drug response | lines that do not express UGT1A1 (22) vs lines expressing it (10) | the lines without UGT1A1 respond 0.83× as strongly (z diff +0.60); strongest at Panobinostat 0.05 µM: 0.74x vs 0.14x (z diff +5.4) | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; target measured in part of the lines; both ways; artifact flags |
| [[MUC12]] | B | UGT1A1 activity weakens MUC12's drug response | lines that do not express UGT1A1 (20) vs lines expressing it (7) | (z diff -2.94); strongest at Homoharringtonine 5 µM: 2.25x vs 0.31x (z diff -9.5) | 0.016 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; target measured in part of the lines; artifact flags |
| [[RSPH1]] | B | UGT1A1 activity raises RSPH1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 1.92× lower at baseline in the lines without UGT1A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[SLC12A2]] | B | UGT1A1 activity raises SLC12A2's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.16× lower at baseline in the lines without UGT1A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[MECOM]] | B | UGT1A1 activity weakens MECOM's drug response | lines that do not express UGT1A1 (19) vs lines expressing it (12) | the lines without UGT1A1 respond 0.89× as strongly (z diff +0.52); strongest at Panobinostat 0.05 µM: 2.10x vs 1.30x (z diff -3.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; target measured in part of the lines; both ways; artifact flags |
| [[MUC3A]] | B | UGT1A1 activity raises MUC3A's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.95× lower at baseline in the lines without UGT1A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[PLCH1]] | B | UGT1A1 activity strengthens PLCH1's drug response | lines that do not express UGT1A1 (28) vs lines expressing it (8) | the lines without UGT1A1 respond 0.65× as strongly (z diff +0.94); strongest at Panobinostat 0.5 µM: 0.61x vs 0.32x (z diff +4.7) | 0.045 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; target measured in part of the lines; artifact flags |
| [[ADD3-AS1]] | B | UGT1A1 activity raises ADD3-AS1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 1.95× lower at baseline in the lines without UGT1A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.881). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 51.3); signed map (63.7, 4.5). **Vector** length 44.0, 16.9% of its response variance represented; |z| ≥ 3 in 298 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.63 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.63 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +1.9 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[4EGI-1 (drug)]] 0.5 µM |  | -1.0 | -3.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | UDP glucuronosyltransferase family 1 member A1 |
| Locus type | complex locus constituent (other) |
| Location | 2q37.1 — chr2:233,760,270-233,773,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UGT1A; previously UGT1, GNT1 |
| Gene groups (HGNC) | UDP glucuronosyltransferases |
| Reactome | 10 pathways, smallest: Glucuronidation; Heme degradation; Aspirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P22309](https://www.uniprot.org/uniprotkb/P22309) (UDP-glucuronosyltransferase 1A1):

> [Isoform 1]: UDP-glucuronosyltransferase (UGT) that catalyzes phase II biotransformation reactions in which lipophilic substrates are conjugated with glucuronic acid to increase the metabolite's water solubility, thereby facilitating excretion into either the urine or bile. Essential for the elimination and detoxification of drugs, xenobiotics and endogenous compounds. Catalyzes the glucuronidation of endogenous estrogen hormones such as estradiol, estrone and estriol. Involved in the …

**Summary**, from NCBI Gene [54658](https://www.ncbi.nlm.nih.gov/gene/54658):

> This gene encodes a UDP-glucuronosyltransferase, an enzyme of the glucuronidation pathway that transforms small lipophilic molecules, such as steroids, bilirubin, hormones, and drugs, into water-soluble, excretable metabolites. This gene is part of a complex locus that encodes several UDP-glucuronosyltransferases. The locus includes thirteen unique alternate first exons followed by four common exons. Four of the alternate first exons are considered pseudogenes. Each of the remaining nine 5' …

**Accessions** — [HGNC:12530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12530) · Entrez [54658](https://www.ncbi.nlm.nih.gov/gene/54658) · UniProt [P22309](https://www.uniprot.org/uniprotkb/P22309) · Ensembl [ENSG00000241635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241635)

## Data

Gene col 14281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14281); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14281]; `tensor/DDL_lfc|DDL_z.npy` [14281]; `embed/gene_vectors.npy` [14281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14281 or target_col == 14281). Every well: [[UGT1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGT1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
