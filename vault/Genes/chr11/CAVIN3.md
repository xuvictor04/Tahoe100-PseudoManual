---
symbol: "CAVIN3"
type: "gene"
col: 10033
ensembl_id: "ENSG00000170955"
name: "caveolae associated protein 3"
location: "11p15.4"
module: 12
arm: "+"
pooled_cpm: 7.55
n_lines_expressing: 27
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CAVIN3

*caveolae associated protein 3* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +5.7, q 7e-06, up in 17 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Carbamazepine (drug)]] 5 µM: 1.83× (z +3.6, q 0.040, up in 15 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.194× (z -9.7, q 1e-19, down in 23 of 25 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMP3]] (+0.52, fdr 2e-04), [[CBR3]] (+0.52, fdr 3e-04), [[APOBEC3G]] (+0.51, fdr 8e-05); moves opposite to [[CPNE7]] (-0.48, fdr 1e-04), [[CPSF6]] (-0.46, fdr 2e-04), [[EML3]] (-0.46, fdr 4e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +5.7 | 7e-06 | 17/21 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +4.6 | 0.001 | 8/15 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.11×** | +4.4 | 0.002 | 15/20 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +3.7 | 0.032 | 6/18 (A498, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | **1.83×** | +3.6 | 0.040 | 15/25 (hTERT-HPNE, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.194×** | -9.7 | 1e-19 | 23/25 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.215×** | -9.1 | 2e-17 | 23/25 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.230×** | -8.7 | 5e-16 | 24/25 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.234×** | -8.6 | 1e-15 | 24/25 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.300×** | -7.1 | 1e-10 | 18/25 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.315×** | -6.9 | 7e-10 | 23/25 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.451×** | -6.7 | 2e-09 | 20/23 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.426×** | -5.0 | 5e-05 | 18/25 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.450×** | -4.7 | 1e-04 | 20/25 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -4.5 | 4e-04 | 16/23 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.235×** | -3.9 | 0.005 | 18/25 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.523×** | -3.8 | 0.006 | 17/24 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -3.7 | 0.010 | 13/23 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.278×** | -3.5 | 0.022 | 14/23 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.564×** | -3.4 | 0.026 | 11/25 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.582×** | -3.2 | 0.044 | 15/25 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -3.1 | 0.052 | 12/23 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.87 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 13.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0308× (z -15.2) |
| [[SW480 (line)]] | alt | 16.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0780× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0922× (z -10.1) |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -9.0) |
| [[J82 (line)]] | alt | 12.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -8.9) |
| [[Hs 766T (line)]] | wt | 20.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -8.5) |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0312× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 7.43 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0553× (z -8.9) |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.112× (z -8.8) |
| [[A-172 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMP3]] | +0.52 | +0.30 / +0.64 | both halves | 2e-04 |  |
| [[CBR3]] | +0.52 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[APOBEC3G]] | +0.51 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[C2orf74]] | +0.51 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[MED7]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[KIFBP]] | +0.50 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[PPP1R12A]] | +0.49 | +0.26 / +0.62 | both halves | 4e-04 |  |
| [[SNAPIN]] | +0.49 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[EID2]] | +0.48 | +0.22 / +0.54 | both halves | 6e-04 |  |
| [[ASF1A]] | +0.48 | +0.29 / +0.48 | both halves | 2e-04 |  |
| [[NSMCE3]] | +0.48 | +0.23 / +0.49 | both halves | 5e-04 |  |
| [[MDP1]] | +0.48 | +0.25 / +0.49 | both halves | 4e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE7]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[CPSF6]] | -0.46 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[EML3]] | -0.46 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[AHCY]] | -0.46 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[PABPC4]] | -0.45 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[SEH1L]] | -0.45 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[SMG1P3]] | -0.44 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[MRPS25]] | -0.44 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[TBCD]] | -0.43 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[NUP210]] | -0.42 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[TBC1D16]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[MTA1]] | -0.42 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity lowers CAVIN3's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 3.09× higher at baseline in the lines without NUP210 | 0.081 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[APOBEC3G]] | C | APOBEC3G activity raises CAVIN3's level | lines that do not express APOBEC3G (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without APOBEC3G | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC02813, PTX3, PDLIM3; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-12.8, -57.1); signed map (-3.2, -18.1). **Vector** length 47.0, 11.9% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.3 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | caveolae associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,318,946-6,320,532 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRBC, HSRBC, MGC20400, cavin-3; previously PRKCDBP |
| Gene groups (HGNC) | Cavins |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969G5](https://www.uniprot.org/uniprotkb/Q969G5) (Caveolae-associated protein 3):

> Regulates the traffic and/or budding of caveolae. Plays a role in caveola formation in a tissue-specific manner. Required for the formation of caveolae in smooth muscle but not in the lung and heart endothelial cells. Regulates the equilibrium between cell surface-associated and cell surface-dissociated caveolae by promoting the rapid release of caveolae from the cell surface. Plays a role in the regulation of the circadian clock. Modulates the period length and phase of circadian gene …

**Summary**, from NCBI Gene [112464](https://www.ncbi.nlm.nih.gov/gene/112464):

> The protein encoded by this gene was identified as a binding protein of the protein kinase C, delta (PRKCD). The expression of this gene in cultured cell lines is strongly induced by serum starvation. The expression of this protein was found to be down-regulated in various cancer cell lines, suggesting the possible tumor suppressor function of this protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9400) · Entrez [112464](https://www.ncbi.nlm.nih.gov/gene/112464) · UniProt [Q969G5](https://www.uniprot.org/uniprotkb/Q969G5) · Ensembl [ENSG00000170955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170955)

## Data

Gene col 10033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10033); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10033]; `tensor/DDL_lfc|DDL_z.npy` [10033]; `embed/gene_vectors.npy` [10033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10033 or target_col == 10033). Every well: [[CAVIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAVIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
