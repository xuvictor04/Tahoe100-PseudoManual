---
symbol: "PPARGC1A"
type: "gene"
col: 3086
ensembl_id: "ENSG00000109819"
name: "PPARG coactivator 1 alpha"
location: "4p15.2"
module: 9
arm: "+"
pooled_cpm: 14.71
n_lines_expressing: 23
n_dd_up: 38
n_dd_down: 6
n_dd_up_clean: 35
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 25
direction_downstream: 22
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PPARGC1A

*PPARG coactivator 1 alpha* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.30× (z +25.5, q 0e+00, up in 17 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Mebendazole (drug)]] 5 µM: 0.653× (z -4.4, q 0.006, down in 4 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC12]] (+0.64, fdr 1e-05), [[PLXDC2]] (+0.60, fdr 1e-05), [[LNX1]] (+0.59, fdr 1e-05); moves opposite to [[NPLOC4]] (-0.49, fdr 8e-05), [[SERPINB6]] (-0.48, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[RASSF6]] → it (grade B ⚠); 22 go from it, the strongest it → [[PLCB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.30×** | +25.5 | 0e+00 | 17/19 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **4.40×** | +22.7 | 0e+00 | 19/21 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **7.27×** | +21.5 | 0e+00 | 19/20 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.56×** | +20.3 | 0e+00 | 17/20 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.40×** | +18.2 | 0e+00 | 19/20 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.20×** | +15.5 | 0e+00 | 19/20 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.01×** | +11.9 | 6e-31 | 14/19 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.04×** | +11.6 | 4e-29 | 16/19 (LS 180, J82, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +11.5 | 1e-28 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.75×** | +10.9 | 5e-26 | 18/19 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +10.2 | 1e-22 | 5/16 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +9.0 | 9e-18 | 3/12 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.76×** | +8.8 | 5e-17 | 17/21 (SW480, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +7.1 | 5e-11 | 11/21 (SW480, COLO 205, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +6.2 | 2e-08 | 13/19 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +6.2 | 2e-08 | 15/20 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.2 | 7e-06 | 2/18 (NCI-H460, J82) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 6e-05 | 8/20 (SW 900, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.653×** | -4.4 | 0.006 | 4/21 (SHP-77, CHP-212, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.758×** | -4.2 | 0.007 | 12/21 (SHP-77, COLO 205, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.669×** | -4.0 | 0.012 | 1/20 (C32) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.024 | 9/20 (SHP-77, COLO 205, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.735×** | -3.3 | 0.098 | 6/20 (HepG2/C3A, SHP-77, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.737×** | -3.3 | 0.098 | 12/20 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.743× | -3.2 | 0.11 | 9/17 (CFPAC-1, J82, …) | all doses, flat |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.747× | -3.1 | 0.11 | 2/20 (A-172, NCI-H460) | inconsistent across doses |  |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.747× | -3.1 | 0.11 | 1/20 (A-172) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.755× | -3.0 | 0.14 | 10/20 (COLO 205, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 247 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0742× (z -24.9) |
| [[J82 (line)]] | alt | 14.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +17.8) | — |
| [[SW480 (line)]] | alt | 5.12 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 8.10× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 70.7 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -14.6) |
| [[COLO 205 (line)]] | alt | 247 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 15.2 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 8.84× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 9.10 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 18.5× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 4.00 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 13.0× (z +9.1) | [[Saquinavir (drug)]] 0.5 µM 0.0871× (z -8.7) |
| [[KATO III (line)]] | alt | 71.3 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.35× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -15.7) |
| [[LoVo (line)]] | wt | 5.46 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 9.60× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0767× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 24.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +9.1) | [[Bortezomib (drug)]] 0.05 µM 0.134× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 6.20 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.35× (z +10.1) | — |
| [[A-172 (line)]] | wt | 3.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +10.4) | — |
| [[C32 (line)]] | wt | 6.84 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.81× (z +9.4) | — |
| [[H4 (line)]] | wt | 4.45 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 38.0× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -13.4) |
| [[A-427 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC12]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PLXDC2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LNX1]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.59 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[RUNX1T1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.58 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FREM2]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PRUNE2]] | +0.57 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[STXBP5L]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KCNB2]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LRFN2]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FUT9]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPLOC4]] | -0.49 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[SERPINB6]] | -0.48 | -0.35 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 10, C 15. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF6]] | B | RASSF6 activity raises PPARGC1A's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.91× lower at baseline in the lines without RASSF6 | 0.022 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[SORL1]] | B | SORL1 activity raises PPARGC1A's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.29× lower at baseline in the lines without SORL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[LNX1]] | B | LNX1 activity raises PPARGC1A's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without LNX1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[ADGRV1]] | B | ADGRV1 activity raises PPARGC1A's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without ADGRV1 | 0.064 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[KCND2]] | B | KCND2 activity raises PPARGC1A's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without KCND2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises PPARGC1A's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without LINC01876 | 0.086 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[LINC01091]] | B | LINC01091 activity raises PPARGC1A's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LINC01091 | 0.094 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity lowers PPARGC1A's level | compounds that target JAK2: 3 of 3 raise it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[CHN2]] | B | CHN2 activity raises PPARGC1A's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without CHN2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[BDKRB2]] | B | BDKRB2 activity raises PPARGC1A's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.84× lower at baseline in the lines without BDKRB2 | 0.098 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[TOX3]] | C | TOX3 activity raises PPARGC1A's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.87× lower at baseline in the lines without TOX3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises PPARGC1A's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.95× lower at baseline in the lines without TSHZ2 | 0.012 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 14, C 8. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCB1]] | B | PPARGC1A activity raises PLCB1's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without PPARGC1A | 0.018 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SPTLC3]] | B | PPARGC1A activity raises SPTLC3's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without PPARGC1A | 0.020 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[CHN2]] | B | PPARGC1A activity raises CHN2's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without PPARGC1A | 0.029 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[RASSF6]] | B | PPARGC1A activity raises RASSF6's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without PPARGC1A | 0.032 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SLC7A8]] | B | PPARGC1A activity raises SLC7A8's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without PPARGC1A | 0.042 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[CPE]] | B | PPARGC1A activity raises CPE's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without PPARGC1A | 0.048 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[RAB17]] | B | PPARGC1A activity raises RAB17's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without PPARGC1A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[ETS2]] | B | PPARGC1A activity raises ETS2's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without PPARGC1A | 0.067 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SELENOP]] | B | PPARGC1A activity raises SELENOP's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.00× lower at baseline in the lines without PPARGC1A | 0.070 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SORL1]] | B | PPARGC1A activity raises SORL1's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without PPARGC1A | 0.071 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[EFNA1]] | B | PPARGC1A activity raises EFNA1's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without PPARGC1A | 0.085 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[ADGRV1]] | B | PPARGC1A activity raises ADGRV1's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without PPARGC1A | 0.089 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 37.0); signed map (46.0, 30.5). **Vector** length 69.3, 18.0% of its response variance represented; |z| ≥ 3 in 733 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +22.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +3.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | PPARG coactivator 1 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:23,755,041-23,904,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PGC1, PGC1A, PGC-1alpha, PPARAGCIα; previously PPARGC1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | HYPOXIA |
| Reactome | 34 pathways, smallest: Regulation of MITF-M dependent genes involved in metabolism; Activation of PPARGC1A (PGC-1alpha) by phosphorylation; FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBK2](https://www.uniprot.org/uniprotkb/Q9UBK2) (Peroxisome proliferator-activated receptor gamma coactivator 1-alpha):

> Transcriptional coactivator for steroid receptors and nuclear receptors. Greatly increases the transcriptional activity of PPARG and thyroid hormone receptor on the uncoupling protein promoter. Can regulate key mitochondrial genes that contribute to the program of adaptive thermogenesis. Plays an essential role in metabolic reprogramming in response to dietary availability through coordination of the expression of a wide array of genes involved in glucose and fatty acid metabolism. Acts as a …

**Summary**, from NCBI Gene [10891](https://www.ncbi.nlm.nih.gov/gene/10891):

> The protein encoded by this gene is a transcriptional coactivator that regulates the genes involved in energy metabolism. This protein interacts with PPARgamma, which permits the interaction of this protein with multiple transcription factors. This protein can interact with, and regulate the activities of, cAMP response element binding protein (CREB) and nuclear respiratory factors (NRFs). It provides a direct link between external physiological stimuli and the regulation of mitochondrial …

**Accessions** — [HGNC:9237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9237) · Entrez [10891](https://www.ncbi.nlm.nih.gov/gene/10891) · UniProt [Q9UBK2](https://www.uniprot.org/uniprotkb/Q9UBK2) · Ensembl [ENSG00000109819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109819)

## Data

Gene col 3086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3086); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3086]; `tensor/DDL_lfc|DDL_z.npy` [3086]; `embed/gene_vectors.npy` [3086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3086 or target_col == 3086). Every well: [[PPARGC1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPARGC1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
