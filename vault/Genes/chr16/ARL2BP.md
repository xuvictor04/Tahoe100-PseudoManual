---
symbol: "ARL2BP"
type: "gene"
col: 2292
ensembl_id: "ENSG00000102931"
name: "ARF like GTPase 2 binding protein"
location: "16q13"
module: 41
arm: "+"
pooled_cpm: 29.67
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ARL2BP

*ARF like GTPase 2 binding protein* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.18× (z +15.0, q 0e+00, up in 28 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +8.9, q 7e-17, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.719× (z -6.6, q 2e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB41]] (+0.63, fdr 7e-06), [[FAM220A]] (+0.59, fdr 1e-05), [[CGGBP1]] (+0.59, fdr 1e-05); moves opposite to [[CMTM8]] (-0.49, fdr 1e-04), [[HSPE1]] (-0.48, fdr 3e-05), [[LINC00106]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +15.0 | 0e+00 | 28/33 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +12.0 | 1e-30 | 34/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +10.4 | 7e-23 | 31/47 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.9 | 7e-17 | 33/48 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.7 | 2e-12 | 29/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +6.5 | 6e-09 | 26/47 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +5.2 | 2e-05 | 16/38 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.1 | 3e-05 | 20/46 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.5 | 5e-04 | 18/48 (RKO, J82, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.24×** | +4.2 | 0.001 | 18/48 (A498, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.018 | 8/48 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.19× | +3.4 | 0.029 | 8/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.039 | 11/48 (SHP-77, COLO 205, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 1.18× | +3.3 | 0.039 | 15/47 (SW1417, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.074 | 9/46 (A549, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.719×** | -6.6 | 2e-08 | 24/48 (SW 1271, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -5.9 | 1e-06 | 26/48 (A498, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -5.7 | 3e-06 | 23/47 (SNU-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.787×** | -4.8 | 2e-04 | 22/48 (SW 1088, SNU-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.794×** | -4.6 | 4e-04 | 22/48 (SNU-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.813×** | -3.9 | 0.008 | 19/48 (J82, HS-578T, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.012 | 16/48 (HS-578T, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.6 | 0.021 | 21/48 (SNU-1, HOP62, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.782×** | -3.5 | 0.027 | 12/48 (A498, J82, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.2 | 0.086 | 17/48 (SNU-1, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -3.1 | 0.10 | 17/48 (A498, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.861× | -3.0 | 0.12 | 13/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 110 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.226× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 73.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 39.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +13.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB41]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[FAM220A]] | +0.59 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[UBE2J1]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A46]] | +0.56 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[FBXO8]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[STYX]] | +0.55 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RAB33B]] | +0.54 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[ARCN1]] | +0.54 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LYSMD3]] | +0.54 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[ARV1]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[MAGED2]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM8]] | -0.49 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[HSPE1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[LINC00106]] | -0.46 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PRKD2]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[TUFM]] | -0.46 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[FBXL19]] | -0.46 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PRIM2]] | -0.45 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[PTK2]] | -0.45 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[UQCRH]] | -0.44 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[LMTK2]] | -0.44 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[EIF3CL]] | -0.44 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[CELF1]] | -0.44 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ARL2BP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CFL2]] | C | CFL2 activity raises ARL2BP's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.16× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.2, -15.9); signed map (-18.6, -13.7). **Vector** length 93.8, 19.5% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.0 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.7 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.6 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +4.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +1.1 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.7 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.2 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 2 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:57,245,259-57,253,635 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BART1, BART; previously RP66 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Transport of vitamins, nucleosides, and related molecules; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Y0](https://www.uniprot.org/uniprotkb/Q9Y2Y0) (ADP-ribosylation factor-like protein 2-binding protein):

> Together with ARL2, plays a role in the nuclear translocation, retention and transcriptional activity of STAT3. May play a role as an effector of ARL2.

**Summary**, from NCBI Gene [23568](https://www.ncbi.nlm.nih.gov/gene/23568):

> ADP-ribosylation factor (ARF)-like proteins (ARLs) comprise a functionally distinct group of the ARF family of RAS-related GTPases. The protein encoded by this gene binds to ARL2.GTP with high affinity but does not interact with ARL2.GDP, activated ARF, or RHO proteins. The lack of detectable membrane association of this protein or ARL2 upon activation of ARL2 is suggestive of actions distinct from those of the ARFs. This protein is considered to be the first ARL2-specific effector identified, …

**Accessions** — [HGNC:17146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17146) · Entrez [23568](https://www.ncbi.nlm.nih.gov/gene/23568) · UniProt [Q9Y2Y0](https://www.uniprot.org/uniprotkb/Q9Y2Y0) · Ensembl [ENSG00000102931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102931)

## Data

Gene col 2292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2292); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2292]; `tensor/DDL_lfc|DDL_z.npy` [2292]; `embed/gene_vectors.npy` [2292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2292 or target_col == 2292). Every well: [[ARL2BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL2BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
