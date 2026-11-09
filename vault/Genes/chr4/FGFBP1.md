---
symbol: "FGFBP1"
type: "gene"
col: 6013
ensembl_id: "ENSG00000137440"
name: "fibroblast growth factor binding protein 1"
location: "4p15.32"
module: 73
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 14
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 29
direction_downstream: 59
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# FGFBP1

*fibroblast growth factor binding protein 1* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.58× (z +9.5, q 9e-19, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.68× (z +4.2, q 0.002, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[BAY1125976 (drug)]] 5 µM: 0.212× (z -4.7, q 0.001, down in 6 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.134×, KATO III 0.155×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.131×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 0.148×); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.0854×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSE]] (+0.68, fdr 1e-05), [[LIPG]] (+0.67, fdr 1e-05), [[CEACAM6]] (+0.66, fdr 1e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[KLK10]] → it (grade C ⚠); 59 go from it, the strongest it → [[PLS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.58×** | +9.5 | 9e-19 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.08×** | +9.4 | 2e-18 | 4/9 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.11×** | +7.5 | 9e-12 | 3/7 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.68×** | +5.5 | 7e-06 | 5/11 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.53×** | +5.3 | 1e-05 | 1/7 (Hs 766T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +4.9 | 8e-05 | 2/8 (CFPAC-1, Panc 03.27) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.03×** | +4.2 | 0.002 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.002 | 4/12 (Hs 766T, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.77×** | +4.2 | 0.002 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.01×** | +4.0 | 0.004 | 1/10 (AsPC-1) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.98×** | +3.9 | 0.004 | 1/11 (Hs 766T) | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.005 | 10/12 (LS 180, AsPC-1, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **3.30×** | +3.6 | 0.014 | 1/6 (LS 180) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.023 | 7/12 (LS 180, LoVo, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.038 | 1/11 (NCI-H2347) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.77×** | +3.2 | 0.047 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.051 | 2/11 (NCI-H2347, CFPAC-1) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +3.0 | 0.086 | 0/11 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.67×** | +2.9 | 0.089 | 1/11 (SW1417) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (Hs 766T 0.134×, KATO III 0.155×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.131×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (Hs 766T 0.148×); [[Ponatinib (drug)]] 5 µM in 1 line (KATO III 0.0854×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **0.212×** | -4.7 | 0.001 | 6/12 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **0.521×** | -3.7 | 0.072 | 2/11 (SW1417, CFPAC-1) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.369× | -3.0 | 0.37 | 7/12 (Hs 766T, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 48.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -13.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.148× (z -9.3) |
| [[KATO III (line)]] | alt | 45.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0854× (z -8.6) |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.1) |
| [[A-172 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.404 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSE]] | +0.68 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LIPG]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CEACAM6]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[TFF2]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PCSK9]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TFF1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TPTEP1-1]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[KLK10]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[FGFR4]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 | pathway: Signaling by FGFR |
| [[LINC02582]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PIWIL1]] | +0.56 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[KLK11]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 0, C 29. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLK10]] | C | KLK10 activity raises FGFBP1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.01× lower at baseline in the lines without KLK10 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises FGFBP1's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.33× lower at baseline in the lines without HS3ST1 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises FGFBP1's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.91× lower at baseline in the lines without ST6GALNAC1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises FGFBP1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.78× lower at baseline in the lines without COL17A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[LINP1]] | C | LINP1 activity raises FGFBP1's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without LINP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises FGFBP1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.79× lower at baseline in the lines without SERPINB5 | 0.007 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[PCSK9]] | C | PCSK9 activity raises FGFBP1's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without PCSK9 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises FGFBP1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.16× lower at baseline in the lines without SLC6A14 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[CAPN8]] | C | CAPN8 activity raises FGFBP1's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without CAPN8 | 0.017 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38; co-absent with the target |
| [[LGR6]] | C | LGR6 activity raises FGFBP1's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.90× lower at baseline in the lines without LGR6 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[CYP3A5]] | C | CYP3A5 activity raises FGFBP1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.74× lower at baseline in the lines without CYP3A5 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[F3]] | C | F3 activity raises FGFBP1's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.18× lower at baseline in the lines without F3 | 0.023 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; co-absent with the target |

### Downstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 13, C 46. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS1]] | B | FGFBP1 activity raises PLS1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.76× lower at baseline in the lines without FGFBP1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[KRT8]] | B | FGFBP1 activity raises KRT8's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without FGFBP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[ITGA6]] | B | FGFBP1 activity raises ITGA6's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.52× lower at baseline in the lines without FGFBP1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | FGFBP1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FGFBP1 (36) vs lines expressing it (12) | the lines without FGFBP1: 1.24× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[IGSF9]] | B | FGFBP1 activity raises IGSF9's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 1.95× lower at baseline in the lines without FGFBP1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[LANCL3]] | B | FGFBP1 activity raises LANCL3's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 2.32× lower at baseline in the lines without FGFBP1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[GPRC5D-AS1]] | B | FGFBP1 activity raises GPRC5D-AS1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 2.82× lower at baseline in the lines without FGFBP1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[SYTL5]] | B | FGFBP1 activity raises SYTL5's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 1.51× lower at baseline in the lines without FGFBP1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | FGFBP1 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express FGFBP1 (36) vs lines expressing it (12) | the lines without FGFBP1: 1.24× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[VILL]] | B | FGFBP1 activity raises VILL's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without FGFBP1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[NOSTRIN]] | B | FGFBP1 activity raises NOSTRIN's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 2.78× lower at baseline in the lines without FGFBP1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| cells under [[EX229 (drug)]] 0.05 µM | B | FGFBP1 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express FGFBP1 (36) vs lines expressing it (12) | the lines without FGFBP1: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.8, 51.6); signed map (67.9, 9.6). **Vector** length 40.3, 13.2% of its response variance represented; |z| ≥ 3 in 316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,935,577-15,938,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBP17, FGFBP |
| Gene groups (HGNC) | Fibroblast growth factor binding protein family |
| Reactome | 5 pathways, smallest: FGFR2b ligand binding and activation; FGFR2 ligand binding and activation; Signaling by FGFR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14512](https://www.uniprot.org/uniprotkb/Q14512) (Fibroblast growth factor-binding protein 1):

> Acts as a carrier protein that release fibroblast-binding factors (FGFs) from the extracellular matrix (EM) storage and thus enhance the mitogenic activity of FGFs. Enhances FGF2 signaling during tissue repair, angiogenesis and in tumor growth.

**Summary**, from NCBI Gene [9982](https://www.ncbi.nlm.nih.gov/gene/9982):

> This gene encodes a secreted fibroblast growth factor carrier protein. The encoded protein plays a critical role in cell proliferation, differentiation and migration by binding to fibroblast growth factors and potentiating their biological effects on target cells. The encoded protein may also play a role in tumor growth as an angiogenic switch molecule, and expression of this gene has been associated with several types of cancer including pancreatic and colorectal adenocarcinoma. A pseudogene …

**Accessions** — [HGNC:19695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19695) · Entrez [9982](https://www.ncbi.nlm.nih.gov/gene/9982) · UniProt [Q14512](https://www.uniprot.org/uniprotkb/Q14512) · Ensembl [ENSG00000137440](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137440)

## Data

Gene col 6013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6013); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6013]; `tensor/DDL_lfc|DDL_z.npy` [6013]; `embed/gene_vectors.npy` [6013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6013 or target_col == 6013). Every well: [[FGFBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGFBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
