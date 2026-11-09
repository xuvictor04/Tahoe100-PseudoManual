---
symbol: "S1PR2"
type: "gene"
col: 15559
ensembl_id: "ENSG00000267534"
name: "sphingosine-1-phosphate receptor 2"
location: "19p13.2"
module: 13
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# S1PR2

*sphingosine-1-phosphate receptor 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.36× (z +5.1, q 2e-04, up in 9 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.208× (z -9.6, q 5e-19, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPFIA3]] (+0.60, fdr 1e-05), [[ARNT2]] (+0.59, fdr 2e-05), [[EPOP]] (+0.56, fdr 3e-05); moves opposite to [[PPHLN1]] (-0.48, fdr 4e-05), [[TMEM245]] (-0.44, fdr 2e-04), [[CLASP1]] (-0.43, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GABBR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.1 | 2e-04 | 9/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.007 | 14/37 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.008 | 9/40 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.4 | 0.091 | 1/8 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.096 | 7/44 (SW 900, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.32× | +3.2 | 0.11 | 7/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.2 | 0.11 | 1/11 (A-172) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15559.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.208×** | -9.6 | 5e-19 | 32/40 (C32, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.527×** | -7.5 | 2e-11 | 20/42 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.310×** | -7.1 | 2e-10 | 21/35 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.557×** | -6.8 | 1e-09 | 20/44 (A-427, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.583×** | -6.3 | 4e-08 | 21/42 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -5.7 | 9e-07 | 17/41 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -5.7 | 1e-06 | 17/42 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.635×** | -5.3 | 9e-06 | 18/42 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -5.1 | 2e-05 | 14/42 (SHP-77, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.670×** | -4.5 | 4e-04 | 14/39 (A498, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -4.4 | 5e-04 | 11/32 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.685×** | -4.4 | 5e-04 | 14/44 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.695×** | -4.0 | 0.003 | 13/42 (SW1417, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -3.8 | 0.006 | 16/41 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.709×** | -3.8 | 0.006 | 17/40 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 6 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0498× (z -15.6) |
| [[C32 (line)]] | wt | 15.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0942× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0266× (z -9.5) |
| [[A-172 (line)]] | wt | 9.57 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.111× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 3.53 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0755× (z -9.6) |
| [[A-427 (line)]] | wt | 5.22 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 6.26 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 3.48 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0771× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0679× (z -11.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 3.76 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0391× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 4.43 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0650× (z -9.7) |
| [[A498 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIA3]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ARNT2]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[EPOP]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[HLA-L-1]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PRR7]] | +0.52 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[PHLDB1]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[GRINA]] | +0.51 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[PRICKLE3]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TRIM47]] | +0.49 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RELA]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[KRBA1]] | +0.48 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PLD6]] | +0.48 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPHLN1]] | -0.48 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TMEM245]] | -0.44 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[CLASP1]] | -0.43 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CCNY]] | -0.42 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[CD99L2]] | -0.42 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[POLR2B]] | -0.42 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[HNRNPA1]] | -0.42 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[RPS3A]] | -0.42 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[STAM]] | -0.41 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[CSDE1]] | -0.41 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[ATP5F1C]] | -0.41 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[STRAP]] | -0.40 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABBR1]] | B | GABBR1 activity raises S1PR2's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 2.33× lower at baseline in the lines without GABBR1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.277). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, -5.0); signed map (9.4, 22.8). **Vector** length 63.4, 9.70% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.5 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.8 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +1.7 |
|  | [[Imiquimod (maleate) (drug)]] 0.05 µM |  | +0.7 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -7.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine-1-phosphate receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,221,433-10,231,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Gpcr13, H218, AGR16; previously EDG5, DFNB68 |
| Gene groups (HGNC) | Sphingosine 1-phosphate receptors |
| Reactome | 6 pathways, smallest: Lysosphingolipid and LPA receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O95136](https://www.uniprot.org/uniprotkb/O95136) (Sphingosine 1-phosphate receptor 2):

> Receptor for the lysosphingolipid sphingosine 1-phosphate (S1P). S1P is a bioactive lysophospholipid that elicits diverse physiological effects on most types of cells and tissues. When expressed in rat HTC4 hepatoma cells, is capable of mediating S1P-induced cell proliferation and suppression of apoptosis. Receptor for the chemokine-like protein FAM19A5. Mediates the inhibitory effect of FAM19A5 on vascular smooth muscle cell proliferation and migration (By similarity). In lymphoid follicles, …

**Summary**, from NCBI Gene [9294](https://www.ncbi.nlm.nih.gov/gene/9294):

> This gene encodes a member of the G protein-coupled receptors, as well as the EDG family of proteins. The encoded protein is a receptor for sphingosine 1-phosphate, which participates in cell proliferation, survival, and transcriptional activation. Defects in this gene have been associated with congenital profound deafness. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:3169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3169) · Entrez [9294](https://www.ncbi.nlm.nih.gov/gene/9294) · UniProt [O95136](https://www.uniprot.org/uniprotkb/O95136) · Ensembl [ENSG00000267534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267534)

## Data

Gene col 15559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15559); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15559]; `tensor/DDL_lfc|DDL_z.npy` [15559]; `embed/gene_vectors.npy` [15559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15559 or target_col == 15559). Every well: [[S1PR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/S1PR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
