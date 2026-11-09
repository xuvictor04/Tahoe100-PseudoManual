---
symbol: "ADGRV1"
type: "gene"
col: 8901
ensembl_id: "ENSG00000164199"
name: "adhesion G protein-coupled receptor V1"
location: "5q14.3"
module: 9
arm: "+"
pooled_cpm: 25.99
n_lines_expressing: 34
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADGRV1

*adhesion G protein-coupled receptor V1* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.89× (z +25.9, q 0e+00, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Mebendazole (drug)]] 5 µM: 0.746× (z -4.9, q 6e-04, down in 5 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.104×); [[Tadalafil (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0509×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.204×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02223]] (+0.63, fdr 7e-06), [[ADGRL3]] (+0.63, fdr 1e-05), [[PCDH9]] (+0.61, fdr 7e-06); moves opposite to [[ARMC10]] (-0.46, fdr 8e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[SOX6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.89×** | +25.9 | 0e+00 | 27/32 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +25.6 | 0e+00 | 21/31 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +16.7 | 0e+00 | 22/32 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +14.9 | 0e+00 | 24/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +14.7 | 0e+00 | 13/23 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +13.6 | 2e-40 | 18/31 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +13.5 | 6e-40 | 23/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +13.5 | 7e-40 | 12/19 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +12.0 | 3e-31 | 21/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +11.8 | 3e-30 | 20/31 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +10.8 | 1e-25 | 7/20 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.83×** | +10.4 | 1e-23 | 12/31 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.9 | 3e-17 | 9/32 (HOP62, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.7 | 2e-16 | 13/29 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +8.2 | 1e-14 | 14/31 (HS-578T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.5 | 2e-12 | 6/28 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.6 | 1e-09 | 11/30 (SW48, HS-578T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.7 | 5e-07 | 15/29 (NCI-H1573, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8901.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.104×); [[Tadalafil (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0509×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.746×** | -4.9 | 6e-04 | 5/32 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.764×** | -4.7 | 9e-04 | 13/30 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -3.9 | 0.018 | 14/32 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.825× | -3.3 | 0.12 | 11/31 (SW480, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.2 | 0.15 | 2/33 (hTERT-HPNE, SW 1088) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.823× | -3.1 | 0.15 | 2/31 (COLO 205, C-33 A) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.830× | -3.1 | 0.15 | 7/30 (C32, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.2 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 9.34× (z +20.5) | — |
| [[SW480 (line)]] | alt | 21.4 | 6 | 1 | [[Tucidinostat (drug)]] 5 µM 4.18× (z +16.7) | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -10.3) |
| [[J82 (line)]] | alt | 17.6 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.07× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 11.8 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.17× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.36× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 42.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.16× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.39× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.115× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 8.23 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 5.14× (z +11.3) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.104× (z -11.0) |
| [[HS-578T (line)]] | alt | 19.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +22.9) | — |
| [[SK-MEL-2 (line)]] | alt | 7.73 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +9.7) | [[Tadalafil (drug)]] 0.05 µM 0.0509× (z -10.9) |
| [[H4 (line)]] | wt | 43.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.48× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.15× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 7.91 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.66× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 6.96 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0618× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 7.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.4) | — |
| [[NCI-H661 (line)]] | alt | 758 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -10.8) |
| [[A-172 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02223]] | +0.63 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[ADGRL3]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[PCDH9]] | +0.61 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SYT1]] | +0.60 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[MARCHF1]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MIR325HG]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[SLC7A8]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 | STRING 439 |
| [[LRP2]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.58 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[SPINK5]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC10]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADGRV1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RUNX1T1]] | B | RUNX1T1 activity raises ADGRV1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.21× lower at baseline in the lines without RUNX1T1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[FUT9]] | B | FUT9 activity raises ADGRV1's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.00× lower at baseline in the lines without FUT9 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[PPARGC1A]] | B | PPARGC1A activity raises ADGRV1's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without PPARGC1A | 0.089 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SLC7A8]] | B | SLC7A8 activity raises ADGRV1's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without SLC7A8 | 0.0997 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[ESRRG]] | C | ESRRG activity raises ADGRV1's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 2.78× lower at baseline in the lines without ESRRG | 0.020 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX6]] | B | ADGRV1 activity raises SOX6's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without ADGRV1 | 0.052 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[LINC00298]] | B | ADGRV1 activity raises LINC00298's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without ADGRV1 | 0.055 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[PPARGC1A]] | B | ADGRV1 activity raises PPARGC1A's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without ADGRV1 | 0.064 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[SLC7A8]] | B | ADGRV1 activity raises SLC7A8's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without ADGRV1 | 0.069 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[TNFRSF19]] | B | ADGRV1 activity raises TNFRSF19's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without ADGRV1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| cells under [[PH-797804 (drug)]] 0.5 µM | B | ADGRV1 activity lowers the cells' numbers under PH-797804 0.5 µM (makes them more sensitive) | lines that do not express ADGRV1 (16) vs lines expressing it (32) | the lines without ADGRV1: 1.29× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[PLCB1]] | B | ADGRV1 activity raises PLCB1's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without ADGRV1 | 0.087 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| cells under [[PH-797804 (drug)]] 0.05 µM | B | ADGRV1 activity raises the cells' numbers under PH-797804 0.05 µM (protects the cells) | lines that do not express ADGRV1 (16) vs lines expressing it (32) | the lines without ADGRV1: 0.85× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| cells under [[Ipatasertib (drug)]] 0.5 µM | B | ADGRV1 activity lowers the cells' numbers under Ipatasertib 0.5 µM (makes them more sensitive) | lines that do not express ADGRV1 (16) vs lines expressing it (32) | the lines without ADGRV1: 1.43× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[ESRRG]] | C | ADGRV1 activity raises ESRRG's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without ADGRV1 | 0.087 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, 34.5); signed map (41.8, 35.9). **Vector** length 60.8, 11.6% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +25.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor V1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:90,529,344-91,164,437 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761P0710, KIAA0686, FEB4, VLGR1; previously USH2C, MASS1, GPR98 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily V; USH2 complex |
| Reactome | 2 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXG9](https://www.uniprot.org/uniprotkb/Q8WXG9) (Adhesion G protein-coupled receptor V1):

> G protein-coupled receptor which has an essential role in the development of hearing and vision. Couples to G-alpha(i)-proteins, GNAI1/2/3, G-alpha(q)-proteins, GNAQ, as well as G-alpha(s)-proteins, GNAS, inhibiting adenylate cyclase (AC) activity and cAMP production. Required for the hair bundle ankle formation, which connects growing stereocilia in developing cochlear hair cells of the inner ear. In response to extracellular calcium, activates kinases PKA and PKC to regulate myelination by …

**Summary**, from NCBI Gene [84059](https://www.ncbi.nlm.nih.gov/gene/84059):

> This gene encodes a member of the G-protein coupled receptor superfamily. The encoded protein contains a 7-transmembrane receptor domain, binds calcium and is expressed in the central nervous system. Mutations in this gene are associated with Usher syndrome 2 and familial febrile seizures. Several alternatively spliced transcripts have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17416) · Entrez [84059](https://www.ncbi.nlm.nih.gov/gene/84059) · UniProt [Q8WXG9](https://www.uniprot.org/uniprotkb/Q8WXG9) · Ensembl [ENSG00000164199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164199)

## Data

Gene col 8901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8901); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8901]; `tensor/DDL_lfc|DDL_z.npy` [8901]; `embed/gene_vectors.npy` [8901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8901 or target_col == 8901). Every well: [[ADGRV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
