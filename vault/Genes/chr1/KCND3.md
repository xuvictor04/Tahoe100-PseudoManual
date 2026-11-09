---
symbol: "KCND3"
type: "gene"
col: 10099
ensembl_id: "ENSG00000171385"
name: "potassium voltage-gated channel subfamily D member 3"
location: "1p13.2"
module: 75
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 29
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# KCND3

*potassium voltage-gated channel subfamily D member 3* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.58× (z +17.0, q 0e+00, up in 13 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.625× (z -4.4, q 0.005, down in 7 of 25 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Clopidogrel (drug)]] 0.05 µM: 0.673× (z -3.7, q 0.052, down in 7 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0885×, SNU-1 0.133×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.170×, SNU-1 0.120×; ⚠ cell-cycle shift, explains ~75% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.273×, SNU-1 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LoVo 0.192×); [[TAK-901 (drug)]] 5 µM in 1 line (LoVo 0.0553×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.305×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAIN1]] (+0.64, fdr 7e-06), [[DOC2B]] (+0.64, fdr 7e-06), [[LINC00457]] (+0.61, fdr 1e-05); moves opposite to [[DZANK1]] (-0.50, fdr 2e-04), [[POLR2G]] (-0.48, fdr 2e-04, ⚠ POLR2G in the vector space only through flagged drug-doses).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00457]] → it (grade B ⚠); 11 go from it, the strongest it → [[GNAL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.58×** | +17.0 | 0e+00 | 13/19 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.49×** | +12.2 | 1e-31 | 15/25 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.03×** | +10.5 | 2e-23 | 14/22 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.1 | 1e-21 | 2/10 (J82, NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +8.9 | 6e-17 | 1/3 (J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +8.5 | 2e-15 | 1/7 (J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.41×** | +8.3 | 9e-15 | 13/22 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.8 | 9e-05 | 2/9 (J82, BT-474) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.9 | 0.005 | 7/25 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.017 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.026 | 2/20 (NCI-H23, SW480) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.026 | 3/23 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.029 | 4/20 (NCI-H460, C-33 A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.079 | 1/16 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10099.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0885×, SNU-1 0.133×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.170×, SNU-1 0.120×; ⚠ cell-cycle shift, explains ~75% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.273×, SNU-1 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LoVo 0.192×); [[TAK-901 (drug)]] 5 µM in 1 line (LoVo 0.0553×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.305×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -4.4 | 0.005 | 7/25 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.673×** | -3.7 | 0.052 | 7/25 (RKO, KATO III, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.515× | -3.3 | 0.17 | 6/21 (LoVo, SHP-77, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.710× | -3.2 | 0.17 | 9/24 (LoVo, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 37.5 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -25.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -13.4) |
| [[SNU-1 (line)]] | wt | 62.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -10.9) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.305× (z -8.6) |
| [[A-427 (line)]] | wt | 5.66 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0861× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAIN1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DOC2B]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LINC00457]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TMEM229B]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[FER1L6]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[LINC01033]] | +0.58 | +0.30 / +0.65 | both halves | 2e-04 |  |
| [[PLXNC1]] | +0.58 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[NCF2]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ERC2]] | +0.57 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[GALNT9]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NEURL1]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SLC9C1]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.50 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[POLR2G]] ⚠ | -0.48 | -0.41 / -0.30 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00457]] | B | LINC00457 activity raises KCND3's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without LINC00457 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |
| [[LRRN2]] | B | LRRN2 activity raises KCND3's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without LRRN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[BCL2]] | B | BCL2 activity raises KCND3's level | lines that do not express BCL2 (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without BCL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CD226 |
| [[RET]] | B | RET activity raises KCND3's level | lines that do not express RET (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without RET | 0.097 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAL]] | B | KCND3 activity raises GNAL's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without KCND3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[BCL2]] | B | KCND3 activity raises BCL2's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without KCND3 | 0.020 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[MTUS2]] | B | KCND3 activity raises MTUS2's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.57× lower at baseline in the lines without KCND3 | 0.034 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[PLCL1]] | B | KCND3 activity raises PLCL1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.24× lower at baseline in the lines without KCND3 | 0.039 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[HRK]] | B | KCND3 activity raises HRK's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without KCND3 | 0.041 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[DOC2B]] | B | KCND3 activity raises DOC2B's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.38× lower at baseline in the lines without KCND3 | 0.061 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[EMID1]] | B | KCND3 activity raises EMID1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.65× lower at baseline in the lines without KCND3 | 0.066 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 5 µM | B | KCND3 activity lowers the cells' numbers under Dinaciclib 5 µM (makes them more sensitive) | lines that do not express KCND3 (21) vs lines expressing it (27) | the lines without KCND3: 2.05× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.5 µM | B | KCND3 activity lowers the cells' numbers under Dinaciclib 0.5 µM (makes them more sensitive) | lines that do not express KCND3 (21) vs lines expressing it (27) | the lines without KCND3: 2.00× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[PLXNC1]] | B | KCND3 activity raises PLXNC1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without KCND3 | 0.090 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[MSI1]] | C | KCND3 activity raises MSI1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without KCND3 | 0.091 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.5, 37.9); signed map (34.2, 22.5). **Vector** length 46.1, 8.56% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +17.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.7 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -3.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily D member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,770,662-111,989,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv4.3, KSHIVB; previously SCA22, SCA19 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 6 pathways, smallest: Phase 1 - inactivation of fast Na+ channels; Voltage gated Potassium channels; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK17](https://www.uniprot.org/uniprotkb/Q9UK17) (A-type voltage-gated potassium channel KCND3):

> Pore-forming (alpha) subunit of voltage-gated A-type potassium channels that mediates transmembrane potassium transport in excitable membranes, in brain and heart. In cardiomyocytes, may generate the transient outward potassium current I(To) (By similarity). In neurons, may conduct the transient subthreshold somatodendritic A-type potassium current (ISA) (By similarity). Kinetics properties are characterized by fast activation at subthreshold membrane potentials, rapid inactivation, and quick …

**Summary**, from NCBI Gene [3752](https://www.ncbi.nlm.nih.gov/gene/3752):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. Four sequence-related potassium channel genes - shaker, shaw, shab, and shal - have been identified in Drosophila, and each has been shown to have …

**Accessions** — [HGNC:6239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6239) · Entrez [3752](https://www.ncbi.nlm.nih.gov/gene/3752) · UniProt [Q9UK17](https://www.uniprot.org/uniprotkb/Q9UK17) · Ensembl [ENSG00000171385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171385)

## Data

Gene col 10099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10099); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10099]; `tensor/DDL_lfc|DDL_z.npy` [10099]; `embed/gene_vectors.npy` [10099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10099 or target_col == 10099). Every well: [[KCND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
