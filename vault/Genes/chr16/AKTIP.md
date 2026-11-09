---
symbol: "AKTIP"
type: "gene"
col: 9397
ensembl_id: "ENSG00000166971"
name: "AKT interacting protein"
location: "16q12.2"
module: 188
arm: "+"
pooled_cpm: 7.33
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# AKTIP

*AKT interacting protein* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.88× (z +9.6, q 3e-19, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.496× (z -10.7, q 7e-24, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPSS1]] (+0.67, fdr 1e-05), [[MPP1]] (+0.66, fdr 1e-05), [[NDRG3]] (+0.65, fdr 1e-05); moves opposite to [[RBBP6]] (-0.68, fdr 1e-05), [[MZF1-AS1]] (-0.63, fdr 1e-05), [[ERCC6L2]] (-0.63, fdr 3e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +9.6 | 3e-19 | 35/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +8.6 | 1e-15 | 29/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +8.5 | 2e-15 | 31/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.8 | 6e-13 | 7/12 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.4 | 2e-08 | 10/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 3e-06 | 15/43 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.1 | 2e-05 | 13/31 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +4.3 | 0.001 | 2/47 (SW480, HEC-1-A) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.009 | 8/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.010 | 5/46 (NCI-H23, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +3.5 | 0.023 | 4/22 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 1.16× | +3.2 | 0.060 | 1/48 (NCI-H460) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.069 | 5/47 (HT-29, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -10.7 | 7e-24 | 33/47 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -9.3 | 6e-18 | 27/42 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.576×** | -8.4 | 9e-15 | 27/46 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.610×** | -7.5 | 7e-12 | 24/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.606×** | -7.3 | 3e-11 | 24/45 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.751×** | -6.2 | 6e-08 | 18/42 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.686×** | -5.7 | 8e-07 | 21/45 (A498, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -5.1 | 2e-05 | 16/46 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.593×** | -4.2 | 0.002 | 10/44 (HOP62, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.762×** | -4.1 | 0.002 | 13/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.765×** | -3.8 | 0.006 | 11/46 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.706×** | -3.8 | 0.007 | 4/45 (SW480, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.803×** | -3.3 | 0.036 | 5/47 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.053 | 12/42 (HCT15, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.816×** | -3.1 | 0.075 | 19/41 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.087 | 8/41 (SW48, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 10.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -9.0) ⚠ toxic |
| [[A549 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -12.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HS-578T (line)]] | alt | 8.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[hTERT-HPNE (line)]] | wt | 5.37 | 0 | 1 | — | [[Flutamide (drug)]] 5 µM 0.0635× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 5.26 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0762× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 5.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.98 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 6.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 6.94 | 0 | 1 | — | [[Bexarotene (drug)]] 0.05 µM 0.0600× (z -8.6) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[MPP1]] | +0.66 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.65 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[GPD1L]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CDS2]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.64 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[NOMO2]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[RNF187]] | +0.63 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[SPAST]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[STX7]] | +0.63 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[EXD2]] | +0.63 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ATP7B]] | +0.63 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.63 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.63 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[SON]] | -0.62 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.62 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ARMC5]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[FBXO10]] | -0.60 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.60 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[PCF11]] | -0.60 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ANGPT2]] | -0.59 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[MIRLET7IHG]] | -0.59 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers AKTIP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[L1CAM]] | B | L1CAM activity raises AKTIP's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.13× lower at baseline in the lines without L1CAM | 0.0997 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -6.9); signed map (-36.0, -13.7). **Vector** length 64.7, 9.63% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +9.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -3.0 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -9.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | AKT interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:53,491,040-53,504,411 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13258; previously FTS |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2; FHF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8T0](https://www.uniprot.org/uniprotkb/Q9H8T0) (AKT-interacting protein):

> Component of the FTS/Hook/FHIP complex (FHF complex). The FHF complex may function to promote vesicle trafficking and/or fusion via the homotypic vesicular protein sorting complex (the HOPS complex). Regulates apoptosis by enhancing phosphorylation and activation of AKT1. Increases release of TNFSF6 via the AKT1/GSK3B/NFATC1 signaling cascade. FHF complex promotes the distribution of AP-4 complex to the perinuclear area of the cell.

**Summary**, from NCBI Gene [64400](https://www.ncbi.nlm.nih.gov/gene/64400):

> The mouse homolog of this gene produces fused toes and thymic hyperplasia in heterozygous mutant animals while homozygous mutants die in early development. This gene may play a role in apoptosis as these morphological abnormalities are caused by altered patterns of programmed cell death. The protein encoded by this gene is similar to the ubiquitin ligase domain of other ubiquitin-conjugating enzymes but lacks the conserved cysteine residue that enables those enzymes to conjugate ubiquitin to …

**Accessions** — [HGNC:16710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16710) · Entrez [64400](https://www.ncbi.nlm.nih.gov/gene/64400) · UniProt [Q9H8T0](https://www.uniprot.org/uniprotkb/Q9H8T0) · Ensembl [ENSG00000166971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166971)

## Data

Gene col 9397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9397); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9397]; `tensor/DDL_lfc|DDL_z.npy` [9397]; `embed/gene_vectors.npy` [9397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9397 or target_col == 9397). Every well: [[AKTIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKTIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
