---
symbol: "SHC3"
type: "gene"
col: 7240
ensembl_id: "ENSG00000148082"
name: "SHC adaptor protein 3"
location: "9q22.1"
module: 92
arm: "+"
pooled_cpm: 21.41
n_lines_expressing: 28
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 15
direction_downstream: 15
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SHC3

*SHC adaptor protein 3* — 9q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +10.4, q 2e-22, up in 5 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.541× (z -8.9, q 2e-16, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNIH3]] (+0.65, fdr 7e-06), [[LINC02454]] (+0.64, fdr 7e-06), [[ANTXR2]] (+0.63, fdr 7e-06); moves opposite to [[KRAS]] (-0.48, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[WNT5A]] → it (grade B ⚠); 15 go from it, the strongest it → [[EVA1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.4 | 2e-22 | 5/23 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +9.8 | 3e-20 | 8/25 (SW48, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +8.6 | 2e-15 | 11/25 (HOP62, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.4 | 2e-11 | 1/18 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.4 | 2e-11 | 8/26 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.6 | 2e-06 | 6/26 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.42×** | +5.1 | 3e-05 | 4/25 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.41×** | +5.0 | 5e-05 | 1/21 (Panc 03.27) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.9 | 5e-05 | 16/25 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.8 | 7e-05 | 5/25 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 1e-04 | 8/23 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.80×** | +4.5 | 4e-04 | 8/22 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +3.9 | 0.005 | 4/26 (MIA PaCa-2, HS-578T, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.007 | 7/26 (Hs 766T, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.008 | 4/25 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.027 | 5/24 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.074 | 8/26 (HOP62, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.541×** | -8.9 | 2e-16 | 20/25 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.537×** | -8.7 | 9e-16 | 20/25 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.604×** | -8.2 | 4e-14 | 20/26 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.646×** | -7.2 | 8e-11 | 16/26 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.608×** | -7.0 | 3e-10 | 16/25 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.677×** | -6.9 | 3e-10 | 19/26 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.625×** | -6.3 | 2e-08 | 13/25 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -6.0 | 1e-07 | 15/25 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.545×** | -4.6 | 2e-04 | 14/21 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.548×** | -4.6 | 3e-04 | 11/25 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.739×** | -4.5 | 3e-04 | 17/26 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.791×** | -4.4 | 5e-04 | 11/26 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose |  |
| [[BI-3406 (drug)]] 5 µM |  | **0.622×** | -3.6 | 0.013 | 11/25 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.631×** | -3.5 | 0.019 | 8/21 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.635×** | -3.5 | 0.021 | 12/22 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.024 | 10/26 (MIA PaCa-2, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 95.4 | 0 | 19 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.249× (z -36.3) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.0965× (z -22.9) |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -21.9) |
| [[SHP-77 (line)]] | alt | 40.3 | 0 | 12 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.174× (z -14.3) |
| [[SW480 (line)]] | alt | 44.3 | 0 | 11 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.183× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 89.5 | 0 | 8 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0883× (z -14.5) |
| [[SW 900 (line)]] | alt | 151 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 33.6 | 1 (1 ⚠) | 6 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.43× (z +9.3) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.243× (z -10.3) |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.5 µM 0.155× (z -9.5) |
| [[COLO 205 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.8× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 51.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -12.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.3) |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0794× (z -8.6) |
| [[SNU-423 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +8.5) | — |
| [[SW48 (line)]] | wt | 5.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +9.6) | — |
| [[A-172 (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNIH3]] | +0.65 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LINC02454]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NPAS2]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[LINC02813]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SGIP1]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[RPSAP52]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PRDM8]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NT5E]] | +0.60 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[HMGA2]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRAS]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 | pathway: MAPK family signaling cascades; STRING 560 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 11, C 4. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5A]] | B | WNT5A activity raises SHC3's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without WNT5A | 0.007 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises SHC3's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without EVA1A-AS | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[MANCR]] | B | MANCR activity raises SHC3's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.54× lower at baseline in the lines without MANCR | 0.029 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[EVA1A]] | B | EVA1A activity raises SHC3's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without EVA1A | 0.035 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises SHC3's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 2.13× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[ANGPTL2]] | B | ANGPTL2 activity raises SHC3's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without ANGPTL2 | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises SHC3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[RASA3]] | B | RASA3 activity raises SHC3's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without RASA3 | 0.070 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[CNIH3]] | B | CNIH3 activity raises SHC3's level | lines that do not express CNIH3 (12) vs lines expressing it (38) | 2.33× lower at baseline in the lines without CNIH3 | 0.080 | ⚠ within organs, on part of the lines; also absent: HDGFL3, RIMKLB, ZNF793; maybe low, not absent |
| [[PRDM8]] | B | PRDM8 activity raises SHC3's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without PRDM8 | 0.082 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[SAMD3]] | B | SAMD3 activity raises SHC3's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without SAMD3 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[RFX8]] | C | RFX8 activity raises SHC3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.50× lower at baseline in the lines without RFX8 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 10, C 5. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1A]] | B | SHC3 activity raises EVA1A's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without SHC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[RAC2]] | B | SHC3 activity raises RAC2's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without SHC3 | 0.041 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[EVA1A-AS]] | B | SHC3 activity raises EVA1A-AS's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without SHC3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[WNT5A]] | B | SHC3 activity raises WNT5A's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without SHC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[GPR68]] | B | SHC3 activity raises GPR68's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without SHC3 | 0.058 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[FIBCD1]] | B | SHC3 activity raises FIBCD1's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.46× lower at baseline in the lines without SHC3 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[C13orf46]] | B | SHC3 activity raises C13orf46's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without SHC3 | 0.086 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[FHAD1]] | B | SHC3 activity raises FHAD1's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without SHC3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[ARL4C]] | B | SHC3 activity raises ARL4C's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.42× lower at baseline in the lines without SHC3 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[ADAMTS12]] | B | SHC3 activity raises ADAMTS12's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without SHC3 | 0.095 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[SLC43A3]] | C | SHC3 activity raises SLC43A3's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.73× lower at baseline in the lines without SHC3 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent; co-absent with the target |
| [[RFX8]] | C | SHC3 activity raises RFX8's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 3.89× lower at baseline in the lines without SHC3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 8.8); signed map (11.4, 49.7). **Vector** length 79.5, 19.5% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +10.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +7.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | +4.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.7 | -8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.0 | -6.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -8.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.0 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | SHC adaptor protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.1 — chr9:89,005,771-89,178,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N-Shc, NSHC, SHCC |
| Gene groups (HGNC) | SH2 domain containing |
| Reactome | 11 pathways, smallest: Signalling to RAS; RET signaling; Signalling to ERKs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92529](https://www.uniprot.org/uniprotkb/Q92529) (SHC-transforming protein 3):

> Signaling adapter that couples activated growth factor receptors to signaling pathway in neurons. Involved in the signal transduction pathways of neurotrophin-activated Trk receptors in cortical neurons.

**Summary**, from NCBI Gene [53358](https://www.ncbi.nlm.nih.gov/gene/53358):

> Enables phosphotyrosine residue binding activity. Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to act upstream of or within glutamatergic synaptic transmission and learning or memory. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18181) · Entrez [53358](https://www.ncbi.nlm.nih.gov/gene/53358) · UniProt [Q92529](https://www.uniprot.org/uniprotkb/Q92529) · Ensembl [ENSG00000148082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148082)

## Data

Gene col 7240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7240); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7240]; `tensor/DDL_lfc|DDL_z.npy` [7240]; `embed/gene_vectors.npy` [7240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7240 or target_col == 7240). Every well: [[SHC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
