---
symbol: "CCDC88B"
type: "gene"
col: 9593
ensembl_id: "ENSG00000168071"
name: "coiled-coil and HOOK domain protein 88B"
location: "11q13.1"
module: 100
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 41
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# CCDC88B

*coiled-coil and HOOK domain protein 88B* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.54× (z +11.8, q 8e-30, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.533× (z -5.7, q 7e-06, down in 18 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNNI3]] (+0.72, fdr 7e-06), [[AHDC1]] (+0.69, fdr 3e-05), [[DBP]] (+0.68, fdr 1e-05); moves opposite to [[ENOX2]] (-0.61, fdr 4e-05), [[ATR]] (-0.60, fdr 3e-05), [[ALG8]] (-0.59, fdr 3e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC01273]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF815P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +11.8 | 8e-30 | 31/36 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +11.8 | 8e-30 | 34/37 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.58×** | +11.5 | 3e-28 | 31/35 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.73×** | +9.1 | 2e-17 | 26/31 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.6 | 4e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +6.1 | 1e-07 | 16/35 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +6.1 | 1e-07 | 11/30 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.1 | 3e-05 | 8/30 (HEC-1-A, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.0 | 4e-05 | 3/17 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 5/29 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.4 | 4e-04 | 13/36 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +4.4 | 6e-04 | 13/36 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.60×** | +4.2 | 0.001 | 13/36 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.003 | 11/32 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.9 | 0.004 | 6/25 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.059 | 4/36 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.065 | 3/17 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -5.7 | 7e-06 | 18/34 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.565×** | -5.2 | 6e-05 | 13/31 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -4.2 | 0.005 | 12/32 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.634×** | -4.1 | 0.005 | 10/36 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.673×** | -3.6 | 0.037 | 13/26 (PANC-1, Hs 766T, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.685×** | -3.4 | 0.056 | 15/36 (PANC-1, KATO III, …) | all doses, flat | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.706× | -3.2 | 0.13 | 7/35 (MIA PaCa-2, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.42 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -10.6) |
| [[KATO III (line)]] | alt | 5.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 4.42 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.72× (z +10.0) ⚠ position not correctable | — |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0677× (z -11.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[Panc 03.27 (line)]] | alt | 8.00 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0567× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNNI3]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[AHDC1]] | +0.69 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[DBP]] | +0.68 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MAST1]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[PLCD1]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[CFD]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[LMTK3]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CAPN12]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[REEP2]] | +0.64 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[VAV1]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[FOXO6]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.61 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ATR]] | -0.60 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ALG8]] | -0.59 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[WDR27]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[MSANTD2]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PTPRG]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PSME3]] | -0.54 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[PRMT3]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[AVEN]] | -0.54 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[E2F3]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.53 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[TOR1A]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01273]] | B | LINC01273 activity raises CCDC88B's level | lines that do not express LINC01273 (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without LINC01273 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287263, A4GALT, TRIM7; maybe low, not absent; its own permutation p |
| [[EPHA10]] | B | EPHA10 activity raises CCDC88B's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without EPHA10 | 0.070 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[CCDC69]] | B | CCDC69 activity lowers CCDC88B's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.25× higher at baseline in the lines without CCDC69 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CDC42BPG]] | B | CDC42BPG activity raises CCDC88B's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.66× lower at baseline in the lines without CDC42BPG | 0.094 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF815P]] | B | CCDC88B activity raises ZNF815P's level | lines that do not express CCDC88B (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without CCDC88B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: TSPAN15, ENSG00000287306; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.0, -3.4); signed map (-5.9, 16.3). **Vector** length 62.3, 11.5% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.3 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil and HOOK domain protein 88B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,340,204-64,357,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37970, BRLZ, HkRP3, FLJ00354, GIPIE; previously CCDC88 |
| Gene groups (HGNC) | HOOK related protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NC98](https://www.uniprot.org/uniprotkb/A6NC98) (Coiled-coil domain-containing protein 88B):

> Acts as a positive regulator of T-cell maturation and inflammatory function. Required for several functions of T-cells, in both the CD4(+) and the CD8(+) compartments and this includes expression of cell surface markers of activation, proliferation, and cytokine production in response to specific or non-specific stimulation (By similarity). Enhances NK cell cytotoxicity by positively regulating polarization of microtubule-organizing center (MTOC) to cytotoxic synapse, lytic granule transport …

**Summary**, from NCBI Gene [283234](https://www.ncbi.nlm.nih.gov/gene/283234):

> This gene encodes a member of the hook-related protein family. Members of this family are characterized by an N-terminal potential microtubule binding domain, a central coiled-coiled and a C-terminal Hook-related domain. The encoded protein may be involved in linking organelles to microtubules. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:26757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26757) · Entrez [283234](https://www.ncbi.nlm.nih.gov/gene/283234) · UniProt [A6NC98](https://www.uniprot.org/uniprotkb/A6NC98) · Ensembl [ENSG00000168071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168071)

## Data

Gene col 9593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9593); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9593]; `tensor/DDL_lfc|DDL_z.npy` [9593]; `embed/gene_vectors.npy` [9593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9593 or target_col == 9593). Every well: [[CCDC88B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC88B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
