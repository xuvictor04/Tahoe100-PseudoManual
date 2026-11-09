---
symbol: "ADGRL1"
type: "gene"
col: 1003
ensembl_id: "ENSG00000072071"
name: "adhesion G protein-coupled receptor L1"
location: "19p13.12"
module: 100
arm: "+"
pooled_cpm: 28.01
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 3
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ADGRL1

*adhesion G protein-coupled receptor L1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +18.6, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.674× (z -12.0, q 3e-30, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC66A2]] (+0.64, fdr 1e-05), [[SEMA6B]] (+0.63, fdr 8e-06), [[SSBP4]] (+0.61, fdr 1e-05); moves opposite to [[VPS39]] (-0.55, fdr 1e-05), [[CCDC90B]] (-0.54, fdr 2e-05), [[FCF1]] (-0.54, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 3 go from it, the strongest it → [[PODXL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +18.6 | 0e+00 | 37/42 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.24×** | +17.3 | 0e+00 | 38/42 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.21×** | +17.0 | 0e+00 | 39/41 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +15.7 | 0e+00 | 31/41 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +15.0 | 0e+00 | 39/41 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.99×** | +14.8 | 0e+00 | 28/42 (SW480, Panc 03.27, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.86×** | +13.4 | 9e-39 | 28/42 (Panc 03.27, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.72×** | +11.2 | 2e-27 | 33/42 (Panc 03.27, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.41×** | +7.3 | 1e-11 | 19/39 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.26×** | +7.1 | 1e-10 | 21/42 (SK-MEL-2, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.37×** | +6.6 | 3e-09 | 15/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +5.9 | 2e-07 | 22/42 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 2e-04 | 19/42 (J82, A549, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 12/40 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.21×** | +4.2 | 0.001 | 9/41 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.026 | 6/42 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.674×** | -12.0 | 3e-30 | 32/42 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -8.2 | 9e-14 | 27/42 (BT-474, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.704×** | -7.5 | 1e-11 | 23/42 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.724×** | -6.9 | 6e-10 | 21/42 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -5.2 | 2e-05 | 16/42 (NCI-H2030, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.764×** | -4.1 | 0.004 | 6/42 (A-172, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.855× | -3.4 | 0.061 | 7/41 (COLO 205, A-172, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.861× | -3.2 | 0.093 | 10/42 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.754×** | -3.2 | 0.099 | 10/41 (HCT15, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -3.1 | 0.099 | 3/42 (SW 1271, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.7 | 8 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.68× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 5 (1 ⚠) | 1 | [[Belinostat (drug)]] 0.5 µM 4.27× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.282× (z -12.2) |
| [[A-172 (line)]] | wt | 37.6 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.19× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 64.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -21.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -13.4) |
| [[SW48 (line)]] | wt | 73.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -11.7) |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 26.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.33× (z +11.0) | — |
| [[J82 (line)]] | alt | 13.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.09× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -9.2) |
| [[A-427 (line)]] | wt | 75.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0788× (z -8.6) |
| [[HOP62 (line)]] | alt | 7.65 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.313× (z -8.8) |
| [[HS-578T (line)]] | alt | 24.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.13× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 36.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.461× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.182× (z -8.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 15.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.59× (z +8.9) | — |
| [[A549 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A2]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SEMA6B]] | +0.63 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[SSBP4]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SAMD1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DDHD1]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SMARCD3]] | +0.58 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[ASIC1]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KCNQ2]] | +0.57 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[CADM4]] | +0.56 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[JAG2]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[EVL]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CCDC90B]] | -0.54 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[FCF1]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[FAM149B1]] | -0.53 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[DUS4L]] | -0.52 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[TSG101]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZNF431]] | -0.52 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LINC01134]] | -0.52 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[RIMOC1]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GPATCH2]] | -0.52 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[AIMP1]] | -0.50 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[METTL6]] | -0.49 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises ADGRL1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.18× lower at baseline in the lines without SEMA6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises ADGRL1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without ARHGAP44 | 0.007 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises ADGRL1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without SEPTIN3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[CMTM8]] | B | CMTM8 activity raises ADGRL1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without CMTM8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[TLE2]] | B | TLE2 activity raises ADGRL1's level | lines that do not express TLE2 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without TLE2 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SOBP]] | B | SOBP activity raises ADGRL1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without SOBP | 0.046 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[PODXL2]] | B | PODXL2 activity raises ADGRL1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without PODXL2 | 0.070 | ⚠ within organs, on part of the lines |
| [[ADCY1]] | B | ADCY1 activity raises ADGRL1's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without ADCY1 | 0.079 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR |
| [[AIF1L]] | B | AIF1L activity raises ADGRL1's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without AIF1L | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises ADGRL1's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without JAG2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[CTXN1]] | B | CTXN1 activity raises ADGRL1's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 2.93× lower at baseline in the lines without CTXN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | ADGRL1 activity raises PODXL2's level | lines that do not express ADGRL1 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without ADGRL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3BP5, DSCC1, NDC80; maybe low, not absent; its own permutation p |
| [[ADA]] | B | ADGRL1 activity raises ADA's level | lines that do not express ADGRL1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without ADGRL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3BP5, DSCC1, NDC80; maybe low, not absent; its own permutation p |
| [[AIF1L]] | B | ADGRL1 activity raises AIF1L's level | lines that do not express ADGRL1 (6) vs lines expressing it (44) | 2.14× lower at baseline in the lines without ADGRL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SH3BP5, DSCC1, NDC80; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.4, -2.2); signed map (-43.3, 25.3). **Vector** length 105, 25.0% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.6 | +17.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +18.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.8 | +17.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +15.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +5.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.5 | +4.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.1 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.3 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -6.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,147,743-14,206,187 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0821, CIRL1, LEC2; previously LPHN1 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily L; Olfactomedin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94910](https://www.uniprot.org/uniprotkb/O94910) (Adhesion G protein-coupled receptor L1):

> Calcium-independent receptor of high affinity for alpha-latrotoxin, an excitatory neurotoxin present in black widow spider venom which triggers massive exocytosis from neurons and neuroendocrine cells. Receptor for TENM2 that mediates heterophilic synaptic cell-cell contact and postsynaptic specialization. Receptor probably implicated in the regulation of exocytosis (By similarity).

**Summary**, from NCBI Gene [22859](https://www.ncbi.nlm.nih.gov/gene/22859):

> This gene encodes a member of the latrophilin subfamily of G-protein coupled receptors (GPCR). Latrophilins may function in both cell adhesion and signal transduction. In experiments with non-human species, endogenous proteolytic cleavage within a cysteine-rich GPS (G-protein-coupled-receptor proteolysis site) domain resulted in two subunits (a large extracellular N-terminal cell adhesion subunit and a subunit with substantial similarity to the secretin/calcitonin family of GPCRs) being …

**Accessions** — [HGNC:20973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20973) · Entrez [22859](https://www.ncbi.nlm.nih.gov/gene/22859) · UniProt [O94910](https://www.uniprot.org/uniprotkb/O94910) · Ensembl [ENSG00000072071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072071)

## Data

Gene col 1003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1003); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1003]; `tensor/DDL_lfc|DDL_z.npy` [1003]; `embed/gene_vectors.npy` [1003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1003 or target_col == 1003). Every well: [[ADGRL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
