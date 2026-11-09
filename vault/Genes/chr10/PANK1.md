---
symbol: "PANK1"
type: "gene"
col: 7658
ensembl_id: "ENSG00000152782"
name: "pantothenate kinase 1"
location: "10q23.31"
module: 62
arm: "+"
pooled_cpm: 10.51
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PANK1

*pantothenate kinase 1* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.43× (z +25.0, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.603× (z -10.3, q 3e-22, down in 33 of 43 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.637× (z -6.5, q 2e-08, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOR3A]] (+0.66, fdr 2e-05), [[EI24]] (+0.65, fdr 7e-06), [[TMEM68]] (+0.64, fdr 1e-05); moves opposite to [[ABAT]] (-0.58, fdr 4e-05), [[NBEAL1]] (-0.56, fdr 2e-05), [[SPAG9]] (-0.56, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC47A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +25.0 | 0e+00 | 42/43 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.14×** | +10.5 | 3e-23 | 28/45 (LS 180, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.94×** | +9.5 | 5e-19 | 26/46 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +9.4 | 1e-18 | 32/47 (A549, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.92×** | +9.4 | 1e-18 | 29/46 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.97×** | +9.3 | 1e-18 | 25/37 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.92×** | +9.0 | 2e-17 | 26/41 (A498, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.70×** | +7.6 | 3e-12 | 24/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.65×** | +7.2 | 5e-11 | 27/46 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +7.0 | 2e-10 | 23/44 (A549, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +6.6 | 3e-09 | 25/46 (A-427, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 8/45 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.2 | 0.001 | 14/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 11/45 (HT-29, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.002 | 5/45 (LoVo, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 10/46 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.013 | 8/45 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.018 | 12/45 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.0 | 0.066 | 10/46 (A549, NCI-H460, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +2.9 | 0.072 | 9/46 (C-33 A, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.23×** | +2.8 | 0.091 | 2/45 (A-172, PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.603×** | -10.3 | 3e-22 | 33/43 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.637×** | -6.5 | 2e-08 | 22/45 (A-172, NCI-H460, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.699×** | -5.0 | 1e-04 | 18/44 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -4.1 | 0.006 | 17/45 (SW480, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -3.7 | 0.021 | 15/44 (C32, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.641×** | -3.4 | 0.076 | 7/44 (HEC-1-A, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.10 | 12/45 (HepG2/C3A, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.8 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -18.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.163× (z -12.7) |
| [[A-172 (line)]] | wt | 9.46 | 2 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.06× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ivermectin (drug)]] 0.5 µM 0.132× (z -10.4) |
| [[A498 (line)]] | wt | 6.56 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +12.0) | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0772× (z -12.1) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 26.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 10.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.9) | [[Bortezomib (drug)]] 5 µM 0.0836× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 7.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.0) | [[Pimozide (drug)]] 0.05 µM 0.0799× (z -10.7) |
| [[A549 (line)]] | wt | 5.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.93× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 7.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +8.5) | — |
| [[LoVo (line)]] | wt | 9.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +16.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 4.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0953× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 6.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +11.2) | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.101× (z -9.3) |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR3A]] | +0.66 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[EI24]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TMEM68]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[FBXO22]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[NDC1]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SLC12A9]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HOXA10]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[TIGAR]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SESN1]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SLC35D1]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ABHD14A]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CIAO2A]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABAT]] | -0.58 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NBEAL1]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[SPAG9]] | -0.56 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[DLGAP4]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[KLF2]] | -0.55 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SPTAN1]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[NEK1]] | -0.52 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[CALN1]] | -0.51 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[SAMD4B]] | -0.51 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[GNG7]] | -0.51 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[CAST]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[CREB3]] | -0.50 | -0.54 / -0.34 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC47A1]] | B | SLC47A1 activity raises PANK1's level | lines that do not express SLC47A1 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without SLC47A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: DUSP9, STOX2, NOVA2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PANK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens PANK1's drug response | lines that do not express PINCR (28) vs lines expressing it (19) | the lines without PINCR respond 0.70× as strongly (z diff +1.05); strongest at Doxorubicin (hydrochloride) 5 µM: 1.66x vs 2.70x (z diff +2.6) | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PANK1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TP53]] | C | TP53 activity strengthens PANK1's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 17 not recorded | the TP53-altered lines respond 0.69× as strongly (z diff +1.14); strongest at Doxorubicin (hydrochloride) 5 µM: 1.61x vs 3.06x (z diff +3.1) | 0.907 over the table, 0.086 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, 34.4); signed map (42.9, -26.2). **Vector** length 88.6, 18.1% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +25.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.5 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +4.8 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.0 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.9 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -1.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.3 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -6.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | pantothenate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,579,497-89,645,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24596, PANK1a, PANK1b; previously PANK |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pantothenate kinase family |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE04](https://www.uniprot.org/uniprotkb/Q8TE04) (Pantothenate kinase 1):

> [Isoform 1]: Catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis.

**Summary**, from NCBI Gene [53354](https://www.ncbi.nlm.nih.gov/gene/53354):

> This gene encodes a member of the pantothenate kinase family. Pantothenate kinases are key regulatory enzymes in the biosynthesis of coenzyme A (CoA). The encoded protein catalyzes the first and rate-limiting enzymatic reaction in CoA biosynthesis and is regulated by CoA through feedback inhibition. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. This gene and an intronic miRNA on the same strand are co-regulated by the tumor suppressor p53 …

**Accessions** — [HGNC:8598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8598) · Entrez [53354](https://www.ncbi.nlm.nih.gov/gene/53354) · UniProt [Q8TE04](https://www.uniprot.org/uniprotkb/Q8TE04) · Ensembl [ENSG00000152782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152782)

## Data

Gene col 7658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7658); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7658]; `tensor/DDL_lfc|DDL_z.npy` [7658]; `embed/gene_vectors.npy` [7658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7658 or target_col == 7658). Every well: [[PANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
