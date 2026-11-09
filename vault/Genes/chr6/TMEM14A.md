---
symbol: "TMEM14A"
type: "gene"
col: 1763
ensembl_id: "ENSG00000096092"
name: "transmembrane protein 14A"
location: "6p12.2"
module: 45
arm: "+"
pooled_cpm: 17.58
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TMEM14A

*transmembrane protein 14A* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.08× (z +10.8, q 1e-24, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.503× (z -7.2, q 4e-10, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGN3]] (+0.79, fdr 7e-06), [[CAT]] (+0.74, fdr 7e-06), [[ORC4]] (+0.72, fdr 7e-06); moves opposite to [[ENOX2]] (-0.66, fdr 1e-05), [[MYH3]] (-0.64, fdr 5e-05), [[HCG18]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TSPAN7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +10.8 | 1e-24 | 45/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.39×** | +9.1 | 3e-17 | 34/41 (NCI-H1573, NCI-H2030, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.18×** | +8.1 | 8e-14 | 39/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.15×** | +8.0 | 2e-13 | 38/48 (LOX-IMVI, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.07×** | +7.6 | 4e-12 | 39/48 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +6.7 | 1e-09 | 40/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +6.7 | 2e-09 | 35/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.7 | 9e-07 | 28/48 (C32, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +5.5 | 2e-06 | 32/48 (C32, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.73×** | +5.5 | 2e-06 | 19/28 (NCI-H460, HT-29, …) | all doses, flat | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.44×** | +5.4 | 4e-06 | 38/48 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.71×** | +5.2 | 9e-06 | 23/36 (A-172, HCT15, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.7 | 9e-05 | 27/43 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.001 | 15/48 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.004 | 21/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.024 | 19/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -7.2 | 4e-10 | 31/47 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.582×** | -5.6 | 5e-06 | 31/48 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -5.4 | 1e-05 | 29/47 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.608×** | -5.2 | 3e-05 | 27/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.580×** | -4.9 | 1e-04 | 28/48 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -4.8 | 2e-04 | 24/48 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.755×** | -4.1 | 0.003 | 26/46 (NCI-H23, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -3.9 | 0.007 | 25/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.009 | 25/46 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.744× | -3.1 | 0.12 | 16/47 (SNU-423, SW480, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.530× | -3.0 | 0.14 | 8/48 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0678× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0562× (z -12.1) |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.40× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 8.29 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -9.0) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | +0.79 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[CAT]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ORC4]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CYB5A]] | +0.71 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ALAD]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.67 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PIP4P2]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.66 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.65 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[ACACB]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[GGH]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RADX]] | +0.65 | +0.46 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.66 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MYH3]] | -0.64 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[HCG18]] | -0.63 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ANKMY1]] | -0.61 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[QRICH2]] | -0.60 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.60 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[AVEN]] | -0.60 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[DESI1]] | -0.59 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CDR2]] | -0.59 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SMIM15-AS1]] | -0.59 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[IDI2-AS1]] | -0.59 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[DPH5-DT]] | -0.58 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN7]] | B | TSPAN7 activity lowers TMEM14A's level | lines that do not express TSPAN7 (22) vs lines expressing it (28) | 1.25× higher at baseline in the lines without TSPAN7 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02147, LINC00992, PINCR; maybe low, not absent |
| [[VWA5A]] | B | VWA5A activity raises TMEM14A's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without VWA5A | 0.082 | ⚠ within organs, on part of the lines |
| [[PSMB5]] | B | PSMB5 activity raises TMEM14A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC44A2]] | C | SLC44A2 activity raises TMEM14A's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without SLC44A2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.5, -8.3); signed map (-28.6, -7.5). **Vector** length 92.1, 23.4% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Iron uptake and transport* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +5.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.5 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 14A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.2 — chr6:52,671,113-52,686,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTD011, C6orf73 |
| Gene groups (HGNC) | Transmembrane protein 14 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6G1](https://www.uniprot.org/uniprotkb/Q9Y6G1) (Transmembrane protein 14A):

> Inhibits apoptosis via negative regulation of the mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway.

**Summary**, from NCBI Gene [28978](https://www.ncbi.nlm.nih.gov/gene/28978):

> Involved in negative regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway. Located in endoplasmic reticulum membrane and mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21076) · Entrez [28978](https://www.ncbi.nlm.nih.gov/gene/28978) · UniProt [Q9Y6G1](https://www.uniprot.org/uniprotkb/Q9Y6G1) · Ensembl [ENSG00000096092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096092)

## Data

Gene col 1763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1763); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1763]; `tensor/DDL_lfc|DDL_z.npy` [1763]; `embed/gene_vectors.npy` [1763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1763 or target_col == 1763). Every well: [[TMEM14A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM14A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
