---
symbol: "VASP"
type: "gene"
col: 4658
ensembl_id: "ENSG00000125753"
name: "vasodilator stimulated phosphoprotein"
location: "19q13.32"
module: 141
arm: "+"
pooled_cpm: 94.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# VASP

*vasodilator stimulated phosphoprotein* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.75× (z +8.7, q 3e-15, up in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.29× (z +4.0, q 0.011, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 2.96×, HS-578T 2.84×, A-427 2.40×, MIA PaCa-2 2.50×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A498 2.71×, J82 2.45×, HS-578T 2.34×, MIA PaCa-2 2.25×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 3.18×, HS-578T 1.84×, NCI-H1792 2.45×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SW480 2.28×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.632× (z -7.1, q 8e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.67, fdr 7e-06), [[EGR3]] (+0.66, fdr 7e-06), [[SOWAHC]] (+0.63, fdr 7e-06).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ACOT11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4658.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 2.96×, HS-578T 2.84×, A-427 2.40×, MIA PaCa-2 2.50×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A498 2.71×, J82 2.45×, HS-578T 2.34×, MIA PaCa-2 2.25×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 3.18×, HS-578T 1.84×, NCI-H1792 2.45×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SW480 2.28×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.7 | 3e-15 | 35/49 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.1 | 4e-07 | 32/42 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.011 | 29/48 (SW480, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.8 | 0.023 | 22/44 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.29 | 20/49 (J82, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.632×** | -7.1 | 8e-10 | 36/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.629×** | -6.9 | 2e-09 | 41/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.677×** | -6.4 | 3e-08 | 40/50 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.657×** | -6.2 | 6e-08 | 36/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.651×** | -6.1 | 1e-07 | 37/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.758×** | -6.0 | 2e-07 | 34/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.689×** | -5.7 | 8e-07 | 34/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.692×** | -5.7 | 9e-07 | 30/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.707×** | -5.3 | 6e-06 | 34/49 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.759×** | -5.0 | 3e-05 | 27/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.774×** | -5.0 | 3e-05 | 30/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -4.8 | 7e-05 | 29/48 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.740×** | -4.6 | 2e-04 | 30/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.789×** | -4.5 | 3e-04 | 28/48 (SW480, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.763×** | -4.2 | 0.001 | 29/48 (LoVo, LS 180, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.839× | -3.8 | 0.004 | 21/48 (LoVo, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 145 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 90.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -10.9) |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.365× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 94.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -10.5) |
| [[HS-578T (line)]] | alt | 92.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 93.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 147 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -12.1) |
| [[HT-29 (line)]] | alt | 179 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.381× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 82.6 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.202× (z -8.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 106 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.28× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 63.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 81.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 67.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 97.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 79.3 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.106× (z -8.8) |
| [[PANC-1 (line)]] | alt | 63.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -9.3) |
| [[A-172 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 86.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[EGR3]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SOWAHC]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SYNE3]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EGR2]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ARPC2]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 474 |
| [[CAPRIN2]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SPRED2]] | +0.61 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.61 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[EPHA2-AS1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LSR]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT11]] | B | ACOT11 activity raises VASP's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without ACOT11 | 0.026 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[LINC00659]] | B | LINC00659 activity raises VASP's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without LINC00659 | 0.031 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[BCL2L1]] | B | BCL2L1 activity raises VASP's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without BCL2L1 | 0.073 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises VASP's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, -1.3); signed map (5.1, 32.1). **Vector** length 131, 41.9% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.9 | +1.4 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -7.4 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.6 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.6 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.4 | -6.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.2 | -6.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -6.1 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | vasodilator stimulated phosphoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,506,579-45,526,989 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ENAH/VASPs |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 9 pathways, smallest: Generation of second messenger molecules; Cell-extracellular matrix interactions; TCR signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P50552](https://www.uniprot.org/uniprotkb/P50552) (Vasodilator-stimulated phosphoprotein):

> Ena/VASP proteins are actin-associated proteins involved in a range of processes dependent on cytoskeleton remodeling and cell polarity such as axon guidance, lamellipodial and filopodial dynamics, platelet activation and cell migration. VASP promotes actin filament elongation. It protects the barbed end of growing actin filaments against capping and increases the rate of actin polymerization in the presence of capping protein. VASP stimulates actin filament elongation by promoting the transfer …

**Summary**, from NCBI Gene [7408](https://www.ncbi.nlm.nih.gov/gene/7408):

> Vasodilator-stimulated phosphoprotein (VASP) is a member of the Ena-VASP protein family. Ena-VASP family members contain an EHV1 N-terminal domain that binds proteins containing E/DFPPPPXD/E motifs and targets Ena-VASP proteins to focal adhesions. In the mid-region of the protein, family members have a proline-rich domain that binds SH3 and WW domain-containing proteins. Their C-terminal EVH2 domain mediates tetramerization and binds both G and F actin. VASP is associated with filamentous actin …

**Accessions** — [HGNC:12652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12652) · Entrez [7408](https://www.ncbi.nlm.nih.gov/gene/7408) · UniProt [P50552](https://www.uniprot.org/uniprotkb/P50552) · Ensembl [ENSG00000125753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125753)

## Data

Gene col 4658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4658); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4658]; `tensor/DDL_lfc|DDL_z.npy` [4658]; `embed/gene_vectors.npy` [4658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4658 or target_col == 4658). Every well: [[VASP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VASP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
