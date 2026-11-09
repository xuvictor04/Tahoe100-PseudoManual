---
symbol: "THEMIS2"
type: "gene"
col: 5125
ensembl_id: "ENSG00000130775"
name: "thymocyte selection associated family member 2"
location: "1p35.3"
module: 167
arm: "+"
pooled_cpm: 9.66
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 38
n_dd_up_clean: 5
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 18
direction_downstream: 6
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# THEMIS2

*thymocyte selection associated family member 2* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +7.3, q 1e-10, up in 10 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.472× (z -11.9, q 4e-30, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASSF4]] (+0.65, fdr 1e-05), [[TYMP]] (+0.62, fdr 1e-05), [[ARID5A]] (+0.62, fdr 1e-05); moves opposite to [[EPM2A]] (-0.59, fdr 1e-04), [[ALG8]] (-0.57, fdr 3e-05), [[SNX5]] (-0.55, fdr 5e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[ADAMTS9-AS2]] → it (grade B ⚠); 6 go from it, the strongest it → [[AHDC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +7.3 | 1e-10 | 10/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.2 | 7e-05 | 12/28 (HOP62, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.007 | 7/27 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +4.0 | 0.008 | 6/20 (HS-578T, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.010 | 12/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.5 | 0.038 | 1/13 (NCI-H1792) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +3.3 | 0.069 | 8/26 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.16 | 7/27 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.31× | +3.0 | 0.16 | 7/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -11.9 | 4e-30 | 23/27 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -11.6 | 1e-28 | 24/28 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -10.3 | 9e-23 | 21/25 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -10.2 | 4e-22 | 23/27 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.530×** | -10.1 | 7e-22 | 20/25 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.487×** | -7.8 | 7e-13 | 20/26 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.281×** | -7.5 | 7e-12 | 21/27 (NCI-H1792, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.523×** | -7.3 | 2e-11 | 21/27 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -7.2 | 3e-11 | 16/27 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.310×** | -6.9 | 3e-10 | 16/24 (Panc 03.27, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -6.9 | 3e-10 | 19/24 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.532×** | -6.8 | 4e-10 | 14/27 (RPMI-7951, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -6.6 | 2e-09 | 16/26 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.698×** | -5.7 | 5e-07 | 15/27 (SK-MEL-2, RPMI-7951, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.604×** | -5.7 | 6e-07 | 16/20 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.705×** | -5.5 | 1e-06 | 16/27 (SK-MEL-2, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.612×** | -5.2 | 6e-06 | 16/27 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.729×** | -5.0 | 2e-05 | 15/28 (SNU-423, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -4.7 | 6e-05 | 15/27 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -3.6 | 0.006 | 14/27 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 41.1 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0996× (z -22.5) |
| [[SNU-423 (line)]] | alt | 28.8 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -23.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0393× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 65.4 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -22.1) |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 8 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.151× (z -16.5) |
| [[A549 (line)]] | wt | 9.47 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0168× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0330× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -14.2) |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0385× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 31.0 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -19.0) |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -19.2) |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.7) |
| [[COLO 205 (line)]] | alt | 7.76 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0590× (z -8.5) |
| [[Hs 766T (line)]] | wt | 4.88 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 2.51 | 0 | 1 | — | [[Sunitinib (drug)]] 0.5 µM 0.0658× (z -9.2) |
| [[PANC-1 (line)]] | alt | 4.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0775× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF4]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TYMP]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ARID5A]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DEPP1]] | +0.60 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ODF3B]] | +0.59 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DUOX2]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NAGK]] | +0.57 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PIGH]] | +0.57 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[C1R]] | +0.57 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[RNF114]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[PTGES]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[GMPR]] | +0.55 | +0.34 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | -0.59 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[ALG8]] | -0.57 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SNX5]] | -0.55 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MSANTD2]] | -0.54 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[ATE1]] | -0.54 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[SLC12A2-DT]] | -0.53 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[DNAAF10]] | -0.52 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[ECHDC1]] | -0.52 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[GABPB1-AS1]] | -0.51 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ZNF876P]] | -0.51 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[NHSL1]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[RCC2]] | -0.50 | -0.48 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity raises THEMIS2's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.37× lower at baseline in the lines without ADAMTS9-AS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[CD38]] | B | CD38 activity raises THEMIS2's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.96× lower at baseline in the lines without CD38 | 0.013 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent |
| [[C15orf48]] | B | C15orf48 activity raises THEMIS2's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 2.60× lower at baseline in the lines without C15orf48 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[LOX]] | B | LOX activity raises THEMIS2's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without LOX | 0.020 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[DEPP1]] | B | DEPP1 activity raises THEMIS2's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without DEPP1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[MAF]] | B | MAF activity raises THEMIS2's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without MAF | 0.021 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[BDKRB2]] | B | BDKRB2 activity raises THEMIS2's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without BDKRB2 | 0.023 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[STRA6]] | B | STRA6 activity raises THEMIS2's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 2.28× lower at baseline in the lines without STRA6 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3 |
| [[ADAMTS14]] | B | ADAMTS14 activity raises THEMIS2's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without ADAMTS14 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[ZNF439]] | B | ZNF439 activity raises THEMIS2's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.32× lower at baseline in the lines without ZNF439 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[TREM1]] | B | TREM1 activity raises THEMIS2's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without TREM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[TNS1]] | B | TNS1 activity raises THEMIS2's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without TNS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHDC1]] | B | THEMIS2 activity raises AHDC1's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without THEMIS2 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[DEPP1]] | B | THEMIS2 activity raises DEPP1's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 2.24× lower at baseline in the lines without THEMIS2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[ADAMTS9-AS2]] | B | THEMIS2 activity raises ADAMTS9-AS2's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without THEMIS2 | 0.055 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[TREM1]] | B | THEMIS2 activity raises TREM1's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without THEMIS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[GIPR]] | B | THEMIS2 activity raises GIPR's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 1.69× lower at baseline in the lines without THEMIS2 | 0.061 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[ARMCX2]] | C | THEMIS2 activity raises ARMCX2's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without THEMIS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.2, -1.8); signed map (20.9, 38.2). **Vector** length 82.6, 21.9% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | thymocyte selection associated family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,872,543-27,886,685 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ICB-1, Icb-1; previously C1orf38 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TEJ8](https://www.uniprot.org/uniprotkb/Q5TEJ8) (Protein THEMIS2):

> May constitute a control point in macrophage inflammatory response, promoting LPS-induced TLR4-mediated TNF production. Determines the threshold for activation of B cells by low-affinity and low-avidity ligands via PLCG2 activation and its downstream pathways (By similarity).

**Summary**, from NCBI Gene [9473](https://www.ncbi.nlm.nih.gov/gene/9473):

> Predicted to be involved in T cell receptor signaling pathway and regulation of B cell activation. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16839) · Entrez [9473](https://www.ncbi.nlm.nih.gov/gene/9473) · UniProt [Q5TEJ8](https://www.uniprot.org/uniprotkb/Q5TEJ8) · Ensembl [ENSG00000130775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130775)

## Data

Gene col 5125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5125); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5125]; `tensor/DDL_lfc|DDL_z.npy` [5125]; `embed/gene_vectors.npy` [5125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5125 or target_col == 5125). Every well: [[THEMIS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THEMIS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
