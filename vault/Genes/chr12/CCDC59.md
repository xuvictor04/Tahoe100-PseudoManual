---
symbol: "CCDC59"
type: "gene"
col: 5473
ensembl_id: "ENSG00000133773"
name: "coiled-coil domain containing 59"
location: "12q21.31"
module: 23
arm: "+"
pooled_cpm: 40.51
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CCDC59

*coiled-coil domain containing 59* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.60× (z +16.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.753× (z -5.1, q 2e-04, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP2L2]] (+0.78, fdr 7e-06), [[THAP2]] (+0.74, fdr 1e-05), [[ATE1OSP]] (+0.73, fdr 1e-05); moves opposite to [[PARP1]] (-0.66, fdr 3e-05), [[CORO1C]] (-0.66, fdr 1e-05), [[MED14]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.60×** | +16.4 | 0e+00 | 44/48 (HT-29, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +10.3 | 3e-22 | 45/47 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.75×** | +10.1 | 1e-21 | 44/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.7 | 6e-16 | 39/48 (BT-474, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.87×** | +7.7 | 1e-12 | 40/48 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.5 | 7e-09 | 35/47 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.66×** | +6.5 | 8e-09 | 39/48 (LoVo, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +6.0 | 2e-07 | 39/48 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.9 | 2e-07 | 33/47 (A498, C-33 A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.8 | 5e-07 | 32/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.7 | 5e-07 | 37/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 2e-05 | 31/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.48×** | +5.0 | 2e-05 | 32/47 (LoVo, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.8 | 5e-05 | 33/42 (PANC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.5 | 3e-04 | 27/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.013 | 27/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.058 | 19/47 (NCI-H23, NCI-H460, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.089 | 15/48 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.753×** | -5.1 | 2e-04 | 36/48 (A-172, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.707×** | -4.4 | 0.002 | 30/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.521×** | -4.3 | 0.002 | 29/48 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.715×** | -4.3 | 0.002 | 31/48 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -4.3 | 0.002 | 27/48 (A-172, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.739×** | -3.8 | 0.011 | 27/48 (SNU-423, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.768×** | -3.3 | 0.066 | 22/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.843× | -3.1 | 0.15 | 22/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 40.0 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.8) | — |
| [[LoVo (line)]] | wt | 52.3 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.39× (z +15.3) | — |
| [[A498 (line)]] | wt | 60.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.88× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 39.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.88× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 43.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 37.6 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +9.9) | — |
| [[A-427 (line)]] | wt | 41.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.69× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 45.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.7) | — |
| [[H4 (line)]] | wt | 39.9 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.28× (z +9.3) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.170× (z -9.8) |
| [[HOP62 (line)]] | alt | 42.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 43.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.02× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 68.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 38.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.21× (z +11.5) | — |
| [[A-172 (line)]] | wt | 33.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +9.9) | — |
| [[A549 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[C-33 A (line)]] | alt | 36.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.28× (z +9.0) | — |
| [[C32 (line)]] | wt | 45.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.64× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 27.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 36.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.86× (z +15.3) | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.00× (z +9.0) | — |
| [[KATO III (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 42.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.82× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 47.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.50× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 30.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 35.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.71× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 38.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 33.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.12× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 48.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.87× (z +12.8) | — |
| [[SW48 (line)]] | wt | 47.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.89× (z +11.0) | — |
| [[SW480 (line)]] | alt | 41.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +14.5) | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L2]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[THAP2]] | +0.74 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.73 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[NKAPD1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[C3orf38]] | +0.72 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[N4BP2L1]] | +0.72 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.70 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[TAS2R4]] | +0.70 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[CDKL3]] | +0.70 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.70 | +0.71 / +0.39 | both halves | 5e-05 |  |
| [[C1S]] | +0.69 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[METTL6]] | +0.69 | +0.77 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP1]] | -0.66 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[MED14]] | -0.65 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[EML4]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PODXL2]] | -0.64 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[ACTN4]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[MSH5]] | -0.62 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[APMAP]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[POLD2]] | -0.61 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[RBBP7]] | -0.61 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[NOMO1]] | -0.60 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[GUSB]] | -0.60 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CCDC59's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CCDC59's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.1, 16.9); signed map (23.1, -11.7). **Vector** length 98.8, 28.9% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.0 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +0.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 59 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:82,223,681-82,358,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC128, TAP26, BR22 |
| Reactome | 1 pathways, smallest: Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P031](https://www.uniprot.org/uniprotkb/Q9P031) (Thyroid transcription factor 1-associated protein 26):

> Component of the transcription complexes of the pulmonary surfactant-associated protein-B (SFTPB) and -C (SFTPC). Enhances homeobox protein Nkx-2.1-activated SFTPB and SFTPC promoter activities.

**Summary**, from NCBI Gene [29080](https://www.ncbi.nlm.nih.gov/gene/29080):

> Enables RNA binding activity. Predicted to be involved in DNA-templated transcription. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25005) · Entrez [29080](https://www.ncbi.nlm.nih.gov/gene/29080) · UniProt [Q9P031](https://www.uniprot.org/uniprotkb/Q9P031) · Ensembl [ENSG00000133773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133773)

## Data

Gene col 5473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5473); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5473]; `tensor/DDL_lfc|DDL_z.npy` [5473]; `embed/gene_vectors.npy` [5473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5473 or target_col == 5473). Every well: [[CCDC59 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC59.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
