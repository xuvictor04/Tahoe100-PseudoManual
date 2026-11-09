---
symbol: "ARHGAP8"
type: "gene"
col: 14278
ensembl_id: "ENSG00000241484"
name: "Rho GTPase activating protein 8"
location: "22q13.31"
module: 23
arm: "-"
pooled_cpm: 30.88
n_lines_expressing: 28
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 18
direction_downstream: 21
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ARHGAP8

*Rho GTPase activating protein 8* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.41× (z +17.1, q 0e+00, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.510× (z -18.4, q 0e+00, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR5]] (+0.73, fdr 1e-05, ⚠ same locus), [[EDA]] (+0.70, fdr 1e-05), [[PRR5-ARHGAP8]] (+0.68, fdr 1e-05, ⚠ same locus), [[ANKS6]] (+0.67, fdr 1e-05), [[UNC5A]] (+0.65, fdr 1e-05); moves opposite to [[C3orf38]] (-0.68, fdr 4e-05), [[ERCC6L2-AS1]] (-0.67, fdr 2e-04), [[METTL6]] (-0.65, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 21 go from it, the strongest it → [[NBEAL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +17.1 | 0e+00 | 20/26 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +12.6 | 1e-33 | 17/26 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +11.5 | 3e-28 | 20/26 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.3 | 3e-18 | 13/26 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.6 | 5e-12 | 16/26 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.9 | 4e-07 | 18/26 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +5.4 | 4e-06 | 10/26 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 9e-06 | 14/26 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 12/26 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.023 | 0/26 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.037 | 9/25 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.11 | 5/26 (NCI-H1573, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.510×** | -18.4 | 0e+00 | 24/26 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -12.1 | 5e-31 | 21/25 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.691×** | -10.1 | 8e-22 | 23/26 (Panc 03.27, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -10.1 | 1e-21 | 19/26 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.602×** | -9.5 | 4e-19 | 23/26 (SW48, A498, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -9.2 | 2e-18 | 23/26 (LoVo, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -6.6 | 3e-09 | 12/26 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -5.5 | 3e-06 | 14/26 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -4.7 | 1e-04 | 10/26 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.871× | -3.8 | 0.008 | 4/26 (A498, KATO III, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.823×** | -3.8 | 0.008 | 2/26 (A498, LS 180) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | 0.839× | -3.4 | 0.032 | 13/24 (SW48, KATO III, …) | all doses, flat | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.723×** | -3.3 | 0.045 | 10/26 (LS 180, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.732×** | -3.2 | 0.063 | 9/25 (NCI-H23, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 128 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -19.9) |
| [[SW48 (line)]] | wt | 112 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -19.8) |
| [[SW480 (line)]] | alt | 29.9 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 85.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 49.6 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 2.90× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.1) |
| [[A-427 (line)]] | wt | 44.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -18.9) |
| [[LoVo (line)]] | wt | 77.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -20.0) |
| [[SW1417 (line)]] | alt | 57.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -22.6) |
| [[A498 (line)]] | wt | 24.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -20.6) |
| [[C-33 A (line)]] | alt | 78.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -16.3) |
| [[COLO 205 (line)]] | alt | 21.3 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 6.40× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -9.4) |
| [[LS 180 (line)]] | wt | 117 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 48.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.5) |
| [[Panc 03.27 (line)]] | alt | 47.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -16.6) |
| [[PANC-1 (line)]] | alt | 12.5 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.13× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.5) |
| [[HCT15 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.5) |
| [[A549 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.4) |
| [[HT-29 (line)]] | alt | 47.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.4) |
| [[A-172 (line)]] | wt | 7.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR5]] | +0.73 | +0.74 / +0.52 | both halves | 1e-05 | STRING 932; ⚠ same locus (14.9 kb, same strand: neighbours can correlate without regulation) |
| [[EDA]] | +0.70 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 | STRING 759; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ANKS6]] | +0.67 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[UNC5A]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TRABD]] | +0.65 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[IGSF9]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TMEM241]] | +0.64 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PACC1]] | +0.64 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ST3GAL4]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[CBLC]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[CMTM8]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.63 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf38]] | -0.68 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | -0.67 | -0.67 / -0.31 | both halves | 2e-04 |  |
| [[METTL6]] | -0.65 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[AHI1-DT]] | -0.64 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ZNF407-AS1]] | -0.64 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.64 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[AK9]] | -0.64 | -0.66 / -0.29 | both halves | 3e-04 |  |
| [[ZNF563]] | -0.64 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[THAP2]] | -0.63 | -0.65 / -0.27 | both halves | 3e-04 |  |
| [[PCNX4-DT]] | -0.63 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[LINC00240]] | -0.62 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[WAC-AS1]] | -0.62 | -0.55 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 7, C 11. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity raises ARHGAP8's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.56× lower at baseline in the lines without RAPGEF5 | 0.054 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises ARHGAP8's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 3.32× lower at baseline in the lines without MCF2L | 0.054 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[STXBP6]] | B | STXBP6 activity raises ARHGAP8's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without STXBP6 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[EEPD1]] | B | EEPD1 activity raises ARHGAP8's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 3.62× lower at baseline in the lines without EEPD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[MAOB]] | B | MAOB activity raises ARHGAP8's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.03× lower at baseline in the lines without MAOB | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ARHGAP8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ARHGAP8's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CBLC]] | C | CBLC activity raises ARHGAP8's level | lines that do not express CBLC (31) vs lines expressing it (19) | 4.37× lower at baseline in the lines without CBLC | 7e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises ARHGAP8's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 5.99× lower at baseline in the lines without ATP2C2 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises ARHGAP8's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 3.73× lower at baseline in the lines without EPHA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[RASAL1]] | C | RASAL1 activity raises ARHGAP8's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 3.38× lower at baseline in the lines without RASAL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; co-absent with the target |
| [[CRYBG2]] | C | CRYBG2 activity raises ARHGAP8's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 4.46× lower at baseline in the lines without CRYBG2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 14, C 7. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBEAL2]] | B | ARHGAP8 activity raises NBEAL2's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without ARHGAP8 | 0.005 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[ST6GALNAC4]] | B | ARHGAP8 activity lowers ST6GALNAC4's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.11× higher at baseline in the lines without ARHGAP8 | 0.007 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[OSBPL10]] | B | ARHGAP8 activity raises OSBPL10's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without ARHGAP8 | 0.017 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[PPCDC]] | B | ARHGAP8 activity raises PPCDC's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without ARHGAP8 | 0.017 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[ACOT11]] | B | ARHGAP8 activity raises ACOT11's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without ARHGAP8 | 0.027 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[TMX4]] | B | ARHGAP8 activity lowers TMX4's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.76× higher at baseline in the lines without ARHGAP8 | 0.028 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[ARHGEF16]] | B | ARHGAP8 activity raises ARHGEF16's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without ARHGAP8 | 0.028 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[TBC1D14]] | B | ARHGAP8 activity raises TBC1D14's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without ARHGAP8 | 0.046 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | ARHGAP8 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ARHGAP8 (22) vs lines expressing it (26) | the lines without ARHGAP8: 0.87× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[FGFR4]] | B | ARHGAP8 activity raises FGFR4's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without ARHGAP8 | 0.058 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[ATP11A]] | B | ARHGAP8 activity raises ATP11A's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without ARHGAP8 | 0.073 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[CARMIL1]] | B | ARHGAP8 activity raises CARMIL1's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without ARHGAP8 | 0.076 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (0.5, 15.0); signed map (-19.8, 36.4). **Vector** length 90.2, 27.3% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +17.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +11.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.4 | -9.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.4 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -18.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -9.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:44,752,558-44,862,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20185, BPGAP1 |
| Gene groups (HGNC) | Rho GTPase activating proteins; BCH domain containing ; CRAL-TRIO lipid binding domain containing |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P85298](https://www.uniprot.org/uniprotkb/P85298) (Rho GTPase-activating protein 8):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [23779](https://www.ncbi.nlm.nih.gov/gene/23779):

> This gene encodes a member of the RHOGAP family. GAP (GTPase-activating) family proteins participate in signaling pathways that regulate cell processes involved in cytoskeletal changes. GAP proteins alternate between an active (GTP-bound) and inactive (GDP-bound) state based on the GTP:GDP ratio in the cell. This family member is a multidomain protein that functions to promote Erk activation and cell motility. Alternative splicing results in multiple transcript variants. Read-through …

**Accessions** — [HGNC:677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:677) · Entrez [23779](https://www.ncbi.nlm.nih.gov/gene/23779) · UniProt [P85298](https://www.uniprot.org/uniprotkb/P85298) · Ensembl [ENSG00000241484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241484)

## Data

Gene col 14278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14278); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14278]; `tensor/DDL_lfc|DDL_z.npy` [14278]; `embed/gene_vectors.npy` [14278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14278 or target_col == 14278). Every well: [[ARHGAP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
