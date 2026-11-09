---
symbol: "CDH8"
type: "gene"
col: 7430
ensembl_id: "ENSG00000150394"
name: "cadherin 8"
location: "16q21"
module: 9
arm: "+"
pooled_cpm: 5.67
n_lines_expressing: 22
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CDH8

*cadherin 8* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.06× (z +15.4, q 0e+00, up in 4 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.666× (z -4.0, q 0.040, down in 11 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (H4 0.0205×, RPMI-7951 0.0572×, NCI-H23 0.0928×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Hs 766T 0.157×, SHP-77 0.297×, NCI-H661 0.112×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.143×, NCI-H1792 0.196×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX5L]] (+0.71, fdr 7e-06), [[CDH12]] (+0.69, fdr 1e-05), [[MAPK10]] (+0.69, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[CALCRL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +15.4 | 0e+00 | 4/16 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +10.8 | 6e-25 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +8.6 | 2e-15 | 1/7 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.7 | 3e-09 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.3 | 1e-05 | 1/12 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.3 | 1e-05 | 8/17 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.2 | 1e-05 | 7/19 (A-172, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.68×** | +4.9 | 8e-05 | 7/15 (J82, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 4/19 (C32, BT-474, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +4.0 | 0.003 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 9/17 (NCI-H23, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.014 | 2/19 (A-172, NCI-H2030) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.017 | 2/18 (A-172, BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.021 | 5/19 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.097 | 2/17 (Hs 766T, SHP-77) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7430.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (H4 0.0205×, RPMI-7951 0.0572×, NCI-H23 0.0928×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Hs 766T 0.157×, SHP-77 0.297×, NCI-H661 0.112×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.143×, NCI-H1792 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -4.0 | 0.040 | 11/18 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.705× | -3.4 | 0.14 | 9/17 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.14 | 2/16 (HS-578T, A-427) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.718× | -3.2 | 0.14 | 9/18 (RPMI-7951, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.718× | -3.2 | 0.14 | 9/19 (NCI-H1792, RPMI-7951, …) | top dose only | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.797× | -3.1 | 0.16 | 0/20 | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 30.5 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0205× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0388× (z -14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.9) |
| [[A-172 (line)]] | wt | 5.84 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 6.61 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0572× (z -9.9) |
| [[SHP-77 (line)]] | alt | 65.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -11.5) |
| [[Hs 766T (line)]] | wt | 55.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 9.50 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0928× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 60.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -9.4) |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.825 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.937 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX5L]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CDH12]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 | same gene group; pathway: Adherens junctions interactions; STRING 893 |
| [[MAPK10]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[LINC02211]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MIR3171HG]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[LINC01116]] | +0.65 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SCN2A]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZIC1]] | +0.62 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[LINC01287]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LINC00648]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CDH8's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ZIC1]] | C | ZIC1 activity raises CDH8's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without ZIC1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |
| [[KC6]] | C | KC6 activity raises CDH8's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.96× lower at baseline in the lines without KC6 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises CDH8's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 3.37× lower at baseline in the lines without PCDH18 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises CDH8's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 3.37× lower at baseline in the lines without SLC25A24P1 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises CDH8's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 1.87× lower at baseline in the lines without BRINP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[MIR646HG]] | C | MIR646HG activity raises CDH8's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without MIR646HG | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises CDH8's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.56× lower at baseline in the lines without CDH12 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCRL]] | B | CDH8 activity raises CALCRL's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without CDH8 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent |
| [[DGKB]] | B | CDH8 activity raises DGKB's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without CDH8 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent |
| [[FLG-AS1]] | B | CDH8 activity raises FLG-AS1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without CDH8 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent |
| [[KC6]] | C | CDH8 activity raises KC6's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 3.68× lower at baseline in the lines without CDH8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[ZIC1]] | C | CDH8 activity raises ZIC1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 4.10× lower at baseline in the lines without CDH8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[GUCY1A1]] | C | CDH8 activity raises GUCY1A1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without CDH8 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[LINC02438]] | C | CDH8 activity raises LINC02438's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 3.15× lower at baseline in the lines without CDH8 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[DOK5]] | C | CDH8 activity raises DOK5's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without CDH8 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[IGFBP5]] | C | CDH8 activity raises IGFBP5's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 6.08× lower at baseline in the lines without CDH8 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[SULF1]] | C | CDH8 activity raises SULF1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without CDH8 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.1, 31.9); signed map (40.8, 33.2). **Vector** length 46.9, 11.5% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:61,647,242-62,037,035 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Type II classical cadherins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 9 pathways, smallest: CDH11 homotypic and heterotypic interactions; Regulation of CDH11 function; Regulation of CDH11 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [P55286](https://www.uniprot.org/uniprotkb/P55286) (Cadherin-8):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1006](https://www.ncbi.nlm.nih.gov/gene/1006):

> This gene encodes a type II classical cadherin from the cadherin superfamily, integral membrane proteins that mediate calcium-dependent cell-cell adhesion. Mature cadherin proteins are composed of a large N-terminal extracellular domain, a single membrane-spanning domain, and a small, highly conserved C-terminal cytoplasmic domain. The extracellular domain consists of 5 subdomains, each containing a cadherin motif, and appears to determine the specificity of the protein's homophilic cell …

**Accessions** — [HGNC:1767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1767) · Entrez [1006](https://www.ncbi.nlm.nih.gov/gene/1006) · UniProt [P55286](https://www.uniprot.org/uniprotkb/P55286) · Ensembl [ENSG00000150394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150394)

## Data

Gene col 7430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7430); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7430]; `tensor/DDL_lfc|DDL_z.npy` [7430]; `embed/gene_vectors.npy` [7430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7430 or target_col == 7430). Every well: [[CDH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
