---
symbol: "CC2D2A"
type: "gene"
col: 532
ensembl_id: "ENSG00000048342"
name: "coiled-coil and C2 domain containing 2A"
location: "4p15.32"
module: 51
arm: "+"
pooled_cpm: 12.55
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# CC2D2A

*coiled-coil and C2 domain containing 2A* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.32× (z +15.1, q 0e+00, up in 30 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.42× (z +9.0, q 5e-17, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.665× (z -7.3, q 2e-10, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF280D]] (+0.73, fdr 7e-06), [[CUL5]] (+0.68, fdr 1e-05), [[FUBP1]] (+0.67, fdr 1e-04); moves opposite to [[DNAJC5]] (-0.69, fdr 1e-05), [[MYO9B]] (-0.66, fdr 1e-05), [[TMEM184B]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SUCLG2-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +15.1 | 0e+00 | 30/35 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +10.4 | 1e-22 | 18/28 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +10.0 | 3e-21 | 14/22 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +9.0 | 5e-17 | 26/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +7.9 | 3e-13 | 23/46 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +7.3 | 2e-11 | 23/48 (NCI-H1792, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +6.1 | 9e-08 | 18/47 (NCI-H1792, SNU-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.8 | 4e-07 | 20/42 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 8e-07 | 18/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 5e-06 | 12/44 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +4.3 | 8e-04 | 17/47 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +4.3 | 9e-04 | 8/47 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 15/47 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.8 | 0.006 | 13/48 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.008 | 8/46 (NCI-H2030, J82, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.013 | 5/48 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.037 | 8/47 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.040 | 1/48 (CFPAC-1) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.042 | 5/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.665×** | -7.3 | 2e-10 | 24/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.676×** | -7.0 | 8e-10 | 19/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.735×** | -5.5 | 7e-06 | 19/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.767×** | -4.7 | 3e-04 | 11/46 (SNU-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -4.1 | 0.005 | 8/48 (C32, LS 180, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.652×** | -4.0 | 0.006 | 13/44 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.019 | 12/47 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.821×** | -3.5 | 0.032 | 18/45 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.828×** | -3.3 | 0.053 | 9/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.836× | -3.2 | 0.085 | 10/48 (NCI-H23, HepG2/C3A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -11.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.283× (z -8.7) |
| [[RKO (line)]] | wt | 27.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -10.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 5.75 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0705× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 8.00 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.122× (z -9.6) |
| [[SW480 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.285× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF280D]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[CUL5]] | +0.68 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FUBP1]] | +0.67 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[PGGT1B]] | +0.65 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[RRAGB]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MTPAP]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NFYC]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[QTRT1]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ZZZ3]] | +0.63 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[SCAF8]] | +0.63 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[DIS3L]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[USP24]] | +0.63 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC5]] | -0.69 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.66 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[MPG]] | -0.62 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[FBH1]] | -0.62 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[FRMD8]] | -0.61 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.59 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.59 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PPFIA1]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SNX25]] | -0.58 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[TRPT1]] | -0.58 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.58 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises CC2D2A's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without SUCLG2-DT | 0.035 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CC2D2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[JHY]] | B | JHY activity raises CC2D2A's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.25× lower at baseline in the lines without JHY | 0.093 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-19.4, 4.3); signed map (9.8, -33.3). **Vector** length 75.7, 12.6% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +4.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.9 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -7.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.2 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -7.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil and C2 domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,469,865-15,601,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1345, MKS6, JBTS9 |
| Gene groups (HGNC) | MKS complex |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2K1](https://www.uniprot.org/uniprotkb/Q9P2K1) (Coiled-coil and C2 domain-containing protein 2A):

> Component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Required for ciliogenesis and sonic hedgehog/SHH signaling (By similarity).

**Summary**, from NCBI Gene [57545](https://www.ncbi.nlm.nih.gov/gene/57545):

> This gene encodes a coiled-coil and calcium binding domain protein that appears to play a critical role in cilia formation. Mutations in this gene cause Meckel syndrome type 6, as well as Joubert syndrome type 9. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:29253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29253) · Entrez [57545](https://www.ncbi.nlm.nih.gov/gene/57545) · UniProt [Q9P2K1](https://www.uniprot.org/uniprotkb/Q9P2K1) · Ensembl [ENSG00000048342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048342)

## Data

Gene col 532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 532); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 532]; `tensor/DDL_lfc|DDL_z.npy` [532]; `embed/gene_vectors.npy` [532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 532 or target_col == 532). Every well: [[CC2D2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CC2D2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
