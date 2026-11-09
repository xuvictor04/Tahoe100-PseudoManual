---
symbol: "MTRF1L"
type: "gene"
col: 3313
ensembl_id: "ENSG00000112031"
name: "mitochondrial translation release factor 1 like"
location: "6q25.2"
module: 54
arm: "-"
pooled_cpm: 17.58
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 11
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MTRF1L

*mitochondrial translation release factor 1 like* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +16.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 5 µM: 0.745× (z -5.3, q 9e-05, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPC4]] (+0.64, fdr 2e-05), [[BTBD1]] (+0.61, fdr 4e-05), [[KRT8P12]] (+0.60, fdr 1e-05); moves opposite to [[LSM2]] (-0.57, fdr 1e-05), [[MTM1]] (-0.56, fdr 1e-05), [[ADCY9]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +16.1 | 0e+00 | 43/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +14.8 | 0e+00 | 36/37 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.9 | 1e-16 | 33/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +8.6 | 8e-16 | 33/47 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.65×** | +8.4 | 5e-15 | 27/43 (LS 180, A549, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +7.9 | 3e-13 | 30/48 (KATO III, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.5 | 4e-12 | 27/47 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.4 | 9e-09 | 22/47 (SW480, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +6.0 | 1e-07 | 27/47 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.3 | 8e-06 | 19/40 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.38×** | +5.2 | 8e-06 | 11/27 (C32, A549, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 9e-06 | 16/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 2e-05 | 17/47 (RKO, LoVo, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 1e-04 | 17/47 (LS 180, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.6 | 1e-04 | 14/44 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.004 | 17/47 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.009 | 15/48 (HEC-1-A, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.029 | 10/48 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.029 | 5/46 (C-33 A, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | **0.745×** | -5.3 | 9e-05 | 19/48 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.804×** | -5.1 | 1e-04 | 23/48 (SW480, A-427, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.799×** | -4.4 | 0.002 | 17/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.807×** | -4.3 | 0.002 | 18/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.807×** | -4.2 | 0.002 | 14/48 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.745×** | -3.6 | 0.034 | 11/45 (J82, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.051 | 12/47 (A-427, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.820×** | -3.4 | 0.052 | 8/47 (A-427, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.822×** | -3.3 | 0.052 | 13/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.079 | 12/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.770×** | -3.2 | 0.079 | 15/47 (Panc 03.27, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 48.4 | 0 | 2 | — | [[Binimetinib (drug)]] 5 µM 0.282× (z -10.0) |
| [[PANC-1 (line)]] | alt | 18.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.0) | — |
| [[KATO III (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.102× (z -13.1) |
| [[SW480 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.94× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC4]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[BTBD1]] | +0.61 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[KRT8P12]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PSMD12]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[YES1]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MSN]] | +0.54 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[RLIM]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[KRR1]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[GNL1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SERPINB8]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 7 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM2]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MTM1]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ADCY9]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[STK38]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CNNM2]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | -0.55 | -0.39 / -0.53 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPP1R12B]] | -0.54 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[C15orf61]] ⚠ | -0.53 | -0.32 / -0.55 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[FBXO42]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[RAB40C]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PIAS4]] | -0.52 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[RASSF7]] | -0.51 | -0.21 / -0.65 | both halves | 6e-04 |  |
| [[RNF114]] | -0.51 | -0.36 / -0.47 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MTRF1L's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises MTRF1L's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.3, -16.7); signed map (13.8, -12.7). **Vector** length 74.7, 13.3% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +14.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.0 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | +1.1 | +0.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.0 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.7 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial translation release factor 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:152,987,362-153,002,709 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HMRF1L, mtRF1a |
| Gene groups (HGNC) | Mitochondrial translation release factor family |
| Reactome | 3 pathways, smallest: Mitochondrial translation termination; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGC7](https://www.uniprot.org/uniprotkb/Q9UGC7) (Peptide chain release factor 1-like, mitochondrial):

> Mitochondrial peptide chain release factor that directs the termination of translation in response to the peptide chain termination codons UAA and UAG.

**Summary**, from NCBI Gene [54516](https://www.ncbi.nlm.nih.gov/gene/54516):

> The protein encoded by this gene plays a role in mitochondrial translation termination, and is thought to be a release factor that is involved in the dissociation of the complete protein from the final tRNA, the ribosome, and the cognate mRNA. This protein acts upon UAA and UAG stop codons, but has no in vitro activity against UGA, which encodes tryptophan in human mitochondrion, or, the mitochondrial non-cognate stop codons, AGA and AGG. This protein shares sequence similarity to bacterial …

**Accessions** — [HGNC:21051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21051) · Entrez [54516](https://www.ncbi.nlm.nih.gov/gene/54516) · UniProt [Q9UGC7](https://www.uniprot.org/uniprotkb/Q9UGC7) · Ensembl [ENSG00000112031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112031)

## Data

Gene col 3313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3313); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3313]; `tensor/DDL_lfc|DDL_z.npy` [3313]; `embed/gene_vectors.npy` [3313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3313 or target_col == 3313). Every well: [[MTRF1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTRF1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
