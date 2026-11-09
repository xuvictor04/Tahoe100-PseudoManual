---
symbol: "HSD3B7"
type: "gene"
col: 1800
ensembl_id: "ENSG00000099377"
name: "hydroxy-delta-5-steroid dehydrogenase, 3 beta- and steroid delta-isomerase 7"
location: "16p11.2"
module: 32
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# HSD3B7

*hydroxy-delta-5-steroid dehydrogenase, 3 beta- and steroid delta-isomerase 7* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.90× (z +9.1, q 3e-17, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.378× (z -8.7, q 3e-15, down in 28 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA7]] (+0.53, fdr 3e-05), [[TARBP2]] (+0.51, fdr 6e-05), [[JMJD8]] (+0.50, fdr 4e-05); moves opposite to [[CCNI]] (-0.48, fdr 5e-05), [[AMN1]] (-0.47, fdr 3e-05), [[TPT1]] (-0.47, fdr 3e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DMTN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.1 | 3e-17 | 3/6 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +8.4 | 1e-14 | 10/17 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +7.2 | 1e-10 | 5/9 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +5.0 | 9e-05 | 5/18 (SW480, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.77×** | +3.6 | 0.031 | 2/12 (A498, HEC-1-A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.67× | +3.3 | 0.11 | 2/19 (LS 180, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Salicylic acid (drug)]] 5 µM |  | 1.28× | +3.1 | 0.14 | 3/40 (NCI-H460, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -8.7 | 3e-15 | 28/34 (NCI-H1792, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -7.3 | 6e-11 | 27/41 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -7.2 | 1e-10 | 24/32 (LS 180, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.449×** | -7.0 | 5e-10 | 25/38 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -6.2 | 6e-08 | 25/40 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.502×** | -6.1 | 8e-08 | 20/41 (RPMI-7951, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -5.3 | 1e-05 | 22/38 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -5.2 | 1e-05 | 20/40 (MIA PaCa-2, A498, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.582×** | -4.7 | 1e-04 | 17/39 (A-172, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -4.7 | 1e-04 | 15/37 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.632×** | -4.1 | 0.002 | 16/28 (SW1417, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -3.9 | 0.004 | 13/28 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -3.9 | 0.004 | 10/29 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.672×** | -3.5 | 0.017 | 13/40 (A498, SK-MEL-2, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -3.4 | 0.021 | 14/35 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.665×** | -3.4 | 0.021 | 19/36 (KATO III, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.9) |
| [[RKO (line)]] | wt | 8.43 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0912× (z -9.1) |
| [[A498 (line)]] | wt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0771× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 8.84 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0741× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 5.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 8.27 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 2.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0676× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -8.7) |
| [[A-172 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.962 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA7]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[TARBP2]] | +0.51 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[JMJD8]] | +0.50 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ADAR]] | +0.50 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[MOV10]] | +0.49 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[HDAC10]] | +0.49 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[SLC25A28]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[ZMYM3]] | +0.48 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[SORBS3]] | +0.48 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MUC1]] | +0.47 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[ACP2]] | +0.47 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[MAP3K6]] | +0.47 | +0.39 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNI]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[AMN1]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TPT1]] | -0.47 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[CHCHD2]] | -0.47 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TRMT112]] | -0.46 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[TPT1-AS1]] | -0.45 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[RPS6]] ⚠ | -0.43 | -0.35 / -0.43 | both halves | 1e-04 | STRING 531; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM158]] | -0.43 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[CSGALNACT2]] | -0.43 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[DAP3]] | -0.43 | -0.38 / -0.45 | both halves | 6e-05 | STRING 465 |
| [[TPTEP2-CSNK1E]] | -0.42 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[RPS23]] | -0.42 | -0.34 / -0.38 | both halves | 1e-04 | STRING 539 |
| [[RPL38]] | -0.40 | -0.33 / -0.36 | both halves | 1e-04 | STRING 510 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMTN]] | B | DMTN activity raises HSD3B7's level | lines that do not express DMTN (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without DMTN | 0.033 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.356). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, -21.0); signed map (21.0, -49.0). **Vector** length 41.0, 4.71% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | hydroxy-delta-5-steroid dehydrogenase, 3 beta- and steroid delta-isomerase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,985,207-30,989,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C(27)-3BETA-HSD, SDR11E3 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 7 pathways, smallest: Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2F3](https://www.uniprot.org/uniprotkb/Q9H2F3) (3 beta-hydroxysteroid dehydrogenase type 7):

> The 3-beta-HSD enzymatic system plays a crucial role in the biosynthesis of all classes of hormonal steroids. HSD VII is active against four 7-alpha-hydroxylated sterols. Does not metabolize several different C(19/21) steroids as substrates. Involved in bile acid synthesis. Plays a key role in cell positioning and movement in lymphoid tissues by mediating degradation of 7-alpha,25-dihydroxycholesterol (7-alpha,25-OHC): 7-alpha,25-OHC acts as a ligand for the G protein-coupled receptor …

**Summary**, from NCBI Gene [80270](https://www.ncbi.nlm.nih.gov/gene/80270):

> This gene encodes an enzyme which is involved in the initial stages of the synthesis of bile acids from cholesterol and a member of the short-chain dehydrogenase/reductase superfamily. The encoded protein is a membrane-associated endoplasmic reticulum protein which is active against 7-alpha hydrosylated sterol substrates. Mutations in this gene are associated with a congenital bile acid synthesis defect which leads to neonatal cholestasis, a form of progressive liver disease. Multiple …

**Accessions** — [HGNC:18324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18324) · Entrez [80270](https://www.ncbi.nlm.nih.gov/gene/80270) · UniProt [Q9H2F3](https://www.uniprot.org/uniprotkb/Q9H2F3) · Ensembl [ENSG00000099377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099377)

## Data

Gene col 1800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1800); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1800]; `tensor/DDL_lfc|DDL_z.npy` [1800]; `embed/gene_vectors.npy` [1800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1800 or target_col == 1800). Every well: [[HSD3B7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD3B7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
