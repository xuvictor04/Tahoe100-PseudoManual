---
symbol: "STRN4"
type: "gene"
col: 1619
ensembl_id: "ENSG00000090372"
name: "striatin 4"
location: "19q13.32"
module: 153
arm: "+"
pooled_cpm: 32.19
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# STRN4

*striatin 4* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.84× (z +14.3, q 1e-43, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.392× (z -12.8, q 6e-35, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASH8P]] (+0.74, fdr 7e-06, ⚠ WASH8P in the vector space only through flagged drug-doses), [[MED12]] (+0.72, fdr 9e-06), [[USP19]] (+0.71, fdr 7e-06), [[DLG5]] (+0.71, fdr 7e-06); moves opposite to [[PIBF1]] (-0.61, fdr 2e-05), [[GNAI3]] (-0.59, fdr 7e-05), [[UBA6]] (-0.58, fdr 1e-04).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.84×** | +14.3 | 1e-43 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.0 | 3e-21 | 42/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +9.7 | 5e-20 | 41/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.92×** | +9.0 | 5e-17 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +8.5 | 2e-15 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +5.8 | 6e-07 | 37/49 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +5.7 | 7e-07 | 34/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.7 | 7e-07 | 36/47 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +5.3 | 9e-06 | 28/48 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 2e-05 | 29/47 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.0 | 3e-05 | 26/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.7 | 1e-04 | 37/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.023 | 23/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.046 | 22/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.075 | 20/48 (HCT15, HS-578T, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.075 | 8/48 (J82, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.392×** | -12.8 | 6e-35 | 47/48 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.465×** | -10.5 | 3e-23 | 43/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.497×** | -9.6 | 2e-19 | 44/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -7.3 | 4e-11 | 42/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -5.4 | 8e-06 | 2/49 (LoVo, CHP-212) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.702×** | -4.8 | 1e-04 | 32/47 (A549, NCI-H661, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.563×** | -4.1 | 0.003 | 26/48 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.742×** | -4.1 | 0.003 | 25/47 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -3.8 | 0.009 | 26/48 (BT-474, NCI-H2030, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.841× | -3.3 | 0.062 | 24/48 (LoVo, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.2 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -8.8) |
| [[SW480 (line)]] | alt | 36.1 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +13.8) | [[Belinostat (drug)]] 5 µM 0.330× (z -11.0) |
| [[PANC-1 (line)]] | alt | 22.7 | 2 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.359× (z -10.1) |
| [[SW1417 (line)]] | alt | 56.3 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -11.0) |
| [[LoVo (line)]] | wt | 29.3 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +10.2) | [[Belinostat (drug)]] 5 µM 0.261× (z -12.3) |
| [[CHP-212 (line)]] | wt | 37.0 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0977× (z -9.4) |
| [[HT-29 (line)]] | alt | 48.0 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.285× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 20.7 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.273× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 33.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +9.6) | — |
| [[A-427 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A498 (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.4) | — |
| [[A549 (line)]] | wt | 41.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -11.2) |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0865× (z -9.4) |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -8.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[COLO 205 (line)]] | alt | 21.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.50× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 22.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +9.7) | — |
| [[KATO III (line)]] | alt | 34.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 29.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 30.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 39.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -8.5) |
| [[RKO (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -8.5) |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.230× (z -8.6) |
| [[SW 900 (line)]] | alt | 35.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +9.3) | — |
| [[SW48 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASH8P]] ⚠ | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MED12]] | +0.72 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[USP19]] | +0.71 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[DLG5]] | +0.71 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[WIZ]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PRDM11]] | +0.67 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ARFGAP2]] | +0.67 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PLXNB1]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MTA2]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.66 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[WDR6]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 | same gene group |
| [[ATP13A1]] | +0.65 | +0.57 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[GNAI3]] | -0.59 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[UBA6]] | -0.58 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[CHCHD2]] | -0.57 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[CIB1]] | -0.57 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[LGALS1]] | -0.55 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[MGST3]] | -0.55 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ANKRD37]] | -0.55 | -0.37 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises STRN4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises STRN4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.1, -23.6); signed map (-10.5, -32.6). **Vector** length 85.6, 20.7% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.5 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +5.3 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | -0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.8 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +0.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -12.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -7.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.7 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | striatin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,719,511-46,746,994 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIN, PPP2R6C |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits; STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRL3](https://www.uniprot.org/uniprotkb/Q9NRL3) (Striatin-4):

> Calmodulin-binding scaffolding protein which is the center of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, differentiation, apoptosis, metabolism and immune regulation (Probable). …

**Summary**, from NCBI Gene [29888](https://www.ncbi.nlm.nih.gov/gene/29888):

> Enables armadillo repeat domain binding activity and protein phosphatase 2A binding activity. Contributes to protein-macromolecule adaptor activity. Involved in negative regulation of hippo signaling. Part of FAR/SIN/STRIPAK complex. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15721) · Entrez [29888](https://www.ncbi.nlm.nih.gov/gene/29888) · UniProt [Q9NRL3](https://www.uniprot.org/uniprotkb/Q9NRL3) · Ensembl [ENSG00000090372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090372)

## Data

Gene col 1619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1619); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1619]; `tensor/DDL_lfc|DDL_z.npy` [1619]; `embed/gene_vectors.npy` [1619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1619 or target_col == 1619). Every well: [[STRN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
