---
symbol: "ST6GALNAC3"
type: "gene"
col: 11480
ensembl_id: "ENSG00000184005"
name: "ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 3"
location: "1p31.1"
module: 82
arm: "+"
pooled_cpm: 18.5
n_lines_expressing: 32
n_dd_up: 32
n_dd_down: 13
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# ST6GALNAC3

*ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 3* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.91× (z +24.5, q 0e+00, up in 28 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -9.8, q 7e-20, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM108]] (+0.69, fdr 1e-05), [[MMP16]] (+0.61, fdr 1e-05), [[GNAO1]] (+0.60, fdr 1e-05); moves opposite to [[EMP3]] (-0.49, fdr 1e-04), [[TBC1D22B]] (-0.47, fdr 9e-04, ⚠ not reproduced), [[CYLD]] (-0.46, fdr 5e-04), [[SYNRG]] (-0.45, fdr 5e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGAP20]] → it (grade B ⚠); 6 go from it, the strongest it → [[ADD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.91×** | +24.5 | 0e+00 | 28/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.95×** | +23.0 | 0e+00 | 28/30 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.27×** | +21.7 | 0e+00 | 27/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.95×** | +21.1 | 0e+00 | 27/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.37×** | +14.4 | 8e-45 | 26/29 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.04×** | +11.4 | 6e-28 | 27/30 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **5.53×** | +10.6 | 3e-24 | 25/29 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +10.4 | 1e-23 | 10/28 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.97×** | +8.0 | 8e-14 | 18/28 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.71×** | +6.2 | 4e-08 | 10/21 (A498, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +4.8 | 8e-05 | 19/29 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 9e-05 | 13/28 (Hs 766T, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 15/29 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 10/28 (SHP-77, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 9e-04 | 12/28 (SW 900, LOX-IMVI, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.62×** | +3.9 | 0.003 | 7/29 (Hs 766T, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.015 | 10/30 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11480.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -9.8 | 7e-20 | 25/30 (C-33 A, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.497×** | -8.3 | 4e-14 | 20/28 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.503×** | -7.8 | 1e-12 | 21/28 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -7.4 | 2e-11 | 26/29 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -6.7 | 3e-09 | 20/27 (C-33 A, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -5.0 | 5e-05 | 21/29 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.672×** | -4.7 | 2e-04 | 13/28 (C32, CHP-212, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -4.2 | 0.002 | 15/29 (C-33 A, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.608×** | -4.1 | 0.003 | 9/29 (H4, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.008 | 6/29 (LS 180, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.022 | 14/30 (C32, CHP-212, …) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.046 | 5/30 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -3.2 | 0.069 | 15/29 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 331 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0517× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -10.1) |
| [[C32 (line)]] | wt | 369 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 14.4 | 5 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.23× (z +14.3) | [[Harringtonine (drug)]] 0.5 µM 0.108× (z -12.3) |
| [[C-33 A (line)]] | alt | 117 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0409× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 19.3 | 5 | 1 | [[Tucidinostat (drug)]] 5 µM 4.35× (z +12.5) | [[Ixazomib citrate (drug)]] 5 µM 0.222× (z -9.1) |
| [[PANC-1 (line)]] | alt | 5.57 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 21.1× (z +14.8) | [[Digitoxin (drug)]] 0.5 µM 0.145× (z -9.5) |
| [[SHP-77 (line)]] | alt | 13.4 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 8.62× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.0769× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 6.26 | 4 | 1 | [[Tucidinostat (drug)]] 5 µM 10.4× (z +12.3) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0846× (z -9.2) |
| [[LoVo (line)]] | wt | 5.06 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.1× (z +19.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 11.0× (z +13.3) | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 4 | 1 | [[Tucidinostat (drug)]] 5 µM 8.31× (z +12.9) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.121× (z -9.1) |
| [[A498 (line)]] | wt | 15.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.51× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.0699× (z -18.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 13.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.8× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.47× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 14.4 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 6.50× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 8.39× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 47.7 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.63× (z +9.1) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.198× (z -8.6) |
| [[SW 900 (line)]] | alt | 25.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.67× (z +9.1) | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0880× (z -9.6) |
| [[A-172 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM108]] | +0.69 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[MMP16]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[GNAO1]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ATRNL1]] | +0.59 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GHR]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[LHX6]] | +0.58 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[CTNNA2]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TEX15]] | +0.55 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SNCA]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[LPAR3]] | +0.53 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[OCA2]] | +0.53 | +0.29 / +0.55 | both halves | 3e-04 |  |
| [[TENM1]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMP3]] | -0.49 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[TBC1D22B]] | -0.47 | -0.19 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[CYLD]] | -0.46 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[RABL2B]] | -0.45 | -0.08 / -0.44 | ⚠ not reproduced | 0.003 |  |
| [[SYNRG]] | -0.45 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[CCDC90B]] | -0.45 | -0.12 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[APOBEC3F]] | -0.45 | -0.20 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[RNF146]] | -0.44 | -0.13 / -0.39 | ⚠ not reproduced | 0.002 |  |
| [[RC3H2]] | -0.44 | -0.09 / -0.46 | ⚠ not reproduced | 0.003 |  |
| [[FBXW4]] | -0.44 | -0.12 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[DDX59]] | -0.44 | -0.23 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP20]] | B | ARHGAP20 activity raises ST6GALNAC3's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 3.63× lower at baseline in the lines without ARHGAP20 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC |
| [[TRIM9]] | C | TRIM9 activity raises ST6GALNAC3's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 3.56× lower at baseline in the lines without TRIM9 | 0.076 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[GHR]] | C | GHR activity raises ST6GALNAC3's level | lines that do not express GHR (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without GHR | 0.084 | ⚠ within organs, on part of the lines; also absent: FAP, LHX2, ADCY1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD2]] | B | ST6GALNAC3 activity raises ADD2's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 3.38× lower at baseline in the lines without ST6GALNAC3 | 0.097 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent |
| [[MMP16]] | C | ST6GALNAC3 activity raises MMP16's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 4.63× lower at baseline in the lines without ST6GALNAC3 | 0.046 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[B3GALT1]] | C | ST6GALNAC3 activity raises B3GALT1's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 2.55× lower at baseline in the lines without ST6GALNAC3 | 0.050 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[GHR]] | C | ST6GALNAC3 activity raises GHR's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 3.88× lower at baseline in the lines without ST6GALNAC3 | 0.068 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[ATRNL1]] | C | ST6GALNAC3 activity raises ATRNL1's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 3.49× lower at baseline in the lines without ST6GALNAC3 | 0.081 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[TRIM9]] | C | ST6GALNAC3 activity raises TRIM9's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 4.45× lower at baseline in the lines without ST6GALNAC3 | 0.084 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.6, 29.9); signed map (36.4, 33.2). **Vector** length 69.2, 15.2% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +23.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +5.1 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +4.7 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -8.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.8 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | +0.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:76,074,746-76,634,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIAT7C |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 17 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Termination of O-glycan biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDV1](https://www.uniprot.org/uniprotkb/Q8NDV1) (Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 3):

> Transfers the sialyl group (N-acetyl-alpha-neuraminyl or NeuAc) from CMP-NeuAc to the GalNAc residue on the NeuAc-alpha-2,3-Gal-beta-1,3-GalNAc sequence of glycoproteins and glycolipids forming an alpha-2,6-linkage. Produces branched type disialyl structures by transfer of a sialyl group onto a GalNAc residue inside the backbone core chains. ST6GalNAcIII prefers glycolipids to glycoproteins, predominantly catalyzing the biosynthesis of ganglioside GD1alpha from GM1b. GD1alpha is a critical …

**Summary**, from NCBI Gene [256435](https://www.ncbi.nlm.nih.gov/gene/256435):

> ST6GALNAC3 belongs to a family of sialyltransferases that transfer sialic acids from CMP-sialic acid to terminal positions of carbohydrate groups in glycoproteins and glycolipids (Lee et al., 1999 [PubMed 10207017]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19343) · Entrez [256435](https://www.ncbi.nlm.nih.gov/gene/256435) · UniProt [Q8NDV1](https://www.uniprot.org/uniprotkb/Q8NDV1) · Ensembl [ENSG00000184005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184005)

## Data

Gene col 11480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11480); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11480]; `tensor/DDL_lfc|DDL_z.npy` [11480]; `embed/gene_vectors.npy` [11480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11480 or target_col == 11480). Every well: [[ST6GALNAC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
