---
symbol: "HCN2"
type: "gene"
col: 1819
ensembl_id: "ENSG00000099822"
name: "hyperpolarization activated cyclic nucleotide gated potassium and sodium channel 2"
location: "19p13.3"
module: 53
arm: "+"
pooled_cpm: 7.8
n_lines_expressing: 44
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# HCN2

*hyperpolarization activated cyclic nucleotide gated potassium and sodium channel 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.04× (z +16.6, q 0e+00, up in 28 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.107×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.165×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APC2]] (+0.70, fdr 7e-06), [[TUBB3]] (+0.69, fdr 7e-06), [[CPNE9]] (+0.66, fdr 7e-06); moves opposite to [[QRSL1]] (-0.53, fdr 2e-05), [[DTWD1]] (-0.53, fdr 3e-05), [[RWDD3]] (-0.52, fdr 2e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); 6 go from it, the strongest it → [[PRKCG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.04×** | +16.6 | 0e+00 | 28/36 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +13.6 | 2e-39 | 31/34 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.10×** | +11.9 | 2e-30 | 35/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.88×** | +11.1 | 1e-26 | 30/39 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +10.3 | 1e-22 | 10/13 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.58×** | +10.0 | 2e-21 | 18/26 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +9.8 | 1e-20 | 29/40 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.39×** | +9.2 | 3e-18 | 29/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +6.5 | 4e-09 | 22/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +6.4 | 9e-09 | 22/36 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.87×** | +6.1 | 6e-08 | 7/17 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.9 | 4e-05 | 14/40 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 7/40 (J82, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 15/40 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.004 | 10/39 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +3.7 | 0.008 | 7/38 (SHP-77, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +3.6 | 0.011 | 6/36 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1819.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.107×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.165×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.728× | -3.2 | 0.56 | 12/38 (SW480, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.745× | -3.1 | 0.56 | 8/41 (AsPC-1, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 11.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.34× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.4) | — |
| [[C32 (line)]] | wt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 3.65 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.3× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.32 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.5) |
| [[A498 (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 4.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.7) | — |
| [[LoVo (line)]] | wt | 8.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.114× (z -8.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APC2]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TUBB3]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | pathway: Neuronal System |
| [[CPNE9]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TGFB1]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[PRX]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TMPRSS9]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[EFNA2]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[DTWD1]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[RWDD3]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ABHD13]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DHFR2]] | -0.49 | -0.36 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises HCN2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without ASGR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[LAG3]] | B | LAG3 activity raises HCN2's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without LAG3 | 0.029 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[TTYH2]] | B | TTYH2 activity raises HCN2's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without TTYH2 | 0.096 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[PDGFA]] | C | PDGFA activity raises HCN2's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without PDGFA | 0.026 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCG]] | B | HCN2 activity raises PRKCG's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without HCN2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[LAG3]] | B | HCN2 activity raises LAG3's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.11× lower at baseline in the lines without HCN2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[NPAS1]] | B | HCN2 activity raises NPAS1's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.70× lower at baseline in the lines without HCN2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[MYO15A]] | B | HCN2 activity raises MYO15A's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 1.58× lower at baseline in the lines without HCN2 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[SMIM41]] | B | HCN2 activity raises SMIM41's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without HCN2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[PDGFA]] | C | HCN2 activity raises PDGFA's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without HCN2 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, -16.5); signed map (17.0, 14.5). **Vector** length 74.1, 13.2% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.2 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | hyperpolarization activated cyclic nucleotide gated potassium and sodium channel 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:589,881-617,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCNG-2, HAC-1; previously BCNG2 |
| Gene groups (HGNC) | Cyclic nucleotide gated channels |
| Reactome | 3 pathways, smallest: HCN channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL51](https://www.uniprot.org/uniprotkb/Q9UL51) (Potassium/sodium hyperpolarization-activated cyclic nucleotide-gated channel 2):

> Hyperpolarization-activated ion channel that is permeable to sodium and potassium ions. Displays lower selectivity for K(+) over Na(+) ions. Contributes to the native pacemaker currents in heart (If) and in neurons (Ih). Can also transport ammonium in the distal nephron (By similarity). Involved in the initiation of neuropathic pain in sensory neurons (By similarity).

**Summary**, from NCBI Gene [610](https://www.ncbi.nlm.nih.gov/gene/610):

> The protein encoded by this gene is a hyperpolarization-activated cation channel involved in the generation of native pacemaker activity in the heart and in the brain. The encoded protein is activated by cAMP and can produce a fast, large current. Defects in this gene were noted as a possible cause of some forms of epilepsy. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:4846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4846) · Entrez [610](https://www.ncbi.nlm.nih.gov/gene/610) · UniProt [Q9UL51](https://www.uniprot.org/uniprotkb/Q9UL51) · Ensembl [ENSG00000099822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099822)

## Data

Gene col 1819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1819); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1819]; `tensor/DDL_lfc|DDL_z.npy` [1819]; `embed/gene_vectors.npy` [1819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1819 or target_col == 1819). Every well: [[HCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
