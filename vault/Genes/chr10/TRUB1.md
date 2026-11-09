---
symbol: "TRUB1"
type: "gene"
col: 9196
ensembl_id: "ENSG00000165832"
name: "TruB pseudouridine synthase family member 1"
location: "10q25.3"
module: 28
arm: "+"
pooled_cpm: 17.89
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TRUB1

*TruB pseudouridine synthase family member 1* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.64× (z +12.2, q 3e-31, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.650× (z -7.6, q 2e-11, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBBP9]] (+0.74, fdr 7e-06), [[GUF1]] (+0.72, fdr 7e-06), [[SMARCE1]] (+0.71, fdr 7e-06); moves opposite to [[MAPKAPK2]] (-0.64, fdr 7e-06), [[WNT2B]] (-0.64, fdr 1e-05), [[RABGEF1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +12.2 | 3e-31 | 40/48 (NCI-H460, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.3 | 2e-14 | 31/47 (A-427, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.3 | 3e-14 | 22/41 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +7.4 | 2e-11 | 27/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.0 | 3e-10 | 28/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.8 | 1e-09 | 22/47 (RKO, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +6.7 | 2e-09 | 23/48 (A-427, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +6.2 | 3e-08 | 28/48 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.7 | 9e-07 | 16/36 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 6e-05 | 16/48 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.5 | 4e-04 | 15/31 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 6e-04 | 12/47 (SW480, C32, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 6/47 (LOX-IMVI, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.003 | 19/46 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.004 | 5/46 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.011 | 8/46 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.028 | 5/47 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.028 | 5/48 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -7.6 | 2e-11 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -6.8 | 4e-09 | 26/46 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -6.1 | 2e-07 | 23/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -4.6 | 6e-04 | 21/48 (NCI-H23, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.771×** | -4.6 | 6e-04 | 18/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.648×** | -4.0 | 0.006 | 12/46 (Hs 766T, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -3.6 | 0.028 | 11/48 (SW480, A-172, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.840× | -3.1 | 0.13 | 11/47 (SW 900, HT-29, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.13 | 12/46 (HOP62, CHP-212, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.885× | -3.0 | 0.13 | 6/48 (NCI-H460, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.0924× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.289× (z -10.9) |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -10.4) |
| [[A-172 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.97× (z +10.1) | — |
| [[A498 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.41× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0720× (z -8.9) |
| [[KATO III (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -12.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0828× (z -8.6) ⚠ toxic |
| [[RKO (line)]] | wt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.8) | — |
| [[A549 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP9]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[GUF1]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[MRPL9]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 | STRING 462 |
| [[MRS2]] | +0.69 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[POMK]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.68 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[PTCD2]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[COX11]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | -0.64 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[WNT2B]] | -0.64 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.64 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[TTLL3]] | -0.61 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[HIC2]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.60 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.59 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.59 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[CYTH1]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PITPNA]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ELL]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TRUB1's level | compounds that target MAP2K1: 3 of 4 raise it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[ZNF391]] | B | ZNF391 activity raises TRUB1's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 1.25× lower at baseline in the lines without ZNF391 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity raises TRUB1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.42× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.7, 3.3); signed map (5.9, -31.9). **Vector** length 92.1, 18.6% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.5 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +4.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | TruB pseudouridine synthase family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:114,938,195-114,977,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PUS4 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWH5](https://www.uniprot.org/uniprotkb/Q8WWH5) (Pseudouridylate synthase TRUB1):

> Pseudouridine synthase that catalyzes pseudouridylation of mRNAs and tRNAs. Mediates pseudouridylation of mRNAs with the consensus sequence 5'-GUUCNANNC-3', harboring a stem-loop structure. Constitutes the major pseudouridine synthase acting on mRNAs. Also catalyzes pseudouridylation of some tRNAs, including synthesis of pseudouridine(55) from uracil-55, in the psi GC loop of a subset of tRNAs. Promotes the processing of pri-let-7 microRNAs (pri-miRNAs) independently of its RNA pseudouridylate …

**Summary**, from NCBI Gene [142940](https://www.ncbi.nlm.nih.gov/gene/142940):

> Pseudouridine is an abundant component of rRNAs and tRNAs and is enzymatically generated by isomerization of uridine by pseudouridine synthase (Zucchini et al., 2003 [PubMed 12736709]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16060) · Entrez [142940](https://www.ncbi.nlm.nih.gov/gene/142940) · UniProt [Q8WWH5](https://www.uniprot.org/uniprotkb/Q8WWH5) · Ensembl [ENSG00000165832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165832)

## Data

Gene col 9196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9196); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9196]; `tensor/DDL_lfc|DDL_z.npy` [9196]; `embed/gene_vectors.npy` [9196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9196 or target_col == 9196). Every well: [[TRUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
