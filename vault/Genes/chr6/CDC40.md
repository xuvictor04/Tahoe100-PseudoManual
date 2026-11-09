---
symbol: "CDC40"
type: "gene"
col: 9651
ensembl_id: "ENSG00000168438"
name: "cell division cycle 40"
location: "6q21"
module: 183
arm: "+"
pooled_cpm: 46.82
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# CDC40

*cell division cycle 40* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.67× (z +11.0, q 2e-25, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.643× (z -9.5, q 2e-18, down in 36 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-427 0.169×, SW480 0.368×, NCI-H2347 0.285×, H4 0.121×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.159×, SHP-77 0.222×, PANC-1 0.521×, HEC-1-A 0.398×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0793×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.103×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.167×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNPDA2]] (+0.77, fdr 7e-06), [[JKAMP]] (+0.76, fdr 7e-06), [[TXNL1]] (+0.74, fdr 7e-06); moves opposite to [[TLNRD1]] (-0.56, fdr 1e-05), [[AGO2]] (-0.55, fdr 1e-05), [[GATAD2A]] (-0.54, fdr 1e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +11.0 | 2e-25 | 42/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +10.6 | 1e-23 | 41/49 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +9.8 | 1e-20 | 40/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +8.4 | 6e-15 | 37/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +7.1 | 2e-10 | 27/48 (AsPC-1, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +5.7 | 1e-06 | 27/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 6e-06 | 27/48 (HEC-1-A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.8 | 1e-04 | 15/48 (AsPC-1, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.16× | +4.5 | 5e-04 | 20/48 (HEC-1-A, LS 180, …) | two highest doses | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 5e-04 | 19/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 20/48 (C32, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 18/47 (SW48, H4, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.005 | 17/48 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.032 | 11/48 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.046 | 16/48 (C-33 A, LoVo, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.067 | 13/48 (KATO III, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9651.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A-427 0.169×, SW480 0.368×, NCI-H2347 0.285×, H4 0.121×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.159×, SHP-77 0.222×, PANC-1 0.521×, HEC-1-A 0.398×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0793×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.103×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.167×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -9.5 | 2e-18 | 36/48 (RKO, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -8.3 | 2e-14 | 25/40 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -6.0 | 5e-07 | 2/49 (AsPC-1, SW 1088) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.776×** | -5.4 | 8e-06 | 27/48 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.815×** | -4.0 | 0.006 | 22/45 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.897× | -3.3 | 0.094 | 19/48 (KATO III, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.755× | -3.1 | 0.14 | 11/48 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | 0.867× | -3.1 | 0.15 | 17/47 (HCT15, COLO 205, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.764× | -3.0 | 0.15 | 17/44 (AsPC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.15 | 17/47 (CHP-212, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 75.0 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.02× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.521× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 59.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.92× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -14.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 58.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.1) ⚠ cell-cycle shift, explains ~10% of this change |
| [[LOX-IMVI (line)]] | wt | 66.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0918× (z -11.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -17.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 84.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.167× (z -9.7) |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.103× (z -10.1) |
| [[H4 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[HEC-1-A (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +9.2) | — |
| [[LoVo (line)]] | wt | 37.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 77.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0793× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[RKO (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -14.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPDA2]] | +0.77 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[TXNL1]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[COPS2]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[LMBRD1]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[RTCA]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[VIRMA]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RNF20]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[CGRRF1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[FAM217B]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[EFCAB7]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.56 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[AGO2]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATL1]] | B | ATL1 activity lowers CDC40's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without ATL1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |
| [[GPX8]] | B | GPX8 activity raises CDC40's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without GPX8 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.8, -6.5); signed map (-26.8, -20.1). **Vector** length 108, 27.3% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.7 | +4.3 |
|  | [[NG25 (drug)]] 5 µM |  | +6.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +11.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | -5.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:110,180,141-110,254,275 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRP17, EHB3, PRPF17, FLJ10564 |
| Gene groups (HGNC) | WD repeat domain containing; NTC associated proteins; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60508](https://www.uniprot.org/uniprotkb/O60508) (Pre-mRNA-processing factor 17):

> Required for pre-mRNA splicing as component of the activated spliceosome. Plays an important role in embryonic brain development; this function does not require proline isomerization.

**Summary**, from NCBI Gene [51362](https://www.ncbi.nlm.nih.gov/gene/51362):

> Pre-mRNA splicing occurs in two sequential transesterification steps. The protein encoded by this gene is found to be essential for the catalytic step II in pre-mRNA splicing process. It is found in the spliceosome, and contains seven WD repeats, which function in protein-protein interactions. This protein has a sequence similarity to yeast Prp17 protein, which functions in two different cellular processes: pre-mRNA splicing and cell cycle progression. It suggests that this protein may play a …

**Accessions** — [HGNC:17350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17350) · Entrez [51362](https://www.ncbi.nlm.nih.gov/gene/51362) · UniProt [O60508](https://www.uniprot.org/uniprotkb/O60508) · Ensembl [ENSG00000168438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168438)

## Data

Gene col 9651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9651); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9651]; `tensor/DDL_lfc|DDL_z.npy` [9651]; `embed/gene_vectors.npy` [9651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9651 or target_col == 9651). Every well: [[CDC40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
