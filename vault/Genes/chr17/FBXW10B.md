---
symbol: "FBXW10B"
type: "gene"
col: 14266
ensembl_id: "ENSG00000241322"
name: "F-box and WD repeat domain containing 10B"
location: "17p12"
module: 47
arm: "+"
pooled_cpm: 7.72
n_lines_expressing: 39
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 15
direction_downstream: 25
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FBXW10B

*F-box and WD repeat domain containing 10B* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.78× (z +14.0, q 1e-41, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.356× (z -8.2, q 9e-14, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A9]] (+0.76, fdr 7e-06), [[C3orf20]] (+0.70, fdr 1e-05), [[MTNR1A]] (+0.68, fdr 1e-05); moves opposite to [[BRAT1]] (-0.60, fdr 4e-05), [[ECI2]] (-0.59, fdr 2e-05), [[SPATA7]] (-0.58, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[CYP4F11]] → it (grade B ⚠); 25 go from it, the strongest it → [[PAX8-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.78×** | +14.0 | 1e-41 | 30/33 (HEC-1-A, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.65×** | +10.3 | 2e-22 | 25/32 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +7.8 | 9e-13 | 18/32 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **2.64×** | +7.7 | 1e-12 | 30/37 (Panc 03.27, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +7.0 | 2e-10 | 15/26 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +6.7 | 2e-09 | 5/14 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.6 | 4e-04 | 14/37 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.5 | 4e-04 | 16/37 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.75×** | +4.2 | 0.002 | 15/35 (A549, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.008 | 15/30 (A549, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.028 | 10/34 (A549, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.067 | 11/34 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.070 | 5/36 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.070 | 12/37 (BT-474, A-172, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.078 | 5/37 (J82, HS-578T, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.089 | 5/36 (A498, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14266.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.356×** | -8.2 | 9e-14 | 28/36 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.483×** | -5.8 | 2e-06 | 21/36 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.522×** | -5.2 | 4e-05 | 23/36 (HEC-1-A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -4.9 | 2e-04 | 20/36 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.552×** | -4.8 | 2e-04 | 21/30 (KATO III, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.553×** | -4.7 | 2e-04 | 20/35 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -4.7 | 2e-04 | 15/36 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.555×** | -4.5 | 4e-04 | 17/29 (SW480, SW1417, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.341×** | -4.5 | 4e-04 | 12/29 (J82, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -3.9 | 0.006 | 12/34 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.037 | 11/36 (KATO III, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -3.4 | 0.037 | 13/31 (SW48, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | **0.682×** | -3.1 | 0.093 | 7/36 (NCI-H460, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 41.2 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0779× (z -12.6) |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0303× (z -13.9) |
| [[LoVo (line)]] | wt | 11.0 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 9.98× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0988× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 19.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 16.6× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -10.7) |
| [[HOP62 (line)]] | alt | 2.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 4.56 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.05 µM 0.0784× (z -8.8) |
| [[SW480 (line)]] | alt | 4.20 | 1 | 1 | [[Auranofin (drug)]] 5 µM 10.8× (z +9.5) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0974× (z -9.0) |
| [[A-172 (line)]] | wt | 3.05 | 1 | 0 | [[Auranofin (drug)]] 5 µM 73.5× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0381× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0741× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0961× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 8.84 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0827× (z -8.8) |
| [[SW48 (line)]] | wt | 35.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0716× (z -8.7) |
| [[A-427 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A9]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.70 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[MTNR1A]] | +0.68 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[NECAB2]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[BTG3-AS1]] | +0.67 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[BTBD16]] | +0.66 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PHEX]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CFAP161]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[PKD1L1]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.60 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ECI2]] | -0.59 | -0.51 / -0.49 | both halves | 2e-05 |  |
| [[SPATA7]] | -0.58 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[UHRF2]] | -0.58 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[SEMA4F]] | -0.58 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FBXO3]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TERF1]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[MARF1]] | -0.57 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[SNX1]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[KLHL7]] | -0.56 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PXMP4]] | -0.56 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[MMS19]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F11]] | B | CYP4F11 activity raises FBXW10B's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without CYP4F11 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[LINC01564]] | B | LINC01564 activity raises FBXW10B's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without LINC01564 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[KRT16]] | B | KRT16 activity raises FBXW10B's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without KRT16 | 0.024 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[GNA14]] | B | GNA14 activity raises FBXW10B's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without GNA14 | 0.027 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[PAX8-AS1]] | B | PAX8-AS1 activity raises FBXW10B's level | lines that do not express PAX8-AS1 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without PAX8-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC68, PAX8, PCSK5; maybe low, not absent |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises FBXW10B's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.70× lower at baseline in the lines without ALOX12P2-1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises FBXW10B's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without NMRAL2P-1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[LMO7DN]] | B | LMO7DN activity raises FBXW10B's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without LMO7DN | 0.055 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[SLCO2B1]] | B | SLCO2B1 activity raises FBXW10B's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without SLCO2B1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |
| [[TNNT2]] | B | TNNT2 activity raises FBXW10B's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.17× lower at baseline in the lines without TNNT2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[LINC01348]] | B | LINC01348 activity raises FBXW10B's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without LINC01348 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[SLC2A9]] | B | SLC2A9 activity raises FBXW10B's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 2.56× lower at baseline in the lines without SLC2A9 | 0.089 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 24, C 1. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX8-AS1]] | B | FBXW10B activity raises PAX8-AS1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 2.61× lower at baseline in the lines without FBXW10B | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[PEBP4]] | B | FBXW10B activity raises PEBP4's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without FBXW10B | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[LINC00571]] | B | FBXW10B activity raises LINC00571's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without FBXW10B | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[PITRM1-AS1]] | B | FBXW10B activity raises PITRM1-AS1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without FBXW10B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[TRIM16]] | B | FBXW10B activity raises TRIM16's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without FBXW10B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[ALPK3]] | B | FBXW10B activity raises ALPK3's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 2.32× lower at baseline in the lines without FBXW10B | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | FBXW10B activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.27× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[UGDH]] | B | FBXW10B activity raises UGDH's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without FBXW10B | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 0.05 µM | B | FBXW10B activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.19× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[AXDND1]] | B | FBXW10B activity lowers AXDND1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.64× higher at baseline in the lines without FBXW10B | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | FBXW10B activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.18× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[EPHA1-AS1]] | B | FBXW10B activity raises EPHA1-AS1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without FBXW10B | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, -10.8); signed map (20.1, 7.7). **Vector** length 95.1, 22.6% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.6 | +14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.7 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 10B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,565,483-15,619,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HREP, SM25H2; previously FBXW10P1, CDRT1 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [O95170](https://www.uniprot.org/uniprotkb/O95170) carries no function annotation.

**Summary**, from NCBI Gene [374286](https://www.ncbi.nlm.nih.gov/gene/374286):

> Members of the F-box protein family, such as FBXW10, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603034), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14379) · Entrez [374286](https://www.ncbi.nlm.nih.gov/gene/374286) · UniProt [O95170](https://www.uniprot.org/uniprotkb/O95170) · Ensembl [ENSG00000241322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241322)

## Data

Gene col 14266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14266); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14266]; `tensor/DDL_lfc|DDL_z.npy` [14266]; `embed/gene_vectors.npy` [14266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14266 or target_col == 14266). Every well: [[FBXW10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
