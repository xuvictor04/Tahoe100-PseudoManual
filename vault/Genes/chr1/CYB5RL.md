---
symbol: "CYB5RL"
type: "gene"
col: 13279
ensembl_id: "ENSG00000215883"
name: "cytochrome b5 reductase 5 (putative)"
location: "1p32.3"
module: 51
arm: "+"
pooled_cpm: 6.02
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# CYB5RL

*cytochrome b5 reductase 5 (putative)* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.03× (z +12.0, q 2e-30, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.587× (z -5.8, q 2e-06, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXRED2]] (+0.70, fdr 7e-06), [[DHRS4L2]] (+0.61, fdr 7e-06), [[WDSUB1]] (+0.57, fdr 1e-05); moves opposite to [[PRDX1]] (-0.51, fdr 4e-05), [[LYG1]] (-0.50, fdr 4e-04), [[UBE2F-SCLY]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RDM1P5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +12.0 | 2e-30 | 38/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +10.4 | 6e-23 | 37/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +10.1 | 1e-21 | 19/22 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +9.2 | 5e-18 | 8/9 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +9.0 | 2e-17 | 24/41 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +8.2 | 3e-14 | 30/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.80×** | +6.4 | 2e-08 | 28/46 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +6.3 | 2e-08 | 8/14 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +5.7 | 9e-07 | 19/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +4.7 | 2e-04 | 13/43 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +4.0 | 0.003 | 9/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 12/45 (A-172, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.003 | 13/46 (HEC-1-A, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 10/47 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 10/40 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.041 | 6/46 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.041 | 1/46 (MIA PaCa-2) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.067 | 11/46 (NCI-H23, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -5.8 | 2e-06 | 21/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -5.8 | 2e-06 | 20/46 (HT-29, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.570×** | -5.7 | 2e-06 | 21/43 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -5.7 | 2e-06 | 21/46 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -5.5 | 5e-06 | 22/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.615×** | -5.2 | 1e-05 | 20/46 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -4.9 | 8e-05 | 13/37 (COLO 205, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.701×** | -3.8 | 0.009 | 15/46 (H4, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.704×** | -3.8 | 0.010 | 15/46 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.070 | 12/46 (SW480, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.076 | 17/45 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -3.1 | 0.096 | 11/44 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.96 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0750× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[SW480 (line)]] | alt | 9.49 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.222× (z -9.4) |
| [[COLO 205 (line)]] | alt | 8.54 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0823× (z -8.9) |
| [[Hs 766T (line)]] | wt | 4.93 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0658× (z -8.7) |
| [[KATO III (line)]] | alt | 9.13 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.120× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0553× (z -8.5) |
| [[RKO (line)]] | wt | 6.12 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0923× (z -8.8) ⚠ transcription drop; unreliable plate only |
| [[SNU-423 (line)]] | alt | 5.26 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0986× (z -8.6) |
| [[A-172 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXRED2]] | +0.70 | +0.77 / +0.68 | both halves | 7e-06 | same gene group |
| [[DHRS4L2]] | +0.61 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[WDSUB1]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SETDB2]] | +0.55 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PATL1]] | +0.54 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[ALDH5A1]] | +0.53 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ASXL1]] | +0.53 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[CHDH]] | +0.53 | +0.46 / +0.61 | both halves | 3e-05 | same gene group |
| [[SPPL3]] | +0.53 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[CDK4]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[C2CD5]] | +0.52 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[ALG1]] | +0.52 | +0.68 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LYG1]] | -0.50 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[UBE2F-SCLY]] | -0.50 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[RHOC]] | -0.50 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[GAN]] | -0.50 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[SNX29]] | -0.50 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[HEATR5A]] | -0.49 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[ELOVL1]] | -0.49 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PCYT1A]] | -0.49 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[C9orf24]] | -0.48 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[AAK1]] | -0.46 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[CCDC168]] | -0.46 | -0.30 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises CYB5RL's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without RDM1P5 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises CYB5RL's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.25× lower at baseline in the lines without MYT1 | 0.086 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[PSMB5]] | B | PSMB5 activity raises CYB5RL's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FOXRED2]] | C | FOXRED2 activity raises CYB5RL's level | lines that do not express FOXRED2 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without FOXRED2 | 0.049 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[ZFHX2]] | C | ZFHX2 activity raises CYB5RL's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without ZFHX2 | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.2, 32.3); signed map (31.1, -28.8). **Vector** length 52.0, 6.96% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.3 | +4.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -5.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 reductase 5 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,169,651-54,200,036 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYB5R5, LOC606495; previously CYB5RL |
| Gene groups (HGNC) | Cytochrome b5 reductases; Flavoproteins |
| Reactome | 3 pathways, smallest: Erythrocytes take up carbon dioxide and release oxygen; O2/CO2 exchange in erythrocytes; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IPT4](https://www.uniprot.org/uniprotkb/Q6IPT4) (NADH-cytochrome b5 reductase-like):

> Putative NADH-cytochrome b5 reductases family protein. May participate in fatty acid desaturation and elongation, cholesterol biosynthesis, drug metabolism, and, in erythrocyte, methemoglobin reduction.

**Summary**, from NCBI Gene [606495](https://www.ncbi.nlm.nih.gov/gene/606495):

> Predicted to enable oxidoreductase activity. Predicted to be involved in bicarbonate transport. Predicted to be located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32220) · Entrez [606495](https://www.ncbi.nlm.nih.gov/gene/606495) · UniProt [Q6IPT4](https://www.uniprot.org/uniprotkb/Q6IPT4) · Ensembl [ENSG00000215883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215883)

## Data

Gene col 13279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13279); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13279]; `tensor/DDL_lfc|DDL_z.npy` [13279]; `embed/gene_vectors.npy` [13279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13279 or target_col == 13279). Every well: [[CYB5RL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5RL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
