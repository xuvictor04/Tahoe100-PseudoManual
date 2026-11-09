---
symbol: "RSKR"
type: "gene"
col: 9478
ensembl_id: "ENSG00000167524"
name: "ribosomal protein S6 kinase related"
location: "17q11.2"
module: 38
arm: "+"
pooled_cpm: 23.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# RSKR

*ribosomal protein S6 kinase related* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +8.9, q 4e-16, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.429× (z -12.2, q 2e-31, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6-1]] (+0.69, fdr 7e-06), [[UBE2F-SCLY]] (+0.63, fdr 1e-05), [[WNT2B]] (+0.62, fdr 7e-06); moves opposite to [[CLK4]] (-0.57, fdr 4e-05), [[UBQLN2]] (-0.55, fdr 6e-05), [[DUSP19]] (-0.55, fdr 8e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPNMB]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +8.9 | 4e-16 | 35/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.3 | 2e-14 | 19/31 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +8.2 | 5e-14 | 32/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +8.1 | 1e-13 | 27/47 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.4 | 1e-08 | 24/41 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 5e-05 | 23/47 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +4.2 | 0.002 | 21/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.9 | 0.008 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.18× | +3.5 | 0.032 | 10/48 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.29×** | +3.4 | 0.032 | 13/38 (SW1417, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +3.1 | 0.086 | 12/48 (A-172, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.24× | +3.1 | 0.11 | 10/47 (SW1417, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.429×** | -12.2 | 2e-31 | 41/47 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -8.3 | 3e-14 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -7.4 | 2e-11 | 28/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -7.3 | 2e-11 | 27/47 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -7.3 | 2e-11 | 26/46 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -7.2 | 5e-11 | 30/45 (SK-MEL-2, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.713×** | -7.2 | 5e-11 | 27/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -6.9 | 3e-10 | 29/48 (HT-29, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.732×** | -6.6 | 2e-09 | 23/48 (LOX-IMVI, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.743×** | -4.5 | 5e-04 | 22/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.001 | 21/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.633×** | -3.6 | 0.016 | 20/45 (A-172, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.022 | 13/47 (NCI-H2030, A-427, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.087 | 9/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.9 | 0 | 11 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.198× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 65.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.228× (z -14.0) |
| [[PANC-1 (line)]] | alt | 32.4 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -10.6) |
| [[A-172 (line)]] | wt | 27.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -13.3) |
| [[A549 (line)]] | wt | 18.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.7) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.1) |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.198× (z -9.0) |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0715× (z -9.8) |
| [[J82 (line)]] | alt | 23.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.231× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.174× (z -11.3) |
| [[HOP62 (line)]] | alt | 20.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.4) |
| [[RKO (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.105× (z -14.9) |
| [[A498 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.138× (z -9.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0373× (z -8.9) |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6-1]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[UBE2F-SCLY]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[WNT2B]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[DRD4]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[IL9RP3]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[NPIPB11]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FBXL18]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SPG7]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PPM1F]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PFDN2]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | -0.57 | -0.40 / -0.63 | both halves | 4e-05 |  |
| [[UBQLN2]] | -0.55 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[DUSP19]] | -0.55 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[SNX2]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[RAB38]] | -0.55 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[CFL2]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ZNF436]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RBM7]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[NDUFA5]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TAB2]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TMEM184C]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NCOA4]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPNMB]] | B | GPNMB activity lowers RSKR's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.15× higher at baseline in the lines without GPNMB | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[HDAC6]] | B | HDAC6 activity lowers RSKR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | RSKR's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | RSKR's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.489). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, -20.9); signed map (-46.6, -1.6). **Vector** length 97.1, 22.4% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.4 | -12.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.1 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -1.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.2 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase related |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,455,752-28,614,197 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25006, SgK494 |
| Gene groups (HGNC) | Ribosomal protein S6 kinase family |
| Matched by | ensembl_id |

UniProt [Q96LW2](https://www.uniprot.org/uniprotkb/Q96LW2) carries no function annotation.

**Summary**, from NCBI Gene [124923](https://www.ncbi.nlm.nih.gov/gene/124923):

> Predicted to enable protein kinase activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26314) · Entrez [124923](https://www.ncbi.nlm.nih.gov/gene/124923) · UniProt [Q96LW2](https://www.uniprot.org/uniprotkb/Q96LW2) · Ensembl [ENSG00000167524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167524)

## Data

Gene col 9478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9478); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9478]; `tensor/DDL_lfc|DDL_z.npy` [9478]; `embed/gene_vectors.npy` [9478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9478 or target_col == 9478). Every well: [[RSKR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSKR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
