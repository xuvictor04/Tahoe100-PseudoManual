---
symbol: "TMEM69"
type: "gene"
col: 8264
ensembl_id: "ENSG00000159596"
name: "transmembrane protein 69"
location: "1p34.1"
module: 10
arm: "+"
pooled_cpm: 9.33
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMEM69

*transmembrane protein 69* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +12.0, q 1e-30, up in 32 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.111×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (BT-474 0.0990×); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.242×; ⚠ toxic; transcription drop); [[Oxaprozin (drug)]] 0.5 µM in 1 line (COLO 205 0.0916×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR73]] (+0.65, fdr 1e-05), [[TSPYL4]] (+0.65, fdr 1e-05), [[TIMM8B]] (+0.61, fdr 3e-05); moves opposite to [[NPHP4]] (-0.53, fdr 1e-04), [[RELL1]] (-0.53, fdr 4e-05), [[RAPGEFL1]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[THBS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +12.0 | 1e-30 | 32/44 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +8.9 | 2e-16 | 33/47 (SW480, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.8 | 3e-16 | 12/16 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +7.3 | 5e-11 | 15/24 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.1 | 1e-07 | 19/32 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.9 | 3e-07 | 23/46 (SW480, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +5.8 | 7e-07 | 20/45 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 1e-05 | 19/45 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +5.0 | 3e-05 | 15/43 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.0 | 3e-05 | 20/45 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +4.5 | 4e-04 | 16/39 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 7e-04 | 16/44 (HT-29, SW480, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +4.0 | 0.003 | 18/46 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.004 | 17/46 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.005 | 11/45 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 7/47 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.039 | 3/47 (LOX-IMVI, KATO III, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.055 | 11/42 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.055 | 8/43 (NCI-H23, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8264.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.111×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (BT-474 0.0990×); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.242×; ⚠ toxic; transcription drop); [[Oxaprozin (drug)]] 0.5 µM in 1 line (COLO 205 0.0916×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.810× | -3.0 | 0.67 | 8/46 (SW48, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.810× | -3.0 | 0.67 | 5/46 (SW480, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.27 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.4) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0990× (z -9.3) |
| [[COLO 205 (line)]] | alt | 9.73 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0916× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 9.32 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.111× (z -10.4) |
| [[HS-578T (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 9.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.0) | — |
| [[SW48 (line)]] | wt | 9.86 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0866× (z -8.5) |
| [[A-172 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR73]] | +0.65 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TSPYL4]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[TIMM8B]] | +0.61 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[MRPS14]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PRR3]] | +0.60 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[RAE1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[THBS4]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZSCAN30]] | +0.57 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[FAHD1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[C6orf120]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[PNISR-AS1]] | +0.56 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZBED5-AS1]] | +0.55 | +0.51 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.53 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[RELL1]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RAPGEFL1]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[CLTCL1]] | -0.49 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[EEF1D]] | -0.49 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CALM1]] | -0.48 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ASL]] | -0.48 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[RRBP1]] | -0.48 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[TRIM3]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZCCHC24]] | -0.48 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[OSBPL6]] | -0.47 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[PBX4]] | -0.47 | -0.44 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS4]] | B | THBS4 activity raises TMEM69's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.22× lower at baseline in the lines without THBS4 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.6, 17.1); signed map (-6.9, -29.7). **Vector** length 61.6, 9.38% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,688,181-45,694,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21029; previously C1orf154 |
| Matched by | ensembl_id |

UniProt [Q5SWH9](https://www.uniprot.org/uniprotkb/Q5SWH9) carries no function annotation.

**Summary**, from NCBI Gene [51249](https://www.ncbi.nlm.nih.gov/gene/51249):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28035) · Entrez [51249](https://www.ncbi.nlm.nih.gov/gene/51249) · UniProt [Q5SWH9](https://www.uniprot.org/uniprotkb/Q5SWH9) · Ensembl [ENSG00000159596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159596)

## Data

Gene col 8264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8264); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8264]; `tensor/DDL_lfc|DDL_z.npy` [8264]; `embed/gene_vectors.npy` [8264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8264 or target_col == 8264). Every well: [[TMEM69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
