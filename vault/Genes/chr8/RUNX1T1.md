---
symbol: "RUNX1T1"
type: "gene"
col: 1239
ensembl_id: "ENSG00000079102"
name: "RUNX1 partner transcriptional co-repressor 1"
location: "8q21.3"
module: 9
arm: "+"
pooled_cpm: 8.43
n_lines_expressing: 12
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 40
direction_downstream: 69
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# RUNX1T1

*RUNX1 partner transcriptional co-repressor 1* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.01× (z +16.0, q 0e+00, up in 3 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.573× (z -4.4, q 0.007, down in 4 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (SHP-77 0.197×, CHP-212 0.144×, SW480 0.190×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.192×, NCI-H661 0.146×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SHP-77 0.229×, CHP-212 0.140×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.370×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYT4]] (+0.84, fdr 7e-06), [[KCNB2]] (+0.83, fdr 7e-06), [[LINC02197]] (+0.82, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[ASCL1]] → it (grade C ⚠); 69 go from it, the strongest it → [[LINC02223]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +16.0 | 0e+00 | 3/9 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +10.0 | 3e-21 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +9.6 | 1e-19 | 4/9 (BT-474, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +7.8 | 9e-13 | 1/7 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +6.2 | 8e-08 | 3/8 (CHP-212, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +5.4 | 7e-06 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.002 | 3/9 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +4.0 | 0.005 | 4/9 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.018 | 0/9 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.53×** | +3.5 | 0.026 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.97×** | +3.3 | 0.044 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.49×** | +3.3 | 0.052 | 1/8 (SW 900) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.053 | 3/8 (SHP-77, SW480, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.053 | 1/9 (H4) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.060 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.060 | 3/9 (SHP-77, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.87×** | +3.1 | 0.069 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (SHP-77 0.197×, CHP-212 0.144×, SW480 0.190×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.192×, NCI-H661 0.146×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SHP-77 0.229×, CHP-212 0.140×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.370×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.573×** | -4.4 | 0.007 | 4/9 (SW480, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.603×** | -3.7 | 0.050 | 0/9 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.674× | -3.2 | 0.23 | 2/9 (A498, SHP-77) | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | 0.639× | -3.1 | 0.23 | 0/9 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.661× | -3.1 | 0.23 | 0/9 | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.675× | -3.0 | 0.23 | 3/9 (SW480, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 284 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -15.5) |
| [[CHP-212 (line)]] | wt | 245 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -10.3) |
| [[A498 (line)]] | wt | 7.44 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.279× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 10.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -9.1) |
| [[A-172 (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYT4]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 | STRING 412 |
| [[KCNB2]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC02197]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[RIT2]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[SRRM4]] | +0.79 | +0.67 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[RMST]] | +0.78 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[DACH1]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP25]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[CSRNP3]] | +0.70 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SNTG1]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 0, C 40. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | C | ASCL1 activity raises RUNX1T1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 9.49× lower at baseline in the lines without ASCL1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises RUNX1T1's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 7.15× lower at baseline in the lines without SNTG1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises RUNX1T1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 6.13× lower at baseline in the lines without SRRM4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | RIMBP2 activity raises RUNX1T1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 3.86× lower at baseline in the lines without RIMBP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RMST activity raises RUNX1T1's level | lines that do not express RMST (35) vs lines expressing it (15) | 4.19× lower at baseline in the lines without RMST | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises RUNX1T1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 3.64× lower at baseline in the lines without SLC25A24P1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises RUNX1T1's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without SERPINF1 | 0.011 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises RUNX1T1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 3.94× lower at baseline in the lines without AK4P3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[SOX2]] | C | SOX2 activity raises RUNX1T1's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 3.44× lower at baseline in the lines without SOX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises RUNX1T1's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.89× lower at baseline in the lines without LINC02197 | 0.015 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[DGKB]] | C | DGKB activity raises RUNX1T1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without DGKB | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises RUNX1T1's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.69× lower at baseline in the lines without POU3F2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 12, C 57. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02223]] | B | RUNX1T1 activity raises LINC02223's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.26× lower at baseline in the lines without RUNX1T1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[ADAMTS19]] | B | RUNX1T1 activity raises ADAMTS19's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without RUNX1T1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[LINC02466]] | B | RUNX1T1 activity raises LINC02466's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.72× lower at baseline in the lines without RUNX1T1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[RALYL]] | B | RUNX1T1 activity raises RALYL's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.08× lower at baseline in the lines without RUNX1T1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[SOBP]] | B | RUNX1T1 activity raises SOBP's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without RUNX1T1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[ZNF711]] | B | RUNX1T1 activity raises ZNF711's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.26× lower at baseline in the lines without RUNX1T1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[FAM13C]] | B | RUNX1T1 activity raises FAM13C's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.62× lower at baseline in the lines without RUNX1T1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[ADGRV1]] | B | RUNX1T1 activity raises ADGRV1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.21× lower at baseline in the lines without RUNX1T1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[CHRM5]] | B | RUNX1T1 activity weakens CHRM5's drug response | lines that do not express RUNX1T1 (37) vs lines expressing it (7) | the lines without RUNX1T1 respond 1.94× as strongly (z diff -0.69); strongest at Dinaciclib 0.05 µM: 4.04x vs 0.88x (z diff -6.1) | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; target measured in part of the lines; artifact flags |
| [[NELL1]] | B | RUNX1T1 activity raises NELL1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.91× lower at baseline in the lines without RUNX1T1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[ADGRL2]] | B | RUNX1T1 activity raises ADGRL2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.44× lower at baseline in the lines without RUNX1T1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[VENTXP1]] | B | RUNX1T1 activity raises VENTXP1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.88× lower at baseline in the lines without RUNX1T1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 37.3); signed map (45.4, 34.1). **Vector** length 39.1, 14.5% of its response variance represented; |z| ≥ 3 in 247 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.54 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RUNX1 partner transcriptional co-repressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:91,954,972-92,103,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDR, ETO, MTG8, ZMYND2; previously AML1T1, CBFA2T1 |
| Gene groups (HGNC) | Zinc fingers MYND-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06455](https://www.uniprot.org/uniprotkb/Q06455) (Protein CBFA2T1):

> Transcriptional corepressor which facilitates transcriptional repression via its association with DNA-binding transcription factors and recruitment of other corepressors and histone-modifying enzymes. Can repress the expression of MMP7 in a ZBTB33-dependent manner. Can repress transactivation mediated by TCF12. Acts as a negative regulator of adipogenesis (By similarity). The AML1-MTG8/ETO fusion protein frequently found in leukemic cells is involved in leukemogenesis and contributes to …

**Summary**, from NCBI Gene [862](https://www.ncbi.nlm.nih.gov/gene/862):

> This gene encodes a member of the myeloid translocation gene family which interact with DNA-bound transcription factors and recruit a range of corepressors to facilitate transcriptional repression. The t(8;21)(q22;q22) translocation is one of the most frequent karyotypic abnormalities in acute myeloid leukemia. The translocation produces a chimeric gene made up of the 5'-region of the runt-related transcription factor 1 gene fused to the 3'-region of this gene. The chimeric protein is thought …

**Accessions** — [HGNC:1535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1535) · Entrez [862](https://www.ncbi.nlm.nih.gov/gene/862) · UniProt [Q06455](https://www.uniprot.org/uniprotkb/Q06455) · Ensembl [ENSG00000079102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079102)

## Data

Gene col 1239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1239); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1239]; `tensor/DDL_lfc|DDL_z.npy` [1239]; `embed/gene_vectors.npy` [1239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1239 or target_col == 1239). Every well: [[RUNX1T1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNX1T1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
