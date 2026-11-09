---
symbol: "TRAF3IP1"
type: "gene"
col: 12812
ensembl_id: "ENSG00000204104"
name: "intraflagellar transport 54"
location: "2q37.3"
module: 36
arm: "+"
pooled_cpm: 44.91
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TRAF3IP1

*intraflagellar transport 54* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +16.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.677× (z -12.2, q 1e-31, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEK4]] (+0.71, fdr 7e-06), [[IQCE]] (+0.63, fdr 2e-05), [[HERC2]] (+0.63, fdr 1e-05); moves opposite to [[C14orf119]] (-0.48, fdr 1e-04), [[CHCHD7]] (-0.48, fdr 8e-05), [[CA13]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +16.3 | 0e+00 | 46/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +14.8 | 0e+00 | 46/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +13.6 | 8e-40 | 42/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +13.0 | 3e-36 | 43/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +12.2 | 4e-32 | 45/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.6 | 3e-29 | 38/46 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +10.5 | 5e-24 | 33/45 (KATO III, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +9.3 | 6e-19 | 38/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.43×** | +7.7 | 1e-12 | 28/42 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +7.1 | 7e-11 | 34/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.8 | 4e-07 | 25/48 (HEC-1-A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.3 | 4e-06 | 27/43 (HEC-1-A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +5.3 | 4e-06 | 26/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 7e-05 | 20/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +4.8 | 7e-05 | 21/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.2 | 8e-04 | 17/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.12× | +3.4 | 0.020 | 7/48 (NCI-H1792, J82, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.029 | 8/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.090 | 10/47 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12812.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.677×** | -12.2 | 1e-31 | 42/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.591×** | -11.7 | 5e-29 | 43/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.797×** | -5.0 | 9e-05 | 20/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.688×** | -4.3 | 0.002 | 21/48 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.844× | -3.8 | 0.017 | 19/48 (SNU-1, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -3.7 | 0.017 | 1/49 (AN3 CA) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.5 | 0.040 | 15/48 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.10 | 7/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.868× | -3.2 | 0.10 | 5/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.872× | -3.1 | 0.13 | 18/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 41.5 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.48× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 42.5 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 66.2 | 3 (2 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +14.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 44.8 | 4 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.20× (z +10.2) | [[Tucidinostat (drug)]] 0.5 µM 0.409× (z -11.4) |
| [[A-172 (line)]] | wt | 58.5 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 43.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.83× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 31.2 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 71.5 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.347× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.495× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 34.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 2 (1 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 2.67× (z +9.0) | [[Tucidinostat (drug)]] 5 µM 0.486× (z -9.9) |
| [[RKO (line)]] | wt | 50.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +11.2) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 0.5 µM 0.394× (z -8.5) |
| [[HT-29 (line)]] | alt | 38.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.21× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 43.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 52.8 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.0) ⚠ cell-cycle shift, explains ~93% of this change | [[Tucidinostat (drug)]] 5 µM 0.392× (z -9.8) |
| [[SNU-423 (line)]] | alt | 40.1 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +8.9) | — |
| [[A-427 (line)]] | wt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -17.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 54.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.6) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[A549 (line)]] | wt | 58.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.4) ⚠ cell-cycle shift, explains ~93% of this change | — |
| [[Hs 766T (line)]] | wt | 37.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.32× (z +10.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 49.7 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.448× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 37.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 73.9 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.22× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.110× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK4]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[IQCE]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[HERC2]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[HERC2P9]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[EXT2]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[VPS50]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[NCBP3]] | +0.56 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[VPS13D]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MAPK9]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[GLB1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C14orf119]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[CHCHD7]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[CA13]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ACAP1]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PLEKHA8P1]] | -0.47 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[FAM117A]] | -0.47 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[TMEM60]] | -0.45 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[MIR4300HG]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[PFN1]] | -0.45 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[INTS6L]] | -0.45 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[NBPF19]] | -0.44 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[NBPF10]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.3, -31.3); signed map (-16.6, -51.5). **Vector** length 117, 32.0% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.6 | +13.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +10.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -13.4 | -12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -11.9 | -11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.5 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +2.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:238,320,441-238,400,897 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIP-T3, DKFZP434F124, MIPT3, FAP116, CFAP116; previously TRAF3IP1 |
| Gene groups (HGNC) | IFT-B2 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDR0](https://www.uniprot.org/uniprotkb/Q8TDR0) (Intraflagellar transport protein 54):

> Plays an inhibitory role on IL13 signaling by binding to IL13RA1. Involved in suppression of IL13-induced STAT6 phosphorylation, transcriptional activity and DNA-binding. Recruits TRAF3 and DISC1 to the microtubules. Involved in kidney development and epithelial morphogenesis. Involved in the regulation of microtubule cytoskeleton organization. Is a negative regulator of microtubule stability, acting through the control of MAP4 levels. Involved in ciliogenesis (By similarity).

**Summary**, from NCBI Gene [26146](https://www.ncbi.nlm.nih.gov/gene/26146):

> The protein encoded by this gene interacts with TNF receptor-associated factor 3, tethering it to cytoskeletal microtubules. The encoded protein is also an inhibitor of the innate type I IFN response. Defects in this gene are a cause of Senior-Loken syndrome 9. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:17861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17861) · Entrez [26146](https://www.ncbi.nlm.nih.gov/gene/26146) · UniProt [Q8TDR0](https://www.uniprot.org/uniprotkb/Q8TDR0) · Ensembl [ENSG00000204104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204104)

## Data

Gene col 12812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12812); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12812]; `tensor/DDL_lfc|DDL_z.npy` [12812]; `embed/gene_vectors.npy` [12812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12812 or target_col == 12812). Every well: [[TRAF3IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF3IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
