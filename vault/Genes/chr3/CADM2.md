---
symbol: "CADM2"
type: "gene"
col: 10570
ensembl_id: "ENSG00000175161"
name: "cell adhesion molecule 2"
location: "3p12.1"
module: 9
arm: "+"
pooled_cpm: 53.66
n_lines_expressing: 19
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CADM2

*cell adhesion molecule 2* — 3p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.05× (z +16.9, q 0e+00, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.505× (z -3.8, q 0.076, down in 11 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AN3 CA 0.150×, C-33 A 0.263×, MIA PaCa-2 0.326×, CHP-212 0.253×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.0877×, AN3 CA 0.122×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.206×, SK-MEL-2 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.144×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAM2]] (+0.75, fdr 7e-06), [[PCDH9]] (+0.67, fdr 7e-06), [[CDH10]] (+0.65, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ARHGEF35-AS1]] → it (grade B ⚠); 4 go from it, the strongest it → [[KCNH5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +16.9 | 0e+00 | 4/17 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +12.0 | 8e-31 | 10/17 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +11.5 | 3e-28 | 11/17 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +11.4 | 5e-28 | 13/17 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +11.0 | 4e-26 | 4/17 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +9.9 | 5e-21 | 12/17 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +8.4 | 4e-15 | 3/15 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +7.3 | 2e-11 | 13/17 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.7 | 1e-09 | 12/17 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.7 | 1e-09 | 4/16 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +6.5 | 4e-09 | 3/17 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 5e-05 | 10/17 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.8 | 7e-05 | 3/19 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +4.7 | 1e-04 | 9/17 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.25×** | +4.5 | 2e-04 | 11/17 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 6e-04 | 9/17 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.001 | 11/17 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 0.001 | 9/17 (SHP-77, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10570.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AN3 CA 0.150×, C-33 A 0.263×, MIA PaCa-2 0.326×, CHP-212 0.253×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.0877×, AN3 CA 0.122×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.206×, SK-MEL-2 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -3.8 | 0.076 | 11/17 (NCI-H1573, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.716× | -3.6 | 0.10 | 13/17 (CHP-212, MIA PaCa-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | 0.802× | -3.3 | 0.15 | 3/17 (AN3 CA, CHP-212, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.727× | -3.3 | 0.15 | 8/17 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.741× | -3.2 | 0.15 | 8/17 (SW 900, A-427, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.744× | -3.2 | 0.15 | 1/17 (NCI-H2347) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.2 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 10.7× (z +16.6) | — |
| [[AN3 CA (line)]] | alt | 1,113 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 17.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 23.4× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 19.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +15.3) | — |
| [[C-33 A (line)]] | alt | 774 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0877× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 393 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.01× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 345 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.187× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 1,269 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -8.6) |
| [[A-172 (line)]] | wt | 5.84 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.91 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM2]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 | same gene group |
| [[PCDH9]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.65 | +0.58 / +0.59 | both halves | 7e-06 | pathway: Adherens junctions interactions |
| [[ERBB4]] | +0.63 | +0.63 / +0.71 | both halves | 7e-06 | same gene group |
| [[MIR99AHG]] | +0.62 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[LINC01194]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ADGRL3]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[BRINP3]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[CTNNA2]] | +0.59 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SNCA]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF35-AS1]] | B | ARHGEF35-AS1 activity lowers CADM2's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 7.34× higher at baseline in the lines without ARHGEF35-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |
| [[VIPR2]] | C | VIPR2 activity raises CADM2's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 5.52× lower at baseline in the lines without VIPR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises CADM2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 8.60× lower at baseline in the lines without KCNH5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[LINC01203]] | C | LINC01203 activity raises CADM2's level | lines that do not express LINC01203 (37) vs lines expressing it (13) | 4.26× lower at baseline in the lines without LINC01203 | 0.029 | ⚠ within organs, on part of the lines; also absent: SIM1, BMP10, LINC02643; maybe low, not absent; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises CADM2's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 5.64× lower at baseline in the lines without CDH7 | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[GASK1B-AS1]] | C | GASK1B-AS1 activity raises CADM2's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 4.80× lower at baseline in the lines without GASK1B-AS1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises CADM2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 6.11× lower at baseline in the lines without KCNH7 | 0.060 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises CADM2's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 5.23× lower at baseline in the lines without LINC01035 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises CADM2's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.65× lower at baseline in the lines without MIR99AHG | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[HERC2P3-1]] | C | HERC2P3-1 activity raises CADM2's level | lines that do not express HERC2P3-1 (23) vs lines expressing it (27) | 4.53× lower at baseline in the lines without HERC2P3-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF880, ENSG00000258732, ZNF829; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises CADM2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.51× lower at baseline in the lines without FUT9 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises CADM2's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 4.21× lower at baseline in the lines without BRINP3 | 0.090 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNH5]] | C | CADM2 activity raises KCNH5's level | lines that do not express CADM2 (31) vs lines expressing it (19) | 4.33× lower at baseline in the lines without CADM2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000263551, KCNH5, KIF1A; co-absent with the target |
| [[CSMD3]] | C | CADM2 activity raises CSMD3's level | lines that do not express CADM2 (31) vs lines expressing it (19) | 3.88× lower at baseline in the lines without CADM2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000263551, KCNH5, KIF1A; co-absent with the target |
| [[HERC2P3-1]] | C | CADM2 activity raises HERC2P3-1's level | lines that do not express CADM2 (31) vs lines expressing it (19) | 4.20× lower at baseline in the lines without CADM2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000263551, KCNH5, KIF1A; co-absent with the target |
| [[ADGRL3]] | C | CADM2 activity raises ADGRL3's level | lines that do not express CADM2 (31) vs lines expressing it (19) | 3.15× lower at baseline in the lines without CADM2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000263551, KCNH5, KIF1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.1, 33.6); signed map (40.7, 35.5). **Vector** length 65.2, 20.9% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +4.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cell adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p12.1 — chr3:84,958,989-86,074,429 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NECL3, Necl-3, SynCAM2, SynCAM-2; previously IGSF4D |
| Gene groups (HGNC) | V-set domain containing; C2-set domain containing; I-set domain containing; MicroRNA protein coding host genes; Nectins and nectin-like molecules |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3J6](https://www.uniprot.org/uniprotkb/Q8N3J6) (Cell adhesion molecule 2):

> Adhesion molecule that engages in homo- and heterophilic interactions with the other nectin-like family members, leading to cell aggregation. Important for synapse organization, providing regulated trans-synaptic adhesion. Preferentially binds to oligodendrocytes.; [Isoform 5]: (Microbial infection) Induces cell fusion in neuron infected by a neuropathogenic strain of measles. Interacts with measles hemagglutinin to trigger hyperfusogenic F-mediated membrane fusion and presumably transsynaptic …

**Summary**, from NCBI Gene [253559](https://www.ncbi.nlm.nih.gov/gene/253559):

> This gene encodes a member of the synaptic cell adhesion molecule 1 (SynCAM) family which belongs to the immunoglobulin (Ig) superfamily. The encoded protein has three Ig-like domains and a cytosolic protein 4.1 binding site near the C-terminus. Proteins belonging to the protein 4.1 family crosslink spectrin and interact with other cytoskeletal proteins. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:29849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29849) · Entrez [253559](https://www.ncbi.nlm.nih.gov/gene/253559) · UniProt [Q8N3J6](https://www.uniprot.org/uniprotkb/Q8N3J6) · Ensembl [ENSG00000175161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175161)

## Data

Gene col 10570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10570); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10570]; `tensor/DDL_lfc|DDL_z.npy` [10570]; `embed/gene_vectors.npy` [10570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10570 or target_col == 10570). Every well: [[CADM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CADM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
