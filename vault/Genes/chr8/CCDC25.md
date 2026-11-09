---
symbol: "CCDC25"
type: "gene"
col: 7181
ensembl_id: "ENSG00000147419"
name: "coiled-coil domain containing 25"
location: "8p21.1"
module: 28
arm: "+"
pooled_cpm: 34.9
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CCDC25

*coiled-coil domain containing 25* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +12.4, q 1e-32, up in 44 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.44× (z +4.8, q 2e-04, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.467× (z -10.0, q 9e-21, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCE1]] (+0.80, fdr 7e-06), [[RAD50]] (+0.75, fdr 7e-06), [[RNF214]] (+0.74, fdr 7e-06); moves opposite to [[TPST2]] (-0.63, fdr 1e-05), [[CD81]] (-0.61, fdr 2e-05), [[SLC27A4]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +12.4 | 1e-32 | 44/46 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +11.7 | 6e-29 | 36/39 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +7.3 | 5e-11 | 30/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.47×** | +5.1 | 5e-05 | 33/46 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 2e-04 | 30/48 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.008 | 23/48 (A-172, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.021 | 26/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +3.3 | 0.060 | 21/48 (A-172, NCI-H1573, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.2 | 0.095 | 20/48 (NCI-H2347, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.10 | 19/48 (Hs 766T, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.26× | +3.0 | 0.14 | 20/48 (A-172, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.467×** | -10.0 | 9e-21 | 45/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -8.7 | 7e-16 | 44/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -8.5 | 3e-15 | 41/46 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -7.3 | 3e-11 | 38/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -5.8 | 6e-07 | 32/47 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -5.5 | 3e-06 | 34/48 (SNU-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -4.4 | 7e-04 | 30/48 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.706×** | -4.1 | 0.003 | 23/48 (AN3 CA, KATO III, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.617×** | -3.3 | 0.060 | 19/47 (NCI-H2347, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +12.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -11.0) |
| [[A498 (line)]] | wt | 26.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.279× (z -10.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 32.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +12.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.319× (z -9.9) |
| [[A-427 (line)]] | wt | 50.9 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.112× (z -10.1) |
| [[A549 (line)]] | wt | 37.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +12.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 58.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 49.7 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.372× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 66.9 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.336× (z -9.2) |
| [[A-172 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0570× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 46.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0841× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCE1]] | +0.80 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[RAD50]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[RNF214]] | +0.74 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.72 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 | STRING 475 |
| [[NDUFA5]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[SLC25A46]] | +0.70 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[DDX1]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PEX1]] | +0.69 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[SUPT20H]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SEPSECS]] | +0.67 | +0.78 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.63 | -0.79 / -0.57 | both halves | 1e-05 |  |
| [[CD81]] | -0.61 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[SLC27A4]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MBOAT7]] | -0.58 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CCDC25's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.864). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.6, 3.8); signed map (7.1, -25.8). **Vector** length 72.4, 16.6% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.4 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.5 | -0.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | +0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:27,733,316-27,772,653 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10853 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WR0](https://www.uniprot.org/uniprotkb/Q86WR0) (Coiled-coil domain-containing protein 25):

> Transmembrane receptor that senses neutrophil extracellular traps (NETs) and triggers the ILK-PARVB pathway to enhance cell motility. NETs are mainly composed of DNA fibers and are released by neutrophils to bind pathogens during inflammation. Formation of NETs is also associated with cancer metastasis, NET-DNA acting as a chemotactic factor to attract cancer cells. Specifically binds NETs on its extracellular region, in particular the 8-OHdG-enriched DNA present in NETs, and recruits ILK, …

**Summary**, from NCBI Gene [55246](https://www.ncbi.nlm.nih.gov/gene/55246):

> Enables DNA binding activity. Involved in positive regulation of cell motility. Located in endomembrane system and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25591) · Entrez [55246](https://www.ncbi.nlm.nih.gov/gene/55246) · UniProt [Q86WR0](https://www.uniprot.org/uniprotkb/Q86WR0) · Ensembl [ENSG00000147419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147419)

## Data

Gene col 7181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7181); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7181]; `tensor/DDL_lfc|DDL_z.npy` [7181]; `embed/gene_vectors.npy` [7181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7181 or target_col == 7181). Every well: [[CCDC25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
