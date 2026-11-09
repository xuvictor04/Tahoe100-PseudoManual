---
symbol: "DOK4"
type: "gene"
col: 4593
ensembl_id: "ENSG00000125170"
name: "docking protein 4"
location: "16q21"
module: 85
arm: "+"
pooled_cpm: 10.65
n_lines_expressing: 44
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# DOK4

*docking protein 4* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.17× (z +10.4, q 2e-22, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.509× (z -9.0, q 9e-17, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.71, fdr 2e-05), [[RASSF7]] (+0.70, fdr 1e-05), [[AHDC1]] (+0.67, fdr 1e-05); moves opposite to [[CPSF2]] (-0.70, fdr 9e-06), [[ST7L]] (-0.69, fdr 1e-05), [[ZNF337-AS1]] (-0.67, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCDH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +10.4 | 2e-22 | 33/40 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +10.3 | 2e-22 | 33/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +8.0 | 3e-13 | 23/42 (A-172, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +7.3 | 3e-11 | 21/40 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.5 | 1e-08 | 14/29 (HEC-1-A, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.5 | 5e-04 | 13/33 (A498, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.5 | 7e-04 | 3/16 (A498, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.022 | 8/39 (LoVo, SNU-423, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.041 | 6/39 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.041 | 6/37 (Panc 03.27, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.3 | 0.056 | 5/19 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.12 | 5/38 (HepG2/C3A, SW480, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -9.0 | 9e-17 | 30/36 (KATO III, A498, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.535×** | -8.4 | 2e-14 | 26/40 (hTERT-HPNE, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.339×** | -7.6 | 7e-12 | 24/40 (Panc 03.27, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -7.3 | 5e-11 | 23/40 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.705×** | -6.6 | 5e-09 | 22/38 (KATO III, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -6.5 | 7e-09 | 21/39 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -5.7 | 8e-07 | 25/37 (KATO III, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -5.2 | 1e-05 | 22/40 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.5 | 4e-04 | 16/39 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -4.4 | 7e-04 | 19/39 (NCI-H2030, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -4.2 | 0.002 | 12/40 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.746×** | -3.7 | 0.010 | 11/40 (CHP-212, A-427, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.021 | 17/39 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 35.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.8) |
| [[KATO III (line)]] | alt | 26.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.2) |
| [[SW48 (line)]] | wt | 18.5 | 0 | 3 (1 ⚠) | — | [[Bendamustine (drug)]] 5 µM 0.0843× (z -10.6) |
| [[A498 (line)]] | wt | 31.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.4) |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0479× (z -12.7) |
| [[A-172 (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.1) |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0662× (z -10.0) |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -13.8) |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.2) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 5.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 9.39 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0377× (z -9.0) |
| [[SW480 (line)]] | alt | 13.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.0) |
| [[A-427 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.71 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RASSF7]] | +0.70 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.67 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TCIRG1]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.65 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[FBXL16]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PLD2]] | +0.65 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[NXPH4]] | +0.65 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.65 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[PLCD1]] | +0.65 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ORMDL3]] | +0.64 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[CAPN5]] | +0.64 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | -0.70 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[ST7L]] | -0.69 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[ZNF337-AS1]] | -0.67 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | -0.65 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.63 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[PCBP1-AS1]] | -0.61 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[TSTD2]] | -0.60 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[MAD2L1-DT]] | -0.60 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[MSANTD2]] | -0.60 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MCTS1]] | -0.59 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ABCE1]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.59 | -0.53 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises DOK4's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without PCDH1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.9, -4.2); signed map (-30.3, 18.6). **Vector** length 62.2, 10.8% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +8.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +4.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | docking protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,471,922-57,487,327 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10488 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Docking protein family |
| Reactome | 3 pathways, smallest: RET signaling; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEW6](https://www.uniprot.org/uniprotkb/Q8TEW6) (Docking protein 4):

> DOK proteins are enzymatically inert adaptor or scaffolding proteins. They provide a docking platform for the assembly of multimolecular signaling complexes. DOK4 functions in RET-mediated neurite outgrowth and plays a positive role in activation of the MAP kinase pathway (By similarity). Putative link with downstream effectors of RET in neuronal differentiation. May be involved in the regulation of the immune response induced by T-cells.

**Summary**, from NCBI Gene [55715](https://www.ncbi.nlm.nih.gov/gene/55715):

> Predicted to enable signaling adaptor activity. Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to act upstream of or within nervous system development and positive regulation of MAPK cascade. Predicted to be located in cytosol. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19868) · Entrez [55715](https://www.ncbi.nlm.nih.gov/gene/55715) · UniProt [Q8TEW6](https://www.uniprot.org/uniprotkb/Q8TEW6) · Ensembl [ENSG00000125170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125170)

## Data

Gene col 4593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4593); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4593]; `tensor/DDL_lfc|DDL_z.npy` [4593]; `embed/gene_vectors.npy` [4593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4593 or target_col == 4593). Every well: [[DOK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
