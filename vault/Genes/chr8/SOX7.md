---
symbol: "SOX7"
type: "gene"
col: 10045
ensembl_id: "ENSG00000171056"
name: "SRY-box transcription factor 7"
location: "8p23.1"
module: 19
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 15
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SOX7

*SRY-box transcription factor 7* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.52× (z +8.5, q 8e-15, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.74× (z +4.3, q 0.002, up in 2 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.510× (z -4.4, q 0.005, down in 4 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0817×, NCI-H460 0.0886×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.0848×, Panc 03.27 0.209×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.0796×, Hs 766T 0.154×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (Hs 766T 0.125×, NCI-H460 0.118×); [[TAK-901 (drug)]] 5 µM in 1 line (Hs 766T 0.0561×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOK5]] (+0.59, fdr 1e-05), [[RNF182]] (+0.59, fdr 3e-05), [[LINC02742]] (+0.54, fdr 4e-05); moves opposite to [[KRT5]] (-0.40, fdr 4e-04), [[CA5BP1-1]] (-0.39, fdr 1e-04), [[CCDC171]] (-0.37, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLITRK4]] → it (grade C ⚠); 2 go from it, the strongest it → [[MN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.52×** | +8.5 | 8e-15 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.09×** | +4.8 | 4e-04 | 0/7 | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.93×** | +4.6 | 7e-04 | 0/7 | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.74×** | +4.3 | 0.002 | 2/7 (HOP62, AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.67×** | +3.5 | 0.061 | 3/7 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.061 | 2/11 (NCI-H23, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.3 | 0.061 | 2/9 (NCI-H460, AsPC-1) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.3 | 0.061 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.061 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.061 | 0/8 | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.59×** | +3.2 | 0.061 | 1/5 (A-427) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.11×** | +3.2 | 0.065 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +3.2 | 0.067 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +3.0 | 0.099 | 1/10 (A-427) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10045.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.0817×, NCI-H460 0.0886×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.0848×, Panc 03.27 0.209×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Panc 03.27 0.0796×, Hs 766T 0.154×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (Hs 766T 0.125×, NCI-H460 0.118×); [[TAK-901 (drug)]] 5 µM in 1 line (Hs 766T 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.510×** | -4.4 | 0.005 | 4/10 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.614× | -3.2 | 0.37 | 0/10 | inconsistent across doses |  |
| [[Pimozide (drug)]] 5 µM |  | 0.648× | -3.1 | 0.37 | 0/10 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 190 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0817× (z -22.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0848× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 8.97 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0796× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.507× (z -9.2) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.904 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOK5]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[RNF182]] | +0.59 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[LINC02742]] | +0.54 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[PRICKLE1]] | +0.53 | +0.46 / +0.45 | both halves | 3e-05 | pathway: Signaling by WNT |
| [[MN1]] | +0.52 | +0.53 / +0.42 | both halves | 4e-05 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ESM1]] | +0.50 | +0.64 / +0.36 | both halves | 1e-04 |  |
| [[SLC14A1]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SIM1]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[PTPN20]] | +0.49 | +0.49 / +0.21 | both halves | 7e-04 |  |
| [[ECSCR]] | +0.49 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[WNT7A]] | +0.48 | +0.37 / +0.48 | both halves | 8e-05 | pathway: Signaling by WNT |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT5]] | -0.40 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[CA5BP1-1]] | -0.39 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CCDC171]] | -0.37 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[GTPBP6]] | -0.36 | -0.35 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLITRK4]] | C | SLITRK4 activity raises SOX7's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 1.93× lower at baseline in the lines without SLITRK4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises SOX7's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 2.43× lower at baseline in the lines without LINC02742 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises SOX7's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 4.76× lower at baseline in the lines without KRT5 | 0.052 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises SOX7's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.18× lower at baseline in the lines without SIM1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[COL4A6]] | C | COL4A6 activity raises SOX7's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.98× lower at baseline in the lines without COL4A6 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[PLAT]] | C | PLAT activity raises SOX7's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without PLAT | 0.096 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MN1]] | B | SOX7 activity raises MN1's level | lines that do not express SOX7 (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without SOX7 | 0.097 | ⚠ within organs, on part of the lines; also absent: COL4A6, MMRN1, PTGIS |
| [[PLAT]] | C | SOX7 activity raises PLAT's level | lines that do not express SOX7 (35) vs lines expressing it (15) | 2.87× lower at baseline in the lines without SOX7 | 0.034 | ⚠ within organs, on part of the lines; also absent: COL4A6, MMRN1, PTGIS; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.414). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 19.2); signed map (42.8, 47.6). **Vector** length 34.4, 11.5% of its response variance represented; |z| ≥ 3 in 220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +1.4 | +3.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.4 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.8 | +0.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -4.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:10,723,768-10,730,511 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SRY-box transcription factors |
| Reactome | 3 pathways, smallest: Deactivation of the beta-catenin transactivating complex; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT81](https://www.uniprot.org/uniprotkb/Q9BT81) (Transcription factor SOX-7):

> Binds to and activates the CDH5 promoter, hence plays a role in the transcriptional regulation of genes expressed in the hemogenic endothelium and blocks further differentiation into blood precursors (By similarity). May be required for the survival of both hematopoietic and endothelial precursors during specification (By similarity). Competes with GATA4 for binding and activation of the FGF3 promoter (By similarity). Represses Wnt/beta-catenin-stimulated transcription, probably by targeting …

**Summary**, from NCBI Gene [83595](https://www.ncbi.nlm.nih.gov/gene/83595):

> This gene encodes a member of the SOX (SRY-related HMG-box) family of transcription factors involved in the regulation of embryonic development and in the determination of the cell fate. The encoded protein may act as a transcriptional regulator after forming a protein complex with other proteins. The protein may play a role in tumorigenesis. A similar protein in mice is involved in the regulation of the wingless-type MMTV integration site family (Wnt) pathway. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18196) · Entrez [83595](https://www.ncbi.nlm.nih.gov/gene/83595) · UniProt [Q9BT81](https://www.uniprot.org/uniprotkb/Q9BT81) · Ensembl [ENSG00000171056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171056)

## Data

Gene col 10045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10045); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10045]; `tensor/DDL_lfc|DDL_z.npy` [10045]; `embed/gene_vectors.npy` [10045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10045 or target_col == 10045). Every well: [[SOX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
