---
symbol: "PID1"
type: "gene"
col: 7741
ensembl_id: "ENSG00000153823"
name: "phosphotyrosine interaction domain containing 1"
location: "2q36.3"
module: 104
arm: "+"
pooled_cpm: 38.05
n_lines_expressing: 28
n_dd_up: 51
n_dd_down: 5
n_dd_up_clean: 45
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# PID1

*phosphotyrosine interaction domain containing 1* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.97× (z +21.1, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.790× (z -4.5, q 0.005, down in 9 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNER]] (+0.83, fdr 7e-06), [[HSD11B1]] (+0.69, fdr 7e-06), [[IL1R1]] (+0.69, fdr 1e-05); moves opposite to [[PTHLH]] (-0.51, fdr 2e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HS3ST3B1]] → it (grade B ⚠); 8 go from it, the strongest it → [[HS3ST3B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 6 with an alert ⚠; shown: the 15 strongest. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.97×** | +21.1 | 0e+00 | 26/26 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.80×** | +14.5 | 7e-45 | 23/26 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.49×** | +12.8 | 4e-35 | 24/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.29×** | +11.6 | 4e-29 | 21/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.28×** | +11.6 | 6e-29 | 22/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.71×** | +11.4 | 4e-28 | 20/27 (RPMI-7951, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **2.20×** | +11.1 | 1e-26 | 21/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.19×** | +11.0 | 2e-26 | 20/26 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.21×** | +10.7 | 6e-25 | 21/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.25×** | +10.5 | 3e-24 | 20/25 (HS-578T, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.97×** | +9.5 | 8e-20 | 19/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +9.2 | 2e-18 | 19/26 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.90×** | +9.0 | 8e-18 | 20/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.85×** | +8.6 | 3e-16 | 21/26 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.79×** | +8.1 | 2e-14 | 20/27 (HS-578T, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.790×** | -4.5 | 0.005 | 9/26 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.024 | 9/27 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.032 | 14/26 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.773×** | -3.6 | 0.041 | 10/27 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.041 | 16/26 (hTERT-HPNE, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.793× | -3.3 | 0.10 | 8/26 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.652× | -3.1 | 0.13 | 10/25 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.800× | -3.0 | 0.17 | 10/26 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | 0.665× | -3.0 | 0.17 | 10/26 (NCI-H1792, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 66.5 | 19 (1 ⚠) | 1 (1 ⚠) | [[Budesonide (drug)]] 5 µM 7.78× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 100 | 20 | 0 | [[Triamcinolone (drug)]] 5 µM 4.52× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 75.1 | 18 | 0 | [[Dexamethasone (drug)]] 0.5 µM 10.4× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 79.9 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 47.3× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.216× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 149 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 269 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 30.3 | 3 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 10.1× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.0 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.65× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0565× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 61.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 12.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.65× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.09× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 94.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 18.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.62× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.59× (z +9.1) | — |
| [[LoVo (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.199× (z -9.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 10.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.43× (z +11.9) | — |
| [[A-172 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNER]] | +0.83 | +0.81 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[HSD11B1]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[IL1R1]] | +0.69 | +0.57 / +0.76 | both halves | 1e-05 |  |
| [[IRAK3]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[DCN]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[CCND3]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[CCBE1]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[TLR2]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MT1E]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TMTC1]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[NNMT]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTHLH]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST3B1]] | B | HS3ST3B1 activity raises PID1's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 3.36× lower at baseline in the lines without HS3ST3B1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[RNF144B]] | B | RNF144B activity raises PID1's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without RNF144B | 0.099 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[WNT5A]] | C | WNT5A activity raises PID1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 5.38× lower at baseline in the lines without WNT5A | 6e-04 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[DNER]] | C | DNER activity raises PID1's level | lines that do not express DNER (32) vs lines expressing it (18) | 6.19× lower at baseline in the lines without DNER | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[SNAI2]] | C | SNAI2 activity raises PID1's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 4.58× lower at baseline in the lines without SNAI2 | 0.039 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[CSF3]] | C | CSF3 activity raises PID1's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 3.95× lower at baseline in the lines without CSF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD; co-absent with the target |
| [[NTS]] | C | NTS activity raises PID1's level | lines that do not express NTS (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without NTS | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, LINC03000, ENSG00000260364; co-absent with the target |
| [[PTX3]] | C | PTX3 activity raises PID1's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 4.64× lower at baseline in the lines without PTX3 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises PID1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.54× lower at baseline in the lines without PTHLH | 0.085 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises PID1's level | lines that do not express SRGN (30) vs lines expressing it (20) | 4.04× lower at baseline in the lines without SRGN | 0.085 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST3B1]] | B | PID1 activity raises HS3ST3B1's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without PID1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[JCAD]] | B | PID1 activity raises JCAD's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.58× lower at baseline in the lines without PID1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[IL1R1]] | B | PID1 activity raises IL1R1's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.90× lower at baseline in the lines without PID1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[SOD2]] | B | PID1 activity raises SOD2's level | lines that do not express PID1 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without PID1 | 0.061 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[NAMPT]] | B | PID1 activity raises NAMPT's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without PID1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[HIPK2]] | B | PID1 activity raises HIPK2's level | lines that do not express PID1 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without PID1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[DNER]] | C | PID1 activity raises DNER's level | lines that do not express PID1 (22) vs lines expressing it (28) | 4.68× lower at baseline in the lines without PID1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600; co-absent with the target |
| [[WNT5A]] | C | PID1 activity raises WNT5A's level | lines that do not express PID1 (22) vs lines expressing it (28) | 4.34× lower at baseline in the lines without PID1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.0, 16.6); signed map (18.5, 32.5). **Vector** length 121, 37.2% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.7 | +12.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +21.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +14.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.4 | +11.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.3 | +11.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphotyrosine interaction domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:228,850,526-229,271,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NYGGF4, FLJ20701 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2X4](https://www.uniprot.org/uniprotkb/Q7Z2X4) (PTB-containing, cubilin and LRP1-interacting protein):

> Increases proliferation of preadipocytes without affecting adipocytic differentiation.

**Summary**, from NCBI Gene [55022](https://www.ncbi.nlm.nih.gov/gene/55022):

> Involved in several processes, including negative regulation of ATP biosynthetic process; negative regulation of D-glucose import across plasma membrane; and regulation of gene expression. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26084) · Entrez [55022](https://www.ncbi.nlm.nih.gov/gene/55022) · UniProt [Q7Z2X4](https://www.uniprot.org/uniprotkb/Q7Z2X4) · Ensembl [ENSG00000153823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153823)

## Data

Gene col 7741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7741); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7741]; `tensor/DDL_lfc|DDL_z.npy` [7741]; `embed/gene_vectors.npy` [7741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7741 or target_col == 7741). Every well: [[PID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
