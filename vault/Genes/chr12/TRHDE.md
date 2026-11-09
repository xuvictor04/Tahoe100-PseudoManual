---
symbol: "TRHDE"
type: "gene"
col: 1025
ensembl_id: "ENSG00000072657"
name: "thyrotropin releasing hormone degrading enzyme"
location: "12q21.1"
module: 202
arm: "+"
pooled_cpm: 10.9
n_lines_expressing: 24
n_dd_up: 44
n_dd_down: 1
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# TRHDE

*thyrotropin releasing hormone degrading enzyme* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.19× (z +42.2, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.821× (z -4.0, q 0.032, down in 5 of 20 measured lines) ⚠ cell-cycle shift, explains ~7% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0812×; ⚠ transcription drop; cell-cycle shift, explains ~41% of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01116]] (+0.71, fdr 1e-05), [[ANKRD18B]] (+0.67, fdr 6e-05), [[CACNA2D1]] (+0.67, fdr 2e-05); moves opposite to [[YIPF1]] (-0.60, fdr 5e-05), [[RNF41]] (-0.59, fdr 4e-05), [[CABLES2]] (-0.59, fdr 1e-04).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RGS20]] → it (grade B ⚠); 2 go from it, the strongest it → [[TAFA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.19×** | +42.2 | 0e+00 | 16/19 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.83×** | +38.5 | 0e+00 | 18/19 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.46×** | +21.2 | 0e+00 | 12/20 (SW 900, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.00×** | +21.1 | 0e+00 | 7/11 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.37×** | +20.9 | 0e+00 | 14/19 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.29×** | +16.6 | 0e+00 | 11/20 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.25×** | +16.1 | 0e+00 | 17/20 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +14.0 | 2e-42 | 12/19 (LS 180, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +13.9 | 2e-42 | 7/15 (SNU-423, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +12.7 | 3e-35 | 7/19 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +12.6 | 2e-34 | 5/10 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.25×** | +11.5 | 6e-29 | 5/19 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +11.4 | 3e-28 | 9/18 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +7.8 | 2e-13 | 8/19 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +7.8 | 2e-13 | 10/20 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +6.7 | 7e-10 | 4/20 (SW1417, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +5.1 | 8e-06 | 2/19 (SW 900, NCI-H1792) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +4.6 | 9e-05 | 6/19 (CFPAC-1, SNU-423, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1025.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0812×; ⚠ transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.821×** | -4.0 | 0.032 | 5/20 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.787× | -3.4 | 0.13 | 1/19 (SW 900) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.718× | -3.4 | 0.13 | 3/20 (NCI-H1792, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.802× | -3.2 | 0.20 | 2/19 (SHP-77, RPMI-7951) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.20 | 3/20 (SHP-77, J82, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.798× | -3.1 | 0.20 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.1) | — |
| [[J82 (line)]] | alt | 4.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.78× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 3.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0812× (z -12.4) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 7.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 3.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 3.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +9.3) | — |
| [[A-172 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01116]] | +0.71 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD18B]] | +0.67 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[CACNA2D1]] | +0.67 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | +0.65 | +0.61 / +0.34 | both halves | 1e-04 |  |
| [[CUBN]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[FLRT2]] | +0.64 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[PPP1R1C]] | +0.63 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ADAMTS3]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SYNPO2]] | +0.63 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[COL21A1]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DRAIC]] | +0.62 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[BMPR1B]] | +0.62 | +0.54 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF1]] | -0.60 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[RNF41]] | -0.59 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[CABLES2]] | -0.59 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[MKRN2]] | -0.59 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[WRAP73]] | -0.58 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[MYPOP]] | -0.58 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[DHTKD1]] | -0.56 | -0.50 / -0.26 | both halves | 3e-04 |  |
| [[SDHAP1]] | -0.56 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[MPG]] | -0.56 | -0.64 / -0.29 | both halves | 3e-04 |  |
| [[DPY30]] | -0.56 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.56 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[LRRC42]] | -0.56 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS20]] | B | RGS20 activity raises TRHDE's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without RGS20 | 0.026 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[TOP2A]] | B | TOP2A activity lowers TRHDE's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACNA2D1]] | B | CACNA2D1 activity raises TRHDE's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without CACNA2D1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[SLC4A4]] | C | SLC4A4 activity raises TRHDE's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 1.64× lower at baseline in the lines without SLC4A4 | 0.055 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises TRHDE's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without NEGR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[ITGBL1]] | C | ITGBL1 activity raises TRHDE's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without ITGBL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[ADAMTS3]] | C | ADAMTS3 activity raises TRHDE's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.81× lower at baseline in the lines without ADAMTS3 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAFA5]] | B | TRHDE activity lowers TAFA5's level | lines that do not express TRHDE (26) vs lines expressing it (24) | 1.66× higher at baseline in the lines without TRHDE | 0.068 | ⚠ within organs, on part of the lines; also absent: ZSCAN23, SAMD3, ITGA11; maybe low, not absent |
| [[SLC4A4]] | C | TRHDE activity raises SLC4A4's level | lines that do not express TRHDE (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without TRHDE | 0.069 | ⚠ within organs, on part of the lines; also absent: ZSCAN23, SAMD3, ITGA11; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.6, 15.6); signed map (43.9, 24.5). **Vector** length 49.1, 11.3% of its response variance represented; |z| ≥ 3 in 456 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +38.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +42.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +21.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +16.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +21.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | thyrotropin releasing hormone degrading enzyme |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:72,087,266-72,670,758 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGPEP2, TRH-DE, PAP-II |
| Gene groups (HGNC) | M1 metallopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKU6](https://www.uniprot.org/uniprotkb/Q9UKU6) (Thyrotropin-releasing hormone-degrading ectoenzyme):

> Specific inactivation of TRH after its release.

**Summary**, from NCBI Gene [29953](https://www.ncbi.nlm.nih.gov/gene/29953):

> This gene encodes a member of the peptidase M1 family. The encoded protein is an extracellular peptidase that specifically cleaves and inactivates the neuropeptide thyrotropin-releasing hormone.[provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:30748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30748) · Entrez [29953](https://www.ncbi.nlm.nih.gov/gene/29953) · UniProt [Q9UKU6](https://www.uniprot.org/uniprotkb/Q9UKU6) · Ensembl [ENSG00000072657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072657)

## Data

Gene col 1025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1025); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1025]; `tensor/DDL_lfc|DDL_z.npy` [1025]; `embed/gene_vectors.npy` [1025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1025 or target_col == 1025). Every well: [[TRHDE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRHDE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
