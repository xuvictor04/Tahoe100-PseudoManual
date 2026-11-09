---
symbol: "DHFR2"
type: "gene"
col: 10950
ensembl_id: "ENSG00000178700"
name: "dihydrofolate reductase 2"
location: "3q11.2"
module: 51
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# DHFR2

*dihydrofolate reductase 2* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.83× (z +8.5, q 7e-15, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.587× (z -5.4, q 5e-05, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPA]] (+0.68, fdr 7e-06), [[TTC12]] (+0.67, fdr 7e-06), [[NFYC]] (+0.66, fdr 7e-06); moves opposite to [[RECQL]] (-0.61, fdr 7e-06), [[ZCCHC17]] (-0.60, fdr 3e-05), [[MBOAT7]] (-0.60, fdr 8e-06).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +8.5 | 7e-15 | 31/46 (A-172, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.9 | 8e-13 | 15/22 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +7.5 | 1e-11 | 5/10 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.91×** | +6.4 | 2e-08 | 25/46 (KATO III, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.9 | 5e-07 | 14/27 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.3 | 8e-06 | 16/46 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +4.9 | 8e-05 | 12/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.6 | 3e-04 | 9/26 (NCI-H460, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.4 | 6e-04 | 11/44 (A-427, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.4 | 7e-04 | 5/8 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 7e-04 | 13/44 (A-172, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 11/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.006 | 10/46 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.009 | 10/47 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.013 | 9/46 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.034 | 7/44 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.034 | 7/39 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.040 | 8/47 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.043 | 4/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.045 | 4/45 (PANC-1, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -5.4 | 5e-05 | 20/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -5.2 | 5e-05 | 21/46 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -5.1 | 6e-05 | 20/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.437×** | -4.3 | 0.002 | 16/37 (COLO 205, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -3.8 | 0.016 | 13/44 (SW480, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -3.7 | 0.023 | 13/43 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.541× | -3.2 | 0.10 | 5/42 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 0.05 µM |  | 0.733× | -3.1 | 0.12 | 10/45 (C32, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 2.67 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0622× (z -8.6) |
| [[PANC-1 (line)]] | alt | 6.84 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.148× (z -10.7) |
| [[A-172 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPA]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[TTC12]] | +0.67 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[NFYC]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[SREK1]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SCAF8]] | +0.64 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ZNF428]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[FAM227B]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CNOT4]] | +0.62 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[OTUD6B-AS1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[COIL]] | +0.61 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ZCCHC17]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.60 | -0.59 / -0.57 | both halves | 8e-06 |  |
| [[DPP9]] | -0.59 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[TMEM104]] | -0.59 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SENP5]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TOP3A]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[POC1B]] | -0.56 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.55 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[CHAF1B]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[EHBP1L1]] | -0.55 | -0.62 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises DHFR2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers DHFR2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[SENP6]] | C | SENP6's natural level weakens DHFR2's drug response | SENP6's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.14; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-29.0, 21.2); signed map (12.2, -35.3). **Vector** length 51.5, 6.87% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.5 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | dihydrofolate reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:94,047,836-94,063,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16119; previously DHFRP4, DHFRL1 |
| Gene groups (HGNC) | Dihydrofolate reductase family |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XF0](https://www.uniprot.org/uniprotkb/Q86XF0) (Dihydrofolate reductase 2, mitochondrial):

> Key enzyme in folate metabolism. Contributes to the de novo mitochondrial thymidylate biosynthesis pathway. Required to prevent uracil accumulation in mtDNA. Binds its own mRNA and that of DHFR.

**Summary**, from NCBI Gene [200895](https://www.ncbi.nlm.nih.gov/gene/200895):

> Enables dihydrofolate reductase activity and mRNA binding activity. Involved in tetrahydrofolate metabolic process and thymidine biosynthetic process. Located in mitochondrial inner membrane and mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27309) · Entrez [200895](https://www.ncbi.nlm.nih.gov/gene/200895) · UniProt [Q86XF0](https://www.uniprot.org/uniprotkb/Q86XF0) · Ensembl [ENSG00000178700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178700)

## Data

Gene col 10950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10950); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10950]; `tensor/DDL_lfc|DDL_z.npy` [10950]; `embed/gene_vectors.npy` [10950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10950 or target_col == 10950). Every well: [[DHFR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHFR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
