---
symbol: "TSPYL4"
type: "gene"
col: 11899
ensembl_id: "ENSG00000187189"
name: "TSPY like 4"
location: "6q22.1"
module: 10
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TSPYL4

*TSPY like 4* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.45× (z +14.7, q 0e+00, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.0913×; ⚠ toxic); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (C-33 A 0.0628×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0755×; ⚠ cell-cycle shift, explains ~0% of this change); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (C-33 A 0.0675×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN30]] (+0.66, fdr 7e-06), [[TMEM69]] (+0.65, fdr 1e-05), [[ZBED5-AS1]] (+0.64, fdr 7e-06); moves opposite to [[GAN]] (-0.58, fdr 2e-05), [[LMBR1]] (-0.55, fdr 4e-05), [[WRN]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.45×** | +14.7 | 0e+00 | 35/47 (SW480, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +12.5 | 1e-33 | 36/43 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.82×** | +12.2 | 4e-32 | 38/47 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.9 | 2e-25 | 7/10 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.49×** | +10.8 | 4e-25 | 38/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +10.6 | 2e-24 | 36/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +9.6 | 6e-20 | 22/29 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +9.1 | 7e-18 | 24/42 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +9.0 | 1e-17 | 15/28 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.26×** | +9.0 | 2e-17 | 34/44 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +8.5 | 1e-15 | 9/16 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +7.4 | 6e-12 | 27/47 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +6.9 | 3e-10 | 20/45 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.8 | 5e-10 | 21/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.81×** | +6.4 | 7e-09 | 15/39 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.68×** | +6.1 | 3e-08 | 19/45 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +5.9 | 1e-07 | 19/47 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.8 | 2e-07 | 18/39 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.3 | 6e-04 | 15/48 (KATO III, LS 180, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11899.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.0913×; ⚠ toxic); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (C-33 A 0.0628×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0755×; ⚠ cell-cycle shift, explains ~0% of this change); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (C-33 A 0.0675×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.798× | -3.7 | 0.11 | 7/48 (COLO 205, HS-578T, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 0.569× | -3.5 | 0.14 | 10/35 (SW480, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.759× | -3.3 | 0.21 | 6/46 (SW 900, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 8.75 | 0 | 2 | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0628× (z -9.7) |
| [[A-172 (line)]] | wt | 7.13 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0913× (z -10.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 4.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0755× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN30]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TMEM69]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ZBED5-AS1]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[GBA1]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KRBA2]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[HNRNPH2]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RAE1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[NXT2]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ACP2]] | +0.58 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[MED12]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[MINDY1]] | +0.57 | +0.36 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAN]] | -0.58 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[LMBR1]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[WRN]] | -0.54 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[NPHP4]] | -0.52 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[EEF1D]] | -0.52 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[SLC25A5]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ACAP2]] | -0.50 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[CLTCL1]] | -0.50 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[PBX4]] | -0.50 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[ZCCHC7]] | -0.50 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[ADARB1]] | -0.50 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[SMC6]] | -0.49 | -0.21 / -0.50 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSPYL4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity lowers TSPYL4's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without ATXN1-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.4, 17.2); signed map (-7.0, -29.9). **Vector** length 59.0, 8.16% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.3 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +12.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.5 | +7.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.3 | +10.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.0 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TSPY like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,249,964-116,254,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ486I3.2, KIAA0721 |
| Gene groups (HGNC) | TSPYL family |
| Matched by | ensembl_id |

UniProt [Q9UJ04](https://www.uniprot.org/uniprotkb/Q9UJ04) carries no function annotation.

**Summary**, from NCBI Gene [23270](https://www.ncbi.nlm.nih.gov/gene/23270):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in nucleosome assembly. Predicted to be active in chromatin and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21559) · Entrez [23270](https://www.ncbi.nlm.nih.gov/gene/23270) · UniProt [Q9UJ04](https://www.uniprot.org/uniprotkb/Q9UJ04) · Ensembl [ENSG00000187189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187189)

## Data

Gene col 11899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11899); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11899]; `tensor/DDL_lfc|DDL_z.npy` [11899]; `embed/gene_vectors.npy` [11899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11899 or target_col == 11899). Every well: [[TSPYL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPYL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
