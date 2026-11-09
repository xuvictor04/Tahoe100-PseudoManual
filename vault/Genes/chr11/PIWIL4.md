---
symbol: "PIWIL4"
type: "gene"
col: 5584
ensembl_id: "ENSG00000134627"
name: "piwi like RNA-mediated gene silencing 4"
location: "11q21"
module: 73
arm: "+"
pooled_cpm: 17.79
n_lines_expressing: 39
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# PIWIL4

*piwi like RNA-mediated gene silencing 4* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +5.1, q 2e-04, up in 15 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 2.46×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.532× (z -8.3, q 6e-14, down in 20 of 36 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.571× (z -7.4, q 4e-11, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEPH]] (+0.61, fdr 7e-06), [[FUT4]] (+0.58, fdr 1e-05, ⚠ same locus), [[SLC6A20]] (+0.57, fdr 1e-05), [[SPON1]] (+0.57, fdr 1e-05); moves opposite to [[TMEM9]] (-0.51, fdr 3e-05), [[ZNF483]] (-0.49, fdr 9e-05), [[SNRPN]] (-0.48, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[EVA1C]] → it (grade B ⚠); 3 go from it, the strongest it → [[EVA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5584.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (PANC-1 2.46×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.1 | 2e-04 | 15/34 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 2e-04 | 14/37 (SW1417, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.29× | +3.4 | 0.12 | 10/36 (A549, SW480, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.532×** | -8.3 | 6e-14 | 20/36 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.571×** | -7.4 | 4e-11 | 23/36 (HT-29, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.581×** | -7.1 | 2e-10 | 25/36 (HT-29, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -6.7 | 4e-09 | 19/34 (LoVo, J82, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.638×** | -5.9 | 4e-07 | 20/35 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.730×** | -5.9 | 5e-07 | 17/36 (LoVo, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -4.6 | 3e-04 | 14/35 (KATO III, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.795×** | -4.2 | 0.002 | 16/35 (LoVo, HT-29, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.737×** | -4.0 | 0.004 | 13/36 (LoVo, KATO III, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.574×** | -3.8 | 0.008 | 9/34 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.753×** | -3.7 | 0.010 | 14/36 (LoVo, KATO III, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.759×** | -3.5 | 0.024 | 12/33 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.040 | 12/34 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.786×** | -3.2 | 0.065 | 8/34 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -3.1 | 0.068 | 8/33 (LOX-IMVI, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 84.8 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0432× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.190× (z -11.9) |
| [[LoVo (line)]] | wt | 56.1 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.418× (z -9.5) |
| [[PANC-1 (line)]] | alt | 21.5 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.319× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -9.4) |
| [[HT-29 (line)]] | alt | 79.1 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.142× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.190× (z -8.8) |
| [[A-172 (line)]] | wt | 9.71 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0922× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 7.72 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0799× (z -8.6) |
| [[HS-578T (line)]] | alt | 5.07 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0671× (z -9.8) |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0917× (z -9.4) |
| [[SW48 (line)]] | wt | 34.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -9.1) |
| [[SW480 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -8.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-427 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEPH]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FUT4]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 | STRING 475; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SLC6A20]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SPON1]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[LINC01956]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF800]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DSG4]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TPTEP1-1]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[FAM3D]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SEPTIN9-DT]] | +0.53 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[MYO7B]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM9]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF483]] | -0.49 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[SNRPN]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TRAPPC2]] | -0.47 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[STARD3NL]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SEPTIN6]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[RAB6B]] | -0.45 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[MED30]] | -0.44 | -0.45 / -0.31 | both halves | 2e-04 | pathway: Epigenetic regulation of gene expression |
| [[BCL9]] | -0.43 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[ZC4H2]] | -0.43 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[ARRB2]] | -0.42 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[RNF212]] | -0.42 | -0.37 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1C]] | B | EVA1C activity raises PIWIL4's level | lines that do not express EVA1C (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without EVA1C | 0.023 | ⚠ within organs, on part of the lines; also absent: PI3, ENSG00000260877, CYB5R2 |
| [[TPRXL]] | B | TPRXL activity raises PIWIL4's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.60× lower at baseline in the lines without TPRXL | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[LINC01133]] | B | LINC01133 activity raises PIWIL4's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without LINC01133 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1 |
| [[IL20RA]] | B | IL20RA activity raises PIWIL4's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 3.71× lower at baseline in the lines without IL20RA | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[GPX2]] | B | GPX2 activity strengthens PIWIL4's drug response | lines that do not express GPX2 (28) vs lines expressing it (9) | the lines without GPX2 respond 0.55× as strongly (z diff +1.33); rises at some drug-doses, falls at others (43% from rises): Digitoxin 5 µM: 0.56x vs 0.42x (z diff +2.3); Ixazomib citrate 5 µM: 0.48x vs 0.39x (z diff +2.2); Filgotinib 5 µM: 1.39x vs 1.83x (z diff +2.0) | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[MYO7B]] | B | MYO7B activity raises PIWIL4's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.43× lower at baseline in the lines without MYO7B | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[FUT4]] | C | FUT4 activity raises PIWIL4's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 4.32× lower at baseline in the lines without FUT4 | 0.012 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3; co-absent with the target |
| [[KRT20]] | C | KRT20 activity raises PIWIL4's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 3.61× lower at baseline in the lines without KRT20 | 0.099 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1C]] | B | PIWIL4 activity raises EVA1C's level | lines that do not express PIWIL4 (11) vs lines expressing it (39) | 3.32× lower at baseline in the lines without PIWIL4 | 0.010 | ⚠ within organs, on part of the lines; also absent: FUT4, CTSZ, ARHGAP23 |
| cells under [[Belumosudil (drug)]] 5 µM | B | PIWIL4 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express PIWIL4 (11) vs lines expressing it (37) | the lines without PIWIL4: 0.68× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: FUT4, CTSZ, ARHGAP23 |
| [[FUT4]] | C | PIWIL4 activity raises FUT4's level | lines that do not express PIWIL4 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without PIWIL4 | 0.007 | ⚠ within organs, on part of the lines; also absent: FUT4, CTSZ, ARHGAP23; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.4, 49.6); signed map (66.3, 7.3). **Vector** length 73.5, 15.5% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.7 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -7.4 |
|  | [[NG25 (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | piwi like RNA-mediated gene silencing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,543,840-94,621,421 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36156, HIWI2, Miwi2 |
| Gene groups (HGNC) | Piwi like RNA-mediated gene silencing family |
| Reactome | 5 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Regulation of endogenous retroelements by Piwi-interacting RNAs (piRNAs); Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3Z4](https://www.uniprot.org/uniprotkb/Q7Z3Z4) (Piwi-like protein 4):

> Plays a central role during spermatogenesis by repressing transposable elements and preventing their mobilization, which is essential for the germline integrity (By similarity). Acts via the piRNA metabolic process, which mediates the repression of transposable elements during meiosis by forming complexes composed of piRNAs and Piwi proteins (By similarity). The PIWIL4-piRNA pathway acts in the nucleus and mediates silencing of active transposons: engages with nascent transposable element …

**Summary**, from NCBI Gene [143689](https://www.ncbi.nlm.nih.gov/gene/143689):

> PIWIL4 belongs to the Argonaute family of proteins, which function in development and maintenance of germline stem cells (Sasaki et al., 2003 [PubMed 12906857]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18444) · Entrez [143689](https://www.ncbi.nlm.nih.gov/gene/143689) · UniProt [Q7Z3Z4](https://www.uniprot.org/uniprotkb/Q7Z3Z4) · Ensembl [ENSG00000134627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134627)

## Data

Gene col 5584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5584); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5584]; `tensor/DDL_lfc|DDL_z.npy` [5584]; `embed/gene_vectors.npy` [5584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5584 or target_col == 5584). Every well: [[PIWIL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIWIL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
