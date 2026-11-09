---
symbol: "PRSS23-AS1"
type: "gene"
col: 14941
ensembl_id: "ENSG00000255471"
name: "PRSS23 antisense RNA 1"
location: "11q14.2"
module: 19
arm: "+"
pooled_cpm: 5.27
n_lines_expressing: 40
n_dd_up: 27
n_dd_down: 16
n_dd_up_clean: 23
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PRSS23-AS1

*PRSS23 antisense RNA 1* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.87× (z +11.5, q 9e-28, up in 23 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.443× (z -8.8, q 7e-16, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FZD4]] (+0.74, fdr 7e-06, ⚠ same locus), [[SLC38A4]] (+0.56, fdr 1e-05), [[PLAC4]] (+0.53, fdr 3e-05), [[RTN1]] (+0.52, fdr 1e-05); moves opposite to [[TRIML2]] (-0.52, fdr 7e-05), [[DESI1]] (-0.46, fdr 3e-04), [[HNF4G]] (-0.42, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ACTR3C]] → it (grade B ⚠); 2 go from it, the strongest it → [[F2R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +11.5 | 9e-28 | 23/37 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +10.3 | 2e-22 | 1/7 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +9.9 | 1e-20 | 23/38 (J82, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +9.7 | 3e-20 | 24/37 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +9.4 | 9e-19 | 15/30 (A498, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +8.1 | 4e-14 | 4/15 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +7.6 | 2e-12 | 20/37 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +7.5 | 3e-12 | 18/36 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +7.3 | 2e-11 | 13/37 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.66×** | +5.5 | 2e-06 | 13/34 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.3 | 5e-06 | 10/34 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.61×** | +5.2 | 1e-05 | 12/31 (NCI-H460, A549, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.2 | 1e-05 | 3/8 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.46×** | +5.1 | 1e-05 | 5/32 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.57×** | +4.9 | 4e-05 | 12/34 (NCI-H460, A549, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.8 | 5e-05 | 6/25 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.5 | 2e-04 | 6/35 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.006 | 2/31 (NCI-H661, NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.443×** | -8.8 | 7e-16 | 22/37 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -7.0 | 1e-09 | 19/35 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.545×** | -6.6 | 1e-08 | 20/37 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -5.7 | 2e-06 | 15/34 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -4.6 | 4e-04 | 15/34 (H4, Hs 766T, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -4.4 | 0.001 | 13/33 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -4.2 | 0.002 | 11/38 (SW480, A549, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.680×** | -4.2 | 0.002 | 11/37 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -4.0 | 0.004 | 14/23 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -3.9 | 0.006 | 13/36 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.725×** | -3.5 | 0.027 | 11/35 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.028 | 11/37 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -3.4 | 0.028 | 8/26 (MIA PaCa-2, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.731×** | -3.4 | 0.029 | 13/36 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Ivermectin (drug)]] 0.05 µM |  | **0.733×** | -3.3 | 0.031 | 4/37 (SW 1271, J82, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.041 | 10/35 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.669×** | -3.1 | 0.065 | 3/38 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0549× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -8.6) |
| [[Hs 766T (line)]] | wt | 80.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.51 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0533× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 2.33 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0723× (z -9.1) |
| [[LoVo (line)]] | wt | 3.16 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0639× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -9.6) |
| [[PANC-1 (line)]] | alt | 2.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0841× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FZD4]] | +0.74 | +0.61 / +0.77 | both halves | 7e-06 | ⚠ same locus (20.6 kb, same strand: neighbours can correlate without regulation) |
| [[SLC38A4]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[PLAC4]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[RTN1]] | +0.52 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[P4HA3]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[AMDHD1]] | +0.52 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ADAMTSL4]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[PCTP]] | +0.51 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[NRCAM]] | +0.50 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GABBR2]] | +0.50 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KCNMB4]] | +0.50 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[PIP4P2]] | +0.48 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[RGS2]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIML2]] | -0.52 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[DESI1]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[HNF4G]] | -0.42 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[RGS20]] | -0.42 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[ANAPC7]] | -0.41 | -0.21 / -0.43 | both halves | 7e-04 |  |
| [[ENOX2]] | -0.41 | -0.23 / -0.36 | both halves | 5e-04 |  |
| [[CUEDC1]] | -0.41 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[CD2BP2]] | -0.41 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[RUFY3]] | -0.40 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[ACTR3C]] | -0.40 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[LYPLAL1-AS1]] | -0.40 | -0.29 / -0.33 | both halves | 3e-04 | same gene group |
| [[CLIP1]] | -0.40 | -0.24 / -0.39 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR3C]] | B | ACTR3C activity lowers PRSS23-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.47× higher at baseline in the lines without ACTR3C | 0.016 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[RTN1]] | B | RTN1 activity raises PRSS23-AS1's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.05× lower at baseline in the lines without RTN1 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530 |
| [[HNF4G]] | B | HNF4G activity lowers PRSS23-AS1's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.12× higher at baseline in the lines without HNF4G | 0.041 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[UNC13A]] | B | UNC13A activity raises PRSS23-AS1's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without UNC13A | 0.045 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[SLITRK4]] | B | SLITRK4 activity raises PRSS23-AS1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 1.71× lower at baseline in the lines without SLITRK4 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R |
| [[FHL1]] | B | FHL1 activity raises PRSS23-AS1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without FHL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[SCARA5]] | B | SCARA5 activity raises PRSS23-AS1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 1.90× lower at baseline in the lines without SCARA5 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[KCNG2]] | C | KCNG2's natural level weakens PRSS23-AS1's drug response | KCNG2's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.27; direction clear | 0.081 | ⚠ tissue can mimic it; precision caveat |
| [[PART1]] | C | PART1's natural level weakens PRSS23-AS1's drug response | PART1's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.34; direction clear | 0.082 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2R]] | B | PRSS23-AS1 activity raises F2R's level | lines that do not express PRSS23-AS1 (10) vs lines expressing it (40) | 1.62× lower at baseline in the lines without PRSS23-AS1 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FZD4]] | C | PRSS23-AS1's natural level weakens FZD4's drug response | PRSS23-AS1's natural level across 34 lines (lineage-adjusted; a glimpse) | r -0.75, reverse -0.72; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.358). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, 35.0); signed map (44.1, 46.8). **Vector** length 56.5, 8.88% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.3 | +7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.9 | +9.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.7 | +1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.5 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -1.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -6.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.4 | -2.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.3 | +0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | PRSS23 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.2 — chr11:86,892,214-86,925,037 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56071) · Entrez [107984429](https://www.ncbi.nlm.nih.gov/gene/107984429) · Ensembl [ENSG00000255471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255471)

## Data

Gene col 14941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14941); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14941]; `tensor/DDL_lfc|DDL_z.npy` [14941]; `embed/gene_vectors.npy` [14941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14941 or target_col == 14941). Every well: [[PRSS23-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS23-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
