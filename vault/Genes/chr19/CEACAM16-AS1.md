---
symbol: "CEACAM16-AS1"
type: "gene"
col: 15502
ensembl_id: "ENSG00000266903"
name: "CEACAM16, CEACAM19 and PVR antisense RNA 1"
location: "19q13.31"
module: 75
arm: "+"
pooled_cpm: 10.72
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# CEACAM16-AS1

*CEACAM16, CEACAM19 and PVR antisense RNA 1* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +19.8, q 0e+00, up in 38 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Decitabine (drug)]] 0.05 µM in 2 lines (HepG2/C3A 0.0713×, RKO 0.116×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.136×); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.0653×; ⚠ cell-cycle shift, explains ~0% of this change); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.0654×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMC1]] (+0.71, fdr 1e-05), [[MVP-DT]] (+0.67, fdr 1e-05), [[HOXA-AS2]] (+0.67, fdr 1e-05); moves opposite to [[MLX]] (-0.62, fdr 2e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TNFSF14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +19.8 | 0e+00 | 38/42 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +9.0 | 1e-16 | 29/48 (Panc 03.27, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +8.4 | 7e-15 | 30/44 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.2 | 2e-14 | 12/30 (SW 900, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +6.9 | 5e-10 | 22/42 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.3 | 4e-08 | 13/27 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.4 | 6e-06 | 18/48 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.0 | 4e-05 | 6/19 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.003 | 11/46 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.022 | 15/40 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.042 | 7/44 (HepG2/C3A, SNU-423, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.073 | 15/44 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.097 | 8/44 (HCT15, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Decitabine (drug)]] 0.05 µM in 2 lines (HepG2/C3A 0.0713×, RKO 0.116×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.136×); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.0653×; ⚠ cell-cycle shift, explains ~0% of this change); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.0654×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -5.1 | 2e-04 | 10/48 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.798× | -3.4 | 0.21 | 6/46 (LS 180, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.813× | -3.1 | 0.30 | 10/46 (NCI-H1792, CHP-212, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.865× | -3.1 | 0.30 | 9/46 (COLO 205, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 15.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +15.2) | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +11.0) | [[Decitabine (drug)]] 0.05 µM 0.0713× (z -12.5) |
| [[RKO (line)]] | wt | 9.05 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Decitabine (drug)]] 0.05 µM 0.116× (z -8.8) |
| [[SW 900 (line)]] | alt | 6.00 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +10.3) | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0654× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 5.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.04× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +8.8) | — |
| [[C32 (line)]] | wt | 5.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 8.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +8.9) | — |
| [[J82 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 5.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +13.8) | — |
| [[SK-MEL-2 (line)]] | alt | 7.37 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.104× (z -8.8) |
| [[A-172 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC1]] | +0.71 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.67 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[HOXA-AS2]] | +0.67 | +0.61 / +0.52 | both halves | 1e-05 | same gene group |
| [[PPP1R15B-AS1]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 | same gene group |
| [[LINC01208]] | +0.65 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CARD14]] | +0.64 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[TPTE2P6]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ALDH1A2]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[EHBP1-AS1]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[DLEU7]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[HSD11B1-AS1]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 | same gene group |
| [[CTDSPL2-DT]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLX]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF14]] | B | TNFSF14 activity raises CEACAM16-AS1's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.49× lower at baseline in the lines without TNFSF14 | 0.005 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CEACAM16-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SERPINB9P1]] | B | SERPINB9P1 activity raises CEACAM16-AS1's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without SERPINB9P1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[CEACAM22P-1]] | B | CEACAM22P-1 activity raises CEACAM16-AS1's level | lines that do not express CEACAM22P-1 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without CEACAM22P-1 | 0.085 | ⚠ within organs, on part of the lines; also absent: PPM1L, ENSG00000287400; maybe low, not absent |
| [[RHBDL2]] | B | RHBDL2 activity raises CEACAM16-AS1's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.40× lower at baseline in the lines without RHBDL2 | 0.086 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[NPHS1]] | C | NPHS1 activity weakens CEACAM16-AS1's drug response | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1 respond 0.52× as strongly (z diff +0.84); strongest at Tucidinostat 0.5 µM: 3.18x vs 1.77x (z diff -3.8) | 0.052 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.6, 22.9); signed map (31.4, 1.0). **Vector** length 75.3, 12.8% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +19.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CEACAM16, CEACAM19 and PVR antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.31 — chr19:44,631,573-44,725,217 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55317) · Entrez [107985305](https://www.ncbi.nlm.nih.gov/gene/107985305) · Ensembl [ENSG00000266903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266903)

## Data

Gene col 15502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15502); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15502]; `tensor/DDL_lfc|DDL_z.npy` [15502]; `embed/gene_vectors.npy` [15502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15502 or target_col == 15502). Every well: [[CEACAM16-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEACAM16-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
