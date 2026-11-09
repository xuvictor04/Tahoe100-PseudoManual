---
symbol: "ABCF2"
type: "gene"
col: 410
ensembl_id: "ENSG00000033050"
name: "ATP binding cassette subfamily F member 2"
location: "7q36.1"
module: 5
arm: "+"
pooled_cpm: 20.34
n_lines_expressing: 50
n_dd_up: 50
n_dd_down: 4
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ABCF2

*ATP binding cassette subfamily F member 2* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (25 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.57× (z +18.3, q 0e+00, up in 28 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +11.3, q 1e-27, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.809× (z -4.5, q 0.003, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSME3]] (+0.87, fdr 7e-06), [[WDR77]] (+0.83, fdr 7e-06), [[LETM1]] (+0.77, fdr 7e-06); moves opposite to [[SIRT2]] (-0.76, fdr 7e-06), [[KRT10]] (-0.73, fdr 8e-06, ⚠ KRT10 in the vector space only through flagged drug-doses), [[AFTPH]] (-0.72, fdr 7e-06), [[KBTBD3]] (-0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 25 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.57×** | +18.3 | 0e+00 | 28/30 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.38×** | +18.2 | 0e+00 | 40/44 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.68×** | +13.6 | 1e-39 | 33/40 (SW480, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.3 | 1e-27 | 37/47 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +10.7 | 8e-25 | 38/47 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +9.9 | 2e-21 | 40/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +8.9 | 3e-17 | 38/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.86×** | +8.8 | 6e-17 | 31/43 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +8.6 | 6e-16 | 38/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +8.5 | 8e-16 | 38/47 (PANC-1, NCI-H1792, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.9 | 1e-13 | 37/48 (HOP62, A-172, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +7.8 | 4e-13 | 34/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.70×** | +7.7 | 4e-13 | 31/46 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.5 | 3e-12 | 32/48 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.61×** | +6.8 | 4e-10 | 27/46 (NCI-H1792, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +6.7 | 9e-10 | 32/48 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +6.2 | 2e-08 | 28/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.0 | 1e-05 | 22/48 (NCI-H1792, A498, …) | two highest doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +4.7 | 6e-05 | 20/47 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.75×** | +4.3 | 3e-04 | 18/47 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 4e-04 | 20/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -4.5 | 0.003 | 24/48 (A498, CHP-212, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.764×** | -4.1 | 0.014 | 21/47 (KATO III, SW1417, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.046 | 11/47 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.085 | 15/47 (HCT15, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 8.63 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.92× (z +8.7) | [[Docetaxel (drug)]] 0.05 µM 0.172× (z -8.6) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 19.2 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.56× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.0× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 11.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.163× (z -9.4) |
| [[A-427 (line)]] | wt | 29.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -11.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 14.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.89× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 22.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 10.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.33× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.03× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.75× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[WDR77]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[LETM1]] | +0.77 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 | STRING 474 |
| [[MAPKAPK5]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[ANKRD40]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[CCDC86]] | +0.75 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | STRING 479 |
| [[EIF4G1]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 | STRING 475 |
| [[ARMC6]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.73 | +0.76 / +0.75 | both halves | 7e-06 | STRING 649 |
| [[TMEM33]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.76 | -0.70 / -0.72 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | -0.73 | -0.58 / -0.71 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[AFTPH]] | -0.72 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.72 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.71 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[IFI27L2]] | -0.69 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.69 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[MINDY2]] | -0.69 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.68 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.68 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[RNF114]] | -0.68 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | -0.67 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[SEC22A]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity raises ABCF2's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without SLC17A7 | 0.027 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[KCTD15]] | B | KCTD15 activity raises ABCF2's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without KCTD15 | 0.060 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[TPST1]] | B | TPST1 activity raises ABCF2's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without TPST1 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[TOP2A]] | B | TOP2A activity lowers ABCF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.2, -32.4); signed map (-6.9, -43.1). **Vector** length 97.7, 24.5% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 13); *rRNA processing* (reactome, mean cos +0.52 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.6 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.3 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.1 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.8 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily F member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,211,484-151,227,205 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST133090, ABC28, M-ABC1, HUSSY-18 |
| Gene groups (HGNC) | ATP binding cassette subfamily F |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: NFE2L2 regulating MDR associated enzymes; Nuclear events mediated by NFE2L2; KEAP1-NFE2L2 pathway |
| Matched by | ensembl_id |

UniProt [Q9UG63](https://www.uniprot.org/uniprotkb/Q9UG63) carries no function annotation.

**Summary**, from NCBI Gene [10061](https://www.ncbi.nlm.nih.gov/gene/10061):

> This gene encodes a member of the ATP-binding cassette (ABC) transporter superfamily. ATP-binding cassette proteins transport various molecules across extra- and intracellular membranes. Alterations in this gene may be involved in cancer progression. Related pseudogenes have been identified on chromosomes 3 and 7. [provided by RefSeq, Mar 2019]

**Accessions** — [HGNC:71](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:71) · Entrez [10061](https://www.ncbi.nlm.nih.gov/gene/10061) · UniProt [Q9UG63](https://www.uniprot.org/uniprotkb/Q9UG63) · Ensembl [ENSG00000033050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033050)

## Data

Gene col 410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 410); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 410]; `tensor/DDL_lfc|DDL_z.npy` [410]; `embed/gene_vectors.npy` [410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 410 or target_col == 410). Every well: [[ABCF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
