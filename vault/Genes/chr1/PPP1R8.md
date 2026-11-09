---
symbol: "PPP1R8"
type: "gene"
col: 3948
ensembl_id: "ENSG00000117751"
name: "protein phosphatase 1 regulatory subunit 8"
location: "1p35.3"
module: 107
arm: "+"
pooled_cpm: 29.58
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# PPP1R8

*protein phosphatase 1 regulatory subunit 8* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +14.6, q 1e-45, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.621× (z -10.1, q 3e-21, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.821× (z -5.9, q 8e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STBD1]] (+0.68, fdr 5e-05), [[DDX59]] (+0.68, fdr 1e-05), [[IREB2]] (+0.67, fdr 7e-06); moves opposite to [[LMTK3]] (-0.59, fdr 3e-05), [[SPAG9]] (-0.55, fdr 5e-05), [[OSBPL8]] (-0.55, fdr 3e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +14.6 | 1e-45 | 40/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +10.3 | 2e-22 | 37/48 (PANC-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +9.5 | 3e-19 | 29/45 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.5 | 4e-19 | 31/47 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +7.7 | 1e-12 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.7 | 2e-09 | 25/48 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +6.6 | 3e-09 | 24/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.7 | 7e-07 | 26/47 (HOP62, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.6 | 1e-06 | 24/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.2 | 1e-05 | 20/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +5.1 | 2e-05 | 22/46 (J82, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.1 | 2e-05 | 21/48 (PANC-1, LS 180, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +4.3 | 9e-04 | 17/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.19× | +3.7 | 0.008 | 9/47 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +3.5 | 0.020 | 11/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.046 | 5/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -10.1 | 3e-21 | 30/46 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -8.2 | 6e-14 | 24/38 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.9 | 8e-07 | 27/48 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.778×** | -5.3 | 1e-05 | 24/48 (SW1417, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.763×** | -5.3 | 1e-05 | 20/41 (C32, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -5.0 | 6e-05 | 24/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.795×** | -4.8 | 1e-04 | 21/48 (C-33 A, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.688×** | -4.1 | 0.003 | 13/48 (NCI-H23, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.7 | 0.014 | 10/48 (NCI-H2030, RKO, …) | inconsistent across doses |  |
| [[Flutamide (drug)]] 0.5 µM |  | 0.844× | -3.6 | 0.021 | 18/48 (NCI-H661, SK-MEL-2, …) | two highest doses |  |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.025 | 9/48 (AsPC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.857× | -3.2 | 0.056 | 13/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | 0.859× | -3.2 | 0.061 | 19/47 (C-33 A, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 64.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.324× (z -9.8) |
| [[C32 (line)]] | wt | 30.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0901× (z -16.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 36.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.08× (z +8.6) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.318× (z -8.5) |
| [[A-427 (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -15.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -13.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.8) | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -11.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0735× (z -20.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.334× (z -9.3) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0617× (z -9.4) |
| [[RKO (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -13.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STBD1]] | +0.68 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[DDX59]] | +0.68 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[IREB2]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MTG2]] | +0.67 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PALB2]] | +0.67 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ZNF419]] | +0.66 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LATS1]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CPT2]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[C8orf33]] | +0.64 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[ZNF773]] | +0.63 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TRAPPC13]] | +0.63 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.63 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK3]] | -0.59 | -0.50 / -0.45 | both halves | 3e-05 | same gene group |
| [[SPAG9]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[OSBPL8]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PLXND1]] | -0.54 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[DNM1]] | -0.54 | -0.37 / -0.59 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises PPP1R8's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without ZNF675 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[TOP2A]] | B | TOP2A activity lowers PPP1R8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PPP1R8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PPP1R8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF253]] | C | ZNF253 activity raises PPP1R8's level | lines that do not express ZNF253 (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without ZNF253 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF20, ZNF440, DEF6; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.2, 18.4); signed map (-7.0, -17.7). **Vector** length 99.8, 21.8% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.3 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.0 | -10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.1 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Elagolix sodium (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,830,782-27,851,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ard-1, NIPP-1, PRO2047, ARD1, NIPP1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Endoribonucleases; Small nucleolar RNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12972](https://www.uniprot.org/uniprotkb/Q12972) (Nuclear inhibitor of protein phosphatase 1):

> Inhibitor subunit of the major nuclear protein phosphatase-1 (PP-1). It has RNA-binding activity but does not cleave RNA and may target PP-1 to RNA-associated substrates. May also be involved in pre-mRNA splicing. Binds DNA and might act as a transcriptional repressor. Seems to be required for cell proliferation.; Isoform Gamma is a site-specific single-strand endoribonuclease that cleaves single strand RNA 3' to purines and pyrimidines in A+U-rich regions. It generates 5'-phosphate termini at …

**Summary**, from NCBI Gene [5511](https://www.ncbi.nlm.nih.gov/gene/5511):

> This gene, through alternative splicing, encodes three different isoforms. Two of the protein isoforms encoded by this gene are specific inhibitors of type 1 serine/threonine protein phosphatases and can bind but not cleave RNA. The third protein isoform lacks the phosphatase inhibitory function but is a single-strand endoribonuclease comparable to RNase E of E. coli. This isoform requires magnesium for its function and cleaves specific sites in A+U-rich regions of RNA. [provided by RefSeq, Jul …

**Accessions** — [HGNC:9296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9296) · Entrez [5511](https://www.ncbi.nlm.nih.gov/gene/5511) · UniProt [Q12972](https://www.uniprot.org/uniprotkb/Q12972) · Ensembl [ENSG00000117751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117751)

## Data

Gene col 3948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3948); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3948]; `tensor/DDL_lfc|DDL_z.npy` [3948]; `embed/gene_vectors.npy` [3948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3948 or target_col == 3948). Every well: [[PPP1R8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
