---
symbol: "CFAP46"
type: "gene"
col: 10165
ensembl_id: "ENSG00000171811"
name: "cilia and flagella associated protein 46"
location: "10q26.3"
module: 73
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# CFAP46

*cilia and flagella associated protein 46* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 22.6× (z +34.9, q 0e+00, up in 15 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Medroxyprogesterone acetate (drug)]] 5 µM: 0.662× (z -4.6, q 0.002, down in 5 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTNR1A]] (+0.66, fdr 7e-06), [[PCDH11X]] (+0.61, fdr 4e-05), [[IL2RG]] (+0.61, fdr 2e-05); moves opposite to [[ZDHHC7]] (-0.47, fdr 7e-05), [[SNHG30]] (-0.47, fdr 4e-05), [[ARSK]] (-0.47, fdr 5e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TPTEP1-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **22.6×** | +34.9 | 0e+00 | 15/17 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.91×** | +16.4 | 0e+00 | 12/16 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +14.8 | 0e+00 | 7/16 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.57×** | +11.6 | 1e-28 | 1/3 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **4.53×** | +11.5 | 2e-28 | 14/20 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.04×** | +11.0 | 2e-26 | 14/23 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.32×** | +9.5 | 2e-19 | 16/22 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +6.8 | 9e-10 | 1/5 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +6.6 | 2e-09 | 2/8 (LS 180, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +5.6 | 1e-06 | 13/22 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.5 | 4e-04 | 3/24 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.3 | 9e-04 | 3/26 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +4.2 | 0.001 | 2/19 (NCI-H460, SNU-1) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.97×** | +3.8 | 0.005 | 1/9 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +3.7 | 0.010 | 7/25 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.034 | 9/25 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.061 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.0 | 0.070 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.662×** | -4.6 | 0.002 | 5/21 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | **0.633×** | -3.6 | 0.078 | 9/18 (A549, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -3.5 | 0.089 | 9/20 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.759× | -3.1 | 0.24 | 2/26 (BT-474, HOP62) | top dose only | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | 0.670× | -3.1 | 0.24 | 3/18 (SNU-1, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.44 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 123× (z +28.2) | — |
| [[A-172 (line)]] | wt | 3.19 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.0× (z +17.2) | — |
| [[SW 900 (line)]] | alt | 2.25 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 148× (z +15.6) | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -11.1) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 1.44 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.1× (z +13.6) | — |
| [[A549 (line)]] | wt | 1.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 0.849 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 136× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 301× (z +21.9) | — |
| [[HEC-1-A (line)]] | alt | 0.738 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 146× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 0.830 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.4× (z +11.5) | — |
| [[KATO III (line)]] | alt | 5.32 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0610× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 4.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +11.3) | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 1 | — | [[Pentagastrin (drug)]] 5 µM 0.462× (z -17.3) |
| [[SW48 (line)]] | wt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 890× (z +11.7) | — |
| [[A-427 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.691 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.681 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.413 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTNR1A]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[PCDH11X]] | +0.61 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[IL2RG]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TPRXL]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[DSG4]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MOB3C]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[OSBP2]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ADAP1]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[HYDIN]] | +0.56 | +0.68 / +0.43 | both halves | 3e-05 | STRING 425 |
| [[KLK10]] | +0.56 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[TPTEP1-1]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC7]] | -0.47 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[SNHG30]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ARSK]] | -0.47 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SUMF2]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPTEP1-1]] | B | TPTEP1-1 activity raises CFAP46's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 1.86× lower at baseline in the lines without TPTEP1-1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[MMP28]] | C | MMP28 activity raises CFAP46's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without MMP28 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.3, 48.4); signed map (4.5, 35.1). **Vector** length 45.6, 9.14% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +34.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.6 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.9 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,808,392-132,942,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434A1721, bA288G11.4, bA288G11.5, bB137A17.2, FLJ25954, bB137A17.3; previously C10orf123, C10orf124, C10orf93, C10orf92, TTC40 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYW2](https://www.uniprot.org/uniprotkb/Q8IYW2) (Cilia- and flagella-associated protein 46):

> As part of the central apparatus of the cilium axoneme plays a role in cilium movement.

**Summary**, from NCBI Gene [54777](https://www.ncbi.nlm.nih.gov/gene/54777):

> Predicted to be involved in axoneme assembly. Predicted to be located in axoneme. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25247) · Entrez [54777](https://www.ncbi.nlm.nih.gov/gene/54777) · UniProt [Q8IYW2](https://www.uniprot.org/uniprotkb/Q8IYW2) · Ensembl [ENSG00000171811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171811)

## Data

Gene col 10165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10165); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10165]; `tensor/DDL_lfc|DDL_z.npy` [10165]; `embed/gene_vectors.npy` [10165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10165 or target_col == 10165). Every well: [[CFAP46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
