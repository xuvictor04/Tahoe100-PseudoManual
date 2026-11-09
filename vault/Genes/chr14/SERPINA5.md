---
symbol: "SERPINA5"
type: "gene"
col: 12015
ensembl_id: "ENSG00000188488"
name: "serpin family A member 5"
location: "14q32.13"
module: 97
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 13
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 35
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# SERPINA5

*serpin family A member 5* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.87× (z +11.6, q 1e-28, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +4.1, q 0.004, up in 7 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (HepG2/C3A 0.119×, SK-MEL-2 0.0379×, Panc 03.27 0.0759×, CFPAC-1 0.0957×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.168×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0712×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (Panc 03.27 0.116×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.238×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGFG2]] (+0.65, fdr 7e-06), [[NCMAP]] (+0.60, fdr 7e-05), [[KRT23]] (+0.54, fdr 4e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[GABRP]] → it (grade C ⚠); 35 go from it, the strongest it → [[RAPGEF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.87×** | +11.6 | 1e-28 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.09×** | +10.2 | 4e-22 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.10×** | +8.2 | 5e-14 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +6.0 | 3e-07 | 2/7 (CFPAC-1, HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.004 | 7/11 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.65×** | +4.1 | 0.004 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.005 | 0/10 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.19×** | +3.8 | 0.010 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +3.7 | 0.012 | 2/4 (HepG2/C3A, CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +3.5 | 0.022 | 1/7 (HOP62) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.5 | 0.022 | 0/6 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.30×** | +3.5 | 0.022 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.29×** | +3.5 | 0.022 | 1/8 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.022 | 5/11 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.027 | 7/11 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +3.3 | 0.034 | 1/7 (SK-MEL-2) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.15×** | +3.2 | 0.045 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.046 | 1/7 (HOP62) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +3.0 | 0.083 | 4/11 (HOP62, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12015.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 5 lines (HepG2/C3A 0.119×, SK-MEL-2 0.0379×, Panc 03.27 0.0759×, CFPAC-1 0.0957×, …); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.168×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0712×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (Panc 03.27 0.116×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.238×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | 0.569× | -3.4 | 0.29 | 7/11 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.574× | -3.3 | 0.29 | 0/11 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.607× | -3.2 | 0.29 | 8/11 (COLO 205, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 40.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0759× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 156 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0957× (z -10.1) |
| [[HOP62 (line)]] | alt | 2.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0393× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 9.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0379× (z -12.9) |
| [[A-172 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.355 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGFG2]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NCMAP]] | +0.60 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[KRT23]] | +0.54 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[HLA-DRB1]] | +0.54 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[GABRP]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[JPH2]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[IRAK3]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PACSIN2]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PRSS8]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[C3]] | +0.51 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SCNN1A]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[FAXDC2]] | +0.51 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRP]] | C | GABRP activity raises SERPINA5's level | lines that do not express GABRP (44) vs lines expressing it (6) | 3.06× lower at baseline in the lines without GABRP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[SERPINA1]] | C | SERPINA1 activity raises SERPINA5's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without SERPINA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[C3]] | C | C3 activity raises SERPINA5's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.15× lower at baseline in the lines without C3 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises SERPINA5's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 2.94× lower at baseline in the lines without SLC6A14 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises SERPINA5's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.56× lower at baseline in the lines without KRT23 | 0.025 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises SERPINA5's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.62× lower at baseline in the lines without WFDC2 | 0.034 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[LRG1]] | C | LRG1 activity raises SERPINA5's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without LRG1 | 0.035 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises SERPINA5's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without ENPP5 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[SERPINA3]] | C | SERPINA3 activity raises SERPINA5's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 3.09× lower at baseline in the lines without SERPINA3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[PRSS51]] | C | PRSS51 activity raises SERPINA5's level | lines that do not express PRSS51 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without PRSS51 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, AK4P3, ASCL1; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises SERPINA5's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without HSD17B2 | 0.064 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises SERPINA5's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 2.13× lower at baseline in the lines without PRSS8 | 0.068 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 12, C 23. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | SERPINA5 activity raises RAPGEF5's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.99× lower at baseline in the lines without SERPINA5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[PROM2]] | B | SERPINA5 activity raises PROM2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.11× lower at baseline in the lines without SERPINA5 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[SAA2]] | B | SERPINA5 activity raises SAA2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.72× lower at baseline in the lines without SERPINA5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[CORO2A]] | B | SERPINA5 activity raises CORO2A's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without SERPINA5 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[DNM2]] | B | SERPINA5 activity raises DNM2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.32× lower at baseline in the lines without SERPINA5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[ADSS1]] | B | SERPINA5 activity raises ADSS1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.68× lower at baseline in the lines without SERPINA5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[CCND3]] | B | SERPINA5 activity raises CCND3's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.57× lower at baseline in the lines without SERPINA5 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[AGFG2]] | B | SERPINA5 activity raises AGFG2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without SERPINA5 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[STK24]] | B | SERPINA5 activity raises STK24's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.53× lower at baseline in the lines without SERPINA5 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[TMEM92]] | B | SERPINA5 activity raises TMEM92's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without SERPINA5 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[ZFYVE19]] | B | SERPINA5 activity raises ZFYVE19's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.34× lower at baseline in the lines without SERPINA5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[IFITM10]] | B | SERPINA5 activity raises IFITM10's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.35× lower at baseline in the lines without SERPINA5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.2, 51.4); signed map (69.2, 15.8). **Vector** length 32.9, 8.97% of its response variance represented; |z| ≥ 3 in 330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +4.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.9 | +1.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.9 | +2.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +0.9 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | serpin family A member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.13 — chr14:94,561,442-94,593,118 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAI3, PROCI; previously PLANH3, PCI |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | ANGIOGENESIS, ESTROGEN_RESPONSE_LATE |
| Reactome | 5 pathways, smallest: Amplification and propagation of coagulation cascade; Fibrin formation; Regulation of clotting cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P05154](https://www.uniprot.org/uniprotkb/P05154) (Plasma serine protease inhibitor):

> Heparin-dependent serine protease inhibitor acting in body fluids and secretions. Inactivates serine proteases by binding irreversibly to their serine activation site. Involved in the regulation of intravascular and extravascular proteolytic activities. Plays hemostatic roles in the blood plasma. Acts as a procoagulant and pro-inflammatory factor by inhibiting the anticoagulant activated protein C factor as well as the generation of activated protein C factor by the thrombin/thrombomodulin …

**Summary**, from NCBI Gene [5104](https://www.ncbi.nlm.nih.gov/gene/5104):

> The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. This family member is a glycoprotein that can inhibit several serine proteases, including protein C and various plasminogen activators and kallikreins, and it thus plays diverse roles in hemostasis and thrombosis in multiple organs. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:8723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8723) · Entrez [5104](https://www.ncbi.nlm.nih.gov/gene/5104) · UniProt [P05154](https://www.uniprot.org/uniprotkb/P05154) · Ensembl [ENSG00000188488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188488)

## Data

Gene col 12015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12015); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12015]; `tensor/DDL_lfc|DDL_z.npy` [12015]; `embed/gene_vectors.npy` [12015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12015 or target_col == 12015). Every well: [[SERPINA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
