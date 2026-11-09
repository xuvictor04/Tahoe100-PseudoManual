---
symbol: "DYNC2I2"
type: "gene"
col: 4055
ensembl_id: "ENSG00000119333"
name: "dynein 2 intermediate chain 2"
location: "9q34.11"
module: 6
arm: "+"
pooled_cpm: 13.92
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DYNC2I2

*dynein 2 intermediate chain 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.61× (z +15.8, q 0e+00, up in 33 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.40× (z +4.2, q 0.002, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.557× (z -7.2, q 4e-10, down in 29 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.571× (z -6.9, q 2e-09, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM4]] (+0.77, fdr 7e-06), [[MCM2]] (+0.75, fdr 7e-06), [[CENPH]] (+0.74, fdr 7e-06); moves opposite to [[RPL37]] (-0.59, fdr 1e-05, ⚠ RPL37 in the vector space only through flagged drug-doses).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.61×** | +15.8 | 0e+00 | 33/34 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.57×** | +15.0 | 0e+00 | 23/23 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.33×** | +9.6 | 1e-19 | 24/27 (J82, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.92×** | +7.7 | 2e-12 | 23/37 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +5.9 | 5e-07 | 25/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +4.2 | 0.002 | 15/48 (HOP62, LoVo, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.27×** | +4.2 | 0.002 | 16/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.002 | 17/48 (A498, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.39×** | +4.0 | 0.003 | 15/39 (SNU-423, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.35×** | +3.6 | 0.020 | 17/44 (A498, NCI-H460, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.32×** | +3.4 | 0.034 | 12/48 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.037 | 16/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.039 | 12/48 (BT-474, A498, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.20×** | +3.2 | 0.056 | 16/46 (A549, A498, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~79% of this change | **1.31×** | +3.2 | 0.056 | 16/39 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.071 | 5/44 (HOP62, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -7.2 | 4e-10 | 29/45 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -6.9 | 2e-09 | 32/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -5.6 | 4e-06 | 22/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.664×** | -4.8 | 3e-04 | 23/46 (HCT15, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -4.6 | 6e-04 | 20/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.776×** | -4.4 | 1e-03 | 23/46 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.005 | 20/47 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.724×** | -4.0 | 0.005 | 17/47 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -3.6 | 0.018 | 11/46 (H4, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.827×** | -3.3 | 0.055 | 14/48 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.759×** | -3.3 | 0.055 | 13/47 (J82, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.055 | 19/47 (C-33 A, Panc 03.27, …) | top dose only |  |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.762×** | -3.2 | 0.059 | 11/47 (hTERT-HPNE, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.780×** | -3.1 | 0.089 | 8/47 (HCT15, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.0 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.93× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Digitoxin (drug)]] 5 µM 0.224× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -8.9) |
| [[A498 (line)]] | wt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.1) |
| [[PANC-1 (line)]] | alt | 9.14 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.202× (z -9.4) |
| [[C32 (line)]] | wt | 4.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0702× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 8.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.69× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 9.96 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0700× (z -10.7) |
| [[SNU-423 (line)]] | alt | 8.72 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.118× (z -8.7) |
| [[A-172 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM4]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MCM2]] | +0.75 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[CENPH]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CENPM]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[TCF19]] | +0.72 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[E2F1]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[TIMELESS]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[HELLS]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[TYMS]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL37]] ⚠ | -0.59 | -0.55 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises DYNC2I2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without CDC25A | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises DYNC2I2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without E2F2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises DYNC2I2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without FAM111B | 0.040 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises DYNC2I2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without TCF19 | 0.062 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises DYNC2I2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without E2F8 | 0.098 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[RRM1]] | C | RRM1's natural level strengthens DYNC2I2's drug response | RRM1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.03; direction clear | 0.004 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[GINS1]] | C | GINS1's natural level strengthens DYNC2I2's drug response | GINS1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.41; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ZNF367]] | C | ZNF367 activity raises DYNC2I2's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without ZNF367 | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises DYNC2I2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without DSCC1 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.0, -44.0); signed map (-38.0, -47.3). **Vector** length 71.9, 13.8% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 65); *DNA strand elongation* (reactome, mean cos +0.58 to 28); *DNA Replication* (reactome, mean cos +0.55 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.0 | +15.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.1 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +3.3 | +7.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.1 | -4.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -2.2 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | dynein 2 intermediate chain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,633,653-128,656,847 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIC5, MGC20486, bA216B9.3, FAP133, CFAP133; previously WDR34 |
| Gene groups (HGNC) | WD repeat domain containing; Cilia and flagella associated; Dynein 2 complex subunits; Dynein intermediate chains |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EX3](https://www.uniprot.org/uniprotkb/Q96EX3) (Cytoplasmic dynein 2 intermediate chain 2):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 2 complex (dynein-2 complex), a motor protein complex that drives the movement of cargos along microtubules within cilia and flagella in concert with the intraflagellar transport (IFT) system. DYNC2I2 plays a major role in retrograde ciliary protein trafficking and in ciliogenesis. Required also to maintain a functional transition zone.; Acts as a negative regulator of the Toll-like and IL-1R receptor signaling …

**Summary**, from NCBI Gene [89891](https://www.ncbi.nlm.nih.gov/gene/89891):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Defects in this gene are a cause of short-rib thoracic dysplasia 11 with or …

**Accessions** — [HGNC:28296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28296) · Entrez [89891](https://www.ncbi.nlm.nih.gov/gene/89891) · UniProt [Q96EX3](https://www.uniprot.org/uniprotkb/Q96EX3) · Ensembl [ENSG00000119333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119333)

## Data

Gene col 4055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4055); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4055]; `tensor/DDL_lfc|DDL_z.npy` [4055]; `embed/gene_vectors.npy` [4055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4055 or target_col == 4055). Every well: [[DYNC2I2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC2I2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
