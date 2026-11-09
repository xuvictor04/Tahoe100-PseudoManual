---
symbol: "PPFIA3"
type: "gene"
col: 10816
ensembl_id: "ENSG00000177380"
name: "PPFI scaffold protein A3"
location: "19q13.33"
module: 103
arm: "+"
pooled_cpm: 10.44
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# PPFIA3

*PPFI scaffold protein A3* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.81× (z +19.5, q 0e+00, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.584× (z -7.2, q 4e-10, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAG3]] (+0.60, fdr 1e-05), [[S1PR2]] (+0.60, fdr 1e-05), [[JMJD6]] (+0.58, fdr 2e-05); moves opposite to [[SIRT5]] (-0.45, fdr 3e-04), [[TFAM]] (-0.44, fdr 0.001, ⚠ not reproduced), [[CLNS1A]] (-0.43, fdr 1e-04), [[RPS3A]] (-0.41, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.81×** | +19.5 | 0e+00 | 35/42 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +15.6 | 0e+00 | 36/43 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.09×** | +15.0 | 0e+00 | 36/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.79×** | +13.6 | 3e-40 | 36/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.56×** | +12.5 | 8e-34 | 33/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +9.2 | 4e-18 | 28/44 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +7.0 | 2e-10 | 23/43 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +6.4 | 1e-08 | 22/42 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.4 | 1e-08 | 23/45 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +5.4 | 4e-06 | 17/43 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +5.2 | 1e-05 | 16/40 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.003 | 18/43 (NCI-H460, HEC-1-A, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.004 | 12/42 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.018 | 15/42 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.018 | 3/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.085 | 6/42 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -7.2 | 4e-10 | 23/44 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -5.9 | 9e-07 | 19/43 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -5.8 | 9e-07 | 19/43 (C32, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -5.6 | 3e-06 | 19/39 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -4.0 | 0.009 | 15/43 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -3.8 | 0.013 | 14/41 (C32, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -3.3 | 0.072 | 17/42 (SNU-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.082 | 9/43 (LoVo, C32, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | 0.781× | -3.1 | 0.11 | 12/45 (hTERT-HPNE, J82, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 42.7 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -13.2) |
| [[HT-29 (line)]] | alt | 8.15 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.9) | — |
| [[KATO III (line)]] | alt | 9.70 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0452× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0459× (z -13.3) |
| [[SW480 (line)]] | alt | 10.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.5) | — |
| [[A549 (line)]] | wt | 4.19 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +12.4) | — |
| [[LoVo (line)]] | wt | 10.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.283× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -8.5) |
| [[LS 180 (line)]] | wt | 8.72 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 7.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 6.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 8.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.1) | — |
| [[A-172 (line)]] | wt | 7.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 7.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 6.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 8.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +9.8) | — |
| [[J82 (line)]] | alt | 5.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 5.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0256× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +12.2) | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0864× (z -10.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SW1417 (line)]] | alt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG3]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[S1PR2]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[JMJD6]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ACAP3]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ZNF77]] | +0.56 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PRICKLE3]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TMEM39B]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[KREMEN2]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[BRSK1]] | +0.53 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[GYS1]] | +0.52 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[KDM2B]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[LZTS2]] | +0.51 | +0.45 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT5]] | -0.45 | -0.26 / -0.47 | both halves | 3e-04 |  |
| [[TFAM]] | -0.44 | -0.17 / -0.36 | ⚠ not reproduced | 0.001 |  |
| [[CLNS1A]] | -0.43 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[RPS3A]] | -0.41 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[ARPP19]] | -0.41 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAG3]] | B | STAG3 activity raises PPFIA3's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.82× lower at baseline in the lines without STAG3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.1, -5.0); signed map (-33.0, 33.9). **Vector** length 79.9, 15.1% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +19.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +7.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +15.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +3.0 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PPFI scaffold protein A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,119,544-49,151,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0654, LPNA3, MGC126567, MGC126569 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; PPFI scaffold protein family |
| Reactome | 10 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; Norepinephrine Neurotransmitter Release Cycle; Receptor-type tyrosine-protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75145](https://www.uniprot.org/uniprotkb/O75145) (Liprin-alpha-3):

> May regulate the disassembly of focal adhesions. May localize receptor-like tyrosine phosphatases type 2A at specific sites on the plasma membrane, possibly regulating their interaction with the extracellular environment and their association with substrates.

**Summary**, from NCBI Gene [8541](https://www.ncbi.nlm.nih.gov/gene/8541):

> The protein encoded by this gene is a member of the LAR protein-tyrosine phosphatase-interacting protein (liprin) family. Liprins interact with members of LAR family of transmembrane protein tyrosine phosphatases, which are known to be important for axon guidance and mammary gland development. Liprin family protein has been shown to localize phosphatase LAR to cell focal adhesions and may be involved in the molecular organization of presynaptic active zones. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9247) · Entrez [8541](https://www.ncbi.nlm.nih.gov/gene/8541) · UniProt [O75145](https://www.uniprot.org/uniprotkb/O75145) · Ensembl [ENSG00000177380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177380)

## Data

Gene col 10816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10816); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10816]; `tensor/DDL_lfc|DDL_z.npy` [10816]; `embed/gene_vectors.npy` [10816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10816 or target_col == 10816). Every well: [[PPFIA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPFIA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
