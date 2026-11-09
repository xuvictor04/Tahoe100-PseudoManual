---
symbol: "YRDC"
type: "gene"
col: 12207
ensembl_id: "ENSG00000196449"
name: "yrdC N6-threonylcarbamoyltransferase domain containing"
location: "1p34.3"
module: 119
arm: "+"
pooled_cpm: 10.88
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# YRDC

*yrdC N6-threonylcarbamoyltransferase domain containing* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (20 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.48× (z +11.6, q 2e-28, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.673× (z -4.1, q 0.027, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF787]] (+0.76, fdr 7e-06), [[EXOSC4]] (+0.71, fdr 7e-06), [[CTU1]] (+0.70, fdr 7e-06); moves opposite to [[HACD2]] (-0.57, fdr 1e-05), [[TXNDC16]] (-0.57, fdr 1e-05), [[PSIP1]] (-0.56, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.48×** | +11.6 | 2e-28 | 46/46 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +9.5 | 5e-19 | 41/46 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.28×** | +9.1 | 1e-17 | 35/45 (SW480, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +8.0 | 2e-13 | 36/43 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.81×** | +7.7 | 1e-12 | 33/42 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +7.0 | 3e-10 | 29/40 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.70×** | +5.9 | 3e-07 | 29/47 (HOP62, SW480, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.65×** | +5.3 | 6e-06 | 21/39 (SW 900, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.57×** | +5.0 | 4e-05 | 26/46 (SW480, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.53×** | +4.7 | 2e-04 | 17/47 (SW480, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.57×** | +4.6 | 2e-04 | 12/29 (NCI-H460, KATO III, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.6 | 2e-04 | 18/46 (LOX-IMVI, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 23/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +4.4 | 4e-04 | 16/36 (A-172, HT-29, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +4.4 | 4e-04 | 20/45 (CFPAC-1, A549, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 7e-04 | 16/46 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.93×** | +3.8 | 0.004 | 14/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.013 | 7/45 (SW480, PANC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.033 | 3/41 (SHP-77, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.035 | 7/44 (SK-MEL-2, BT-474, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.053 | 8/46 (J82, SW1417, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.053 | 8/43 (SHP-77, H4, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.060 | 13/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.063 | 8/46 (RPMI-7951, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.673×** | -4.1 | 0.027 | 19/47 (LoVo, SW480, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.6 | 0.054 | 8/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.694×** | -3.6 | 0.054 | 17/48 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -3.5 | 0.056 | 16/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.796×** | -3.5 | 0.056 | 19/47 (HCT15, RPMI-7951, …) | all doses, flat |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -3.2 | 0.095 | 10/47 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.095 | 12/47 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.095 | 15/48 (A498, HOP62, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.095 | 11/47 (LS 180, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.754×** | -3.1 | 0.095 | 9/45 (NCI-H2347, H4, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.747×** | -3.1 | 0.095 | 16/45 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.12 | 16/45 (MIA PaCa-2, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.6 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.60× (z +10.1) | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -8.6) ⚠ cell-cycle shift, explains ~98% of this change |
| [[HepG2_C3A (line)]] | wt | 9.92 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0968× (z -8.9) |
| [[A-172 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF787]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[EXOSC4]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CTU1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 | pathway: tRNA processing; STRING 548 |
| [[TRMT10C]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 | pathway: tRNA modification in the mitochondrion |
| [[KTI12]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GAR1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ISG20L2]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RPUSD2]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ZNF276]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD2]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PSIP1]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises YRDC's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises YRDC's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.3, -8.6); signed map (-14.7, -21.9). **Vector** length 66.4, 12.6% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +11.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.4 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | yrdC N6-threonylcarbamoyltransferase domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,802,945-37,808,208 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23476, IRIP, SUA5 |
| Hallmark sets | KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U90](https://www.uniprot.org/uniprotkb/Q86U90) (Threonylcarbamoyl-AMP synthase):

> Cytoplasmic and mitochondrial threonylcarbamoyl-AMP synthase required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Catalyzes the conversion of L-threonine, HCO(3)(-)/CO(2) and ATP to give threonylcarbamoyl-AMP (TC-AMP) as the acyladenylate intermediate, with the release of diphosphate. Participates in t(6)A37 formation in cytoplasmic and mitochondrial tRNAs. May regulate the activity of some transporters …

**Summary**, from NCBI Gene [79693](https://www.ncbi.nlm.nih.gov/gene/79693):

> Enables L-threonylcarbamoyladenylate synthase activity. Involved in tRNA threonylcarbamoyladenosine modification. Acts upstream of or within negative regulation of transport. Is active in mitochondrion. Implicated in Galloway-Mowat syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28905) · Entrez [79693](https://www.ncbi.nlm.nih.gov/gene/79693) · UniProt [Q86U90](https://www.uniprot.org/uniprotkb/Q86U90) · Ensembl [ENSG00000196449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196449)

## Data

Gene col 12207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12207); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12207]; `tensor/DDL_lfc|DDL_z.npy` [12207]; `embed/gene_vectors.npy` [12207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12207 or target_col == 12207). Every well: [[YRDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YRDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
