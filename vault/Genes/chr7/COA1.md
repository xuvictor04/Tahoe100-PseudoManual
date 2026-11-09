---
symbol: "COA1"
type: "gene"
col: 2779
ensembl_id: "ENSG00000106603"
name: "cytochrome c oxidase assembly factor 1"
location: "7p13"
module: 4
arm: "+"
pooled_cpm: 133.63
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# COA1

*cytochrome c oxidase assembly factor 1* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.52× (z +7.0, q 1e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -10.0, q 1e-20, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRPD1]] (+0.79, fdr 7e-06), [[AGK]] (+0.75, fdr 7e-06), [[MRPS27]] (+0.75, fdr 7e-06); moves opposite to [[FAM117A]] (-0.69, fdr 1e-05), [[RSRP1]] (-0.67, fdr 7e-06), [[YPEL5]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +7.0 | 1e-09 | 38/48 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +4.7 | 8e-04 | 29/48 (AsPC-1, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +4.5 | 0.001 | 28/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 0.001 | 31/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.026 | 26/47 (NCI-H2347, BT-474, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.039 | 28/49 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.080 | 22/49 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.080 | 23/48 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.25×** | +3.2 | 0.080 | 26/48 (KATO III, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.093 | 19/48 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.0 | 0.13 | 15/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -10.0 | 1e-20 | 39/49 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.575×** | -9.3 | 5e-18 | 36/48 (SW480, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -7.7 | 2e-12 | 38/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -7.1 | 2e-10 | 36/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -5.2 | 2e-05 | 31/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -5.1 | 4e-05 | 27/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -4.3 | 0.001 | 27/50 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.797×** | -3.8 | 0.010 | 25/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.801×** | -3.7 | 0.013 | 25/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.810×** | -3.4 | 0.040 | 22/48 (SW1417, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.825×** | -3.2 | 0.063 | 23/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.873× | -3.2 | 0.063 | 21/48 (SK-MEL-2, SW1417, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 142 | 0 | 13 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 241 | 0 | 7 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -17.0) |
| [[RKO (line)]] | wt | 119 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -10.6) |
| [[C32 (line)]] | wt | 131 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.8) |
| [[SW1417 (line)]] | alt | 132 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.9) |
| [[A498 (line)]] | wt | 141 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 198 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 49.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.1) |
| [[PANC-1 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.531× (z -9.0) |
| [[SHP-77 (line)]] | alt | 321 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.470× (z -10.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -9.2) |
| [[SW48 (line)]] | wt | 180 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.284× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.2) |
| [[SW480 (line)]] | alt | 199 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.422× (z -12.9) |
| [[H4 (line)]] | wt | 235 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.9) |
| [[KATO III (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.340× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 183 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 182 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.8) |
| [[SW 1088 (line)]] | alt | 154 | 0 | 2 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0672× (z -11.3) |
| [[A-172 (line)]] | wt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.2) |
| [[A-427 (line)]] | wt | 129 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.364× (z -12.9) |
| [[A549 (line)]] | wt | 93.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.2) |
| [[HT-29 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.403× (z -11.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 97.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.495× (z -8.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 74.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 174 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.2) |
| [[AN3 CA (line)]] | alt | 173 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 99.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD1]] | +0.79 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[AGK]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[LCLAT1]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[FARSB]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.69 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NOL10]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.69 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.67 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[YPEL5]] | -0.63 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ERO1B]] | -0.62 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.61 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[CD27-AS1]] | -0.60 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[UPK2]] | -0.60 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ATOSA]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MXD1]] | -0.59 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[GNAS]] | -0.59 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TOB2]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COA1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF239]] | B | ZNF239 activity lowers COA1's level | lines that do not express ZNF239 (8) vs lines expressing it (42) | 1.34× higher at baseline in the lines without ZNF239 | 0.089 | ⚠ within organs, on part of the lines |
| [[HDAC6]] | B | HDAC6 activity lowers COA1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.4, -41.3); signed map (-9.9, -47.8). **Vector** length 118, 38.5% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.54 to 8); *tRNA processing* (reactome, mean cos +0.53 to 10); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.57 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.2 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:43,608,456-43,729,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10803, MITRAC15; previously C7orf44 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Mitochondrial complex I assembly complex |
| Reactome | 4 pathways, smallest: Complex IV assembly; Complex I biogenesis; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZY4](https://www.uniprot.org/uniprotkb/Q9GZY4) (Cytochrome c oxidase assembly factor 1 homolog):

> Component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex, that regulates cytochrome c oxidase assembly. MITRAC complexes regulate both translation of mitochondrial encoded components and assembly of nuclear-encoded components imported in mitochondrion. Required for assembly of mitochondrial respiratory chain complex I and complex IV. As part of the MCIA complex, required for efficient assembly of the mitochondrial complex I.

**Summary**, from NCBI Gene [55744](https://www.ncbi.nlm.nih.gov/gene/55744):

> Involved in mitochondrial respiratory chain complex I assembly and mitochondrial respiratory chain complex IV assembly. Located in mitochondrial inner membrane. Part of mitochondrial complex I intermediate assembly complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21868) · Entrez [55744](https://www.ncbi.nlm.nih.gov/gene/55744) · UniProt [Q9GZY4](https://www.uniprot.org/uniprotkb/Q9GZY4) · Ensembl [ENSG00000106603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106603)

## Data

Gene col 2779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2779); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2779]; `tensor/DDL_lfc|DDL_z.npy` [2779]; `embed/gene_vectors.npy` [2779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2779 or target_col == 2779). Every well: [[COA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
