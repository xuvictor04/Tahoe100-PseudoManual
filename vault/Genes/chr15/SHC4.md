---
symbol: "SHC4"
type: "gene"
col: 11708
ensembl_id: "ENSG00000185634"
name: "SHC adaptor protein 4"
location: "15q21.1"
module: 84
arm: "+"
pooled_cpm: 15.15
n_lines_expressing: 27
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 9
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 18
direction_downstream: 20
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# SHC4

*SHC adaptor protein 4* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +9.8, q 8e-20, up in 3 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +8.6, q 7e-16, up in 5 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.573× (z -6.1, q 5e-07, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAEP]] (+0.68, fdr 1e-05), [[COL13A1]] (+0.68, fdr 7e-06), [[KCNN4]] (+0.66, fdr 7e-06).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PLAC4]] → it (grade B ⚠); 20 go from it, the strongest it → [[TRIB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.51×** | +9.8 | 8e-20 | 3/20 (SW1417, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.41×** | +9.3 | 3e-18 | 13/24 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.40×** | +9.3 | 3e-18 | 14/24 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.6 | 7e-16 | 5/25 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.33×** | +8.6 | 8e-16 | 3/16 (SW1417, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.15×** | +8.1 | 4e-14 | 14/24 (LoVo, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.9 | 3e-13 | 16/25 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +7.7 | 1e-12 | 17/24 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.06×** | +7.1 | 8e-11 | 3/17 (SNU-423, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.2 | 9e-06 | 10/25 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.5 | 3e-04 | 6/24 (SW480, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 6e-04 | 6/23 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.001 | 11/23 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.012 | 2/24 (NCI-H460, NCI-H2030) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.023 | 3/22 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.573×** | -6.1 | 5e-07 | 19/26 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.636×** | -6.0 | 5e-07 | 17/25 (SK-MEL-2, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.547×** | -6.0 | 5e-07 | 14/24 (CFPAC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -4.8 | 2e-04 | 11/24 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.676×** | -4.2 | 0.003 | 16/24 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.680×** | -4.1 | 0.004 | 12/26 (SHP-77, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.716×** | -4.0 | 0.004 | 12/25 (CFPAC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.516×** | -3.7 | 0.016 | 9/24 (NCI-H460, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.705×** | -3.6 | 0.020 | 15/23 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.797×** | -3.4 | 0.030 | 5/25 (NCI-H460, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.030 | 15/25 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.031 | 9/26 (CFPAC-1, SHP-77, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.036 | 6/24 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.559×** | -3.2 | 0.045 | 7/21 (C32, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.045 | 3/23 (CFPAC-1, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 88.6 | 0 | 13 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~73% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.230× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 12 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.112× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.105× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 11 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.213× (z -11.3) |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 6 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0514× (z -11.8) |
| [[C32 (line)]] | wt | 123 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.359× (z -8.9) |
| [[LoVo (line)]] | wt | 4.17 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +9.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0396× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 9.36 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.29× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 1 | — | [[Niclosamide (olamine) (drug)]] 0.5 µM 0.0351× (z -10.4) |
| [[HOP62 (line)]] | alt | 38.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.117× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 6.77 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -8.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAEP]] | +0.68 | +0.57 / +0.73 | both halves | 1e-05 | **novel candidate** |
| [[COL13A1]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[KCNN4]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CLDN10-AS1]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[DUSP4]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[STX1A]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CPNE5]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[WWTR1]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[AMOTL1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.61 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 4, C 14. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | PLAC4 activity raises SHC4's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 2.66× lower at baseline in the lines without PLAC4 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[ABHD17C]] | B | ABHD17C activity raises SHC4's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without ABHD17C | 0.053 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[CYGB]] | B | CYGB activity raises SHC4's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without CYGB | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises SHC4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC16A6]] | C | SLC16A6 activity raises SHC4's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without SLC16A6 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7; co-absent with the target |
| [[PRUNE2]] | C | PRUNE2 activity raises SHC4's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without PRUNE2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[PLAT]] | C | PLAT activity raises SHC4's level | lines that do not express PLAT (28) vs lines expressing it (22) | 3.54× lower at baseline in the lines without PLAT | 0.011 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2; co-absent with the target |
| [[SUCNR1]] | C | SUCNR1 activity raises SHC4's level | lines that do not express SUCNR1 (44) vs lines expressing it (6) | 4.71× lower at baseline in the lines without SUCNR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, TBXT, ENSG00000230258; co-absent with the target |
| [[SYTL5]] | C | SYTL5 activity raises SHC4's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without SYTL5 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400; co-absent with the target |
| [[DUSP4]] | C | DUSP4 activity raises SHC4's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without DUSP4 | 0.013 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5; co-absent with the target |
| [[SERPINB11]] | C | SERPINB11 activity raises SHC4's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 3.96× lower at baseline in the lines without SERPINB11 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[SGIP1]] | C | SGIP1 activity raises SHC4's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.72× lower at baseline in the lines without SGIP1 | 0.024 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 8, C 12. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIB2]] | B | SHC4 activity raises TRIB2's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 3.03× lower at baseline in the lines without SHC4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[TNC]] | B | SHC4 activity raises TNC's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 4.26× lower at baseline in the lines without SHC4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[MANCR]] | B | SHC4 activity raises MANCR's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.31× lower at baseline in the lines without SHC4 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[ZNF697]] | B | SHC4 activity raises ZNF697's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without SHC4 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[COL13A1]] | B | SHC4 activity raises COL13A1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.82× lower at baseline in the lines without SHC4 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[MILR1]] | B | SHC4 activity raises MILR1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without SHC4 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[ABHD17C]] | B | SHC4 activity raises ABHD17C's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without SHC4 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[RASD1]] | B | SHC4 activity raises RASD1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without SHC4 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[IL19]] | C | SHC4 activity raises IL19's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without SHC4 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |
| [[SLC16A6]] | C | SHC4 activity raises SLC16A6's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.96× lower at baseline in the lines without SHC4 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |
| [[TREM1]] | C | SHC4 activity raises TREM1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without SHC4 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |
| [[CEMIP]] | C | SHC4 activity raises CEMIP's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 3.39× lower at baseline in the lines without SHC4 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.7, 6.2); signed map (6.4, 50.4). **Vector** length 93.7, 26.8% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.9 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.4 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.9 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.0 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -6.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | SHC adaptor protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:48,823,741-48,963,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RaLP, SHCD |
| Gene groups (HGNC) | SH2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6S5L8](https://www.uniprot.org/uniprotkb/Q6S5L8) (SHC-transforming protein 4):

> Activates both Ras-dependent and Ras-independent migratory pathways in melanomas. Contributes to the early phases of agrin-induced tyrosine phosphorylation of CHRNB1.

**Summary**, from NCBI Gene [399694](https://www.ncbi.nlm.nih.gov/gene/399694):

> Predicted to enable receptor tyrosine kinase binding activity. Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to act upstream of or within several processes, including apoptotic process; positive regulation of cell population proliferation; and stem cell differentiation. Predicted to be located in postsynaptic membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16743) · Entrez [399694](https://www.ncbi.nlm.nih.gov/gene/399694) · UniProt [Q6S5L8](https://www.uniprot.org/uniprotkb/Q6S5L8) · Ensembl [ENSG00000185634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185634)

## Data

Gene col 11708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11708); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11708]; `tensor/DDL_lfc|DDL_z.npy` [11708]; `embed/gene_vectors.npy` [11708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11708 or target_col == 11708). Every well: [[SHC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
