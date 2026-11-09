---
symbol: "ELL3"
type: "gene"
col: 4928
ensembl_id: "ENSG00000128886"
name: "elongation factor for RNA polymerase II 3"
location: "15q15.3"
module: 100
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ELL3

*elongation factor for RNA polymerase II 3* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.91× (z +8.5, q 1e-14, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.73× (z +8.3, q 3e-14, up in 25 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 0.5 µM in 1 line (LS 180 0.0450×); [[Busulfan (drug)]] 0.05 µM in 1 line (SW480 0.0605×); [[Talc (drug)]] 0.5 µM in 1 line (BT-474 0.0723×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNN]] (+0.69, fdr 1e-05), [[PEDS1]] (+0.66, fdr 1e-05), [[RIMS3]] (+0.66, fdr 1e-05); moves opposite to [[DNAJC11]] (-0.64, fdr 1e-05), [[ERCC6L2]] (-0.63, fdr 3e-05), [[CPSF3]] (-0.61, fdr 1e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +8.5 | 1e-14 | 1/2 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +8.3 | 3e-14 | 25/35 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +7.9 | 4e-13 | 25/39 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.8 | 1e-12 | 8/20 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +6.4 | 1e-08 | 17/35 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.4 | 1e-08 | 1/8 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.5 | 3e-06 | 12/38 (NCI-H2030, NCI-H23, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +5.4 | 4e-06 | 2/4 (PANC-1, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.2 | 1e-05 | 8/40 (NCI-H23, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.0 | 3e-05 | 3/12 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +4.9 | 5e-05 | 21/40 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +4.2 | 0.001 | 7/19 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.2 | 0.001 | 8/16 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.9 | 0.004 | 5/11 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.007 | 4/23 (NCI-H1573, HEC-1-A, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.87×** | +3.7 | 0.008 | 2/11 (LoVo, NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.021 | 1/14 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.022 | 1/16 (HT-29) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.066 | 0/17 | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 0.5 µM in 1 line (LS 180 0.0450×); [[Busulfan (drug)]] 0.05 µM in 1 line (SW480 0.0605×); [[Talc (drug)]] 0.5 µM in 1 line (BT-474 0.0723×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.670× | -3.3 | 0.39 | 8/41 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.679× | -3.2 | 0.39 | 7/39 (SNU-423, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.690× | -3.1 | 0.41 | 4/39 (C-33 A, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.16 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0723× (z -8.5) |
| [[LS 180 (line)]] | wt | 3.48 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0450× (z -10.2) |
| [[SW480 (line)]] | alt | 1.47 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0605× (z -8.7) |
| [[A-172 (line)]] | wt | 0.867 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.741 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.561 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.725 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.619 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.717 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.668 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.732 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.755 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.537 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.884 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNN]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.66 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.63 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[NPTN]] | +0.63 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.63 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ANO8]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.61 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.64 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.63 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[CPSF3]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[R3HDM2]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PRORP]] | -0.60 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TAF2]] | -0.59 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[ST7L]] | -0.59 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[MSRA]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ALG8]] | -0.58 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TASOR]] | -0.58 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MED1]] | -0.58 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises ELL3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without IRF6 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CDS1]] | B | CDS1 activity raises ELL3's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without CDS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.8, -3.0); signed map (-28.9, 21.0). **Vector** length 34.5, 3.89% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | elongation factor for RNA polymerase II 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,772,605-43,777,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22637 |
| Gene groups (HGNC) | Super elongation complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB65](https://www.uniprot.org/uniprotkb/Q9HB65) (RNA polymerase II elongation factor ELL3):

> Enhancer-binding elongation factor that specifically binds enhancers in embryonic stem cells (ES cells), marks them, and is required for their future activation during stem cell specification. Does not only bind to enhancer regions of active genes, but also marks the enhancers that are in a poised or inactive state in ES cells and is required for establishing proper RNA polymerase II occupancy at developmentally regulated genes in a cohesin-dependent manner. Probably required for priming …

**Summary**, from NCBI Gene [80237](https://www.ncbi.nlm.nih.gov/gene/80237):

> Predicted to enable cis-regulatory region sequence-specific DNA binding activity. Involved in positive regulation of DNA-templated transcription and transcription by RNA polymerase II. Located in nucleoplasm. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23113) · Entrez [80237](https://www.ncbi.nlm.nih.gov/gene/80237) · UniProt [Q9HB65](https://www.uniprot.org/uniprotkb/Q9HB65) · Ensembl [ENSG00000128886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128886)

## Data

Gene col 4928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4928); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4928]; `tensor/DDL_lfc|DDL_z.npy` [4928]; `embed/gene_vectors.npy` [4928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4928 or target_col == 4928). Every well: [[ELL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
