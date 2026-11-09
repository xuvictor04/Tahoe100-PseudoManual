---
symbol: "NOMO1"
type: "gene"
col: 2378
ensembl_id: "ENSG00000103512"
name: "NODAL modulator 1"
location: "16p13.11"
module: 50
arm: "+"
pooled_cpm: 22.34
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# NOMO1

*NODAL modulator 1* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.65× (z +20.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Norepinephrine (hydrochloride) (drug)]] 5 µM: 0.809× (z -6.2, q 4e-07, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO3]] (+0.76, fdr 7e-06), [[SLC25A39]] (+0.73, fdr 7e-06), [[APMAP]] (+0.70, fdr 1e-05); moves opposite to [[PBDC1]] (-0.69, fdr 3e-05), [[N4BP2L1]] (-0.66, fdr 6e-05), [[BTN2A3P-1]] (-0.63, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LIX1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.65×** | +20.2 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +19.7 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +19.2 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.52×** | +19.2 | 0e+00 | 37/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.31×** | +16.7 | 0e+00 | 29/33 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.79×** | +11.1 | 7e-27 | 28/35 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +9.6 | 9e-20 | 33/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +9.3 | 1e-18 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +5.7 | 7e-07 | 19/47 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.28×** | +4.9 | 5e-05 | 20/47 (RKO, HOP62, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 10/48 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.25×** | +4.4 | 5e-04 | 18/45 (RKO, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.3 | 9e-04 | 14/48 (NCI-H1573, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 7/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.008 | 10/28 (C32, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.012 | 7/47 (NCI-H2030, NCI-H661, …) | two highest doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.038 | 3/48 (SW1417, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.044 | 8/46 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -6.2 | 4e-07 | 24/48 (BT-474, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.825×** | -4.0 | 0.019 | 17/46 (A-172, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.024 | 12/47 (HT-29, KATO III, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.831×** | -3.7 | 0.024 | 15/47 (HOP62, C32, …) | top dose only | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.838× | -3.6 | 0.024 | 7/48 (NCI-H1792, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.6 | 0.024 | 10/48 (RKO, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.6 | 0.024 | 17/48 (A-172, C32, …) | inconsistent across doses | composition shift |
| [[Penfluridol (drug)]] 5 µM |  | 0.835× | -3.6 | 0.024 | 16/46 (C-33 A, NCI-H661, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.891× | -3.4 | 0.049 | 11/48 (Hs 766T, SNU-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.2 | 0.069 | 16/47 (A-172, NCI-H2030, …) | two highest doses | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.723×** | -3.1 | 0.088 | 5/47 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | 0.853× | -3.0 | 0.11 | 11/48 (AN3 CA, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.3 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.57× (z +10.5) | — |
| [[SW480 (line)]] | alt | 15.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +11.8) | — |
| [[A-172 (line)]] | wt | 35.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 17.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.32× (z +9.5) | — |
| [[LoVo (line)]] | wt | 18.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.26× (z +9.4) | — |
| [[A549 (line)]] | wt | 22.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 34.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 25.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +9.3) | — |
| [[KATO III (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 15.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.40× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 29.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.24× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO3]] | +0.76 | +0.62 / +0.64 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 637 |
| [[SLC25A39]] | +0.73 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[APMAP]] | +0.70 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.69 | +0.53 / +0.67 | both halves | 1e-05 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[CHID1]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[INTS1]] | +0.67 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.67 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[RAB5C]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.66 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[ATRN]] | +0.66 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.69 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[N4BP2L1]] | -0.66 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[BTN2A3P-1]] | -0.63 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[THAP2]] | -0.62 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[BTN2A3P]] | -0.62 | -0.58 / -0.49 | both halves | 2e-05 |  |
| [[CCDC122]] | -0.62 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[ATE1OSP]] | -0.62 | -0.56 / -0.25 | both halves | 4e-04 |  |
| [[KCNMB3]] | -0.62 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ZNF181]] | -0.61 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.61 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R12A-AS2]] | -0.61 | -0.53 / -0.24 | both halves | 4e-04 |  |
| [[CREB3L4]] | -0.61 | -0.56 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIX1L]] | B | LIX1L activity raises NOMO1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 1.34× lower at baseline in the lines without LIX1L | 0.068 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.3, -21.4); signed map (-45.9, -11.9). **Vector** length 75.3, 13.8% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.2 | +19.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +19.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.4 | +19.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.4 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.1 | -0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NODAL modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:14,833,721-14,896,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PM5 |
| Gene groups (HGNC) | BOS complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15155](https://www.uniprot.org/uniprotkb/Q15155) (BOS complex subunit NOMO1):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions.

**Summary**, from NCBI Gene [23420](https://www.ncbi.nlm.nih.gov/gene/23420):

> This gene encodes a protein originally thought to be related to the collagenase gene family. This gene is one of three highly similar genes in a region of duplication located on the p arm of chromosome 16. These three genes encode closely related proteins that may have the same function. The protein encoded by one of these genes has been identified as part of a protein complex that participates in the Nodal signaling pathway during vertebrate development. Mutations in ABCC6, which is located …

**Accessions** — [HGNC:30060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30060) · Entrez [23420](https://www.ncbi.nlm.nih.gov/gene/23420) · UniProt [Q15155](https://www.uniprot.org/uniprotkb/Q15155) · Ensembl [ENSG00000103512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103512)

## Data

Gene col 2378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2378); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2378]; `tensor/DDL_lfc|DDL_z.npy` [2378]; `embed/gene_vectors.npy` [2378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2378 or target_col == 2378). Every well: [[NOMO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOMO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
