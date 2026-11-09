---
symbol: "LRFN5"
type: "gene"
col: 9112
ensembl_id: "ENSG00000165379"
name: "leucine rich repeat and fibronectin type III domain containing 5"
location: "14q21.1"
module: 13
arm: "+"
pooled_cpm: 18.5
n_lines_expressing: 14
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LRFN5

*leucine rich repeat and fibronectin type III domain containing 5* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.89× (z +19.6, q 0e+00, up in 7 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.627× (z -4.8, q 9e-04, down in 7 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.65, fdr 1e-05), [[SHANK1]] (+0.64, fdr 1e-05), [[RDUR]] (+0.62, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 6 go from it, the strongest it → [[SH2B3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +19.6 | 0e+00 | 7/12 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.91×** | +15.5 | 0e+00 | 10/11 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +9.2 | 6e-18 | 0/9 | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +8.8 | 2e-16 | 0/11 | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +8.8 | 2e-16 | 1/10 (HS-578T) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +7.9 | 4e-13 | 10/12 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +7.1 | 1e-10 | 5/12 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +6.9 | 4e-10 | 5/12 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.4 | 1e-08 | 6/12 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +5.8 | 3e-07 | 5/12 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +4.9 | 5e-05 | 4/12 (SHP-77, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 1e-04 | 8/11 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.4 | 5e-04 | 6/12 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.4 | 5e-04 | 1/11 (NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.9 | 0.004 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.055 | 0/12 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.056 | 1/12 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.063 | 0/12 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9112.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.627×** | -4.8 | 9e-04 | 7/12 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.078 | 6/12 (HOP62, J82, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.078 | 2/12 (HOP62, NCI-H460) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.703× | -3.3 | 0.12 | 4/12 (HOP62, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.777× | -3.2 | 0.13 | 7/12 (HOP62, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.802× | -3.2 | 0.13 | 5/12 (CHP-212, HS-578T, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.568× | -3.0 | 0.18 | 1/12 (HOP62) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.727× | -3.0 | 0.18 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 70.3 | 0 | 14 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.223× (z -24.1) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.104× (z -12.8) |
| [[PANC-1 (line)]] | alt | 109 | 1 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.5) | [[Docetaxel (drug)]] 0.05 µM 0.256× (z -11.1) ⚠ transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.256× (z -11.1) |
| [[CHP-212 (line)]] | wt | 830 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 26.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +23.5) | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 8.12× (z +10.0) | — |
| [[J82 (line)]] | alt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +15.3) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 11.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +10.7) | [[Cepharanthine (drug)]] 0.5 µM 0.111× (z -9.1) |
| [[SNU-423 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +14.2) | — |
| [[A-172 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[RDUR]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[EVA1A]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EDARADD]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[AFF3]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[NALF1]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NTNG2]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GPR68]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NHSL2]] | +0.58 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[CSF1R]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ROBO4]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises LRFN5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers LRFN5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises LRFN5's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RGS4]] | C | RGS4 activity raises LRFN5's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 3.73× lower at baseline in the lines without RGS4 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises LRFN5's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.32× lower at baseline in the lines without CDH13 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises LRFN5's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 2.76× lower at baseline in the lines without CARD18 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH2B3]] | B | LRFN5 activity raises SH2B3's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without LRFN5 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1 |
| [[NALF1]] | C | LRFN5 activity raises NALF1's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 5.58× lower at baseline in the lines without LRFN5 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |
| [[CARD18]] | C | LRFN5 activity raises CARD18's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 2.22× lower at baseline in the lines without LRFN5 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |
| [[RDUR]] | C | LRFN5 activity raises RDUR's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without LRFN5 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |
| [[CDH13]] | C | LRFN5 activity raises CDH13's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 3.65× lower at baseline in the lines without LRFN5 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |
| [[MIR4527HG]] | C | LRFN5 activity raises MIR4527HG's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 2.11× lower at baseline in the lines without LRFN5 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.0, 12.9); signed map (18.7, 47.8). **Vector** length 57.2, 19.9% of its response variance represented; |z| ≥ 3 in 402 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +19.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.4 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +0.9 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.8 | +0.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and fibronectin type III domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:41,606,876-41,904,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FIGLER8, SALM5; previously C14orf146 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NI6](https://www.uniprot.org/uniprotkb/Q96NI6) (Leucine-rich repeat and fibronectin type-III domain-containing protein 5):

> Cell adhesion molecule that mediates homophilic cell-cell adhesion in a Ca(2+)-independent manner. Promotes neurite outgrowth in hippocampal neurons.

**Summary**, from NCBI Gene [145581](https://www.ncbi.nlm.nih.gov/gene/145581):

> This gene encodes a protein that belongs to the leucine-rich repeat and fibronectin type III domain-containing family of proteins. A similar protein in mouse, a glycosylated transmembrane protein, is thought to function in presynaptic differentiation. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:20360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20360) · Entrez [145581](https://www.ncbi.nlm.nih.gov/gene/145581) · UniProt [Q96NI6](https://www.uniprot.org/uniprotkb/Q96NI6) · Ensembl [ENSG00000165379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165379)

## Data

Gene col 9112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9112); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9112]; `tensor/DDL_lfc|DDL_z.npy` [9112]; `embed/gene_vectors.npy` [9112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9112 or target_col == 9112). Every well: [[LRFN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRFN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
