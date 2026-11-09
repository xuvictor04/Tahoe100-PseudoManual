---
symbol: "CCDC144CP"
type: "gene"
col: 7851
ensembl_id: "ENSG00000154898"
name: "coiled-coil domain containing 144C, pseudogene"
location: "17p11.2"
module: 39
arm: "+"
pooled_cpm: 8.59
n_lines_expressing: 43
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CCDC144CP

*coiled-coil domain containing 144C, pseudogene* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.00× (z +19.5, q 0e+00, up in 25 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.628× (z -5.7, q 7e-06, down in 19 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.564× (z -3.8, q 0.040, down in 13 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCUBE2]] (+0.64, fdr 1e-05), [[DPYS]] (+0.62, fdr 1e-05), [[SSUH2]] (+0.62, fdr 1e-05); moves opposite to [[LRIG2]] (-0.60, fdr 1e-05), [[MTFMT]] (-0.58, fdr 2e-04), [[DUSP11]] (-0.57, fdr 1e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KATNAL2]] → it (grade B ⚠); 8 go from it, the strongest it → [[SPECC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.00×** | +19.5 | 0e+00 | 25/32 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.49×** | +11.5 | 5e-28 | 31/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +9.1 | 2e-17 | 19/32 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +8.7 | 3e-16 | 22/40 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.9 | 4e-13 | 20/36 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +7.6 | 2e-12 | 20/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +6.7 | 1e-09 | 7/17 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.6 | 2e-09 | 18/40 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +6.5 | 5e-09 | 17/37 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.5 | 6e-09 | 5/12 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.0 | 1e-07 | 17/40 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.0 | 2e-05 | 8/23 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 11/37 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.029 | 7/39 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.081 | 10/38 (HS-578T, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.081 | 6/40 (A-172, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -5.7 | 7e-06 | 19/29 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -3.8 | 0.040 | 13/35 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.077 | 16/39 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pentagastrin (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.079 | 8/39 (SNU-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.767×** | -3.4 | 0.079 | 15/33 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.618× | -3.2 | 0.13 | 12/37 (RKO, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.790× | -3.0 | 0.20 | 13/40 (NCI-H23, PANC-1, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 9.36 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0672× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 5.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0848× (z -12.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 6.20 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0866× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 4.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 8.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +16.9) | — |
| [[HS-578T (line)]] | alt | 7.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +11.2) | — |
| [[J82 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.9) | — |
| [[KATO III (line)]] | alt | 8.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +10.5) | — |
| [[LoVo (line)]] | wt | 8.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 4.00 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0931× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.162× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +13.4) | — |
| [[SW 1271 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0754× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.4) | — |
| [[A498 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCUBE2]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[DPYS]] | +0.62 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SSUH2]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[KIF17]] | +0.61 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ALPK3]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.59 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.59 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ANKS1B]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[USP50]] | +0.58 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[LINC01934]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MMP25]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SLC8A2]] | +0.58 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MTFMT]] | -0.58 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[DUSP11]] | -0.57 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[CMC1]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MTERF3]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[C8orf76]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[TAB1]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[NDUFV1]] | -0.54 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[SPATA7]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ALG9]] | -0.53 | -0.61 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | KATNAL2 activity raises CCDC144CP's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.66× lower at baseline in the lines without KATNAL2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[SPECC1]] | B | SPECC1 activity raises CCDC144CP's level | lines that do not express SPECC1 (6) vs lines expressing it (44) | 3.31× lower at baseline in the lines without SPECC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: BMP8B, FARP1, KIAA1522 |
| [[CHST11]] | B | CHST11 activity raises CCDC144CP's level | lines that do not express CHST11 (13) vs lines expressing it (37) | 2.06× lower at baseline in the lines without CHST11 | 0.063 | ⚠ within organs, on part of the lines; also absent: SGCE, MAP9, BVES-AS1 |
| [[SYNM]] | B | SYNM activity raises CCDC144CP's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without SYNM | 0.079 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPECC1]] | B | CCDC144CP activity raises SPECC1's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 4.67× lower at baseline in the lines without CCDC144CP | 5e-04 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[PILRA]] | B | CCDC144CP activity raises PILRA's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without CCDC144CP | 0.011 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[KATNAL2]] | B | CCDC144CP activity raises KATNAL2's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without CCDC144CP | 0.030 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[PTCH2]] | B | CCDC144CP activity raises PTCH2's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without CCDC144CP | 0.077 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[TAB1]] | B | CCDC144CP activity raises TAB1's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without CCDC144CP | 0.078 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[TMED8]] | B | CCDC144CP activity raises TMED8's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without CCDC144CP | 0.079 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[PRMT7]] | B | CCDC144CP activity raises PRMT7's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without CCDC144CP | 0.087 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |
| [[SPOCK2]] | B | CCDC144CP activity raises SPOCK2's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without CCDC144CP | 0.093 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, -11.5); signed map (19.9, 9.4). **Vector** length 60.2, 9.37% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +19.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 144C, pseudogene |
| Locus type | pseudogene |
| Location | 17p11.2 — chr17:20,321,317-20,403,557 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously CCDC144C |
| Matched by | ensembl_id |

UniProt [Q8IYA2](https://www.uniprot.org/uniprotkb/Q8IYA2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29073) · Entrez [348254](https://www.ncbi.nlm.nih.gov/gene/348254) · UniProt [Q8IYA2](https://www.uniprot.org/uniprotkb/Q8IYA2) · Ensembl [ENSG00000154898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154898)

## Data

Gene col 7851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7851); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7851]; `tensor/DDL_lfc|DDL_z.npy` [7851]; `embed/gene_vectors.npy` [7851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7851 or target_col == 7851). Every well: [[CCDC144CP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC144CP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
