---
symbol: "NGRN"
type: "gene"
col: 11323
ensembl_id: "ENSG00000182768"
name: "neugrin, neurite outgrowth associated"
location: "15q26.1"
module: 81
arm: "+"
pooled_cpm: 45.4
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# NGRN

*neugrin, neurite outgrowth associated* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.07× (z +11.2, q 4e-26, up in 29 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.79× (z +8.6, q 2e-15, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.05 µM: 0.805× (z -4.8, q 9e-04, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFL1]] (+0.61, fdr 1e-05), [[ITGA2]] (+0.60, fdr 7e-06), [[ANTXR2]] (+0.60, fdr 1e-05); moves opposite to [[RHOBTB3]] (-0.55, fdr 1e-05), [[TNS3]] (-0.48, fdr 6e-05), [[STOM]] (-0.47, fdr 6e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.07×** | +11.2 | 4e-26 | 29/39 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.86×** | +9.6 | 2e-19 | 38/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +8.6 | 2e-15 | 43/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +6.3 | 3e-08 | 33/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.51×** | +6.1 | 1e-07 | 28/43 (Panc 03.27, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 1e-07 | 34/48 (HT-29, LoVo, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.8 | 5e-07 | 33/47 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +5.7 | 6e-07 | 30/47 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 7e-06 | 30/48 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.37×** | +5.1 | 2e-05 | 28/47 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 26/47 (HT-29, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.001 | 22/47 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.001 | 20/48 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.003 | 22/48 (SK-MEL-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.28×** | +3.8 | 0.006 | 24/48 (HEC-1-A, A-427, …) | two highest doses | composition shift |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.019 | 16/48 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.036 | 19/48 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.061 | 18/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.05 µM |  | **0.805×** | -4.8 | 9e-04 | 21/48 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.742×** | -4.6 | 9e-04 | 24/47 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.734×** | -4.5 | 9e-04 | 25/49 (NCI-H1792, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.814×** | -4.5 | 9e-04 | 29/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.619×** | -4.0 | 0.007 | 22/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.820×** | -3.9 | 0.008 | 20/48 (LoVo, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.836× | -3.6 | 0.025 | 18/48 (NCI-H1792, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.032 | 18/47 (LoVo, HS-578T, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.810×** | -3.2 | 0.099 | 18/48 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 110 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 55.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 39.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HS-578T (line)]] | alt | 62.6 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.328× (z -8.7) |
| [[KATO III (line)]] | alt | 37.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A549 (line)]] | wt | 65.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 93.6 | 0 | 1 | — | [[Binimetinib (drug)]] 0.05 µM 0.475× (z -8.7) |
| [[HOP62 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 61.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.06× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 78.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.647× (z -12.0) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.02× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFL1]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.60 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ANXA10]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MOCS2-DT]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[S100A16]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A51]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[IL1B]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RAC2]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MMP1]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOBTB3]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TNS3]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[STOM]] | -0.47 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[TMEM131L]] | -0.45 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[UBE2E1]] | -0.45 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[PRELID2]] | -0.45 | -0.37 / -0.48 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises NGRN's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without BCL2A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[MAP2K1]] | B | MAP2K1 activity raises NGRN's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SEMA7A]] | B | SEMA7A activity raises NGRN's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without SEMA7A | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises NGRN's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.8, -1.9); signed map (4.7, 46.3). **Vector** length 90.2, 22.0% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +6.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.5 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | -3.8 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.8 | -4.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.7 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | neugrin, neurite outgrowth associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,265,659-90,275,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DSC92 |
| Reactome | 5 pathways, smallest: rRNA modification in the mitochondrion; Mitochondrial mRNA modification; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPE2](https://www.uniprot.org/uniprotkb/Q9NPE2) (Neugrin):

> Plays an essential role in mitochondrial ribosome biogenesis. As a component of a functional protein-RNA module, consisting of RCC1L, NGRN, RPUSD3, RPUSD4, TRUB2, FASTKD2 and 16S mitochondrial ribosomal RNA (16S mt-rRNA), controls 16S mt-rRNA abundance and is required for intra-mitochondrial translation of core subunits of the oxidative phosphorylation system.

**Summary**, from NCBI Gene [51335](https://www.ncbi.nlm.nih.gov/gene/51335):

> Enables rRNA binding activity. Involved in mitochondrial ribosome assembly and positive regulation of mitochondrial translation. Located in mitochondrial matrix; mitochondrial membrane; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18077) · Entrez [51335](https://www.ncbi.nlm.nih.gov/gene/51335) · UniProt [Q9NPE2](https://www.uniprot.org/uniprotkb/Q9NPE2) · Ensembl [ENSG00000182768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182768)

## Data

Gene col 11323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11323); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11323]; `tensor/DDL_lfc|DDL_z.npy` [11323]; `embed/gene_vectors.npy` [11323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11323 or target_col == 11323). Every well: [[NGRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NGRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
