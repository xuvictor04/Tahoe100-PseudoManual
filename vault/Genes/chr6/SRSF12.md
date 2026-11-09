---
symbol: "SRSF12"
type: "gene"
col: 7814
ensembl_id: "ENSG00000154548"
name: "serine and arginine rich splicing factor 12"
location: "6q15"
module: 140
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 45
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# SRSF12

*serine and arginine rich splicing factor 12* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +11.6, q 2e-28, up in 10 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.111×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0509×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.240×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (A549 0.0689×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAP2]] (+0.67, fdr 7e-06), [[FAXC]] (+0.57, fdr 2e-05), [[CARNMT1-AS1]] (+0.57, fdr 4e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[LINC01122]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +11.6 | 2e-28 | 10/19 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +8.1 | 2e-13 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +7.5 | 1e-11 | 13/25 (C-33 A, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +7.0 | 4e-10 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +6.1 | 9e-08 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.2 | 2e-05 | 1/9 (PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.0 | 4e-05 | 3/8 (A549, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +4.4 | 7e-04 | 5/23 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.002 | 2/17 (NCI-H460, CHP-212) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.0 | 0.004 | 1/14 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.7 | 0.010 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.018 | 4/24 (A-427, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +3.5 | 0.021 | 1/26 (SHP-77) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.021 | 1/12 (NCI-H2347) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.026 | 1/35 (A-427) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.038 | 2/17 (HOP62, LoVo) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.041 | 0/28 | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.043 | 0/32 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.053 | 6/35 (PANC-1, SW 900, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.063 | 5/23 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.066 | 7/31 (SHP-77, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7814.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.111×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0509×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.240×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (A549 0.0689×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Arbutin (drug)]] 0.5 µM |  | 0.685× | -3.3 | 0.37 | 4/35 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.691× | -3.2 | 0.37 | 13/36 (NCI-H661, NCI-H23, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -3.1 | 0.37 | 10/41 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.54 | 0 | 2 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0689× (z -10.0) |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0509× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 7.93 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.138× (z -9.8) |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -11.0) |
| [[A-172 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.636 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.660 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.774 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.769 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.654 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.915 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.674 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.653 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.959 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.604 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAP2]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[FAXC]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CARNMT1-AS1]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[GALNT17]] | +0.56 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[CDH23]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[APBB1]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SCN1A-AS1]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CUX2]] | +0.53 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[PTPRO]] | +0.53 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[BTG3]] | +0.52 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[KCNB1]] | +0.51 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[GPLD1]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01122]] | B | SRSF12 activity raises LINC01122's level | lines that do not express SRSF12 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without SRSF12 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZNF655, CPNE5, DIP2C; maybe low, not absent; its own permutation p |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | SRSF12's natural level lowers the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (makes them more sensitive) | SRSF12's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.362 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | SRSF12's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | SRSF12's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.9, 31.8); signed map (31.6, 10.4). **Vector** length 33.5, 3.67% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +7.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,095,959-89,118,071 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRrp35, SFRS19; previously SFRS13B |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXF0](https://www.uniprot.org/uniprotkb/Q8WXF0) (Serine/arginine-rich splicing factor 12):

> Splicing factor that seems to antagonize SR proteins in pre-mRNA splicing regulation.

**Summary**, from NCBI Gene [135295](https://www.ncbi.nlm.nih.gov/gene/135295):

> Enables RNA binding activity. Involved in mRNA 5'-splice site recognition and regulation of alternative mRNA splicing, via spliceosome. Predicted to be located in nucleoplasm. Predicted to be active in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21220) · Entrez [135295](https://www.ncbi.nlm.nih.gov/gene/135295) · UniProt [Q8WXF0](https://www.uniprot.org/uniprotkb/Q8WXF0) · Ensembl [ENSG00000154548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154548)

## Data

Gene col 7814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7814); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7814]; `tensor/DDL_lfc|DDL_z.npy` [7814]; `embed/gene_vectors.npy` [7814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7814 or target_col == 7814). Every well: [[SRSF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
