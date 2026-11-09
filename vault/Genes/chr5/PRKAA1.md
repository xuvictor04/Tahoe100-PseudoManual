---
symbol: "PRKAA1"
type: "gene"
col: 5304
ensembl_id: "ENSG00000132356"
name: "protein kinase AMP-activated catalytic subunit alpha 1"
location: "5p13.1"
module: 17
arm: "+"
pooled_cpm: 81.9
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PRKAA1

*protein kinase AMP-activated catalytic subunit alpha 1* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +11.0, q 3e-25, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.597× (z -11.0, q 3e-25, down in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.697× (z -7.7, q 4e-12, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAPA]] (+0.60, fdr 1e-05), [[SAAL1]] (+0.59, fdr 8e-06), [[MTPAP]] (+0.58, fdr 1e-05); moves opposite to [[MROH1]] (-0.63, fdr 4e-05), [[NPIPB11]] (-0.60, fdr 1e-05), [[RABGEF1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +11.0 | 3e-25 | 38/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +10.0 | 4e-21 | 42/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 9e-09 | 36/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 6e-06 | 32/49 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.19× | +4.9 | 1e-04 | 17/48 (HOP62, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.5 | 5e-04 | 19/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.010 | 23/48 (C32, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.011 | 20/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.018 | 17/38 (SK-MEL-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.029 | 18/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.069 | 20/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.084 | 16/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.084 | 14/49 (J82, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.597×** | -11.0 | 3e-25 | 36/49 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -9.7 | 1e-19 | 33/43 (SW48, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -7.7 | 4e-12 | 34/48 (SW 900, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -7.0 | 5e-10 | 33/49 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.9 | 5e-07 | 29/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.769×** | -5.2 | 2e-05 | 24/45 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.817×** | -4.1 | 0.003 | 25/50 (LS 180, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -3.8 | 0.012 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.17 | 15/48 (SW 1088, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 78.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.542× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.0) | — |
| [[A549 (line)]] | wt | 72.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.6) |
| [[BT-474 (line)]] | alt | 86.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.6) |
| [[LS 180 (line)]] | wt | 63.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -11.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.434× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.1) |
| [[KATO III (line)]] | alt | 59.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.2) |
| [[LoVo (line)]] | wt | 63.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 70.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 65.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0898× (z -9.6) |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.122× (z -9.5) |
| [[SW 900 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 91.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAPA]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.59 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[MTPAP]] | +0.58 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.58 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ZNF45]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[C2CD5]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[EXOSC9]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[KBTBD6]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[GEMIN2]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SMG7]] | +0.54 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CHIC1]] | +0.52 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MROH1]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[NPIPB11]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.59 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[SENP5]] | -0.55 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[DNHD1]] | -0.54 | -0.37 / -0.62 | both halves | 9e-05 |  |
| [[VPS53]] | -0.53 | -0.36 / -0.62 | both halves | 9e-05 |  |
| [[PHKG1]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SMG1P6]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GLYR1]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[NPIPB12]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DRD4]] | -0.50 | -0.39 / -0.62 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRKAA1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-17.3, -0.0); signed map (-22.8, -16.2). **Vector** length 99.9, 25.1% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +5.0 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +11.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -4.0 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase AMP-activated catalytic subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:40,759,389-40,798,374 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AMPKa1 |
| Gene groups (HGNC) | Protein kinase AMP-activated catalytic subunit alpha family |
| Reactome | 23 pathways, smallest: AMP and AMPK regulate the circadian clock; Activation of AMPK downstream of NMDARs; Energy dependent regulation of mTOR by LKB1-AMPK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13131](https://www.uniprot.org/uniprotkb/Q13131) (5'-AMP-activated protein kinase catalytic subunit alpha-1):

> Catalytic subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation of …

**Summary**, from NCBI Gene [5562](https://www.ncbi.nlm.nih.gov/gene/5562):

> The protein encoded by this gene belongs to the ser/thr protein kinase family. It is the catalytic subunit of the 5'-prime-AMP-activated protein kinase (AMPK). AMPK is a cellular energy sensor conserved in all eukaryotic cells. The kinase activity of AMPK is activated by the stimuli that increase the cellular AMP/ATP ratio. AMPK regulates the activities of a number of key metabolic enzymes through phosphorylation. It protects cells from stresses that cause ATP depletion by switching off …

**Accessions** — [HGNC:9376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9376) · Entrez [5562](https://www.ncbi.nlm.nih.gov/gene/5562) · UniProt [Q13131](https://www.uniprot.org/uniprotkb/Q13131) · Ensembl [ENSG00000132356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132356)

## Data

Gene col 5304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5304); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5304]; `tensor/DDL_lfc|DDL_z.npy` [5304]; `embed/gene_vectors.npy` [5304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5304 or target_col == 5304). Every well: [[PRKAA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
