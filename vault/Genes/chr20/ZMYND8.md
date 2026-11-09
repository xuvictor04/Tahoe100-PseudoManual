---
symbol: "ZMYND8"
type: "gene"
col: 2062
ensembl_id: "ENSG00000101040"
name: "zinc finger MYND-type containing 8"
location: "20q13.12"
module: 113
arm: "+"
pooled_cpm: 365.13
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 51
n_dd_up_clean: 19
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ZMYND8

*zinc finger MYND-type containing 8* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (none with an alert); the strongest is [[Budesonide (drug)]] 0.5 µM: 1.50× (z +8.0, q 9e-13, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.149× (z -37.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.72, fdr 7e-06), [[KLF9]] (+0.71, fdr 7e-06), [[MT1E]] (+0.71, fdr 7e-06); moves opposite to [[IGFN1]] (-0.53, fdr 4e-05), [[SIRLNT]] (-0.52, fdr 4e-05), [[SLAMF7]] (-0.51, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAFB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 3 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.5 µM |  | **1.50×** | +8.0 | 9e-13 | 30/47 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.49×** | +7.9 | 1e-12 | 31/47 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +7.1 | 3e-10 | 34/47 (A-172, LOX-IMVI, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 2e-07 | 30/47 (A-172, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.36×** | +6.0 | 2e-07 | 27/47 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.33×** | +5.6 | 2e-06 | 26/47 (A-172, H4, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.5 | 3e-06 | 29/47 (A-172, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.31×** | +5.2 | 1e-05 | 26/47 (Hs 766T, LOX-IMVI, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 2e-05 | 28/47 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +5.0 | 4e-05 | 23/47 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.30×** | +4.9 | 4e-05 | 26/48 (A-172, SK-MEL-2, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 2e-04 | 24/49 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 27/47 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 6e-04 | 25/46 (A-172, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.24×** | +4.3 | 6e-04 | 26/47 (A-172, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.149×** | -37.1 | 0e+00 | 47/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.264×** | -36.7 | 0e+00 | 43/47 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.190×** | -32.4 | 0e+00 | 47/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.241×** | -27.8 | 0e+00 | 47/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.314×** | -22.6 | 0e+00 | 47/47 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.325×** | -21.9 | 0e+00 | 47/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.452×** | -21.9 | 0e+00 | 42/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.341×** | -20.1 | 0e+00 | 42/47 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.351×** | -19.6 | 0e+00 | 42/46 (HepG2/C3A, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.370×** | -19.4 | 0e+00 | 46/47 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.359×** | -19.2 | 0e+00 | 38/43 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.386×** | -18.5 | 0e+00 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.395×** | -16.7 | 0e+00 | 41/44 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.425×** | -16.0 | 0e+00 | 44/46 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.456×** | -15.3 | 0e+00 | 38/47 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.486×** | -14.0 | 3e-43 | 44/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.676×** | -10.8 | 2e-25 | 39/47 (NCI-H1573, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.578×** | -10.7 | 4e-25 | 36/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.649×** | -8.4 | 1e-15 | 35/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.452×** | -8.1 | 2e-14 | 41/47 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -7.5 | 2e-12 | 35/47 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 385 | 17 | 20 (7 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.36× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -36.2) |
| [[A-172 (line)]] | wt | 325 | 17 | 16 (7 ⚠) | [[Budesonide (drug)]] 0.5 µM 3.17× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.144× (z -25.5) |
| [[Hs 766T (line)]] | wt | 450 | 18 | 15 (7 ⚠) | [[Budesonide (drug)]] 0.5 µM 3.40× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -23.2) |
| [[H4 (line)]] | wt | 256 | 7 | 23 (8 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.92× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -22.8) |
| [[RPMI-7951 (line)]] | alt | 526 | 7 | 23 (9 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.47× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -34.2) |
| [[SNU-423 (line)]] | alt | 670 | 7 | 23 (9 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.50× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -30.6) |
| [[HOP62 (line)]] | alt | 396 | 8 | 20 (8 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.35× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.0829× (z -28.2) |
| [[MIA PaCa-2 (line)]] | alt | 695 | 0 | 28 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -49.0) |
| [[HS-578T (line)]] | alt | 193 | 12 | 14 (4 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.98× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.131× (z -19.7) |
| [[LOX-IMVI (line)]] | wt | 199 | 17 | 9 (3 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.96× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.187× (z -20.5) |
| [[NCI-H1573 (line)]] | alt | 561 | 0 | 26 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -49.2) |
| [[NCI-H23 (line)]] | alt | 304 | 0 | 26 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -30.9) |
| [[PANC-1 (line)]] | alt | 279 | 0 | 24 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -39.0) |
| [[BT-474 (line)]] | alt | 2,113 | 0 | 23 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -21.1) |
| [[NCI-H460 (line)]] | wt | 240 | 0 | 23 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -33.3) |
| [[SW 900 (line)]] | alt | 339 | 0 | 23 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -33.5) |
| [[C32 (line)]] | wt | 664 | 1 | 21 (10 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.83× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -50.4) |
| [[J82 (line)]] | alt | 316 | 1 | 20 (10 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 1.82× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.124× (z -29.9) |
| [[NCI-H1792 (line)]] | alt | 548 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0475× (z -49.1) |
| [[SW480 (line)]] | alt | 466 | 0 | 20 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0998× (z -42.6) |
| [[CFPAC-1 (line)]] | alt | 315 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -23.7) |
| [[COLO 205 (line)]] | alt | 1,427 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0523× (z -51.0) |
| [[SNU-1 (line)]] | wt | 479 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.5) |
| [[A549 (line)]] | wt | 280 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -26.0) |
| [[HepG2_C3A (line)]] | wt | 751 | 0 | 17 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -32.4) |
| [[NCI-H2030 (line)]] | alt | 310 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -33.9) |
| [[HT-29 (line)]] | alt | 368 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0993× (z -31.2) |
| [[KATO III (line)]] | alt | 286 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -25.1) |
| [[SHP-77 (line)]] | alt | 231 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -26.3) |
| [[AsPC-1 (line)]] | alt | 321 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -30.8) |
| [[SW1417 (line)]] | alt | 416 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -26.0) |
| [[LS 180 (line)]] | wt | 198 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -26.3) |
| [[A498 (line)]] | wt | 248 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -25.0) |
| [[LoVo (line)]] | wt | 151 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -27.1) |
| [[RKO (line)]] | wt | 121 | 0 | 11 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.227× (z -15.5) |
| [[C-33 A (line)]] | alt | 279 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -22.7) |
| [[SW 1271 (line)]] | alt | 500 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 183 | 1 | 6 (2 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.21× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.178× (z -18.9) |
| [[SW 1088 (line)]] | alt | 452 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -12.9) |
| [[AN3 CA (line)]] | alt | 260 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.7) |
| [[hTERT-HPNE (line)]] | wt | 165 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -21.0) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -17.4) |
| [[CHP-212 (line)]] | wt | 130 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.196× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 190 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -23.3) |
| [[SW48 (line)]] | wt | 115 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -14.9) |
| [[HCT15 (line)]] | alt | 192 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.456× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -9.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 77.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 406 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 363 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[KLF9]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MT1E]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[IRX3]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[ITGA10]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[MT2A]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ID1]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[HS3ST3B1]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[TLR2]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PIK3R1]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFN1]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SIRLNT]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SLAMF7]] | -0.51 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[IRGQ]] | -0.50 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[C5orf46]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SHISAL1]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[PSG9]] | -0.45 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[FGF5]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFB]] | B | MAFB activity raises ZMYND8's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without MAFB | 0.008 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[MAOA]] | B | MAOA activity raises ZMYND8's level | lines that do not express MAOA (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without MAOA | 0.018 | ⚠ within organs, on part of the lines; also absent: OAS1, CKB; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises ZMYND8's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises ZMYND8's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.72× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[SAA2]] | B | SAA2 activity raises ZMYND8's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without SAA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[TBC1D8]] | B | TBC1D8 activity raises ZMYND8's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without TBC1D8 | 0.094 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 14.3); signed map (15.7, 31.0). **Vector** length 106, 43.3% of its response variance represented; |z| ≥ 3 in 2,600 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.53 to 11); *Metallothioneins bind metals* (reactome, mean cos +0.64 to 5); *metallothionein* (control, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.5 µM |  | +7.2 | +8.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.1 | +7.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +7.0 | +4.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +6.9 | +5.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +6.9 | +6.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.6 | -12.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.3 | -10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.9 | -19.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.1 | -18.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.2 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -6.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYND-type containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:47,209,214-47,356,889 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RACK7, KIAA1125; previously PRKCBP1 |
| Gene groups (HGNC) | Zinc fingers MYND-type; PHD finger proteins; PWWP domain containing; Bromodomain containing |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULU4](https://www.uniprot.org/uniprotkb/Q9ULU4) (MYND-type zinc finger-containing chromatin reader ZMYND8):

> Chromatin reader that recognizes dual histone modifications such as histone H3.1 dimethylated at 'Lys-36' and histone H4 acetylated at 'Lys-16' (H3.1K36me2-H4K16ac) and histone H3 methylated at 'Lys-4' and histone H4 acetylated at 'Lys-14' (H3K4me1-H3K14ac). May act as a transcriptional corepressor for KDM5D by recognizing the dual histone signature H3K4me1-H3K14ac. May also act as a transcriptional corepressor for KDM5C and EZH2. Recognizes acetylated histone H4 and recruits the NuRD chromatin …

**Summary**, from NCBI Gene [23613](https://www.ncbi.nlm.nih.gov/gene/23613):

> The protein encoded by this gene is a receptor for activated C-kinase (RACK) protein. The encoded protein has been shown to bind in vitro to activated protein kinase C beta I. In addition, this protein is a cutaneous T-cell lymphoma-associated antigen. Finally, the protein contains a bromodomain and two zinc fingers, and is thought to be a transcriptional regulator. Multiple transcript variants encoding several different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9397) · Entrez [23613](https://www.ncbi.nlm.nih.gov/gene/23613) · UniProt [Q9ULU4](https://www.uniprot.org/uniprotkb/Q9ULU4) · Ensembl [ENSG00000101040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101040)

## Data

Gene col 2062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2062); `tables/drug_effects.parquet` (99 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2062]; `tensor/DDL_lfc|DDL_z.npy` [2062]; `embed/gene_vectors.npy` [2062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2062 or target_col == 2062). Every well: [[ZMYND8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYND8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
