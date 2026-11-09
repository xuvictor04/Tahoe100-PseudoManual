---
symbol: "MPP1"
type: "gene"
col: 5140
ensembl_id: "ENSG00000130830"
name: "MAGUK p55 scaffold protein 1"
location: "Xq28"
module: 45
arm: "+"
pooled_cpm: 9.09
n_lines_expressing: 43
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# MPP1

*MAGUK p55 scaffold protein 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.26× (z +20.0, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.642× (z -6.1, q 5e-07, down in 19 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG3]] (+0.74, fdr 7e-06), [[PAPSS1]] (+0.73, fdr 7e-06), [[ALAD]] (+0.71, fdr 1e-05); moves opposite to [[LINC01004]] (-0.67, fdr 4e-05), [[ANKRD17-DT]] (-0.67, fdr 1e-04), [[SLC13A3]] (-0.65, fdr 2e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIP4P2]] → it (grade C ⚠); 7 go from it, the strongest it → [[SNX30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.26×** | +20.0 | 0e+00 | 38/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.07×** | +19.3 | 0e+00 | 38/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.93×** | +18.8 | 0e+00 | 39/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.38×** | +11.9 | 1e-30 | 33/40 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.26×** | +11.2 | 4e-27 | 29/37 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.22×** | +8.4 | 4e-15 | 29/41 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.76×** | +7.8 | 6e-13 | 14/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.74×** | +7.3 | 2e-11 | 7/15 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.0 | 2e-10 | 20/41 (LS 180, J82, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.35×** | +5.8 | 5e-07 | 15/41 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.56×** | +5.6 | 9e-07 | 11/20 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.9 | 4e-05 | 11/31 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 11/40 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.5 | 3e-04 | 15/40 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +4.3 | 7e-04 | 8/40 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +4.3 | 7e-04 | 15/38 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.027 | 3/41 (COLO 205, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bexarotene (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.046 | 9/40 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.049 | 8/41 (NCI-H460, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -6.1 | 5e-07 | 19/39 (SNU-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -5.3 | 3e-05 | 14/38 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.689×** | -5.2 | 5e-05 | 15/36 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -5.1 | 5e-05 | 14/40 (A-172, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.731×** | -4.3 | 0.002 | 11/40 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.744×** | -4.1 | 0.004 | 10/40 (J82, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.760×** | -3.8 | 0.011 | 11/39 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.833× | -3.6 | 0.023 | 13/41 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.836× | -3.5 | 0.026 | 11/41 (MIA PaCa-2, NCI-H661, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.033 | 8/40 (A498, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.038 | 10/40 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.730×** | -3.1 | 0.085 | 5/36 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.857× | -3.1 | 0.099 | 6/41 (J82, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.28× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 26.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.5) | — |
| [[SW480 (line)]] | alt | 4.53 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.14× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 8.77 | 0 | 2 | — | [[Gallic acid (drug)]] 0.05 µM 0.0968× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 6.34 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.6× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 5.62 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 9.51 | 1 | 0 | [[Belinostat (drug)]] 5 µM 5.27× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 4.47 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 10.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +9.2) | — |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | +0.74 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.73 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ALAD]] | +0.71 | +0.50 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[HLTF]] | +0.68 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.68 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[THYN1]] | +0.67 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[AKTIP]] | +0.66 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.65 | +0.53 / +0.47 | both halves | 2e-05 | STRING 823 |
| [[RAB3A]] | +0.65 | +0.39 / +0.53 | both halves | 5e-05 | pathway: Sensory Perception |
| [[PLA2G12A]] | +0.65 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ARL6]] | +0.65 | +0.51 / +0.49 | both halves | 2e-05 |  |
| [[CAT]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01004]] | -0.67 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD17-DT]] | -0.67 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[SLC13A3]] | -0.65 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[ITPA]] | -0.64 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[HSPBAP1]] | -0.62 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | -0.62 | -0.36 / -0.29 | both halves | 3e-04 |  |
| [[ZNF337-AS1]] | -0.62 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[SPRY3]] | -0.61 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[PBLD]] | -0.61 | -0.34 / -0.32 | both halves | 1e-04 |  |
| [[MTG2]] | -0.61 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SPON1-AS1]] | -0.61 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[MRPL45P2]] | -0.60 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIP4P2]] | C | PIP4P2 activity raises MPP1's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 3.08× lower at baseline in the lines without PIP4P2 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX30]] | B | MPP1 activity raises SNX30's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without MPP1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[SCPEP1]] | B | MPP1 activity raises SCPEP1's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without MPP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[LINC00888]] | B | MPP1 activity raises LINC00888's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without MPP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[TMEM187]] | B | MPP1 activity lowers TMEM187's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without MPP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[TBCB]] | B | MPP1 activity raises TBCB's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without MPP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[TRAM2]] | B | MPP1 activity raises TRAM2's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 2.50× lower at baseline in the lines without MPP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[HLTF]] | C | MPP1 activity raises HLTF's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 5.60× lower at baseline in the lines without MPP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.9, -7.0); signed map (-35.4, -13.3). **Vector** length 70.4, 13.3% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.0 | +19.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +18.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +20.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +8.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +7.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.9 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MAGUK p55 scaffold protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,778,684-154,821,007 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEMP; previously DXS552E |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00013](https://www.uniprot.org/uniprotkb/Q00013) (55 kDa erythrocyte membrane protein):

> Essential regulator of neutrophil polarity. Regulates neutrophil polarization by regulating AKT1 phosphorylation through a mechanism that is independent of PIK3CG activity (By similarity).

**Summary**, from NCBI Gene [4354](https://www.ncbi.nlm.nih.gov/gene/4354):

> This gene encodes the prototype of the membrane-associated guanylate kinase (MAGUK) family proteins. MAGUKs interact with the cytoskeleton and regulate cell proliferation, signaling pathways, and intercellular junctions. The encoded protein is an extensively palmitoylated membrane phosphoprotein containing a PDZ domain, a Src homology 3 (SH3) motif, and a guanylate kinase domain. This gene product interacts with various cytoskeletal proteins and cell junctional proteins in different tissue and …

**Accessions** — [HGNC:7219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7219) · Entrez [4354](https://www.ncbi.nlm.nih.gov/gene/4354) · UniProt [Q00013](https://www.uniprot.org/uniprotkb/Q00013) · Ensembl [ENSG00000130830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130830)

## Data

Gene col 5140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5140); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5140]; `tensor/DDL_lfc|DDL_z.npy` [5140]; `embed/gene_vectors.npy` [5140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5140 or target_col == 5140). Every well: [[MPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
