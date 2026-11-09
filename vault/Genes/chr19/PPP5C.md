---
symbol: "PPP5C"
type: "gene"
col: 245
ensembl_id: "ENSG00000011485"
name: "protein phosphatase 5 catalytic subunit"
location: "19q13.32"
module: 4
arm: "+"
pooled_cpm: 26.16
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PPP5C

*protein phosphatase 5 catalytic subunit* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.02× (z +14.5, q 6e-45, up in 35 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.34× (z +6.0, q 3e-07, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.592× (z -15.3, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPS1]] (+0.78, fdr 7e-06), [[TUBGCP3]] (+0.73, fdr 7e-06), [[PRPF19]] (+0.73, fdr 1e-05); moves opposite to [[SPATC1]] (-0.71, fdr 7e-06), [[CATSPERG]] (-0.65, fdr 7e-06), [[ARID4B]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.02×** | +14.5 | 6e-45 | 35/43 (HT-29, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +12.2 | 6e-32 | 29/42 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.72×** | +10.8 | 8e-25 | 29/37 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +7.7 | 1e-12 | 35/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.0 | 3e-07 | 23/47 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.28×** | +4.9 | 1e-04 | 17/44 (C-33 A, HT-29, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.26×** | +4.7 | 2e-04 | 16/47 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 9/46 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 15/48 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.21×** | +3.9 | 0.004 | 14/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.21×** | +3.9 | 0.004 | 14/47 (SW480, KATO III, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.007 | 16/47 (Hs 766T, A549, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.020 | 9/46 (HEC-1-A, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.020 | 14/47 (NCI-H1792, Panc 03.27, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.024 | 10/47 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.034 | 5/47 (C32, RKO, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.034 | 11/47 (RKO, COLO 205, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.052 | 12/47 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.053 | 14/47 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.080 | 3/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.086 | 8/47 (C32, A-172, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.087 | 13/47 (HOP62, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -15.3 | 0e+00 | 40/48 (SHP-77, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.681×** | -11.2 | 2e-26 | 31/47 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -4.3 | 0.002 | 20/46 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.811×** | -4.3 | 0.002 | 5/48 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.2 | 0.002 | 17/48 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.7 | 0.024 | 17/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Cilostazol (drug)]] 5 µM |  | 0.849× | -3.2 | 0.098 | 5/47 (A498, HCT15, …) | top dose only | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.896× | -3.2 | 0.10 | 7/48 (SW1417, NCI-H2030, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.7) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -10.0) |
| [[HT-29 (line)]] | alt | 39.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.3) |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.3) |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.7) |
| [[SHP-77 (line)]] | alt | 46.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.1) |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.0) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS1]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.73 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[GOT2]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.71 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[DLAT]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[FAM98B]] | +0.69 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[RPE]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SSX2IP]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[CSTF2]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATC1]] | -0.71 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[CATSPERG]] | -0.65 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ARID4B]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.63 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[OFD1]] | -0.63 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[PLA2G12B]] | -0.63 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[RNASEK]] | -0.62 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[CD63]] | -0.62 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.62 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[SYNRG]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TESK2]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[GCC2]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PPP5C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMEM106A]] | B | TMEM106A activity lowers PPP5C's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.68× higher at baseline in the lines without TMEM106A | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DAGLA]] | C | DAGLA activity raises PPP5C's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without DAGLA | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.7, -34.8); signed map (-15.9, -45.3). **Vector** length 97.5, 21.0% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.2 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.7 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.6 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +6.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.8 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -15.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 5 catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,347,087-46,392,981 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP5; previously PPP5 |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits; Tetratricopeptide repeat domain containing |
| Reactome | 10 pathways, smallest: Negative regulation of MAPK pathway; Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; DNA Double Strand Break Response |
| Matched by | ensembl_id |

**Function**, from UniProt [P53041](https://www.uniprot.org/uniprotkb/P53041) (Serine/threonine-protein phosphatase 5):

> Serine/threonine-protein phosphatase that dephosphorylates a myriad of proteins involved in different signaling pathways including the kinases CSNK1E, ASK1/MAP3K5, PRKDC and RAF1, the nuclear receptors NR3C1, PPARG, ESR1 and ESR2, SMAD proteins and TAU/MAPT. Implicated in wide ranging cellular processes, including apoptosis, differentiation, DNA damage response, cell survival, regulation of ion channels or circadian rhythms, in response to steroid and thyroid hormones, calcium, fatty acids, …

**Summary**, from NCBI Gene [5536](https://www.ncbi.nlm.nih.gov/gene/5536):

> This gene encodes a serine/threonine phosphatase which is a member of the protein phosphatase catalytic subunit family. Proteins in this family participate in pathways regulated by reversible phosphorylation at serine and threonine residues; many of these pathways are involved in the regulation of cell growth and differentiation. The product of this gene has been shown to participate in signaling pathways in response to hormones or cellular stress, and elevated levels of this protein may be …

**Accessions** — [HGNC:9322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9322) · Entrez [5536](https://www.ncbi.nlm.nih.gov/gene/5536) · UniProt [P53041](https://www.uniprot.org/uniprotkb/P53041) · Ensembl [ENSG00000011485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011485)

## Data

Gene col 245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 245); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 245]; `tensor/DDL_lfc|DDL_z.npy` [245]; `embed/gene_vectors.npy` [245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 245 or target_col == 245). Every well: [[PPP5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
