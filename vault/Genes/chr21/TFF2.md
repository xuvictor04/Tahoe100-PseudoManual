---
symbol: "TFF2"
type: "gene"
col: 8307
ensembl_id: "ENSG00000160181"
name: "trefoil factor 2"
location: "21q22.3"
module: 73
arm: "+"
pooled_cpm: 7.36
n_lines_expressing: 11
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 45
direction_downstream: 85
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# TFF2

*trefoil factor 2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.45× (z +8.5, q 8e-15, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.415× (z -3.8, q 0.097, down in 5 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.0306×, KATO III 0.0807×, LS 180 0.0285×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (AsPC-1 0.0180×, KATO III 0.0646×, LS 180 0.0376×); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.125×, AsPC-1 0.0966×); [[Panobinostat (drug)]] 0.5 µM in 1 line (AsPC-1 0.0742×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK10]] (+0.86, fdr 7e-06), [[KLK11]] (+0.84, fdr 7e-06), [[TFF1]] (+0.79, fdr 7e-06, ⚠ same locus), [[NPSR1]] (+0.72, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[DHRS9]] → it (grade C ⚠); 85 go from it, the strongest it → [[PLEKHM1P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.45×** | +8.5 | 8e-15 | 3/5 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.55×** | +8.3 | 4e-14 | 2/4 (KATO III, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +4.7 | 6e-04 | 1/5 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +4.2 | 0.005 | 2/6 (CFPAC-1, Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.44×** | +4.1 | 0.005 | 4/6 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.3 | 0.096 | 1/8 (CFPAC-1) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.95× | +3.0 | 0.19 | 0/8 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 0.0306×, KATO III 0.0807×, LS 180 0.0285×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (AsPC-1 0.0180×, KATO III 0.0646×, LS 180 0.0376×); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.125×, AsPC-1 0.0966×); [[Panobinostat (drug)]] 0.5 µM in 1 line (AsPC-1 0.0742×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.415×** | -3.8 | 0.097 | 5/9 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.462× | -3.6 | 0.10 | 7/8 (AsPC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | 0.486× | -3.2 | 0.25 | 5/9 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.486× | -3.1 | 0.25 | 1/9 (CFPAC-1) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.494× | -3.0 | 0.25 | 2/9 (AsPC-1, LS 180) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.522× | -3.0 | 0.25 | 3/9 (AsPC-1, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 35.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0306× (z -18.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0180× (z -15.2) |
| [[KATO III (line)]] | alt | 160 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0646× (z -12.5) |
| [[LS 180 (line)]] | wt | 9.21 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0285× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0376× (z -10.5) |
| [[A-172 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK10]] | +0.86 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[KLK11]] | +0.84 | +0.83 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TFF1]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | ⚠ same locus (11.3 kb, same strand: neighbours can correlate without regulation) |
| [[NPSR1]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[CTSE]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 | STRING 421 |
| [[HS3ST1]] | +0.70 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[CEACAM6]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB5]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[CALB1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[REG4]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 | STRING 643 |
| [[MUC2]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 | STRING 646 |
| [[FGFBP1]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 0, C 45. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DHRS9]] | C | DHRS9 activity raises TFF2's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 5.84× lower at baseline in the lines without DHRS9 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises TFF2's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 1.67× lower at baseline in the lines without PHGR1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[PIWIL1]] | C | PIWIL1 activity raises TFF2's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 3.85× lower at baseline in the lines without PIWIL1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises TFF2's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.47× lower at baseline in the lines without MUC6 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[CADPS]] | C | CADPS activity raises TFF2's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.09× lower at baseline in the lines without CADPS | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises TFF2's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.70× lower at baseline in the lines without KLK10 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises TFF2's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.70× lower at baseline in the lines without SERPINB5 | 0.016 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises TFF2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without PKP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises TFF2's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.40× lower at baseline in the lines without CEACAM6 | 0.019 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises TFF2's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 4.21× lower at baseline in the lines without FGFBP1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises TFF2's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.54× lower at baseline in the lines without CEACAM1 | 0.023 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises TFF2's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 2.12× lower at baseline in the lines without SLC14A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*85 arrows, 85 of them with an alert ⚠; grade A 0, B 17, C 68. Shown: the 12 strongest; 73 more arrows (73 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHM1P1]] | B | TFF2 activity raises PLEKHM1P1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 1.93× lower at baseline in the lines without TFF2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[SDCBP2]] | B | TFF2 activity raises SDCBP2's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 5.03× lower at baseline in the lines without TFF2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[FAM83E]] | B | TFF2 activity raises FAM83E's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.51× lower at baseline in the lines without TFF2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[PTK6]] | B | TFF2 activity raises PTK6's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 4.23× lower at baseline in the lines without TFF2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[NOSTRIN]] | B | TFF2 activity raises NOSTRIN's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.44× lower at baseline in the lines without TFF2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | TFF2 activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without TFF2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[VILL]] | B | TFF2 activity raises VILL's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.71× lower at baseline in the lines without TFF2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[EFNB1]] | B | TFF2 activity raises EFNB1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.14× lower at baseline in the lines without TFF2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[KPNA2P3]] | B | TFF2 activity raises KPNA2P3's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.07× lower at baseline in the lines without TFF2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[INPP1]] | B | TFF2 activity raises INPP1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.33× lower at baseline in the lines without TFF2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[VILL]] | B | TFF2 activity strengthens VILL's drug response | lines that do not express TFF2 (22) vs lines expressing it (8) | the lines without TFF2 respond 0.43× as strongly (z diff +1.98); strongest at Idarubicin (hydrochloride) 0.5 µM: 0.61x vs 0.26x (z diff +4.3) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; target measured in part of the lines; artifact flags |
| [[YOD1]] | B | TFF2 activity raises YOD1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without TFF2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.2, 53.6); signed map (68.1, 9.5). **Vector** length 44.1, 22.0% of its response variance represented; |z| ≥ 3 in 213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.7 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.8 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Afatinib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | trefoil factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,346,357-42,350,997 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SML1 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03403](https://www.uniprot.org/uniprotkb/Q03403) (Trefoil factor 2):

> Inhibits gastrointestinal motility and gastric acid secretion. Could function as a structural component of gastric mucus, possibly by stabilizing glycoproteins in the mucus gel through interactions with carbohydrate side chains (By similarity).

**Summary**, from NCBI Gene [7032](https://www.ncbi.nlm.nih.gov/gene/7032):

> Members of the trefoil family are characterized by having at least one copy of the trefoil motif, a 40-amino acid domain that contains three conserved disulfides. They are stable secretory proteins expressed in gastrointestinal mucosa. Their functions are not defined, but they may protect the mucosa from insults, stabilize the mucus layer and affect healing of the epithelium. The encoded protein inhibits gastric acid secretion. This gene and two other related trefoil family member genes are …

**Accessions** — [HGNC:11756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11756) · Entrez [7032](https://www.ncbi.nlm.nih.gov/gene/7032) · UniProt [Q03403](https://www.uniprot.org/uniprotkb/Q03403) · Ensembl [ENSG00000160181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160181)

## Data

Gene col 8307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8307); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8307]; `tensor/DDL_lfc|DDL_z.npy` [8307]; `embed/gene_vectors.npy` [8307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8307 or target_col == 8307). Every well: [[TFF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
