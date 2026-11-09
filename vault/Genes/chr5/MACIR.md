---
symbol: "MACIR"
type: "gene"
col: 11210
ensembl_id: "ENSG00000181751"
name: "macrophage immunometabolism regulator"
location: "5q21.1"
module: 146
arm: "+"
pooled_cpm: 18.15
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# MACIR

*macrophage immunometabolism regulator* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.58× (z +7.4, q 8e-11, up in 26 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.40× (z +5.7, q 3e-06, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.709× (z -5.8, q 4e-06, down in 21 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.589× (z -4.7, q 6e-04, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHCTF1]] (+0.65, fdr 1e-05), [[DYNC1LI1]] (+0.62, fdr 1e-05), [[SYBU]] (+0.59, fdr 8e-06); moves opposite to [[ATP6V1D]] (-0.59, fdr 1e-05), [[ENDOV]] (-0.52, fdr 2e-05), [[ENSA]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM131L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +7.4 | 8e-11 | 26/41 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.7 | 3e-06 | 19/45 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.3 | 2e-05 | 19/42 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 2e-05 | 18/44 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +5.2 | 2e-05 | 19/45 (A-427, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 1e-04 | 21/44 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.3 | 0.001 | 16/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 17/44 (HOP62, C32, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 0.001 | 11/45 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.0 | 0.004 | 11/46 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.005 | 10/42 (NCI-H460, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.007 | 11/46 (SK-MEL-2, C32, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.009 | 8/45 (A-172, C-33 A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +3.6 | 0.013 | 12/43 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.016 | 6/44 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.041 | 7/43 (A549, SHP-77, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.058 | 13/45 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.064 | 10/45 (LoVo, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -5.8 | 4e-06 | 21/44 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.0 | 2e-04 | 19/37 (SW1417, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.589×** | -4.7 | 6e-04 | 20/44 (H4, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.807×** | -3.6 | 0.034 | 13/44 (RPMI-7951, A549, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.808×** | -3.6 | 0.034 | 16/45 (J82, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.809×** | -3.5 | 0.053 | 13/27 (A-172, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.074 | 17/45 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 43.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -13.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 20.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.195× (z -8.9) |
| [[LS 180 (line)]] | wt | 27.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.10× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 7.83 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0561× (z -10.1) |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCTF1]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[DYNC1LI1]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SYBU]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[CSNK1G3]] | +0.58 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[RPP40]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[NOD1]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ABCC4]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TMEM131L]] | +0.54 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[TADA1]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[MCMBP]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[GPR63]] | +0.52 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[PMS1]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ENDOV]] | -0.52 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ENSA]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ARMH4]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CYTH2]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZSWIM4]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[WDR26]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[YIPF6]] | -0.45 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CD63]] | -0.45 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ATG2A]] | -0.45 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[ASPHD1]] | -0.45 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[STX5]] | -0.44 | -0.53 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM131L]] | C | TMEM131L activity raises MACIR's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.2, -7.1); signed map (-35.8, -17.8). **Vector** length 96.1, 21.2% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.5 | +7.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +5.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.2 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -0.7 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | macrophage immunometabolism regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:103,258,763-103,278,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25291; previously C5orf30 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GV9](https://www.uniprot.org/uniprotkb/Q96GV9) (Macrophage immunometabolism regulator):

> Regulates the macrophage function, by enhancing the resolution of inflammation and wound repair functions mediated by M2 macrophages. The regulation of macrophage function is, due at least in part, to its ability to inhibit glycolysis. May also play a role in trafficking of proteins via its interaction with UNC119 and UNC119B cargo adapters: may help the release of UNC119 and UNC119B cargo or the recycling of UNC119 and UNC119B. May play a role in ciliary membrane localization via its …

**Summary**, from NCBI Gene [90355](https://www.ncbi.nlm.nih.gov/gene/90355):

> This gene, MACIR (previously known as C5orf30), has been associated with rheumatoid arthritis, functioning as a negative regulator of tissue damage and modulating the activity of synovial fibroblasts and macrophages. The encoded protein is highly conserved in vertebrate genomes but has no significant similarity to any other human protein. [provided by RefSeq, Dec 2019]

**Accessions** — [HGNC:25052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25052) · Entrez [90355](https://www.ncbi.nlm.nih.gov/gene/90355) · UniProt [Q96GV9](https://www.uniprot.org/uniprotkb/Q96GV9) · Ensembl [ENSG00000181751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181751)

## Data

Gene col 11210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11210); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11210]; `tensor/DDL_lfc|DDL_z.npy` [11210]; `embed/gene_vectors.npy` [11210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11210 or target_col == 11210). Every well: [[MACIR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACIR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
