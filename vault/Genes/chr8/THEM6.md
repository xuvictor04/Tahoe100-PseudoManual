---
symbol: "THEM6"
type: "gene"
col: 5031
ensembl_id: "ENSG00000130193"
name: "thioesterase superfamily member 6"
location: "8q24.3"
module: 35
arm: "-"
pooled_cpm: 3.84
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# THEM6

*thioesterase superfamily member 6* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.54× (z +9.3, q 5e-18, up in 32 of 42 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.71× (z +5.3, q 9e-06, up in 16 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.456× (z -7.9, q 2e-12, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA7L]] (+0.70, fdr 7e-06), [[PAFAH1B3]] (+0.66, fdr 4e-05), [[SLC27A2]] (+0.61, fdr 2e-05); moves opposite to [[ZFHX2-AS1]] (-0.67, fdr 6e-05), [[ZNF213-AS1]] (-0.66, fdr 2e-04), [[AP4S1]] (-0.66, fdr 5e-05).
> It sits in the **-** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.54×** | +9.3 | 5e-18 | 32/42 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.50×** | +9.2 | 1e-17 | 31/44 (J82, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.46×** | +8.7 | 1e-15 | 3/5 (J82, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.82×** | +6.0 | 3e-07 | 24/42 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.77×** | +5.7 | 1e-06 | 8/18 (SW480, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +5.3 | 9e-06 | 16/43 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.3 | 1e-05 | 18/43 (HS-578T, J82, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +5.1 | 3e-05 | 8/22 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.43×** | +3.4 | 0.037 | 5/19 (SW480, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.45×** | +3.4 | 0.038 | 0/7 | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +3.3 | 0.057 | 3/38 (HS-578T, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5031.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -7.9 | 2e-12 | 30/45 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -6.6 | 2e-08 | 20/43 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -5.9 | 7e-07 | 18/33 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -5.8 | 1e-06 | 20/35 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.705×** | -5.0 | 6e-05 | 22/35 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.610×** | -5.0 | 6e-05 | 14/36 (SW1417, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -4.8 | 1e-04 | 17/39 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -4.8 | 1e-04 | 15/40 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.633×** | -4.6 | 3e-04 | 20/40 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.424×** | -4.5 | 4e-04 | 12/29 (KATO III, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.665×** | -4.1 | 0.002 | 12/38 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.006 | 16/37 (J82, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -3.5 | 0.019 | 13/37 (PANC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.030 | 13/41 (COLO 205, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.723×** | -3.3 | 0.041 | 11/39 (NCI-H2030, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0533× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 4.90 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 7.87 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0396× (z -12.9) |
| [[A-427 (line)]] | wt | 4.89 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0890× (z -8.9) |
| [[BT-474 (line)]] | alt | 5.02 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0720× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0729× (z -10.0) |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA7L]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PAFAH1B3]] | +0.66 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SLC27A2]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SMYD3]] | +0.61 | +0.37 / +0.40 | both halves | 8e-05 |  |
| [[PODXL2]] | +0.60 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[C20orf27]] | +0.60 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[NPM3]] | +0.60 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[CCDC88C]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SLC37A4]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[THYN1]] | +0.59 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[EXOSC5]] | +0.59 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[ANTKMT]] | +0.59 | +0.35 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2-AS1]] | -0.67 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ZNF213-AS1]] | -0.66 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[AP4S1]] | -0.66 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ZNF451-AS1]] | -0.65 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[NRSN2-AS1]] | -0.65 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[USP34-DT]] | -0.65 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[ZNF529-AS1]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[ANXA2R-OT1]] | -0.63 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SPATA1]] | -0.63 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ATE1OSP]] | -0.63 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[TBCE-1]] | -0.63 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[MCF2]] | -0.62 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers THEM6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers THEM6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (1.0, 21.7); signed map (-9.1, -57.7). **Vector** length 57.0, 8.38% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.0 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.0 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.7 | +6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.8 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.1 | +0.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | thioesterase superfamily member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:142,727,223-142,736,927 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DSCD75; previously C8orf55 |
| Gene groups (HGNC) | Thioesterase superfamily |
| Matched by | ensembl_id |

UniProt [Q8WUY1](https://www.uniprot.org/uniprotkb/Q8WUY1) carries no function annotation.

**Summary**, from NCBI Gene [51337](https://www.ncbi.nlm.nih.gov/gene/51337):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29656) · Entrez [51337](https://www.ncbi.nlm.nih.gov/gene/51337) · UniProt [Q8WUY1](https://www.uniprot.org/uniprotkb/Q8WUY1) · Ensembl [ENSG00000130193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130193)

## Data

Gene col 5031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5031); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5031]; `tensor/DDL_lfc|DDL_z.npy` [5031]; `embed/gene_vectors.npy` [5031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5031 or target_col == 5031). Every well: [[THEM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THEM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
