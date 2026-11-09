---
symbol: "SCN1B"
type: "gene"
col: 2652
ensembl_id: "ENSG00000105711"
name: "sodium voltage-gated channel beta subunit 1"
location: "19q13.11"
module: 47
arm: "+"
pooled_cpm: 3.26
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SCN1B

*sodium voltage-gated channel beta subunit 1* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +9.1, q 8e-17, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.425× (z -8.1, q 2e-13, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPN]] (+0.69, fdr 7e-06, ⚠ same locus), [[CCDC28B]] (+0.60, fdr 1e-05), [[GRAMD1A]] (+0.58, fdr 1e-05, ⚠ read-through risk), [[BIK]] (+0.53, fdr 5e-05), [[ARHGAP45]] (+0.53, fdr 5e-05); moves opposite to [[GPALPP1]] (-0.55, fdr 1e-04), [[ZCCHC4]] (-0.51, fdr 4e-05), [[PAAF1]] (-0.48, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +9.1 | 8e-17 | 29/42 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +7.0 | 6e-10 | 2/5 (HOP62, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +6.7 | 4e-09 | 22/37 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.8 | 3e-04 | 5/18 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +4.6 | 5e-04 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.7 | 0.018 | 9/43 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.077 | 4/26 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.425×** | -8.1 | 2e-13 | 20/38 (A549, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.558×** | -5.5 | 8e-06 | 19/42 (Hs 766T, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -5.2 | 4e-05 | 17/35 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.586×** | -5.1 | 5e-05 | 17/38 (A-427, SK-MEL-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -4.3 | 0.002 | 15/41 (HepG2/C3A, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.732×** | -4.2 | 0.002 | 12/41 (CHP-212, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.643×** | -4.2 | 0.002 | 12/35 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -4.1 | 0.002 | 14/27 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.008 | 8/36 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.683×** | -3.6 | 0.016 | 8/38 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -3.3 | 0.056 | 8/26 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -3.2 | 0.057 | 14/38 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.063 | 13/30 (SNU-423, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.714×** | -3.1 | 0.082 | 9/33 (HOP62, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.59 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0474× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Carbamazepine (drug)]] 0.5 µM 0.0506× (z -10.6) |
| [[LoVo (line)]] | wt | 3.98 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0936× (z -9.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.66× (z +8.8) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[Hs 766T (line)]] | wt | 7.68 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0816× (z -9.0) |
| [[HS-578T (line)]] | alt | 6.45 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.8× (z +8.5) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[SNU-423 (line)]] | alt | 3.50 | 0 | 1 | — | [[Entrectinib (drug)]] 0.05 µM 0.0608× (z -8.6) |
| [[A-427 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPN]] | +0.69 | +0.73 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[CCDC28B]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GRAMD1A]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 | STRING 624; ⚠ **readthrough risk**: this gene lies 4.0 kb 3′ of GRAMD1A on the same strand (can correlate by spillover, not regulation) |
| [[BIK]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ARHGAP45]] | +0.53 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[ARHGAP40]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RASSF5]] | +0.51 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[LSMEM2]] | +0.51 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SEMA6B]] | +0.50 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TTLL13]] | +0.49 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ACOXL]] | +0.49 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ATAD3C]] | +0.49 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[AMN]] | +0.49 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[PDE9A]] | +0.48 | +0.32 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPALPP1]] | -0.55 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[ZCCHC4]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PAAF1]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[DHX35]] | -0.47 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[NUP133]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[MSL3]] | -0.45 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[STRADB]] | -0.45 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[C17orf80]] | -0.44 | -0.26 / -0.38 | both halves | 3e-04 |  |
| [[STX16]] | -0.44 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[DNAJC13]] | -0.44 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[PI4K2B]] | -0.44 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[TMEM234]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAG3]] | B | LAG3 activity raises SCN1B's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without LAG3 | 0.083 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 21.2); signed map (14.3, 18.0). **Vector** length 56.1, 8.02% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +7.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | sodium voltage-gated channel beta subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:35,030,470-35,040,449 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | V-set domain containing; Sodium voltage-gated channel beta subunits |
| Hallmark sets | INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP |
| Reactome | 10 pathways, smallest: Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07699](https://www.uniprot.org/uniprotkb/Q07699) (Sodium channel regulatory subunit beta-1):

> Regulatory subunit of multiple voltage-gated sodium (Nav) channels directly mediating the depolarization of excitable membranes. Navs, also called VGSCs (voltage-gated sodium channels) or VDSCs (voltage-dependent sodium channels), operate by switching between closed and open conformations depending on the voltage difference across the membrane. In the open conformation they allow Na(+) ions to selectively pass through the pore, along their electrochemical gradient. The influx of Na+ ions …

**Summary**, from NCBI Gene [6324](https://www.ncbi.nlm.nih.gov/gene/6324):

> Voltage-gated sodium channels are heteromeric proteins that function in the generation and propagation of action potentials in muscle and neuronal cells. They are composed of one alpha and two beta subunits, where the alpha subunit provides channel activity and the beta-1 subunit modulates the kinetics of channel inactivation. This gene encodes a sodium channel beta-1 subunit. Mutations in this gene result in generalized epilepsy with febrile seizures plus, Brugada syndrome 5, and defects in …

**Accessions** — [HGNC:10586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10586) · Entrez [6324](https://www.ncbi.nlm.nih.gov/gene/6324) · UniProt [Q07699](https://www.uniprot.org/uniprotkb/Q07699) · Ensembl [ENSG00000105711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105711)

## Data

Gene col 2652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2652); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2652]; `tensor/DDL_lfc|DDL_z.npy` [2652]; `embed/gene_vectors.npy` [2652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2652 or target_col == 2652). Every well: [[SCN1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
