---
symbol: "GTPBP10"
type: "gene"
col: 2667
ensembl_id: "ENSG00000105793"
name: "GTP binding protein 10"
location: "7q21.13"
module: 119
arm: "+"
pooled_cpm: 41.09
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# GTPBP10

*GTP binding protein 10* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +12.2, q 2e-31, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.486× (z -11.1, q 1e-25, down in 30 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SK-MEL-2 0.0911×, HEC-1-A 0.125×, SW1417 0.293×, AsPC-1 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW1417 0.0931×, Panc 03.27 0.126×, AsPC-1 0.226×, HEC-1-A 0.277×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (LS 180 0.134×, NCI-H2030 0.0912×, RKO 0.202×, HS-578T 0.162×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR53]] (+0.75, fdr 7e-06), [[ZSCAN25]] (+0.64, fdr 7e-06), [[ALKBH3]] (+0.63, fdr 1e-05); moves opposite to [[SLC9A3R1]] (-0.50, fdr 1e-04), [[FAM222A]] (-0.49, fdr 2e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAFIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +12.2 | 2e-31 | 39/48 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +8.5 | 8e-15 | 40/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.61×** | +8.0 | 3e-13 | 38/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.4 | 1e-05 | 28/48 (SK-MEL-2, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 8e-05 | 29/47 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.009 | 24/48 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.28×** | +3.8 | 0.012 | 22/47 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +3.3 | 0.064 | 13/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.072 | 19/48 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 1.21× | +3.0 | 0.14 | 18/48 (hTERT-HPNE, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.21× | +3.0 | 0.14 | 17/48 (HOP62, A498, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2667.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SK-MEL-2 0.0911×, HEC-1-A 0.125×, SW1417 0.293×, AsPC-1 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW1417 0.0931×, Panc 03.27 0.126×, AsPC-1 0.226×, HEC-1-A 0.277×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (LS 180 0.134×, NCI-H2030 0.0912×, RKO 0.202×, HS-578T 0.162×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.486×** | -11.1 | 1e-25 | 30/39 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.572×** | -8.2 | 5e-14 | 32/43 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.598×** | -8.2 | 5e-14 | 38/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.760×** | -4.2 | 0.004 | 24/47 (A498, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -3.2 | 0.14 | 12/48 (HEC-1-A, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 50.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.6) | [[Harringtonine (drug)]] 5 µM 0.398× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 59.8 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.0931× (z -24.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 63.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 32.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 68.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.41× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0911× (z -21.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 48.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.05× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -12.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -11.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 49.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.402× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -17.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0912× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0871× (z -8.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -15.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 50.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.5) | — |
| [[A-172 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR53]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ZSCAN25]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TRMT61B]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 | STRING 473 |
| [[TRMT12]] | +0.62 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[MIEF1]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MTG2]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 | STRING 560 |
| [[ZNF7]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A3R1]] | -0.50 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[FAM222A]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFIP]] | B | MAFIP activity raises GTPBP10's level | lines that do not express MAFIP (7) vs lines expressing it (43) | 1.21× lower at baseline in the lines without MAFIP | 0.094 | ⚠ within organs, on part of the lines |
| [[ZNF302]] | C | ZNF302 activity raises GTPBP10's level | lines that do not express ZNF302 (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without ZNF302 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.6, 6.9); signed map (-9.8, -16.6). **Vector** length 92.3, 21.4% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | +6.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.6 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -3.7 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +1.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.3 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Artemether (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:90,335,223-90,391,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP686A10121, FLJ38242, OBGH2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D1E9](https://www.uniprot.org/uniprotkb/A4D1E9) (GTP-binding protein 10):

> May be involved in the ribosome maturation process. Complements an ObgE(CgtA) function in E.coli ribosome maturation. Plays a role of GTPase in vitro. When missing, disorganization of the nucleolar architecture is observed.

**Summary**, from NCBI Gene [85865](https://www.ncbi.nlm.nih.gov/gene/85865):

> Small G proteins, such as GTPBP10, act as molecular switches that play crucial roles in the regulation of fundamental cellular processes such as protein synthesis, nuclear transport, membrane trafficking, and signal transduction (Hirano et al., 2006 [PubMed 17054726]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25106) · Entrez [85865](https://www.ncbi.nlm.nih.gov/gene/85865) · UniProt [A4D1E9](https://www.uniprot.org/uniprotkb/A4D1E9) · Ensembl [ENSG00000105793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105793)

## Data

Gene col 2667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2667); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2667]; `tensor/DDL_lfc|DDL_z.npy` [2667]; `embed/gene_vectors.npy` [2667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2667 or target_col == 2667). Every well: [[GTPBP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
