---
symbol: "PIGW"
type: "gene"
col: 15887
ensembl_id: "ENSG00000277161"
name: "phosphatidylinositol glycan anchor biosynthesis class W"
location: "17q12"
module: 5
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PIGW

*phosphatidylinositol glycan anchor biosynthesis class W* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.98× (z +18.7, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.443× (z -7.8, q 4e-12, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPM2A]] (+0.75, fdr 3e-05), [[E2F3]] (+0.74, fdr 7e-06), [[MRM1]] (+0.73, fdr 9e-06); moves opposite to [[ARL3]] (-0.67, fdr 2e-05), [[UBE2B]] (-0.66, fdr 1e-05), [[KBTBD3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +18.7 | 0e+00 | 36/37 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.72×** | +12.1 | 4e-31 | 21/23 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +11.9 | 4e-30 | 4/6 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.19×** | +11.0 | 4e-26 | 18/20 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +9.8 | 1e-20 | 8/10 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +8.6 | 7e-16 | 25/44 (PANC-1, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +7.8 | 4e-13 | 31/45 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +7.6 | 2e-12 | 28/43 (C-33 A, SNU-423, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +6.7 | 2e-09 | 20/31 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +6.2 | 4e-08 | 22/36 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.3 | 5e-06 | 12/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.2 | 9e-06 | 17/36 (CFPAC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.0 | 2e-05 | 8/26 (Panc 03.27, Hs 766T, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +4.7 | 1e-04 | 12/44 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 11/45 (J82, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.005 | 11/43 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.13×** | +3.8 | 0.005 | 6/31 (A498, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.006 | 13/44 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.08×** | +3.7 | 0.007 | 7/31 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.037 | 8/42 (COLO 205, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.88×** | +3.2 | 0.040 | 1/39 (HT-29) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.443×** | -7.8 | 4e-12 | 28/44 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.530×** | -6.1 | 3e-07 | 19/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.700×** | -4.8 | 2e-04 | 17/44 (KATO III, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.611×** | -4.7 | 3e-04 | 19/45 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.634×** | -4.4 | 0.001 | 14/43 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.683×** | -3.5 | 0.040 | 10/36 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.749×** | -3.2 | 0.093 | 7/43 (AsPC-1, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.093 | 8/40 (SW1417, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.714× | -3.1 | 0.12 | 9/37 (SW1417, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.93 | 0 | 1 | — | [[Nevirapine (drug)]] 0.5 µM 0.0630× (z -8.9) |
| [[A-427 (line)]] | wt | 5.35 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0873× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 4.23 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0815× (z -9.7) |
| [[HOP62 (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +8.6) | — |
| [[KATO III (line)]] | alt | 7.15 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0595× (z -10.2) |
| [[SW1417 (line)]] | alt | 4.63 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.0685× (z -9.2) |
| [[SW480 (line)]] | alt | 5.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +9.5) | — |
| [[A498 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | +0.75 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[E2F3]] | +0.74 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MRM1]] | +0.73 | +0.66 / +0.57 | both halves | 9e-06 | STRING 657 |
| [[SLC5A6]] | +0.73 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[BEND3]] | +0.73 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TRNT1]] | +0.73 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TLCD3A]] | +0.71 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[ALG8]] | +0.71 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[AVEN]] | +0.71 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CCNJ]] | +0.70 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF124]] | +0.70 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[ARMC6]] | +0.70 | +0.75 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | -0.67 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.66 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.65 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.65 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ZCRB1]] | -0.65 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[RNF114]] | -0.65 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[ALAD]] | -0.65 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[OSBPL9]] | -0.64 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TMEM256]] | -0.64 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[SIRT2]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[OAZ1]] | -0.63 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[ACSF2]] | -0.62 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIGW's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LLGL2]] | B | LLGL2 activity raises PIGW's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without LLGL2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PIGW's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PIGW's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TBXAS1]] | B | TBXAS1 activity lowers PIGW's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.20× higher at baseline in the lines without TBXAS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[FAR2]] | B | FAR2 activity lowers PIGW's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.19× higher at baseline in the lines without FAR2 | 0.0996 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[SYP]] | C | SYP activity raises PIGW's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.5, 9.5); signed map (24.0, -29.4). **Vector** length 75.1, 13.0% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.56 to 13); *ribosome biogenesis* (control, mean cos +0.50 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.62 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +18.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.3 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class W |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,534,987-36,539,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Gwt1, FLJ37433, PIG-W |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Acyltransferases |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7B1](https://www.uniprot.org/uniprotkb/Q7Z7B1) (Glucosaminyl-phosphatidylinositol-acyltransferase PIGW):

> Acyltransferase that catalyzes the acyl transfer from an acyl-CoA at the 2-OH position of the inositol ring of a 6-(alpha-D-glucosaminyl)-1-(1,2-diacyl-sn-glycero-3-phospho)-1D-myo-inositol (glucosaminyl phosphatidylinositol, GlcN-PI) to generate a 2-acyl-6-alpha-D-glucosaminyl-1-(1,2-diacyl-sn-glycero-3-phospho)-1D-myo-inositol (glucosaminyl acyl phosphatidylinositol, GlcN-(acyl)PI) and participates in the fourth step of GPI-anchor biosynthesis (By similarity). Required for the transport of …

**Summary**, from NCBI Gene [284098](https://www.ncbi.nlm.nih.gov/gene/284098):

> The protein encoded by this gene is an inositol acyltransferase that acylates the inositol ring of phosphatidylinositol. This occurs in the endoplasmic reticulum and is a step in the biosynthesis of glycosylphosphatidylinositol (GPI), which anchors many cell surface proteins to the membrane. Defects in this gene are a cause of the age-dependent epileptic encephalopathy West syndrome as well as a syndrome exhibiting hyperphosphatasia and cognitive disability (HPMRS5). [provided by RefSeq, Jul …

**Accessions** — [HGNC:23213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23213) · Entrez [284098](https://www.ncbi.nlm.nih.gov/gene/284098) · UniProt [Q7Z7B1](https://www.uniprot.org/uniprotkb/Q7Z7B1) · Ensembl [ENSG00000277161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277161)

## Data

Gene col 15887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15887); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15887]; `tensor/DDL_lfc|DDL_z.npy` [15887]; `embed/gene_vectors.npy` [15887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15887 or target_col == 15887). Every well: [[PIGW — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGW.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
