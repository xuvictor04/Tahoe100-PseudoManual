---
symbol: "STXBP4"
type: "gene"
col: 9272
ensembl_id: "ENSG00000166263"
name: "syntaxin binding protein 4"
location: "17q22"
module: 4
arm: "+"
pooled_cpm: 57.01
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# STXBP4

*syntaxin binding protein 4* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +10.7, q 5e-24, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.73× (z +8.7, q 5e-16, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.747× (z -4.5, q 0.002, down in 25 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.846× (z -3.8, q 0.017, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLPB]] (+0.62, fdr 1e-05), [[TAS2R14]] (+0.61, fdr 1e-05), [[MTHFD2L]] (+0.53, fdr 1e-05); moves opposite to [[LNX2]] (-0.45, fdr 2e-04), [[DDI2]] (-0.44, fdr 1e-04), [[PARD6B]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF605]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.95×** | +10.7 | 5e-24 | 37/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.87×** | +10.0 | 6e-21 | 39/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +8.7 | 5e-16 | 33/47 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.64×** | +7.9 | 3e-13 | 32/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +6.7 | 2e-09 | 35/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.6 | 3e-06 | 28/47 (HT-29, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.41×** | +5.5 | 3e-06 | 33/47 (LoVo, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.3 | 7e-06 | 26/47 (SNU-423, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.3 | 7e-06 | 28/47 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.2 | 1e-05 | 24/47 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.35×** | +4.8 | 8e-05 | 28/47 (HOP62, COLO 205, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.35×** | +4.6 | 2e-04 | 28/47 (HT-29, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 2e-04 | 29/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 3e-04 | 23/47 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.003 | 25/47 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.038 | 14/46 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.057 | 20/47 (SW480, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -4.5 | 0.002 | 25/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.756×** | -4.5 | 0.002 | 27/47 (SW 1271, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.784×** | -3.9 | 0.015 | 26/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.8 | 0.017 | 24/48 (CHP-212, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.801×** | -3.6 | 0.030 | 17/47 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.6 | 0.030 | 26/46 (KATO III, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.6 | 0.030 | 18/47 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.812×** | -3.4 | 0.054 | 21/46 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.055 | 19/46 (RKO, H4, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.820× | -3.0 | 0.13 | 17/46 (SNU-423, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 46.2 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.1) | — |
| [[NCI-H460 (line)]] | wt | 91.6 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.349× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 44.2 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.37× (z +11.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0921× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 64.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[J82 (line)]] | alt | 32.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 34.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 37.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.0) | [[AZD2858 (drug)]] 0.5 µM 0.0988× (z -9.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 52.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +9.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[AN3 CA (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[HOP62 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +8.9) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.238× (z -8.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SK-MEL-2 (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW48 (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 69.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.7) | — |
| [[A-172 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPB]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TAS2R14]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MTHFD2L]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ERCC8]] | +0.52 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PSMD1]] | +0.52 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[IDE]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PHTF1]] | +0.50 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[TRRAP]] | +0.50 | +0.27 / +0.40 | both halves | 3e-04 |  |
| [[PRH1]] | +0.50 | +0.66 / +0.32 | both halves | 2e-04 |  |
| [[CWC27]] | +0.50 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[PRKACB]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[VWA8]] | +0.49 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | -0.45 | -0.37 / -0.32 | both halves | 2e-04 | same gene group |
| [[DDI2]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PARD6B]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 | same gene group |
| [[FRG1DP]] | -0.43 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[GRB7]] | -0.42 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CNPPD1]] | -0.41 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[FBXO31]] | -0.41 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[REPS2]] | -0.41 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[PHETA1]] | -0.41 | -0.21 / -0.34 | both halves | 6e-04 |  |
| [[CAPN10]] | -0.41 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[NATD1]] | -0.41 | -0.26 / -0.25 | both halves | 4e-04 |  |
| [[DGKQ]] | -0.41 | -0.25 / -0.37 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF605]] | B | ZNF605 activity raises STXBP4's level | lines that do not express ZNF605 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without ZNF605 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, CMTM3, TUBA1A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.384). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.6, 14.7); signed map (7.7, -43.3). **Vector** length 94.6, 24.2% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.4 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | +2.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | -4.9 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.6 | +10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:54,968,727-55,173,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Synip, MGC50337 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWJ1](https://www.uniprot.org/uniprotkb/Q6ZWJ1) (Syntaxin-binding protein 4):

> Plays a role in the translocation of transport vesicles from the cytoplasm to the plasma membrane. Inhibits the translocation of SLC2A4 from intracellular vesicles to the plasma membrane by STX4A binding and preventing the interaction between STX4A and VAMP2. Stimulation with insulin disrupts the interaction with STX4A, leading to increased levels of SLC2A4 at the plasma membrane. May also play a role in the regulation of insulin release by pancreatic beta cells after stimulation by glucose (By …

**Summary**, from NCBI Gene [252983](https://www.ncbi.nlm.nih.gov/gene/252983):

> Involved in several processes, including positive regulation of cell cycle G1/S phase transition; positive regulation of keratinocyte proliferation; and protein stabilization. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19694) · Entrez [252983](https://www.ncbi.nlm.nih.gov/gene/252983) · UniProt [Q6ZWJ1](https://www.uniprot.org/uniprotkb/Q6ZWJ1) · Ensembl [ENSG00000166263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166263)

## Data

Gene col 9272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9272); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9272]; `tensor/DDL_lfc|DDL_z.npy` [9272]; `embed/gene_vectors.npy` [9272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9272 or target_col == 9272). Every well: [[STXBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
