---
symbol: "RALYL"
type: "gene"
col: 11564
ensembl_id: "ENSG00000184672"
name: "RALY RNA binding protein like"
location: "8q21.2"
module: 9
arm: "+"
pooled_cpm: 6.8
n_lines_expressing: 33
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 12
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# RALYL

*RALY RNA binding protein like* — 8q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.32× (z +19.0, q 0e+00, up in 17 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (CHP-212 0.0575×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CHP-212 0.0468×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (CHP-212 0.0658×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNBD1]] (+0.78, fdr 7e-06), [[NRXN1]] (+0.77, fdr 7e-06), [[VENTXP1]] (+0.74, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[ASCL1]] → it (grade B ⚠); 12 go from it, the strongest it → [[SEMA6D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.32×** | +19.0 | 0e+00 | 17/20 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.44×** | +14.0 | 3e-42 | 17/22 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.39×** | +11.9 | 3e-30 | 5/9 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.87×** | +10.5 | 2e-23 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +9.4 | 8e-19 | 3/5 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.91×** | +8.6 | 8e-16 | 20/25 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +7.5 | 4e-12 | 13/28 (C32, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.00×** | +5.6 | 2e-06 | 2/9 (BT-474, HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.5 | 4e-04 | 7/20 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +4.3 | 0.001 | 12/22 (HOP62, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.9 | 0.004 | 2/12 (AsPC-1, HEC-1-A) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.012 | 3/16 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.6 | 0.013 | 1/15 (NCI-H460) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.017 | 7/20 (CHP-212, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.024 | 8/20 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.067 | 8/22 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11564.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (CHP-212 0.0575×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CHP-212 0.0468×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (CHP-212 0.0658×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.670× | -3.2 | 0.67 | 4/28 (SHP-77, C32, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.686× | -3.0 | 0.67 | 1/29 (HCT15) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 224 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0575× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.112× (z -8.8) |
| [[HOP62 (line)]] | alt | 2.33 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +8.9) | — |
| [[A498 (line)]] | wt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +9.2) | — |
| [[C32 (line)]] | wt | 1.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 2.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.41× (z +8.7) | — |
| [[J82 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +14.1) | — |
| [[A-172 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNBD1]] | +0.78 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[VENTXP1]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.74 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[LINC02306]] | +0.73 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[GRID2]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[GLRA3]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[UNC80]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | B | ASCL1 activity raises RALYL's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.35× lower at baseline in the lines without ASCL1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[SYT4]] | B | SYT4 activity raises RALYL's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 7.31× lower at baseline in the lines without SYT4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[CALCA]] | B | CALCA activity raises RALYL's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.20× lower at baseline in the lines without CALCA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[RIT2]] | B | RIT2 activity raises RALYL's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.37× lower at baseline in the lines without RIT2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[KCNB2]] | B | KCNB2 activity raises RALYL's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.78× lower at baseline in the lines without KCNB2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[PDZRN3]] | B | PDZRN3 activity raises RALYL's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without PDZRN3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[AK4P3]] | B | AK4P3 activity raises RALYL's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.71× lower at baseline in the lines without AK4P3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[SRRM4]] | B | SRRM4 activity raises RALYL's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.40× lower at baseline in the lines without SRRM4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[RUNX1T1]] | B | RUNX1T1 activity raises RALYL's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.08× lower at baseline in the lines without RUNX1T1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[SNTG1]] | B | SNTG1 activity raises RALYL's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.03× lower at baseline in the lines without SNTG1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[LINC01320]] | B | LINC01320 activity raises RALYL's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 1.87× lower at baseline in the lines without LINC01320 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[HGF]] | B | HGF activity raises RALYL's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.16× lower at baseline in the lines without HGF | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6D]] | B | RALYL activity raises SEMA6D's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.09× lower at baseline in the lines without RALYL | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[PDZRN3]] | B | RALYL activity raises PDZRN3's level | lines that do not express RALYL (17) vs lines expressing it (33) | 3.50× lower at baseline in the lines without RALYL | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[LINC01320]] | B | RALYL activity raises LINC01320's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without RALYL | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[SCN2A]] | B | RALYL activity raises SCN2A's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without RALYL | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[PGR]] | B | RALYL activity raises PGR's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without RALYL | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[HGF]] | B | RALYL activity raises HGF's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.69× lower at baseline in the lines without RALYL | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[MIR4300HG]] | B | RALYL activity raises MIR4300HG's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.46× lower at baseline in the lines without RALYL | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[HAND2-AS1]] | B | RALYL activity raises HAND2-AS1's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without RALYL | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[PRKG1]] | B | RALYL activity raises PRKG1's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.47× lower at baseline in the lines without RALYL | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[FGF13]] | B | RALYL activity raises FGF13's level | lines that do not express RALYL (17) vs lines expressing it (33) | 3.23× lower at baseline in the lines without RALYL | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[LINC02268]] | B | RALYL activity raises LINC02268's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without RALYL | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[MARCHF1]] | C | RALYL activity raises MARCHF1's level | lines that do not express RALYL (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without RALYL | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 34.7); signed map (42.6, 32.8). **Vector** length 48.0, 8.96% of its response variance represented; |z| ≥ 3 in 626 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.57 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RALY RNA binding protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.2 — chr8:84,182,787-84,921,844 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNRPCL3 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q86SE5](https://www.uniprot.org/uniprotkb/Q86SE5) carries no function annotation.

**Summary**, from NCBI Gene [138046](https://www.ncbi.nlm.nih.gov/gene/138046):

> Enables identical protein binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27036) · Entrez [138046](https://www.ncbi.nlm.nih.gov/gene/138046) · UniProt [Q86SE5](https://www.uniprot.org/uniprotkb/Q86SE5) · Ensembl [ENSG00000184672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184672)

## Data

Gene col 11564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11564); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11564]; `tensor/DDL_lfc|DDL_z.npy` [11564]; `embed/gene_vectors.npy` [11564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11564 or target_col == 11564). Every well: [[RALYL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALYL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
