---
symbol: "CXXC4"
type: "gene"
col: 9695
ensembl_id: "ENSG00000168772"
name: "CXXC finger protein 4"
location: "4q24"
module: 223
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 25
n_dd_up: 29
n_dd_down: 20
n_dd_up_clean: 19
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# CXXC4

*CXXC finger protein 4* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.17× (z +12.9, q 4e-35, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.476× (z -5.9, q 2e-06, down in 18 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRC4-KLRK1]] (+0.68, fdr 7e-06), [[KLRK1]] (+0.68, fdr 7e-06), [[KLRC3]] (+0.67, fdr 7e-06); moves opposite to [[TPD52L2]] (-0.58, fdr 1e-05), [[MYO9B]] (-0.48, fdr 2e-05), [[ZFYVE21]] (-0.47, fdr 4e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ESRRG]] → it (grade C ⚠); 4 go from it, the strongest it → [[PBX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.17×** | +12.9 | 4e-35 | 14/23 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.01×** | +10.1 | 1e-21 | 2/9 (CFPAC-1, SW 900) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +9.9 | 5e-21 | 2/7 (NCI-H2347, A498) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +8.6 | 9e-16 | 4/12 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.81×** | +8.2 | 4e-14 | 13/20 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.42×** | +7.0 | 3e-10 | 13/23 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.99×** | +5.4 | 5e-06 | 15/23 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.2 | 1e-05 | 2/17 (A498, LS 180) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 8/22 (SW 900, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.3 | 1e-03 | 2/11 (SHP-77, NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.67×** | +3.8 | 0.008 | 10/21 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.60×** | +3.7 | 0.011 | 3/22 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.017 | 8/20 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.017 | 8/19 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.019 | 5/20 (HT-29, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.029 | 1/18 (NCI-H460) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.031 | 5/21 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.037 | 1/23 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.052 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -5.9 | 2e-06 | 18/22 (C-33 A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.628×** | -5.2 | 5e-05 | 17/21 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.528×** | -5.1 | 7e-05 | 17/22 (AN3 CA, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.531×** | -4.7 | 3e-04 | 16/20 (AN3 CA, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.553×** | -4.7 | 3e-04 | 14/21 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.547×** | -4.5 | 6e-04 | 14/22 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -4.5 | 6e-04 | 15/23 (NCI-H460, C-33 A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.571×** | -4.5 | 6e-04 | 9/23 (CHP-212, NCI-H1573, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.565×** | -4.4 | 8e-04 | 6/23 (CFPAC-1, NCI-H23, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.600×** | -4.1 | 0.003 | 11/23 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.595×** | -3.9 | 0.005 | 13/22 (C-33 A, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.644×** | -3.5 | 0.022 | 11/23 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.636×** | -3.5 | 0.023 | 15/21 (HT-29, NCI-H2030, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.648×** | -3.4 | 0.023 | 10/23 (SW 900, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.627×** | -3.4 | 0.023 | 4/21 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.555×** | -3.3 | 0.030 | 6/23 (NCI-H460, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.453×** | -3.3 | 0.034 | 7/20 (NCI-H460, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.678×** | -3.1 | 0.062 | 12/18 (NCI-H661, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 94.6 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 23.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.153× (z -11.6) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 5.32 | 0 | 2 | — | [[Peretinoin (drug)]] 5 µM 0.0644× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 3.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0498× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 4.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0473× (z -9.8) |
| [[NCI-H661 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0561× (z -10.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.516 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRC4-KLRK1]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[KLRK1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[KLRC3]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[KLRC2]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[NR4A3]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SLITRK6]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PBX1]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ID4]] | +0.57 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[CFH]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZFYVE21]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MFN1]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SPRYD3]] | -0.46 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[RARS2]] | -0.46 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRRG]] | C | ESRRG activity raises CXXC4's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without ESRRG | 0.048 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent; co-absent with the target |
| [[NOVA1]] | C | NOVA1 activity raises CXXC4's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without NOVA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[SOX2]] | C | SOX2 activity raises CXXC4's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.85× lower at baseline in the lines without SOX2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises CXXC4's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.67× lower at baseline in the lines without KCNH5 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBX1]] | B | CXXC4 activity raises PBX1's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without CXXC4 | 0.091 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1 |
| [[RHOV]] | B | CXXC4 activity raises RHOV's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without CXXC4 | 0.095 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1 |
| [[LINC01876]] | C | CXXC4 activity raises LINC01876's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 3.52× lower at baseline in the lines without CXXC4 | 0.006 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1; co-absent with the target |
| [[FOXP2]] | C | CXXC4 activity raises FOXP2's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without CXXC4 | 0.073 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1; co-absent with the target |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.6, 33.5); signed map (51.2, 19.9). **Vector** length 50.4, 11.3% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.8 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.1 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.1 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -3.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | CXXC finger protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:104,468,308-104,494,901 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IDAX |
| Gene groups (HGNC) | Zinc fingers CXXC-type |
| Reactome | 3 pathways, smallest: Negative regulation of TCF-dependent signaling by DVL-interacting proteins; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2H0](https://www.uniprot.org/uniprotkb/Q9H2H0) (CXXC-type zinc finger protein 4):

> Acts as a negative regulator of the Wnt signaling pathway via its interaction with DVL1 (By similarity). Binds preferentially to DNA containing cytidine-phosphate-guanosine (CpG) dinucleotides over CpH (H=A, T, and C), hemimethylated-CpG and hemimethylated-hydroxymethyl-CpG.

**Summary**, from NCBI Gene [80319](https://www.ncbi.nlm.nih.gov/gene/80319):

> This gene encodes a CXXC-type zinc finger domain-containing protein that functions as an antagonist of the canonical wingless/integrated signaling pathway. The encoded protein negatively regulates wingless/integrated signaling through interaction with the post synaptic density protein/ Drosophila disc large tumor suppressor/ zonula occludens-1 protein domain of Dishevelled, a scaffolding protein required for the stabilization of the transcriptional co-activator beta-catenin. In addition, the …

**Accessions** — [HGNC:24593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24593) · Entrez [80319](https://www.ncbi.nlm.nih.gov/gene/80319) · UniProt [Q9H2H0](https://www.uniprot.org/uniprotkb/Q9H2H0) · Ensembl [ENSG00000168772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168772)

## Data

Gene col 9695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9695); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9695]; `tensor/DDL_lfc|DDL_z.npy` [9695]; `embed/gene_vectors.npy` [9695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9695 or target_col == 9695). Every well: [[CXXC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXXC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
