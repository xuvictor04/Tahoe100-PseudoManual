---
symbol: "DNMT3B"
type: "gene"
col: 1527
ensembl_id: "ENSG00000088305"
name: "DNA methyltransferase 3 beta"
location: "20q11.21"
module: 82
arm: "+"
pooled_cpm: 12.97
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 19
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# DNMT3B

*DNA methyltransferase 3 beta* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.40× (z +13.9, q 3e-41, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -9.3, q 8e-18, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS3]] (+0.70, fdr 1e-05), [[NEURL1B]] (+0.67, fdr 7e-06), [[TSPAN33]] (+0.67, fdr 3e-05); moves opposite to [[AEBP2]] (-0.67, fdr 3e-05), [[MCPH1]] (-0.65, fdr 3e-05), [[EFCAB6]] (-0.64, fdr 3e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 19 go from it, the strongest it → [[SLC29A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +13.9 | 3e-41 | 38/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +13.4 | 1e-38 | 35/43 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +13.1 | 4e-37 | 32/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +10.5 | 2e-23 | 32/44 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +9.3 | 3e-18 | 25/43 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +7.1 | 2e-10 | 19/42 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +6.1 | 8e-08 | 19/43 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 1e-06 | 15/41 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +3.6 | 0.019 | 11/43 (LoVo, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.020 | 5/42 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +3.5 | 0.020 | 9/43 (A498, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +3.5 | 0.021 | 11/43 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.23×** | +3.2 | 0.051 | 5/41 (SW480, CFPAC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +3.1 | 0.078 | 9/43 (HOP62, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -9.3 | 8e-18 | 31/43 (SNU-423, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -8.4 | 1e-14 | 31/42 (SW480, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -7.9 | 4e-13 | 20/26 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -7.7 | 2e-12 | 26/42 (NCI-H2347, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -7.6 | 4e-12 | 24/41 (LoVo, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.659×** | -6.6 | 5e-09 | 22/43 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.663×** | -6.5 | 8e-09 | 20/34 (HepG2/C3A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -5.8 | 5e-07 | 18/40 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -5.6 | 2e-06 | 21/41 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.703×** | -5.5 | 2e-06 | 22/43 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -4.5 | 3e-04 | 19/44 (A-427, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.002 | 17/41 (SW48, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.775×** | -4.0 | 0.003 | 17/41 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.777×** | -4.0 | 0.003 | 9/43 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.005 | 17/41 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.796×** | -3.4 | 0.021 | 6/41 (RKO, SHP-77, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.799×** | -3.4 | 0.024 | 8/43 (NCI-H2347, A-172, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.810×** | -3.3 | 0.031 | 10/41 (Hs 766T, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 28.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.5) |
| [[SNU-1 (line)]] | wt | 48.8 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -13.9) |
| [[A-427 (line)]] | wt | 22.6 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.343× (z -10.4) |
| [[A498 (line)]] | wt | 40.7 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.92× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.37 | 1 | 2 | [[Auranofin (drug)]] 5 µM 5.29× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0537× (z -16.7) |
| [[PANC-1 (line)]] | alt | 8.02 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 3.96 | 0 | 2 (1 ⚠) | — | [[Pemigatinib (drug)]] 0.05 µM 0.122× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.4) |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -16.8) |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0837× (z -11.5) |
| [[HCT15 (line)]] | alt | 8.50 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0827× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0716× (z -11.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 8.34 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.307× (z -9.4) |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.9) |
| [[J82 (line)]] | alt | 16.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -12.0) |
| [[KATO III (line)]] | alt | 8.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -10.1) |
| [[SW480 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | +0.70 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NEURL1B]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TSPAN33]] | +0.67 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[GALNT12]] | +0.66 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PIP4K2A]] | +0.65 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PBX4]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CBX2]] | +0.64 | +0.49 / +0.56 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[LDLRAP1]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CEP131]] | +0.64 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[CAMK2G]] | +0.64 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[GPRIN1]] | +0.63 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AEBP2]] | -0.67 | -0.56 / -0.44 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression; STRING 589 |
| [[MCPH1]] | -0.65 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[EFCAB6]] | -0.64 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.63 | -0.53 / -0.26 | both halves | 3e-04 |  |
| [[INO80D]] | -0.62 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MCTS1]] | -0.62 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[HCG17]] | -0.62 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[GGPS1]] | -0.61 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[UBE3B]] | -0.61 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[TBCE-1]] | -0.61 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CHD1-DT]] | -0.61 | -0.55 / -0.24 | both halves | 5e-04 |  |
| [[PKN2-AS1]] | -0.61 | -0.52 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DNMT3B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MPP2]] | B | MPP2 activity raises DNMT3B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.20× lower at baseline in the lines without MPP2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[DAGLA]] | C | DAGLA activity raises DNMT3B's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without DAGLA | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises DNMT3B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 3.99× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC29A1]] | C | DNMT3B activity raises SLC29A1's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 3.16× lower at baseline in the lines without DNMT3B | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[ANKRD36C]] | C | DNMT3B activity raises ANKRD36C's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without DNMT3B | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[INPP5F]] | C | DNMT3B activity raises INPP5F's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without DNMT3B | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| cells under [[MK-3903 (drug)]] 5 µM | C | DNMT3B activity raises the cells' numbers under MK-3903 5 µM (protects the cells) | lines that do not express DNMT3B (4) vs lines expressing it (44) | the lines without DNMT3B: 0.67× the cells of the other lines | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[SCAI]] | C | DNMT3B activity raises SCAI's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without DNMT3B | 0.051 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[MIIP]] | C | DNMT3B activity raises MIIP's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without DNMT3B | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[GNA12]] | C | DNMT3B activity raises GNA12's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without DNMT3B | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[LINC00571]] | C | DNMT3B activity lowers LINC00571's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 2.35× higher at baseline in the lines without DNMT3B | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[CCDC134]] | C | DNMT3B activity raises CCDC134's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without DNMT3B | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[MAST2]] | C | DNMT3B activity raises MAST2's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.58× lower at baseline in the lines without DNMT3B | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[BRF1]] | C | DNMT3B activity raises BRF1's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without DNMT3B | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[VASH2]] | C | DNMT3B activity raises VASH2's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without DNMT3B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.6, 5.8); signed map (-40.3, -6.9). **Vector** length 94.8, 20.1% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +13.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +13.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +10.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DNA methyltransferase 3 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,762,385-32,809,359 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PWWP domain containing; 7BS C5-cytosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 10 pathways, smallest: SUMOylation of DNA methylation proteins; DNA methylation; Defective pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBC3](https://www.uniprot.org/uniprotkb/Q9UBC3) (DNA):

> DNA (cytosine-5)-methyltransferase that mediates genome-wide de novo methylation and which is essential for the establishment of DNA methylation patterns during development. Modifies DNA at CpG sites with selectivity for residues flanking the target CpG site at positions -1 and +1, and strong preference for a guanine (G) immediately following the CpG sites. Methylates DNA in a non-cooperative processive manner, allowing the enzyme to diffuse along DNA and methylate multiple sites before …

**Summary**, from NCBI Gene [1789](https://www.ncbi.nlm.nih.gov/gene/1789):

> CpG methylation is an epigenetic modification that is important for embryonic development, imprinting, and X-chromosome inactivation. Studies in mice have demonstrated that DNA methylation is required for mammalian development. This gene encodes a DNA methyltransferase which is thought to function in de novo methylation, rather than maintenance methylation. The protein localizes primarily to the nucleus and its expression is developmentally regulated. Mutations in this gene cause the …

**Accessions** — [HGNC:2979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2979) · Entrez [1789](https://www.ncbi.nlm.nih.gov/gene/1789) · UniProt [Q9UBC3](https://www.uniprot.org/uniprotkb/Q9UBC3) · Ensembl [ENSG00000088305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088305)

## Data

Gene col 1527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1527); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1527]; `tensor/DDL_lfc|DDL_z.npy` [1527]; `embed/gene_vectors.npy` [1527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1527 or target_col == 1527). Every well: [[DNMT3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNMT3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
