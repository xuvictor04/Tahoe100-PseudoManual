---
symbol: "GALNT3"
type: "gene"
col: 3661
ensembl_id: "ENSG00000115339"
name: "polypeptide N-acetylgalactosaminyltransferase 3"
location: "2q24.3"
module: 31
arm: "+"
pooled_cpm: 42.43
n_lines_expressing: 20
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 55
direction_downstream: 89
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# GALNT3

*polypeptide N-acetylgalactosaminyltransferase 3* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +13.0, q 1e-35, up in 1 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.512× (z -11.1, q 1e-25, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESRP1]] (+0.78, fdr 7e-06), [[FUT3]] (+0.69, fdr 7e-06), [[MCTP2]] (+0.67, fdr 1e-05); moves opposite to [[TMEM80]] (-0.49, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 89 go from it, the strongest it → [[JUP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +13.0 | 1e-35 | 1/18 (NCI-H1792) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +12.6 | 7e-34 | 2/17 (CFPAC-1, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +11.4 | 9e-28 | 2/19 (CFPAC-1, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.0 | 3e-17 | 1/19 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +7.6 | 3e-12 | 1/17 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +6.8 | 1e-09 | 1/18 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.52×** | +6.6 | 3e-09 | 0/18 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +5.8 | 5e-07 | 10/19 (LS 180, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 5e-05 | 5/19 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.4 | 5e-04 | 1/18 (LS 180) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.015 | 4/18 (LS 180, NCI-H1573, …) | rises with dose | position effect removed |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.023 | 0/19 | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.029 | 5/18 (COLO 205, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.036 | 12/18 (NCI-H2347, HT-29, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.036 | 0/18 | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.051 | 11/18 (LS 180, SW 900, …) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.070 | 4/18 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -11.1 | 1e-25 | 18/18 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -9.7 | 6e-20 | 18/18 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.644×** | -7.6 | 7e-12 | 18/18 (HS-578T, NCI-H2347, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -6.3 | 5e-08 | 12/18 (SW 900, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.696×** | -6.2 | 5e-08 | 18/18 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.702×** | -6.1 | 1e-07 | 16/18 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -5.6 | 2e-06 | 18/18 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.734×** | -5.3 | 8e-06 | 15/18 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.558×** | -5.2 | 1e-05 | 15/18 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.574×** | -5.0 | 4e-05 | 17/19 (LoVo, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.767×** | -4.6 | 3e-04 | 14/18 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.5 | 4e-04 | 18/18 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.776×** | -4.4 | 6e-04 | 18/18 (HS-578T, NCI-H2347, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.778×** | -4.1 | 0.001 | 17/18 (COLO 205, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.7 | 0.007 | 12/18 (HS-578T, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.013 | 16/18 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.810×** | -3.3 | 0.028 | 1/18 (BT-474) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.047 | 1/18 (HS-578T) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.077 | 0/18 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 61.5 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -17.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.146× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -29.4) |
| [[LoVo (line)]] | wt | 191 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -14.8) |
| [[KATO III (line)]] | alt | 137 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 93.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -17.3) |
| [[COLO 205 (line)]] | alt | 147 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.238× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 88.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 31.0 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0799× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.188× (z -10.0) |
| [[SW 900 (line)]] | alt | 60.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.183× (z -11.6) |
| [[SW48 (line)]] | wt | 73.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 58.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.6) |
| [[HCT15 (line)]] | alt | 98.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.6) |
| [[LS 180 (line)]] | wt | 144 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.297× (z -10.0) |
| [[BT-474 (line)]] | alt | 145 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -11.2) |
| [[HT-29 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 54.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.0) |
| [[SW480 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -11.2) |
| [[A-172 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.49 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESRP1]] | +0.78 | +0.79 / +0.76 | both halves | 7e-06 | pathway: Signaling by FGFR |
| [[FUT3]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MCTP2]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.67 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CLDN7]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PRSS8]] | +0.62 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[TTC9]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CDH1]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MPZL2]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[MAL2]] | +0.61 | +0.68 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM80]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 8, C 47. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers GALNT3's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 7.03× higher at baseline in the lines without TTC28 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[JUP]] | B | JUP activity raises GALNT3's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.79× lower at baseline in the lines without JUP | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[CDS1]] | B | CDS1 activity raises GALNT3's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without CDS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises GALNT3's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.66× lower at baseline in the lines without SEMA3B | 0.052 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[ARHGAP30]] | B | ARHGAP30 activity raises GALNT3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.63× lower at baseline in the lines without ARHGAP30 | 0.061 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[BNC2]] | B | BNC2 activity lowers GALNT3's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 5.17× higher at baseline in the lines without BNC2 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[KCNK6]] | B | KCNK6 activity raises GALNT3's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 4.27× lower at baseline in the lines without KCNK6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[RALGPS2]] | B | RALGPS2 activity raises GALNT3's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 3.97× lower at baseline in the lines without RALGPS2 | 0.086 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[TMPRSS4]] | C | TMPRSS4 activity raises GALNT3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 12.29× lower at baseline in the lines without TMPRSS4 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises GALNT3's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 12.38× lower at baseline in the lines without ATP2C2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises GALNT3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 13.70× lower at baseline in the lines without TMEM125 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises GALNT3's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 12.25× lower at baseline in the lines without RAB25 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |

### Downstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 40, C 49. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | GALNT3 activity raises JUP's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 5.31× lower at baseline in the lines without GALNT3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[CDS1]] | B | GALNT3 activity raises CDS1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 4.83× lower at baseline in the lines without GALNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[FAM83E]] | B | GALNT3 activity raises FAM83E's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 3.66× lower at baseline in the lines without GALNT3 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[BNC2]] | B | GALNT3 activity lowers BNC2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 5.05× higher at baseline in the lines without GALNT3 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[RALGPS2]] | B | GALNT3 activity raises RALGPS2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without GALNT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[QSOX1]] | B | GALNT3 activity raises QSOX1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without GALNT3 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[TTC28]] | B | GALNT3 activity lowers TTC28's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 4.25× higher at baseline in the lines without GALNT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | GALNT3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express GALNT3 (30) vs lines expressing it (18) | the lines without GALNT3: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[IQANK1]] | B | GALNT3 activity raises IQANK1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 3.92× lower at baseline in the lines without GALNT3 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | GALNT3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express GALNT3 (30) vs lines expressing it (18) | the lines without GALNT3: 0.90× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[SERP1]] | B | GALNT3 activity raises SERP1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without GALNT3 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[SEC31A]] | B | GALNT3 activity raises SEC31A's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.23× lower at baseline in the lines without GALNT3 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.6, 56.7); signed map (58.2, 7.0). **Vector** length 94.4, 37.8% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +0.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:165,747,588-165,846,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T3, HHS, HFTC |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 11 pathways, smallest: FGFR3 ligand binding and activation; FGFR3c ligand binding and activation; Defective GALNT3 causes HFTC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14435](https://www.uniprot.org/uniprotkb/Q14435) (Polypeptide N-acetylgalactosaminyltransferase 3):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has activity toward HIV envelope glycoprotein gp120, EA2, MUC2, MUC1A and MUC5AC. Probably glycosylates fibronectin in vivo. Glycosylates FGF23.

**Summary**, from NCBI Gene [2591](https://www.ncbi.nlm.nih.gov/gene/2591):

> This gene encodes UDP-GalNAc transferase 3, a member of the GalNAc-transferases family. This family transfers an N-acetyl galactosamine to the hydroxyl group of a serine or threonine residue in the first step of O-linked oligosaccharide biosynthesis. Individual GalNAc-transferases have distinct activities and initiation of O-glycosylation is regulated by a repertoire of GalNAc-transferases. The protein encoded by this gene is highly homologous to other family members, however the enzymes have …

**Accessions** — [HGNC:4125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4125) · Entrez [2591](https://www.ncbi.nlm.nih.gov/gene/2591) · UniProt [Q14435](https://www.uniprot.org/uniprotkb/Q14435) · Ensembl [ENSG00000115339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115339)

## Data

Gene col 3661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3661); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3661]; `tensor/DDL_lfc|DDL_z.npy` [3661]; `embed/gene_vectors.npy` [3661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3661 or target_col == 3661). Every well: [[GALNT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
