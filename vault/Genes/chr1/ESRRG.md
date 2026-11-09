---
symbol: "ESRRG"
type: "gene"
col: 12218
ensembl_id: "ENSG00000196482"
name: "estrogen related receptor gamma"
location: "1q41"
module: 9
arm: "+"
pooled_cpm: 12.71
n_lines_expressing: 24
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 19
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ESRRG

*estrogen related receptor gamma* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.77× (z +18.8, q 0e+00, up in 8 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.515× (z -6.3, q 1e-07, down in 13 of 19 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRXN1]] (+0.69, fdr 7e-06), [[SYT4]] (+0.67, fdr 7e-06), [[SRRM4]] (+0.66, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[RUNX1T1]] → it (grade C ⚠); 5 go from it, the strongest it → [[RORA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.77×** | +18.8 | 0e+00 | 8/18 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.65×** | +13.8 | 1e-40 | 16/20 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +11.2 | 9e-27 | 3/10 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +11.2 | 9e-27 | 8/18 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +8.5 | 3e-15 | 4/12 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +7.0 | 2e-10 | 16/20 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.96×** | +6.7 | 2e-09 | 5/20 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +6.5 | 7e-09 | 12/20 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +6.3 | 2e-08 | 14/20 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +5.2 | 1e-05 | 15/20 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +5.1 | 2e-05 | 11/19 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 2/18 (NCI-H661, NCI-H460) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.4 | 5e-04 | 3/19 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +4.3 | 6e-04 | 13/19 (NCI-H460, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.002 | 9/20 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.005 | 10/19 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.033 | 2/20 (H4, HT-29) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.033 | 4/19 (BT-474, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -6.3 | 1e-07 | 13/19 (SHP-77, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -4.6 | 0.001 | 12/20 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -4.5 | 0.002 | 8/20 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.645×** | -4.4 | 0.002 | 10/20 (A498, SHP-77, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.663×** | -4.1 | 0.004 | 8/19 (SHP-77, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.028 | 6/19 (SHP-77, CHP-212, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.042 | 13/20 (SHP-77, CHP-212, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.710×** | -3.4 | 0.042 | 7/18 (SHP-77, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -3.4 | 0.045 | 11/19 (SW 900, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ivermectin (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.055 | 0/21 | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.719× | -3.1 | 0.11 | 4/20 (NCI-H460, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 389 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0863× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 3.51 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.95× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0570× (z -17.1) |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.5) |
| [[A-172 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRXN1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SYT4]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SRRM4]] | +0.66 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RIT2]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ASCL1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[LRFN2]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[FUT9]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[DGKB]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GRIK1]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SNTG1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RUNX1T1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RUNX1T1]] | C | RUNX1T1 activity raises ESRRG's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 4.81× lower at baseline in the lines without RUNX1T1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[FOXP2]] | C | FOXP2 activity raises ESRRG's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without FOXP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises ESRRG's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.31× lower at baseline in the lines without SNTG1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises ESRRG's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without LINC02197 | 0.022 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises ESRRG's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.85× lower at baseline in the lines without IGFBP5 | 0.026 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises ESRRG's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.36× lower at baseline in the lines without ASCL1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[CGA]] | C | CGA activity raises ESRRG's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.43× lower at baseline in the lines without CGA | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises ESRRG's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 4.11× lower at baseline in the lines without LINC01456 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises ESRRG's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without TSHZ2 | 0.049 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises ESRRG's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.31× lower at baseline in the lines without RIT2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises ESRRG's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 5.18× lower at baseline in the lines without FUT9 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[PPARGC1A]] | C | PPARGC1A activity raises ESRRG's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without PPARGC1A | 0.053 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RORA]] | B | ESRRG activity raises RORA's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without ESRRG | 0.029 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent |
| [[PBX1]] | B | ESRRG activity raises PBX1's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 2.67× lower at baseline in the lines without ESRRG | 0.074 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent |
| [[ADGRV1]] | C | ESRRG activity raises ADGRV1's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 2.78× lower at baseline in the lines without ESRRG | 0.020 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent; co-absent with the target |
| [[RUNX1T1]] | C | ESRRG activity raises RUNX1T1's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 3.36× lower at baseline in the lines without ESRRG | 0.038 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent; co-absent with the target |
| [[CXXC4]] | C | ESRRG activity raises CXXC4's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without ESRRG | 0.048 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 36.8); signed map (44.6, 33.6). **Vector** length 61.7, 17.3% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.50 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +18.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | -1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | estrogen related receptor gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:216,503,246-217,137,755 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NR3B3, ERRg, ERR-gamma |
| Gene groups (HGNC) | Estrogen related receptors |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P62508](https://www.uniprot.org/uniprotkb/P62508) (Estrogen-related receptor gamma):

> Orphan receptor that acts as a transcription activator in the absence of bound ligand. Binds specifically to an estrogen response element and activates reporter genes controlled by estrogen response elements (By similarity). Induces the expression of PERM1 in the skeletal muscle.

**Summary**, from NCBI Gene [2104](https://www.ncbi.nlm.nih.gov/gene/2104):

> This gene encodes a member of the estrogen receptor-related receptor (ESRR) family, which belongs to the nuclear hormone receptor superfamily. All members of the ESRR family share an almost identical DNA binding domain, which is composed of two C4-type zinc finger motifs. The ESRR members are orphan nuclear receptors; they bind to the estrogen response element and steroidogenic factor 1 response element, and activate genes controlled by both response elements in the absence of any ligands. The …

**Accessions** — [HGNC:3474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3474) · Entrez [2104](https://www.ncbi.nlm.nih.gov/gene/2104) · UniProt [P62508](https://www.uniprot.org/uniprotkb/P62508) · Ensembl [ENSG00000196482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196482)

## Data

Gene col 12218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12218); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12218]; `tensor/DDL_lfc|DDL_z.npy` [12218]; `embed/gene_vectors.npy` [12218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12218 or target_col == 12218). Every well: [[ESRRG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESRRG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
