---
symbol: "SYTL5"
type: "gene"
col: 7141
ensembl_id: "ENSG00000147041"
name: "synaptotagmin like 5"
location: "Xp11.4"
module: 235
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 30
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 14
direction_downstream: 18
tags: ["gene", "module/235"]
generated_by: "tahoemap"
---

# SYTL5

*synaptotagmin like 5* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.07× (z +9.0, q 1e-16, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.04× (z +8.4, q 1e-14, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.614× (z -5.8, q 5e-06, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC14A1]] (+0.66, fdr 7e-06), [[COL13A1]] (+0.54, fdr 1e-05), [[ADAM19]] (+0.54, fdr 1e-05); moves opposite to [[SLC19A2]] (-0.48, fdr 4e-05), [[MEAF6]] (-0.47, fdr 3e-05), [[SH3BP4]] (-0.45, fdr 1e-04).
> It is in [[Module 235]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[KIAA0040]] → it (grade B ⚠); 18 go from it, the strongest it → [[ABHD17C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +9.0 | 1e-16 | 1/4 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +8.4 | 1e-14 | 15/26 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +7.1 | 2e-10 | 2/5 (SNU-423, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +5.9 | 6e-07 | 9/24 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.0 | 7e-05 | 6/13 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.007 | 6/26 (A-172, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.016 | 1/23 (PANC-1) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.078 | 4/26 (BT-474, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, none with an alert; shown: the 15 strongest. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.614×** | -5.8 | 5e-06 | 17/25 (BT-474, H4, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.653×** | -5.0 | 1e-04 | 13/27 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.550×** | -5.0 | 1e-04 | 14/25 (AsPC-1, C32, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.559×** | -4.6 | 7e-04 | 13/25 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.582×** | -4.5 | 7e-04 | 10/27 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **0.606×** | -4.2 | 0.003 | 11/26 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.632×** | -3.8 | 0.010 | 9/24 (SW1417, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.738×** | -3.6 | 0.020 | 10/25 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.631×** | -3.6 | 0.020 | 9/25 (C32, LoVo, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.653×** | -3.6 | 0.020 | 10/21 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -3.5 | 0.020 | 10/25 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.665×** | -3.4 | 0.031 | 11/26 (C32, SHP-77, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM |  | **0.756×** | -3.3 | 0.037 | 10/26 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.688×** | -3.3 | 0.037 | 13/26 (SHP-77, H4, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -3.3 | 0.037 | 10/26 (HOP62, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.43 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0683× (z -12.0) |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -11.3) |
| [[KATO III (line)]] | alt | 9.13 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0432× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0353× (z -17.0) |
| [[LoVo (line)]] | wt | 4.31 | 0 | 2 | — | [[Binimetinib (drug)]] 0.5 µM 0.0843× (z -10.8) |
| [[C32 (line)]] | wt | 4.23 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0373× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 6.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0364× (z -8.9) |
| [[A-172 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.794 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.617 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC14A1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[COL13A1]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ADAM19]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CEACAM6]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ITGA3]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[PTHLH]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PAK3]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SH3TC2-DT]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[DUSP4]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[VSIG1]] | +0.53 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[CEMIP]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SPTSSB]] | +0.52 | +0.36 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC19A2]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MEAF6]] | -0.47 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SH3BP4]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[SORBS2]] | -0.44 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[BATF]] | -0.44 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[FLVCR2]] | -0.43 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PLEKHM2]] | -0.43 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[PAAF1]] | -0.42 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[UBE2E1]] | -0.42 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[VPS37A]] | -0.42 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[MT1M]] | -0.42 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0040]] | B | KIAA0040 activity raises SYTL5's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.84× lower at baseline in the lines without KIAA0040 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[ABHD17C]] | B | ABHD17C activity raises SYTL5's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without ABHD17C | 0.043 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[FGFBP1]] | B | FGFBP1 activity raises SYTL5's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 1.51× lower at baseline in the lines without FGFBP1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[TRIB2]] | B | TRIB2 activity raises SYTL5's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without TRIB2 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers SYTL5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[CEACAM5]] | C | CEACAM5 activity raises SYTL5's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.49× lower at baseline in the lines without CEACAM5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises SYTL5's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 2.89× lower at baseline in the lines without SLC14A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises SYTL5's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 2.27× lower at baseline in the lines without CEACAM6 | 0.008 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[DUSP4]] | C | DUSP4 activity raises SYTL5's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without DUSP4 | 0.029 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises SYTL5's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 1.60× lower at baseline in the lines without COL17A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[PAK3]] | C | PAK3 activity raises SYTL5's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without PAK3 | 0.039 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[SHC4]] | C | SHC4 activity raises SYTL5's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without SHC4 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 11, C 7. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | SYTL5 activity raises ABHD17C's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without SYTL5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[TRIB2]] | B | SYTL5 activity raises TRIB2's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 3.13× lower at baseline in the lines without SYTL5 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[NYAP2]] | B | SYTL5 activity raises NYAP2's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without SYTL5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[TSPAN1]] | B | SYTL5 activity raises TSPAN1's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without SYTL5 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[GALNT5]] | B | SYTL5 activity raises GALNT5's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without SYTL5 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[SLC19A2]] | B | SYTL5 activity raises SLC19A2's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without SYTL5 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[MIR3681HG]] | B | SYTL5 activity raises MIR3681HG's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without SYTL5 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[MEAF6]] | B | SYTL5 activity lowers MEAF6's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 1.40× higher at baseline in the lines without SYTL5 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[SLC19A2]] | B | SYTL5 activity strengthens SLC19A2's drug response | lines that do not express SYTL5 (19) vs lines expressing it (28) | the lines without SYTL5 respond 0.66× as strongly (z diff +1.32); strongest at Homoharringtonine 5 µM: 1.28x vs 1.74x (z diff +2.4) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400; target measured in part of the lines; artifact flags |
| cells under [[Trifluridine (drug)]] 5 µM | B | SYTL5 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express SYTL5 (20) vs lines expressing it (28) | the lines without SYTL5: 0.91× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[PLA2G4A]] | B | SYTL5 activity raises PLA2G4A's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without SYTL5 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[CEMIP]] | C | SYTL5 activity raises CEMIP's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 4.29× lower at baseline in the lines without SYTL5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400; co-absent with the target |

## Where it sits

- **Module**: [[Module 235]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.7, 6.5); signed map (7.3, 51.4). **Vector** length 68.9, 16.1% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.0 | +2.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:38,006,553-38,128,819 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Slp5 |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDW5](https://www.uniprot.org/uniprotkb/Q8TDW5) (Synaptotagmin-like protein 5):

> May act as Rab effector protein and play a role in vesicle trafficking. Binds phospholipids.

**Summary**, from NCBI Gene [94122](https://www.ncbi.nlm.nih.gov/gene/94122):

> The protein encoded by this gene belongs to the synaptotagmin-like (Slp) protein family, which contains a unique homology domain at the N-terminus, referred to as the Slp homology domain (SHD). The SHD functions as a binding site for Rab27A, which plays a role in protein transport. Expression of this gene is restricted to placenta and liver, suggesting that it might be involved in Rab27A-dependent membrane trafficking in specific tissues. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:15589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15589) · Entrez [94122](https://www.ncbi.nlm.nih.gov/gene/94122) · UniProt [Q8TDW5](https://www.uniprot.org/uniprotkb/Q8TDW5) · Ensembl [ENSG00000147041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147041)

## Data

Gene col 7141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7141); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7141]; `tensor/DDL_lfc|DDL_z.npy` [7141]; `embed/gene_vectors.npy` [7141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7141 or target_col == 7141). Every well: [[SYTL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYTL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
