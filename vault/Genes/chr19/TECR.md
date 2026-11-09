---
symbol: "TECR"
type: "gene"
col: 1811
ensembl_id: "ENSG00000099797"
name: "trans-2,3-enoyl-CoA reductase"
location: "19p13.12"
module: 11
arm: "-"
pooled_cpm: 12.93
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TECR

*trans-2,3-enoyl-CoA reductase* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +9.3, q 8e-18, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.506× (z -8.7, q 3e-15, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.67, fdr 7e-06), [[ERMP1]] (+0.65, fdr 1e-05), [[PIK3R2]] (+0.65, fdr 7e-06); moves opposite to [[RPP25L]] (-0.70, fdr 7e-06), [[NSRP1]] (-0.64, fdr 1e-05), [[RPP38]] (-0.63, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ELOVL5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +9.3 | 8e-18 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +8.3 | 2e-14 | 34/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +7.3 | 4e-11 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.5 | 1e-08 | 23/35 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.2 | 8e-08 | 22/46 (A549, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.7 | 1e-06 | 29/48 (SNU-423, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.6 | 2e-06 | 14/33 (A549, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.6 | 2e-06 | 14/25 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.6 | 2e-04 | 16/41 (NCI-H23, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.002 | 12/48 (NCI-H23, PANC-1, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.9 | 0.005 | 17/36 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.038 | 15/47 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.038 | 7/44 (NCI-H23, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.050 | 6/47 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +3.0 | 0.10 | 10/48 (HS-578T, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.506×** | -8.7 | 3e-15 | 28/45 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.663×** | -7.4 | 4e-11 | 29/47 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -6.1 | 3e-07 | 28/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.614×** | -6.0 | 3e-07 | 26/46 (SW 900, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.685×** | -4.8 | 2e-04 | 21/47 (A-427, A498, …) | all doses, stronger at high dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.769×** | -3.3 | 0.078 | 14/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 9.40 | 0 | 2 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0694× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 7.73 | 0 | 2 (1 ⚠) | — | [[Fenofibrate (drug)]] 5 µM 0.0799× (z -9.0) |
| [[KATO III (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 8.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -8.9) |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.167× (z -9.1) |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.139× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -9.4) |
| [[RKO (line)]] | wt | 7.45 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.101× (z -8.6) |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[HDAC1]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CLSTN1]] | +0.63 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[CRTAP]] | +0.63 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[RBM14-RBM4]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PPT1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 | pathway: Fatty acid metabolism |
| [[SUMO1]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | -0.70 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.64 | -0.67 / -0.53 | both halves | 1e-05 | same gene group |
| [[RPP38]] | -0.63 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[NT5C]] | -0.63 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[EID2]] | -0.63 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[ARL14EP]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[NIFK]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ERCC4]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELOVL5]] | B | ELOVL5 activity raises TECR's level | lines that do not express ELOVL5 (6) vs lines expressing it (44) | 1.17× lower at baseline in the lines without ELOVL5 | 0.076 | ⚠ within organs, on part of the lines; also absent: PDE4A, TCEA2, MPP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-6.5, -15.3); signed map (-28.2, -35.7). **Vector** length 82.3, 15.1% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +7.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.7 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.6 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | trans-2,3-enoyl-CoA reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,517,085-14,565,980 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TER, MRT14; previously SC2, GPSN2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Steroid 5-alpha reductase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ01](https://www.uniprot.org/uniprotkb/Q9NZ01) (Very-long-chain enoyl-CoA reductase):

> Involved in both the production of very long-chain fatty acids for sphingolipid synthesis and the degradation of the sphingosine moiety in sphingolipids through the sphingosine 1-phosphate metabolic pathway. Catalyzes the last of the four reactions of the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process, allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids/VLCFAs per cycle. This enzyme reduces the trans-2,3-enoyl-CoA …

**Summary**, from NCBI Gene [9524](https://www.ncbi.nlm.nih.gov/gene/9524):

> This gene encodes a multi-pass membrane protein that resides in the endoplasmic reticulum, and belongs to the steroid 5-alpha reductase family. The elongation of microsomal long and very long chain fatty acid consists of 4 sequential reactions. This protein catalyzes the final step, reducing trans-2,3-enoyl-CoA to saturated acyl-CoA. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Apr 2011]

**Accessions** — [HGNC:4551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4551) · Entrez [9524](https://www.ncbi.nlm.nih.gov/gene/9524) · UniProt [Q9NZ01](https://www.uniprot.org/uniprotkb/Q9NZ01) · Ensembl [ENSG00000099797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099797)

## Data

Gene col 1811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1811); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1811]; `tensor/DDL_lfc|DDL_z.npy` [1811]; `embed/gene_vectors.npy` [1811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1811 or target_col == 1811). Every well: [[TECR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TECR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
