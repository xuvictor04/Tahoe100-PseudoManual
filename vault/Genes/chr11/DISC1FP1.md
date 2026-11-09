---
symbol: "DISC1FP1"
type: "gene"
col: 15358
ensembl_id: "ENSG00000261645"
name: "DISC1 fusion partner 1"
location: "11q14.3"
module: 9
arm: "+"
pooled_cpm: 33.54
n_lines_expressing: 21
n_dd_up: 47
n_dd_down: 0
n_dd_up_clean: 38
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DISC1FP1

*DISC1 fusion partner 1* — 11q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.70× (z +23.0, q 0e+00, up in 11 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (KATO III 0.197×, RPMI-7951 0.207×, SNU-1 0.327×, SK-MEL-2 0.336×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.0520×, SK-MEL-2 0.195×, KATO III 0.227×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.263×, KATO III 0.297×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSTL5]] (+0.83, fdr 7e-06), [[LINC01320]] (+0.72, fdr 1e-05), [[LINC01695]] (+0.70, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PYDC2-AS1]] → it (grade B ⚠); 9 go from it, the strongest it → [[LINC00882]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.70×** | +23.0 | 0e+00 | 11/19 (SHP-77, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.52×** | +18.7 | 0e+00 | 12/19 (SW 900, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +17.5 | 0e+00 | 10/18 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.51×** | +16.1 | 0e+00 | 18/19 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.6 | 5e-29 | 1/16 (C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.35×** | +10.6 | 3e-24 | 15/19 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +10.2 | 1e-22 | 3/15 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +10.2 | 1e-22 | 13/19 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +9.5 | 2e-19 | 6/16 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.15×** | +9.1 | 5e-18 | 8/18 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.99×** | +8.5 | 8e-16 | 2/19 (J82, C32) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +8.3 | 5e-15 | 12/19 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +7.8 | 3e-13 | 10/18 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +7.1 | 7e-11 | 12/19 (SK-MEL-2, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +6.2 | 2e-08 | 15/19 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.1 | 4e-08 | 2/18 (NCI-H23, SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +5.4 | 2e-06 | 12/19 (PANC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +5.2 | 6e-06 | 8/20 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15358.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (KATO III 0.197×, RPMI-7951 0.207×, SNU-1 0.327×, SK-MEL-2 0.336×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.0520×, SK-MEL-2 0.195×, KATO III 0.227×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.263×, KATO III 0.297×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.754× | -3.5 | 0.24 | 5/19 (KATO III, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.2 | 0.36 | 0/19 | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.785× | -3.0 | 0.42 | 5/19 (NCI-H2030, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 237 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.69× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -21.1) |
| [[SK-MEL-2 (line)]] | alt | 766 | 7 (2 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.60× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -12.9) |
| [[C32 (line)]] | wt | 26.0 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.26× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 287 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0520× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -13.3) |
| [[PANC-1 (line)]] | alt | 9.39 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 30.3× (z +17.2) | — |
| [[A-172 (line)]] | wt | 12.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.5× (z +17.2) | — |
| [[HepG2_C3A (line)]] | wt | 136 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.37× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 162 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.62× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -14.6) |
| [[SHP-77 (line)]] | alt | 67.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 9.11 | 2 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.76× (z +11.6) ⚠ position not correctable · without an alert: [[Auranofin (drug)]] 5 µM 21.3× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 9.86 | 2 | 0 | [[Auranofin (drug)]] 5 µM 24.2× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 8.39 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.18× (z +10.9) | — |
| [[J82 (line)]] | alt | 8.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.95× (z +8.9) ⚠ position not correctable | — |
| [[NCI-H661 (line)]] | alt | 559 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.13 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.77 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSTL5]] | +0.83 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC01320]] | +0.72 | +0.69 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[LINC01695]] | +0.70 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[ANKRD30B]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LINC02241]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[FAM110B]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ITGBL1]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[EPHA5]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A48]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[LINC02484]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYDC2-AS1]] | B | PYDC2-AS1 activity raises DISC1FP1's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 3.80× lower at baseline in the lines without PYDC2-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[LINC00698]] | C | LINC00698 activity raises DISC1FP1's level | lines that do not express LINC00698 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without LINC00698 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253642, HEPH, SRRM4; maybe low, not absent; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises DISC1FP1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 4.94× lower at baseline in the lines without FSTL5 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises DISC1FP1's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without NR1H4 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[LINC02327]] | C | LINC02327 activity raises DISC1FP1's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 2.49× lower at baseline in the lines without LINC02327 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605; co-absent with the target |
| [[RERG]] | C | RERG activity raises DISC1FP1's level | lines that do not express RERG (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without RERG | 0.0999 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00882]] | B | DISC1FP1 activity raises LINC00882's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without DISC1FP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574 |
| [[KCNH1]] | B | DISC1FP1 activity raises KCNH1's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 1.70× lower at baseline in the lines without DISC1FP1 | 0.035 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574 |
| [[LINC01933]] | B | DISC1FP1 activity raises LINC01933's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without DISC1FP1 | 0.0998 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574 |
| [[NFASC]] | C | DISC1FP1 activity raises NFASC's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.94× lower at baseline in the lines without DISC1FP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[ID4]] | C | DISC1FP1 activity raises ID4's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 3.23× lower at baseline in the lines without DISC1FP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[CTNNA2]] | C | DISC1FP1 activity raises CTNNA2's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 3.35× lower at baseline in the lines without DISC1FP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[FAM133A]] | C | DISC1FP1 activity raises FAM133A's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without DISC1FP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[FSTL5]] | C | DISC1FP1 activity raises FSTL5's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without DISC1FP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[ANKRD30B]] | C | DISC1FP1 activity raises ANKRD30B's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without DISC1FP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 27.3); signed map (38.6, 26.4). **Vector** length 59.4, 15.3% of its response variance represented; |z| ≥ 3 in 543 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +18.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -3.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | DISC1 fusion partner 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.3 — chr11:90,251,204-90,915,052 (+) |
| Ensembl biotype | lncRNA |
| Also known as | Boymaw |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33625) · Entrez [101929222](https://www.ncbi.nlm.nih.gov/gene/101929222) · Ensembl [ENSG00000261645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261645)

## Data

Gene col 15358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15358); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15358]; `tensor/DDL_lfc|DDL_z.npy` [15358]; `embed/gene_vectors.npy` [15358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15358 or target_col == 15358). Every well: [[DISC1FP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DISC1FP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
