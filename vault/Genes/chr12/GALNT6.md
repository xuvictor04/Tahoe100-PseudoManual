---
symbol: "GALNT6"
type: "gene"
col: 6324
ensembl_id: "ENSG00000139629"
name: "polypeptide N-acetylgalactosaminyltransferase 6"
location: "12q13.13"
module: 116
arm: "+"
pooled_cpm: 20.74
n_lines_expressing: 36
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# GALNT6

*polypeptide N-acetylgalactosaminyltransferase 6* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.64× (z +6.4, q 1e-07, up in 20 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.55× (z +5.6, q 4e-06, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.419× (z -11.2, q 4e-26, down in 31 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5R2]] (+0.64, fdr 7e-06), [[ADTRP]] (+0.56, fdr 1e-05), [[MAST4]] (+0.56, fdr 1e-05); moves opposite to [[FTH1]] (-0.46, fdr 4e-05), [[NPR3]] (-0.44, fdr 6e-04), [[C1R]] (-0.43, fdr 2e-04).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 2 go from it, the strongest it → [[OR4F15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.64×** | +6.4 | 1e-07 | 20/30 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.65×** | +6.2 | 2e-07 | 13/20 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.6 | 4e-06 | 20/33 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.79×** | +4.3 | 0.002 | 12/32 (RKO, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.002 | 16/34 (PANC-1, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 0.002 | 17/34 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.055 | 12/33 (NCI-H1573, HT-29, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -11.2 | 4e-26 | 31/34 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.474×** | -9.6 | 3e-19 | 23/33 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.537×** | -8.0 | 3e-13 | 22/33 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -7.4 | 2e-11 | 22/33 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.452×** | -5.3 | 1e-05 | 23/33 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -4.8 | 2e-04 | 15/32 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -3.8 | 0.012 | 12/34 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.748×** | -3.7 | 0.015 | 11/33 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.019 | 14/34 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.032 | 12/34 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.755×** | -3.4 | 0.036 | 12/33 (SW480, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.041 | 15/34 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **0.617×** | -3.2 | 0.054 | 8/34 (NCI-H1573, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.776×** | -3.1 | 0.074 | 8/33 (HT-29, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.0 | 0.093 | 14/33 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 191 | 0 | 19 (12 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -20.1) |
| [[SW480 (line)]] | alt | 42.9 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 38.6 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -9.7) |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -9.0) |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.4) |
| [[A-427 (line)]] | wt | 33.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -11.2) |
| [[A-172 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -9.3) ⚠ position not correctable |
| [[LoVo (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.324× (z -9.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.52 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0825× (z -11.0) |
| [[PANC-1 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.136× (z -9.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A498 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R2]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ADTRP]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MAST4]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.55 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[BCL2A1]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[NAV3]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[VEPH1]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CA13]] | +0.54 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CD274]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[IL31RA]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[DTNA]] | +0.51 | +0.34 / +0.43 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTH1]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NPR3]] | -0.44 | -0.49 / -0.22 | both halves | 6e-04 |  |
| [[C1R]] | -0.43 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CP]] | -0.43 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GALNT6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[BSPRY]] | B | BSPRY activity raises GALNT6's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.95× lower at baseline in the lines without BSPRY | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[OR4F15]] | B | OR4F15 activity lowers GALNT6's level | lines that do not express OR4F15 (32) vs lines expressing it (18) | 2.10× higher at baseline in the lines without OR4F15 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, PHACTR1, ITGA4 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OR4F15]] | B | GALNT6 activity lowers OR4F15's level | lines that do not express GALNT6 (14) vs lines expressing it (36) | 2.36× higher at baseline in the lines without GALNT6 | 0.040 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, ACOT11, TNFRSF10A-DT |
| [[NPR3]] | B | GALNT6 activity lowers NPR3's level | lines that do not express GALNT6 (14) vs lines expressing it (36) | 1.70× higher at baseline in the lines without GALNT6 | 0.081 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, ACOT11, TNFRSF10A-DT |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.8, 11.4); signed map (15.3, 45.0). **Vector** length 74.9, 16.6% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.8 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -8.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -11.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,351,247-51,392,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T6 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCL4](https://www.uniprot.org/uniprotkb/Q8NCL4) (Polypeptide N-acetylgalactosaminyltransferase 6):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. May participate in synthesis of oncofetal fibronectin. Has activity toward MUC1A, MUC2, EA2 and fibronectin peptides. Glycosylates FGF23.

**Summary**, from NCBI Gene [11226](https://www.ncbi.nlm.nih.gov/gene/11226):

> This gene encodes a member of the UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase (GalNAc-T) family of enzymes. GalNAc-Ts initiate mucin-type O-linked glycosylation in the Golgi apparatus by catalyzing the transfer of GalNAc to serine and threonine residues on target proteins. They are characterized by an N-terminal transmembrane domain, a stem region, a lumenal catalytic domain containing a GT1 motif and Gal/GalNAc transferase motif, and a C-terminal …

**Accessions** — [HGNC:4128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4128) · Entrez [11226](https://www.ncbi.nlm.nih.gov/gene/11226) · UniProt [Q8NCL4](https://www.uniprot.org/uniprotkb/Q8NCL4) · Ensembl [ENSG00000139629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139629)

## Data

Gene col 6324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6324); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6324]; `tensor/DDL_lfc|DDL_z.npy` [6324]; `embed/gene_vectors.npy` [6324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6324 or target_col == 6324). Every well: [[GALNT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
