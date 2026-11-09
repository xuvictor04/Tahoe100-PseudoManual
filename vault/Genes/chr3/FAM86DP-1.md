---
symbol: "FAM86DP-1"
type: "gene"
col: 16632
ensembl_id: "ENSG00000291223"
name: ""
location: ""
module: 5
arm: "+"
pooled_cpm: 5.16
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# FAM86DP-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +7.0, q 2e-09, up in 18 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.620× (z -5.8, q 3e-06, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM86DP]] (+0.70, fdr 7e-06, ⚠ same locus), [[SPRY4-AS1]] (+0.61, fdr 1e-05), [[PUS1]] (+0.58, fdr 1e-05), [[SRPK1]] (+0.56, fdr 1e-05); moves opposite to [[GALM]] (-0.53, fdr 3e-05), [[GBP2]] (-0.51, fdr 3e-05), [[ADD3]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCND1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.0 | 2e-09 | 18/37 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.3 | 3e-05 | 2/14 (SW1417, HOP62) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.0 | 1e-04 | 1/9 (SNU-423) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.5 | 8e-04 | 11/24 (NCI-H2030, SW 900, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.015 | 9/37 (Hs 766T, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.80×** | +3.7 | 0.018 | 6/29 (A498, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +3.5 | 0.032 | 5/45 (NCI-H1573, KATO III, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.4 | 0.042 | 10/45 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.3 | 0.066 | 5/38 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.072 | 6/38 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.44×** | +3.2 | 0.081 | 2/23 (NCI-H1573, LoVo) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -5.8 | 3e-06 | 18/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -5.6 | 8e-06 | 18/40 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -5.2 | 4e-05 | 15/35 (SK-MEL-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.761×** | -4.3 | 0.002 | 14/44 (HEC-1-A, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.724×** | -3.9 | 0.009 | 16/44 (SNU-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -3.8 | 0.015 | 13/43 (RPMI-7951, SNU-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.017 | 10/46 (HEC-1-A, C32, …) | two highest doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.747×** | -3.5 | 0.027 | 12/45 (HEC-1-A, LoVo, …) | all doses, flat |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.752×** | -3.5 | 0.034 | 5/45 (SW48, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.738×** | -3.4 | 0.035 | 10/46 (H4, AN3 CA, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.826×** | -3.3 | 0.051 | 17/39 (HEC-1-A, SK-MEL-2, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.771×** | -3.2 | 0.071 | 14/44 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.780× | -3.0 | 0.11 | 7/45 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -12.2) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.400× (z -8.6) |
| [[A-427 (line)]] | wt | 3.93 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0729× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0397× (z -9.2) |
| [[A549 (line)]] | wt | 8.06 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 2.63 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0878× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 4.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM86DP]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SPRY4-AS1]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PUS1]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SRPK1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[IRAK1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[BCAR3]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[WDR4]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ZBED4]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NPAS2]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TRIM65]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PRMT3]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[WDR27]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALM]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[GBP2]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ADD3]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[GABARAP]] ⚠ | -0.48 | -0.36 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ARL6IP5]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[RASGEF1B]] | -0.47 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[SECISBP2L]] | -0.46 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[CXXC5]] | -0.46 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[SYNE2]] | -0.46 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ATL1]] | -0.45 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCND1]] | B | CCND1 activity raises FAM86DP-1's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without CCND1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (43.3, 7.5); signed map (8.7, 46.6). **Vector** length 53.6, 7.03% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +7.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +2.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -2.6 |

## What is on record

> [!warning] No registry record
> FAM86DP-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16632); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16632]; `tensor/DDL_lfc|DDL_z.npy` [16632]; `embed/gene_vectors.npy` [16632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16632 or target_col == 16632). Every well: [[FAM86DP-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM86DP-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
