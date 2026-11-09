---
symbol: "GLB1L2"
type: "gene"
col: 7367
ensembl_id: "ENSG00000149328"
name: "galactosidase beta 1 like 2"
location: "11q25"
module: 176
arm: "+"
pooled_cpm: 5.07
n_lines_expressing: 34
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# GLB1L2

*galactosidase beta 1 like 2* — 11q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.13× (z +16.7, q 0e+00, up in 5 of 6 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 2.18× (z +9.5, q 2e-19, up in 20 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.488× (z -8.5, q 1e-14, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PODXL2]] (+0.79, fdr 7e-06), [[CDCA7]] (+0.75, fdr 7e-06), [[WNK2]] (+0.73, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.66, fdr 8e-06), [[CCDC174]] (-0.65, fdr 1e-05), [[GATAD1]] (-0.65, fdr 1e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[YBX2]] → it (grade B ⚠); 2 go from it, the strongest it → [[NBEAL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **4.13×** | +16.7 | 0e+00 | 5/6 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.39×** | +14.9 | 0e+00 | 28/31 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.06×** | +13.6 | 5e-40 | 13/14 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.87×** | +12.9 | 1e-35 | 24/29 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.69×** | +12.1 | 1e-31 | 21/30 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.18×** | +9.5 | 2e-19 | 20/31 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.30×** | +9.4 | 4e-19 | 9/10 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.3 | 2e-08 | 12/29 (CFPAC-1, PANC-1, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 4e-07 | 8/26 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +5.5 | 2e-06 | 8/30 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.25×** | +5.2 | 1e-05 | 11/26 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.9 | 4e-05 | 1/7 (SW480) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.32×** | +4.8 | 7e-05 | 7/24 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.38×** | +3.9 | 0.004 | 4/23 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.016 | 8/27 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.038 | 3/27 (NCI-H23, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.038 | 2/23 (RKO, SW48) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.039 | 4/27 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.039 | 2/31 (NCI-H23, HEC-1-A) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.054 | 5/28 (LoVo, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.488×** | -8.5 | 1e-14 | 17/29 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -8.3 | 2e-14 | 15/24 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -5.4 | 1e-05 | 14/24 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -5.1 | 5e-05 | 12/30 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **0.699×** | -4.3 | 0.002 | 5/28 (A-172, NCI-H460, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.819×** | -3.5 | 0.037 | 7/32 (KATO III, SNU-1, …) | rises with dose | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **0.745×** | -3.5 | 0.037 | 6/24 (COLO 205, RKO, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.606×** | -3.2 | 0.089 | 4/20 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.763× | -3.1 | 0.12 | 8/24 (SW48, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.19 | 1 (1 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 3.75× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.5) |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.9) |
| [[SW48 (line)]] | wt | 26.0 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0867× (z -10.8) |
| [[SW480 (line)]] | alt | 12.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.3) |
| [[C-33 A (line)]] | alt | 9.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 5.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0750× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.0) |
| [[RKO (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0685× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.2) |
| [[A-172 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL2]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[WNK2]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[POLD2]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[AHCY]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MEST]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ASIC1]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CHID1]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PRPS2]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[COLGALT1]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.67 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.66 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[CCDC174]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.65 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SNRNP27]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | -0.64 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[NKAP]] | -0.64 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[TRIP11]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NFU1]] | -0.63 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[N4BP2L2]] | -0.62 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises GLB1L2's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without YBX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[SLC29A2]] | B | SLC29A2 activity raises GLB1L2's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 2.62× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[CKMT1A]] | B | CKMT1A activity raises GLB1L2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without CKMT1A | 0.095 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBEAL2]] | B | GLB1L2 activity raises NBEAL2's level | lines that do not express GLB1L2 (16) vs lines expressing it (34) | 1.76× lower at baseline in the lines without GLB1L2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CHDH, PLS1, ASTL |
| [[UBXN4]] | B | GLB1L2 activity raises UBXN4's level | lines that do not express GLB1L2 (16) vs lines expressing it (34) | 1.23× lower at baseline in the lines without GLB1L2 | 0.078 | ⚠ within organs, on part of the lines; also absent: CHDH, PLS1, ASTL |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-28.2, -30.0); signed map (-29.9, -44.0). **Vector** length 63.8, 13.7% of its response variance represented; |z| ≥ 3 in 687 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.4 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.9 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.8 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.3 | +14.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.9 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | galactosidase beta 1 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q25 — chr11:134,331,988-134,378,341 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Galactosidases beta |
| Reactome | 10 pathways, smallest: Keratan sulfate degradation; CS/DS degradation; Keratan sulfate/keratin metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW92](https://www.uniprot.org/uniprotkb/Q8IW92) (Beta-galactosidase-1-like protein 2):

> Probably cleaves beta-linked terminal galactosyl residues from gangliosides, glycoproteins, and glycosaminoglycans.

**Summary**, from NCBI Gene [89944](https://www.ncbi.nlm.nih.gov/gene/89944):

> Predicted to enable beta-galactosidase activity. Predicted to be involved in galactose catabolic process. Predicted to be active in vacuole. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25129) · Entrez [89944](https://www.ncbi.nlm.nih.gov/gene/89944) · UniProt [Q8IW92](https://www.uniprot.org/uniprotkb/Q8IW92) · Ensembl [ENSG00000149328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149328)

## Data

Gene col 7367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7367); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7367]; `tensor/DDL_lfc|DDL_z.npy` [7367]; `embed/gene_vectors.npy` [7367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7367 or target_col == 7367). Every well: [[GLB1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLB1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
