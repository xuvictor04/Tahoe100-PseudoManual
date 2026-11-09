---
symbol: "CDH13"
type: "gene"
col: 6467
ensembl_id: "ENSG00000140945"
name: "cadherin 13"
location: "16q23.3"
module: 13
arm: "+"
pooled_cpm: 277.8
n_lines_expressing: 15
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 33
direction_downstream: 68
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CDH13

*cadherin 13* — 16q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.08× (z +18.7, q 0e+00, up in 9 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.463× (z -9.0, q 1e-16, down in 13 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NALF1]] (+0.73, fdr 7e-06), [[GPR68]] (+0.67, fdr 7e-06), [[ADAMTS6]] (+0.66, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[C13orf46]] → it (grade B ⚠); 68 go from it, the strongest it → [[RASA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.08×** | +18.7 | 0e+00 | 9/13 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +13.1 | 6e-37 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +8.4 | 6e-15 | 7/13 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +7.8 | 1e-12 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.75×** | +6.4 | 2e-08 | 6/13 (RPMI-7951, SK-MEL-2, …) | top dose only | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.2 | 7e-08 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.0 | 1e-07 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.3 | 0.001 | 6/12 (CHP-212, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.002 | 0/13 | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +3.6 | 0.017 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.023 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.081 | 2/13 (SNU-423, SK-MEL-2) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.081 | 0/14 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.463×** | -9.0 | 1e-16 | 13/13 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.559×** | -6.8 | 3e-09 | 13/13 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.600×** | -6.0 | 4e-07 | 13/13 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.613×** | -5.7 | 1e-06 | 13/13 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.593×** | -5.7 | 2e-06 | 5/13 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.647×** | -5.1 | 3e-05 | 12/13 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -4.8 | 1e-04 | 1/12 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.652×** | -4.8 | 1e-04 | 11/15 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.748×** | -4.7 | 2e-04 | 4/13 (SK-MEL-2, NCI-H1792, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.496×** | -4.3 | 1e-03 | 12/14 (NCI-H460, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.719×** | -3.9 | 0.006 | 0/13 | two highest doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.710×** | -3.7 | 0.010 | 0/13 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.022 | 4/13 (SNU-423, HOP62, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.043 | 0/13 | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.589×** | -3.2 | 0.045 | 8/13 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.767×** | -3.1 | 0.069 | 6/13 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.768×** | -3.1 | 0.069 | 9/13 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,279 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -21.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0743× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 863 | 0 | 10 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.495× (z -16.2) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -12.2) |
| [[SW480 (line)]] | alt | 669 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0960× (z -15.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.101× (z -15.0) |
| [[A-172 (line)]] | wt | 1,134 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.136× (z -15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.138× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 463 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.152× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.169× (z -13.3) |
| [[HOP62 (line)]] | alt | 1,135 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.122× (z -14.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.126× (z -14.0) |
| [[HS-578T (line)]] | alt | 1,704 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -15.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 541 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.283× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.288× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 468 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.212× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -9.1) |
| [[SNU-423 (line)]] | alt | 527 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 340 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.388× (z -9.2) ⚠ cell-cycle shift, explains ~86% of this change |
| [[SW 1088 (line)]] | alt | 929 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0608× (z -11.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.108× (z -9.0) |
| [[A-427 (line)]] | wt | 17.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 51.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 36.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 65.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 29.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 31.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 24.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 34.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 34.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 30.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NALF1]] | +0.73 | +0.61 / +0.79 | both halves | 7e-06 | same gene group |
| [[GPR68]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[SAMD3]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SPOCK1]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[EVA1A]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[HS3ST3A1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[TCF4]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TMEM200A]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[FRMD4A]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[RFX8]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FGF5]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 1, C 32. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C13orf46]] | B | C13orf46 activity raises CDH13's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 3.59× lower at baseline in the lines without C13orf46 | 0.061 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[WNT5A]] | C | WNT5A activity raises CDH13's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 8.56× lower at baseline in the lines without WNT5A | 4e-04 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[NTM]] | C | NTM activity raises CDH13's level | lines that do not express NTM (33) vs lines expressing it (17) | 10.38× lower at baseline in the lines without NTM | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises CDH13's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 9.92× lower at baseline in the lines without APCDD1L | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ANGPTL2]] | C | ANGPTL2 activity raises CDH13's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 5.86× lower at baseline in the lines without ANGPTL2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises CDH13's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 9.56× lower at baseline in the lines without HS3ST3A1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[MME]] | C | MME activity raises CDH13's level | lines that do not express MME (30) vs lines expressing it (20) | 7.56× lower at baseline in the lines without MME | 0.002 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises CDH13's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 6.18× lower at baseline in the lines without PDCD1LG2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises CDH13's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 5.75× lower at baseline in the lines without ADAMTS6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[FLI1]] | C | FLI1 activity raises CDH13's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 6.09× lower at baseline in the lines without FLI1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises CDH13's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 5.97× lower at baseline in the lines without RFX8 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises CDH13's level | lines that do not express GYPC (35) vs lines expressing it (15) | 7.91× lower at baseline in the lines without GYPC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 21, C 47. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA3]] | B | CDH13 activity raises RASA3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without CDH13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[FHAD1]] | B | CDH13 activity raises FHAD1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.40× lower at baseline in the lines without CDH13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[C13orf46]] | B | CDH13 activity raises C13orf46's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without CDH13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[SLCO1C1]] | B | CDH13 activity raises SLCO1C1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without CDH13 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[REP15]] | B | CDH13 activity raises REP15's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 1.62× lower at baseline in the lines without CDH13 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[FMNL1-DT]] | B | CDH13 activity raises FMNL1-DT's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without CDH13 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[RASSF8]] | B | CDH13 activity raises RASSF8's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without CDH13 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[SH2B3]] | B | CDH13 activity raises SH2B3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without CDH13 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[FMNL3]] | B | CDH13 activity raises FMNL3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without CDH13 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[CD82]] | B | CDH13 activity raises CD82's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.24× lower at baseline in the lines without CDH13 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[PDE4DIPP2]] | B | CDH13 activity raises PDE4DIPP2's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.64× lower at baseline in the lines without CDH13 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[NMNAT2]] | B | CDH13 activity weakens NMNAT2's drug response | lines that do not express CDH13 (20) vs lines expressing it (9) | the lines without CDH13 respond 3.09× as strongly (z diff -2.51); strongest at Tucidinostat 0.5 µM: 3.88x vs 1.57x (z diff -5.0) | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 14.5); signed map (20.0, 48.2). **Vector** length 89.0, 38.6% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +18.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +4.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -5.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.3 — chr16:82,626,965-83,800,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHH |
| Gene groups (HGNC) | Major cadherins; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS, COMPLEMENT, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55290](https://www.uniprot.org/uniprotkb/P55290) (Cadherin-13):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. May act as a negative regulator of neural cell growth.

**Summary**, from NCBI Gene [1012](https://www.ncbi.nlm.nih.gov/gene/1012):

> This gene encodes a member of the cadherin superfamily. The encoded protein is localized to the surface of the cell membrane and is anchored by a GPI moiety, rather than by a transmembrane domain. The protein lacks the cytoplasmic domain characteristic of other cadherins, and so is not thought to be a cell-cell adhesion glycoprotein. This protein acts as a negative regulator of axon growth during neural differentiation. It also protects vascular endothelial cells from apoptosis due to oxidative …

**Accessions** — [HGNC:1753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1753) · Entrez [1012](https://www.ncbi.nlm.nih.gov/gene/1012) · UniProt [P55290](https://www.uniprot.org/uniprotkb/P55290) · Ensembl [ENSG00000140945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140945)

## Data

Gene col 6467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6467); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6467]; `tensor/DDL_lfc|DDL_z.npy` [6467]; `embed/gene_vectors.npy` [6467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6467 or target_col == 6467). Every well: [[CDH13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
