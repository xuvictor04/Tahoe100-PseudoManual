---
symbol: "PDLIM7"
type: "gene"
col: 12304
ensembl_id: "ENSG00000196923"
name: "PDZ and LIM domain 7"
location: "5q35.3"
module: 189
arm: "+"
pooled_cpm: 47.06
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# PDLIM7

*PDZ and LIM domain 7* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +5.5, q 2e-05, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.355× (z -7.9, q 1e-12, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID3B]] (+0.72, fdr 7e-06), [[ZCCHC24]] (+0.70, fdr 7e-06), [[DLGAP4]] (+0.70, fdr 7e-06); moves opposite to [[PLCH1]] (-0.62, fdr 1e-05), [[RPRD2]] (-0.56, fdr 1e-05), [[RAVER2]] (-0.54, fdr 1e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL13A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-05 | 27/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.47×** | +5.4 | 2e-05 | 20/36 (A498, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +4.3 | 0.003 | 24/48 (LoVo, SW1417, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.31×** | +3.9 | 0.011 | 23/48 (A498, SNU-423, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +3.9 | 0.012 | 23/48 (LoVo, SW1417, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.016 | 21/47 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +3.6 | 0.021 | 21/47 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.5 | 0.032 | 21/47 (SW1417, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +3.4 | 0.040 | 22/48 (LS 180, LoVo, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.094 | 15/47 (HT-29, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -7.9 | 1e-12 | 42/49 (HOP62, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.794×** | -4.8 | 5e-04 | 24/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.560×** | -4.4 | 0.002 | 28/47 (HOP62, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.752×** | -4.0 | 0.008 | 21/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.766×** | -3.9 | 0.011 | 22/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.033 | 20/48 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.846× | -3.5 | 0.035 | 13/48 (PANC-1, A498, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.035 | 17/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.777×** | -3.4 | 0.035 | 23/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.035 | 21/49 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.049 | 16/48 (KATO III, SW1417, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.801×** | -3.2 | 0.054 | 17/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.094 | 16/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Vandetanib (drug)]] 5 µM |  | 0.813× | -3.0 | 0.10 | 11/48 (HOP62, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 91.5 | 1 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Binimetinib (drug)]] 0.5 µM 0.340× (z -11.9) |
| [[HOP62 (line)]] | alt | 91.7 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.230× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.336× (z -9.0) |
| [[A498 (line)]] | wt | 42.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[HS-578T (line)]] | alt | 98.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.437× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 85.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 20.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.642× (z -12.0) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 65.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.441× (z -12.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 56.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.516× (z -8.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.404× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.522× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0918× (z -15.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[SW 1088 (line)]] | alt | 68.4 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0562× (z -9.0) |
| [[SW 1271 (line)]] | alt | 71.6 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0747× (z -9.3) |
| [[A-172 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3B]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ZCCHC24]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DLGAP4]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[STX1A]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SMTN]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS; STRING 652 |
| [[SH3BGRL3]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TUBB6]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DRAP1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CD59]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[ESAM]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCH1]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[RPRD2]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RAVER2]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[MGAM2]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MTUS1]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SUPV3L1]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[HNF4G]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PLBD1]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | COL13A1 activity raises PDLIM7's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without COL13A1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[MMP14]] | B | MMP14 activity raises PDLIM7's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without MMP14 | 0.022 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[CD59]] | B | CD59 activity raises PDLIM7's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without CD59 | 0.027 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[PLAT]] | B | PLAT activity raises PDLIM7's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without PLAT | 0.032 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[MAP2K1]] | B | MAP2K1 activity raises PDLIM7's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[HRH1]] | B | HRH1 activity raises PDLIM7's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 1.53× lower at baseline in the lines without HRH1 | 0.061 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises PDLIM7's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without CLDN14-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[RNF144A]] | B | RNF144A activity raises PDLIM7's level | lines that do not express RNF144A (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without RNF144A | 0.073 | ⚠ within organs, on part of the lines; also absent: PTPRU |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 1.5); signed map (-1.2, 46.7). **Vector** length 132, 38.9% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +5.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.8 | +3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.2 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.0 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.4 | -4.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -7.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.0 | -3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.5 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PDZ and LIM domain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,483,394-177,497,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ENIGMA |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: RET signaling; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR12](https://www.uniprot.org/uniprotkb/Q9NR12) (PDZ and LIM domain protein 7):

> May function as a scaffold on which the coordinated assembly of proteins can occur. May play a role as an adapter that, via its PDZ domain, localizes LIM-binding proteins to actin filaments of both skeletal muscle and nonmuscle tissues. Involved in both of the two fundamental mechanisms of bone formation, direct bone formation (e.g. embryonic flat bones mandible and cranium), and endochondral bone formation (e.g. embryonic long bone development). Plays a role during fracture repair. Involved in …

**Summary**, from NCBI Gene [9260](https://www.ncbi.nlm.nih.gov/gene/9260):

> The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The gene product is involved in the assembly of an actin filament-associated complex essential for …

**Accessions** — [HGNC:22958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22958) · Entrez [9260](https://www.ncbi.nlm.nih.gov/gene/9260) · UniProt [Q9NR12](https://www.uniprot.org/uniprotkb/Q9NR12) · Ensembl [ENSG00000196923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196923)

## Data

Gene col 12304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12304); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12304]; `tensor/DDL_lfc|DDL_z.npy` [12304]; `embed/gene_vectors.npy` [12304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12304 or target_col == 12304). Every well: [[PDLIM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDLIM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
