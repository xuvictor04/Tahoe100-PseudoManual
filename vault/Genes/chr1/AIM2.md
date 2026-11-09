---
symbol: "AIM2"
type: "gene"
col: 8719
ensembl_id: "ENSG00000163568"
name: "absent in melanoma 2"
location: "1q23.1-q23.2"
module: 13
arm: "+"
pooled_cpm: 8.33
n_lines_expressing: 24
n_dd_up: 13
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 17
direction_downstream: 22
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# AIM2

*absent in melanoma 2* — 1q23.1-q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.19× (z +11.7, q 8e-29, up in 2 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +7.7, q 4e-12, up in 9 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.483× (z -7.6, q 2e-11, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETBP1]] (+0.69, fdr 7e-06), [[APCDD1L]] (+0.62, fdr 2e-05), [[APOBEC3G]] (+0.60, fdr 1e-05); moves opposite to [[LRP5]] (-0.47, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[BST2]] → it (grade B ⚠); 22 go from it, the strongest it → [[LINC01358]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +11.7 | 8e-29 | 2/11 (J82, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +7.7 | 4e-12 | 3/17 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +7.7 | 4e-12 | 9/22 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.3 | 3e-11 | 2/13 (J82, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.9 | 1e-04 | 0/22 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.5 | 7e-04 | 10/20 (C32, H4, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 1e-03 | 7/21 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.036 | 2/21 (SW 900, RPMI-7951) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.091 | 2/21 (HOP62, NCI-H1792) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.1 | 0.091 | 0/11 | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.091 | 1/21 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.091 | 3/20 (hTERT-HPNE, NCI-H23, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.75×** | +3.1 | 0.096 | 3/17 (NCI-H2347, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.10 | 1/22 (NCI-H2347) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -7.6 | 2e-11 | 17/21 (NCI-H1792, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -7.3 | 1e-10 | 21/22 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.709×** | -5.1 | 7e-05 | 11/22 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.625×** | -4.9 | 1e-04 | 14/22 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.640×** | -4.6 | 5e-04 | 13/22 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -4.3 | 0.002 | 18/21 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -4.2 | 0.002 | 10/21 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.667×** | -4.2 | 0.002 | 12/21 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -4.2 | 0.002 | 16/20 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -4.1 | 0.002 | 14/22 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.674×** | -4.1 | 0.002 | 11/21 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.758×** | -4.1 | 0.002 | 14/22 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.002 | 12/22 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.004 | 12/21 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.510×** | -3.7 | 0.009 | 8/19 (SK-MEL-2, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.010 | 8/22 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.699×** | -3.6 | 0.011 | 10/22 (SNU-423, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 49.3 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0450× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 41.1 | 0 | 12 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.161× (z -15.0) |
| [[C32 (line)]] | wt | 79.8 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0672× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 29.1 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 50.2 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0841× (z -13.6) |
| [[H4 (line)]] | wt | 32.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0477× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.108× (z -9.7) |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0540× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0397× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.0494× (z -9.4) |
| [[A-172 (line)]] | wt | 5.59 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0592× (z -9.6) |
| [[HS-578T (line)]] | alt | 5.93 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0903× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 3.65 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0486× (z -9.0) |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0984× (z -9.2) |
| [[A-427 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.739 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETBP1]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[APOBEC3G]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[KC6]] | +0.60 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CTHRC1]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[LINC01358]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[GBP5]] | +0.59 | +0.47 / +0.63 | both halves | 2e-05 | STRING 620 |
| [[NAV1]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.58 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[SAMD9]] | +0.58 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[DIRC3]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[OR9Q1]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP5]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BST2]] | B | BST2 activity raises AIM2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without BST2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[XAF1]] | B | XAF1 activity raises AIM2's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.48× lower at baseline in the lines without XAF1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[STING1]] | B | STING1 activity raises AIM2's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.75× lower at baseline in the lines without STING1 | 0.036 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[SAMD9L]] | B | SAMD9L activity raises AIM2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.49× lower at baseline in the lines without SAMD9L | 0.069 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[TIMP3]] | C | TIMP3 activity raises AIM2's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 5.06× lower at baseline in the lines without TIMP3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[NYAP2]] | C | NYAP2 activity raises AIM2's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 3.52× lower at baseline in the lines without NYAP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises AIM2's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 3.64× lower at baseline in the lines without NAV1 | 0.009 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[TNC]] | C | TNC activity raises AIM2's level | lines that do not express TNC (23) vs lines expressing it (27) | 3.28× lower at baseline in the lines without TNC | 0.013 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[SPOCD1]] | C | SPOCD1 activity raises AIM2's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 3.32× lower at baseline in the lines without SPOCD1 | 0.017 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; co-absent with the target |
| [[ADAMTS9-AS2]] | C | ADAMTS9-AS2 activity raises AIM2's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without ADAMTS9-AS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; co-absent with the target |
| [[MIR3681HG]] | C | MIR3681HG activity raises AIM2's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 3.17× lower at baseline in the lines without MIR3681HG | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent; co-absent with the target |
| [[ZNF521]] | C | ZNF521 activity raises AIM2's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 3.14× lower at baseline in the lines without ZNF521 | 0.048 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 6, C 16. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01358]] | B | AIM2 activity raises LINC01358's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without AIM2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[ABCA13]] | B | AIM2 activity raises ABCA13's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without AIM2 | 0.038 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[XAF1]] | B | AIM2 activity raises XAF1's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without AIM2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[ZPLD1]] | B | AIM2 activity raises ZPLD1's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without AIM2 | 0.058 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[ARHGEF28]] | B | AIM2 activity weakens ARHGEF28's drug response | lines that do not express AIM2 (22) vs lines expressing it (21) | the lines without AIM2 respond 1.52× as strongly (z diff -1.17); strongest at Dinaciclib 0.5 µM: 0.41x vs 0.81x (z diff -4.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; target measured in part of the lines; artifact flags |
| [[ARL10]] | B | AIM2 activity raises ARL10's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without AIM2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[SPOCD1]] | C | AIM2 activity raises SPOCD1's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 4.54× lower at baseline in the lines without AIM2 | 0.009 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |
| [[MIR3681HG]] | C | AIM2 activity raises MIR3681HG's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without AIM2 | 0.030 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |
| [[NAV1]] | C | AIM2 activity raises NAV1's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 4.83× lower at baseline in the lines without AIM2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |
| [[NYAP2]] | C | AIM2 activity raises NYAP2's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without AIM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |
| [[LOXL2]] | C | AIM2 activity raises LOXL2's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 4.84× lower at baseline in the lines without AIM2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |
| [[APCDD1L-DT]] | C | AIM2 activity raises APCDD1L-DT's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 4.11× lower at baseline in the lines without AIM2 | 0.056 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.2, 18.5); signed map (28.8, 44.1). **Vector** length 72.9, 20.0% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +0.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | absent in melanoma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1-q23.2 — chr1:159,061,599-159,187,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PYHIN4 |
| Gene groups (HGNC) | Pyrin domain containing; Pyrin and HIN domain family |
| Reactome | 4 pathways, smallest: Inflammasomes; Nucleotide-binding domain, leucine rich repeat containing receptor (NLR) signaling pathways; Cytosolic sensors of pathogen-associated DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O14862](https://www.uniprot.org/uniprotkb/O14862) (Interferon-inducible protein AIM2):

> Sensor component of the AIM2 inflammasome, which mediates inflammasome activation in response to the presence of double-stranded DNA (dsDNA) in the cytosol, leading to subsequent pyroptosis. Inflammasomes are supramolecular complexes that assemble in the cytosol in response to pathogens and other damage-associated signals and play critical roles in innate immunity and inflammation. Acts as a recognition receptor (PRR): specifically recognizes and binds dsDNA in the cytosol, and mediates the …

**Summary**, from NCBI Gene [9447](https://www.ncbi.nlm.nih.gov/gene/9447):

> AIM2 is a member of the IFI20X /IFI16 family. It plays a putative role in tumorigenic reversion and may control cell proliferation. Interferon-gamma induces expression of AIM2. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:357) · Entrez [9447](https://www.ncbi.nlm.nih.gov/gene/9447) · UniProt [O14862](https://www.uniprot.org/uniprotkb/O14862) · Ensembl [ENSG00000163568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163568)

## Data

Gene col 8719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8719); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8719]; `tensor/DDL_lfc|DDL_z.npy` [8719]; `embed/gene_vectors.npy` [8719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8719 or target_col == 8719). Every well: [[AIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
