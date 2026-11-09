---
symbol: "PPP1R2"
type: "gene"
col: 11501
ensembl_id: "ENSG00000184203"
name: "protein phosphatase 1 regulatory inhibitor subunit 2"
location: "3q29"
module: 204
arm: "+"
pooled_cpm: 76.08
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# PPP1R2

*protein phosphatase 1 regulatory inhibitor subunit 2* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.38× (z +13.0, q 1e-35, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.189×, NCI-H2347 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.387×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.126×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL3]] (+0.76, fdr 7e-06), [[GMCL1]] (+0.71, fdr 1e-05), [[MOSPD3]] (+0.71, fdr 1e-05); moves opposite to [[DNAJC11]] (-0.71, fdr 7e-06), [[REXO1]] (-0.70, fdr 7e-06), [[ZSCAN29]] (-0.69, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR160]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.38×** | +13.0 | 1e-35 | 47/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +11.9 | 3e-30 | 46/48 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +11.0 | 6e-26 | 45/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.89×** | +9.5 | 2e-19 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.64×** | +7.4 | 1e-11 | 34/48 (NCI-H460, KATO III, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.32×** | +5.9 | 4e-07 | 32/48 (A498, SW1417, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.53×** | +5.8 | 5e-07 | 37/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.8 | 6e-07 | 30/49 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.72×** | +4.2 | 0.001 | 32/49 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.1 | 0.002 | 23/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.31×** | +4.1 | 0.002 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.012 | 22/48 (LoVo, KATO III, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.4 | 0.035 | 20/45 (LoVo, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.060 | 15/49 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.060 | 17/49 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.076 | 21/48 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.078 | 22/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11501.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.189×, NCI-H2347 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.387×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.6 | 0.002 | 1/50 (SW48) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.795× | -3.1 | 0.48 | 18/48 (KATO III, NCI-H1792, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.2 | 8 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.48× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.70× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 69.2 | 8 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.77× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.67× (z +12.3) | — |
| [[LoVo (line)]] | wt | 54.4 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +11.7) | — |
| [[KATO III (line)]] | alt | 103 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.56× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.57× (z +12.9) | — |
| [[SW1417 (line)]] | alt | 123 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.09× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.71× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 104 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 63.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 68.4 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.93× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.75× (z +9.3) | — |
| [[A-427 (line)]] | wt | 45.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 46.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 53.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.98× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.65× (z +9.1) | — |
| [[A-172 (line)]] | wt | 57.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +9.0) | — |
| [[A498 (line)]] | wt | 63.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.3) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[AsPC-1 (line)]] | alt | 91.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 80.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.41× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HEC-1-A (line)]] | alt | 81.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 72.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 74.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 71.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.00× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 56.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 81.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 80.2 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[A549 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 116 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 152 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | +0.76 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.71 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.71 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ORC4]] | +0.70 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RAB8B]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.69 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.67 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SNX1]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.67 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PJA2]] | +0.67 | +0.71 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.71 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[REXO1]] | -0.70 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[ZSCAN29]] | -0.69 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ST7L]] | -0.68 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.68 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[EXOSC6]] | -0.67 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[EMG1]] | -0.67 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ITPA]] | -0.66 | -0.68 / -0.40 | both halves | 4e-05 |  |
| [[TAF2]] | -0.65 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.65 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[MIS12]] | -0.64 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MED1]] | -0.64 | -0.70 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR160]] | B | GPR160 activity raises PPP1R2's level | lines that do not express GPR160 (8) vs lines expressing it (42) | 1.22× lower at baseline in the lines without GPR160 | 0.076 | ⚠ within organs, on part of the lines; also absent: PNPLA4, PRKCZ; maybe low, not absent |
| [[IRF6]] | B | IRF6 activity raises PPP1R2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.32× lower at baseline in the lines without IRF6 | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, -12.6); signed map (-33.7, 16.9). **Vector** length 95.3, 27.7% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.7 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +2.7 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,514,428-195,543,386 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPP2, PPP1R2A |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P41236](https://www.uniprot.org/uniprotkb/P41236) (Protein phosphatase inhibitor 2):

> Inhibitor of protein-phosphatase 1.

**Summary**, from NCBI Gene [5504](https://www.ncbi.nlm.nih.gov/gene/5504):

> Protein phosphatase-1 (PP1) is one of the main eukaryotic serine/threonine phosphatases. The protein encoded by this gene binds to the catalytic subunit of PP1, strongly inhibiting its activity. Ten related pseudogenes have been found throughout the human genome. Several splice variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:9288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9288) · Entrez [5504](https://www.ncbi.nlm.nih.gov/gene/5504) · UniProt [P41236](https://www.uniprot.org/uniprotkb/P41236) · Ensembl [ENSG00000184203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184203)

## Data

Gene col 11501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11501); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11501]; `tensor/DDL_lfc|DDL_z.npy` [11501]; `embed/gene_vectors.npy` [11501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11501 or target_col == 11501). Every well: [[PPP1R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
