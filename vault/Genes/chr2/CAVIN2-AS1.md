---
symbol: "CAVIN2-AS1"
type: "gene"
col: 13921
ensembl_id: "ENSG00000233766"
name: "CAVIN2 and TMEFF2 antisense RNA 1"
location: "2q32.3"
module: 19
arm: "+"
pooled_cpm: 18.29
n_lines_expressing: 19
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CAVIN2-AS1

*CAVIN2 and TMEFF2 antisense RNA 1* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 23.1× (z +50.6, q 0e+00, up in 15 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Futibatinib (drug)]] 0.05 µM: 0.630× (z -5.0, q 3e-04, down in 2 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMNTD1]] (+0.69, fdr 7e-06), [[CAVIN2]] (+0.66, fdr 7e-06, ⚠ same locus), [[PDE1A]] (+0.64, fdr 8e-06), [[CPED1]] (+0.61, fdr 1e-05); moves opposite to [[CDR2L]] (-0.49, fdr 6e-05), [[DIP2A]] (-0.49, fdr 3e-05), [[TSPAN17]] (-0.48, fdr 5e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAVIN2]] → it (grade C ⚠); 4 go from it, the strongest it → [[LINC02269]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **23.1×** | +50.6 | 0e+00 | 15/16 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **11.6×** | +28.0 | 0e+00 | 14/16 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **7.48×** | +22.1 | 0e+00 | 12/17 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.20×** | +18.7 | 0e+00 | 5/16 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.20×** | +16.4 | 0e+00 | 6/16 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.34×** | +9.7 | 4e-20 | 5/17 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +9.5 | 1e-19 | 7/16 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.2 | 4e-18 | 2/15 (J82, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.9 | 2e-13 | 1/16 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +6.9 | 4e-10 | 8/17 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +6.4 | 8e-09 | 5/16 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.2 | 2e-08 | 5/16 (A-172, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.2 | 3e-08 | 1/15 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +6.0 | 6e-08 | 14/17 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.65×** | +5.7 | 5e-07 | 14/16 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 2e-06 | 3/16 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +5.3 | 5e-06 | 7/16 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +5.0 | 1e-05 | 11/16 (NCI-H2347, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Futibatinib (drug)]] 0.05 µM |  | **0.630×** | -5.0 | 3e-04 | 2/16 (Hs 766T, NCI-H1573) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.713×** | -3.9 | 0.029 | 9/17 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.735×** | -3.5 | 0.075 | 12/16 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.095 | 7/17 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.752× | -3.1 | 0.19 | 1/16 (J82) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.751× | -3.0 | 0.22 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.6 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0603× (z -16.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0973× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 50.8 | 9 | 0 | [[Panobinostat (drug)]] 0.5 µM 55.7× (z +19.4) | — |
| [[HepG2_C3A (line)]] | wt | 200 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -15.2) |
| [[Hs 766T (line)]] | wt | 39.0 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0852× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.211× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.66× (z +8.7) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.163× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 110 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +10.4) | [[Bortezomib (drug)]] 0.05 µM 0.205× (z -9.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.9) |
| [[SW480 (line)]] | alt | 12.7 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +17.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.195× (z -9.7) |
| [[J82 (line)]] | alt | 8.85 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +19.6) | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 58.5× (z +23.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0943× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 84.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.216× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.7× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 6.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.8× (z +17.5) | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +14.0) | — |
| [[A-172 (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 6.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +12.0) | — |
| [[A-427 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMNTD1]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CAVIN2]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PDE1A]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[CPED1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ALPK2]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NALCN]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[IGSF1]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[LINC02945]] | +0.54 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SLFN12]] | +0.54 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[DLEU1]] | +0.53 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[CDH7]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SLC6A7]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ABCC9]] | +0.53 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2L]] | -0.49 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[DIP2A]] | -0.49 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[TSPAN17]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[TPST2]] | -0.46 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[CERS5]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CORO7]] | -0.45 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[SENP5]] | -0.45 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ASB16-AS1]] | -0.45 | -0.38 / -0.29 | both halves | 2e-04 | same gene group |
| [[FARP2]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CD81]] | -0.45 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[CCDC168]] | -0.44 | -0.37 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAVIN2]] | C | CAVIN2 activity raises CAVIN2-AS1's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 6.14× lower at baseline in the lines without CAVIN2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises CAVIN2-AS1's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without NLGN4Y | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02269]] | B | CAVIN2-AS1 activity raises LINC02269's level | lines that do not express CAVIN2-AS1 (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without CAVIN2-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CAVIN2, NLGN4Y, LINC02154 |
| [[LINC01836]] | B | CAVIN2-AS1 activity raises LINC01836's level | lines that do not express CAVIN2-AS1 (31) vs lines expressing it (19) | 1.20× lower at baseline in the lines without CAVIN2-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CAVIN2, NLGN4Y, LINC02154 |
| [[CAVIN2]] | C | CAVIN2-AS1 activity raises CAVIN2's level | lines that do not express CAVIN2-AS1 (31) vs lines expressing it (19) | 5.11× lower at baseline in the lines without CAVIN2-AS1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CAVIN2, NLGN4Y, LINC02154; co-absent with the target |
| [[NLGN4Y]] | C | CAVIN2-AS1 activity raises NLGN4Y's level | lines that do not express CAVIN2-AS1 (31) vs lines expressing it (19) | 3.28× lower at baseline in the lines without CAVIN2-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: CAVIN2, NLGN4Y, LINC02154; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, 26.6); signed map (41.6, 28.1). **Vector** length 66.0, 20.5% of its response variance represented; |z| ≥ 3 in 525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +50.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +28.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +22.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +16.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +9.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +4.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +5.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | +1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | CAVIN2 and TMEFF2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q32.3 — chr2:191,846,534-192,044,525 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC105373813 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40517) · Entrez [105373813](https://www.ncbi.nlm.nih.gov/gene/105373813) · Ensembl [ENSG00000233766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233766)

## Data

Gene col 13921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13921); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13921]; `tensor/DDL_lfc|DDL_z.npy` [13921]; `embed/gene_vectors.npy` [13921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13921 or target_col == 13921). Every well: [[CAVIN2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAVIN2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
