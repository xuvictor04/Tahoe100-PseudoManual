---
symbol: "MATN3"
type: "gene"
col: 5273
ensembl_id: "ENSG00000132031"
name: "matrilin 3"
location: "2p24.1"
module: 50
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 35
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# MATN3

*matrilin 3* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.66× (z +18.2, q 0e+00, up in 19 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.603× (z -4.8, q 8e-04, down in 10 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.164×, A-172 0.227×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.155×, A-172 0.143×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.152×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSZ]] (+0.62, fdr 1e-05), [[SUSD5]] (+0.60, fdr 9e-05), [[SELENON]] (+0.60, fdr 2e-05); moves opposite to [[TIPRL]] (-0.66, fdr 1e-05), [[UPF3B]] (-0.58, fdr 3e-05), [[RBMX2]] (-0.58, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MXRA8]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF514]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.66×** | +18.2 | 0e+00 | 19/22 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.22×** | +13.7 | 3e-40 | 3/3 (HOP62, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.06×** | +12.8 | 3e-35 | 5/6 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +12.0 | 4e-31 | 10/12 (HOP62, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **7.10×** | +10.1 | 4e-22 | 19/23 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.58×** | +9.0 | 2e-17 | 3/8 (NCI-H2030, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +7.7 | 8e-13 | 5/29 (HOP62, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +6.7 | 2e-09 | 12/27 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +6.6 | 2e-09 | 7/24 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.0 | 1e-07 | 8/30 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.5 | 2e-06 | 3/24 (Panc 03.27, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.4 | 3e-06 | 3/12 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.81×** | +5.3 | 4e-06 | 4/7 (NCI-H2030, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.1 | 1e-05 | 5/27 (NCI-H460, SNU-423, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.62×** | +5.0 | 2e-05 | 5/19 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +4.7 | 8e-05 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +4.4 | 3e-04 | 3/30 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.4 | 3e-04 | 6/21 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.005 | 3/26 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.016 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.3 | 0.022 | 1/20 (RPMI-7951) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5273.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.164×, A-172 0.227×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.155×, A-172 0.143×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -4.8 | 8e-04 | 10/24 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.675×** | -3.7 | 0.066 | 4/27 (SNU-1, SNU-423, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.3 | 0.17 | 8/31 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.713× | -3.2 | 0.18 | 3/28 (J82, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -13.2) |
| [[A-172 (line)]] | wt | 9.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.8) |
| [[A-427 (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.962 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.895 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.781 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.800 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.890 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.855 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSZ]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SUSD5]] | +0.60 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[SELENON]] | +0.60 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[FSTL1]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[NAGA]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SIAE]] | +0.57 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[FKBP9]] | +0.57 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ITM2C]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CD302]] | +0.56 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[LAMP1]] | +0.55 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[DKK3]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DDOST]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIPRL]] | -0.66 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RBMX2]] | -0.58 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[NKAP]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CROCCP2-1]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NEMF]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[CEP290]] | -0.53 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[MRPL2]] | -0.50 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[RNF166]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[EMC2]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NSRP1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[SDHAF2]] | -0.49 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MXRA8]] | B | MXRA8 activity raises MATN3's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without MXRA8 | 0.025 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[MYL9]] | B | MYL9 activity raises MATN3's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without MYL9 | 0.045 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF514]] | B | MATN3 activity strengthens ZNF514's drug response | lines that do not express MATN3 (15) vs lines expressing it (33) | the lines without MATN3 respond 0.69× as strongly (z diff +1.29); strongest at Harringtonine 5 µM: 0.61x vs 0.36x (z diff +2.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: LTBP2, DNAAF9, FSTL1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SDHAF2]] | B | MATN3 activity lowers SDHAF2's level | lines that do not express MATN3 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without MATN3 | 0.073 | ⚠ within organs, on part of the lines; also absent: LTBP2, DNAAF9, FSTL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.9, 4.7); signed map (45.8, -8.6). **Vector** length 35.9, 4.90% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.7 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | matrilin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:19,992,052-20,012,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EDM5, HOA |
| Gene groups (HGNC) | Matrilins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: ECM proteoglycans; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [O15232](https://www.uniprot.org/uniprotkb/O15232) (Matrilin-3):

> Major component of the extracellular matrix of cartilage and may play a role in the formation of extracellular filamentous networks.

**Summary**, from NCBI Gene [4148](https://www.ncbi.nlm.nih.gov/gene/4148):

> This gene encodes a member of von Willebrand factor A domain containing protein family. This family of proteins is thought to be involved in the formation of filamentous networks in the extracellular matrices of various tissues. This protein contains two von Willebrand factor A domains; it is present in the cartilage extracellular matrix and has a role in the development and homeostasis of cartilage and bone. Mutations in this gene result in multiple epiphyseal dysplasia. [provided by RefSeq, …

**Accessions** — [HGNC:6909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6909) · Entrez [4148](https://www.ncbi.nlm.nih.gov/gene/4148) · UniProt [O15232](https://www.uniprot.org/uniprotkb/O15232) · Ensembl [ENSG00000132031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132031)

## Data

Gene col 5273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5273); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5273]; `tensor/DDL_lfc|DDL_z.npy` [5273]; `embed/gene_vectors.npy` [5273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5273 or target_col == 5273). Every well: [[MATN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MATN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
