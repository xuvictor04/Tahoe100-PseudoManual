---
symbol: "KBTBD3"
type: "gene"
col: 11278
ensembl_id: "ENSG00000182359"
name: "kelch repeat and BTB domain containing 3"
location: "11q22.3"
module: 45
arm: "+"
pooled_cpm: 4.84
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 21
n_dd_up_clean: 19
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# KBTBD3

*kelch repeat and BTB domain containing 3* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.70× (z +7.8, q 3e-12, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.480× (z -7.7, q 1e-11, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX2]] (+0.74, fdr 7e-06), [[FAM229B]] (+0.74, fdr 7e-06), [[ORC4]] (+0.71, fdr 1e-05); moves opposite to [[PSME3]] (-0.74, fdr 7e-06), [[AVEN]] (-0.73, fdr 1e-05), [[ABCF2]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TCEA3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +7.8 | 3e-12 | 31/46 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +7.6 | 1e-11 | 29/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +7.5 | 1e-11 | 33/46 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.96×** | +7.0 | 3e-10 | 30/47 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.88×** | +6.6 | 5e-09 | 28/46 (HOP62, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +6.5 | 8e-09 | 28/47 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +4.7 | 2e-04 | 17/47 (AsPC-1, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 3e-04 | 9/39 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.005 | 15/44 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +3.7 | 0.012 | 6/45 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.019 | 9/45 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.019 | 6/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.036 | 4/47 (LS 180, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.046 | 10/47 (HOP62, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +3.2 | 0.046 | 6/46 (LS 180, LoVo, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.049 | 8/46 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.480×** | -7.7 | 1e-11 | 28/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.512×** | -7.0 | 8e-10 | 26/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.554×** | -6.2 | 1e-07 | 21/46 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -5.7 | 2e-06 | 17/36 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -5.1 | 4e-05 | 17/46 (NCI-H1792, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.616×** | -5.0 | 4e-05 | 17/45 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.625×** | -4.9 | 8e-05 | 21/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.624×** | -4.6 | 2e-04 | 19/45 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -4.5 | 5e-04 | 15/38 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -4.3 | 9e-04 | 17/41 (Panc 03.27, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -4.2 | 0.001 | 17/45 (NCI-H23, HCT15, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -3.9 | 0.004 | 15/43 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -3.9 | 0.004 | 18/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.712×** | -3.5 | 0.016 | 14/23 (HT-29, SNU-423, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.016 | 8/45 (RKO, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.720×** | -3.4 | 0.021 | 8/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -3.2 | 0.041 | 7/44 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.744×** | -3.1 | 0.059 | 10/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 5.58 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0806× (z -9.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0492× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0842× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 5.43 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 6.87 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.173× (z -9.2) |
| [[A-172 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[FAM229B]] | +0.74 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[ORC4]] | +0.71 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[AFTPH]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.71 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.70 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.69 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.68 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[RCOR3]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RNF114]] | +0.67 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MBIP]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.74 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[AVEN]] | -0.73 | -0.55 / -0.76 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.72 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ARMC6]] | -0.71 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[HCG18]] | -0.69 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ALG8]] | -0.68 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[E2F3]] | -0.68 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.68 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[RNASEH1]] | -0.67 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[WDR4]] | -0.67 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[PIGW]] | -0.65 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.65 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCEA3]] | B | TCEA3 activity raises KBTBD3's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.20× lower at baseline in the lines without TCEA3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers KBTBD3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PLAG1]] | B | PLAG1 activity raises KBTBD3's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without PLAG1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | KBTBD3's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | KBTBD3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.9, -9.3); signed map (-26.1, -7.8). **Vector** length 65.2, 10.3% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +3.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.1 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.8 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:106,051,098-106,077,459 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BKLHD3 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q8NAB2](https://www.uniprot.org/uniprotkb/Q8NAB2) carries no function annotation.

**Summary**, from NCBI Gene [143879](https://www.ncbi.nlm.nih.gov/gene/143879):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be located in nucleus. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22934) · Entrez [143879](https://www.ncbi.nlm.nih.gov/gene/143879) · UniProt [Q8NAB2](https://www.uniprot.org/uniprotkb/Q8NAB2) · Ensembl [ENSG00000182359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182359)

## Data

Gene col 11278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11278); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11278]; `tensor/DDL_lfc|DDL_z.npy` [11278]; `embed/gene_vectors.npy` [11278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11278 or target_col == 11278). Every well: [[KBTBD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
