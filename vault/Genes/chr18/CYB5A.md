---
symbol: "CYB5A"
type: "gene"
col: 9290
ensembl_id: "ENSG00000166347"
name: "cytochrome b5 type A"
location: "18q22.3"
module: 45
arm: "+"
pooled_cpm: 15.86
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 8
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CYB5A

*cytochrome b5 type A* — 18q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.55× (z +14.5, q 1e-44, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +11.4, q 1e-27, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.573× (z -6.3, q 1e-07, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM14A]] (+0.71, fdr 1e-05), [[HMGN3]] (+0.67, fdr 2e-05), [[ORC4]] (+0.67, fdr 7e-06); moves opposite to [[KCNJ14]] (-0.59, fdr 1e-05), [[CREM]] (-0.59, fdr 3e-05), [[FAM120B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 8 go from it, the strongest it → [[PRR14L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.55×** | +14.5 | 1e-44 | 34/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +11.4 | 1e-27 | 39/42 (RKO, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.96×** | +11.1 | 3e-26 | 23/25 (J82, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.57×** | +10.8 | 5e-25 | 39/42 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.57×** | +10.8 | 5e-25 | 37/42 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.40×** | +9.3 | 2e-18 | 25/29 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.08×** | +8.4 | 4e-15 | 37/41 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +6.3 | 2e-08 | 30/42 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +5.9 | 3e-07 | 24/41 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.67×** | +5.2 | 1e-05 | 23/39 (LoVo, J82, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.61×** | +5.2 | 1e-05 | 22/42 (BT-474, SW48, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 24/42 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.35×** | +3.1 | 0.091 | 13/36 (J82, HepG2/C3A, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.100 | 4/41 (A549, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -6.3 | 1e-07 | 28/41 (LOX-IMVI, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.7 | 2e-06 | 21/42 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.606×** | -5.7 | 2e-06 | 23/42 (SW1417, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -5.6 | 3e-06 | 26/41 (LOX-IMVI, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.681×** | -4.4 | 0.001 | 15/41 (KATO III, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.682×** | -4.1 | 0.004 | 21/42 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -3.6 | 0.025 | 10/41 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -3.2 | 0.078 | 14/41 (NCI-H23, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.546×** | -3.2 | 0.078 | 8/41 (BT-474, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.556×** | -3.1 | 0.092 | 8/42 (BT-474, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -3.1 | 0.092 | 17/40 (HT-29, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 0.768× | -3.0 | 0.12 | 11/37 (SHP-77, Hs 766T, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.691× | -3.0 | 0.12 | 6/42 (KATO III, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 23.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 15.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 24.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 16.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0623× (z -9.6) |
| [[C32 (line)]] | wt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.87 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 11.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.55× (z +8.6) | — |
| [[SW480 (line)]] | alt | 5.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14A]] | +0.71 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.67 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[ORC4]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.66 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TMEM106C]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[TBC1D2B]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CAT]] | +0.65 | +0.50 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[EHMT2]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ALAD]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNJ14]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CREM]] | -0.59 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[CDR2]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[MRPL45P2]] | -0.57 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CDK12]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[MIATNB]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[LRRC41]] | -0.56 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PRR14L]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR14L]] | B | CYB5A activity raises PRR14L's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without CYB5A | 0.035 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[NIPSNAP1]] | B | CYB5A activity raises NIPSNAP1's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without CYB5A | 0.048 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[ALAD]] | B | CYB5A activity raises ALAD's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CYB5A | 0.058 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[MDH1]] | B | CYB5A activity raises MDH1's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.14× lower at baseline in the lines without CYB5A | 0.071 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[THYN1]] | B | CYB5A activity raises THYN1's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without CYB5A | 0.090 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[BBS2]] | B | CYB5A activity raises BBS2's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without CYB5A | 0.091 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[ABHD10]] | B | CYB5A activity raises ABHD10's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without CYB5A | 0.096 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[TMEM106C]] | B | CYB5A activity raises TMEM106C's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without CYB5A | 0.098 | ⚠ within organs, on part of the lines; also absent: FGF11 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.3, -8.2); signed map (-28.6, -7.3). **Vector** length 92.0, 23.3% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | +5.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +5.0 | +14.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 type A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.3 — chr18:74,250,846-74,291,973 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCB5; previously CYB5 |
| Gene groups (HGNC) | Cytochrome b5 domain containing |
| Hallmark sets | XENOBIOTIC_METABOLISM, GLYCOLYSIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Vitamin C (ascorbate) metabolism; Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P00167](https://www.uniprot.org/uniprotkb/P00167) (Cytochrome b5):

> Cytochrome b5 is a membrane-bound hemoprotein functioning as an electron carrier for several membrane-bound oxygenases.

**Summary**, from NCBI Gene [1528](https://www.ncbi.nlm.nih.gov/gene/1528):

> The protein encoded by this gene is a membrane-bound cytochrome that reduces ferric hemoglobin (methemoglobin) to ferrous hemoglobin, which is required for stearyl-CoA-desaturase activity. Defects in this gene are a cause of type IV hereditary methemoglobinemia. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:2570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2570) · Entrez [1528](https://www.ncbi.nlm.nih.gov/gene/1528) · UniProt [P00167](https://www.uniprot.org/uniprotkb/P00167) · Ensembl [ENSG00000166347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166347)

## Data

Gene col 9290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9290); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9290]; `tensor/DDL_lfc|DDL_z.npy` [9290]; `embed/gene_vectors.npy` [9290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9290 or target_col == 9290). Every well: [[CYB5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
