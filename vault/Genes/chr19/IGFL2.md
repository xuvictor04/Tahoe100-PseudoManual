---
symbol: "IGFL2"
type: "gene"
col: 12929
ensembl_id: "ENSG00000204866"
name: "IGF like family member 2"
location: "19q13.32"
module: 73
arm: "+"
pooled_cpm: 5.66
n_lines_expressing: 12
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 27
direction_downstream: 34
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# IGFL2

*IGF like family member 2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.53× (z +9.0, q 9e-17, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.77× (z +6.0, q 3e-07, up in 5 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0277×, LoVo 0.130×, AsPC-1 0.0353×, C32 0.240×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0931×, LS 180 0.0603×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 0.117×, LS 180 0.0728×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 0.115×, LS 180 0.125×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.244×, LS 180 0.211×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSG4]] (+0.75, fdr 7e-06), [[CALB1]] (+0.72, fdr 7e-06), [[SLC6A20]] (+0.71, fdr 1e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[MMP28]] → it (grade B ⚠); 34 go from it, the strongest it → [[ITPK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +9.0 | 9e-17 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +8.6 | 2e-15 | 2/7 (NCI-H2347, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +6.5 | 1e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +6.0 | 3e-07 | 5/10 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +5.5 | 5e-06 | 6/10 (LoVo, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +5.0 | 5e-05 | 1/10 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.4 | 9e-04 | 1/9 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **3.00×** | +4.3 | 0.001 | 4/9 (AsPC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.92×** | +4.2 | 0.002 | 0/2 | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.73×** | +3.9 | 0.005 | 4/8 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.023 | 5/10 (HCT15, LoVo, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.4 | 0.034 | 0/10 | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.044 | 3/10 (HCT15, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.048 | 2/10 (LoVo, NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.95×** | +3.1 | 0.068 | 2/10 (AsPC-1, LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.075 | 1/10 (LoVo) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.50×** | +3.0 | 0.082 | 1/10 (NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12929.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0277×, LoVo 0.130×, AsPC-1 0.0353×, C32 0.240×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.0931×, LS 180 0.0603×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 0.117×, LS 180 0.0728×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 0.115×, LS 180 0.125×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.244×, LS 180 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 5 µM |  | 0.466× | -3.0 | 0.64 | 2/10 (LS 180, LoVo) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 42.9 | 1 | 9 (6 ⚠) | [[Selinexor (drug)]] 5 µM 3.34× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0931× (z -12.8) |
| [[LS 180 (line)]] | wt | 104 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0277× (z -22.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0603× (z -12.4) |
| [[C32 (line)]] | wt | 20.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0353× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.730 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG4]] | +0.75 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[CALB1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.71 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.70 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[FAM3D]] | +0.68 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[LINC02582]] | +0.67 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[TPTEP1-1]] | +0.66 | +0.78 / +0.46 | both halves | 2e-05 |  |
| [[SPON1]] | +0.66 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SERPINB5]] | +0.65 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[DSG3]] | +0.65 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[CADPS]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 1, C 26. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP28]] | B | MMP28 activity raises IGFL2's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without MMP28 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[DSG4]] | C | DSG4 activity raises IGFL2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 9.49× lower at baseline in the lines without DSG4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises IGFL2's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.94× lower at baseline in the lines without LINC02582 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises IGFL2's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 4.05× lower at baseline in the lines without SPON1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[REG4]] | C | REG4 activity raises IGFL2's level | lines that do not express REG4 (43) vs lines expressing it (7) | 4.56× lower at baseline in the lines without REG4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises IGFL2's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without LINC00589 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[LINC01956]] | C | LINC01956 activity raises IGFL2's level | lines that do not express LINC01956 (38) vs lines expressing it (12) | 1.81× lower at baseline in the lines without LINC01956 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01440, SYT4, LINC03000; co-absent with the target |
| [[C4BPB]] | C | C4BPB activity raises IGFL2's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.98× lower at baseline in the lines without C4BPB | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises IGFL2's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.48× lower at baseline in the lines without SERPINB5 | 0.031 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises IGFL2's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.01× lower at baseline in the lines without EPHA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[XYLT1]] | C | XYLT1 activity raises IGFL2's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without XYLT1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises IGFL2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.17× lower at baseline in the lines without PKP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 12, C 22. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPK1]] | B | IGFL2 activity raises ITPK1's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without IGFL2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[GRHL3]] | B | IGFL2 activity raises GRHL3's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without IGFL2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[SLC9A2]] | B | IGFL2 activity raises SLC9A2's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without IGFL2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[NOSTRIN]] | B | IGFL2 activity raises NOSTRIN's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.61× lower at baseline in the lines without IGFL2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[INPP1]] | B | IGFL2 activity raises INPP1's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.25× lower at baseline in the lines without IGFL2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[ITPK1]] | B | IGFL2 activity weakens ITPK1's drug response | lines that do not express IGFL2 (34) vs lines expressing it (11) | the lines without IGFL2 respond 1.83× as strongly (z diff -1.17); strongest at Panobinostat 5 µM: 1.47x vs 0.75x (z diff -5.2) | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33; target measured in part of the lines; artifact flags |
| [[AMN]] | B | IGFL2 activity raises AMN's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 1.92× lower at baseline in the lines without IGFL2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[B4GALNT3]] | B | IGFL2 activity raises B4GALNT3's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 3.25× lower at baseline in the lines without IGFL2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[HTR1D]] | B | IGFL2 activity raises HTR1D's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 1.80× lower at baseline in the lines without IGFL2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[MUC12]] | B | IGFL2 activity raises MUC12's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.19× lower at baseline in the lines without IGFL2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[SDCBP2]] | B | IGFL2 activity raises SDCBP2's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.53× lower at baseline in the lines without IGFL2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[LOXL1-AS1]] | B | IGFL2 activity lowers LOXL1-AS1's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 1.69× higher at baseline in the lines without IGFL2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.9, 50.5); signed map (65.6, 8.0). **Vector** length 39.3, 14.1% of its response variance represented; |z| ≥ 3 in 255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +1.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.3 | +1.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.0 | +4.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.6 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -0.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -3.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -0.6 | -2.9 |
|  | [[Paclitaxel (drug)]] 5 µM |  | -0.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | IGF like family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,143,106-46,161,298 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ645 |
| Gene groups (HGNC) | IGF like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWQ7](https://www.uniprot.org/uniprotkb/Q6UWQ7) (Insulin growth factor-like family member 2):

> Potential ligand of the IGFLR1 cell membrane receptor.

**Summary**, from NCBI Gene [147920](https://www.ncbi.nlm.nih.gov/gene/147920):

> IGFL2 belongs to the insulin-like growth factor (IGF; see MIM 147440) family of signaling molecules that play critical roles in cellular energy metabolism and in growth and development, especially prenatal growth (Emtage et al., 2006 [PubMed 16890402]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:32929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32929) · Entrez [147920](https://www.ncbi.nlm.nih.gov/gene/147920) · UniProt [Q6UWQ7](https://www.uniprot.org/uniprotkb/Q6UWQ7) · Ensembl [ENSG00000204866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204866)

## Data

Gene col 12929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12929); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12929]; `tensor/DDL_lfc|DDL_z.npy` [12929]; `embed/gene_vectors.npy` [12929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12929 or target_col == 12929). Every well: [[IGFL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
