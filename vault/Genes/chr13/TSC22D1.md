---
symbol: "TSC22D1"
type: "gene"
col: 2274
ensembl_id: "ENSG00000102804"
name: "TSC22 domain family member 1"
location: "13q14.11"
module: 57
arm: "-"
pooled_cpm: 175.44
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# TSC22D1

*TSC22 domain family member 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.34× (z +7.3, q 2e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.550× (z -10.6, q 2e-23, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP1]] (+0.66, fdr 1e-05), [[KLF10]] (+0.65, fdr 7e-06), [[MAD2L1BP]] (+0.64, fdr 1e-05); moves opposite to [[SEC23A]] (-0.71, fdr 1e-05), [[VAMP7]] (-0.64, fdr 1e-05), [[HSPB11]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.3 | 2e-10 | 32/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.3 | 1e-07 | 24/49 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.3 | 2e-05 | 28/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 8e-05 | 26/48 (AsPC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.010 | 22/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.064 | 24/48 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.066 | 12/48 (A549, SW1417, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.068 | 21/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.068 | 20/49 (A549, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -10.6 | 2e-23 | 40/48 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -10.4 | 8e-23 | 38/44 (C-33 A, SW480, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.573×** | -9.9 | 9e-21 | 42/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.559×** | -9.5 | 2e-19 | 33/45 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -8.9 | 7e-17 | 36/49 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.626×** | -8.3 | 8e-15 | 37/48 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -8.3 | 9e-15 | 38/48 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.435×** | -7.7 | 7e-13 | 29/38 (HEC-1-A, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -7.3 | 2e-11 | 38/48 (LS 180, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -5.3 | 7e-06 | 27/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -4.7 | 1e-04 | 28/48 (LOX-IMVI, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -4.3 | 9e-04 | 26/48 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.840× | -4.3 | 9e-04 | 22/48 (MIA PaCa-2, NCI-H2030, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 0.001 | 24/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.658×** | -3.9 | 0.004 | 23/47 (RPMI-7951, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.018 | 21/48 (LOX-IMVI, H4, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.034 | 20/49 (LS 180, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.877× | -3.1 | 0.050 | 10/49 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.070 | 18/48 (NCI-H460, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.842× | -2.9 | 0.092 | 17/47 (LOX-IMVI, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 738 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0806× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 8 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.246× (z -11.8) |
| [[COLO 205 (line)]] | alt | 833 | 2 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.45× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.293× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 172 | 3 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.97× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.453× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 82.4 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +20.6) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.0× (z +18.9) | — |
| [[SNU-1 (line)]] | wt | 336 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -13.7) |
| [[A-427 (line)]] | wt | 81.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.245× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 115 | 0 | 5 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.108× (z -13.9) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.431× (z -10.1) |
| [[LS 180 (line)]] | wt | 305 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -10.2) |
| [[HOP62 (line)]] | alt | 96.9 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.33× (z +12.5) | [[Lonafarnib (drug)]] 5 µM 0.159× (z -8.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 468 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.363× (z -10.4) |
| [[HT-29 (line)]] | alt | 245 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.504× (z -8.5) |
| [[KATO III (line)]] | alt | 177 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 115 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.86× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 74.7 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.439× (z -9.1) |
| [[SW48 (line)]] | wt | 199 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.83× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 323 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -10.3) |
| [[LoVo (line)]] | wt | 129 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.487× (z -8.9) |
| [[A-172 (line)]] | wt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.71× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.111× (z -10.7) ⚠ toxic |
| [[C-33 A (line)]] | alt | 190 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0805× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.417× (z -9.2) |
| [[SW1417 (line)]] | alt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +10.2) | — |
| [[SW480 (line)]] | alt | 204 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -20.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.368× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[J82 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H2347 (line)]] | alt | 62.0 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.04× (z +9.1) | — |
| [[RKO (line)]] | wt | 95.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 230 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 260 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP1]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KLF10]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MAD2L1BP]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SATB2]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ASXL2]] | +0.63 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[CUX1]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SKIL]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[MED1]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SPEN]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZBED5]] | +0.62 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PNRC2]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TCF12]] | +0.61 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC23A]] | -0.71 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.64 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SGSM3]] | -0.63 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.62 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC5]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ATPAF1]] | -0.61 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[RARS2]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[MSTO2P]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ARPC1A]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[NUS1]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GPR107]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.2, -5.3); signed map (15.4, -9.6). **Vector** length 122, 36.1% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.6 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.3 | +5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +2.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.8 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.4 | -8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.4 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | TSC22 domain family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:44,432,143-44,577,147 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSC22, MGC17597; previously TGFB1I4 |
| Gene groups (HGNC) | TSC22 domain family |
| Hallmark sets | ANDROGEN_RESPONSE, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 2 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation; Transcriptional regulation of pluripotent stem cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15714](https://www.uniprot.org/uniprotkb/Q15714) (TSC22 domain family protein 1):

> Transcriptional repressor. Acts on the C-type natriuretic peptide (CNP) promoter. Acts to promote CASP3-mediated apoptosis. Positively regulates TGF-beta signaling by interacting with SMAD7 which inhibits binding of SMAD7 to TGFBR1, preventing recruitment of SMURF ubiquitin ligases to TGFBR1 and inhibiting SMURF-mediated ubiquitination and degradation of TGFBR1. Contributes to enhancement of TGF-beta signaling by binding to and modulating the transcription activator activity of SMAD4. Promotes …

**Summary**, from NCBI Gene [8848](https://www.ncbi.nlm.nih.gov/gene/8848):

> This gene encodes a member of the TSC22 domain family of leucine zipper transcription factors. The encoded protein is stimulated by transforming growth factor beta, and regulates the transcription of multiple genes including C-type natriuretic peptide. The encoded protein may play a critical role in tumor suppression through the induction of cancer cell apoptosis, and a single nucleotide polymorphism in the promoter of this gene has been associated with diabetic nephropathy. Alternatively …

**Accessions** — [HGNC:16826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16826) · Entrez [8848](https://www.ncbi.nlm.nih.gov/gene/8848) · UniProt [Q15714](https://www.uniprot.org/uniprotkb/Q15714) · Ensembl [ENSG00000102804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102804)

## Data

Gene col 2274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2274); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2274]; `tensor/DDL_lfc|DDL_z.npy` [2274]; `embed/gene_vectors.npy` [2274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2274 or target_col == 2274). Every well: [[TSC22D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSC22D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
