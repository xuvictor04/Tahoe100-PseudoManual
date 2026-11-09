---
symbol: "HOXC4"
type: "gene"
col: 12575
ensembl_id: "ENSG00000198353"
name: "homeobox C4"
location: "12q13.13"
module: 10
arm: "+"
pooled_cpm: 4.96
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 5
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# HOXC4

*homeobox C4* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.45× (z +4.7, q 0.001, up in 6 of 36 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.44× (z +4.5, q 0.001, up in 15 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -10.4, q 1e-22, down in 26 of 29 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.463× (z -6.8, q 1e-09, down in 23 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLJ12825]] (+0.82, fdr 7e-06, ⚠ same locus), [[HOXC6]] (+0.71, fdr 7e-06, ⚠ same locus), [[KLHL14]] (+0.52, fdr 6e-05), [[PATZ1]] (+0.51, fdr 5e-05), [[SEPTIN5]] (+0.50, fdr 3e-05); moves opposite to [[BACE2]] (-0.49, fdr 6e-05), [[GABRE]] (-0.45, fdr 7e-05), [[ATG12]] (-0.45, fdr 8e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CTNNA2]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.45×** | +4.7 | 0.001 | 6/36 (AsPC-1, HT-29, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.6 | 0.001 | 1/7 (C32) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.44×** | +4.5 | 0.001 | 15/35 (PANC-1, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.004 | 11/34 (A549, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.037 | 11/35 (RKO, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.039 | 10/33 (PANC-1, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.433×** | -10.4 | 1e-22 | 26/29 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.320×** | -10.0 | 3e-21 | 29/35 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.359×** | -8.2 | 6e-14 | 22/34 (AsPC-1, AN3 CA, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.407×** | -7.9 | 4e-13 | 24/35 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.417×** | -7.7 | 2e-12 | 26/35 (AsPC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.463×** | -6.8 | 1e-09 | 23/35 (A-172, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.472×** | -6.6 | 3e-09 | 20/36 (AN3 CA, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -6.4 | 9e-09 | 20/28 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.497×** | -6.2 | 5e-08 | 17/35 (HOP62, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.519×** | -5.8 | 5e-07 | 23/35 (SW480, A-427, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.549×** | -5.3 | 7e-06 | 18/28 (PANC-1, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.565×** | -5.0 | 3e-05 | 20/34 (AN3 CA, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.576×** | -4.8 | 6e-05 | 19/36 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.582×** | -4.7 | 9e-05 | 16/34 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -4.5 | 3e-04 | 12/21 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.593×** | -4.2 | 0.001 | 12/36 (PANC-1, RKO, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.005 | 11/35 (HT-29, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.746×** | -3.6 | 0.009 | 11/34 (SW480, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.667×** | -3.3 | 0.024 | 15/32 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.685×** | -3.3 | 0.025 | 12/35 (AN3 CA, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.7 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 4.38 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0964× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0363× (z -12.4) |
| [[C32 (line)]] | wt | 13.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HOP62 (line)]] | alt | 2.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 4.95 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.123× (z -9.1) |
| [[SW480 (line)]] | alt | 4.98 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLJ12825]] | +0.82 | +0.83 / +0.72 | both halves | 7e-06 | ⚠ same locus (2.2 kb, same strand: neighbours can correlate without regulation) |
| [[HOXC6]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; STRING 966; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[KLHL14]] | +0.52 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[PATZ1]] | +0.51 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[SEPTIN5]] | +0.50 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[AMER1]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PCDHB2]] | +0.49 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[TBX1]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ERICH6-AS1]] | +0.49 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[ARHGEF25]] | +0.48 | +0.53 / +0.32 | both halves | 2e-04 |  |
| [[ZNF362]] | +0.48 | +0.44 / +0.36 | both halves | 1e-04 |  |
| [[ADGRB1]] | +0.47 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[HENMT1]] | +0.47 | +0.43 / +0.27 | both halves | 3e-04 |  |
| [[CD99L2]] | +0.46 | +0.44 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACE2]] | -0.49 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GABRE]] | -0.45 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[ATG12]] | -0.45 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[LUCAT1]] | -0.44 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[RSPH3]] | -0.43 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[WFDC10B]] | -0.42 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SERPINB1]] | -0.40 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[SIRT6]] | -0.40 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[PPP1R13L]] | -0.40 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[WFDC3]] | -0.39 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[KRBOX4]] | -0.39 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[BACH1]] | -0.39 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTNNA2]] | B | CTNNA2 activity raises HOXC4's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.67× lower at baseline in the lines without CTNNA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[HOTAIR]] | B | HOTAIR activity raises HOXC4's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without HOTAIR | 0.011 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[MXRA8]] | B | MXRA8 activity raises HOXC4's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without MXRA8 | 0.055 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[TM4SF19-DYNLT2B]] | B | TM4SF19-DYNLT2B activity lowers HOXC4's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 2.15× higher at baseline in the lines without TM4SF19-DYNLT2B | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[HOTAIR]] | B | HOTAIR activity strengthens HOXC4's drug response | lines that do not express HOTAIR (18) vs lines expressing it (19) | the lines without HOTAIR respond 0.67× as strongly (z diff +1.05); strongest at Homoharringtonine 0.5 µM: 0.46x vs 0.23x (z diff +2.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P; target measured in part of the lines; artifact flags |
| [[FLJ12825]] | C | FLJ12825 activity raises HOXC4's level | lines that do not express FLJ12825 (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without FLJ12825 | 0.002 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent; co-absent with the target |
| [[HOXC6]] | C | HOXC6 activity raises HOXC4's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without HOXC6 | 0.022 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |
| [[LINC01013]] | C | LINC01013 activity raises HOXC4's level | lines that do not express LINC01013 (7) vs lines expressing it (43) | 3.10× lower at baseline in the lines without LINC01013 | 0.061 | ⚠ within organs, on part of the lines; also absent: HOXC9, HOXC4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | HOXC4 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express HOXC4 (11) vs lines expressing it (37) | the lines without HOXC4: 0.89× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent |
| [[NUDT13]] | B | HOXC4 activity raises NUDT13's level | lines that do not express HOXC4 (11) vs lines expressing it (39) | 1.22× lower at baseline in the lines without HOXC4 | 0.095 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 5 µM | B | HOXC4 activity lowers the cells' numbers under Trifluridine 5 µM (makes them more sensitive) | lines that do not express HOXC4 (11) vs lines expressing it (37) | the lines without HOXC4: 1.12× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent |
| [[HOXC6]] | C | HOXC4 activity raises HOXC6's level | lines that do not express HOXC4 (11) vs lines expressing it (39) | 4.62× lower at baseline in the lines without HOXC4 | 0.006 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent; co-absent with the target |
| [[FLJ12825]] | C | HOXC4 activity raises FLJ12825's level | lines that do not express HOXC4 (11) vs lines expressing it (39) | 2.40× lower at baseline in the lines without HOXC4 | 0.071 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.215). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.1, 25.7); signed map (33.7, -22.7). **Vector** length 52.1, 8.01% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.3 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +1.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | +4.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.4 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.4 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.3 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.3 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | homeobox C4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,016,931-54,056,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX3, HOX3E |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 6 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis; Somatic hypermutation of immunoglobulin genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P09017](https://www.uniprot.org/uniprotkb/P09017) (Homeobox protein Hox-C4):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3221](https://www.ncbi.nlm.nih.gov/gene/3221):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, which are located on different chromosomes and consist of 9 to 11 genes arranged in tandem. This gene, HOXC4, is one of several homeobox HOXC genes located in a cluster on chromosome 12. Three genes, HOXC5, HOXC4 …

**Accessions** — [HGNC:5126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5126) · Entrez [3221](https://www.ncbi.nlm.nih.gov/gene/3221) · UniProt [P09017](https://www.uniprot.org/uniprotkb/P09017) · Ensembl [ENSG00000198353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198353)

## Data

Gene col 12575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12575); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12575]; `tensor/DDL_lfc|DDL_z.npy` [12575]; `embed/gene_vectors.npy` [12575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12575 or target_col == 12575). Every well: [[HOXC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
