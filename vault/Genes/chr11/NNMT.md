---
symbol: "NNMT"
type: "gene"
col: 9349
ensembl_id: "ENSG00000166741"
name: "nicotinamide N-methyltransferase"
location: "11q23.2"
module: 139
arm: "+"
pooled_cpm: 25.97
n_lines_expressing: 26
n_dd_up: 57
n_dd_down: 34
n_dd_up_clean: 53
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# NNMT

*nicotinamide N-methyltransferase* — 11q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 57 drug-doses (4 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 4.14× (z +13.0, q 9e-36, up in 22 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.118× (z -19.6, q 0e+00, down in 24 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA2-SAA4]] (+0.72, fdr 7e-06), [[KLF9]] (+0.70, fdr 7e-06), [[SAA1]] (+0.70, fdr 7e-06); moves opposite to [[MMP1]] (-0.59, fdr 1e-05), [[GALNT12]] (-0.58, fdr 1e-05), [[PKIA]] (-0.57, fdr 2e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC16A7]] → it (grade C ⚠); 6 go from it, the strongest it → [[TNS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 5 with an alert ⚠; shown: the 15 strongest. 57 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **4.14×** | +13.0 | 9e-36 | 22/23 (A549, HS-578T, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **4.03×** | +12.7 | 9e-35 | 20/24 (NCI-H1792, H4, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **3.65×** | +11.8 | 5e-30 | 23/23 (Hs 766T, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **2.47×** | +11.6 | 3e-29 | 21/24 (NCI-H1792, H4, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +11.3 | 1e-27 | 20/24 (A549, H4, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **3.33×** | +11.0 | 4e-26 | 21/24 (Hs 766T, H4, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **3.29×** | +10.9 | 1e-25 | 20/24 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **3.45×** | +10.5 | 8e-24 | 18/22 (A498, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **3.08×** | +10.3 | 6e-23 | 20/24 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **3.06×** | +10.2 | 9e-23 | 16/23 (A549, Hs 766T, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **3.01×** | +10.1 | 4e-22 | 23/24 (A549, A498, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **2.95×** | +9.9 | 2e-21 | 19/24 (A549, HS-578T, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.95×** | +9.5 | 9e-20 | 19/24 (A549, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.79×** | +9.4 | 3e-19 | 17/23 (A549, HS-578T, …) | all doses, flat | position effect removed |
| [[Econazole (drug)]] 5 µM |  | **2.74×** | +9.2 | 1e-18 | 19/24 (A549, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.118×** | -19.6 | 0e+00 | 24/24 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.130×** | -18.7 | 0e+00 | 24/24 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.159×** | -16.9 | 0e+00 | 24/24 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.298×** | -11.1 | 1e-26 | 19/24 (HT-29, NCI-H23, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.430×** | -11.0 | 5e-26 | 21/24 (C32, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.442×** | -7.5 | 5e-12 | 16/22 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.448×** | -7.4 | 1e-11 | 16/24 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -7.2 | 5e-11 | 15/24 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.478×** | -6.8 | 7e-10 | 20/24 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.487×** | -6.6 | 2e-09 | 17/24 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.602×** | -6.6 | 2e-09 | 16/24 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -6.1 | 5e-08 | 15/23 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.517×** | -6.1 | 5e-08 | 16/23 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.553×** | -5.5 | 2e-06 | 16/24 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.561×** | -5.3 | 4e-06 | 14/22 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.687×** | -4.9 | 3e-05 | 12/24 (SHP-77, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 42.8 | 7 (1 ⚠) | 5 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 4.67× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.0549× (z -15.0) |
| [[A-427 (line)]] | wt | 88.9 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0634× (z -24.9) |
| [[Hs 766T (line)]] | wt | 33.8 | 7 | 4 | [[Clobetasol propionate (drug)]] 0.05 µM 6.13× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.135× (z -11.2) |
| [[HS-578T (line)]] | alt | 39.2 | 7 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 8.14× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.0687× (z -13.7) |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 240 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.6) |
| [[SHP-77 (line)]] | alt | 58.0 | 1 | 9 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 4.31× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0501× (z -26.2) |
| [[LOX-IMVI (line)]] | wt | 55.1 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0547× (z -17.4) |
| [[A549 (line)]] | wt | 21.0 | 7 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 13.9× (z +10.7) | [[Belinostat (drug)]] 0.5 µM 0.0909× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0491× (z -19.9) |
| [[A498 (line)]] | wt | 46.7 | 3 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 4.73× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.116× (z -13.8) |
| [[H4 (line)]] | wt | 64.4 | 5 | 1 | [[Triamcinolone (drug)]] 5 µM 4.61× (z +10.2) | [[Ixazomib citrate (drug)]] 5 µM 0.125× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0394× (z -15.6) |
| [[C32 (line)]] | wt | 38.1 | 0 | 5 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.145× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 85.4 | 1 | 4 | [[Clobetasol propionate (drug)]] 0.05 µM 5.80× (z +9.1) | [[Tofacitinib (drug)]] 5 µM 0.217× (z -11.3) |
| [[SNU-423 (line)]] | alt | 57.4 | 1 | 4 | [[Triamcinolone (drug)]] 5 µM 3.30× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.0391× (z -16.7) |
| [[A-172 (line)]] | wt | 15.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 44.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.103× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0852× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.130× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA2-SAA4]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SAA2]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SAA4]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[IL1R1]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CEBPD]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[STOM]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[C1RL]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MT1M]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[BCL6]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP1]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GALNT12]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PKIA]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TMEM158]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[WNT7B]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TNFRSF11A]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[OTUB2]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PTHLH]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GRK5]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[TCP10L]] | -0.52 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[PODXL]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[MANCR]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A7]] | C | SLC16A7 activity raises NNMT's level | lines that do not express SLC16A7 (23) vs lines expressing it (27) | 4.00× lower at baseline in the lines without SLC16A7 | 0.073 | ⚠ within organs, on part of the lines; also absent: NDNF, EDIL3-DT, ZNF229; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS2]] | B | NNMT activity raises TNS2's level | lines that do not express NNMT (24) vs lines expressing it (26) | 1.71× lower at baseline in the lines without NNMT | 0.025 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615 |
| [[PDE4D]] | B | NNMT activity raises PDE4D's level | lines that do not express NNMT (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without NNMT | 0.059 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615 |
| [[SLC16A7]] | C | NNMT activity raises SLC16A7's level | lines that do not express NNMT (24) vs lines expressing it (26) | 3.63× lower at baseline in the lines without NNMT | 0.020 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[TWIST1]] | C | NNMT activity raises TWIST1's level | lines that do not express NNMT (24) vs lines expressing it (26) | 3.69× lower at baseline in the lines without NNMT | 0.031 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[CCBE1]] | C | NNMT activity raises CCBE1's level | lines that do not express NNMT (24) vs lines expressing it (26) | 5.01× lower at baseline in the lines without NNMT | 0.043 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[TBX18]] | C | NNMT activity raises TBX18's level | lines that do not express NNMT (24) vs lines expressing it (26) | 3.37× lower at baseline in the lines without NNMT | 0.088 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, 16.1); signed map (17.1, 29.4). **Vector** length 127, 39.2% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.57 to 6); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.3 | +13.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.7 | +11.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.2 | +11.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.1 | +10.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.9 | -11.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -16.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -19.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -18.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.0 | -6.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.9 | -6.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide N-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.2 — chr11:114,257,787-114,313,536 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 9 pathways, smallest: Metabolism of ingested SeMet, Sec, MeSec into H2Se; Methylation; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P40261](https://www.uniprot.org/uniprotkb/P40261) (Nicotinamide N-methyltransferase):

> Catalyzes the N-methylation of nicotinamide using the universal methyl donor S-adenosyl-L-methionine to form N1-methylnicotinamide and S-adenosyl-L-homocysteine, a predominant nicotinamide/vitamin B3 clearance pathway. Plays a central role in regulating cellular methylation potential, by consuming S-adenosyl-L-methionine and limiting its availability for other methyltransferases. Actively mediates genome-wide epigenetic and transcriptional changes through hypomethylation of repressive chromatin …

**Summary**, from NCBI Gene [4837](https://www.ncbi.nlm.nih.gov/gene/4837):

> N-methylation is one method by which drug and other xenobiotic compounds are metabolized by the liver. This gene encodes the protein responsible for this enzymatic activity which uses S-adenosyl methionine as the methyl donor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7861) · Entrez [4837](https://www.ncbi.nlm.nih.gov/gene/4837) · UniProt [P40261](https://www.uniprot.org/uniprotkb/P40261) · Ensembl [ENSG00000166741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166741)

## Data

Gene col 9349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9349); `tables/drug_effects.parquet` (92 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9349]; `tensor/DDL_lfc|DDL_z.npy` [9349]; `embed/gene_vectors.npy` [9349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9349 or target_col == 9349). Every well: [[NNMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NNMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
