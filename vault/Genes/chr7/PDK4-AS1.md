---
symbol: "PDK4-AS1"
type: "gene"
col: 13782
ensembl_id: "ENSG00000231170"
name: "PDK4 antisense RNA 1"
location: "7q21.3"
module: 27
arm: "+"
pooled_cpm: 3.14
n_lines_expressing: 43
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PDK4-AS1

*PDK4 antisense RNA 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +11.6, q 1e-28, up in 18 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (LS 180 0.0286×, SW480 0.183×); [[Bortezomib (drug)]] 0.05 µM in 2 lines (LS 180 0.0607×, SW480 0.171×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.185×, LS 180 0.124×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (LS 180 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB4]] (+0.67, fdr 7e-06, ⚠ same locus), [[CCDC170]] (+0.67, fdr 7e-06), [[PKHD1]] (+0.66, fdr 7e-06), [[CHDH]] (+0.63, fdr 1e-05); moves opposite to [[YKT6]] (-0.54, fdr 7e-05), [[PPM1F]] (-0.51, fdr 9e-05), [[EHD4]] (-0.50, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ASB4]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Irinotecan (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +11.6 | 1e-28 | 18/24 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +10.4 | 5e-23 | 4/10 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +9.5 | 4e-19 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +7.1 | 2e-10 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.0 | 2e-07 | 10/36 (SHP-77, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +5.9 | 3e-07 | 8/25 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +5.3 | 1e-05 | 11/37 (PANC-1, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.2 | 1e-05 | 4/21 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.003 | 7/24 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.007 | 10/37 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.008 | 6/26 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.008 | 7/30 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.025 | 7/38 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.029 | 4/38 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.042 | 4/27 (NCI-H460, A549, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.095 | 4/28 (LoVo, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13782.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (LS 180 0.0286×, SW480 0.183×); [[Bortezomib (drug)]] 0.05 µM in 2 lines (LS 180 0.0607×, SW480 0.171×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.185×, LS 180 0.124×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (LS 180 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.688× | -3.3 | 0.37 | 13/38 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.693× | -3.2 | 0.37 | 8/30 (LS 180, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 22.1 | 0 | 8 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0286× (z -15.1) |
| [[A-427 (line)]] | wt | 20.9 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0728× (z -10.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.185× (z -9.2) |
| [[SW480 (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[A-172 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.961 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.893 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.881 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.995 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB4]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 | ⚠ same locus (5.0 kb, same strand: neighbours can correlate without regulation) |
| [[CCDC170]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PKHD1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CHDH]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[MIR4500HG]] | +0.62 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[ERICH2-DT]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[BCAR3-AS1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 | same gene group |
| [[LINC02058]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FGF20]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[LINC02254]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[BANK1]] | +0.61 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MYO3B]] | +0.59 | +0.66 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YKT6]] | -0.54 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[PPM1F]] | -0.51 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[EHD4]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[DPP9]] | -0.49 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASB4]] | B | ASB4 activity raises PDK4-AS1's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.47× lower at baseline in the lines without ASB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[SMOC2]] | B | SMOC2 activity raises PDK4-AS1's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without SMOC2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent |
| [[ST18]] | B | ST18 activity raises PDK4-AS1's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without ST18 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent |
| [[LINC02058]] | B | LINC02058 activity raises PDK4-AS1's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without LINC02058 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |
| [[APCDD1]] | B | APCDD1 activity raises PDK4-AS1's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.00× lower at baseline in the lines without APCDD1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[TFF3]] | B | TFF3 activity raises PDK4-AS1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 1.72× lower at baseline in the lines without TFF3 | 0.078 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[LRRTM4]] | B | LRRTM4 activity raises PDK4-AS1's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 1.33× lower at baseline in the lines without LRRTM4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[LGR5]] | B | LGR5 activity raises PDK4-AS1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without LGR5 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[AXIN2]] | B | AXIN2 activity raises PDK4-AS1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.01× lower at baseline in the lines without AXIN2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Irinotecan (drug)]] 0.5 µM | B | PDK4-AS1 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express PDK4-AS1 (7) vs lines expressing it (41) | the lines without PDK4-AS1: 0.72× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, 44.1); signed map (60.3, 16.0). **Vector** length 48.2, 7.13% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | PDK4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.3 — chr7:95,545,191-95,615,132 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55767) · Entrez [107986824](https://www.ncbi.nlm.nih.gov/gene/107986824) · Ensembl [ENSG00000231170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231170)

## Data

Gene col 13782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13782); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13782]; `tensor/DDL_lfc|DDL_z.npy` [13782]; `embed/gene_vectors.npy` [13782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13782 or target_col == 13782). Every well: [[PDK4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDK4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
