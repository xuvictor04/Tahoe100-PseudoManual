---
symbol: "DNAAF3"
type: "gene"
col: 9511
ensembl_id: "ENSG00000167646"
name: "dynein axonemal assembly factor 3"
location: "19q13.42"
module: 137
arm: "-"
pooled_cpm: 2.35
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# DNAAF3

*dynein axonemal assembly factor 3* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 12.1× (z +24.6, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.516× (z -6.5, q 6e-08, down in 16 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.611× (z -4.9, q 3e-04, down in 12 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.123×; ⚠ toxic).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNNI3]] (+0.74, fdr 7e-06, ⚠ same locus), [[RAB3A]] (+0.73, fdr 1e-05), [[SLC27A1]] (+0.72, fdr 4e-05), [[GNAI2]] (+0.71, fdr 7e-05); moves opposite to [[FAIM]] (-0.73, fdr 2e-05), [[GTF3C6]] (-0.72, fdr 3e-05), [[NIPAL2]] (-0.71, fdr 5e-05).
> It sits in the **-** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TNNI3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **12.1×** | +24.6 | 0e+00 | 40/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **8.86×** | +21.5 | 0e+00 | 37/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.84×** | +21.5 | 0e+00 | 39/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.57×** | +12.5 | 6e-34 | 39/41 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.83×** | +10.2 | 1e-22 | 20/25 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +9.2 | 5e-18 | 16/28 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.4 | 4e-15 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.87×** | +7.0 | 2e-10 | 16/33 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +6.0 | 1e-07 | 14/40 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 11/31 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.0 | 3e-05 | 1/12 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.9 | 4e-05 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.5 | 3e-04 | 13/30 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +3.8 | 0.007 | 1/13 (HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.032 | 1/14 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.89×** | +3.3 | 0.035 | 1/23 (PANC-1) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.038 | 4/37 (PANC-1, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.038 | 4/40 (A-172, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.057 | 7/36 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9511.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.123×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -6.5 | 6e-08 | 16/40 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -4.9 | 3e-04 | 12/40 (NCI-H1573, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.695×** | -3.6 | 0.061 | 7/36 (HS-578T, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.703×** | -3.5 | 0.073 | 6/34 (A549, SW 900, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.725× | -3.2 | 0.17 | 7/43 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.17 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.57× (z +11.5) | — |
| [[SW480 (line)]] | alt | 1.64 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 23.6× (z +10.2) | — |
| [[KATO III (line)]] | alt | 1.65 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 33.9× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 4.79 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.123× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.768 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.616 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.634 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.858 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNNI3]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 | STRING 432; ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[RAB3A]] | +0.73 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.72 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.71 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[CARD19]] | +0.71 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.70 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MPND]] | +0.70 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.69 | +0.48 / +0.32 | both halves | 2e-04 |  |
| [[FCHO1]] | +0.69 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[CASP9]] | +0.69 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.68 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[FOXO6]] | +0.68 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SUN1]] | +0.68 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | -0.73 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GTF3C6]] | -0.72 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[NIPAL2]] | -0.71 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[DNAJC11]] | -0.71 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.69 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ITPA]] | -0.69 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ALG8]] | -0.68 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[AP5M1]] | -0.68 | -0.49 / -0.26 | both halves | 3e-04 |  |
| [[KLHL42]] | -0.67 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[RCBTB2]] | -0.67 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[UTP20]] | -0.66 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.66 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNI3]] | B | TNNI3 activity raises DNAAF3's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without TNNI3 | 0.009 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FCHO1]] | B | FCHO1 activity raises DNAAF3's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without FCHO1 | 0.024 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[TNNT1]] | B | TNNT1 activity raises DNAAF3's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without TNNT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |
| [[SLC17A7]] | B | SLC17A7 activity raises DNAAF3's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without SLC17A7 | 0.068 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **-** arm (projection on the module's main direction -0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.9, -2.5); signed map (-29.2, 20.2). **Vector** length 53.2, 7.99% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +21.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +24.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +21.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +12.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +6.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.0 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,158,661-55,166,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40069, FLJ36139, pf22, PCD; previously C19orf51, CILD2 |
| Gene groups (HGNC) | Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9W5](https://www.uniprot.org/uniprotkb/Q8N9W5) (Dynein axonemal assembly factor 3):

> Required for the assembly of axonemal inner and outer dynein arms. Involved in preassembly of dyneins into complexes before their transport into cilia.

**Summary**, from NCBI Gene [352909](https://www.ncbi.nlm.nih.gov/gene/352909):

> The protein encoded by this gene is required for the assembly of axonemal inner and outer dynein arms and plays a role in assembling dynein complexes for transport into cilia. Defects in this gene are a cause of primary ciliary dyskinesia type 2 (CILD2). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:30492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30492) · Entrez [352909](https://www.ncbi.nlm.nih.gov/gene/352909) · UniProt [Q8N9W5](https://www.uniprot.org/uniprotkb/Q8N9W5) · Ensembl [ENSG00000167646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167646)

## Data

Gene col 9511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9511); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9511]; `tensor/DDL_lfc|DDL_z.npy` [9511]; `embed/gene_vectors.npy` [9511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9511 or target_col == 9511). Every well: [[DNAAF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
