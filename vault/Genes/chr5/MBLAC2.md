---
symbol: "MBLAC2"
type: "gene"
col: 10676
ensembl_id: "ENSG00000176055"
name: "metallo-beta-lactamase domain containing 2"
location: "5q14.3"
module: 28
arm: "+"
pooled_cpm: 5.35
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MBLAC2

*metallo-beta-lactamase domain containing 2* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +10.3, q 6e-22, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.382× (z -9.7, q 2e-19, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED8]] (+0.61, fdr 7e-06), [[KLHL11]] (+0.59, fdr 1e-05), [[KCTD18]] (+0.59, fdr 2e-05); moves opposite to [[UBE2M]] (-0.56, fdr 2e-05), [[FRMD8]] (-0.51, fdr 4e-05), [[NECTIN2]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF391]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +10.3 | 6e-22 | 38/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +9.1 | 3e-17 | 39/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.9 | 1e-16 | 29/42 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.76×** | +8.0 | 2e-13 | 27/47 (A-427, SW480, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **2.03×** | +7.1 | 1e-10 | 29/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +6.9 | 5e-10 | 26/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.5 | 3e-06 | 19/47 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.2 | 1e-05 | 23/40 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 15/42 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.26×** | +4.3 | 0.001 | 7/45 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.002 | 15/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.005 | 15/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.44×** | +3.7 | 0.011 | 4/44 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.032 | 15/43 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.41×** | +3.3 | 0.036 | 10/27 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.038 | 5/47 (SK-MEL-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.041 | 5/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.059 | 8/47 (SW480, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.382×** | -9.7 | 2e-19 | 33/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.421×** | -8.7 | 1e-15 | 30/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -7.9 | 6e-13 | 28/40 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.504×** | -6.9 | 8e-10 | 31/46 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.509×** | -6.8 | 1e-09 | 24/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.517×** | -6.6 | 3e-09 | 25/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.572×** | -5.3 | 9e-06 | 20/43 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -5.1 | 3e-05 | 16/34 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.641×** | -4.5 | 5e-04 | 16/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -3.9 | 0.006 | 15/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.717×** | -3.2 | 0.069 | 9/45 (C32, C-33 A, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.650×** | -3.1 | 0.094 | 10/39 (NCI-H1573, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.16 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0704× (z -14.6) |
| [[A498 (line)]] | wt | 6.49 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -8.7) |
| [[J82 (line)]] | alt | 5.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.77 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0651× (z -9.7) |
| [[SHP-77 (line)]] | alt | 8.21 | 0 | 1 | — | [[Olanzapine (drug)]] 0.5 µM 0.0808× (z -8.5) |
| [[SNU-423 (line)]] | alt | 6.73 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0730× (z -10.8) |
| [[SW480 (line)]] | alt | 6.18 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -9.4) |
| [[A-172 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED8]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[KLHL11]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.59 | +0.67 / +0.49 | both halves | 2e-05 |  |
| [[OSGEPL1]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PCMTD1-DT]] | +0.58 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[MTPAP]] | +0.58 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[ERMARD]] | +0.56 | +0.62 / +0.37 | both halves | 7e-05 |  |
| [[ZNF391]] | +0.56 | +0.65 / +0.38 | both halves | 7e-05 |  |
| [[CYP4V2]] | +0.56 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[FAM120C]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ZNF25]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[DIS3L]] | +0.54 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2M]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[FRMD8]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[NECTIN2]] | -0.50 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.50 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[SAMD4B]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[VRK3]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[POMP]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CLEC16A]] | -0.48 | -0.18 / -0.37 | ⚠ not reproduced | 0.001 |  |
| [[RAB5IF]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[WNT2B]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CYTH1]] | -0.47 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[NDUFA11]] ⚠ | -0.47 | -0.42 / -0.33 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CHMP1A]] | -0.47 | -0.26 / -0.51 | both halves | 3e-04 |  |
| [[NEDD8]] | -0.47 | -0.52 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF391]] | B | ZNF391 activity raises MBLAC2's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without ZNF391 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.0, 19.3); signed map (9.4, -39.8). **Vector** length 58.7, 8.53% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.4 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -6.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | metallo-beta-lactamase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:90,458,209-90,474,771 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686P15118, MGC46734 |
| Gene groups (HGNC) | MBL domain containing glyoxalase 2 subfamily; Thioester hydrolases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68D91](https://www.uniprot.org/uniprotkb/Q68D91) (Acyl-coenzyme A thioesterase MBLAC2):

> Acyl-CoA thioesterases are a group of enzymes that catalyze the hydrolysis of acyl-CoAs to the free fatty acid and coenzyme A (CoASH), providing the potential to regulate intracellular levels of acyl-CoAs, free fatty acids and CoASH. Has an acyl-CoA thioesterase activity towards the long chain fatty acyl-CoA thioester palmitoyl-CoA (hexadecanoyl-CoA; C16:0-CoA). Displays a substrate preference for fatty acyl-CoAs with chain-lengths C12-C18. Possesses beta-lactamase activity, catalyzing the …

**Summary**, from NCBI Gene [153364](https://www.ncbi.nlm.nih.gov/gene/153364):

> Enables beta-lactamase activity and long-chain fatty acyl-CoA hydrolase activity. Predicted to be involved in fatty acid metabolic process. Located in endoplasmic reticulum membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33711) · Entrez [153364](https://www.ncbi.nlm.nih.gov/gene/153364) · UniProt [Q68D91](https://www.uniprot.org/uniprotkb/Q68D91) · Ensembl [ENSG00000176055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176055)

## Data

Gene col 10676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10676); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10676]; `tensor/DDL_lfc|DDL_z.npy` [10676]; `embed/gene_vectors.npy` [10676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10676 or target_col == 10676). Every well: [[MBLAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBLAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
