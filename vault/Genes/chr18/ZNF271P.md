---
symbol: "ZNF271P"
type: "gene"
col: 15029
ensembl_id: "ENSG00000257267"
name: "zinc finger protein 271, pseudogene"
location: "18q12.2"
module: 114
arm: "+"
pooled_cpm: 27.54
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZNF271P

*zinc finger protein 271, pseudogene* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +15.6, q 0e+00, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.186×, RKO 0.235×, C-33 A 0.204×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.115×); [[Ranolazine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0579×); [[Tucatinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0605×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRK7]] (+0.72, fdr 7e-06), [[ZNF721]] (+0.69, fdr 7e-06), [[ZC3HC1]] (+0.67, fdr 1e-05); moves opposite to [[DDX12P]] (-0.67, fdr 1e-05), [[RBBP7]] (-0.64, fdr 1e-05), [[RAD54L]] (-0.59, fdr 2e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WBP2NL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +15.6 | 0e+00 | 41/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +14.1 | 6e-43 | 43/47 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +9.7 | 7e-20 | 35/47 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +8.6 | 2e-15 | 34/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.0 | 2e-13 | 28/45 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.8 | 6e-13 | 28/48 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +7.6 | 3e-12 | 31/48 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.8 | 7e-10 | 22/40 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.4 | 1e-08 | 24/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +5.8 | 3e-07 | 20/48 (NCI-H23, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +5.6 | 1e-06 | 20/43 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.5 | 2e-06 | 23/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +5.1 | 2e-05 | 20/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **1.24×** | +4.8 | 6e-05 | 21/47 (SHP-77, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.23×** | +4.6 | 1e-04 | 17/48 (RKO, C-33 A, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 7e-04 | 13/48 (SW 900, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 15/48 (A-172, LS 180, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.016 | 7/48 (RKO, LS 180, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.018 | 13/47 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.021 | 8/46 (MIA PaCa-2, A549, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.059 | 5/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.186×, RKO 0.235×, C-33 A 0.204×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.115×); [[Ranolazine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0579×); [[Tucatinib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0605×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.842× | -3.8 | 0.099 | 17/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.856× | -3.5 | 0.12 | 3/48 (MIA PaCa-2, HT-29, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.862× | -3.4 | 0.13 | 12/48 (NCI-H460, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 49.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.9) | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 2 | — | [[Ranolazine (drug)]] 0.5 µM 0.0579× (z -9.1) |
| [[RKO (line)]] | wt | 53.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -13.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -14.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.115× (z -9.7) |
| [[HCT15 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.5) | — |
| [[SW48 (line)]] | wt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.1) | — |
| [[SW480 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK7]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZC3HC1]] | +0.67 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.67 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[GPN2]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[ZNF35]] | +0.64 | +0.69 / +0.45 | both halves | 3e-05 | same gene group |
| [[CDKL3]] | +0.63 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[ZNF583]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 | same gene group |
| [[ALKBH1]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.62 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[TRIM4]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[DCTN6]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX12P]] | -0.67 | -0.74 / -0.55 | both halves | 1e-05 | same gene group |
| [[RBBP7]] | -0.64 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[RAD54L]] | -0.59 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[CDCA7]] | -0.58 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[DDX11]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[PCLAF]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[METAP1]] | -0.57 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[EZH2]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ARHGEF26]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[DSCC1]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[GLB1L2]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[IMPA2]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WBP2NL]] | B | WBP2NL activity lowers ZNF271P's level | lines that do not express WBP2NL (17) vs lines expressing it (33) | 1.35× higher at baseline in the lines without WBP2NL | 0.015 | ⚠ within organs, on part of the lines; also absent: ATP2A3, GCNT2, ENSG00000235726; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.4, 6.7); signed map (-3.3, -14.2). **Vector** length 83.6, 15.9% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +9.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.0 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 271, pseudogene |
| Locus type | pseudogene |
| Location | 18q12.2 — chr18:35,291,184-35,307,896 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | HZF7, ZNFEB; previously ZNF271 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [10778](https://www.ncbi.nlm.nih.gov/gene/10778):

> Zinc finger proteins interact with nucleic acids and have diverse functions. The zinc finger domain is a conserved amino acid sequence motif containing 2 specifically positioned cysteines and 2 histidines that are involved in coordinating zinc. Kruppel-related proteins form 1 family of zinc finger proteins. See ZFP93 (MIM 604749) for additional information on zinc finger proteins.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:13065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13065) · Entrez [10778](https://www.ncbi.nlm.nih.gov/gene/10778) · Ensembl [ENSG00000257267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257267)

## Data

Gene col 15029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15029); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15029]; `tensor/DDL_lfc|DDL_z.npy` [15029]; `embed/gene_vectors.npy` [15029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15029 or target_col == 15029). Every well: [[ZNF271P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF271P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
