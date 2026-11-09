---
symbol: "FAM229B"
type: "gene"
col: 12787
ensembl_id: "ENSG00000203778"
name: "family with sequence similarity 229 member B"
location: "6q21"
module: 45
arm: "+"
pooled_cpm: 3.51
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 12
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# FAM229B

*family with sequence similarity 229 member B* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.92× (z +8.4, q 2e-14, up in 24 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.375× (z -8.9, q 4e-16, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KBTBD3]] (+0.74, fdr 7e-06), [[ZNF14]] (+0.67, fdr 1e-05), [[PRMT9]] (+0.66, fdr 1e-05); moves opposite to [[HNRNPAB]] (-0.65, fdr 1e-05), [[ENOX2]] (-0.65, fdr 2e-05), [[E2F3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); 12 go from it, the strongest it → [[LCA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +8.4 | 2e-14 | 24/41 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +8.2 | 8e-14 | 28/40 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +7.8 | 2e-12 | 25/39 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +7.1 | 2e-10 | 26/42 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +6.9 | 7e-10 | 20/42 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +5.7 | 1e-06 | 11/41 (SW 900, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +5.6 | 1e-06 | 4/7 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +5.3 | 8e-06 | 15/33 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.2 | 1e-05 | 6/16 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.2 | 1e-05 | 9/20 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +4.6 | 2e-04 | 6/20 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 9/41 (A-172, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.002 | 12/30 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +4.1 | 0.002 | 2/8 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +3.6 | 0.013 | 2/36 (PANC-1, LOX-IMVI) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.035 | 5/42 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.043 | 1/42 (PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -8.9 | 4e-16 | 26/37 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -8.4 | 1e-14 | 29/43 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.463×** | -7.0 | 6e-10 | 23/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.509×** | -6.1 | 1e-07 | 23/41 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.542×** | -5.5 | 3e-06 | 16/37 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -5.1 | 3e-05 | 12/23 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -4.8 | 1e-04 | 13/27 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.633×** | -4.1 | 0.003 | 11/41 (SW 1271, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.640×** | -3.8 | 0.009 | 11/37 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -3.7 | 0.011 | 13/37 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.660×** | -3.5 | 0.020 | 9/36 (CFPAC-1, RPMI-7951, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -3.4 | 0.031 | 11/35 (SHP-77, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -3.4 | 0.031 | 16/40 (HCT15, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.772×** | -3.3 | 0.037 | 11/42 (SNU-423, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -3.3 | 0.037 | 11/27 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.685×** | -3.3 | 0.037 | 11/36 (hTERT-HPNE, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.702×** | -3.2 | 0.047 | 9/42 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.704×** | -3.2 | 0.049 | 10/31 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -3.1 | 0.065 | 8/29 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.715×** | -3.0 | 0.069 | 10/40 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0828× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 5.83 | 0 | 1 | — | [[Tubulin inhibitor 6 (drug)]] 0.05 µM 0.0526× (z -8.6) |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.11 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0715× (z -10.8) |
| [[SW 900 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -9.2) ⚠ cell-cycle shift, explains <1% of this change |
| [[SW480 (line)]] | alt | 1.75 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0634× (z -8.5) |
| [[A-427 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | +0.74 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[USP30]] | +0.64 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[COPS4]] | +0.64 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[PIGH]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RAB3A]] | +0.64 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CAT]] | +0.63 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SNX2]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ORC4]] | +0.63 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ABHD8]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[FRRS1]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.65 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.65 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[E2F3]] | -0.64 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[DOCK1]] | -0.63 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[RBM19]] | -0.62 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[PTPRG]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[AVEN]] | -0.61 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[HCG18]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PSME3]] | -0.60 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[EPM2A]] | -0.59 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises FAM229B's level | lines that do not express EID2B (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without EID2B | 0.030 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[GXYLT2]] | B | GXYLT2 activity raises FAM229B's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without GXYLT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[GAMT]] | B | GAMT activity raises FAM229B's level | lines that do not express GAMT (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without GAMT | 0.062 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[FRG1FP]] | B | FRG1FP activity raises FAM229B's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without FRG1FP | 0.079 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent |
| [[PKIG]] | B | PKIG activity raises FAM229B's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PKIG | 0.088 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[ZNF404]] | B | ZNF404 activity raises FAM229B's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 2.16× lower at baseline in the lines without ZNF404 | 0.0999 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |
| [[MPP2]] | C | MPP2 activity raises FAM229B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.54× lower at baseline in the lines without MPP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LCA5]] | B | FAM229B activity raises LCA5's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 2.96× lower at baseline in the lines without FAM229B | 0.054 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[NAT14]] | B | FAM229B activity raises NAT14's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without FAM229B | 0.054 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[TTLL7]] | B | FAM229B activity raises TTLL7's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 4.33× lower at baseline in the lines without FAM229B | 0.056 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[ZCRB1]] | B | FAM229B activity raises ZCRB1's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without FAM229B | 0.057 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[MBD3]] | B | FAM229B activity raises MBD3's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without FAM229B | 0.060 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[AFTPH]] | B | FAM229B activity lowers AFTPH's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.27× higher at baseline in the lines without FAM229B | 0.067 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[GXYLT2]] | B | FAM229B activity raises GXYLT2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 4.64× lower at baseline in the lines without FAM229B | 0.076 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[REEP2]] | B | FAM229B activity raises REEP2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without FAM229B | 0.085 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[FAM104B]] | B | FAM229B activity raises FAM104B's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without FAM229B | 0.086 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[GPCPD1]] | B | FAM229B activity lowers GPCPD1's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.68× higher at baseline in the lines without FAM229B | 0.088 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[SNX2]] | B | FAM229B activity raises SNX2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without FAM229B | 0.090 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[MPP2]] | C | FAM229B activity raises MPP2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 4.01× lower at baseline in the lines without FAM229B | 0.040 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (0.1, -9.8); signed map (-28.6, -8.6). **Vector** length 56.5, 9.35% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.9 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 229 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:112,087,591-112,102,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586F0922, LOC619208; previously C6orf225 |
| Matched by | ensembl_id |

UniProt [Q4G0N7](https://www.uniprot.org/uniprotkb/Q4G0N7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33858) · Entrez [619208](https://www.ncbi.nlm.nih.gov/gene/619208) · UniProt [Q4G0N7](https://www.uniprot.org/uniprotkb/Q4G0N7) · Ensembl [ENSG00000203778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203778)

## Data

Gene col 12787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12787); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12787]; `tensor/DDL_lfc|DDL_z.npy` [12787]; `embed/gene_vectors.npy` [12787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12787 or target_col == 12787). Every well: [[FAM229B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM229B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
