---
symbol: "BLOC1S2"
type: "gene"
col: 12124
ensembl_id: "ENSG00000196072"
name: "biogenesis of lysosomal organelles complex 1 subunit 2"
location: "10q24.31"
module: 62
arm: "+"
pooled_cpm: 23.34
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# BLOC1S2

*biogenesis of lysosomal organelles complex 1 subunit 2* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.06× (z +14.2, q 2e-43, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.308×; ⚠ cell-cycle shift, explains ~21% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDM2]] (+0.73, fdr 7e-06), [[PHLDA3]] (+0.68, fdr 1e-05), [[RAB21]] (+0.67, fdr 1e-05); moves opposite to [[SAPCD2]] (-0.54, fdr 3e-05), [[KIF18B]] (-0.53, fdr 3e-05), [[NUP98]] (-0.51, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.06×** | +14.2 | 2e-43 | 46/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +14.2 | 2e-43 | 43/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.79×** | +13.1 | 1e-36 | 46/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.91×** | +12.9 | 1e-35 | 45/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +11.1 | 1e-26 | 42/47 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +9.6 | 5e-20 | 39/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +8.7 | 2e-16 | 32/41 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +7.1 | 1e-10 | 36/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +6.7 | 1e-09 | 36/48 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.9 | 2e-07 | 29/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.88×** | +5.7 | 6e-07 | 36/48 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.37×** | +5.7 | 6e-07 | 26/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 2e-06 | 32/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.5 | 2e-06 | 25/48 (A-427, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.53×** | +5.4 | 3e-06 | 24/43 (SW 900, NCI-H460, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.6 | 1e-04 | 24/46 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +4.5 | 2e-04 | 23/46 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 18/48 (NCI-H460, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12124.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.308×; ⚠ cell-cycle shift, explains ~21% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.769× | -3.4 | 0.13 | 12/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.769× | -3.4 | 0.13 | 17/47 (AsPC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.771× | -3.3 | 0.13 | 13/48 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.833× | -3.3 | 0.13 | 14/48 (SW 900, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.8 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.00× (z +11.8) | — |
| [[SW480 (line)]] | alt | 19.1 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.56× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 21.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.91× (z +12.7) | — |
| [[A498 (line)]] | wt | 38.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 18.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.73× (z +10.4) | — |
| [[KATO III (line)]] | alt | 13.9 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.71× (z +9.6) | — |
| [[RKO (line)]] | wt | 34.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[SW48 (line)]] | wt | 33.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.9) | — |
| [[A549 (line)]] | wt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 12.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.41× (z +9.9) | — |
| [[LoVo (line)]] | wt | 15.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.87× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.68× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 18.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.61× (z +9.9) | — |
| [[A-172 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDM2]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PHLDA3]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[RAB21]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.64 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[BAX]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ZMAT3]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.61 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[TP53I3]] | +0.61 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[EDA2R]] | +0.59 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[RPS27L]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FAS]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAPCD2]] | -0.54 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[KIF18B]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NUP98]] | -0.51 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[CD320]] | -0.50 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[POLR1E]] | -0.50 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[KIFC1]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CCNF]] | -0.49 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[PIMREG]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ODF2]] | -0.49 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[GNB1L]] | -0.48 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[C20orf27]] | -0.47 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 1, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens BLOC1S2's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.84× as strongly (z diff +0.67); strongest at Topotecan (hydrochloride) 5 µM: 1.77x vs 3.06x (z diff +3.2) | 0.031 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens BLOC1S2's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.82× as strongly (z diff +0.80); strongest at Topotecan (hydrochloride) 5 µM: 1.74x vs 2.94x (z diff +3.0) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers BLOC1S2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises BLOC1S2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.36× lower at baseline in the lines without EDA2R | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[PTCHD4]] | B | PTCHD4 activity raises BLOC1S2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.43× lower at baseline in the lines without PTCHD4 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PINCR]] | B | PINCR activity raises BLOC1S2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.34× lower at baseline in the lines without PINCR | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[FDXR]] | B | FDXR activity raises BLOC1S2's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without FDXR | 0.047 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[ACTA2]] | B | ACTA2 activity raises BLOC1S2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without ACTA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, 35.5); signed map (41.4, -23.8). **Vector** length 106, 30.6% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +13.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.1 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +5.0 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | +0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | biogenesis of lysosomal organelles complex 1 subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,273,280-100,286,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10120, FLJ30135, BLOS2, BORCS2 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits; BLOC-1 related complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6QNY1](https://www.uniprot.org/uniprotkb/Q6QNY1) (Biogenesis of lysosome-related organelles complex 1 subunit 2):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension (By similarity). As part of the …

**Summary**, from NCBI Gene [282991](https://www.ncbi.nlm.nih.gov/gene/282991):

> This gene encodes a protein with multiple functions. The encoded protein has been found in association with the centrosome, shown to co-localize with gamma-tubulin, and also found to be one of the proteins in the BLOC-1 complex which functions in the formation of lysosome-related organelles. A pseudogene of this gene is located on the X chromosome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:20984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20984) · Entrez [282991](https://www.ncbi.nlm.nih.gov/gene/282991) · UniProt [Q6QNY1](https://www.uniprot.org/uniprotkb/Q6QNY1) · Ensembl [ENSG00000196072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196072)

## Data

Gene col 12124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12124); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12124]; `tensor/DDL_lfc|DDL_z.npy` [12124]; `embed/gene_vectors.npy` [12124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12124 or target_col == 12124). Every well: [[BLOC1S2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLOC1S2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
