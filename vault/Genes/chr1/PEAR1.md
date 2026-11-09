---
symbol: "PEAR1"
type: "gene"
col: 11951
ensembl_id: "ENSG00000187800"
name: "platelet endothelial aggregation receptor 1"
location: "1q23.1"
module: 34
arm: "+"
pooled_cpm: 8.72
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PEAR1

*platelet endothelial aggregation receptor 1* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.21× (z +6.3, q 1e-07, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.18× (z +4.6, q 7e-04, up in 6 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (Hs 766T 0.0872×, CFPAC-1 0.170×, AsPC-1 0.258×, NCI-H1792 0.195×; ⚠ cell-cycle shift, explains ~19% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.150×, AsPC-1 0.210×, Hs 766T 0.177×; ⚠ cell-cycle shift, explains ~92% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0652×, AsPC-1 0.277×); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.121×, AsPC-1 0.249×); [[Trametinib (drug)]] 5 µM in 1 line (AsPC-1 0.247×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESAM]] (+0.66, fdr 1e-05), [[PLEK2]] (+0.62, fdr 1e-05), [[TNFRSF25]] (+0.61, fdr 1e-05); moves opposite to [[MBNL3]] (-0.46, fdr 1e-04), [[GTF2I]] (-0.45, fdr 2e-04), [[RARRES1]] (-0.45, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LANCL3]] → it (grade B ⚠); 7 go from it, the strongest it → [[GIPR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +6.3 | 1e-07 | 1/9 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +4.8 | 4e-04 | 2/12 (hTERT-HPNE, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.18×** | +4.6 | 7e-04 | 6/22 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.2 | 0.003 | 4/11 (AsPC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.96×** | +4.0 | 0.006 | 6/24 (AsPC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.006 | 7/24 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.35×** | +3.7 | 0.016 | 3/17 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.027 | 7/24 (KATO III, PANC-1, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.81×** | +3.5 | 0.027 | 3/24 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +3.4 | 0.045 | 6/24 (A-172, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.068 | 4/23 (AsPC-1, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.068 | 1/24 (SW480) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.46×** | +3.2 | 0.068 | 5/24 (SW 900, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.44× | +3.0 | 0.10 | 3/18 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (Hs 766T 0.0872×, CFPAC-1 0.170×, AsPC-1 0.258×, NCI-H1792 0.195×; ⚠ cell-cycle shift, explains ~19% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.150×, AsPC-1 0.210×, Hs 766T 0.177×; ⚠ cell-cycle shift, explains ~92% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (Hs 766T 0.0652×, AsPC-1 0.277×); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.121×, AsPC-1 0.249×); [[Trametinib (drug)]] 5 µM in 1 line (AsPC-1 0.247×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.681× | -3.2 | 0.41 | 7/24 (hTERT-HPNE, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | 0.683× | -3.2 | 0.41 | 6/24 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.672× | -3.1 | 0.41 | 5/24 (AsPC-1, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 88.2 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0777× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.247× (z -9.9) |
| [[Hs 766T (line)]] | wt | 75.6 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0872× (z -20.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0652× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 50.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -15.6) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.337× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0803× (z -10.8) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 5.60 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0804× (z -9.4) |
| [[A549 (line)]] | wt | 2.72 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +10.5) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 2.27 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 0.05 µM 0.0540× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -8.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[PANC-1 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.23× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.799 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESAM]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 | STRING 451 |
| [[PLEK2]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TNFRSF25]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KISS1]] | +0.61 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[ATG9B]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SIGIRR]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[DHRS9]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.58 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[KLC3]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ADAM8]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SLC9A3R2]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL3]] | -0.46 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[GTF2I]] | -0.45 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[RARRES1]] | -0.45 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TNS3]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[NAF1]] | -0.45 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[PAXBP1]] | -0.44 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[DPY19L1P1]] | -0.44 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[TBC1D5]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[HNF4G]] | -0.44 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[PON2]] | -0.43 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[TMEM123]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LANCL3]] | B | LANCL3 activity raises PEAR1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.64× lower at baseline in the lines without LANCL3 | 0.051 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[IL2RG]] | B | IL2RG activity raises PEAR1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without IL2RG | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[ZNF185]] | B | ZNF185 activity raises PEAR1's level | lines that do not express ZNF185 (15) vs lines expressing it (35) | 1.87× lower at baseline in the lines without ZNF185 | 0.068 | ⚠ within organs, on part of the lines; also absent: HTR1D, KLF5, IL18 |
| [[NLRP1]] | B | NLRP1 activity raises PEAR1's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without NLRP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[DHRS9]] | C | DHRS9 activity raises PEAR1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 3.70× lower at baseline in the lines without DHRS9 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises PEAR1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without TINAGL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[PRSS3]] | C | PRSS3 activity raises PEAR1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without PRSS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR; co-absent with the target |
| [[RAC2]] | C | RAC2 activity raises PEAR1's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.61× lower at baseline in the lines without RAC2 | 0.043 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR; co-absent with the target |
| [[KISS1]] | C | KISS1 activity raises PEAR1's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without KISS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GIPR]] | B | PEAR1 activity raises GIPR's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without PEAR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[PLEKHM1]] | B | PEAR1 activity raises PLEKHM1's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without PEAR1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[KCNN4]] | B | PEAR1 activity raises KCNN4's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without PEAR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[ZNF185]] | B | PEAR1 activity raises ZNF185's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without PEAR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[PIGH]] | B | PEAR1 activity lowers PIGH's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 1.09× higher at baseline in the lines without PEAR1 | 0.090 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3 |
| [[RAC2]] | C | PEAR1 activity raises RAC2's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without PEAR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3; co-absent with the target |
| [[TINAGL1]] | C | PEAR1 activity raises TINAGL1's level | lines that do not express PEAR1 (24) vs lines expressing it (26) | 4.08× lower at baseline in the lines without PEAR1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LY75, AFAP1L2, PRSS3; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 60.6); signed map (-1.0, 44.9). **Vector** length 64.9, 16.7% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | platelet endothelial aggregation receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,893,698-156,916,429 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JEDI, FLJ00193; previously MEGF12 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VY43](https://www.uniprot.org/uniprotkb/Q5VY43) (Platelet endothelial aggregation receptor 1):

> Required for SVEP1-mediated platelet activation, via its interaction with SVEP1 and subsequent activation of AKT/mTOR signaling. May be involved in the early stages of hematopoiesis (By similarity).

**Summary**, from NCBI Gene [375033](https://www.ncbi.nlm.nih.gov/gene/375033):

> PEAR1 is a platelet receptor that signals upon the formation of platelet-platelet contacts independent of platelet activation and secondary to platelet aggregation (Nanda et al., 2005 [PubMed 15851471]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:33631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33631) · Entrez [375033](https://www.ncbi.nlm.nih.gov/gene/375033) · UniProt [Q5VY43](https://www.uniprot.org/uniprotkb/Q5VY43) · Ensembl [ENSG00000187800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187800)

## Data

Gene col 11951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11951); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11951]; `tensor/DDL_lfc|DDL_z.npy` [11951]; `embed/gene_vectors.npy` [11951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11951 or target_col == 11951). Every well: [[PEAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
