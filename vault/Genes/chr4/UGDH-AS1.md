---
symbol: "UGDH-AS1"
type: "gene"
col: 14606
ensembl_id: "ENSG00000249348"
name: "UGDH antisense RNA 1"
location: "4p14"
module: 23
arm: "+"
pooled_cpm: 14.39
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 14
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# UGDH-AS1

*UGDH antisense RNA 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +11.1, q 1e-25, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.540× (z -9.1, q 4e-17, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.645× (z -6.5, q 1e-08, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX59-AS1]] (+0.76, fdr 7e-06), [[EPM2A-DT]] (+0.76, fdr 7e-06), [[OXA1L-DT]] (+0.75, fdr 7e-06); moves opposite to [[RGS19]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DPH6-DT]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.1 | 1e-25 | 37/45 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +9.9 | 1e-20 | 20/33 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +9.5 | 3e-19 | 25/38 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +6.4 | 2e-08 | 28/48 (KATO III, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.2 | 6e-08 | 17/27 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.9 | 3e-07 | 4/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +4.9 | 8e-05 | 13/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.6 | 3e-04 | 17/46 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +4.5 | 4e-04 | 18/48 (SW480, HOP62, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 5e-04 | 13/47 (A-427, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 15/45 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 11/48 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +3.8 | 0.006 | 14/48 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.006 | 14/47 (LS 180, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 11/47 (SW480, CHP-212, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.015 | 5/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.015 | 10/47 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.015 | 15/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.016 | 5/47 (NCI-H2030, NCI-H661, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.016 | 8/47 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.540×** | -9.1 | 4e-17 | 32/48 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.619×** | -7.1 | 3e-10 | 25/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.629×** | -6.9 | 1e-09 | 26/46 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.645×** | -6.5 | 1e-08 | 28/47 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -5.7 | 1e-06 | 21/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.690×** | -5.3 | 1e-05 | 20/42 (PANC-1, SNU-423, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -5.1 | 3e-05 | 20/43 (HOP62, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -4.9 | 6e-05 | 20/48 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.551×** | -4.6 | 2e-04 | 14/44 (C32, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.736×** | -4.6 | 3e-04 | 17/47 (SW48, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.755×** | -3.9 | 0.004 | 17/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Methotrexate (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.037 | 2/48 (SW 1271, SW 1088) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.079 | 8/47 (KATO III, SW48, …) | top dose only | plate-row cell shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.079 | 3/48 (KATO III, NCI-H1792, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.085 | 3/48 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 28.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0564× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.77× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0647× (z -10.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX59-AS1]] | +0.76 | +0.80 / +0.61 | both halves | 7e-06 | same gene group |
| [[EPM2A-DT]] | +0.76 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.75 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[COPB2-DT]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[HEXIM2-AS1]] | +0.73 | +0.77 / +0.57 | both halves | 1e-05 | same gene group |
| [[DNAJC27-AS1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 | same gene group |
| [[CHD1-DT]] | +0.72 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[TMEM9B-AS1]] | +0.72 | +0.78 / +0.48 | both halves | 2e-05 | same gene group |
| [[CYB5D2]] | +0.71 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[INTS6-AS1]] | +0.70 | +0.75 / +0.53 | both halves | 1e-05 | same gene group |
| [[ITFG2-AS1]] | +0.70 | +0.78 / +0.50 | both halves | 1e-05 | same gene group |
| [[ENTPD3-AS1]] | +0.69 | +0.70 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS19]] | -0.58 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPH6-DT]] | C | DPH6-DT activity raises UGDH-AS1's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 1.41× lower at baseline in the lines without DPH6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.6, 19.1); signed map (30.2, -7.4). **Vector** length 76.2, 14.0% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +4.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | UGDH antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p14 — chr4:39,527,720-39,594,707 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40601) · Entrez [100885776](https://www.ncbi.nlm.nih.gov/gene/100885776) · Ensembl [ENSG00000249348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249348)

## Data

Gene col 14606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14606); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14606]; `tensor/DDL_lfc|DDL_z.npy` [14606]; `embed/gene_vectors.npy` [14606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14606 or target_col == 14606). Every well: [[UGDH-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGDH-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
