---
symbol: "TPK1"
type: "gene"
col: 12227
ensembl_id: "ENSG00000196511"
name: "thiamin pyrophosphokinase 1"
location: "7q35"
module: 5
arm: "+"
pooled_cpm: 36.51
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TPK1

*thiamin pyrophosphokinase 1* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +7.3, q 1e-10, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.452× (z -11.2, q 2e-26, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIPA1L1]] (+0.61, fdr 1e-05), [[MTHFD2L]] (+0.57, fdr 2e-05), [[PTPRG]] (+0.56, fdr 2e-05); moves opposite to [[GOLGA2]] (-0.50, fdr 5e-05), [[GDPD3]] (-0.50, fdr 3e-05), [[ANKMY2]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KLC4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.3 | 1e-10 | 26/45 (HT-29, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +5.4 | 2e-05 | 28/45 (SW1417, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.63×** | +5.3 | 2e-05 | 31/44 (SHP-77, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.2 | 3e-05 | 23/44 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +4.3 | 0.002 | 19/44 (AsPC-1, NCI-H1792, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.011 | 17/44 (SHP-77, A549, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.020 | 15/45 (A498, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.039 | 18/44 (A549, A498, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.068 | 12/44 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.25× | +3.1 | 0.11 | 12/44 (SHP-77, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.13 | 11/44 (SHP-77, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.452×** | -11.2 | 2e-26 | 31/45 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.485×** | -10.2 | 5e-22 | 35/44 (SHP-77, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.480×** | -10.0 | 4e-21 | 30/45 (NCI-H460, SHP-77, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -9.3 | 3e-18 | 36/45 (A-427, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.642×** | -8.8 | 1e-16 | 26/45 (A-427, SHP-77, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -8.4 | 3e-15 | 29/43 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.553×** | -8.4 | 5e-15 | 32/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.594×** | -7.4 | 1e-11 | 28/44 (NCI-H460, SNU-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -6.6 | 3e-09 | 27/43 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.700×** | -5.0 | 3e-05 | 24/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.706×** | -4.9 | 5e-05 | 24/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.698×** | -4.8 | 8e-05 | 23/44 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.004 | 19/45 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.755×** | -3.8 | 0.006 | 18/42 (SHP-77, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.008 | 14/45 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.704×** | -3.5 | 0.014 | 14/45 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.780×** | -3.4 | 0.023 | 15/45 (PANC-1, A549, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.804×** | -3.0 | 0.084 | 9/44 (RKO, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 142 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.6) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 72.2 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -15.9) |
| [[A-427 (line)]] | wt | 56.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.2) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0344× (z -16.4) |
| [[AN3 CA (line)]] | alt | 655 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0719× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 85.1 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0998× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0414× (z -9.9) |
| [[PANC-1 (line)]] | alt | 27.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.3) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -10.7) |
| [[A-172 (line)]] | wt | 15.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +15.0) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[KATO III (line)]] | alt | 39.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -10.8) |
| [[RKO (line)]] | wt | 73.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -8.5) |
| [[SW480 (line)]] | alt | 30.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -14.4) |
| [[A549 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.3) ⚠ cell-cycle shift, explains ~66% of this change |
| [[H4 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.229× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 9.57 | 0 | 1 | — | [[Oxaliplatin (drug)]] 0.05 µM 0.0844× (z -9.3) |
| [[HT-29 (line)]] | alt | 10.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.48× (z +10.0) | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -8.9) |
| [[LoVo (line)]] | wt | 25.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Panc 03.27 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0274× (z -10.4) |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 14.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +9.0) | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0728× (z -9.3) |
| [[A498 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.36 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.86 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIPA1L1]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MTHFD2L]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 | pathway: Metabolism of vitamins and cofactors |
| [[PTPRG]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SPOPL-DT]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[LDLRAD3]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TANGO6]] | +0.54 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[PRMT3]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PPM1L]] | +0.53 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[GALNT10]] | +0.53 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TMEM164]] | +0.52 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[CMSS1]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EFNA5]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | -0.50 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[GDPD3]] | -0.50 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ANKMY2]] | -0.50 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[LRP1]] | -0.50 | -0.51 / -0.46 | both halves | 2e-05 | pathway: Metabolism of vitamins and cofactors |
| [[FAM114A1]] | -0.48 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[PLCD1]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[TBC1D23]] | -0.47 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[MAPK3]] | -0.46 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TULP3]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[SWI5]] | -0.45 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[MTMR11]] | -0.45 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[CLIP3]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TPK1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLC4]] | C | TPK1 activity lowers KLC4's level | lines that do not express TPK1 (3) vs lines expressing it (47) | 1.66× higher at baseline in the lines without TPK1 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: NMRAL1, CYP2R1, PPP1R26; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (21.4, -8.5); signed map (12.8, 22.1). **Vector** length 85.0, 19.4% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | thiamin pyrophosphokinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q35 — chr7:144,451,941-144,836,395 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HTPK1, PP20 |
| Reactome | 3 pathways, smallest: Vitamin B1 (thiamin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3S4](https://www.uniprot.org/uniprotkb/Q9H3S4) (Thiamine pyrophosphokinase 1):

> Catalyzes the phosphorylation of thiamine to thiamine pyrophosphate (TPP) utilizing UTP and therefore links the biosynthesis of TPP to pyrimidines metabolism. By producing thiamine pyrophosphate, a cofactor of the mitochondrial pyruvate dehydrogenase indirectly regulates pyruvate oxidation and lipogenesis. Although it can also catalyze thiamine phosphorylation using ATP and CTP in vitro, it does so with significantly lower efficiency and without physiological relevance evidence.

**Summary**, from NCBI Gene [27010](https://www.ncbi.nlm.nih.gov/gene/27010):

> The protein encoded by this gene functions as a homodimer and catalyzes the conversion of thiamine to thiamine pyrophosphate, a cofactor for some enzymes of the glycolytic and energy production pathways. Defects in this gene are a cause of thiamine metabolism dysfunction syndrome-5. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:17358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17358) · Entrez [27010](https://www.ncbi.nlm.nih.gov/gene/27010) · UniProt [Q9H3S4](https://www.uniprot.org/uniprotkb/Q9H3S4) · Ensembl [ENSG00000196511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196511)

## Data

Gene col 12227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12227); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12227]; `tensor/DDL_lfc|DDL_z.npy` [12227]; `embed/gene_vectors.npy` [12227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12227 or target_col == 12227). Every well: [[TPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
