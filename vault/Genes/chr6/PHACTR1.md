---
symbol: "PHACTR1"
type: "gene"
col: 3323
ensembl_id: "ENSG00000112137"
name: "phosphatase and actin regulator 1"
location: "6p24.1"
module: 121
arm: "+"
pooled_cpm: 44.64
n_lines_expressing: 15
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 22
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# PHACTR1

*phosphatase and actin regulator 1* — 6p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.65× (z +19.8, q 0e+00, up in 6 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.28× (z +15.6, q 0e+00, up in 5 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.743× (z -4.0, q 0.038, down in 2 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.145×, J82 0.354×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 0.0871×, LOX-IMVI 0.142×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.118×, J82 0.155×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.137×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.122×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSR1]] (+0.68, fdr 7e-06), [[DOCK10]] (+0.65, fdr 1e-05), [[NETO1]] (+0.62, fdr 1e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC01828]] → it (grade B ⚠); 22 go from it, the strongest it → [[SLC9A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.65×** | +19.8 | 0e+00 | 6/11 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.39×** | +16.4 | 0e+00 | 4/12 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +15.6 | 0e+00 | 5/13 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +14.9 | 0e+00 | 10/13 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +11.4 | 7e-28 | 8/13 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +8.9 | 5e-17 | 4/12 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.88×** | +8.4 | 3e-15 | 6/13 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 3e-10 | 6/12 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.5 | 6e-09 | 3/12 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.7 | 8e-07 | 9/13 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +5.2 | 8e-06 | 7/13 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 0/13 | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 3e-05 | 7/13 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.4 | 5e-04 | 6/12 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.001 | 3/12 (HOP62, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.002 | 7/12 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.003 | 0/12 | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.012 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.023 | 2/12 (SNU-423, SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3323.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.145×, J82 0.354×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (J82 0.0871×, LOX-IMVI 0.142×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.118×, J82 0.155×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.137×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.743×** | -4.0 | 0.038 | 2/13 (A-172, SW 1088) | two highest doses |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | 0.776× | -3.4 | 0.14 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.766× | -3.3 | 0.14 | 0/12 | inconsistent across doses |  |
| [[Delamanid (drug)]] 0.05 µM |  | 0.784× | -3.3 | 0.14 | 0/13 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.793× | -3.1 | 0.20 | 0/13 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.1 | 0.20 | 1/13 (NCI-H23) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.798× | -3.0 | 0.20 | 3/13 (H4, J82, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 579 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.6) |
| [[J82 (line)]] | alt | 800 | 1 | 9 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -11.3) |
| [[A-172 (line)]] | wt | 14.0 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +15.0) | [[Menadione (drug)]] 0.05 µM 0.136× (z -9.5) |
| [[HOP62 (line)]] | alt | 13.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 96.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +18.4) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.128× (z -11.6) ⚠ cell-cycle shift, explains ~3% of this change |
| [[RPMI-7951 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +8.8) | — |
| [[A-427 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSR1]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[DOCK10]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NETO1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MIR4307HG]] | +0.60 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[ZFHX4]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC02945]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[LINC02241]] | +0.58 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[PSG5]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[LINC01776]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[FBN2]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SYT14]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[FAP]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01828]] | B | LINC01828 activity raises PHACTR1's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without LINC01828 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent |
| [[PSG5]] | C | PSG5 activity raises PHACTR1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 5.27× lower at baseline in the lines without PSG5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises PHACTR1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.59× lower at baseline in the lines without DSCAM | 0.021 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises PHACTR1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.92× lower at baseline in the lines without PSG4 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[PRKG1]] | C | PRKG1 activity raises PHACTR1's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without PRKG1 | 0.049 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises PHACTR1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.16× lower at baseline in the lines without MAGI2-AS3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises PHACTR1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without ADAMTS12 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises PHACTR1's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 4.42× lower at baseline in the lines without APBB1IP | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 6, C 16. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC9A9]] | B | PHACTR1 activity raises SLC9A9's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 1.78× lower at baseline in the lines without PHACTR1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[LINC01828]] | B | PHACTR1 activity raises LINC01828's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 3.42× lower at baseline in the lines without PHACTR1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[SLC8A1-AS1]] | B | PHACTR1 activity raises SLC8A1-AS1's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 1.58× lower at baseline in the lines without PHACTR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[CALD1]] | B | PHACTR1 activity raises CALD1's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 4.36× lower at baseline in the lines without PHACTR1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[C12orf50]] | B | PHACTR1 activity raises C12orf50's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without PHACTR1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[LINC00882]] | B | PHACTR1 activity raises LINC00882's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 4.17× lower at baseline in the lines without PHACTR1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[MAGI2-AS3]] | C | PHACTR1 activity raises MAGI2-AS3's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 5.73× lower at baseline in the lines without PHACTR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[LINC00702]] | C | PHACTR1 activity raises LINC00702's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 4.52× lower at baseline in the lines without PHACTR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[ADAMTS12]] | C | PHACTR1 activity raises ADAMTS12's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 6.41× lower at baseline in the lines without PHACTR1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[ANKRD30B]] | C | PHACTR1 activity raises ANKRD30B's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 3.62× lower at baseline in the lines without PHACTR1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[LINC02476]] | C | PHACTR1 activity raises LINC02476's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 5.58× lower at baseline in the lines without PHACTR1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |
| [[LINC00504]] | C | PHACTR1 activity raises LINC00504's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 2.71× lower at baseline in the lines without PHACTR1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.6, 24.7); signed map (40.2, 26.9). **Vector** length 53.5, 18.1% of its response variance represented; |z| ≥ 3 in 382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -2.3 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase and actin regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.1 — chr6:12,716,312-13,290,446 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1733, dJ257A7.2; previously RPEL1 |
| Gene groups (HGNC) | Phosphatase and actin regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D0](https://www.uniprot.org/uniprotkb/Q9C0D0) (Phosphatase and actin regulator 1):

> Binds actin monomers (G actin) and plays a role in multiple processes including the regulation of actin cytoskeleton dynamics, actin stress fibers formation, cell motility and survival, formation of tubules by endothelial cells, and regulation of PPP1CA activity. Involved in the regulation of cortical neuron migration and dendrite arborization (By similarity).

**Summary**, from NCBI Gene [221692](https://www.ncbi.nlm.nih.gov/gene/221692):

> The protein encoded by this gene is a member of the phosphatase and actin regulator family of proteins. This family member can bind actin and regulate the reorganization of the actin cytoskeleton. It plays a role in tubule formation and in endothelial cell survival. Polymorphisms in this gene are associated with susceptibility to myocardial infarction, coronary artery disease and cervical artery dissection. Alternative splicing of this gene results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:20990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20990) · Entrez [221692](https://www.ncbi.nlm.nih.gov/gene/221692) · UniProt [Q9C0D0](https://www.uniprot.org/uniprotkb/Q9C0D0) · Ensembl [ENSG00000112137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112137)

## Data

Gene col 3323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3323); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3323]; `tensor/DDL_lfc|DDL_z.npy` [3323]; `embed/gene_vectors.npy` [3323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3323 or target_col == 3323). Every well: [[PHACTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHACTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
