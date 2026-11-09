---
symbol: "PLCE1"
type: "gene"
col: 6143
ensembl_id: "ENSG00000138193"
name: "phospholipase C epsilon 1"
location: "10q23.33"
module: 197
arm: "+"
pooled_cpm: 43.45
n_lines_expressing: 34
n_dd_up: 41
n_dd_down: 10
n_dd_up_clean: 28
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# PLCE1

*phospholipase C epsilon 1* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.18× (z +16.3, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.681× (z -5.7, q 6e-06, down in 20 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.724× (z -4.8, q 3e-04, down in 18 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALCAM]] (+0.64, fdr 7e-06), [[SYNE2]] (+0.60, fdr 1e-05), [[SLCO3A1]] (+0.59, fdr 1e-05); moves opposite to [[KRBOX4]] (-0.54, fdr 1e-05), [[ZNF778]] (-0.54, fdr 2e-04), [[C19orf25]] (-0.52, fdr 3e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANGPT1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ELAVL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +16.3 | 0e+00 | 29/32 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +14.4 | 3e-44 | 18/32 (hTERT-HPNE, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.26×** | +12.1 | 3e-31 | 26/31 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.81×** | +8.8 | 2e-16 | 11/28 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.83×** | +8.6 | 9e-16 | 14/24 (H4, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +8.5 | 3e-15 | 20/32 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.70×** | +7.7 | 1e-12 | 24/32 (NCI-H460, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 6e-12 | 25/32 (HCT15, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +7.0 | 2e-10 | 25/31 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.55×** | +6.9 | 2e-10 | 25/32 (HCT15, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.59×** | +6.9 | 3e-10 | 16/32 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 9e-09 | 25/31 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.53×** | +6.3 | 2e-08 | 14/32 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +6.2 | 2e-08 | 22/31 (AsPC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 4e-08 | 25/32 (HCT15, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +6.1 | 4e-08 | 22/32 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +6.0 | 5e-08 | 17/32 (HT-29, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +5.9 | 1e-07 | 24/32 (LS 180, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 4e-06 | 21/32 (LS 180, HCT15, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -5.7 | 6e-06 | 20/30 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.724×** | -4.8 | 3e-04 | 18/31 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -4.8 | 3e-04 | 16/31 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.744×** | -4.4 | 0.001 | 19/32 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.827×** | -4.0 | 0.006 | 9/32 (NCI-H460, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.006 | 17/32 (HT-29, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.770×** | -3.9 | 0.008 | 15/30 (H4, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.639×** | -3.5 | 0.035 | 11/30 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.059 | 16/31 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.858× | -3.2 | 0.066 | 15/32 (HT-29, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.073 | 6/32 (A-427, Hs 766T, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.818× | -3.0 | 0.13 | 7/31 (SW48, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 282 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0552× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.298× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 12.6 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.91× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 52.9 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.201× (z -11.8) |
| [[LoVo (line)]] | wt | 133 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -9.7) |
| [[A-172 (line)]] | wt | 11.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +10.5) | — |
| [[A-427 (line)]] | wt | 74.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.495× (z -8.9) |
| [[PANC-1 (line)]] | alt | 193 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.399× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.410× (z -8.8) |
| [[Hs 766T (line)]] | wt | 152 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -13.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.6) |
| [[HS-578T (line)]] | alt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +14.7) | — |
| [[KATO III (line)]] | alt | 90.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.266× (z -10.5) |
| [[SW 900 (line)]] | alt | 33.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.4) | — |
| [[A498 (line)]] | wt | 86.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.516× (z -8.8) ⚠ cell-cycle shift, explains ~8% of this change |
| [[LS 180 (line)]] | wt | 61.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.64× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 16.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.17× (z +8.5) | — |
| [[A549 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALCAM]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SYNE2]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SLCO3A1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[COBL]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | same gene group; pathway: Inositol phosphate metabolism; STRING 688 |
| [[PDLIM1]] | +0.58 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[NFIB]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SHROOM3]] | +0.56 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[CARMIL1]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TSPAN2]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EHF]] | +0.54 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[CRYBG1]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ZNF778]] | -0.54 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[C19orf25]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SWI5]] | -0.51 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[TUSC2]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GLE1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RABEP2]] | -0.48 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CCDC32]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[CAPN10-DT]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TAF12]] | -0.47 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[VRK3]] | -0.46 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SLC30A6]] | -0.46 | -0.45 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPT1]] | B | ANGPT1 activity raises PLCE1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without ANGPT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELAVL2]] | B | PLCE1 activity lowers ELAVL2's level | lines that do not express PLCE1 (16) vs lines expressing it (34) | 1.87× higher at baseline in the lines without PLCE1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |
| [[SYNM]] | B | PLCE1 activity raises SYNM's level | lines that do not express PLCE1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without PLCE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |
| cells under [[9-ING-41 (drug)]] 5 µM | B | PLCE1 activity raises the cells' numbers under 9-ING-41 5 µM (protects the cells) | lines that do not express PLCE1 (16) vs lines expressing it (32) | the lines without PLCE1: 0.89× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |
| [[ARHGAP17]] | B | PLCE1 activity raises ARHGAP17's level | lines that do not express PLCE1 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without PLCE1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 39.3); signed map (47.7, 17.0). **Vector** length 99.8, 26.3% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +14.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +6.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.0 | -3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.4 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C epsilon 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:93,993,931-94,332,823 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1516, PLCE, NPHS3 |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P212](https://www.uniprot.org/uniprotkb/Q9P212) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase epsilon-1):

> The production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) is mediated by activated phosphatidylinositol-specific phospholipase C enzymes. PLCE1 is a bifunctional enzyme which also regulates small GTPases of the Ras superfamily through its Ras guanine-exchange factor (RasGEF) activity. As an effector of heterotrimeric and small G protein, it may play a role in cell survival, cell growth, actin organization and T-cell activation. In podocytes, is …

**Summary**, from NCBI Gene [51196](https://www.ncbi.nlm.nih.gov/gene/51196):

> This gene encodes a phospholipase enzyme that catalyzes the hydrolysis of phosphatidylinositol-4,5-bisphosphate to generate two second messengers: inositol 1,4,5-triphosphate (IP3) and diacylglycerol (DAG). These second messengers subsequently regulate various processes affecting cell growth, differentiation, and gene expression. This enzyme is regulated by small monomeric GTPases of the Ras and Rho families and by heterotrimeric G proteins. In addition to its phospholipase C catalytic …

**Accessions** — [HGNC:17175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17175) · Entrez [51196](https://www.ncbi.nlm.nih.gov/gene/51196) · UniProt [Q9P212](https://www.uniprot.org/uniprotkb/Q9P212) · Ensembl [ENSG00000138193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138193)

## Data

Gene col 6143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6143); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6143]; `tensor/DDL_lfc|DDL_z.npy` [6143]; `embed/gene_vectors.npy` [6143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6143 or target_col == 6143). Every well: [[PLCE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
