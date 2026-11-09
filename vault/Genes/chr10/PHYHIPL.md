---
symbol: "PHYHIPL"
type: "gene"
col: 9121
ensembl_id: "ENSG00000165443"
name: "phytanoyl-CoA 2-hydroxylase interacting protein like"
location: "10q21.1"
module: 27
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 11
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 22
direction_downstream: 40
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PHYHIPL

*phytanoyl-CoA 2-hydroxylase interacting protein like* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.46× (z +9.4, q 3e-18, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +9.1, q 3e-17, up in 1 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.0931×; ⚠ toxic; transcription drop); [[Daptomycin (drug)]] 5 µM in 1 line (HepG2/C3A 0.190×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMST]] (+0.70, fdr 1e-05), [[SMOC2]] (+0.67, fdr 1e-05), [[A1CF]] (+0.66, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[JAKMIP2-AS1]] → it (grade C ⚠); 40 go from it, the strongest it → [[LINC01980]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.46×** | +9.4 | 3e-18 | 1/4 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +9.1 | 3e-17 | 1/5 (NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +7.5 | 1e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +6.1 | 1e-07 | 2/4 (NCI-H2030, SW480) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +6.0 | 2e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.42×** | +5.6 | 2e-06 | 3/6 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.84×** | +5.5 | 3e-06 | 3/6 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.88×** | +5.1 | 2e-05 | 2/6 (SW480, HepG2/C3A) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.95×** | +5.0 | 3e-05 | 4/6 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **2.20×** | +4.9 | 6e-05 | 2/5 (SW480, HepG2/C3A) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +4.7 | 1e-04 | 3/6 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.03×** | +4.6 | 2e-04 | 2/6 (SW480, HepG2/C3A) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **2.06×** | +4.5 | 3e-04 | 2/7 (SW480, HepG2/C3A) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +4.2 | 0.001 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.43×** | +4.2 | 0.001 | 1/4 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.77×** | +3.8 | 0.006 | 2/6 (SW480, HepG2/C3A) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.81×** | +3.7 | 0.006 | 2/4 (SW480, HepG2/C3A) | all doses, stronger at high dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.74×** | +3.6 | 0.009 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.16×** | +3.6 | 0.009 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.0931×; ⚠ toxic; transcription drop); [[Daptomycin (drug)]] 5 µM in 1 line (HepG2/C3A 0.190×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.05 µM |  | 0.609× | -3.3 | 0.38 | 0/6 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.626× | -3.1 | 0.38 | 0/6 | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.604× | -3.1 | 0.38 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.0 | 4 | 1 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 4.12× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0931× (z -10.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.190× (z -9.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.979 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMST]] | +0.70 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[A1CF]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[B3GAT1-DT]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[HS3ST5]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SERPINF1]] | +0.64 | +0.64 / +0.28 | both halves | 3e-04 | **novel candidate** |
| [[NOTUM]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[RUNX1T1]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ST18]] | +0.63 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[JAKMIP2-AS1]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises PHYHIPL's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without JAKMIP2-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises PHYHIPL's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without LINC00491 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises PHYHIPL's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.16× lower at baseline in the lines without RUNX1T1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises PHYHIPL's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without TFF3 | 0.018 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises PHYHIPL's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.07× lower at baseline in the lines without POU6F2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | ST18 activity raises PHYHIPL's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without ST18 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises PHYHIPL's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without GABRG2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises PHYHIPL's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.51× lower at baseline in the lines without LGR5 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[BMP5]] | C | BMP5 activity raises PHYHIPL's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 2.46× lower at baseline in the lines without BMP5 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[F5]] | C | F5 activity raises PHYHIPL's level | lines that do not express F5 (39) vs lines expressing it (11) | 3.34× lower at baseline in the lines without F5 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises PHYHIPL's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without SERPINF1 | 0.062 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[FGL1]] | C | FGL1 activity raises PHYHIPL's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.59× lower at baseline in the lines without FGL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 12, C 28. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01980]] | B | PHYHIPL activity raises LINC01980's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.29× lower at baseline in the lines without PHYHIPL | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[LINC01091]] | B | PHYHIPL activity raises LINC01091's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 4.77× lower at baseline in the lines without PHYHIPL | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[LINC02466]] | B | PHYHIPL activity raises LINC02466's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.83× lower at baseline in the lines without PHYHIPL | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[FGD3]] | B | PHYHIPL activity raises FGD3's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.28× lower at baseline in the lines without PHYHIPL | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[LINC01170]] | B | PHYHIPL activity raises LINC01170's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.36× lower at baseline in the lines without PHYHIPL | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[PSD2]] | B | PHYHIPL activity raises PSD2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.70× lower at baseline in the lines without PHYHIPL | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[SOBP]] | B | PHYHIPL activity raises SOBP's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 4.59× lower at baseline in the lines without PHYHIPL | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[ATL1]] | B | PHYHIPL activity raises ATL1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.92× lower at baseline in the lines without PHYHIPL | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[CNTNAP2]] | B | PHYHIPL activity raises CNTNAP2's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without PHYHIPL | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[F10]] | B | PHYHIPL activity raises F10's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.04× lower at baseline in the lines without PHYHIPL | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[DIP2C-AS1]] | B | PHYHIPL activity raises DIP2C-AS1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.55× lower at baseline in the lines without PHYHIPL | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[TSPEAR]] | B | PHYHIPL activity raises TSPEAR's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.68× lower at baseline in the lines without PHYHIPL | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 43.0); signed map (62.5, 17.4). **Vector** length 28.1, 11.3% of its response variance represented; |z| ≥ 3 in 179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phytanoyl-CoA 2-hydroxylase interacting protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:59,176,643-59,247,774 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1796, Em:AC025038.1 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FC7](https://www.uniprot.org/uniprotkb/Q96FC7) (Phytanoyl-CoA hydroxylase-interacting protein-like):

> May play a role in the development of the central system.

**Summary**, from NCBI Gene [84457](https://www.ncbi.nlm.nih.gov/gene/84457):

> Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29378) · Entrez [84457](https://www.ncbi.nlm.nih.gov/gene/84457) · UniProt [Q96FC7](https://www.uniprot.org/uniprotkb/Q96FC7) · Ensembl [ENSG00000165443](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165443)

## Data

Gene col 9121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9121); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9121]; `tensor/DDL_lfc|DDL_z.npy` [9121]; `embed/gene_vectors.npy` [9121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9121 or target_col == 9121). Every well: [[PHYHIPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHYHIPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
