---
symbol: "SEMA6D"
type: "gene"
col: 6088
ensembl_id: "ENSG00000137872"
name: "semaphorin 6D"
location: "15q21.1"
module: 90
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# SEMA6D

*semaphorin 6D* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.74× (z +24.1, q 0e+00, up in 23 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW 900 0.0595×, SHP-77 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.0332×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.114×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.315×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (C32 0.0623×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.79, fdr 7e-06), [[CNBD1]] (+0.78, fdr 7e-06), [[GLRA3]] (+0.76, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[PDZRN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.74×** | +24.1 | 0e+00 | 23/27 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +11.1 | 4e-26 | 25/43 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +11.0 | 4e-26 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +10.1 | 7e-22 | 2/11 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.76×** | +9.9 | 5e-21 | 24/42 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +9.6 | 1e-19 | 12/32 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.4 | 9e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.8 | 7e-10 | 7/42 (NCI-H460, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +6.3 | 2e-08 | 6/28 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.9 | 6e-05 | 15/35 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.0 | 0.003 | 1/19 (LoVo) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.006 | 13/45 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.007 | 4/18 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.008 | 12/41 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.63×** | +3.4 | 0.023 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.031 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.075 | 11/44 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.087 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW 900 0.0595×, SHP-77 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.0332×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.114×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.315×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (C32 0.0623×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 1.80 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 26.4× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0332× (z -19.6) |
| [[C32 (line)]] | wt | 5.95 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0623× (z -8.8) |
| [[LoVo (line)]] | wt | 1.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 1.000 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +10.6) | — |
| [[SW480 (line)]] | alt | 1.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +10.8) | — |
| [[A-172 (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.997 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.827 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.863 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.858 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.993 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.986 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.79 | +0.67 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CNBD1]] | +0.78 | +0.65 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[GLRA3]] | +0.76 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SORCS1]] | +0.73 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[DACH2]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SGCZ]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[DCC]] | +0.72 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[CNTN5]] | +0.72 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[CNTNAP4]] | +0.71 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[LDB2]] | +0.70 | +0.57 / +0.74 | both halves | 9e-06 | **novel candidate** |
| [[USH2A]] | +0.70 | +0.48 / +0.79 | both halves | 2e-05 |  |
| [[CNTNAP5]] | +0.70 | +0.51 / +0.79 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZRN3]] | B | PDZRN3 activity raises SEMA6D's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without PDZRN3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[BAALC]] | B | BAALC activity raises SEMA6D's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without BAALC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[GAP43]] | B | GAP43 activity raises SEMA6D's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without GAP43 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[RALYL]] | B | RALYL activity raises SEMA6D's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.09× lower at baseline in the lines without RALYL | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[DGKB]] | B | DGKB activity raises SEMA6D's level | lines that do not express DGKB (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without DGKB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[PTH2R]] | B | PTH2R activity raises SEMA6D's level | lines that do not express PTH2R (36) vs lines expressing it (14) | 2.60× lower at baseline in the lines without PTH2R | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, ENSG00000286523, CNTN6; maybe low, not absent |
| [[NPFFR2]] | B | NPFFR2 activity raises SEMA6D's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without NPFFR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[TOP2A]] | B | TOP2A activity lowers SEMA6D's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SRRM4]] | B | SRRM4 activity raises SEMA6D's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.34× lower at baseline in the lines without SRRM4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[GRIK1]] | B | GRIK1 activity raises SEMA6D's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without GRIK1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[ASCL1]] | B | ASCL1 activity raises SEMA6D's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.69× lower at baseline in the lines without ASCL1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[LRFN2]] | B | LRFN2 activity raises SEMA6D's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without LRFN2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.1, 30.3); signed map (33.2, 16.1). **Vector** length 52.7, 7.38% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 6D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:47,184,101-47,774,228 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1479, FLJ11598 |
| Gene groups (HGNC) | Semaphorins |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFY4](https://www.uniprot.org/uniprotkb/Q8NFY4) (Semaphorin-6D):

> Shows growth cone collapsing activity on dorsal root ganglion (DRG) neurons in vitro. May be a stop signal for the DRG neurons in their target areas, and possibly also for other neurons. May also be involved in the maintenance and remodeling of neuronal connections. Ligand of TREM2 with PLXNA1 as coreceptor in dendritic cells, plays a role in the generation of immune responses and skeletal homeostasis (By similarity).

**Summary**, from NCBI Gene [80031](https://www.ncbi.nlm.nih.gov/gene/80031):

> Semaphorins are a large family, including both secreted and membrane associated proteins, many of which have been implicated as inhibitors or chemorepellents in axon pathfinding, fasciculation and branching, and target selection. All semaphorins possess a semaphorin (Sema) domain and a PSI domain (found in plexins, semaphorins and integrins) in the N-terminal extracellular portion. Additional sequence motifs C-terminal to the semaphorin domain allow classification into distinct subfamilies. …

**Accessions** — [HGNC:16770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16770) · Entrez [80031](https://www.ncbi.nlm.nih.gov/gene/80031) · UniProt [Q8NFY4](https://www.uniprot.org/uniprotkb/Q8NFY4) · Ensembl [ENSG00000137872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137872)

## Data

Gene col 6088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6088); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6088]; `tensor/DDL_lfc|DDL_z.npy` [6088]; `embed/gene_vectors.npy` [6088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6088 or target_col == 6088). Every well: [[SEMA6D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA6D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
