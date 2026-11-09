---
symbol: "ATG16L1"
type: "gene"
col: 1446
ensembl_id: "ENSG00000085978"
name: "autophagy related 16 like 1"
location: "2q37.1"
module: 34
arm: "+"
pooled_cpm: 42.97
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ATG16L1

*autophagy related 16 like 1* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.83× (z +11.5, q 1e-27, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.543× (z -8.2, q 1e-13, down in 26 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.05 µM: 0.711× (z -4.4, q 0.002, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCR]] (+0.70, fdr 7e-06), [[LPCAT4]] (+0.66, fdr 2e-05), [[MALL]] (+0.66, fdr 7e-06); moves opposite to [[MTUS1-DT]] (-0.68, fdr 1e-05), [[ZC3H6]] (-0.66, fdr 1e-05), [[KANSL1L]] (-0.64, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCEL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.83×** | +11.5 | 1e-27 | 46/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.21×** | +11.0 | 1e-25 | 41/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.79×** | +9.7 | 6e-20 | 42/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.93×** | +9.1 | 9e-18 | 42/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.83×** | +8.4 | 4e-15 | 40/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +7.5 | 5e-12 | 33/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.1 | 1e-07 | 32/48 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 3e-07 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +5.6 | 2e-06 | 27/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.5 | 2e-06 | 29/48 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +5.5 | 2e-06 | 29/48 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 2e-05 | 28/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.0 | 3e-05 | 26/47 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.3 | 6e-04 | 23/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.001 | 21/47 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.002 | 24/47 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.007 | 22/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1446.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -8.2 | 1e-13 | 26/38 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.689×** | -5.2 | 5e-05 | 24/44 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.711×** | -4.4 | 0.002 | 23/47 (AsPC-1, SW48, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.741×** | -4.2 | 0.004 | 24/49 (AsPC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.020 | 20/47 (AsPC-1, LoVo, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.659×** | -3.5 | 0.043 | 21/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.677×** | -3.3 | 0.082 | 20/48 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.804× | -3.1 | 0.15 | 14/47 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.855× | -3.0 | 0.15 | 16/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.793× | -3.0 | 0.15 | 20/41 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 139 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.176× (z -10.0) |
| [[HT-29 (line)]] | alt | 24.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.53× (z +14.5) | — |
| [[LoVo (line)]] | wt | 105 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 5 µM 0.339× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 73.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.85× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 41.2 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.46× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 86.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.157× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.206× (z -9.1) |
| [[LS 180 (line)]] | wt | 76.8 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.24× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 71.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0398× (z -19.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.88× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -12.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.26× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 33.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.22× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0770× (z -15.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCR]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.66 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MALL]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 | same gene group |
| [[PLEK2]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.64 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[RNGTT]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 | same gene group |
| [[S100A16]] | +0.62 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[SERPINB5]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GJB3]] | +0.61 | +0.68 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTUS1-DT]] | -0.68 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.66 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[KANSL1L]] | -0.64 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[APLF]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.60 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[RSF1]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[STAP2]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.58 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[NFYB]] | -0.57 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[FILIP1L]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LITAF]] | -0.56 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCEL]] | B | SCEL activity raises ATG16L1's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.54× lower at baseline in the lines without SCEL | 0.034 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 7.2); signed map (-10.5, 42.4). **Vector** length 101, 26.7% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.8 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.6 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.5 | +11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.7 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -4.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 16 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,210,051-233,295,674 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WDR30, FLJ10035, ATG16A; previously APG16L, ATG16L |
| Gene groups (HGNC) | WD repeat domain containing; Autophagy related |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q676U5](https://www.uniprot.org/uniprotkb/Q676U5) (Autophagy-related protein 16-1):

> Plays an essential role in both canonical and non-canonical autophagy: interacts with ATG12-ATG5 to mediate the lipidation to ATG8 family proteins (MAP1LC3A, MAP1LC3B, MAP1LC3C, GABARAPL1, GABARAPL2 and GABARAP). Acts as a molecular hub, coordinating autophagy pathways via distinct domains that support either canonical or non-canonical signaling. During canonical autophagy, interacts with ATG12-ATG5 to mediate the conjugation of phosphatidylethanolamine (PE) to ATG8 proteins, to produce a …

**Summary**, from NCBI Gene [55054](https://www.ncbi.nlm.nih.gov/gene/55054):

> The protein encoded by this gene is part of a large protein complex that is necessary for autophagy, the major process by which intracellular components are targeted to lysosomes for degradation. Defects in this gene are a cause of susceptibility to inflammatory bowel disease type 10 (IBD10). Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:21498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21498) · Entrez [55054](https://www.ncbi.nlm.nih.gov/gene/55054) · UniProt [Q676U5](https://www.uniprot.org/uniprotkb/Q676U5) · Ensembl [ENSG00000085978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085978)

## Data

Gene col 1446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1446); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1446]; `tensor/DDL_lfc|DDL_z.npy` [1446]; `embed/gene_vectors.npy` [1446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1446 or target_col == 1446). Every well: [[ATG16L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG16L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
