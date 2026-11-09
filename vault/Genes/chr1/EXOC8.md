---
symbol: "EXOC8"
type: "gene"
col: 3854
ensembl_id: "ENSG00000116903"
name: "exocyst complex component 8"
location: "1q42.2"
module: 7
arm: "+"
pooled_cpm: 21.85
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EXOC8

*exocyst complex component 8* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +23.7, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (HCT15 0.132×; ⚠ toxic); [[Menadione (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0973×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP4]] (+0.74, fdr 7e-06), [[CBLL1]] (+0.68, fdr 7e-06), [[VCPIP1]] (+0.67, fdr 7e-06); moves opposite to [[USP3]] (-0.59, fdr 7e-06), [[PEBP1]] (-0.58, fdr 2e-05), [[PIGX]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF845]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +23.7 | 0e+00 | 45/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.96×** | +22.7 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +21.7 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +18.7 | 0e+00 | 46/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +16.0 | 0e+00 | 44/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +14.7 | 0e+00 | 43/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +13.8 | 2e-41 | 42/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +12.4 | 1e-33 | 30/44 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +12.0 | 1e-31 | 37/47 (SW480, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +11.5 | 1e-28 | 38/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +10.5 | 5e-24 | 37/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.4 | 1e-23 | 30/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +9.6 | 3e-20 | 32/48 (PANC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +9.1 | 5e-18 | 28/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +8.1 | 2e-14 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +7.0 | 8e-11 | 26/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3854.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.252×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Simotinib (drug)]] 5 µM in 1 line (HCT15 0.132×; ⚠ toxic); [[Menadione (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0973×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.4 | 0.008 | 2/48 (SNU-1, CHP-212) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.34 | 8/47 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.34 | 10/47 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.757× | -3.0 | 0.34 | 10/30 (HT-29, A-427, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.4 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +14.6) | — |
| [[SW480 (line)]] | alt | 20.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.55× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 20.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.8) | — |
| [[A-427 (line)]] | wt | 23.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.43× (z +9.9) | — |
| [[A549 (line)]] | wt | 24.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 27.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 25.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 15.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +9.9) | — |
| [[C32 (line)]] | wt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.132× (z -10.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0973× (z -9.1) |
| [[HOP62 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.4) | — |
| [[J82 (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.5) | — |
| [[KATO III (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[A-172 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP4]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.68 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[VCPIP1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | STRING 453 |
| [[ZNF426]] | +0.66 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[GCC1]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LENG1]] | +0.65 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[CREB3]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MED7]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[BRF2]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DNTTIP2]] | +0.64 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.64 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP3]] | -0.59 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[PEBP1]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PIGX]] | -0.57 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[STT3B]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PTMA]] | -0.55 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[KDM1A]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NDC1]] | -0.54 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[NAP1L1]] | -0.54 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[SUMF2]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[LRP5L]] | -0.54 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[SNRPA1]] | -0.53 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF845]] | B | ZNF845 activity raises EXOC8's level | lines that do not express ZNF845 (5) vs lines expressing it (45) | 1.14× lower at baseline in the lines without ZNF845 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF160, ZNF468, ZNF761 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.7, -0.4); signed map (-1.2, -25.7). **Vector** length 70.3, 12.9% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +16.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +14.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +12.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +5.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.1 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,332,753-231,337,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC84, EXO84, Exo84p |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Exocyst complex |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYI6](https://www.uniprot.org/uniprotkb/Q8IYI6) (Exocyst complex component 8):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane.

**Summary**, from NCBI Gene [149371](https://www.ncbi.nlm.nih.gov/gene/149371):

> This gene encodes a component of the exocyst complex, an evolutionarily conserved multi-protein complex that plays a critical role in vesicular trafficking and the secretory pathway by targeting post-Golgi vesicles to the plasma membrane. This protein is a target of activated Ral subfamily of GTPases and thereby regulates exocytosis by tethering vesicles to the plasma membrane. Mutations in this gene may be related to Joubert syndrome. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:24659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24659) · Entrez [149371](https://www.ncbi.nlm.nih.gov/gene/149371) · UniProt [Q8IYI6](https://www.uniprot.org/uniprotkb/Q8IYI6) · Ensembl [ENSG00000116903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116903)

## Data

Gene col 3854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3854); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3854]; `tensor/DDL_lfc|DDL_z.npy` [3854]; `embed/gene_vectors.npy` [3854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3854 or target_col == 3854). Every well: [[EXOC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
