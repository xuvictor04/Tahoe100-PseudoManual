---
symbol: "USP9Y"
type: "gene"
col: 3544
ensembl_id: "ENSG00000114374"
name: "ubiquitin specific peptidase 9 Y-linked"
location: "Yq11.221"
module: 177
arm: "+"
pooled_cpm: 45.85
n_lines_expressing: 20
n_dd_up: 19
n_dd_down: 30
n_dd_up_clean: 14
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 8
direction_downstream: 8
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# USP9Y

*ubiquitin specific peptidase 9 Y-linked* — Yq11.221

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +15.3, q 0e+00, up in 0 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.69× (z +8.2, q 3e-14, up in 14 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.622× (z -7.8, q 3e-12, down in 17 of 18 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.633× (z -7.5, q 1e-11, down in 16 of 18 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTY]] (+0.69, fdr 7e-06), [[LINC01518]] (+0.54, fdr 5e-04), [[KCNE4]] (+0.51, fdr 8e-05); moves opposite to [[KBTBD2]] (-0.36, fdr 4e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KDM5D]] → it (grade C ⚠); 8 go from it, the strongest it → [[CPA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +15.3 | 0e+00 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +11.5 | 2e-28 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +8.2 | 3e-14 | 14/18 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +6.9 | 7e-10 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.2 | 6e-08 | 2/18 (HCT15, A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 1e-05 | 15/18 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 7e-05 | 0/18 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 7e-05 | 0/19 | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.9 | 7e-05 | 14/18 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 1e-04 | 0/18 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 5e-04 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 2/20 (NCI-H460, A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.003 | 2/19 (SK-MEL-2, LoVo) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.009 | 0/18 | two highest doses | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.009 | 0/18 | top dose only |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.013 | 0/18 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.045 | 1/18 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.054 | 0/18 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.059 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.622×** | -7.8 | 3e-12 | 17/18 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -7.5 | 1e-11 | 16/18 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.698×** | -5.5 | 8e-06 | 0/18 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.731×** | -5.2 | 4e-05 | 15/18 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.747×** | -4.8 | 2e-04 | 11/18 (HCT15, C32, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -4.7 | 2e-04 | 8/18 (LoVo, SW 1088, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.747×** | -4.5 | 5e-04 | 0/18 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.776×** | -4.2 | 0.002 | 9/18 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.771×** | -4.1 | 0.002 | 16/17 (HCT15, C32, …) | two highest doses |  |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.718×** | -3.9 | 0.006 | 0/18 | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -3.8 | 0.007 | 10/18 (SNU-1, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.788×** | -3.8 | 0.008 | 5/18 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucatinib (drug)]] 0.5 µM |  | **0.737×** | -3.6 | 0.015 | 0/18 | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.017 | 0/18 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.809×** | -3.5 | 0.019 | 1/17 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.021 | 0/18 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.023 | 1/18 (SW 1088) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.038 | 0/18 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.038 | 0/18 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 250 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -8.8) |
| [[A549 (line)]] | wt | 166 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.424× (z -9.0) |
| [[C32 (line)]] | wt | 179 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -16.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 273 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -16.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 228 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 175 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -14.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 284 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 319 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 55.3 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.378× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.440× (z -8.6) |
| [[LoVo (line)]] | wt | 76.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 241 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTY]] | +0.69 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; STRING 999 |
| [[LINC01518]] | +0.54 | +0.24 / +0.54 | both halves | 5e-04 |  |
| [[KCNE4]] | +0.51 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[FBXL7]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[TTTY14]] | +0.48 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[P4HA2]] | +0.48 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[NBAS]] | +0.47 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[FAM230C]] | +0.47 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[ABI3BP]] | +0.47 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[KDM5D]] | +0.46 | +0.22 / +0.56 | both halves | 6e-04 | same gene group; STRING 999 |
| [[RAB18]] | +0.45 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[KRBOX4]] | +0.45 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD2]] | -0.36 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM5D]] | C | KDM5D activity raises USP9Y's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 20.37× lower at baseline in the lines without KDM5D | 7e-06 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P; co-absent with the target |
| [[UTY]] | C | UTY activity raises USP9Y's level | lines that do not express UTY (31) vs lines expressing it (19) | 18.21× lower at baseline in the lines without UTY | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[TTTY14]] | C | TTTY14 activity raises USP9Y's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 11.86× lower at baseline in the lines without TTTY14 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises USP9Y's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 16.75× lower at baseline in the lines without NLGN4Y | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[LRCH2]] | C | LRCH2 activity raises USP9Y's level | lines that do not express LRCH2 (27) vs lines expressing it (23) | 5.04× lower at baseline in the lines without LRCH2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PDGFRA, ENSG00000263655, PCDH17; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises USP9Y's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.56× lower at baseline in the lines without ZEB2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises USP9Y's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 4.71× lower at baseline in the lines without KCNE4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises USP9Y's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without COL5A2 | 0.091 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPA6]] | B | USP9Y activity raises CPA6's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without USP9Y | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1 |
| [[KDM5D]] | C | USP9Y activity raises KDM5D's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 12.89× lower at baseline in the lines without USP9Y | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[UTY]] | C | [[PRKY]], USP9Y activity raises UTY's level | lines that do not express PRKY, USP9Y (30) vs lines expressing them (20) | 17.21× lower at baseline in the lines without PRKY, USP9Y | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target; co-absent genes |
| [[TTTY14]] | C | USP9Y activity raises TTTY14's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 6.18× lower at baseline in the lines without USP9Y | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[NLGN4Y]] | C | USP9Y activity raises NLGN4Y's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 7.17× lower at baseline in the lines without USP9Y | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[COL5A2]] | C | USP9Y activity raises COL5A2's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without USP9Y | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[CRYAB]] | C | USP9Y activity raises CRYAB's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 1.57× lower at baseline in the lines without USP9Y | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |
| [[ZEB2]] | C | USP9Y activity raises ZEB2's level | lines that do not express USP9Y (30) vs lines expressing it (20) | 3.92× lower at baseline in the lines without USP9Y | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.7, 28.4); signed map (35.6, 38.1). **Vector** length 56.7, 16.0% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[4EGI-1 (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 9 Y-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yq11.221 — chrY:12,537,650-12,860,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DFFRY, FAF-Y, AZFA |
| Gene groups (HGNC) | Ubiquitin specific peptidases; Minor histocompatibility antigens; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O00507](https://www.uniprot.org/uniprotkb/O00507) (Ubiquitin carboxyl-terminal hydrolase 9Y):

> Deubiquitinase that mediates deubiquitination of target proteins. May stabilize target proteins that are important for male germ cell development.

**Summary**, from NCBI Gene [8287](https://www.ncbi.nlm.nih.gov/gene/8287):

> This gene is a member of the peptidase C19 family. It encodes a protein that is similar to ubiquitin-specific proteases, which cleave the ubiquitin moiety from ubiquitin-fused precursors and ubiquitinylated proteins. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:12633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12633) · Entrez [8287](https://www.ncbi.nlm.nih.gov/gene/8287) · UniProt [O00507](https://www.uniprot.org/uniprotkb/O00507) · Ensembl [ENSG00000114374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114374)

## Data

Gene col 3544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3544); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3544]; `tensor/DDL_lfc|DDL_z.npy` [3544]; `embed/gene_vectors.npy` [3544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3544 or target_col == 3544). Every well: [[USP9Y — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP9Y.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
