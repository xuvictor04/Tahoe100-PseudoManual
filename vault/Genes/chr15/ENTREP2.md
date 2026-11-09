---
symbol: "ENTREP2"
type: "gene"
col: 2410
ensembl_id: "ENSG00000104059"
name: "endosomal transmembrane epsin interactor 2"
location: "15q13.1"
module: 115
arm: "+"
pooled_cpm: 18.9
n_lines_expressing: 28
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 10
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# ENTREP2

*endosomal transmembrane epsin interactor 2* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.10× (z +24.2, q 0e+00, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.678× (z -5.9, q 3e-06, down in 16 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS19]] (+0.66, fdr 7e-06), [[NCALD]] (+0.65, fdr 2e-05), [[LINC02832]] (+0.62, fdr 1e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[EPB41L4A]] → it (grade B ⚠); 10 go from it, the strongest it → [[NMNAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.10×** | +24.2 | 0e+00 | 23/25 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +19.9 | 0e+00 | 13/25 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +16.4 | 0e+00 | 7/20 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +12.6 | 5e-34 | 20/25 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +12.3 | 7e-33 | 6/14 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +11.9 | 9e-31 | 14/25 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +11.7 | 8e-30 | 3/15 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.13×** | +11.4 | 3e-28 | 15/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +7.7 | 7e-13 | 17/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +7.4 | 1e-11 | 13/25 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.52×** | +6.4 | 1e-08 | 12/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.49×** | +5.8 | 3e-07 | 4/25 (NCI-H460, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +4.9 | 4e-05 | 7/25 (NCI-H460, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.5 | 3e-04 | 1/24 (C32) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 3e-04 | 9/24 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.007 | 14/26 (NCI-H460, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.007 | 2/25 (SW 900, SW480) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.011 | 10/25 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.055 | 2/25 (SW480, COLO 205) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -5.9 | 3e-06 | 16/25 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -5.5 | 1e-05 | 15/25 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.790×** | -5.0 | 9e-05 | 12/25 (COLO 205, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -4.4 | 0.002 | 16/25 (LoVo, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clotrimazole (drug)]] 5 µM |  | 0.835× | -3.9 | 0.011 | 5/25 (BT-474, J82, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.835× | -3.8 | 0.011 | 6/26 (SW48, SW 900, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.6 | 0.030 | 2/26 (NCI-H2030, NCI-H23) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.064 | 15/25 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.072 | 3/25 (Hs 766T, HOP62, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.088 | 0/25 | rises with dose |  |
| [[BI-78D3 (drug)]] 0.05 µM |  | **0.804×** | -3.1 | 0.095 | 2/24 (AN3 CA, SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.26 | 9 (5 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 17.5× (z +18.9) | — |
| [[SW480 (line)]] | alt | 35.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.1) |
| [[C-33 A (line)]] | alt | 137 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.4) |
| [[LoVo (line)]] | wt | 113 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.96× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.180× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 6.20 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.80× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 9.36 | 5 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.06× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 131 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 11.0× (z +16.0) | — |
| [[A549 (line)]] | wt | 19.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +13.2) | — |
| [[A-427 (line)]] | wt | 25.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.19× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 18.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.11× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.40× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.44× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 32.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.79× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 5.68 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.69× (z +9.2) | — |
| [[A-172 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS19]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[NCALD]] | +0.65 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[LINC02832]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[HS6ST3]] | +0.60 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HUNK]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SUSD4]] | +0.59 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[IQGAP2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ROR2]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NELL2]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.57 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[VWA2]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NKD2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4A]] | B | EPB41L4A activity raises ENTREP2's level | lines that do not express EPB41L4A (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without EPB41L4A | 0.052 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, ANKRD20A11P |
| [[LINC02832]] | B | LINC02832 activity raises ENTREP2's level | lines that do not express LINC02832 (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without LINC02832 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000235337, ENSG00000288902, ENSG00000239498 |
| [[NELL2]] | B | NELL2 activity raises ENTREP2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.20× lower at baseline in the lines without NELL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[MED12L]] | B | MED12L activity raises ENTREP2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without MED12L | 0.072 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[AXIN2]] | B | AXIN2 activity raises ENTREP2's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.93× lower at baseline in the lines without AXIN2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[NUDT11]] | B | NUDT11 activity raises ENTREP2's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.12× lower at baseline in the lines without NUDT11 | 0.084 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |
| [[BMP7]] | B | BMP7 activity raises ENTREP2's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without BMP7 | 0.087 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[PTPRZ1]] | B | PTPRZ1 activity raises ENTREP2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 1.94× lower at baseline in the lines without PTPRZ1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[CACNA1D]] | C | CACNA1D activity raises ENTREP2's level | lines that do not express CACNA1D (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without CACNA1D | 0.037 | ⚠ within organs, on part of the lines; also absent: TESC, ENSG00000291189, CDX2; maybe low, not absent; co-absent with the target |
| [[RET]] | C | RET activity raises ENTREP2's level | lines that do not express RET (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without RET | 0.045 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[HS6ST3]] | C | HS6ST3 activity raises ENTREP2's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without HS6ST3 | 0.051 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMNAT3]] | B | ENTREP2 activity raises NMNAT3's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without ENTREP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[ZNF704]] | B | ENTREP2 activity raises ZNF704's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without ENTREP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[SUSD4]] | B | ENTREP2 activity raises SUSD4's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without ENTREP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[PAX5]] | B | ENTREP2 activity raises PAX5's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without ENTREP2 | 0.081 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[LINC02832]] | B | ENTREP2 activity raises LINC02832's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without ENTREP2 | 0.087 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[MED12L]] | B | ENTREP2 activity raises MED12L's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without ENTREP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[UNC80]] | B | ENTREP2 activity raises UNC80's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without ENTREP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[IGFL4]] | C | ENTREP2 activity raises IGFL4's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without ENTREP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent; co-absent with the target |
| [[INHBB]] | C | ENTREP2 activity raises INHBB's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without ENTREP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent; co-absent with the target |
| [[ROR2]] | C | ENTREP2 activity raises ROR2's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 3.03× lower at baseline in the lines without ENTREP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.8, 41.1); signed map (55.3, 15.9). **Vector** length 67.0, 16.4% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +24.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.7 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.4 | -5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | endosomal transmembrane epsin interactor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.1 — chr15:29,120,252-29,570,979 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0574, TMEM228; previously FAM189A1 |
| Matched by | ensembl_id |

UniProt [O60320](https://www.uniprot.org/uniprotkb/O60320) carries no function annotation.

**Summary**, from NCBI Gene [23359](https://www.ncbi.nlm.nih.gov/gene/23359):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29075) · Entrez [23359](https://www.ncbi.nlm.nih.gov/gene/23359) · UniProt [O60320](https://www.uniprot.org/uniprotkb/O60320) · Ensembl [ENSG00000104059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104059)

## Data

Gene col 2410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2410); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2410]; `tensor/DDL_lfc|DDL_z.npy` [2410]; `embed/gene_vectors.npy` [2410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2410 or target_col == 2410). Every well: [[ENTREP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTREP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
