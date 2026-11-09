---
symbol: "ENPP1"
type: "gene"
col: 12428
ensembl_id: "ENSG00000197594"
name: "ectonucleotide pyrophosphatase/phosphodiesterase 1"
location: "6q23.2"
module: 142
arm: "+"
pooled_cpm: 15.77
n_lines_expressing: 39
n_dd_up: 35
n_dd_down: 11
n_dd_up_clean: 25
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# ENPP1

*ectonucleotide pyrophosphatase/phosphodiesterase 1* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.63× (z +23.2, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.580× (z -6.6, q 2e-08, down in 20 of 34 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIMA1]] (+0.60, fdr 1e-05), [[AMOT]] (+0.57, fdr 3e-05), [[CXADR]] (+0.55, fdr 3e-04); moves opposite to [[GID4]] (-0.61, fdr 1e-05), [[RILPL1]] (-0.59, fdr 1e-05), [[PAM16]] (-0.57, fdr 3e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC01117]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.63×** | +23.2 | 0e+00 | 36/37 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.44×** | +22.2 | 0e+00 | 31/36 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.07×** | +17.9 | 0e+00 | 34/36 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.99×** | +17.6 | 0e+00 | 33/36 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.50×** | +15.9 | 0e+00 | 24/27 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.40×** | +15.0 | 0e+00 | 14/18 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.90×** | +13.5 | 6e-40 | 32/36 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.80×** | +13.1 | 3e-37 | 30/36 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +12.0 | 2e-31 | 16/23 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.50×** | +11.7 | 1e-29 | 30/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +10.2 | 1e-22 | 24/35 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +9.1 | 5e-18 | 21/36 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.90×** | +7.1 | 6e-11 | 21/37 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.44×** | +6.5 | 4e-09 | 14/36 (SW480, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +5.8 | 2e-07 | 17/35 (SNU-423, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +5.2 | 7e-06 | 15/35 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 1e-04 | 11/37 (HepG2/C3A, SW480, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 9/37 (A-172, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.001 | 13/37 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 13/37 (NCI-H1792, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.580×** | -6.6 | 2e-08 | 20/34 (HOP62, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -6.1 | 4e-07 | 21/36 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -5.5 | 8e-06 | 13/33 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -5.4 | 1e-05 | 16/36 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -5.3 | 1e-05 | 16/36 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -5.1 | 3e-05 | 17/36 (BT-474, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -4.4 | 1e-03 | 12/36 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.801×** | -4.1 | 0.004 | 11/37 (AsPC-1, RPMI-7951, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.013 | 7/37 (RKO, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.058 | 13/37 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.778×** | -3.2 | 0.058 | 11/35 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.058 | 7/36 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.846× | -3.1 | 0.089 | 3/36 (SW 900, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.54 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.73× (z +13.3) | — |
| [[A-172 (line)]] | wt | 7.05 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 8.34 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +10.2) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0864× (z -12.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 5.35 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +12.4) | — |
| [[LoVo (line)]] | wt | 13.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +12.4) | — |
| [[A-427 (line)]] | wt | 10.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.02× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.52× (z +9.9) | — |
| [[SW480 (line)]] | alt | 5.31 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +13.3) | — |
| [[A498 (line)]] | wt | 12.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 54.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +14.8) | [[Ixazomib citrate (drug)]] 0.5 µM 0.263× (z -8.6) |
| [[HOP62 (line)]] | alt | 141 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 8.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +8.5) | — |
| [[C32 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 4.42 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.19× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 6.16 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.18× (z +11.2) | — |
| [[J82 (line)]] | alt | 5.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.12× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 9.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 6.01 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +12.7) | — |
| [[A549 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMA1]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[AMOT]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CXADR]] | +0.55 | +0.26 / +0.62 | both halves | 3e-04 |  |
| [[SEMA3C]] | +0.55 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[TAGLN2]] | +0.54 | +0.37 / +0.41 | both halves | 7e-05 |  |
| [[CCDC148]] | +0.54 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[COL5A3]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MYLK]] | +0.54 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[ITGAV]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ALCAM]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[PDLIM3]] | +0.53 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[PLCE1]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GID4]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RILPL1]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PAM16]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZNF500]] | -0.57 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[DRD4]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[IL17RA]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TRMT44]] | -0.55 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[AGAP4]] | -0.54 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TUSC2]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ARMC10]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ENPP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DAPK2]] | B | DAPK2 activity lowers ENPP1's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 1.77× higher at baseline in the lines without DAPK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises ENPP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01117]] | B | ENPP1 activity raises LINC01117's level | lines that do not express ENPP1 (11) vs lines expressing it (39) | 2.25× lower at baseline in the lines without ENPP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: MEIS3, EPHB1, MCTP1; maybe low, not absent |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | B | ENPP1 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express ENPP1 (11) vs lines expressing it (37) | the lines without ENPP1: 0.87× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: MEIS3, EPHB1, MCTP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction -0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 9.2); signed map (48.7, 5.3). **Vector** length 77.8, 15.8% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +23.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +7.1 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +13.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +4.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.6 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleotide pyrophosphatase/phosphodiesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:131,808,016-131,895,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC-1, PCA1; previously NPPS, M6S1, PDNP1 |
| Gene groups (HGNC) | Ectonucleotide pyrophosphatase/phosphodiesterase family |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 4 pathways, smallest: Vitamin B2 (riboflavin) metabolism; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P22413](https://www.uniprot.org/uniprotkb/P22413) (Ectonucleotide pyrophosphatase/phosphodiesterase family member 1):

> Nucleotide pyrophosphatase that generates diphosphate (PPi) and functions in bone mineralization and soft tissue calcification by regulating pyrophosphate levels (By similarity). PPi inhibits bone mineralization and soft tissue calcification by binding to nascent hydroxyapatite crystals, thereby preventing further growth of these crystals. Preferentially hydrolyzes ATP, but can also hydrolyze other nucleoside 5' triphosphates such as GTP, CTP and UTP to their corresponding monophosphates with …

**Summary**, from NCBI Gene [5167](https://www.ncbi.nlm.nih.gov/gene/5167):

> This gene is a member of the ecto-nucleotide pyrophosphatase/phosphodiesterase (ENPP) family. The encoded protein is a type II transmembrane glycoprotein comprising two identical disulfide-bonded subunits. This protein has broad specificity and cleaves a variety of substrates, including phosphodiester bonds of nucleotides and nucleotide sugars and pyrophosphate bonds of nucleotides and nucleotide sugars. This protein may function to hydrolyze nucleoside 5' triphosphates to their corresponding …

**Accessions** — [HGNC:3356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3356) · Entrez [5167](https://www.ncbi.nlm.nih.gov/gene/5167) · UniProt [P22413](https://www.uniprot.org/uniprotkb/P22413) · Ensembl [ENSG00000197594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197594)

## Data

Gene col 12428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12428); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12428]; `tensor/DDL_lfc|DDL_z.npy` [12428]; `embed/gene_vectors.npy` [12428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12428 or target_col == 12428). Every well: [[ENPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
