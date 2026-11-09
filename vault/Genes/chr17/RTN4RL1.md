---
symbol: "RTN4RL1"
type: "gene"
col: 11754
ensembl_id: "ENSG00000185924"
name: "reticulon 4 receptor like 1"
location: "17p13.3"
module: 98
arm: "+"
pooled_cpm: 4.8
n_lines_expressing: 36
n_dd_up: 43
n_dd_down: 8
n_dd_up_clean: 32
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 16
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# RTN4RL1

*reticulon 4 receptor like 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.72× (z +32.4, q 0e+00, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.522× (z -6.9, q 3e-09, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPOR2]] (+0.69, fdr 7e-06), [[KCNB1]] (+0.66, fdr 9e-06), [[KLF9]] (+0.59, fdr 1e-05); moves opposite to [[SIRLNT]] (-0.52, fdr 3e-05), [[GJA1]] (-0.48, fdr 3e-05), [[RSPO3]] (-0.46, fdr 6e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GCNT1]] → it (grade B ⚠); 16 go from it, the strongest it → [[ADAMTSL4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.72×** | +32.4 | 0e+00 | 24/25 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **4.16×** | +21.3 | 0e+00 | 14/24 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +12.0 | 5e-31 | 21/31 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +10.0 | 3e-21 | 4/16 (RPMI-7951, SW 900, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +9.0 | 4e-17 | 19/32 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +8.8 | 1e-16 | 17/31 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.3 | 6e-15 | 1/6 (A-172) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +8.2 | 2e-14 | 2/9 (PANC-1, SW1417) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **2.06×** | +7.6 | 1e-12 | 15/30 (HS-578T, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.02×** | +7.4 | 5e-12 | 14/28 (HS-578T, A498, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +7.2 | 3e-11 | 12/23 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.61×** | +7.1 | 5e-11 | 15/31 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +7.1 | 5e-11 | 14/26 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.79×** | +6.1 | 3e-08 | 13/30 (HS-578T, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.72×** | +5.7 | 4e-07 | 13/31 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.6 | 1e-06 | 7/28 (SW480, NCI-H460, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.4 | 2e-06 | 14/31 (HS-578T, A498, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.68×** | +5.0 | 1e-05 | 12/27 (HS-578T, A498, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.47×** | +5.0 | 2e-05 | 10/28 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 1e-04 | 5/31 (A498, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.522×** | -6.9 | 3e-09 | 19/31 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.577×** | -5.8 | 2e-06 | 15/28 (C32, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.605×** | -5.3 | 2e-05 | 15/31 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.623×** | -5.0 | 6e-05 | 16/32 (SNU-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.623×** | -5.0 | 6e-05 | 12/32 (LoVo, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -5.0 | 7e-05 | 14/24 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.712×** | -3.6 | 0.024 | 10/28 (HOP62, C-33 A, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.05 µM |  | **0.727×** | -3.4 | 0.050 | 2/26 (SNU-1, BT-474) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.751× | -3.0 | 0.15 | 9/28 (BT-474, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.06 | 13 | 1 | [[Triamcinolone (drug)]] 5 µM 7.21× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -8.8) |
| [[A498 (line)]] | wt | 13.6 | 9 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +16.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -9.0) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0589× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.204× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 3.56 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.6× (z +18.5) | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0350× (z -15.1) |
| [[LoVo (line)]] | wt | 4.16 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +11.3) ⚠ position correction uncertain | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -8.7) |
| [[SW480 (line)]] | alt | 2.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +14.6) | — |
| [[A-172 (line)]] | wt | 12.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.153× (z -10.0) |
| [[A549 (line)]] | wt | 4.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.7× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +9.8) | — |
| [[J82 (line)]] | alt | 1.61 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +9.2) ⚠ position correction uncertain | — |
| [[LS 180 (line)]] | wt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 5.15 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +9.2) ⚠ position correction uncertain | — |
| [[SW1417 (line)]] | alt | 4.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +8.6) | — |
| [[A-427 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.929 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPOR2]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KCNB1]] | +0.66 | +0.57 / +0.70 | both halves | 9e-06 | **novel candidate** |
| [[KLF9]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ITGA10]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[EFHD1]] | +0.56 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[FOXC2]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[IRX3]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[EDN2]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ACSL1]] | +0.53 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[GJA1]] | -0.48 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[RSPO3]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[TNFRSF11B]] | -0.45 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[NCKAP5]] | -0.44 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[C5orf46]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[EXT1]] | -0.44 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ANXA10]] | -0.44 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[IGFN1]] | -0.43 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[PAK3]] | -0.43 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[BMPER]] | -0.42 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[KIRREL3]] | -0.42 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCNT1]] | B | GCNT1 activity lowers RTN4RL1's level | lines that do not express GCNT1 (5) vs lines expressing it (45) | 2.64× higher at baseline in the lines without GCNT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ANKH, MLLT3, TLE4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RTN4RL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TLR6]] | B | TLR6 activity lowers RTN4RL1's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.63× higher at baseline in the lines without TLR6 | 0.073 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[KREMEN2]] | B | KREMEN2 activity raises RTN4RL1's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.77× lower at baseline in the lines without KREMEN2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[LINC02006]] | C | LINC02006's natural level weakens RTN4RL1's drug response | LINC02006's natural level across 32 lines (lineage-adjusted; a glimpse) | r -0.79, reverse -0.39; direction clear | 0.064 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTSL4]] | B | RTN4RL1 activity raises ADAMTSL4's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without RTN4RL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[ADGRA2]] | B | RTN4RL1 activity raises ADGRA2's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without RTN4RL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[ADAMTS7]] | B | RTN4RL1 activity raises ADAMTS7's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without RTN4RL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[PRDM6]] | B | RTN4RL1 activity raises PRDM6's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without RTN4RL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[SH3RF3]] | B | RTN4RL1 activity raises SH3RF3's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 3.19× lower at baseline in the lines without RTN4RL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[TSC22D3]] | B | RTN4RL1 activity lowers TSC22D3's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.77× higher at baseline in the lines without RTN4RL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[B3GNT5]] | B | RTN4RL1 activity lowers B3GNT5's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.07× higher at baseline in the lines without RTN4RL1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | RTN4RL1 activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express RTN4RL1 (14) vs lines expressing it (34) | the lines without RTN4RL1: 0.85× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[EFHD1]] | B | RTN4RL1 activity raises EFHD1's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without RTN4RL1 | 0.077 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| cells under [[Afatinib (drug)]] 5 µM | B | RTN4RL1 activity raises the cells' numbers under Afatinib 5 µM (protects the cells) | lines that do not express RTN4RL1 (14) vs lines expressing it (34) | the lines without RTN4RL1: 0.87× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | RTN4RL1 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express RTN4RL1 (14) vs lines expressing it (34) | the lines without RTN4RL1: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[ANXA10]] | B | RTN4RL1 activity lowers ANXA10's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.24× higher at baseline in the lines without RTN4RL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.3, 20.1); signed map (19.3, 30.4). **Vector** length 79.0, 17.0% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +32.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | +4.2 | +21.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.4 | +7.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.2 | +7.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.2 | +7.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.1 | +6.1 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -5.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.4 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Vilanterol (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 4 receptor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,934,677-2,025,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NGRH2, NgR3, DKFZp547J144 |
| Gene groups (HGNC) | Reticulon 4 receptor family |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UN2](https://www.uniprot.org/uniprotkb/Q86UN2) (Reticulon-4 receptor-like 1):

> Cell surface receptor. Plays a functionally redundant role in postnatal brain development and in regulating axon regeneration in the adult central nervous system. Contributes to normal axon migration across the brain midline and normal formation of the corpus callosum. Protects motoneurons against apoptosis; protection against apoptosis is probably mediated by MAG. Plays a role in inhibiting neurite outgrowth and axon regeneration via its binding to neuronal chondroitin sulfate proteoglycans. …

**Summary**, from NCBI Gene [146760](https://www.ncbi.nlm.nih.gov/gene/146760):

> Enables signaling receptor activity. Predicted to be involved in negative regulation of axon regeneration and positive regulation of synapse assembly. Located in cell surface and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21329) · Entrez [146760](https://www.ncbi.nlm.nih.gov/gene/146760) · UniProt [Q86UN2](https://www.uniprot.org/uniprotkb/Q86UN2) · Ensembl [ENSG00000185924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185924)

## Data

Gene col 11754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11754); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11754]; `tensor/DDL_lfc|DDL_z.npy` [11754]; `embed/gene_vectors.npy` [11754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11754 or target_col == 11754). Every well: [[RTN4RL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN4RL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
