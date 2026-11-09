---
symbol: "OSGIN2"
type: "gene"
col: 9011
ensembl_id: "ENSG00000164823"
name: "oxidative stress induced growth inhibitor family member 2"
location: "8q21.3"
module: 94
arm: "+"
pooled_cpm: 31.89
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# OSGIN2

*oxidative stress induced growth inhibitor family member 2* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +19.6, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.726× (z -5.1, q 2e-04, down in 19 of 36 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 0.0543×, C32 0.131×, LOX-IMVI 0.277×; ⚠ toxic; transcription drop); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.0916×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.335×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLN5]] (+0.68, fdr 7e-06), [[ZNF442]] (+0.67, fdr 1e-05), [[OGFRL1]] (+0.61, fdr 5e-05); moves opposite to [[MLXIP]] (-0.58, fdr 1e-05), [[FARP2]] (-0.54, fdr 2e-05), [[FBRSL1]] (-0.52, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF44]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +19.6 | 0e+00 | 41/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +13.3 | 8e-38 | 41/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +11.5 | 2e-28 | 38/48 (PANC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +11.1 | 1e-26 | 37/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +9.9 | 5e-21 | 39/48 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +7.4 | 1e-11 | 29/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +6.5 | 9e-09 | 28/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 24/47 (HT-29, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 5e-06 | 24/48 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.38×** | +5.3 | 5e-06 | 27/48 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 3e-05 | 19/47 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.003 | 16/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.008 | 17/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 15/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +3.3 | 0.033 | 17/48 (LoVo, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9011.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 0.0543×, C32 0.131×, LOX-IMVI 0.277×; ⚠ toxic; transcription drop); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.0916×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.335×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -5.1 | 2e-04 | 19/36 (AsPC-1, C32, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.823× | -3.2 | 0.20 | 10/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.871× | -3.2 | 0.20 | 14/48 (HCT15, C-33 A, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.817× | -3.2 | 0.20 | 6/48 (SW 1088, Panc 03.27, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 37.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +17.7) | — |
| [[HOP62 (line)]] | alt | 22.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +17.9) | — |
| [[A-172 (line)]] | wt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.4) | — |
| [[A-427 (line)]] | wt | 31.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.2) | — |
| [[J82 (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 57.2 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 3.76× (z +10.4) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.335× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 55.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 26.3 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.04× (z +10.6) | — |
| [[RKO (line)]] | wt | 41.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[A498 (line)]] | wt | 92.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -18.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.1) | — |
| [[KATO III (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0916× (z -11.5) |
| [[SNU-423 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +14.5) | — |
| [[SW1417 (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.5) | — |
| [[A549 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN5]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.67 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[OGFRL1]] | +0.61 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[ZNF433]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZNF627]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SLC43A2]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TDP2]] | +0.59 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[SEPSECS]] | +0.58 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[C17orf75]] | +0.57 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[TLR1]] | +0.57 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZNF563]] | +0.56 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[ARMT1]] | +0.56 | +0.61 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLXIP]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[FARP2]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[FBRSL1]] | -0.52 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[GNB1L]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[SKI]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CYTH3]] | -0.51 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[NPHP4]] | -0.51 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[RRP7BP-1]] | -0.51 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[PI4KAP2]] | -0.51 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[SCART1]] | -0.51 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[LMBR1]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SMC5]] | -0.49 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF44]] | C | ZNF44 activity strengthens OSGIN2's drug response | lines that do not express ZNF44 (3) vs lines expressing it (44) | the lines without ZNF44 respond 0.50× as strongly (z diff +2.69); strongest at Idarubicin (hydrochloride) 5 µM: 0.97x vs 1.64x (z diff +6.0) | 0.073 | ⚠ few lines (3 vs 46); across organs; also absent: ZNF20, ENSG00000268870, SORT1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.8, 23.4); signed map (16.6, -17.0). **Vector** length 98.2, 22.4% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.2 | +11.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.0 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +0.9 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | oxidative stress induced growth inhibitor family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:89,901,849-89,927,888 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hT41; previously C8orf1 |
| Gene groups (HGNC) | Oxidative stress induced growth inhibitor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y236](https://www.uniprot.org/uniprotkb/Q9Y236) (Oxidative stress-induced growth inhibitor 2):

> Monooxygenase catalytic activity (By similarity). May be involved in meiosis or the maturation of germ cells.

**Summary**, from NCBI Gene [734](https://www.ncbi.nlm.nih.gov/gene/734):

> Predicted to enable growth factor activity. Predicted to be involved in negative regulation of cell growth. Predicted to be located in midbody. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1355) · Entrez [734](https://www.ncbi.nlm.nih.gov/gene/734) · UniProt [Q9Y236](https://www.uniprot.org/uniprotkb/Q9Y236) · Ensembl [ENSG00000164823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164823)

## Data

Gene col 9011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9011); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9011]; `tensor/DDL_lfc|DDL_z.npy` [9011]; `embed/gene_vectors.npy` [9011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9011 or target_col == 9011). Every well: [[OSGIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSGIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
