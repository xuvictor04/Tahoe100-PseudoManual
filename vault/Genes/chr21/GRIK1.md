---
symbol: "GRIK1"
type: "gene"
col: 10069
ensembl_id: "ENSG00000171189"
name: "glutamate ionotropic receptor kainate type subunit 1"
location: "21q21.3"
module: 9
arm: "+"
pooled_cpm: 18.61
n_lines_expressing: 16
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 24
direction_downstream: 12
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GRIK1

*glutamate ionotropic receptor kainate type subunit 1* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.28× (z +9.4, q 2e-18, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +7.2, q 1e-10, up in 7 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.552× (z -4.5, q 0.004, down in 3 of 13 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASCL1]] (+0.89, fdr 7e-06), [[RIT2]] (+0.89, fdr 7e-06), [[LRFN2]] (+0.87, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CALCA]] → it (grade C ⚠); 12 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +9.4 | 2e-18 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +9.4 | 2e-18 | 6/7 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.2 | 1e-10 | 7/11 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +6.7 | 4e-09 | 2/4 (HOP62, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.0 | 0.006 | 1/8 (HOP62) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.079 | 2/11 (C32, HOP62) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.68× | +3.1 | 0.16 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.30× | +3.0 | 0.16 | 2/13 (C32, HS-578T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.552×** | -4.5 | 0.004 | 3/13 (HEC-1-A, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -3.8 | 0.038 | 4/13 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.644×** | -3.6 | 0.057 | 4/13 (SHP-77, NCI-H1573, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.743× | -3.3 | 0.12 | 3/12 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.658× | -3.2 | 0.17 | 2/13 (LOX-IMVI, HOP62) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 839 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0833× (z -19.8) |
| [[A-172 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASCL1]] | +0.89 | +0.91 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[RIT2]] | +0.89 | +0.90 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 | pathway: Neuronal System |
| [[SYT4]] | +0.86 | +0.89 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SRRM4]] | +0.86 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SNTG1]] | +0.84 | +0.77 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[CALCA]] | +0.82 | +0.85 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.79 | +0.80 / +0.70 | both halves | 7e-06 | pathway: Neuronal System |
| [[PCSK1]] | +0.78 | +0.76 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CGA]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MYT1L]] | +0.75 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[CHRM5]] | +0.75 | +0.78 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | C | CALCA activity raises GRIK1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.44× lower at baseline in the lines without CALCA | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises GRIK1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 5.72× lower at baseline in the lines without RIT2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises GRIK1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.37× lower at baseline in the lines without SYT4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises GRIK1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 4.54× lower at baseline in the lines without KCNB2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[CGA]] | C | CGA activity raises GRIK1's level | lines that do not express CGA (44) vs lines expressing it (6) | 5.68× lower at baseline in the lines without CGA | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises GRIK1's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.74× lower at baseline in the lines without LINC01456 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[H19]] | C | H19 activity raises GRIK1's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without H19 | 0.017 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises GRIK1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.19× lower at baseline in the lines without ASCL1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[HGF]] | C | HGF activity raises GRIK1's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.54× lower at baseline in the lines without HGF | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises GRIK1's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without MIR3667HG | 0.022 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises GRIK1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.28× lower at baseline in the lines without SRRM4 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | ST18 activity raises GRIK1's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.49× lower at baseline in the lines without ST18 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | GRIK1 activity raises SEMA6D's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without GRIK1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[SNCAIP]] | B | GRIK1 activity raises SNCAIP's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.40× lower at baseline in the lines without GRIK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[ADGRL2]] | B | GRIK1 activity raises ADGRL2's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.65× lower at baseline in the lines without GRIK1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[GRIA4]] | B | GRIK1 activity raises GRIA4's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 1.64× lower at baseline in the lines without GRIK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[LRATD1]] | C | GRIK1 activity raises LRATD1's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without GRIK1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | GRIK1 activity raises HGF's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without GRIK1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[PCDH9]] | C | GRIK1 activity raises PCDH9's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without GRIK1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[LINC02999]] | C | GRIK1 activity raises LINC02999's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without GRIK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[LINC02050]] | C | GRIK1 activity raises LINC02050's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without GRIK1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[RUNX1T1]] | C | GRIK1 activity raises RUNX1T1's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without GRIK1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[LINC01592]] | C | GRIK1 activity raises LINC01592's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 1.43× lower at baseline in the lines without GRIK1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | GRIK1 activity raises SNTG1's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without GRIK1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 36.8); signed map (44.7, 34.0). **Vector** length 33.8, 9.76% of its response variance represented; |z| ≥ 3 in 229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -4.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor kainate type subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:29,536,933-29,940,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluK1; previously GLUR5 |
| Gene groups (HGNC) | Glutamate ionotropic receptor kainate type subunits |
| Reactome | 6 pathways, smallest: Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors; Activation of kainate receptors upon glutamate binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P39086](https://www.uniprot.org/uniprotkb/P39086) (Glutamate receptor ionotropic, kainate 1):

> Ionotropic glutamate receptor that functions as a cation-permeable ligand-gated ion channel, gated by L-glutamate and the glutamatergic agonist kainic acid. L-glutamate acts as an excitatory neurotransmitter at many synapses in the central nervous system. Binding of the excitatory neurotransmitter L-glutamate induces a conformation change, leading to the opening of the cation channel, and thereby converts the chemical signal to an electrical impulse. The receptor then desensitizes rapidly and …

**Summary**, from NCBI Gene [2897](https://www.ncbi.nlm.nih.gov/gene/2897):

> Glutamate receptors are the predominant excitatory neurotransmitter receptors in the mammalian brain and are activated in a variety of normal neurophysiologic processes. This gene product belongs to the kainate family of glutamate receptors, which are composed of four subunits and function as ligand-activated ion channels. The subunit encoded by this gene is subject to RNA editing (CAG->CGG; Q->R) within the second transmembrane domain, which is thought to alter the properties of ion flow. …

**Accessions** — [HGNC:4579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4579) · Entrez [2897](https://www.ncbi.nlm.nih.gov/gene/2897) · UniProt [P39086](https://www.uniprot.org/uniprotkb/P39086) · Ensembl [ENSG00000171189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171189)

## Data

Gene col 10069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10069); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10069]; `tensor/DDL_lfc|DDL_z.npy` [10069]; `embed/gene_vectors.npy` [10069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10069 or target_col == 10069). Every well: [[GRIK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
