---
symbol: "CACNA1C"
type: "gene"
col: 7482
ensembl_id: "ENSG00000151067"
name: "calcium voltage-gated channel subunit alpha1 C"
location: "12p13.33"
module: 104
arm: "+"
pooled_cpm: 20.11
n_lines_expressing: 37
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 16
direction_downstream: 2
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# CACNA1C

*calcium voltage-gated channel subunit alpha1 C* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.34× (z +29.5, q 0e+00, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.627× (z -8.1, q 3e-13, down in 19 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD11B1]] (+0.59, fdr 1e-04), [[ABLIM3]] (+0.58, fdr 1e-05), [[PLD5]] (+0.57, fdr 3e-05); moves opposite to [[LRRC27]] (-0.42, fdr 2e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ERC2]] → it (grade B ⚠); 2 go from it, the strongest it → [[HS6ST3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +29.5 | 0e+00 | 21/32 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.72×** | +24.5 | 0e+00 | 29/34 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.07×** | +19.4 | 0e+00 | 30/33 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +13.0 | 1e-36 | 26/35 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +12.2 | 3e-32 | 8/24 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.2 | 3e-27 | 2/18 (BT-474, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +10.0 | 2e-21 | 15/33 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.1 | 3e-14 | 11/34 (SW48, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +7.7 | 8e-13 | 18/31 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.5 | 5e-09 | 8/32 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.4 | 9e-09 | 4/20 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 11/34 (SW480, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +5.0 | 2e-05 | 13/34 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.32×** | +4.8 | 8e-05 | 12/35 (A-427, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 2e-04 | 9/33 (SW48, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 1e-03 | 9/33 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 10/31 (hTERT-HPNE, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.004 | 9/32 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.005 | 9/31 (HOP62, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.627×** | -8.1 | 3e-13 | 19/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.690×** | -6.2 | 2e-07 | 18/34 (A498, SW480, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.703×** | -6.1 | 2e-07 | 18/35 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -6.1 | 2e-07 | 18/34 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -6.0 | 2e-07 | 18/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -6.0 | 2e-07 | 15/31 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.743×** | -5.2 | 2e-05 | 16/31 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.790×** | -4.1 | 0.003 | 7/33 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.805×** | -3.8 | 0.011 | 10/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.869× | -3.5 | 0.031 | 10/35 (LoVo, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.2 | 5 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.65× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.278× (z -11.1) |
| [[A-427 (line)]] | wt | 18.1 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.39× (z +17.1) | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 3 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.99× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.107× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.216× (z -8.8) |
| [[A498 (line)]] | wt | 34.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 39.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[LoVo (line)]] | wt | 36.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -12.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.240× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 6.25 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 13.5× (z +15.3) | — |
| [[SW1417 (line)]] | alt | 74.5 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -16.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 11.0 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.35× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 10.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +9.5) | — |
| [[H4 (line)]] | wt | 70.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.158× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[LS 180 (line)]] | wt | 7.34 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.38× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.98× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 8.42 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.63× (z +9.1) | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0426× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[CHP-212 (line)]] | wt | 47.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0520× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0838× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[hTERT-HPNE (line)]] | wt | 99.2 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 2.94× (z +8.7) | — |
| [[J82 (line)]] | alt | 21.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 175 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.0655× (z -8.6) |
| [[A-172 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD11B1]] | +0.59 | +0.33 / +0.66 | both halves | 1e-04 | **novel candidate** |
| [[ABLIM3]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PLD5]] | +0.57 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[SVEP1]] | +0.56 | +0.38 / +0.69 | both halves | 6e-05 |  |
| [[GAB3]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[LTBP1]] | +0.52 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[SH3RF3]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TMTC1]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[S1PR3]] | +0.50 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ENTREP2]] | +0.50 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[JCAD]] | +0.49 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[KCNB1]] | +0.49 | +0.36 / +0.50 | both halves | 1e-04 | pathway: Integration of energy metabolism; STRING 693 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.42 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERC2]] | B | ERC2 activity raises CACNA1C's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ERC2 | 0.006 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CACNA1C's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[AMPH]] | B | AMPH activity raises CACNA1C's level | lines that do not express AMPH (36) vs lines expressing it (14) | 3.95× lower at baseline in the lines without AMPH | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ANKRD30B, GRIN2A, GYPC |
| [[PRR16]] | B | PRR16 activity raises CACNA1C's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 2.81× lower at baseline in the lines without PRR16 | 0.016 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[DAAM2]] | B | DAAM2 activity raises CACNA1C's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.00× lower at baseline in the lines without DAAM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent |
| [[ADAMTS2]] | B | ADAMTS2 activity raises CACNA1C's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.19× lower at baseline in the lines without ADAMTS2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[GLIS1]] | B | GLIS1 activity raises CACNA1C's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.44× lower at baseline in the lines without GLIS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[ITGA8]] | B | ITGA8 activity raises CACNA1C's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 3.71× lower at baseline in the lines without ITGA8 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent |
| [[CCBE1]] | B | CCBE1 activity weakens CACNA1C's drug response | lines that do not express CCBE1 (22) vs lines expressing it (14) | the lines without CCBE1 respond 2.08× as strongly (z diff -2.00); strongest at Dinaciclib 0.5 µM: 1.58x vs 0.57x (z diff -5.0) | 0.036 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; target measured in part of the lines; artifact flags |
| [[RNF175]] | B | RNF175 activity raises CACNA1C's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without RNF175 | 0.045 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG |
| [[SDK2]] | B | SDK2 activity raises CACNA1C's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.40× lower at baseline in the lines without SDK2 | 0.056 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[VGLL3]] | B | VGLL3 activity weakens CACNA1C's drug response | lines that do not express VGLL3 (22) vs lines expressing it (14) | the lines without VGLL3 respond 1.88× as strongly (z diff -1.94); strongest at Idarubicin (hydrochloride) 5 µM: 2.59x vs 1.31x (z diff -4.0) | 0.074 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS6ST3]] | B | CACNA1C activity raises HS6ST3's level | lines that do not express CACNA1C (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without CACNA1C | 0.090 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, PSD2, LINC01579; maybe low, not absent |
| [[ADAMTS2]] | B | CACNA1C activity raises ADAMTS2's level | lines that do not express CACNA1C (13) vs lines expressing it (37) | 3.26× lower at baseline in the lines without CACNA1C | 0.094 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, PSD2, LINC01579; maybe low, not absent |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 16.6); signed map (20.2, 36.0). **Vector** length 78.1, 15.6% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.4 | +24.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.1 | +19.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +29.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +4.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -8.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel subunit alpha1 C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:1,970,772-2,697,950 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cav1.2, CACH2, CACN2, TS, LQT8; previously CCHL1A1, CACNL1A1, CACNA1C-IT2 |
| Gene groups (HGNC) | Calcium voltage-gated channel alpha1 subunits |
| Reactome | 11 pathways, smallest: Phase 2 - plateau phase; Adrenaline,noradrenaline inhibits insulin secretion; Phase 0 - rapid depolarisation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13936](https://www.uniprot.org/uniprotkb/Q13936) (Voltage-dependent L-type calcium channel subunit alpha-1C):

> Pore-forming, alpha-1C subunit of the voltage-gated calcium channel that gives rise to L-type calcium currents. Mediates influx of calcium ions into the cytoplasm, and thereby triggers calcium release from the sarcoplasm (By similarity). Plays an important role in excitation-contraction coupling in the heart. Required for normal heart development and normal regulation of heart rhythm. Required for normal contraction of smooth muscle cells in blood vessels and in the intestine. Essential for …

**Summary**, from NCBI Gene [775](https://www.ncbi.nlm.nih.gov/gene/775):

> This gene encodes an alpha-1 subunit of a voltage-dependent calcium channel. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization. The alpha-1 subunit consists of 24 transmembrane segments and forms the pore through which ions pass into the cell. The calcium channel consists of a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. There are multiple isoforms of each of these proteins, either encoded by different genes or the …

**Accessions** — [HGNC:1390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1390) · Entrez [775](https://www.ncbi.nlm.nih.gov/gene/775) · UniProt [Q13936](https://www.uniprot.org/uniprotkb/Q13936) · Ensembl [ENSG00000151067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151067)

## Data

Gene col 7482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7482); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7482]; `tensor/DDL_lfc|DDL_z.npy` [7482]; `embed/gene_vectors.npy` [7482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7482 or target_col == 7482). Every well: [[CACNA1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
