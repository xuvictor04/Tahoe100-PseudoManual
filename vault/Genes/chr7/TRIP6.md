---
symbol: "TRIP6"
type: "gene"
col: 1479
ensembl_id: "ENSG00000087077"
name: "thyroid hormone receptor interactor 6"
location: "7q22.1"
module: 68
arm: "+"
pooled_cpm: 12.81
n_lines_expressing: 38
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 20
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TRIP6

*thyroid hormone receptor interactor 6* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +13.5, q 6e-39, up in 33 of 35 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.43× (z +9.9, q 1e-20, up in 29 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.323× (z -13.1, q 1e-36, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDSL]] (+0.72, fdr 1e-05), [[TAPBPL]] (+0.69, fdr 1e-05), [[PATL2]] (+0.69, fdr 1e-05); moves opposite to [[SNRPD2]] (-0.67, fdr 8e-05), [[NME2]] (-0.63, fdr 6e-05), [[UQCRH]] (-0.61, fdr 9e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL7R]] → it (grade B ⚠); 20 go from it, the strongest it → [[NFYC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.28×** | +13.5 | 6e-39 | 33/35 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +9.9 | 1e-20 | 29/36 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.0 | 2e-13 | 30/35 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +7.2 | 6e-11 | 26/36 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.9 | 9e-05 | 21/36 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.3 | 0.001 | 14/31 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.040 | 7/33 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.062 | 11/33 (C32, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.062 | 4/35 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.31×** | +3.1 | 0.092 | 13/32 (Panc 03.27, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.1 | 0.092 | 1/36 (AN3 CA) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.094 | 8/34 (SW 900, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.323×** | -13.1 | 1e-36 | 35/36 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.335×** | -12.7 | 1e-34 | 34/36 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -12.4 | 6e-33 | 34/36 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.515×** | -7.7 | 2e-12 | 29/36 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.380×** | -5.4 | 7e-06 | 25/35 (HCT15, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.423×** | -4.8 | 1e-04 | 22/36 (NCI-H460, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -4.6 | 4e-04 | 19/36 (KATO III, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.683×** | -4.4 | 7e-04 | 17/34 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.687×** | -4.2 | 0.002 | 16/35 (SW 900, A498, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.002 | 15/36 (SW48, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.054 | 13/36 (CHP-212, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.764×** | -3.1 | 0.081 | 4/36 (HS-578T, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.6 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.92× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.346× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -18.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 13.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 5 µM 0.186× (z -11.1) |
| [[A-172 (line)]] | wt | 26.7 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +14.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.276× (z -8.8) |
| [[KATO III (line)]] | alt | 15.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -12.4) |
| [[C32 (line)]] | wt | 22.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.117× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 25.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -8.7) |
| [[A549 (line)]] | wt | 5.99 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0853× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 6.78 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.114× (z -8.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 6.43 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.132× (z -9.2) |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.271× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 57.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -8.5) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -10.8) |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDSL]] | +0.72 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PATL2]] | +0.69 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[REPIN1]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.69 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LACC1]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[C19orf54]] | +0.68 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[PBDC1]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[PLD6]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.66 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[ZFY]] | +0.66 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[TRIM47]] | +0.66 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD2]] | -0.67 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[NME2]] | -0.63 | -0.66 / -0.38 | both halves | 6e-05 |  |
| [[UQCRH]] | -0.61 | -0.65 / -0.36 | both halves | 9e-05 |  |
| [[HSP90B1]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 | same gene group |
| [[GNA12]] | -0.59 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[STRAP]] | -0.59 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[WASF3]] | -0.59 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.59 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[IER3IP1]] | -0.59 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.59 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[DCUN1D2]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SDHAP1]] | -0.59 | -0.61 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL7R]] | B | IL7R activity raises TRIP6's level | lines that do not express IL7R (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without IL7R | 0.013 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[ABCC9]] | B | ABCC9 activity raises TRIP6's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without ABCC9 | 0.062 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent |
| [[S100A3]] | B | S100A3 activity raises TRIP6's level | lines that do not express S100A3 (15) vs lines expressing it (35) | 2.72× lower at baseline in the lines without S100A3 | 0.089 | ⚠ within organs, on part of the lines; also absent: S100A4; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFYC]] | B | TRIP6 activity lowers NFYC's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.67× higher at baseline in the lines without TRIP6 | 0.002 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[TXNDC12]] | B | TRIP6 activity lowers TXNDC12's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.39× higher at baseline in the lines without TRIP6 | 0.005 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[CIC]] | B | TRIP6 activity raises CIC's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without TRIP6 | 0.012 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[IL7R]] | B | TRIP6 activity raises IL7R's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 2.97× lower at baseline in the lines without TRIP6 | 0.013 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[DECR2]] | B | TRIP6 activity lowers DECR2's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without TRIP6 | 0.040 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[SDR39U1]] | B | TRIP6 activity lowers SDR39U1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.38× higher at baseline in the lines without TRIP6 | 0.044 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[PIGF]] | B | TRIP6 activity lowers PIGF's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.48× higher at baseline in the lines without TRIP6 | 0.050 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[MR1]] | B | TRIP6 activity raises MR1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without TRIP6 | 0.063 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[PIGV]] | B | TRIP6 activity weakens PIGV's drug response | lines that do not express TRIP6 (12) vs lines expressing it (36) | the lines without TRIP6 respond 1.39× as strongly (z diff -1.06); strongest at Ouabain (Octahydrate) 0.5 µM: 0.29x vs 0.52x (z diff -3.3) | 0.065 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4; target measured in part of the lines; artifact flags |
| [[PIGV]] | B | TRIP6 activity lowers PIGV's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.40× higher at baseline in the lines without TRIP6 | 0.066 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[PEF1]] | B | TRIP6 activity lowers PEF1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.14× higher at baseline in the lines without TRIP6 | 0.068 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[FIZ1]] | B | TRIP6 activity lowers FIZ1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.18× higher at baseline in the lines without TRIP6 | 0.069 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.2, 9.9); signed map (19.1, -15.7). **Vector** length 77.5, 18.3% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +9.0 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | +4.9 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +0.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | -12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor interactor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,867,387-100,873,454 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZRP-1, OIP1, MGC10556, MGC10558, MGC29959, MGC3837, MGC4423 |
| Gene groups (HGNC) | Zyxin family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15654](https://www.uniprot.org/uniprotkb/Q15654) (Thyroid receptor-interacting protein 6):

> Relays signals from the cell surface to the nucleus to weaken adherens junction and promote actin cytoskeleton reorganization and cell invasiveness. Involved in lysophosphatidic acid-induced cell adhesion and migration. Acts as a transcriptional coactivator for NF-kappa-B and JUN, and mediates the transrepression of these transcription factors induced by glucocorticoid receptor.

**Summary**, from NCBI Gene [7205](https://www.ncbi.nlm.nih.gov/gene/7205):

> This gene is a member of the zyxin family and encodes a protein with three LIM zinc-binding domains. This protein localizes to focal adhesion sites and along actin stress fibers. Recruitment of this protein to the plasma membrane occurs in a lysophosphatidic acid (LPA)-dependent manner and it regulates LPA-induced cell migration. Alternatively spliced variants which encode different protein isoforms have been described; however, not all variants have been fully characterized. [provided by …

**Accessions** — [HGNC:12311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12311) · Entrez [7205](https://www.ncbi.nlm.nih.gov/gene/7205) · UniProt [Q15654](https://www.uniprot.org/uniprotkb/Q15654) · Ensembl [ENSG00000087077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087077)

## Data

Gene col 1479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1479); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1479]; `tensor/DDL_lfc|DDL_z.npy` [1479]; `embed/gene_vectors.npy` [1479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1479 or target_col == 1479). Every well: [[TRIP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
