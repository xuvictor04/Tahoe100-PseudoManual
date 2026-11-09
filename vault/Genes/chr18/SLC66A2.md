---
symbol: "SLC66A2"
type: "gene"
col: 4344
ensembl_id: "ENSG00000122490"
name: "solute carrier family 66 member 2"
location: "18q23"
module: 160
arm: "+"
pooled_cpm: 28.62
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# SLC66A2

*solute carrier family 66 member 2* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.26× (z +18.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.695× (z -8.3, q 5e-14, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRTN]] (+0.68, fdr 3e-05), [[SH2B2]] (+0.67, fdr 2e-05), [[RALGDS]] (+0.65, fdr 1e-05); moves opposite to [[MBTPS2]] (-0.67, fdr 7e-06), [[HDHD2]] (-0.64, fdr 1e-05), [[DUS4L]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTXN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.26×** | +18.6 | 0e+00 | 46/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +18.3 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +16.1 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +10.4 | 2e-23 | 37/47 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +9.3 | 1e-18 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.27×** | +7.7 | 1e-12 | 24/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +6.1 | 7e-08 | 23/48 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +5.4 | 6e-06 | 22/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +5.1 | 2e-05 | 16/48 (MIA PaCa-2, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 2e-05 | 16/47 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.8 | 7e-05 | 16/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.15× | +4.6 | 2e-04 | 20/48 (NCI-H460, HEC-1-A, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.5 | 3e-04 | 18/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 16/46 (A-427, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.20×** | +4.2 | 0.001 | 17/48 (NCI-H460, SW48, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 15/48 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.004 | 5/48 (NCI-H1792, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.6 | 0.009 | 8/48 (NCI-H1792, A498, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.020 | 6/46 (LOX-IMVI, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -8.3 | 5e-14 | 31/48 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -7.2 | 2e-10 | 22/37 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -7.0 | 5e-10 | 25/48 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.739×** | -6.4 | 3e-08 | 25/47 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.763×** | -6.2 | 7e-08 | 23/43 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.828×** | -6.1 | 9e-08 | 21/48 (NCI-H2347, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.771×** | -5.7 | 8e-07 | 25/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -5.4 | 5e-06 | 14/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.825×** | -4.0 | 0.003 | 11/48 (SW48, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -3.2 | 0.078 | 12/42 (A-427, C32, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.861× | -3.1 | 0.087 | 3/48 (LS 180, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.2 | 12 (9 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.40× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.19× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.1 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -12.8) |
| [[PANC-1 (line)]] | alt | 48.0 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.28× (z +15.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.62× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.17× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -24.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.507× (z -10.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[C-33 A (line)]] | alt | 67.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.40× (z +10.2) | — |
| [[SW48 (line)]] | wt | 68.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +8.5) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -11.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.19× (z +9.8) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 29.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +8.9) | — |
| [[A-172 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRTN]] | +0.68 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SH2B2]] | +0.67 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RALGDS]] | +0.65 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CFD]] | +0.65 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[RAC3]] | +0.65 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[RTN2]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ADGRL1]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[NECTIN2]] | +0.64 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[MEX3D]] | +0.64 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[FBXO46]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.63 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SH3GL1]] | +0.63 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBTPS2]] | -0.67 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[HDHD2]] | -0.64 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[DUS4L]] | -0.63 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[ZNF564]] | -0.63 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[EIF4G2]] | -0.63 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RNF6]] | -0.62 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.62 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[DDX6]] | -0.61 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.61 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PRKAR1A]] | -0.60 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ZNF280D]] | -0.60 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[ZMPSTE24]] | -0.60 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTXN1]] | B | CTXN1 activity raises SLC66A2's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without CTXN1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (6.8, -0.1); signed map (-29.0, 18.4). **Vector** length 95.3, 20.8% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.5 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +16.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +18.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +18.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +4.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +2.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +5.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.1 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.9 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 66 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,902,420-79,951,657 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22378; previously PQLC1 |
| Gene groups (HGNC) | Solute carrier family 66 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [Q8N2U9](https://www.uniprot.org/uniprotkb/Q8N2U9) carries no function annotation.

**Summary**, from NCBI Gene [80148](https://www.ncbi.nlm.nih.gov/gene/80148):

> Predicted to be involved in phospholipid translocation and retrograde transport, endosome to Golgi. Predicted to be located in cytosol and membrane. Predicted to be active in endosome membrane and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26188) · Entrez [80148](https://www.ncbi.nlm.nih.gov/gene/80148) · UniProt [Q8N2U9](https://www.uniprot.org/uniprotkb/Q8N2U9) · Ensembl [ENSG00000122490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122490)

## Data

Gene col 4344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4344); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4344]; `tensor/DDL_lfc|DDL_z.npy` [4344]; `embed/gene_vectors.npy` [4344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4344 or target_col == 4344). Every well: [[SLC66A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC66A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
