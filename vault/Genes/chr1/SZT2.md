---
symbol: "SZT2"
type: "gene"
col: 12551
ensembl_id: "ENSG00000198198"
name: "SZT2 subunit of KICSTOR complex"
location: "1p34.2"
module: 52
arm: "+"
pooled_cpm: 49.02
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SZT2

*SZT2 subunit of KICSTOR complex* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.50× (z +5.1, q 2e-04, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (MIA PaCa-2 3.20×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.446× (z -10.1, q 2e-21, down in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.740× (z -3.8, q 0.008, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 6 lines (LS 180 0.152×, PANC-1 0.226×, HS-578T 0.184×, SW480 0.273×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (LoVo 0.234×, PANC-1 0.293×, LS 180 0.245×; ⚠ cell-cycle shift, explains ~47% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (COLO 205 0.115×, LoVo 0.183×; ⚠ toxic); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.179×); [[Zileuton (drug)]] 0.5 µM in 1 line (NCI-H661 0.0575×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UVSSA]] (+0.73, fdr 7e-06), [[CHFR]] (+0.71, fdr 7e-06), [[RER1]] (+0.69, fdr 7e-06); moves opposite to [[SPPL3]] (-0.58, fdr 1e-05), [[SSH2]] (-0.57, fdr 1e-05), [[FCHSD2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[POLR3D]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12551.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (MIA PaCa-2 3.20×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +5.1 | 2e-04 | 29/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.005 | 27/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12551.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 6 lines (LS 180 0.152×, PANC-1 0.226×, HS-578T 0.184×, SW480 0.273×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (LoVo 0.234×, PANC-1 0.293×, LS 180 0.245×; ⚠ cell-cycle shift, explains ~47% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (COLO 205 0.115×, LoVo 0.183×; ⚠ toxic); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.179×); [[Zileuton (drug)]] 0.5 µM in 1 line (NCI-H661 0.0575×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.446×** | -10.1 | 2e-21 | 46/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.439×** | -8.3 | 3e-14 | 41/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.556×** | -7.4 | 3e-11 | 39/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.580×** | -6.8 | 1e-09 | 32/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.555×** | -5.9 | 3e-07 | 32/48 (C32, HEC-1-A, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.637×** | -5.7 | 1e-06 | 27/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.524×** | -4.2 | 0.002 | 31/49 (PANC-1, A549, …) | all doses, stronger at high dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.794×** | -4.1 | 0.003 | 26/47 (C32, HEC-1-A, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.726×** | -4.0 | 0.003 | 25/47 (NCI-H1573, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.708×** | -4.0 | 0.003 | 24/44 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.008 | 26/48 (J82, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.748×** | -3.6 | 0.012 | 23/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.0 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.261× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 60.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LS 180 (line)]] | wt | 42.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 82.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 50.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[SNU-1 (line)]] | wt | 62.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 70.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -12.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 79.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[PANC-1 (line)]] | alt | 64.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.208× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C32 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H661 (line)]] | alt | 37.4 | 0 | 1 | — | [[Zileuton (drug)]] 0.5 µM 0.0575× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 31.9 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.179× (z -9.3) |
| [[A-172 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UVSSA]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CHFR]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[RER1]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ZNF417]] | +0.63 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TPD52L2]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[YKT6]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[RUSF1]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MBD1]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TMEM214]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PIGG]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[B4GALT7]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SSH2]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FCHSD2]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CACHD1]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 | same gene group |
| [[FOXP1]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 | same gene group |
| [[MAP3K1]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ARL15]] | -0.52 | -0.50 / -0.39 | both halves | 6e-05 | same gene group |
| [[CDC14A]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PUM1]] | -0.51 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[DENND4C]] | -0.50 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[TCF7L2]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[UVRAG]] | -0.50 | -0.38 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR3D]] | C | SZT2's natural level strengthens POLR3D's drug response | SZT2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.13; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.8, -28.0); signed map (-51.0, 2.8). **Vector** length 81.7, 20.3% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.1 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | -0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | -1.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.6 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | SZT2 subunit of KICSTOR complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,389,882-43,454,247 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10387, SZT2B, RP11-506B15.1, FLJ34502, SZT2A, KICS1; previously C1orf84, KIAA0467 |
| Gene groups (HGNC) | KICSTOR complex; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T011](https://www.uniprot.org/uniprotkb/Q5T011) (KICSTOR complex protein SZT2):

> As part of the KICSTOR complex functions in the amino acid-sensing branch of the TORC1 signaling pathway. Recruits, in an amino acid-independent manner, the GATOR1 complex to the lysosomal membranes and allows its interaction with GATOR2 and the RAG GTPases. Functions upstream of the RAG GTPases and is required to negatively regulate mTORC1 signaling in absence of amino acids. In absence of the KICSTOR complex mTORC1 is constitutively localized to the lysosome and activated. The KICSTOR complex …

**Summary**, from NCBI Gene [23334](https://www.ncbi.nlm.nih.gov/gene/23334):

> The protein encoded by this gene is expressed in the brain, predominantly in the parietal and frontal cortex as well as in dorsal root ganglia. It is localized to the peroxisome, and is implicated in resistance to oxidative stress. It likely functions by increasing superoxide dismutase (SOD) activity, but itself has no direct SOD activity. Studies in mice show that this gene confers low seizure threshold, and may also enhance epileptogenesis. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:29040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29040) · Entrez [23334](https://www.ncbi.nlm.nih.gov/gene/23334) · UniProt [Q5T011](https://www.uniprot.org/uniprotkb/Q5T011) · Ensembl [ENSG00000198198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198198)

## Data

Gene col 12551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12551); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12551]; `tensor/DDL_lfc|DDL_z.npy` [12551]; `embed/gene_vectors.npy` [12551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12551 or target_col == 12551). Every well: [[SZT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SZT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
