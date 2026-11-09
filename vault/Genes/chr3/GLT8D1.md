---
symbol: "GLT8D1"
type: "gene"
col: 300
ensembl_id: "ENSG00000016864"
name: "glycosyltransferase 8 domain containing 1"
location: "3p21.1"
module: 40
arm: "+"
pooled_cpm: 19.15
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# GLT8D1

*glycosyltransferase 8 domain containing 1* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.31× (z +4.7, q 0.001, up in 11 of 28 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -24.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POGLUT2]] (+0.68, fdr 1e-05), [[CRLS1]] (+0.66, fdr 7e-06), [[PRRC1]] (+0.66, fdr 7e-06); moves opposite to [[LINC02516]] (-0.60, fdr 1e-05), [[CPEB1]] (-0.58, fdr 1e-05), [[SKIL]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CERCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.7 | 0.001 | 11/28 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **1.23×** | +3.7 | 0.060 | 21/47 (SW48, A549, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.381×** | -24.5 | 0e+00 | 44/47 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.335×** | -18.9 | 0e+00 | 42/47 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.362×** | -18.2 | 0e+00 | 41/47 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -15.2 | 0e+00 | 44/48 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -13.1 | 7e-37 | 42/48 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -13.0 | 7e-37 | 41/46 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.513×** | -12.0 | 5e-31 | 38/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.561×** | -10.3 | 4e-23 | 39/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -10.1 | 3e-22 | 34/48 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.586×** | -9.5 | 8e-20 | 34/48 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -8.0 | 5e-14 | 30/46 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.645×** | -7.8 | 2e-13 | 29/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -7.7 | 6e-13 | 30/48 (KATO III, SW 1088, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.688×** | -6.7 | 1e-09 | 23/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.501×** | -6.5 | 4e-09 | 27/48 (SW 900, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -6.2 | 2e-08 | 25/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -5.9 | 1e-07 | 24/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 39.7 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -32.8) |
| [[A-172 (line)]] | wt | 36.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 9 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.232× (z -11.8) |
| [[HOP62 (line)]] | alt | 28.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -25.9) |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -22.1) |
| [[A498 (line)]] | wt | 18.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -21.6) |
| [[C32 (line)]] | wt | 20.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.9) |
| [[J82 (line)]] | alt | 21.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -15.2) |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0238× (z -21.8) |
| [[H4 (line)]] | wt | 23.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0567× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.1) |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.4) |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -17.8) |
| [[A549 (line)]] | wt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -12.0) |
| [[SW480 (line)]] | alt | 16.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.406× (z -8.9) |
| [[A-427 (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -15.8) |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.185× (z -10.0) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.6) |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.2) |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -12.4) |
| [[RKO (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.1) |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -9.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -9.4) |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0908× (z -10.2) |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -10.8) |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.66 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CHPF]] | +0.66 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[P3H1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MAN1B1]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[IDH2]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[APAF1]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MLEC]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02516]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CPEB1]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SKIL]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[LINC02241]] | -0.54 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[ZFPM2-AS1]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[ARAP2]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MTHFD2L]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TUSC3]] | -0.53 | -0.57 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | CERCAM activity raises GLT8D1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without CERCAM | 0.009 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[GPX8]] | B | GPX8 activity raises GLT8D1's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without GPX8 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |
| [[VNN1]] | B | VNN1 activity lowers GLT8D1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.36× higher at baseline in the lines without VNN1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[CPEB1]] | B | CPEB1 activity raises GLT8D1's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 1.62× lower at baseline in the lines without CPEB1 | 0.063 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (8.5, -31.3); signed map (-47.9, 7.4). **Vector** length 73.9, 14.7% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +1.7 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.6 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -5.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -7.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | glycosyltransferase 8 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,694,486-52,706,032 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AD-017, FLJ14611 |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CQ7](https://www.uniprot.org/uniprotkb/Q68CQ7) (Glycosyltransferase 8 domain-containing protein 1):

> In vitro, catalyzes the transfer of a galactose residue from UDP-galactose onto GalNAc and GlcNAc structures.

**Summary**, from NCBI Gene [55830](https://www.ncbi.nlm.nih.gov/gene/55830):

> This gene encodes a member of the glycosyltransferase family. The specific function of this protein has not been determined. Alternative splicing results in multiple transcript variants of this gene [provided by RefSeq, May 2013]

**Accessions** — [HGNC:24870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24870) · Entrez [55830](https://www.ncbi.nlm.nih.gov/gene/55830) · UniProt [Q68CQ7](https://www.uniprot.org/uniprotkb/Q68CQ7) · Ensembl [ENSG00000016864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000016864)

## Data

Gene col 300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 300); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 300]; `tensor/DDL_lfc|DDL_z.npy` [300]; `embed/gene_vectors.npy` [300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 300 or target_col == 300). Every well: [[GLT8D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLT8D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
