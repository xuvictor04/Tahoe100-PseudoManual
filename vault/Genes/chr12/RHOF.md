---
symbol: "RHOF"
type: "gene"
col: 6340
ensembl_id: "ENSG00000139725"
name: "ras homolog family member F, filopodia associated"
location: "12q24.31"
module: 34
arm: "+"
pooled_cpm: 45.13
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# RHOF

*ras homolog family member F, filopodia associated* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +11.0, q 3e-25, up in 18 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +6.1, q 2e-07, up in 14 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.689× (z -9.5, q 2e-18, down in 22 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3B]] (+0.65, fdr 7e-06), [[PRSS3]] (+0.62, fdr 8e-06), [[LAMC2]] (+0.62, fdr 7e-06); moves opposite to [[TNS3]] (-0.47, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PRSS22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +11.0 | 3e-25 | 18/30 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.9 | 6e-13 | 20/35 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.1 | 2e-07 | 14/39 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.7 | 2e-06 | 16/32 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | **1.25×** | +5.5 | 4e-06 | 24/42 (RKO, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **1.31×** | +4.8 | 1e-04 | 13/37 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 1e-04 | 15/40 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 21/40 (SW480, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.7 | 1e-04 | 13/41 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.28×** | +4.4 | 6e-04 | 16/40 (RKO, PANC-1, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.005 | 13/40 (AsPC-1, SW1417, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.010 | 14/42 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.011 | 14/41 (SW1417, SW480, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +3.5 | 0.019 | 12/40 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.038 | 8/39 (HepG2/C3A, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.044 | 13/41 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.044 | 13/41 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.051 | 14/40 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -9.5 | 2e-18 | 22/40 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.715×** | -6.0 | 5e-07 | 20/40 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.756×** | -4.8 | 2e-04 | 19/39 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.774×** | -4.6 | 6e-04 | 16/41 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.5 | 1e-03 | 2/42 (NCI-H23, HOP62) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.852× | -4.1 | 0.004 | 22/41 (NCI-H23, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.853× | -4.0 | 0.005 | 13/41 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.810×** | -3.6 | 0.020 | 22/40 (HT-29, CHP-212, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.020 | 14/39 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.811×** | -3.6 | 0.020 | 14/40 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.855× | -3.5 | 0.021 | 14/41 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.029 | 14/41 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.073 | 13/42 (LoVo, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.080 | 12/40 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 83.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -20.3) |
| [[NCI-H23 (line)]] | alt | 67.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -21.7) |
| [[A498 (line)]] | wt | 27.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +15.3) | — |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -12.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 17.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.3× (z +15.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 12.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.1× (z +13.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 73.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 79.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 25.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 26.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.0× (z +15.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 39.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.2) |
| [[HCT15 (line)]] | alt | 55.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -14.4) |
| [[PANC-1 (line)]] | alt | 37.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | — |
| [[A-427 (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[C32 (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.311× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.7) |
| [[SW48 (line)]] | wt | 55.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.5) |
| [[A-172 (line)]] | wt | 9.82 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3B]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.62 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[LAMC2]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[PLEK2]] | +0.62 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[DENND2C]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.61 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[KLK11]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[FERMT1]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[FGD6]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ARHGAP27]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS3]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS22]] | B | PRSS22 activity raises RHOF's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without PRSS22 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[SULT2B1]] | B | SULT2B1 activity raises RHOF's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.19× lower at baseline in the lines without SULT2B1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises RHOF's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without EPHA2-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[TMPRSS4]] | B | TMPRSS4 activity raises RHOF's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without TMPRSS4 | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CRYBG2]] | B | CRYBG2 activity raises RHOF's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without CRYBG2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[MYO5B]] | B | MYO5B activity raises RHOF's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without MYO5B | 0.027 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[LEMD1]] | B | LEMD1 activity raises RHOF's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without LEMD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[GJB3]] | B | GJB3 activity raises RHOF's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without GJB3 | 0.032 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[TMC6]] | B | TMC6 activity raises RHOF's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.75× lower at baseline in the lines without TMC6 | 0.036 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[SPINT2]] | B | SPINT2 activity raises RHOF's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without SPINT2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[FGD6]] | B | FGD6 activity raises RHOF's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 2.54× lower at baseline in the lines without FGD6 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[CLDN4]] | B | CLDN4 activity raises RHOF's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without CLDN4 | 0.057 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, 54.9); signed map (-0.2, 39.6). **Vector** length 107, 27.7% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.4 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ras homolog family member F, filopodia associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,777,754-121,803,403 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20247, RIF; previously ARHF |
| Gene groups (HGNC) | Rho family GTPases |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 6 pathways, smallest: RHOF GTPase cycle; Neutrophil degranulation; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBH0](https://www.uniprot.org/uniprotkb/Q9HBH0) (Rho-related GTP-binding protein RhoF):

> Plasma membrane-associated small GTPase which cycles between an active GTP-bound and an inactive GDP-bound state. Causes the formation of thin, actin-rich surface projections called filopodia. Functions cooperatively with CDC42 and Rac to generate additional structures, increasing the diversity of actin-based morphology.

**Summary**, from NCBI Gene [54509](https://www.ncbi.nlm.nih.gov/gene/54509):

> Predicted to enable GTP binding activity; GTPase activity; and protein kinase binding activity. Involved in actin filament organization. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15703) · Entrez [54509](https://www.ncbi.nlm.nih.gov/gene/54509) · UniProt [Q9HBH0](https://www.uniprot.org/uniprotkb/Q9HBH0) · Ensembl [ENSG00000139725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139725)

## Data

Gene col 6340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6340); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6340]; `tensor/DDL_lfc|DDL_z.npy` [6340]; `embed/gene_vectors.npy` [6340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6340 or target_col == 6340). Every well: [[RHOF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
