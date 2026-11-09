---
symbol: "NIM1K"
type: "gene"
col: 10823
ensembl_id: "ENSG00000177453"
name: "NIM1 serine/threonine protein kinase"
location: "5p12"
module: 38
arm: "+"
pooled_cpm: 5.76
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# NIM1K

*NIM1 serine/threonine protein kinase* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.69× (z +29.1, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.521× (z -8.7, q 2e-15, down in 22 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.569× (z -7.5, q 1e-11, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADORA1]] (+0.64, fdr 1e-05), [[ISM2]] (+0.60, fdr 2e-05), [[TMEM45A]] (+0.59, fdr 1e-05); moves opposite to [[PTAR1]] (-0.49, fdr 4e-05), [[EFR3A]] (-0.47, fdr 1e-04), [[MDM1]] (-0.47, fdr 0.001, ⚠ one half only (not replicated)).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HTRA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.69×** | +29.1 | 0e+00 | 37/38 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.96×** | +14.5 | 6e-45 | 29/41 (SW480, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +13.5 | 3e-39 | 25/37 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +12.0 | 5e-31 | 31/38 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.36×** | +11.4 | 3e-28 | 31/44 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +9.8 | 1e-20 | 27/43 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +9.6 | 9e-20 | 24/43 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.00×** | +9.2 | 2e-18 | 28/43 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +8.9 | 3e-17 | 27/45 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.5 | 8e-16 | 15/45 (BT-474, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +7.8 | 4e-13 | 5/14 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.73×** | +7.0 | 1e-10 | 0/12 | all doses, flat | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +6.4 | 7e-09 | 16/39 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +6.2 | 3e-08 | 15/46 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +5.5 | 1e-06 | 12/41 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +5.5 | 2e-06 | 14/38 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.54×** | +5.4 | 2e-06 | 10/41 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 1e-05 | 10/34 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 5e-04 | 5/34 (A-427, A498, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -8.7 | 2e-15 | 22/34 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -7.5 | 1e-11 | 19/44 (NCI-H1792, C32, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -7.5 | 1e-11 | 20/41 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.8 | 2e-04 | 15/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.535×** | -4.4 | 0.001 | 12/37 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -4.3 | 0.002 | 17/32 (NCI-H1792, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.728×** | -4.2 | 0.002 | 15/44 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Bestatin (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.039 | 2/44 (AsPC-1, HCT15) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.839× | -3.3 | 0.056 | 9/43 (C32, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.786×** | -3.2 | 0.070 | 9/43 (RPMI-7951, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.076 | 4/45 (C-33 A, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 35.8 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -13.4) |
| [[PANC-1 (line)]] | alt | 3.28 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 12.5× (z +12.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0389× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.98 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0608× (z -11.2) |
| [[C32 (line)]] | wt | 9.40 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0781× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -8.5) |
| [[HOP62 (line)]] | alt | 8.24 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +10.4) | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.97 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 3.26 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +9.9) | — |
| [[A498 (line)]] | wt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.8) | — |
| [[KATO III (line)]] | alt | 3.43 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0781× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 3.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 7.11 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0984× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 10.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.80× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0984× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0782× (z -11.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADORA1]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ISM2]] | +0.60 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[TMEM45A]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PLCD4]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[C9]] | +0.57 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[GRPEL1]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[WDR5B-DT]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SPAG4]] | +0.56 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[C9orf24]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[LDHC]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CCDC181]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LRRC23]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTAR1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[EFR3A]] | -0.47 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MDM1]] | -0.47 | -0.15 / -0.51 | ⚠ one half (not replicated) | 0.001 |  |
| [[TTC12]] | -0.46 | -0.17 / -0.41 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTRA3]] | B | HTRA3 activity raises NIM1K's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without HTRA3 | 0.038 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[CRABP2]] | B | CRABP2 activity raises NIM1K's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without CRABP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |
| [[TOP2A]] | B | TOP2A activity lowers NIM1K's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCTD16]] | B | KCTD16 activity raises NIM1K's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without KCTD16 | 0.066 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[LRAT]] | B | LRAT activity raises NIM1K's level | lines that do not express LRAT (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without LRAT | 0.068 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, NR0B1, IL6 |
| [[RNF165]] | B | RNF165 activity raises NIM1K's level | lines that do not express RNF165 (21) vs lines expressing it (29) | 1.89× lower at baseline in the lines without RNF165 | 0.085 | ⚠ within organs, on part of the lines; also absent: TDRP, ZSCAN18, SH3GL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.2, -18.8); signed map (12.9, 19.1). **Vector** length 73.7, 12.6% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +29.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +14.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.7 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -7.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | +1.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NIM1 serine/threonine protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,192,071-43,280,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC42105, NIM1 |
| Gene groups (HGNC) | NIM1K family kinases |
| Matched by | ensembl_id |

UniProt [Q8IY84](https://www.uniprot.org/uniprotkb/Q8IY84) carries no function annotation.

**Summary**, from NCBI Gene [167359](https://www.ncbi.nlm.nih.gov/gene/167359):

> Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Predicted to be involved in intracellular signal transduction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28646) · Entrez [167359](https://www.ncbi.nlm.nih.gov/gene/167359) · UniProt [Q8IY84](https://www.uniprot.org/uniprotkb/Q8IY84) · Ensembl [ENSG00000177453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177453)

## Data

Gene col 10823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10823); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10823]; `tensor/DDL_lfc|DDL_z.npy` [10823]; `embed/gene_vectors.npy` [10823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10823 or target_col == 10823). Every well: [[NIM1K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIM1K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
