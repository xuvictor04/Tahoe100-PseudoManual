---
symbol: "CEACAM19"
type: "gene"
col: 11830
ensembl_id: "ENSG00000186567"
name: "CEA cell adhesion molecule 19"
location: "19q13.31"
module: 38
arm: "+"
pooled_cpm: 10.97
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CEACAM19

*CEA cell adhesion molecule 19* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +15.8, q 0e+00, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.435× (z -6.0, q 1e-06, down in 18 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PVR]] (+0.69, fdr 7e-06, ⚠ same locus), [[PILRA]] (+0.66, fdr 7e-06), [[CDKL1]] (+0.66, fdr 1e-05), [[NLGN3]] (+0.64, fdr 1e-05); moves opposite to [[BAG4]] (-0.60, fdr 1e-05), [[LANCL1]] (-0.60, fdr 1e-05), [[PEX2]] (-0.59, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +15.8 | 0e+00 | 33/41 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +9.1 | 3e-17 | 35/46 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +8.7 | 5e-16 | 27/41 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +8.2 | 3e-14 | 30/45 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.4 | 1e-08 | 16/34 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +6.2 | 5e-08 | 24/44 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.2 | 5e-08 | 21/38 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 6e-05 | 15/46 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.92×** | +4.7 | 2e-04 | 9/45 (SW480, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +4.6 | 2e-04 | 14/39 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 14/45 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +4.3 | 7e-04 | 17/46 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.001 | 11/47 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.003 | 14/43 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.033 | 9/46 (NCI-H2030, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.048 | 8/44 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.052 | 12/40 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.068 | 0/47 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.435×** | -6.0 | 1e-06 | 18/36 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -5.8 | 2e-06 | 19/43 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.734×** | -4.1 | 0.008 | 10/45 (A549, A498, …) | top dose only | plate-row cell shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -3.8 | 0.017 | 13/41 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.772×** | -3.6 | 0.042 | 10/37 (A549, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.046 | 11/44 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.064 | 8/44 (A-172, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.064 | 15/44 (NCI-H23, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.3) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HepG2_C3A (line)]] | wt | 13.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +9.9) | [[Silodosin (drug)]] 5 µM 0.113× (z -8.9) |
| [[SNU-423 (line)]] | alt | 8.59 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +8.7) | [[Decitabine (drug)]] 0.5 µM 0.0748× (z -10.7) |
| [[HOP62 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +15.4) | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.120× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 7.50 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.120× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 6.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 4.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0686× (z -8.9) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 4.23 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0578× (z -8.7) |
| [[A-172 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PVR]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 | same gene group; STRING 505; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PILRA]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 | same gene group |
| [[CDKL1]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.64 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CDKL4]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[WNK4]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PPIEL-1]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[SMCO2]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[MYH3]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[TXK]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[KCNJ14]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[CHADL]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAG4]] | -0.60 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PEX2]] | -0.59 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[POT1]] | -0.56 | -0.67 / -0.40 | both halves | 4e-05 |  |
| [[LONP2]] | -0.56 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[MDH1]] | -0.55 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[USP30]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[RBL2]] | -0.54 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[UBAC1]] | -0.54 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[IARS2]] | -0.54 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[RPA1]] | -0.54 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[SNAPC3]] | -0.53 | -0.62 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CEACAM19's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHA6]] | B | PLEKHA6 activity raises CEACAM19's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.63× lower at baseline in the lines without PLEKHA6 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, -13.2); signed map (17.5, 5.4). **Vector** length 90.2, 17.7% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +8.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +3.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.9 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CEA cell adhesion molecule 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:44,662,278-44,684,359 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEAL1 |
| Gene groups (HGNC) | V-set domain containing; CEA cell adhesion molecule family |
| Matched by | ensembl_id |

UniProt [Q7Z692](https://www.uniprot.org/uniprotkb/Q7Z692) carries no function annotation.

**Summary**, from NCBI Gene [56971](https://www.ncbi.nlm.nih.gov/gene/56971):

> Predicted to be involved in heterophilic cell-cell adhesion and homophilic cell-cell adhesion. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31951) · Entrez [56971](https://www.ncbi.nlm.nih.gov/gene/56971) · UniProt [Q7Z692](https://www.uniprot.org/uniprotkb/Q7Z692) · Ensembl [ENSG00000186567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186567)

## Data

Gene col 11830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11830); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11830]; `tensor/DDL_lfc|DDL_z.npy` [11830]; `embed/gene_vectors.npy` [11830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11830 or target_col == 11830). Every well: [[CEACAM19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEACAM19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
