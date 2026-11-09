---
symbol: "DAGLB"
type: "gene"
col: 8959
ensembl_id: "ENSG00000164535"
name: "diacylglycerol lipase beta"
location: "7p22.1"
module: 192
arm: "+"
pooled_cpm: 33.36
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# DAGLB

*diacylglycerol lipase beta* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.10× (z +11.4, q 1e-27, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.406× (z -13.9, q 2e-41, down in 37 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.169×, NCI-H1792 0.162×, A-172 0.147×, NCI-H2347 0.220×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 0.202×, SW480 0.334×, A498 0.271×, SNU-423 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.159×, LOX-IMVI 0.208×, PANC-1 0.309×; ⚠ toxic; transcription drop); [[Ixazomib (drug)]] 5 µM in 1 line (H4 0.0897×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGST3]] (+0.55, fdr 2e-05), [[TMEM184B]] (+0.54, fdr 5e-05), [[PLIN3]] (+0.53, fdr 8e-05); moves opposite to [[TTC12]] (-0.54, fdr 7e-05), [[TIA1]] (-0.49, fdr 1e-04), [[FBXL17]] (-0.49, fdr 4e-05).
> It is in [[Module 192]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +11.4 | 1e-27 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +11.4 | 1e-27 | 46/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +11.2 | 1e-26 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.0 | 2e-17 | 36/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +8.7 | 5e-16 | 29/47 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.9 | 3e-13 | 39/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +7.5 | 6e-12 | 36/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +7.4 | 9e-12 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +7.3 | 1e-11 | 37/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +6.2 | 3e-08 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 5e-05 | 24/47 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 24/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +4.4 | 5e-04 | 25/48 (A549, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 7e-04 | 22/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.2 | 9e-04 | 25/48 (LoVo, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8959.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.169×, NCI-H1792 0.162×, A-172 0.147×, NCI-H2347 0.220×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 0.202×, SW480 0.334×, A498 0.271×, SNU-423 0.228×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.159×, LOX-IMVI 0.208×, PANC-1 0.309×; ⚠ toxic; transcription drop); [[Ixazomib (drug)]] 5 µM in 1 line (H4 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.406×** | -13.9 | 2e-41 | 37/45 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -9.8 | 3e-20 | 28/36 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.505×** | -9.8 | 3e-20 | 30/39 (SHP-77, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Belzutifan (drug)]] 5 µM |  | 0.679× | -3.1 | 0.24 | 17/45 (HCT15, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.7 | 6 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.89× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 67.7 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib (drug)]] 5 µM 0.0897× (z -8.5) |
| [[KATO III (line)]] | alt | 38.2 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -19.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 60.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -8.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.82× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 37.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.2) | — |
| [[J82 (line)]] | alt | 34.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -12.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST3]] | +0.55 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[TMEM184B]] | +0.54 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[PLIN3]] | +0.53 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[MIR193BHG]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RRAS]] | +0.51 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[ANKRD27]] | +0.51 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[DAPK3]] | +0.51 | +0.53 / +0.37 | both halves | 7e-05 |  |
| [[PDZD7]] | +0.51 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[RALA]] | +0.51 | +0.49 / +0.32 | both halves | 1e-04 |  |
| [[GIPR]] | +0.50 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[TBC1D25]] | +0.50 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[ARHGEF10]] | +0.50 | +0.36 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC12]] | -0.54 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[TIA1]] | -0.49 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[FBXL17]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[NT5DC1]] | -0.48 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[GTF3C6]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[RGS5]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 | pathway: G alpha (q) signalling events |
| [[PRR4]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[RAP2C]] | -0.47 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[MCCC2]] | -0.46 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[PRH1]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ZFP91]] | -0.46 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[ZNF280D]] | -0.46 | -0.31 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.0, 1.3); signed map (-23.7, 20.8). **Vector** length 82.9, 18.5% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.0 | +2.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol lipase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,409,126-6,484,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCCR13L, DAGLBETA |
| Gene groups (HGNC) | Lipases |
| Reactome | 7 pathways, smallest: Arachidonate production from DAG; Effects of PIP2 hydrolysis; G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCG7](https://www.uniprot.org/uniprotkb/Q8NCG7) (Diacylglycerol lipase-beta):

> Lipase that catalyzes the hydrolysis of arachidonic acid (AA)-esterified diacylglycerols (DAGs) to produce the principal endocannabinoid, 2-arachidonoylglycerol (2-AG) which can be further cleaved by downstream enzymes to release arachidonic acid (AA) for cyclooxygenase (COX)-mediated eicosanoid production. Preferentially hydrolyzes DAGs at the sn-1 position in a calcium-dependent manner and has negligible activity against other lipids including monoacylglycerols and phospholipids. Plays a key …

**Summary**, from NCBI Gene [221955](https://www.ncbi.nlm.nih.gov/gene/221955):

> Enables lipase activity. Involved in arachidonate metabolic process. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28923) · Entrez [221955](https://www.ncbi.nlm.nih.gov/gene/221955) · UniProt [Q8NCG7](https://www.uniprot.org/uniprotkb/Q8NCG7) · Ensembl [ENSG00000164535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164535)

## Data

Gene col 8959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8959); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8959]; `tensor/DDL_lfc|DDL_z.npy` [8959]; `embed/gene_vectors.npy` [8959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8959 or target_col == 8959). Every well: [[DAGLB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAGLB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
