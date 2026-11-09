---
symbol: "CCDC102B"
type: "gene"
col: 7449
ensembl_id: "ENSG00000150636"
name: "coiled-coil domain containing 102B"
location: "18q22.1"
module: 108
arm: "+"
pooled_cpm: 17.96
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# CCDC102B

*coiled-coil domain containing 102B* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.83× (z +5.6, q 2e-05, up in 20 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.302× (z -11.0, q 3e-25, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02211]] (+0.63, fdr 7e-06), [[ADGRB3]] (+0.61, fdr 1e-05), [[PRR16]] (+0.59, fdr 1e-05); moves opposite to [[PHLPP2]] (-0.47, fdr 6e-05), [[SLC37A1]] (-0.43, fdr 6e-05), [[GAN]] (-0.42, fdr 5e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ALS2CL]] → it (grade B ⚠); 4 go from it, the strongest it → [[CCDC7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +5.6 | 2e-05 | 20/39 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.5 | 0.002 | 16/39 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.009 | 19/38 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.031 | 15/39 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.71×** | +3.6 | 0.031 | 13/39 (HOP62, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.063 | 13/38 (J82, C32, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.42× | +3.2 | 0.11 | 9/39 (J82, SW 1088, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.13 | 12/38 (MIA PaCa-2, HepG2/C3A, …) | two highest doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.44× | +3.1 | 0.13 | 5/37 (HCT15, NCI-H460, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.302×** | -11.0 | 3e-25 | 37/39 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.453×** | -10.3 | 3e-22 | 32/38 (NCI-H460, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -9.4 | 1e-18 | 28/36 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.387×** | -8.7 | 5e-16 | 34/39 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.398×** | -8.4 | 4e-15 | 30/38 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.415×** | -8.0 | 8e-14 | 27/36 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.575×** | -5.1 | 3e-05 | 22/38 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.679×** | -5.0 | 4e-05 | 22/39 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.580×** | -5.0 | 4e-05 | 24/39 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.570×** | -4.9 | 4e-05 | 24/38 (hTERT-HPNE, J82, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.577×** | -4.8 | 9e-05 | 23/37 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.595×** | -4.8 | 9e-05 | 22/39 (H4, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -4.4 | 5e-04 | 18/39 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -4.2 | 9e-04 | 15/38 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.651×** | -3.9 | 0.003 | 15/38 (H4, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.454×** | -3.8 | 0.005 | 19/36 (LOX-IMVI, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.663×** | -3.8 | 0.005 | 18/38 (H4, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.005 | 17/38 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.576×** | -3.7 | 0.006 | 17/39 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.682×** | -3.5 | 0.013 | 11/39 (BT-474, hTERT-HPNE, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.701×** | -3.2 | 0.030 | 16/39 (hTERT-HPNE, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.8 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -14.1) |
| [[H4 (line)]] | wt | 84.1 | 0 | 10 (6 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0307× (z -11.9) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 0.0337× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.00880× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0207× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 74.2 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 56.3 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.129× (z -12.0) |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -9.5) |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0384× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.155× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0699× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -8.6) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 9.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 9.59 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0674× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -15.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0911× (z -9.9) |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02211]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ADGRB3]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[PRR16]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[MIR3171HG]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ACSS3]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[PCDHGA2]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ANTXR1]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZNF471]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PDE3A]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[C2orf74-DT]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TCF4]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PDGFRB]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLPP2]] | -0.47 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[SLC37A1]] | -0.43 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GAN]] | -0.42 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[DAPK1]] | -0.41 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ALS2CL]] | -0.40 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ARHGEF34P]] | -0.40 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[LPAR5]] | -0.40 | -0.40 / -0.22 | both halves | 6e-04 |  |
| [[PTK6]] | -0.39 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[PROM1]] | -0.39 | -0.40 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALS2CL]] | B | ALS2CL activity lowers CCDC102B's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.65× higher at baseline in the lines without ALS2CL | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[ADGRB3]] | B | ADGRB3 activity raises CCDC102B's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.11× lower at baseline in the lines without ADGRB3 | 0.033 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[DAPK1]] | B | DAPK1 activity lowers CCDC102B's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.85× higher at baseline in the lines without DAPK1 | 0.036 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[GLIS1]] | B | GLIS1 activity raises CCDC102B's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without GLIS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent |
| [[PAPPA]] | B | PAPPA activity strengthens CCDC102B's drug response | lines that do not express PAPPA (25) vs lines expressing it (14) | the lines without PAPPA respond 0.66× as strongly (z diff +1.37); strongest at Vinblastine (sulfate) 5 µM: 0.71x vs 0.43x (z diff +3.0) | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CCDC102B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PRR16]] | B | PRR16 activity raises CCDC102B's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.12× lower at baseline in the lines without PRR16 | 0.069 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2 |
| [[PAX3]] | B | PAX3 activity raises CCDC102B's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 3.47× lower at baseline in the lines without PAX3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168 |
| [[MSRB3]] | B | MSRB3 activity raises CCDC102B's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.75× lower at baseline in the lines without MSRB3 | 0.075 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[LPAR5]] | B | LPAR5 activity lowers CCDC102B's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.24× higher at baseline in the lines without LPAR5 | 0.092 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[PCBP3]] | B | PCBP3 activity raises CCDC102B's level | lines that do not express PCBP3 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without PCBP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SDK1, RBM20, ANO4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC7]] | B | CCDC102B activity raises CCDC7's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without CCDC102B | 0.008 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[PRDX6-AS1]] | B | CCDC102B activity raises PRDX6-AS1's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without CCDC102B | 0.024 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[TBC1D32]] | B | CCDC102B activity raises TBC1D32's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without CCDC102B | 0.042 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[PTPRD]] | B | CCDC102B activity raises PTPRD's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 4.29× lower at baseline in the lines without CCDC102B | 0.054 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.2, 22.5); signed map (34.7, 43.9). **Vector** length 81.0, 18.6% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | -9.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.0 | -3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.0 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 102B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:68,715,209-69,055,189 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23594, HsT1731, AN; previously C18orf14, ACY1L |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68D86](https://www.uniprot.org/uniprotkb/Q68D86) (Coiled-coil domain-containing protein 102B):

> During interphase, forms fibers at the proximal ends of centrioles to maintain centrosome cohesion. During mitosis, dissociates from the centrosome following phosphorylation to allow centrosome separation. Contributes to CROCC/rootletin filament formation.

**Summary**, from NCBI Gene [79839](https://www.ncbi.nlm.nih.gov/gene/79839):

> Enables protein serine/threonine kinase binding activity. Involved in centriole-centriole cohesion. Located in centriole. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26295) · Entrez [79839](https://www.ncbi.nlm.nih.gov/gene/79839) · UniProt [Q68D86](https://www.uniprot.org/uniprotkb/Q68D86) · Ensembl [ENSG00000150636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150636)

## Data

Gene col 7449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7449); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7449]; `tensor/DDL_lfc|DDL_z.npy` [7449]; `embed/gene_vectors.npy` [7449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7449 or target_col == 7449). Every well: [[CCDC102B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC102B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
