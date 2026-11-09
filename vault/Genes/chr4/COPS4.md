---
symbol: "COPS4"
type: "gene"
col: 6207
ensembl_id: "ENSG00000138663"
name: "COP9 signalosome subunit 4"
location: "4q21.22"
module: 45
arm: "+"
pooled_cpm: 39.63
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# COPS4

*COP9 signalosome subunit 4* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.32× (z +13.0, q 7e-36, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.668× (z -6.0, q 1e-06, down in 29 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.718× (z -4.9, q 2e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG9]] (+0.72, fdr 7e-06), [[PRMT9]] (+0.71, fdr 7e-06), [[HSF2]] (+0.69, fdr 7e-06); moves opposite to [[AGO2]] (-0.63, fdr 1e-05), [[TNFRSF12A]] (-0.62, fdr 7e-06), [[SSUH2]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Almonertinib (mesylate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.32×** | +13.0 | 7e-36 | 48/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.60×** | +10.0 | 6e-21 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +9.9 | 8e-21 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.8 | 1e-09 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.002 | 25/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.20×** | +3.8 | 0.013 | 23/48 (A-427, NCI-H460, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.021 | 20/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.021 | 21/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.025 | 17/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.032 | 19/48 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +3.2 | 0.060 | 18/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.2 | 0.070 | 16/34 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.23× | +3.0 | 0.10 | 18/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.668×** | -6.0 | 1e-06 | 29/46 (CHP-212, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -5.3 | 4e-05 | 25/41 (KATO III, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -4.9 | 2e-04 | 30/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.767×** | -3.9 | 0.011 | 21/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.086 | 17/48 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.086 | 14/48 (AsPC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.086 | 14/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.817× | -3.0 | 0.19 | 14/48 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 39.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.70× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 11.8× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.3 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 29.4 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +16.1) | — |
| [[SW480 (line)]] | alt | 39.2 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +13.9) | — |
| [[KATO III (line)]] | alt | 29.3 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0923× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 82.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Pioglitazone (drug)]] 0.5 µM 0.169× (z -9.4) |
| [[LoVo (line)]] | wt | 35.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.03× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 45.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 39.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.63× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +9.0) | — |
| [[C32 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0663× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 30.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.45× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +9.1) | — |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG9]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HSF2]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[USP30]] | +0.68 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[TFG]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MBIP]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[TERF1]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SNX1]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TMEM183A]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.66 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO2]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SSUH2]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[NABP1]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[TBILA]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.56 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[THOC6]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MSRA]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[NPIPB5]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Almonertinib (mesylate) (drug)]] 5 µM | C | COPS4's natural level lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | COPS4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.715). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-2.4, -10.6); signed map (-31.1, -10.1). **Vector** length 91.6, 22.8% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +13.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +10.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | -1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:83,034,447-83,075,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSN4, SGN4 |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 16 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; DNA Damage Recognition in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT78](https://www.uniprot.org/uniprotkb/Q9BT78) (COP9 signalosome complex subunit 4):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. Involved in the deneddylation of non-cullin subunits such as STON2. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, …

**Summary**, from NCBI Gene [51138](https://www.ncbi.nlm.nih.gov/gene/51138):

> This gene encodes one of eight subunits composing COP9 signalosome, a highly conserved protein complex that functions as an important regulator in multiple signaling pathways. The structure and function of COP9 signalosome is similar to that of the 19S regulatory particle of 26S proteasome. COP9 signalosome has been shown to interact with SCF-type E3 ubiquitin ligases and act as a positive regulator of E3 ubiquitin ligases. Two transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:16702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16702) · Entrez [51138](https://www.ncbi.nlm.nih.gov/gene/51138) · UniProt [Q9BT78](https://www.uniprot.org/uniprotkb/Q9BT78) · Ensembl [ENSG00000138663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138663)

## Data

Gene col 6207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6207); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6207]; `tensor/DDL_lfc|DDL_z.npy` [6207]; `embed/gene_vectors.npy` [6207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6207 or target_col == 6207). Every well: [[COPS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
