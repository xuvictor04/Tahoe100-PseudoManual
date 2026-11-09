---
symbol: "THY1"
type: "gene"
col: 7768
ensembl_id: "ENSG00000154096"
name: "Thy-1 cell surface antigen"
location: "11q23.3"
module: 66
arm: "+"
pooled_cpm: 8.69
n_lines_expressing: 12
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 13
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# THY1

*Thy-1 cell surface antigen* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.18× (z +13.5, q 6e-39, up in 8 of 9 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +6.0, q 2e-07, up in 5 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0760×; ⚠ cell-cycle shift, explains ~49% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPARC]] (+0.73, fdr 7e-06), [[PTN]] (+0.65, fdr 4e-05), [[POSTN]] (+0.60, fdr 1e-05); moves opposite to [[ZNF765]] (-0.46, fdr 1e-04), [[SNHG11]] (-0.43, fdr 2e-04), [[EPB41L4A-AS1]] (-0.43, fdr 3e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[PCOLCE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **9.18×** | +13.5 | 6e-39 | 8/9 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.1×** | +13.4 | 1e-38 | 6/6 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.10×** | +10.2 | 4e-22 | 6/6 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.22×** | +7.1 | 1e-10 | 5/9 (A-172, HS-578T, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +6.0 | 2e-07 | 5/10 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **6.04×** | +5.7 | 9e-07 | 3/5 (HS-578T, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +5.1 | 3e-05 | 7/10 (RPMI-7951, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.20×** | +4.6 | 4e-04 | 5/9 (HS-578T, RPMI-7951, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.4 | 7e-04 | 3/7 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **2.01×** | +4.2 | 0.001 | 1/9 (A-172) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **2.05×** | +4.2 | 0.002 | 4/7 (CHP-212, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.002 | 6/10 (A-172, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.85×** | +3.6 | 0.016 | 3/9 (HS-578T, A-172, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.69×** | +3.5 | 0.021 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.4 | 0.024 | 0/8 | top dose only | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **1.78×** | +3.3 | 0.032 | 2/9 (H4, HS-578T) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +3.1 | 0.067 | 6/10 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7768.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0760×; ⚠ cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Econazole (drug)]] 0.5 µM |  | 0.567× | -3.5 | 0.28 | 0/10 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.559× | -3.3 | 0.28 | 0/10 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 125 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.18× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0760× (z -9.7) ⚠ cell-cycle shift, explains ~49% of this change |
| [[RPMI-7951 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.552 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPARC]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 545 |
| [[PTN]] | +0.65 | +0.41 / +0.73 | both halves | 4e-05 | **novel candidate** |
| [[POSTN]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 551 |
| [[MMP2]] | +0.56 | +0.61 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 461 |
| [[COL3A1]] | +0.56 | +0.52 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 487 |
| [[COL1A1]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 807 |
| [[PDIA3]] | +0.54 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[GGH]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ECM1]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[COL1A2]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 734 |
| [[TMSB4X]] | +0.51 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[FSTL1]] | +0.51 | +0.56 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 641 |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF765]] | -0.46 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[SNHG11]] | -0.43 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[EPB41L4A-AS1]] | -0.43 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[PWP2]] | -0.41 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[ZNF286B]] | -0.41 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[ZNF593]] | -0.40 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[NDUFB9]] | -0.40 | -0.44 / -0.29 | both halves | 3e-04 |  |
| [[ZNF691]] | -0.40 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[KRTCAP3]] | -0.40 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[NOL8]] | -0.40 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[FOXO3B]] | -0.39 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[LINC02335]] | -0.39 | -0.11 / -0.44 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers THY1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL3A1]] | C | COL3A1 activity raises THY1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 8.05× lower at baseline in the lines without COL3A1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises THY1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 4.78× lower at baseline in the lines without COL1A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises THY1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 8.22× lower at baseline in the lines without SPARC | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises THY1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 5.54× lower at baseline in the lines without COL1A2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises THY1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 5.15× lower at baseline in the lines without POSTN | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[MXRA8]] | C | MXRA8 activity raises THY1's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 4.20× lower at baseline in the lines without MXRA8 | 0.064 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3; co-absent with the target |
| [[LUM]] | C | LUM activity raises THY1's level | lines that do not express LUM (34) vs lines expressing it (16) | 4.29× lower at baseline in the lines without LUM | 0.076 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises THY1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 7.10× lower at baseline in the lines without MMP2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCOLCE]] | B | THY1 activity raises PCOLCE's level | lines that do not express THY1 (38) vs lines expressing it (12) | 5.40× lower at baseline in the lines without THY1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1 |
| [[COL3A1]] | C | THY1 activity raises COL3A1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 20.95× lower at baseline in the lines without THY1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[COL1A2]] | C | THY1 activity raises COL1A2's level | lines that do not express THY1 (38) vs lines expressing it (12) | 12.22× lower at baseline in the lines without THY1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[COL1A1]] | C | THY1 activity raises COL1A1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 8.82× lower at baseline in the lines without THY1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[MMP2]] | C | THY1 activity raises MMP2's level | lines that do not express THY1 (38) vs lines expressing it (12) | 12.22× lower at baseline in the lines without THY1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[PTN]] | C | THY1 activity raises PTN's level | lines that do not express THY1 (38) vs lines expressing it (12) | 6.49× lower at baseline in the lines without THY1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[CHRDL1]] | C | THY1 activity raises CHRDL1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 1.48× lower at baseline in the lines without THY1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[SPARC]] | C | THY1 activity raises SPARC's level | lines that do not express THY1 (38) vs lines expressing it (12) | 12.04× lower at baseline in the lines without THY1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[POSTN]] | C | THY1 activity raises POSTN's level | lines that do not express THY1 (38) vs lines expressing it (12) | 4.62× lower at baseline in the lines without THY1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[ITGA4]] | C | THY1 activity raises ITGA4's level | lines that do not express THY1 (38) vs lines expressing it (12) | 6.91× lower at baseline in the lines without THY1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[LUM]] | C | THY1 activity raises LUM's level | lines that do not express THY1 (38) vs lines expressing it (12) | 4.45× lower at baseline in the lines without THY1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[FSTL1]] | C | THY1 activity raises FSTL1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 5.19× lower at baseline in the lines without THY1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.9, 23.6); signed map (44.4, 21.7). **Vector** length 29.0, 8.76% of its response variance represented; |z| ≥ 3 in 201 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Binding and Uptake of Ligands by Scavenger Receptors* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +0.9 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +0.9 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.9 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.7 | +0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | -0.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.6 | +1.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | -0.9 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -0.9 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -0.9 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -0.9 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.7 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.7 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | Thy-1 cell surface antigen |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,415,476-119,424,985 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD90 |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | HEDGEHOG_SIGNALING, APICAL_SURFACE, ALLOGRAFT_REJECTION, APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P04216](https://www.uniprot.org/uniprotkb/P04216) (Thy-1 membrane glycoprotein):

> May play a role in cell-cell or cell-ligand interactions during synaptogenesis and other events in the brain.

**Summary**, from NCBI Gene [7070](https://www.ncbi.nlm.nih.gov/gene/7070):

> This gene encodes a cell surface glycoprotein and member of the immunoglobulin superfamily of proteins. The encoded protein is involved in cell adhesion and cell communication in numerous cell types, but particularly in cells of the immune and nervous systems. The encoded protein is widely used as a marker for hematopoietic stem cells. This gene may function as a tumor suppressor in nasopharyngeal carcinoma. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul …

**Accessions** — [HGNC:11801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11801) · Entrez [7070](https://www.ncbi.nlm.nih.gov/gene/7070) · UniProt [P04216](https://www.uniprot.org/uniprotkb/P04216) · Ensembl [ENSG00000154096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154096)

## Data

Gene col 7768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7768); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7768]; `tensor/DDL_lfc|DDL_z.npy` [7768]; `embed/gene_vectors.npy` [7768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7768 or target_col == 7768). Every well: [[THY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
