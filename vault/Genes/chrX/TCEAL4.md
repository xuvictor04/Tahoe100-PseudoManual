---
symbol: "TCEAL4"
type: "gene"
col: 5427
ensembl_id: "ENSG00000133142"
name: "transcription elongation factor A like 4"
location: "Xq22.2"
module: 68
arm: "+"
pooled_cpm: 69.83
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TCEAL4

*transcription elongation factor A like 4* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.07× (z +10.6, q 2e-23, up in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +8.4, q 6e-15, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.583× (z -5.1, q 2e-04, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF563]] (+0.74, fdr 1e-05), [[WAC-AS1]] (+0.73, fdr 1e-05), [[TCEAL1]] (+0.70, fdr 1e-05, ⚠ same locus), [[PHYH]] (+0.70, fdr 4e-05); moves opposite to [[FBXW2]] (-0.69, fdr 1e-05), [[ST6GALNAC4]] (-0.66, fdr 8e-05), [[GNB1L]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +10.6 | 2e-23 | 46/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +8.8 | 3e-16 | 41/43 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +8.4 | 6e-15 | 44/47 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.10×** | +6.8 | 2e-09 | 45/47 (AsPC-1, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +6.2 | 8e-08 | 39/44 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.9 | 3e-07 | 45/46 (CFPAC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.6 | 2e-06 | 40/47 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.48×** | +5.3 | 1e-05 | 31/47 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.71×** | +5.1 | 3e-05 | 37/46 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.60×** | +4.4 | 6e-04 | 31/47 (A-172, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.003 | 30/49 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.005 | 34/47 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.010 | 27/47 (A-172, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.028 | 34/47 (AsPC-1, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.583×** | -5.1 | 2e-04 | 39/47 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.422×** | -4.3 | 0.004 | 37/47 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.640×** | -4.2 | 0.004 | 33/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.015 | 32/47 (SW 1088, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.707× | -3.3 | 0.11 | 26/46 (SW 1271, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.714× | -3.2 | 0.13 | 28/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.533× | -3.1 | 0.15 | 32/47 (AN3 CA, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 52.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.1) | — |
| [[A-172 (line)]] | wt | 54.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 66.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 48.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +12.0) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 46.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.9) | — |
| [[J82 (line)]] | alt | 116 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 124 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 82.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.0) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 166 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.3) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[H4 (line)]] | wt | 61.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 68.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 61.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.3) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 68.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 99.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 57.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 78.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 72.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.0) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[SW480 (line)]] | alt | 90.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF563]] | +0.74 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.73 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 | same gene group; STRING 963; ⚠ same locus (41.0 kb, same strand: neighbours can correlate without regulation) |
| [[PHYH]] | +0.70 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[CCAR1]] | +0.70 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[ATE1OSP]] | +0.69 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SDSL]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PLS3-AS1]] | +0.68 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[ZNF441]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[UBXN2A]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD26]] | +0.67 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[PATL2]] | +0.67 | +0.67 / +0.36 | both halves | 1e-04 |  |
| [[OXA1L-DT]] | +0.67 | +0.69 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.69 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.66 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[GNB1L]] | -0.65 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.64 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[LPCAT1]] | -0.62 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[SIPA1]] | -0.61 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[STRAP]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TRABD]] | -0.60 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[BRI3BP]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[AP3M2]] | -0.60 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[CHID1]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TCEAL4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers TCEAL4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-0.2, 13.2); signed map (17.7, -16.4). **Vector** length 102, 37.3% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +7.5 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.1 | +6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.2 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +1.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.2 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +2.2 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,576,231-103,587,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21174, WEX7 |
| Gene groups (HGNC) | Transcription elongation factor A like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EI5](https://www.uniprot.org/uniprotkb/Q96EI5) (Transcription elongation factor A protein-like 4):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [79921](https://www.ncbi.nlm.nih.gov/gene/79921):

> This gene encodes a member of the transcription elongation factor A (SII)-like (TCEAL) gene family. This family is comprised of nuclear phosphoproteins that modulate transcription in a promoter context-dependent manner. Multiple family members are located on the X chromosome. Alternatively splicing results in multiple transcript variants. There is a pseudogene for this gene on chromosome 13. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:26121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26121) · Entrez [79921](https://www.ncbi.nlm.nih.gov/gene/79921) · UniProt [Q96EI5](https://www.uniprot.org/uniprotkb/Q96EI5) · Ensembl [ENSG00000133142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133142)

## Data

Gene col 5427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5427); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5427]; `tensor/DDL_lfc|DDL_z.npy` [5427]; `embed/gene_vectors.npy` [5427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5427 or target_col == 5427). Every well: [[TCEAL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEAL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
