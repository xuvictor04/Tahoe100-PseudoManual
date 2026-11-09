---
symbol: "ARNT2"
type: "gene"
col: 10249
ensembl_id: "ENSG00000172379"
name: "aryl hydrocarbon receptor nuclear translocator 2"
location: "15q25.1"
module: 87
arm: "+"
pooled_cpm: 18.14
n_lines_expressing: 28
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# ARNT2

*aryl hydrocarbon receptor nuclear translocator 2* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +11.7, q 9e-29, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.497× (z -10.4, q 1e-22, down in 19 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARNT2-DT]] (+0.73, fdr 7e-06, ⚠ same locus), [[COL19A1]] (+0.62, fdr 1e-05), [[L3MBTL4]] (+0.62, fdr 1e-05), [[LEF1-AS1]] (+0.60, fdr 1e-05); moves opposite to [[HMBOX1]] (-0.54, fdr 5e-05), [[PPP1R12B]] (-0.50, fdr 4e-05), [[OXNAD1]] (-0.49, fdr 7e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZNF704]] → it (grade B ⚠); 11 go from it, the strongest it → [[STK32B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.7 | 9e-29 | 15/26 (BT-474, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +8.4 | 1e-14 | 15/26 (BT-474, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +8.0 | 2e-13 | 14/26 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.4 | 2e-08 | 15/25 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.1 | 0.005 | 0/20 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.006 | 8/26 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.39×** | +3.5 | 0.032 | 0/22 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.032 | 4/25 (A549, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.038 | 10/25 (LoVo, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.038 | 2/25 (NCI-H23, A-172) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.044 | 4/25 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.11 | 4/25 (A549, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -10.4 | 1e-22 | 19/25 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.525×** | -9.6 | 2e-19 | 18/26 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -7.1 | 2e-10 | 18/25 (LoVo, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.637×** | -6.7 | 2e-09 | 17/26 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -6.5 | 8e-09 | 18/26 (A549, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.701×** | -5.3 | 1e-05 | 14/26 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.711×** | -5.1 | 3e-05 | 14/26 (LoVo, NCI-H1792, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -4.3 | 0.001 | 10/25 (HOP62, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.004 | 9/26 (C32, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.8 | 0.009 | 9/26 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.837× | -3.7 | 0.009 | 7/26 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.019 | 13/25 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.789×** | -3.5 | 0.019 | 7/25 (H4, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.806×** | -3.2 | 0.055 | 5/25 (H4, NCI-H2030, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.814×** | -3.1 | 0.085 | 10/25 (LoVo, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 178 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 71.2 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0984× (z -15.4) |
| [[C-33 A (line)]] | alt | 66.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.213× (z -11.3) |
| [[A-172 (line)]] | wt | 26.3 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -11.2) |
| [[LoVo (line)]] | wt | 36.7 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.177× (z -14.5) |
| [[SW480 (line)]] | alt | 35.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -12.8) |
| [[RKO (line)]] | wt | 31.4 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -11.1) |
| [[A549 (line)]] | wt | 61.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -8.9) |
| [[BT-474 (line)]] | alt | 18.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +14.0) | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0584× (z -11.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.106× (z -8.7) |
| [[J82 (line)]] | alt | 4.59 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0552× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0579× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 29.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 6.35 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.48× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 9.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.4) | — |
| [[A-427 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT2-DT]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[COL19A1]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[L3MBTL4]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 | same gene group |
| [[LEF1-AS1]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[S1PR2]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[C10orf90]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[PHLDB1]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[STK32B]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[FRMD4A]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MIR3681HG]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TRPM8]] | +0.55 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[ZNF702P]] | +0.54 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[TNC]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMBOX1]] | -0.54 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R12B]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[OXNAD1]] | -0.49 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[TSPO]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CDS2]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ALDH6A1]] | -0.49 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[SEL1L]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[RARS2]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ATF6B]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TM9SF2]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ZDHHC7]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF704]] | B | ZNF704 activity raises ARNT2's level | lines that do not express ZNF704 (17) vs lines expressing it (33) | 2.45× lower at baseline in the lines without ZNF704 | 0.046 | ⚠ within organs, on part of the lines |
| [[DOCK2]] | B | DOCK2 activity raises ARNT2's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without DOCK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[ZNF462]] | B | ZNF462 activity raises ARNT2's level | lines that do not express ZNF462 (5) vs lines expressing it (45) | 3.95× lower at baseline in the lines without ZNF462 | 0.068 | ⚠ within organs, on part of the lines; also absent: PDE11A, ENSG00000214803 |
| [[SOX5]] | B | SOX5 activity raises ARNT2's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without SOX5 | 0.071 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5 |
| [[STK32B]] | B | STK32B activity raises ARNT2's level | lines that do not express STK32B (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without STK32B | 0.073 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[CNTNAP3]] | B | CNTNAP3 activity raises ARNT2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without CNTNAP3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[ARNT2-DT]] | C | ARNT2-DT activity raises ARNT2's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 6.95× lower at baseline in the lines without ARNT2-DT | 1e-05 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises ARNT2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without FRMD4A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[L3MBTL4]] | C | L3MBTL4 activity raises ARNT2's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without L3MBTL4 | 0.013 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1; co-absent with the target |
| [[ELOVL2]] | C | ELOVL2 activity raises ARNT2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without ELOVL2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK32B]] | B | ARNT2 activity raises STK32B's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without ARNT2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[LINC01239]] | B | ARNT2 activity raises LINC01239's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without ARNT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[C1QTNF1]] | B | ARNT2 activity raises C1QTNF1's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without ARNT2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[TRAF1]] | B | ARNT2 activity raises TRAF1's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.31× lower at baseline in the lines without ARNT2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[CHST11]] | B | ARNT2 activity raises CHST11's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.58× lower at baseline in the lines without ARNT2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[NKX3-1]] | B | ARNT2 activity raises NKX3-1's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without ARNT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[RTL6]] | B | ARNT2 activity raises RTL6's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.31× lower at baseline in the lines without ARNT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[ADAMTS3]] | B | ARNT2 activity raises ADAMTS3's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without ARNT2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015 |
| [[ARNT2-DT]] | C | ARNT2 activity raises ARNT2-DT's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without ARNT2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015; co-absent with the target |
| [[BOC]] | C | ARNT2 activity raises BOC's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without ARNT2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015; co-absent with the target |
| [[FRMD4A]] | C | ARNT2 activity raises FRMD4A's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 3.20× lower at baseline in the lines without ARNT2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.5, 28.0); signed map (28.0, 38.6). **Vector** length 81.4, 22.9% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.1 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.5 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.9 | -10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | aryl hydrocarbon receptor nuclear translocator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:80,404,350-80,597,933 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0307, bHLHe1 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MicroRNA protein coding host genes; PAS domain containing |
| Reactome | 11 pathways, smallest: Aryl hydrocarbon receptor signalling; Xenobiotics; Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBZ2](https://www.uniprot.org/uniprotkb/Q9HBZ2) (Aryl hydrocarbon receptor nuclear translocator 2):

> Transcription factor that plays a role in the development of the hypothalamo-pituitary axis, postnatal brain growth, and visual and renal function. Specifically recognizes the xenobiotic response element (XRE).

**Summary**, from NCBI Gene [9915](https://www.ncbi.nlm.nih.gov/gene/9915):

> This gene encodes a member of the basic-helix-loop-helix-Per-Arnt-Sim (bHLH-PAS) superfamily of transcription factors. The encoded protein acts as a partner for several sensor proteins of the bHLH-PAS family, forming heterodimers with the sensor proteins that bind regulatory DNA sequences in genes responsive to developmental and environmental stimuli. Under hypoxic conditions, the encoded protein complexes with hypoxia-inducible factor 1alpha in the nucleus and this complex binds to …

**Accessions** — [HGNC:16876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16876) · Entrez [9915](https://www.ncbi.nlm.nih.gov/gene/9915) · UniProt [Q9HBZ2](https://www.uniprot.org/uniprotkb/Q9HBZ2) · Ensembl [ENSG00000172379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172379)

## Data

Gene col 10249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10249); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10249]; `tensor/DDL_lfc|DDL_z.npy` [10249]; `embed/gene_vectors.npy` [10249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10249 or target_col == 10249). Every well: [[ARNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
