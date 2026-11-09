---
symbol: "NFATC4"
type: "gene"
col: 2050
ensembl_id: "ENSG00000100968"
name: "nuclear factor of activated T cells 4"
location: "14q12"
module: 35
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# NFATC4

*nuclear factor of activated T cells 4* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +4.3, q 0.010, up in 10 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.280× (z -10.9, q 6e-25, down in 24 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CA11]] (+0.54, fdr 4e-05), [[SFTA3-1]] (+0.54, fdr 3e-05), [[HOXB-AS1]] (+0.53, fdr 3e-05); moves opposite to [[LYPLA1]] (-0.50, fdr 1e-04), [[ANKS6]] (-0.49, fdr 1e-04), [[VKORC1L1]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EDIL3]] → it (grade B ⚠); 7 go from it, the strongest it → [[ABCA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.010 | 10/25 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.88×** | +3.9 | 0.032 | 7/22 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.062 | 11/28 (BT-474, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Thymol (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.080 | 3/28 (SW 900, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.4 | 0.088 | 1/8 (HOP62) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.68× | +3.2 | 0.13 | 3/24 (SHP-77, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.43× | +3.1 | 0.17 | 4/28 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.97× | +3.0 | 0.17 | 1/8 (C32) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.280×** | -10.9 | 6e-25 | 24/28 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.297×** | -10.4 | 6e-23 | 23/28 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.303×** | -10.2 | 2e-22 | 24/29 (HT-29, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.423×** | -7.4 | 2e-11 | 19/28 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.524×** | -5.5 | 4e-06 | 15/25 (C32, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.542×** | -5.3 | 1e-05 | 12/29 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.548×** | -5.2 | 2e-05 | 17/29 (NCI-H1573, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.531×** | -5.1 | 2e-05 | 17/28 (LS 180, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -4.8 | 9e-05 | 15/28 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.602×** | -4.3 | 8e-04 | 15/29 (HCT15, SW 900, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -4.3 | 8e-04 | 12/28 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.607×** | -4.3 | 9e-04 | 16/28 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.619×** | -4.1 | 0.002 | 16/24 (SW480, C32, …) | all doses, stronger at high dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.436×** | -3.7 | 0.008 | 11/23 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -3.7 | 0.009 | 9/25 (NCI-H1573, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -3.5 | 0.018 | 14/27 (C32, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -3.4 | 0.019 | 10/27 (C32, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.691×** | -3.2 | 0.050 | 10/28 (CHP-212, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.498×** | -3.1 | 0.054 | 9/23 (NCI-H23, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.698×** | -3.1 | 0.055 | 7/28 (Panc 03.27, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 21.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0791× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 6.07 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0422× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 9.64 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0540× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0996× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0172× (z -13.4) |
| [[SW480 (line)]] | alt | 2.40 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0546× (z -8.8) |
| [[COLO 205 (line)]] | alt | 5.08 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 9.89 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0464× (z -9.0) |
| [[HT-29 (line)]] | alt | 5.46 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0142× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 4.22 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0371× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.161× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0475× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 3.82 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0373× (z -9.0) |
| [[A-172 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA11]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SFTA3-1]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[HOXB-AS1]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[PPFIA3]] | +0.51 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TGFB3]] | +0.51 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[DTX3]] | +0.50 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[UBR5]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[PI15]] | +0.49 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[FGF11]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[UPK2]] | +0.48 | +0.26 / +0.44 | both halves | 4e-04 |  |
| [[WBP1]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[PRRT2]] | +0.47 | +0.38 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLA1]] | -0.50 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[ANKS6]] | -0.49 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[VKORC1L1]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TSEN2]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SIMC1]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CLYBL]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[LINC02666]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[HLCS]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[EIF2B3]] | -0.44 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[EEFSEC]] | -0.44 | -0.24 / -0.50 | both halves | 5e-04 |  |
| [[ASAP2]] | -0.44 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[NUDCD1]] | -0.43 | -0.33 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDIL3]] | B | EDIL3 activity raises NFATC4's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without EDIL3 | 0.003 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[ABCA3]] | B | ABCA3 activity lowers NFATC4's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.29× higher at baseline in the lines without ABCA3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[NLGN1]] | B | NLGN1 activity raises NFATC4's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without NLGN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | NFATC4 activity lowers ABCA3's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 1.87× higher at baseline in the lines without NFATC4 | 0.027 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[EDIL3]] | B | NFATC4 activity raises EDIL3's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without NFATC4 | 0.043 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[CCL28]] | B | NFATC4 activity raises CCL28's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without NFATC4 | 0.055 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[PTPRD]] | B | NFATC4 activity raises PTPRD's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 2.44× lower at baseline in the lines without NFATC4 | 0.062 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[NUDCD1]] | B | NFATC4 activity lowers NUDCD1's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 1.42× higher at baseline in the lines without NFATC4 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM | B | NFATC4 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express NFATC4 (17) vs lines expressing it (31) | the lines without NFATC4: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[FAP]] | C | NFATC4 activity raises FAP's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 3.14× lower at baseline in the lines without NFATC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1; co-absent with the target |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.365). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (22.6, 21.2); signed map (36.2, -3.6). **Vector** length 56.0, 11.6% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | -0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -10.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor of activated T cells 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,365,673-24,379,604 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NFAT3 |
| Gene groups (HGNC) | Nuclear factors of activated T-cells; IPT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14934](https://www.uniprot.org/uniprotkb/Q14934) (Nuclear factor of activated T-cells, cytoplasmic 4):

> Ca(2+)-regulated transcription factor that is involved in several processes, including the development and function of the immune, cardiovascular, musculoskeletal, and nervous systems. Involved in T-cell activation, stimulating the transcription of cytokine genes, including that of IL2 and IL4. Along with NFATC3, involved in embryonic heart development. Following JAK/STAT signaling activation and as part of a complex with NFATC3 and STAT3, binds to the alpha-beta E4 promoter region of CRYAB and …

**Summary**, from NCBI Gene [4776](https://www.ncbi.nlm.nih.gov/gene/4776):

> This gene encodes a member of the nuclear factor of activated T cells (NFAT) protein family. The encoded protein is part of a DNA-binding transcription complex. This complex consists of at least two components: a preexisting cytosolic component that translocates to the nucleus upon T cell receptor stimulation and an inducible nuclear component. NFAT proteins are activated by the calmodulin-dependent phosphatase, calcineurin. The encoded protein plays a role in the inducible expression of …

**Accessions** — [HGNC:7778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7778) · Entrez [4776](https://www.ncbi.nlm.nih.gov/gene/4776) · UniProt [Q14934](https://www.uniprot.org/uniprotkb/Q14934) · Ensembl [ENSG00000100968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100968)

## Data

Gene col 2050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2050); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2050]; `tensor/DDL_lfc|DDL_z.npy` [2050]; `embed/gene_vectors.npy` [2050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2050 or target_col == 2050). Every well: [[NFATC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFATC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
