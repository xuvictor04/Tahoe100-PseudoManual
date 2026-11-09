---
symbol: "SLC9A3R2"
type: "gene"
col: 770
ensembl_id: "ENSG00000065054"
name: "NHERF family PDZ scaffold protein 2"
location: "16p13.3"
module: 189
arm: "+"
pooled_cpm: 16.62
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# SLC9A3R2

*NHERF family PDZ scaffold protein 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +6.6, q 3e-08, up in 23 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.58× (z +4.0, q 0.010, up in 21 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.45×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.88×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -7.9, q 1e-12, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[R3HCC1]] (+0.63, fdr 1e-05), [[DLGAP4]] (+0.61, fdr 1e-05), [[PORCN]] (+0.60, fdr 2e-05); moves opposite to [[NAF1]] (-0.61, fdr 2e-05), [[TM9SF3]] (-0.55, fdr 5e-05), [[PHC2-AS1]] (-0.54, fdr 1e-04).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 770.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.45×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.88×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +6.6 | 3e-08 | 23/31 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +4.7 | 8e-04 | 15/23 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.59×** | +4.0 | 0.010 | 17/39 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.010 | 21/43 (KATO III, AsPC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.8 | 0.016 | 7/45 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.3 | 0.088 | 7/27 (AsPC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.088 | 18/44 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.42× | +3.0 | 0.16 | 12/43 (H4, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -7.9 | 1e-12 | 27/40 (Hs 766T, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -6.3 | 8e-08 | 32/45 (SNU-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.260×** | -6.1 | 2e-07 | 31/43 (AsPC-1, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.504×** | -5.9 | 4e-07 | 33/44 (SW 900, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -5.3 | 1e-05 | 27/40 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.565×** | -4.9 | 8e-05 | 29/42 (AsPC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -4.4 | 9e-04 | 28/39 (Panc 03.27, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -4.3 | 0.001 | 25/44 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -3.4 | 0.038 | 15/44 (LOX-IMVI, SNU-423, …) | rises with dose | position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.687×** | -3.2 | 0.062 | 12/45 (HepG2/C3A, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.672×** | -3.2 | 0.062 | 17/43 (A-172, SW480, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.499×** | -3.1 | 0.077 | 13/43 (SW 900, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.696×** | -3.1 | 0.077 | 14/45 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -3.0 | 0.094 | 17/41 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 97.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -12.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.3) |
| [[PANC-1 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +9.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 49.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -11.6) |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -10.1) |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -10.7) |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -14.7) |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.4) |
| [[HT-29 (line)]] | alt | 40.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 9.38 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -8.9) |
| [[RKO (line)]] | wt | 9.69 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -14.1) |
| [[A-172 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HCC1]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PORCN]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PDLIM4]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 | same gene group |
| [[SURF2]] | +0.57 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[ARVCF]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SIGIRR]] | +0.56 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[MAP1S]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TSR3]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DNAJB2]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PEAR1]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CLIP2]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAF1]] | -0.61 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[TM9SF3]] | -0.55 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[PHC2-AS1]] | -0.54 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[SLC39A8]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[M6PR]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ANAPC1]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RBBP4]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CTSC]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PPIA]] | -0.50 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[SNX5]] | -0.50 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ECHDC1]] | -0.49 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[RPRD1B]] | -0.49 | -0.40 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC9A3R2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RAC2]] | B | RAC2 activity raises SLC9A3R2's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without RAC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.9, 1.2); signed map (-21.5, 25.4). **Vector** length 76.0, 16.3% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | NHERF family PDZ scaffold protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,025,356-2,039,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIP-1, TKA-1, NHERF-2, E3KARP, OCTS2; previously SLC9A3R2 |
| Gene groups (HGNC) | PDZ domain containing; NHERF family PDZ scaffold proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15599](https://www.uniprot.org/uniprotkb/Q15599) (Na(+)/H(+) exchange regulatory cofactor NHE-RF2):

> Scaffold protein that connects plasma membrane proteins with members of the ezrin/moesin/radixin family and thereby helps to link them to the actin cytoskeleton and to regulate their surface expression. Necessary for cAMP-mediated phosphorylation and inhibition of SLC9A3. May also act as scaffold protein in the nucleus.

**Summary**, from NCBI Gene [9351](https://www.ncbi.nlm.nih.gov/gene/9351):

> This gene encodes a member of the NHERF family of PDZ scaffolding proteins. These proteins mediate many cellular processes by binding to and regulating the membrane expression and protein-protein interactions of membrane receptors and transport proteins. The encoded protein plays a role in intestinal sodium absorption by regulating the activity of the sodium/hydrogen exchanger 3, and may also regulate the cystic fibrosis transmembrane regulator (CFTR) ion channel. Alternatively spliced …

**Accessions** — [HGNC:11076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11076) · Entrez [9351](https://www.ncbi.nlm.nih.gov/gene/9351) · UniProt [Q15599](https://www.uniprot.org/uniprotkb/Q15599) · Ensembl [ENSG00000065054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065054)

## Data

Gene col 770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 770); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 770]; `tensor/DDL_lfc|DDL_z.npy` [770]; `embed/gene_vectors.npy` [770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 770 or target_col == 770). Every well: [[SLC9A3R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A3R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
