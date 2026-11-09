---
symbol: "ZUP1"
type: "gene"
col: 7756
ensembl_id: "ENSG00000153975"
name: "zinc finger containing ubiquitin peptidase 1"
location: "6q22.1"
module: 15
arm: "+"
pooled_cpm: 27.36
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 13
n_dd_up_clean: 31
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZUP1

*zinc finger containing ubiquitin peptidase 1* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.37× (z +12.9, q 4e-35, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.619× (z -7.2, q 3e-10, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.727× (z -6.8, q 2e-09, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED8]] (+0.70, fdr 7e-06), [[TMEM68]] (+0.66, fdr 1e-05), [[PAAF1]] (+0.66, fdr 1e-04); moves opposite to [[JUNB]] (-0.58, fdr 2e-05), [[IER2]] (-0.57, fdr 3e-05), [[SFPQ]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PMEPA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.37×** | +12.9 | 4e-35 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +12.4 | 7e-33 | 39/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +12.0 | 7e-31 | 43/48 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +10.5 | 2e-23 | 43/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +10.0 | 2e-21 | 39/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.88×** | +9.4 | 5e-19 | 43/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +8.0 | 1e-13 | 34/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.8 | 3e-13 | 34/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.7 | 8e-13 | 31/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +7.6 | 2e-12 | 34/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +7.0 | 1e-10 | 32/48 (PANC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +6.8 | 5e-10 | 33/48 (KATO III, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 5e-09 | 29/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +6.3 | 9e-09 | 30/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +6.2 | 2e-08 | 27/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 2e-08 | 28/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +5.8 | 2e-07 | 28/47 (C32, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -7.2 | 3e-10 | 31/44 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -6.9 | 1e-09 | 19/36 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.727×** | -6.8 | 2e-09 | 33/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.698×** | -5.0 | 8e-05 | 21/41 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.745×** | -4.4 | 0.001 | 23/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -4.2 | 0.003 | 17/48 (HT-29, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.759×** | -4.2 | 0.003 | 21/48 (SW 900, RPMI-7951, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.785×** | -3.7 | 0.018 | 10/48 (HOP62, C32, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.788×** | -3.6 | 0.021 | 15/48 (SW 1088, C32, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.026 | 14/48 (CHP-212, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.038 | 15/48 (A-172, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.044 | 7/48 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.053 | 17/48 (SHP-77, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.2 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.46× (z +15.7) | — |
| [[LoVo (line)]] | wt | 31.5 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +14.3) | — |
| [[SW480 (line)]] | alt | 54.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.70× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 33.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -12.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.4) | — |
| [[A549 (line)]] | wt | 18.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 23.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.31× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 21.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.7) | — |
| [[RKO (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.257× (z -8.7) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED8]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMEM68]] | +0.66 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.66 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[TIAL1]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC13]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[UROD]] | +0.59 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[C5orf34]] | +0.57 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[C8orf76]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.56 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[NMNAT1]] | +0.55 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[CNPY2]] | +0.55 | +0.21 / +0.47 | both halves | 7e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[IER2]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SFPQ]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[DHRS2]] | -0.49 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[EGR1]] | -0.49 | -0.45 / -0.39 | both halves | 5e-05 | same gene group |
| [[RPRD1A]] | -0.49 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[NR4A1]] | -0.49 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[CSRNP1]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MAPK8]] | -0.48 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[RALY]] | -0.48 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[CCN1]] | -0.47 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[RNF123]] | -0.47 | -0.38 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMEPA1]] | B | PMEPA1 activity lowers ZUP1's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.60× higher at baseline in the lines without PMEPA1 | 0.091 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.4, 19.7); signed map (-30.2, -20.1). **Vector** length 71.6, 15.6% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.1 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -2.7 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +5.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger containing ubiquitin peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,635,618-116,668,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ412I7.3; previously C6orf113, ZUFSP |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZUP1 deubiquitinase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AP4](https://www.uniprot.org/uniprotkb/Q96AP4) (Zinc finger-containing ubiquitin peptidase 1):

> Deubiquitinase with endodeubiquitinase activity that specifically interacts with and cleaves 'Lys-63'-linked long polyubiquitin chains. Shows only weak activity against 'Lys-11' and 'Lys-48'-linked chains. Plays an important role in genome stability pathways, functioning to prevent spontaneous DNA damage and also promote cellular survival in response to exogenous DNA damage. Modulates the ubiquitination status of replication protein A (RPA) complex proteins in response to replication stress.

**Summary**, from NCBI Gene [221302](https://www.ncbi.nlm.nih.gov/gene/221302):

> This gene encodes a protein containing zinc finger motifs and a cysteine peptidase domain. The encoded protein functions as a K63-specific de-ubiquitinating enzyme that specifically cleaves long K63-linked polyubiquitin chains in the middle of a chain (i.e. "endo cleavage) rather than by removing the terminal ubiquitin from a chain. This enzyme is thought to be involved in the regulation of DNA repair by cleaving K63-linked ubiquitin chains at repair foci. This protein is related to proteases …

**Accessions** — [HGNC:21224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21224) · Entrez [221302](https://www.ncbi.nlm.nih.gov/gene/221302) · UniProt [Q96AP4](https://www.uniprot.org/uniprotkb/Q96AP4) · Ensembl [ENSG00000153975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153975)

## Data

Gene col 7756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7756); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7756]; `tensor/DDL_lfc|DDL_z.npy` [7756]; `embed/gene_vectors.npy` [7756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7756 or target_col == 7756). Every well: [[ZUP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZUP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
