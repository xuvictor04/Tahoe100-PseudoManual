---
symbol: "CMYA5"
type: "gene"
col: 8927
ensembl_id: "ENSG00000164309"
name: "cardiomyopathy associated 5"
location: "5q14.1"
module: 37
arm: "+"
pooled_cpm: 12.77
n_lines_expressing: 48
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 33
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CMYA5

*cardiomyopathy associated 5* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.91× (z +29.3, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.563× (z -6.7, q 1e-08, down in 18 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.733× (z -3.6, q 0.074, down in 8 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0896×, NCI-H1573 0.0849×, RPMI-7951 0.119×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.0789×, NCI-H1573 0.0835×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (A-172 0.103×); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (SW48 0.0823×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRK7]] (+0.77, fdr 7e-06), [[CFAP53]] (+0.74, fdr 7e-06), [[LINC00640]] (+0.74, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC01917]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.91×** | +29.3 | 0e+00 | 42/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.18×** | +16.7 | 0e+00 | 44/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.87×** | +15.8 | 0e+00 | 40/43 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.69×** | +15.2 | 0e+00 | 38/45 (LoVo, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +14.5 | 3e-45 | 38/44 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.49×** | +14.0 | 1e-42 | 42/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.32×** | +12.9 | 3e-36 | 42/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **8.20×** | +12.8 | 8e-36 | 40/43 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +12.0 | 2e-31 | 32/45 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +9.9 | 2e-21 | 29/44 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +9.9 | 3e-21 | 32/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.26×** | +9.5 | 1e-19 | 35/45 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +8.9 | 2e-17 | 38/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +8.8 | 8e-17 | 35/46 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +8.4 | 2e-15 | 30/46 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +8.4 | 2e-15 | 33/46 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8927.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0896×, NCI-H1573 0.0849×, RPMI-7951 0.119×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.0789×, NCI-H1573 0.0835×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (A-172 0.103×); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (SW48 0.0823×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.563×** | -6.7 | 1e-08 | 18/35 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.733×** | -3.6 | 0.074 | 8/46 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.754× | -3.3 | 0.17 | 14/44 (SW 900, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.760× | -3.0 | 0.30 | 11/46 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.774× | -3.0 | 0.30 | 11/45 (SW480, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 31.0 | 8 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +19.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -18.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.6 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 20.2× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +20.0) | — |
| [[SW480 (line)]] | alt | 14.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 7.85 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +19.9) | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0849× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 13.1 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.05× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.27× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 18.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.78× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 11.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.03 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 7.16 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 16.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 27.1× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +15.4) | — |
| [[SNU-1 (line)]] | wt | 23.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.5) | — |
| [[A498 (line)]] | wt | 9.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +16.8) | — |
| [[A549 (line)]] | wt | 8.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +12.8) | — |
| [[C32 (line)]] | wt | 13.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 36.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.1) | — |
| [[KATO III (line)]] | alt | 7.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +13.5) | — |
| [[SW 900 (line)]] | alt | 19.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +10.8) | — |
| [[SW48 (line)]] | wt | 13.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.9) | [[Betamethasone dipropionate (drug)]] 5 µM 0.0823× (z -8.7) |
| [[A-172 (line)]] | wt | 6.95 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.103× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 4.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 8.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +10.2) | — |
| [[J82 (line)]] | alt | 9.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 7.05 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 11.5× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 6.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +9.4) | — |
| [[RKO (line)]] | wt | 6.27 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.8× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 6.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +10.6) | — |
| [[A-427 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK7]] | +0.77 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.74 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.74 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CCDC13]] | +0.73 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[CASS4]] | +0.73 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SNX31]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.73 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.72 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[LINC01031]] | +0.72 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.72 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[FRZB]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01917]] | B | LINC01917 activity raises CMYA5's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without LINC01917 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises CMYA5's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without LINC02641 | 0.041 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[CXCL13]] | B | CXCL13 activity raises CMYA5's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without CXCL13 | 0.051 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CMYA5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DYSF]] | B | DYSF activity raises CMYA5's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without DYSF | 0.058 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[LINC02398]] | B | LINC02398 activity raises CMYA5's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without LINC02398 | 0.073 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[IGSF11]] | B | IGSF11 activity raises CMYA5's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without IGSF11 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[ST8SIA5]] | B | ST8SIA5 activity raises CMYA5's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without ST8SIA5 | 0.078 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[FRZB]] | C | FRZB activity raises CMYA5's level | lines that do not express FRZB (4) vs lines expressing it (46) | 2.90× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | CMYA5's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | CMYA5's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.287 over the table, 0.023 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, -15.7); signed map (13.6, 4.6). **Vector** length 92.0, 23.2% of its response variance represented; |z| ≥ 3 in 1,388 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +15.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +14.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.2 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +12.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.6 | +7.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.3 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[LB-100 (drug)]] 0.05 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cardiomyopathy associated 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:79,689,836-79,800,240 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPRYD2, DKFZp451G223, TRIM76; previously C5orf10 |
| Gene groups (HGNC) | Tripartite motif family; A-kinase anchoring proteins; Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3K9](https://www.uniprot.org/uniprotkb/Q8N3K9) (Cardiomyopathy-associated protein 5):

> May serve as an anchoring protein that mediates the subcellular compartmentation of protein kinase A (PKA) via binding to PRKAR2A (By similarity). May function as a repressor of calcineurin-mediated transcriptional activity. May attenuate calcineurin ability to induce slow-fiber gene program in muscle and may negatively modulate skeletal muscle regeneration (By similarity). Plays a role in the assembly of ryanodine receptor (RYR2) clusters in striated muscle (By similarity).

**Summary**, from NCBI Gene [202333](https://www.ncbi.nlm.nih.gov/gene/202333):

> Predicted to enable identical protein binding activity and protein phosphatase inhibitor activity. Predicted to act upstream of or within negative regulation of calcineurin-NFAT signaling cascade and regulation of skeletal muscle adaptation. Predicted to be located in several cellular components, including costamere; perinuclear region of cytoplasm; and sarcoplasmic reticulum. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14305) · Entrez [202333](https://www.ncbi.nlm.nih.gov/gene/202333) · UniProt [Q8N3K9](https://www.uniprot.org/uniprotkb/Q8N3K9) · Ensembl [ENSG00000164309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164309)

## Data

Gene col 8927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8927); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8927]; `tensor/DDL_lfc|DDL_z.npy` [8927]; `embed/gene_vectors.npy` [8927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8927 or target_col == 8927). Every well: [[CMYA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMYA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
