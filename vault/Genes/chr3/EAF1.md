---
symbol: "EAF1"
type: "gene"
col: 6903
ensembl_id: "ENSG00000144597"
name: "ELL associated factor 1"
location: "3p25.1"
module: 7
arm: "+"
pooled_cpm: 30.57
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 2
n_dd_up_clean: 28
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EAF1

*ELL associated factor 1* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.66× (z +18.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.830× (z -5.3, q 8e-05, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAE1]] (+0.67, fdr 1e-05), [[SUPT7L]] (+0.65, fdr 3e-05), [[POLR2M]] (+0.64, fdr 1e-05); moves opposite to [[NUP98]] (-0.55, fdr 4e-05), [[H2AZ2]] (-0.55, fdr 3e-05), [[MAPK8]] (-0.54, fdr 9e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PGAP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.66×** | +18.1 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +16.4 | 0e+00 | 43/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +15.2 | 0e+00 | 41/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +14.3 | 6e-44 | 41/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +11.7 | 2e-29 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +11.0 | 6e-26 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +10.4 | 1e-23 | 39/48 (A549, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +10.2 | 1e-22 | 39/47 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.64×** | +10.1 | 3e-22 | 37/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +9.5 | 9e-20 | 38/48 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.0 | 2e-17 | 32/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +8.9 | 2e-17 | 40/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +7.8 | 3e-13 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.4 | 4e-12 | 31/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +6.9 | 2e-10 | 22/41 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 2e-09 | 27/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 3e-08 | 29/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -5.3 | 8e-05 | 22/48 (SW1417, C-33 A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.4 | 0.003 | 2/48 (NCI-H23, CHP-212) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.825×** | -3.8 | 0.023 | 16/48 (SW480, CHP-212, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.843× | -3.3 | 0.14 | 15/38 (AN3 CA, PANC-1, …) | top dose only | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.19 | 15/47 (HCT15, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.6 | 8 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.55× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 6.75× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 26.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 22.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +17.5) | — |
| [[A549 (line)]] | wt | 30.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.5) | — |
| [[A498 (line)]] | wt | 25.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.6) | — |
| [[A-172 (line)]] | wt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.3) | — |
| [[A-427 (line)]] | wt | 29.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 25.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +9.7) | — |
| [[C32 (line)]] | wt | 22.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.16× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.2) | — |
| [[J82 (line)]] | alt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.6) | — |
| [[LoVo (line)]] | wt | 28.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.69× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.53× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.9) | — |
| [[RKO (line)]] | wt | 47.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.39× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 45.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.70× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 61.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.57× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 28.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.96× (z +8.9) | — |
| [[SW48 (line)]] | wt | 35.1 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.98× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAE1]] | +0.67 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SUPT7L]] | +0.65 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[POLR2M]] | +0.64 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[DCTN5]] | +0.64 | +0.44 / +0.52 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[ZNF234]] | +0.64 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ZNF304]] | +0.64 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[OTUB1]] | +0.63 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZNF808]] | +0.63 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SMCR8]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TMEM199]] | +0.62 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[ZNF408]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SNIP1]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP98]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[H2AZ2]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MAPK8]] | -0.54 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[CENPI]] | -0.54 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CHD1]] | -0.54 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[SMC6]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[GPSM2]] | -0.53 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[CEP85]] | -0.52 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[SAPCD2]] | -0.51 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[KIAA1328]] | -0.51 | -0.33 / -0.32 | both halves | 1e-04 |  |
| [[LLGL2]] | -0.51 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[RBFA]] | -0.51 | -0.32 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity raises EAF1's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.23× lower at baseline in the lines without PGAP4 | 0.011 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[MAPK13]] | B | MAPK13 activity weakens EAF1's drug response | lines that do not express MAPK13 (15) vs lines expressing it (33) | the lines without MAPK13 respond 1.14× as strongly (z diff -0.68); strongest at Homoharringtonine 5 µM: 2.11x vs 1.66x (z diff -2.4) | 0.039 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.6, 13.4); signed map (-8.9, -22.8). **Vector** length 69.9, 14.0% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.3 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +14.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +18.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +10.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | -0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -3.1 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | -3.0 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -2.8 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ELL associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,427,598-15,450,635 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JC9](https://www.uniprot.org/uniprotkb/Q96JC9) (ELL-associated factor 1):

> Acts as a transcriptional transactivator of ELL and ELL2 elongation activities.

**Summary**, from NCBI Gene [85403](https://www.ncbi.nlm.nih.gov/gene/85403):

> Enables transcription elongation factor activity. Involved in regulation of transcription elongation by RNA polymerase II. Located in nuclear body. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20907) · Entrez [85403](https://www.ncbi.nlm.nih.gov/gene/85403) · UniProt [Q96JC9](https://www.uniprot.org/uniprotkb/Q96JC9) · Ensembl [ENSG00000144597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144597)

## Data

Gene col 6903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6903); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6903]; `tensor/DDL_lfc|DDL_z.npy` [6903]; `embed/gene_vectors.npy` [6903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6903 or target_col == 6903). Every well: [[EAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
