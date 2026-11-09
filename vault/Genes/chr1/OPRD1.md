---
symbol: "OPRD1"
type: "gene"
col: 3789
ensembl_id: "ENSG00000116329"
name: "opioid receptor delta 1"
location: "1p35.3"
module: 87
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 22
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 20
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# OPRD1

*opioid receptor delta 1* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.46× (z +19.2, q 0e+00, up in 8 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.112×, SW480 0.146×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.149×, SHP-77 0.173×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.117×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.235×); [[Panobinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.172×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEF1-AS1]] (+0.66, fdr 1e-05), [[FKBP9P1-1]] (+0.66, fdr 1e-05), [[LEF1]] (+0.65, fdr 1e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[FKBP9P1-1]] → it (grade B ⚠); 20 go from it, the strongest it → [[LINC02981]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.46×** | +19.2 | 0e+00 | 8/10 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **7.80×** | +15.0 | 0e+00 | 4/9 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.12×** | +12.7 | 1e-34 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.65×** | +12.6 | 3e-34 | 2/4 (SHP-77, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.12×** | +11.7 | 1e-29 | 6/12 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.31×** | +9.8 | 7e-21 | 1/4 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +6.9 | 4e-10 | 0/7 | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.60×** | +6.6 | 4e-09 | 4/13 (HEC-1-A, C-33 A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.0 | 1e-07 | 2/15 (PANC-1, C-33 A) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.0 | 4e-05 | 0/6 | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +4.9 | 5e-05 | 2/8 (SK-MEL-2, C32) | top dose only | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.50×** | +4.8 | 9e-05 | 2/7 (PANC-1, HEC-1-A) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **3.42×** | +4.7 | 1e-04 | 3/12 (HEC-1-A, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.30×** | +4.3 | 6e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.09×** | +4.3 | 7e-04 | 1/4 (SW480) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +4.0 | 0.002 | 2/10 (C-33 A, SW480) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.005 | 2/6 (C32, SK-MEL-2) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.006 | 4/14 (RPMI-7951, C-33 A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.04×** | +3.7 | 0.007 | 1/7 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.007 | 0/6 | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.011 | 0/9 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.012 | 0/15 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (SK-MEL-2 0.112×, SW480 0.146×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.149×, SHP-77 0.173×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.117×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.235×); [[Panobinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.172×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Finasteride (drug)]] 5 µM |  | 0.611× | -3.5 | 0.15 | 2/9 (HEC-1-A, CFPAC-1) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.625× | -3.5 | 0.15 | 1/15 (SW480) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.616× | -3.3 | 0.16 | 1/17 (HepG2/C3A) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.621× | -3.3 | 0.16 | 0/14 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.640× | -3.1 | 0.26 | 2/15 (HEC-1-A, NCI-H2030) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 42.5 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -11.8) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0896× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.821 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.724 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEF1-AS1]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[FKBP9P1-1]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LEF1]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[ANO4]] | +0.63 | +0.44 / +0.51 | both halves | 3e-05 | **novel candidate** |
| [[IL19]] | +0.63 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ST18]] | +0.62 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LINC01980]] | +0.60 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[ARNT2-DT]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FKBP9P1]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 | **novel candidate** |
| [[PROX1]] | +0.57 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[PTPRZ1]] | +0.56 | +0.30 / +0.30 | both halves | 2e-04 |  |
| [[LOXL4]] | +0.56 | +0.33 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises OPRD1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without FKBP9P1-1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers OPRD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PCSK1]] | C | PCSK1 activity raises OPRD1's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.84× lower at baseline in the lines without PCSK1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises OPRD1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.95× lower at baseline in the lines without SLC25A24P1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises OPRD1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without GABRG2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LAPTM5]] | C | LAPTM5 activity raises OPRD1's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without LAPTM5 | 0.048 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises OPRD1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.09× lower at baseline in the lines without AK4P3 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises OPRD1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.14× lower at baseline in the lines without CSMD3 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises OPRD1's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 1.85× lower at baseline in the lines without PSG1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises OPRD1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.81× lower at baseline in the lines without JAKMIP2-AS1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises OPRD1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.11× lower at baseline in the lines without POU6F2 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 14, C 6. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02981]] | B | OPRD1 activity raises LINC02981's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.19× lower at baseline in the lines without OPRD1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[RBM15-AS1]] | B | OPRD1 activity raises RBM15-AS1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.27× lower at baseline in the lines without OPRD1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[RAB17]] | B | OPRD1 activity raises RAB17's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.51× lower at baseline in the lines without OPRD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[COLGALT2]] | B | OPRD1 activity strengthens COLGALT2's drug response | lines that do not express OPRD1 (12) vs lines expressing it (12) | the lines without OPRD1 respond 0.86× as strongly (z diff +0.83); strongest at Homoharringtonine 0.5 µM: 0.49x vs 0.29x (z diff +3.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ATP6V0A4]] | B | OPRD1 activity raises ATP6V0A4's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without OPRD1 | 0.053 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[COLGALT2]] | B | OPRD1 activity raises COLGALT2's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without OPRD1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[HS3ST5]] | B | OPRD1 activity raises HS3ST5's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without OPRD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[TIRAP-AS1]] | B | OPRD1 activity raises TIRAP-AS1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.28× lower at baseline in the lines without OPRD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[G2E3-AS1]] | B | OPRD1 activity raises G2E3-AS1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.39× lower at baseline in the lines without OPRD1 | 0.075 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[RDH5]] | B | OPRD1 activity raises RDH5's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without OPRD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[LINC02254]] | B | OPRD1 activity raises LINC02254's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without OPRD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[NEIL1]] | B | OPRD1 activity raises NEIL1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.43× lower at baseline in the lines without OPRD1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.0, 42.0); signed map (64.7, 16.8). **Vector** length 28.5, 6.33% of its response variance represented; |z| ≥ 3 in 323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +19.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -3.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -0.9 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | opioid receptor delta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,812,170-28,871,267 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Opioid receptors |
| Reactome | 9 pathways, smallest: Peptide ligand-binding receptors; Interleukin-4 and Interleukin-13 signaling; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P41143](https://www.uniprot.org/uniprotkb/P41143) (Delta-type opioid receptor):

> G protein-coupled receptor that functions as a receptor for endogenous enkephalins and for a subset of other opioids. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors, such as adenylate cyclase. Signaling leads to the inhibition of adenylate cyclase activity. Inhibits neurotransmitter release by reducing calcium ion currents and increasing potassium ion conductance. Plays …

**Summary**, from NCBI Gene [4985](https://www.ncbi.nlm.nih.gov/gene/4985):

> Enables G protein-coupled enkephalin receptor activity. Involved in several processes, including G protein-coupled opioid receptor signaling pathway; cellular response to hypoxia; and regulation of mitochondrial membrane potential. Located in plasma membrane. Implicated in alcohol dependence; alcohol use disorder; drug dependence (multiple); opioid abuse; and withdrawal disorder. Biomarker of opioid abuse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8153) · Entrez [4985](https://www.ncbi.nlm.nih.gov/gene/4985) · UniProt [P41143](https://www.uniprot.org/uniprotkb/P41143) · Ensembl [ENSG00000116329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116329)

## Data

Gene col 3789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3789); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3789]; `tensor/DDL_lfc|DDL_z.npy` [3789]; `embed/gene_vectors.npy` [3789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3789 or target_col == 3789). Every well: [[OPRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
