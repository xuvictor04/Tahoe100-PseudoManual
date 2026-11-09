---
symbol: "TBX18"
type: "gene"
col: 3410
ensembl_id: "ENSG00000112837"
name: "T-box transcription factor 18"
location: "6q14.3"
module: 108
arm: "+"
pooled_cpm: 18.83
n_lines_expressing: 23
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 12
direction_downstream: 12
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# TBX18

*T-box transcription factor 18* — 6q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +15.6, q 0e+00, up in 11 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.531× (z -8.4, q 3e-14, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HECW2]] (+0.57, fdr 1e-04), [[GPC6]] (+0.54, fdr 1e-05), [[PAX3]] (+0.53, fdr 1e-05); moves opposite to [[LASTR]] (-0.48, fdr 1e-04), [[ZDHHC11B]] (-0.45, fdr 1e-04), [[SEC11C]] (-0.42, fdr 3e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[PCOLCE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +15.6 | 0e+00 | 11/20 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.7 | 8e-09 | 1/18 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.0 | 1e-04 | 0/19 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.011 | 6/20 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.040 | 5/21 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.049 | 3/21 (C32, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.062 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.12 | 8/21 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -8.4 | 3e-14 | 18/20 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.555×** | -7.8 | 2e-12 | 15/21 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.575×** | -7.3 | 5e-11 | 14/21 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.682×** | -7.2 | 1e-10 | 18/20 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -7.0 | 3e-10 | 14/21 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.601×** | -6.8 | 1e-09 | 18/21 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.599×** | -6.5 | 5e-09 | 17/20 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -5.1 | 2e-05 | 12/21 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -5.0 | 4e-05 | 19/21 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.714×** | -4.5 | 5e-04 | 13/21 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.726×** | -4.2 | 0.001 | 10/21 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.721×** | -4.2 | 0.001 | 5/21 (SHP-77, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -4.0 | 0.003 | 15/21 (C32, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.749×** | -3.8 | 0.005 | 8/20 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |
| [[Aspirin (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.007 | 2/21 (NCI-H2030, A549) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -3.5 | 0.015 | 10/21 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.038 | 2/21 (SNU-423, J82) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.790×** | -3.1 | 0.053 | 5/21 (SNU-423, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.3 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.220× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 39.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -21.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -8.9) |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -10.4) |
| [[A-427 (line)]] | wt | 56.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0351× (z -13.2) |
| [[C32 (line)]] | wt | 32.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.247× (z -8.7) |
| [[SHP-77 (line)]] | alt | 98.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0512× (z -11.3) |
| [[A549 (line)]] | wt | 59.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.7) | [[TAK-901 (drug)]] 5 µM 0.0599× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 7.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.4) | — |
| [[A-172 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECW2]] | +0.57 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[GPC6]] | +0.54 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PAX3]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC01139]] | +0.52 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[CNRIP1]] | +0.51 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[NETO1]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[FGF14]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[STEAP1B]] | +0.48 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[BASP1-AS1]] | +0.48 | +0.48 / +0.31 | both halves | 2e-04 |  |
| [[LINC03041]] | +0.48 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[ZNF804A]] | +0.48 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[CARD18]] | +0.48 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LASTR]] | -0.48 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ZDHHC11B]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[SEC11C]] | -0.42 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[MCTP2]] | -0.42 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[TMEM125]] | -0.41 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[EZR]] | -0.41 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[HMSD]] | -0.41 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[DPF1]] | -0.40 | -0.37 / -0.22 | both halves | 6e-04 |  |
| [[NET1]] | -0.40 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[CREB3]] | -0.39 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[TTC3]] | -0.38 | -0.32 / -0.26 | both halves | 4e-04 |  |
| [[TPPP]] | -0.38 | -0.29 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TBX18's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC2A10]] | B | SLC2A10 activity lowers TBX18's level | lines that do not express SLC2A10 (18) vs lines expressing it (32) | 2.95× higher at baseline in the lines without SLC2A10 | 0.069 | ⚠ within organs, on part of the lines; also absent: SARDH, CSF1 |
| [[ZFHX4]] | C | ZFHX4 activity raises TBX18's level | lines that do not express ZFHX4 (23) vs lines expressing it (27) | 4.00× lower at baseline in the lines without ZFHX4 | 0.010 | ⚠ within organs, on part of the lines; also absent: SNCA, UCHL1, SLITRK5; co-absent with the target |
| [[GLIS3]] | C | GLIS3 activity raises TBX18's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 3.13× lower at baseline in the lines without GLIS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises TBX18's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 3.82× lower at baseline in the lines without NCKAP5-AS2 | 0.034 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[LRRK2]] | C | LRRK2 activity raises TBX18's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 4.34× lower at baseline in the lines without LRRK2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[FGF14]] | C | FGF14 activity raises TBX18's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 4.69× lower at baseline in the lines without FGF14 | 0.053 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[WNT5B]] | C | WNT5B activity raises TBX18's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 3.83× lower at baseline in the lines without WNT5B | 0.059 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |
| [[ANTXR1]] | C | ANTXR1 activity raises TBX18's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 4.08× lower at baseline in the lines without ANTXR1 | 0.062 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises TBX18's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.76× lower at baseline in the lines without PAPPA | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[NNMT]] | C | NNMT activity raises TBX18's level | lines that do not express NNMT (24) vs lines expressing it (26) | 3.37× lower at baseline in the lines without NNMT | 0.088 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises TBX18's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.41× lower at baseline in the lines without MSC-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCOLCE2]] | B | TBX18 activity raises PCOLCE2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.58× lower at baseline in the lines without TBX18 | 0.012 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[SLC2A10]] | B | TBX18 activity lowers SLC2A10's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.65× higher at baseline in the lines without TBX18 | 0.036 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[BVES-AS1]] | B | TBX18 activity raises BVES-AS1's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without TBX18 | 0.050 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[EPM2A]] | B | TBX18 activity raises EPM2A's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 1.52× lower at baseline in the lines without TBX18 | 0.059 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[THSD7A]] | B | TBX18 activity raises THSD7A's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without TBX18 | 0.093 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[LRRK2]] | C | TBX18 activity raises LRRK2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.80× lower at baseline in the lines without TBX18 | 0.025 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[PAPPA]] | C | TBX18 activity raises PAPPA's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 4.26× lower at baseline in the lines without TBX18 | 0.026 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[ANTXR1]] | C | TBX18 activity raises ANTXR1's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without TBX18 | 0.027 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[ZNF804A]] | C | TBX18 activity raises ZNF804A's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 4.27× lower at baseline in the lines without TBX18 | 0.043 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[HECW2]] | C | TBX18 activity raises HECW2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without TBX18 | 0.063 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[NLGN1]] | C | TBX18 activity raises NLGN1's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 3.89× lower at baseline in the lines without TBX18 | 0.088 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[NCKAP5-AS2]] | C | TBX18 activity raises NCKAP5-AS2's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 1.65× lower at baseline in the lines without TBX18 | 0.098 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.414). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.1, 28.1); signed map (35.7, 41.4). **Vector** length 63.2, 19.2% of its response variance represented; |z| ≥ 3 in 472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.5 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.0 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.6 | -4.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.3 — chr6:84,687,351-84,764,598 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | T-box transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95935](https://www.uniprot.org/uniprotkb/O95935) (T-box transcription factor TBX18):

> Acts as a transcriptional repressor involved in developmental processes of a variety of tissues and organs, including the heart and coronary vessels, the ureter and the vertebral column. Required for embryonic development of the sino atrial node (SAN) head area.

**Summary**, from NCBI Gene [9096](https://www.ncbi.nlm.nih.gov/gene/9096):

> This genes codes for a member of an evolutionarily conserved family of transcription factors that plays a crucial role in embryonic development. The family is characterized by the presence of the DNA-binding T-box domain and is divided into five sub-families based on sequence conservation in this domain. The encoded protein belongs to the vertebrate specific Tbx1 sub-family. The protein acts as a transcriptional repressor by antagonizing transcriptional activators in the T-box family. The …

**Accessions** — [HGNC:11595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11595) · Entrez [9096](https://www.ncbi.nlm.nih.gov/gene/9096) · UniProt [O95935](https://www.uniprot.org/uniprotkb/O95935) · Ensembl [ENSG00000112837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112837)

## Data

Gene col 3410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3410); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3410]; `tensor/DDL_lfc|DDL_z.npy` [3410]; `embed/gene_vectors.npy` [3410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3410 or target_col == 3410). Every well: [[TBX18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
