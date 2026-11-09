---
symbol: "ADGRF1"
type: "gene"
col: 7712
ensembl_id: "ENSG00000153292"
name: "adhesion G protein-coupled receptor F1"
location: "6p12.3"
module: 8
arm: "+"
pooled_cpm: 29.31
n_lines_expressing: 15
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 113
direction_downstream: 168
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ADGRF1

*adhesion G protein-coupled receptor F1* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +9.8, q 4e-20, up in 0 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +4.5, q 0.001, up in 0 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.501× (z -6.3, q 1e-07, down in 13 of 13 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.661× (z -5.4, q 1e-05, down in 13 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.86, fdr 7e-06), [[SLC44A4]] (+0.77, fdr 7e-06), [[CLIC5]] (+0.76, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 113 arrows point to it, the strongest [[MUC20]] → it (grade B ⚠); 168 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.8 | 4e-20 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.7 | 6e-09 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.5 | 0.001 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.33×** | +3.9 | 0.011 | 8/12 (AsPC-1, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.015 | 9/13 (AsPC-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.015 | 7/13 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.4 | 0.052 | 1/13 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.4 | 0.052 | 10/12 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.058 | 5/13 (LS 180, SW1417, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.91×** | +3.2 | 0.088 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.088 | 1/13 (HT-29) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.501×** | -6.3 | 1e-07 | 13/13 (KATO III, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.525×** | -5.9 | 1e-06 | 13/13 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.549×** | -5.5 | 7e-06 | 13/13 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -5.4 | 1e-05 | 13/13 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.600×** | -4.7 | 3e-04 | 6/13 (NCI-H1573, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.594×** | -4.6 | 4e-04 | 12/13 (Panc 03.27, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.652×** | -3.9 | 0.007 | 10/13 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -3.9 | 0.007 | 10/13 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.679×** | -3.5 | 0.025 | 0/13 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.683×** | -3.5 | 0.028 | 10/13 (LoVo, SW 900, …) | top dose only | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.028 | 11/13 (HEC-1-A, KATO III, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.706×** | -3.2 | 0.066 | 6/13 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.075 | 2/13 (LS 180, LoVo) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.082 | 12/13 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.791×** | -3.0 | 0.092 | 6/13 (NCI-H1573, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 174 | 0 | 23 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0490× (z -23.8) |
| [[Panc 03.27 (line)]] | alt | 232 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -24.9) |
| [[KATO III (line)]] | alt | 180 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0103× (z -29.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0894× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 173 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.5) |
| [[LoVo (line)]] | wt | 50.4 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 87.9 | 2 (1 ⚠) | 3 (2 ⚠) | [[Trametinib (drug)]] 0.05 µM 3.81× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.0984× (z -11.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.114× (z -10.8) |
| [[HT-29 (line)]] | alt | 61.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 99.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0803× (z -19.3) |
| [[A-172 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.86 | +0.85 / +0.82 | both halves | 7e-06 | same gene group |
| [[SLC44A4]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[NECTIN4]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HHLA2]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ALOX5]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RBM47]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.72 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[TMC5]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[OCLN]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[TC2N]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*113 arrows, 113 of them with an alert ⚠; grade A 0, B 14, C 99. Shown: the 12 strongest; 101 more arrows (101 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | MUC20 activity raises ADGRF1's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 3.43× lower at baseline in the lines without MUC20 | 0.040 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises ADGRF1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.60× lower at baseline in the lines without IKZF2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises ADGRF1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.06× lower at baseline in the lines without MTUS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ADGRF1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.35× lower at baseline in the lines without ELF3-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LGALS9]] | B | LGALS9 activity raises ADGRF1's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.19× lower at baseline in the lines without LGALS9 | 0.056 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises ADGRF1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.15× lower at baseline in the lines without POU5F1B | 0.059 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[IL22RA1]] | B | IL22RA1 activity raises ADGRF1's level | lines that do not express IL22RA1 (17) vs lines expressing it (33) | 3.24× lower at baseline in the lines without IL22RA1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SH2D4A, GOLT1A, ARHGEF5 |
| [[LMO7]] | B | LMO7 activity raises ADGRF1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.98× lower at baseline in the lines without LMO7 | 0.060 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises ADGRF1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without EPS8L1 | 0.061 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[JUP]] | B | JUP activity raises ADGRF1's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.49× lower at baseline in the lines without JUP | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ATP8B1]] | B | ATP8B1 activity raises ADGRF1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.18× lower at baseline in the lines without ATP8B1 | 0.073 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[RBPMS]] | B | RBPMS activity raises ADGRF1's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 2.65× lower at baseline in the lines without RBPMS | 0.075 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |

### Downstream of this gene

*168 arrows, 168 of them with an alert ⚠; grade A 0, B 64, C 104. Shown: the 12 strongest; 156 more arrows (156 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | ADGRF1 activity raises FAM83E's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.14× lower at baseline in the lines without ADGRF1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[JUP]] | B | ADGRF1 activity raises JUP's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.51× lower at baseline in the lines without ADGRF1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[MUC20]] | B | ADGRF1 activity raises MUC20's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.61× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[IL22RA1]] | B | ADGRF1 activity raises IL22RA1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.40× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[EPS8L1]] | B | ADGRF1 activity raises EPS8L1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.29× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ELF3-AS1]] | B | ADGRF1 activity raises ELF3-AS1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[SLC44A3]] | B | ADGRF1 activity raises SLC44A3's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.71× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[TNFRSF21]] | B | ADGRF1 activity raises TNFRSF21's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 5.37× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[LINC01504]] | B | ADGRF1 activity raises LINC01504's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.14× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[SLC37A1]] | B | ADGRF1 activity raises SLC37A1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.71× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[LGALS9]] | B | ADGRF1 activity raises LGALS9's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ATP1B1]] | B | ADGRF1 activity raises ATP1B1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.51× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.806). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 55.0); signed map (59.3, 4.8). **Vector** length 97.5, 46.5% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.55 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor F1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:46,997,708-47,042,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hGPCR36, PGR19; previously GPR110 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily F; SEA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T601](https://www.uniprot.org/uniprotkb/Q5T601) (Adhesion G protein-coupled receptor F1):

> Adhesion G protein-coupled receptor (aGPCR) for N-docosahexaenoylethanolamine (synaptamide), an omega-3 fatty acid lipid highly enriched in the brain. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. ADGRF1 is coupled to G(s) G proteins and mediates activation of adenylate cyclase activity. Also able to couple to G(q), G(i) and G(12)/G(13) G …

**Summary**, from NCBI Gene [266977](https://www.ncbi.nlm.nih.gov/gene/266977):

> Enables G protein-coupled receptor activity. Involved in adenylate cyclase-activating G protein-coupled receptor signaling pathway. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18990) · Entrez [266977](https://www.ncbi.nlm.nih.gov/gene/266977) · UniProt [Q5T601](https://www.uniprot.org/uniprotkb/Q5T601) · Ensembl [ENSG00000153292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153292)

## Data

Gene col 7712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7712); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7712]; `tensor/DDL_lfc|DDL_z.npy` [7712]; `embed/gene_vectors.npy` [7712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7712 or target_col == 7712). Every well: [[ADGRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
