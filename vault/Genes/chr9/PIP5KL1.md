---
symbol: "PIP5KL1"
type: "gene"
col: 9414
ensembl_id: "ENSG00000167103"
name: "phosphatidylinositol-4-phosphate 5-kinase like 1"
location: "9q34.11"
module: 47
arm: "+"
pooled_cpm: 4.56
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# PIP5KL1

*phosphatidylinositol-4-phosphate 5-kinase like 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.25× (z +9.1, q 7e-17, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.411× (z -9.5, q 5e-19, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6-1]] (+0.70, fdr 8e-06, ⚠ same locus), [[FERMT3]] (+0.68, fdr 7e-06), [[ATP2A1]] (+0.66, fdr 7e-06), [[LHX4]] (+0.66, fdr 8e-06); moves opposite to [[NHLRC2]] (-0.58, fdr 4e-05), [[SEPSECS]] (-0.58, fdr 3e-05), [[ZNF214]] (-0.57, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +9.1 | 7e-17 | 28/44 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +8.0 | 5e-13 | 23/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +7.9 | 5e-13 | 26/46 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.4 | 3e-08 | 15/37 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +5.7 | 1e-06 | 14/44 (SW1417, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +5.4 | 6e-06 | 14/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.2 | 2e-05 | 13/45 (HOP62, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.56×** | +4.7 | 1e-04 | 6/23 (NCI-H460, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.0 | 0.004 | 9/45 (LoVo, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.005 | 8/43 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.007 | 14/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.021 | 4/31 (NCI-H23, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.022 | 11/39 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.4 | 0.025 | 2/9 (HOP62, NCI-H2347) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.1 | 0.078 | 6/45 (BT-474, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.411×** | -9.5 | 5e-19 | 27/42 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.426×** | -9.5 | 5e-19 | 28/44 (KATO III, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -6.3 | 7e-08 | 16/34 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -5.2 | 3e-05 | 19/45 (KATO III, A-427, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.631×** | -5.1 | 3e-05 | 18/42 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.674×** | -4.4 | 0.001 | 18/36 (BT-474, Hs 766T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -4.3 | 0.001 | 14/44 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -4.2 | 0.002 | 19/46 (BT-474, KATO III, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.681×** | -4.1 | 0.002 | 12/41 (NCI-H1792, LoVo, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.814×** | -3.3 | 0.064 | 12/36 (BT-474, NCI-H2347, …) | all doses, flat | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.740×** | -3.2 | 0.064 | 11/40 (A-172, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.064 | 10/45 (LoVo, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.9 | 0 | 7 (3 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0455× (z -11.9) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0544× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0913× (z -8.6) |
| [[KATO III (line)]] | alt | 9.34 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0661× (z -11.7) |
| [[LoVo (line)]] | wt | 5.67 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0883× (z -10.5) |
| [[RKO (line)]] | wt | 9.95 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0455× (z -12.2) |
| [[SNU-423 (line)]] | alt | 3.81 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0372× (z -10.3) |
| [[A-172 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6-1]] | +0.70 | +0.57 / +0.71 | both halves | 8e-06 | ⚠ same locus (14.9 kb, same strand: neighbours can correlate without regulation) |
| [[FERMT3]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.66 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[LHX4]] | +0.66 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[UCKL1-AS1]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.63 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[IL20RB]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[FER1L4]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NECAB2]] | +0.62 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[PYGM]] | +0.61 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.58 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[SEPSECS]] | -0.58 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[ZNF214]] | -0.57 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[CASD1]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[CEPT1]] | -0.55 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[NFYB]] | -0.55 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[SCAF11]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CLK4]] | -0.54 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[WASHC3]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[COQ9]] | -0.54 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[PHC3]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[STXBP3]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.4, -20.1); signed map (14.9, 15.2). **Vector** length 68.8, 10.4% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.2 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4-phosphate 5-kinase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:127,920,881-127,930,785 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA203J24.5, MGC46424, PIPKH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T9C9](https://www.uniprot.org/uniprotkb/Q5T9C9) (Phosphatidylinositol 4-phosphate 5-kinase-like protein 1):

> Likely functions as a regulatory or scaffold-like protein that modulates the subcellular localization and activity of type I PI(4)P 5-kinases (PIPKs) (By similarity). Lacks intrinsic lipid kinase activity (By similarity).

**Summary**, from NCBI Gene [138429](https://www.ncbi.nlm.nih.gov/gene/138429):

> PIP5KL1 is a phosphoinositide kinase-like protein that lacks intrinsic lipid kinase activity but associates with type I PIPKs (see PIP5K1A; MIM 603275) and may play a role in localization of PIPK activity (Chang et al., 2004 [PubMed 14701839]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:28711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28711) · Entrez [138429](https://www.ncbi.nlm.nih.gov/gene/138429) · UniProt [Q5T9C9](https://www.uniprot.org/uniprotkb/Q5T9C9) · Ensembl [ENSG00000167103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167103)

## Data

Gene col 9414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9414); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9414]; `tensor/DDL_lfc|DDL_z.npy` [9414]; `embed/gene_vectors.npy` [9414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9414 or target_col == 9414). Every well: [[PIP5KL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP5KL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
