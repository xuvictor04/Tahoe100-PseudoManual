---
symbol: "SGSM3"
type: "gene"
col: 1939
ensembl_id: "ENSG00000100359"
name: "small G protein signaling modulator 3"
location: "22q13.1"
module: 40
arm: "+"
pooled_cpm: 28.11
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SGSM3

*small G protein signaling modulator 3* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.31× (z +5.3, q 2e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.580× (z -10.4, q 1e-22, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.656× (z -8.4, q 7e-15, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHDDS]] (+0.74, fdr 7e-06), [[YIPF2]] (+0.70, fdr 7e-06), [[CUL7]] (+0.70, fdr 7e-06); moves opposite to [[TIGD2]] (-0.64, fdr 1e-05), [[TSC22D1]] (-0.63, fdr 1e-05), [[VEZF1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +5.3 | 2e-05 | 22/48 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +5.3 | 2e-05 | 24/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.3 | 2e-05 | 1/48 (A549) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +5.1 | 6e-05 | 20/48 (C32, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 7e-04 | 18/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.16× | +4.2 | 0.003 | 17/48 (SK-MEL-2, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.22×** | +3.7 | 0.017 | 15/48 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.16 | 9/48 (C32, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.580×** | -10.4 | 1e-22 | 41/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.703×** | -9.9 | 1e-20 | 28/47 (AsPC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.621×** | -9.5 | 5e-19 | 32/48 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -8.4 | 7e-15 | 31/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.694×** | -7.3 | 4e-11 | 32/48 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.700×** | -7.1 | 1e-10 | 21/47 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -7.0 | 2e-10 | 32/48 (CFPAC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -7.0 | 2e-10 | 30/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.706×** | -6.9 | 3e-10 | 27/46 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -5.7 | 7e-07 | 28/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.779×** | -4.8 | 1e-04 | 21/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.796×** | -4.4 | 6e-04 | 15/36 (SW1417, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.810×** | -4.0 | 0.002 | 22/47 (SHP-77, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.8 | 0.005 | 15/47 (H4, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.706×** | -3.6 | 0.011 | 18/47 (Hs 766T, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.015 | 21/48 (SNU-1, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.030 | 17/47 (SW 1271, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.750×** | -3.0 | 0.082 | 12/47 (RPMI-7951, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.863× | -2.9 | 0.095 | 9/48 (HCT15, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.7) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[KATO III (line)]] | alt | 32.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 20.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.323× (z -8.7) |
| [[A-427 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -8.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.381× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0473× (z -19.9) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -10.6) |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHDDS]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CUL7]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SEC13]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[DPH7]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[COG6]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[BET1L]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.68 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[ZCCHC17]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD2]] | -0.64 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[TSC22D1]] | -0.63 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.60 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.59 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZNF462]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.59 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ATF7IP]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LEPROT]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[NFKB1]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[KLF10]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SGSM3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SGSM3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.6, -32.1); signed map (-48.2, 8.4). **Vector** length 93.9, 19.5% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.6 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.4 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +2.4 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.8 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.4 | -7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Busulfan (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | small G protein signaling modulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:40,370,591-40,410,289 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DJ1042K10.2, RUSC3, RabGAP-5, RABGAP5; previously RUTBC3 |
| Gene groups (HGNC) | Small G protein signaling modulators; TBC1 domain family members; RUN domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HU1](https://www.uniprot.org/uniprotkb/Q96HU1) (Small G protein signaling modulator 3):

> GTPase-activating protein (GAP) specific for Rab5 small GTPase for which it accelerates the intrinsic GTP hydrolysis rate, thereby controlling trafficking through the early endocytic pathway. May play a cooperative role in NF2-mediated growth suppression of cells.

**Summary**, from NCBI Gene [27352](https://www.ncbi.nlm.nih.gov/gene/27352):

> Enables GTPase activator activity and small GTPase binding activity. Involved in several processes, including Rap protein signal transduction; positive regulation of GTPase activity; and regulation of Rab protein signal transduction. Located in Golgi apparatus and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25228) · Entrez [27352](https://www.ncbi.nlm.nih.gov/gene/27352) · UniProt [Q96HU1](https://www.uniprot.org/uniprotkb/Q96HU1) · Ensembl [ENSG00000100359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100359)

## Data

Gene col 1939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1939); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1939]; `tensor/DDL_lfc|DDL_z.npy` [1939]; `embed/gene_vectors.npy` [1939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1939 or target_col == 1939). Every well: [[SGSM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGSM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
