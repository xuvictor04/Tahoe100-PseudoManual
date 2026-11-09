---
symbol: "MFSD14CP"
type: "gene"
col: 12176
ensembl_id: "ENSG00000196312"
name: "solute carrier family 71 member 3, pseudogene"
location: "9q22.33"
module: 163
arm: "+"
pooled_cpm: 18.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# MFSD14CP

*solute carrier family 71 member 3, pseudogene* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.84× (z +9.0, q 1e-16, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.340× (z -13.8, q 2e-40, down in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.605× (z -6.4, q 2e-08, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED17]] (+0.77, fdr 7e-06), [[CCT6P3-1]] (+0.74, fdr 7e-06), [[RNF4]] (+0.72, fdr 7e-06); moves opposite to [[ZC3H11A]] (-0.76, fdr 7e-06), [[USP16]] (-0.68, fdr 7e-06), [[ARCN1]] (-0.66, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PROSER2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.84×** | +9.0 | 1e-16 | 40/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +7.6 | 7e-12 | 34/47 (LoVo, A-427, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +7.5 | 1e-11 | 35/45 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.7 | 2e-06 | 26/47 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.6 | 2e-06 | 28/46 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +5.5 | 3e-06 | 31/47 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +4.8 | 1e-04 | 23/48 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +4.2 | 0.002 | 16/47 (NCI-H460, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.2 | 0.002 | 21/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +3.8 | 0.010 | 20/47 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.010 | 18/47 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.024 | 16/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.024 | 12/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.29×** | +3.2 | 0.066 | 13/43 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.340×** | -13.8 | 2e-40 | 36/40 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.471×** | -9.3 | 6e-18 | 24/31 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.503×** | -8.1 | 8e-14 | 24/32 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.605×** | -6.4 | 2e-08 | 33/47 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.703×** | -4.5 | 8e-04 | 22/46 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.707×** | -4.4 | 9e-04 | 22/41 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.711×** | -4.2 | 0.002 | 23/47 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[LJI308 (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.043 | 9/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.768×** | -3.4 | 0.048 | 19/47 (A-172, A498, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.846× | -3.0 | 0.15 | 12/48 (NCI-H2030, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0769× (z -19.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 3 (3 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.109× (z -11.0) ⚠ toxic |
| [[C32 (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0684× (z -13.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0188× (z -27.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -11.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -12.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.336× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 9.54 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0826× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0994× (z -22.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED17]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | +0.74 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[RNF4]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SMPD4BP]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.70 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SCAF4]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[AUNIP]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CCZ1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H11A]] | -0.76 | -0.65 / -0.77 | both halves | 7e-06 |  |
| [[USP16]] | -0.68 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[ARCN1]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.65 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[C21orf91]] | -0.62 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[JUN]] | -0.61 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[DARS1]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[THAP5]] | -0.60 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.60 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[YIPF6]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[LZIC]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROSER2]] | B | PROSER2 activity raises MFSD14CP's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without PROSER2 | 0.035 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.4, -5.6); signed map (-41.6, -0.5). **Vector** length 94.6, 21.6% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.2 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | +4.7 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +9.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.1 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.0 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 71 member 3, pseudogene |
| Locus type | pseudogene |
| Location | 9q22.33 — chr9:96,949,555-97,013,366 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | MGC12945; previously HIATL2, MFSD14C, MFSD14CP |
| Gene groups (HGNC) | Solute carrier family 71 |
| Matched by | ensembl_id |

UniProt [Q5VZR4](https://www.uniprot.org/uniprotkb/Q5VZR4) carries no function annotation.

**Summary**, from NCBI Gene [84278](https://www.ncbi.nlm.nih.gov/gene/84278):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23672) · Entrez [84278](https://www.ncbi.nlm.nih.gov/gene/84278) · UniProt [Q5VZR4](https://www.uniprot.org/uniprotkb/Q5VZR4) · Ensembl [ENSG00000196312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196312)

## Data

Gene col 12176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12176); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12176]; `tensor/DDL_lfc|DDL_z.npy` [12176]; `embed/gene_vectors.npy` [12176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12176 or target_col == 12176). Every well: [[MFSD14CP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD14CP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
