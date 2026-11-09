---
symbol: "DPY19L2"
type: "gene"
col: 10886
ensembl_id: "ENSG00000177990"
name: "dpy-19 like 2"
location: "12q14.2"
module: 121
arm: "+"
pooled_cpm: 7.05
n_lines_expressing: 28
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 16
direction_downstream: 17
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# DPY19L2

*dpy-19 like 2* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.02× (z +14.8, q 0e+00, up in 19 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.377× (z -9.2, q 7e-18, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L2P2-1]] (+0.76, fdr 7e-06), [[MAGI2-AS3]] (+0.74, fdr 7e-06), [[DPY19L2P2]] (+0.73, fdr 7e-06); moves opposite to [[TPST2]] (-0.56, fdr 2e-05), [[RALGPS1]] (-0.52, fdr 1e-04), [[WIPI1]] (-0.52, fdr 7e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PLS3-AS1]] → it (grade B ⚠); 17 go from it, the strongest it → [[C7orf31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +14.8 | 0e+00 | 19/22 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.86×** | +8.3 | 2e-14 | 17/24 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.25×** | +7.7 | 3e-12 | 19/24 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +7.2 | 1e-10 | 12/21 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +6.7 | 2e-09 | 15/24 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.7 | 1e-06 | 11/23 (A-172, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 9e-06 | 16/23 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.7 | 2e-04 | 10/21 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.62×** | +4.5 | 4e-04 | 13/23 (NCI-H2030, hTERT-HPNE, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 12/24 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.013 | 9/22 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.019 | 11/24 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.045 | 4/23 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.045 | 6/24 (A-427, C-33 A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +3.2 | 0.061 | 8/24 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.064 | 4/23 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.377×** | -9.2 | 7e-18 | 21/24 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.377×** | -9.2 | 7e-18 | 18/24 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.442×** | -7.7 | 2e-12 | 16/23 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.447×** | -7.6 | 3e-12 | 16/23 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.461×** | -7.3 | 2e-11 | 18/23 (C32, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.500×** | -6.2 | 5e-08 | 17/23 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.539×** | -5.7 | 8e-07 | 13/24 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -5.0 | 5e-05 | 16/23 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.763×** | -3.6 | 0.018 | 8/23 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.3 | 0.048 | 9/23 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.705×** | -3.3 | 0.049 | 8/24 (C32, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.544× | -3.0 | 0.12 | 12/16 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 36.0 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0185× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0797× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 17.4 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -11.3) |
| [[PANC-1 (line)]] | alt | 12.6 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.233× (z -9.7) |
| [[A-172 (line)]] | wt | 6.65 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.9) | [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 7.92 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0981× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -9.3) |
| [[A-427 (line)]] | wt | 11.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -9.5) |
| [[A549 (line)]] | wt | 4.05 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0716× (z -8.6) |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0502× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +10.1) | — |
| [[H4 (line)]] | wt | 9.03 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0612× (z -8.8) |
| [[HOP62 (line)]] | alt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 4.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.99× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +12.0) | — |
| [[J82 (line)]] | alt | 4.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +13.5) | — |
| [[A498 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.597 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | +0.76 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[MAGI2-AS3]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[DPY19L2P2]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[LINC00882]] | +0.68 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[NLGN1]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[FRG1-DT]] | +0.63 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[DPH6-DT]] | +0.62 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[PLS3-AS1]] | +0.61 | +0.65 / +0.43 | both halves | 4e-05 |  |
| [[EIF1B-AS1]] | +0.61 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[KCNT2]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RBMS3]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[RALGPS1]] | -0.52 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[WIPI1]] | -0.52 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[ATP7B]] | -0.52 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[DIP2A]] | -0.51 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[GTF2E2]] | -0.51 | -0.53 / -0.32 | both halves | 1e-04 |  |
| [[HERC2P2]] | -0.51 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[GSDMB]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises DPY19L2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without PLS3-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[PSMB5]] | B | PSMB5 activity raises DPY19L2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAGI2]] | C | MAGI2 activity raises DPY19L2's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 3.76× lower at baseline in the lines without MAGI2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises DPY19L2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without MAGI2-AS3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises DPY19L2's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.95× lower at baseline in the lines without NEGR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises DPY19L2's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 3.02× lower at baseline in the lines without FAT4 | 0.031 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises DPY19L2's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without NLGN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[NREP]] | C | NREP activity raises DPY19L2's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.72× lower at baseline in the lines without NREP | 0.061 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[DPY19L2P2-1]] | C | DPY19L2P2-1 activity raises DPY19L2's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 3.34× lower at baseline in the lines without DPY19L2P2-1 | 0.062 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2; co-absent with the target |
| [[CCDC169]] | C | CCDC169 activity raises DPY19L2's level | lines that do not express CCDC169 (17) vs lines expressing it (33) | 2.85× lower at baseline in the lines without CCDC169 | 0.074 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, SPART, FIGN; co-absent with the target; its own permutation p |
| [[FMN2]] | C | FMN2 activity raises DPY19L2's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without FMN2 | 0.075 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[PCDH7]] | C | PCDH7 activity raises DPY19L2's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 2.68× lower at baseline in the lines without PCDH7 | 0.080 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C7orf31]] | B | DPY19L2 activity raises C7orf31's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without DPY19L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[LINC01013]] | B | DPY19L2 activity raises LINC01013's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without DPY19L2 | 0.030 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[TENM3-AS1]] | B | DPY19L2 activity raises TENM3-AS1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without DPY19L2 | 0.040 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[RIPK2-DT]] | B | DPY19L2 activity raises RIPK2-DT's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without DPY19L2 | 0.055 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[EIF1B-AS1]] | B | DPY19L2 activity raises EIF1B-AS1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without DPY19L2 | 0.065 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ |
| [[FAT4]] | C | DPY19L2 activity raises FAT4's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 5.83× lower at baseline in the lines without DPY19L2 | 0.003 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[NREP]] | C | DPY19L2 activity raises NREP's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 4.61× lower at baseline in the lines without DPY19L2 | 0.003 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[NEGR1]] | C | DPY19L2 activity raises NEGR1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 4.65× lower at baseline in the lines without DPY19L2 | 0.014 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[LINC00882]] | C | DPY19L2 activity raises LINC00882's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 3.79× lower at baseline in the lines without DPY19L2 | 0.028 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[MAGI2-AS3]] | C | DPY19L2 activity raises MAGI2-AS3's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 4.31× lower at baseline in the lines without DPY19L2 | 0.038 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[BEND6]] | C | DPY19L2 activity raises BEND6's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 2.84× lower at baseline in the lines without DPY19L2 | 0.048 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[MAGI2]] | C | DPY19L2 activity raises MAGI2's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 5.50× lower at baseline in the lines without DPY19L2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 25.4); signed map (44.0, 25.8). **Vector** length 73.4, 20.9% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +7.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | dpy-19 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:63,558,913-63,668,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32949, SPATA34 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUT2](https://www.uniprot.org/uniprotkb/Q6NUT2) (Probable C-mannosyltransferase DPY19L2):

> Probable C-mannosyltransferase that mediates C-mannosylation of tryptophan residues on target proteins.; Required during spermatogenesis for sperm head elongation and acrosome formation. Also plays a role in acrosome attachment to the nuclear envelope (By similarity).

**Summary**, from NCBI Gene [283417](https://www.ncbi.nlm.nih.gov/gene/283417):

> The protein encoded by this gene belongs to the dpy-19 family. It is highly expressed in testis, and is required for sperm head elongation and acrosome formation during spermatogenesis. Mutations in this gene are associated with an infertility disorder, spermatogenic failure type 9 (SPGF9). [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:19414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19414) · Entrez [283417](https://www.ncbi.nlm.nih.gov/gene/283417) · UniProt [Q6NUT2](https://www.uniprot.org/uniprotkb/Q6NUT2) · Ensembl [ENSG00000177990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177990)

## Data

Gene col 10886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10886); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10886]; `tensor/DDL_lfc|DDL_z.npy` [10886]; `embed/gene_vectors.npy` [10886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10886 or target_col == 10886). Every well: [[DPY19L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
