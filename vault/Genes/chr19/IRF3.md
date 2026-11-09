---
symbol: "IRF3"
type: "gene"
col: 4735
ensembl_id: "ENSG00000126456"
name: "interferon regulatory factor 3"
location: "19q13.33"
module: 80
arm: "+"
pooled_cpm: 36.65
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# IRF3

*interferon regulatory factor 3* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.81× (z +38.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.693× (z -6.3, q 1e-07, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGL2]] (+0.66, fdr 7e-06), [[CD27-AS1]] (+0.66, fdr 8e-06), [[USP11]] (+0.64, fdr 1e-05); moves opposite to [[MRPL42]] (-0.61, fdr 3e-05), [[NAA40]] (-0.58, fdr 1e-04), [[ACTR5]] (-0.57, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.81×** | +38.4 | 0e+00 | 47/47 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +16.1 | 0e+00 | 41/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +15.9 | 0e+00 | 40/46 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +14.0 | 2e-42 | 34/47 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +8.4 | 4e-15 | 36/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.1 | 9e-08 | 26/48 (HOP62, A-172, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.7 | 0.014 | 13/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.014 | 16/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.3 | 0.056 | 0/48 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.056 | 17/47 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.058 | 11/45 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.065 | 12/48 (AsPC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -6.3 | 1e-07 | 29/48 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.576×** | -5.0 | 2e-04 | 24/47 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -4.9 | 2e-04 | 18/48 (HT-29, NCI-H23, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.737×** | -4.7 | 3e-04 | 22/48 (SW1417, J82, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.763×** | -4.7 | 3e-04 | 23/47 (C-33 A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.766×** | -4.6 | 4e-04 | 22/48 (SNU-423, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.850× | -3.9 | 0.008 | 16/48 (HOP62, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.798×** | -3.8 | 0.012 | 21/48 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.015 | 18/49 (SW48, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.816×** | -3.5 | 0.025 | 14/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.028 | 14/48 (NCI-H23, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.039 | 14/48 (HT-29, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.823×** | -3.2 | 0.053 | 10/47 (SNU-1, NCI-H661, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.085 | 14/47 (A-172, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.4 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.54× (z +26.7) | — |
| [[SW 900 (line)]] | alt | 46.1 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 41.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.50× (z +28.4) | — |
| [[BT-474 (line)]] | alt | 40.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.72× (z +22.5) | — |
| [[C32 (line)]] | wt | 27.6 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 66.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +19.3) | — |
| [[HOP62 (line)]] | alt | 26.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +25.0) | — |
| [[hTERT-HPNE (line)]] | wt | 32.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +16.9) | [[Pimozide (drug)]] 0.5 µM 0.221× (z -9.4) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 31.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.35× (z +15.8) | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.76× (z +28.4) | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +17.9) | — |
| [[Panc 03.27 (line)]] | alt | 46.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[RPMI-7951 (line)]] | alt | 38.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +16.5) | — |
| [[HS-578T (line)]] | alt | 32.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +25.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +23.3) | — |
| [[RKO (line)]] | wt | 30.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +19.0) | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +15.7) | — |
| [[SNU-1 (line)]] | wt | 34.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 26.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +17.7) | — |
| [[SW48 (line)]] | wt | 36.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +14.0) | — |
| [[SW480 (line)]] | alt | 50.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +20.0) | — |
| [[A549 (line)]] | wt | 27.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.80× (z +24.0) | — |
| [[AN3 CA (line)]] | alt | 39.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.2) | [[Silodosin (drug)]] 5 µM 0.0926× (z -9.4) |
| [[C-33 A (line)]] | alt | 54.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 37.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +13.6) | — |
| [[Hs 766T (line)]] | wt | 32.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +19.0) | — |
| [[LoVo (line)]] | wt | 32.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 25.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +19.2) | — |
| [[A498 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +19.9) | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.93× (z +20.3) | — |
| [[COLO 205 (line)]] | alt | 51.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 84.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +14.0) | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 77.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +12.4) | — |
| [[J82 (line)]] | alt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +18.8) | — |
| [[KATO III (line)]] | alt | 38.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +18.6) | — |
| [[LS 180 (line)]] | wt | 57.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 34.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +21.2) | — |
| [[NCI-H23 (line)]] | alt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +20.9) | — |
| [[SHP-77 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 97.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +15.9) | — |
| [[A-427 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGL2]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CD27-AS1]] | +0.66 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[USP11]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NEK8]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ENO3]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NFKBID]] | +0.62 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MAP3K11]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CREB3L4]] | +0.61 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PDCD7]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[BOLA1]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL42]] | -0.61 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[NAA40]] | -0.58 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[ACTR5]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SLC23A2]] | -0.57 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NOMO3]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FITM2]] | -0.56 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[FYCO1]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[EXOC2]] | -0.55 | -0.56 / -0.40 | both halves | 4e-05 | STRING 602 |
| [[ANKRD52]] | -0.55 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[NUTF2]] | -0.54 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[OPA1]] | -0.54 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[SOAT1]] | -0.53 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IRF3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOAT1]] | C | SOAT1 activity lowers IRF3's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.83× higher at baseline in the lines without SOAT1 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, 9.3); signed map (20.7, -6.2). **Vector** length 109, 27.2% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +38.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +15.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +16.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | +1.5 | +0.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.6 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | -5.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,659,569-49,665,875 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Interferon regulatory factors |
| Reactome | 36 pathways, smallest: IRF3 mediated activation of type 1 IFN; LRR FLII-interacting protein 1 (LRRFIP1) activates type I IFN production; IRF3-mediated induction of type I IFN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14653](https://www.uniprot.org/uniprotkb/Q14653) (Interferon regulatory factor 3):

> Key transcriptional regulator of type I interferon (IFN)-dependent immune responses which plays a critical role in the innate immune response against DNA and RNA viruses. Regulates the transcription of type I IFN genes (IFN-alpha and IFN-beta) and IFN-stimulated genes (ISG) by binding to an interferon-stimulated response element (ISRE) in their promoters. Acts as a more potent activator of the IFN-beta (IFNB) gene than the IFN-alpha (IFNA) gene and plays a critical role in both the early and …

**Summary**, from NCBI Gene [3661](https://www.ncbi.nlm.nih.gov/gene/3661):

> This gene encodes a member of the interferon regulatory transcription factor (IRF) family. The encoded protein is found in an inactive cytoplasmic form that upon serine/threonine phosphorylation forms a complex with CREBBP. This complex translocates to the nucleus and activates the transcription of interferons alpha and beta, as well as other interferon-induced genes. The protein plays an important role in the innate immune response against DNA and RNA viruses. Mutations in this gene are …

**Accessions** — [HGNC:6118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6118) · Entrez [3661](https://www.ncbi.nlm.nih.gov/gene/3661) · UniProt [Q14653](https://www.uniprot.org/uniprotkb/Q14653) · Ensembl [ENSG00000126456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126456)

## Data

Gene col 4735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4735); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4735]; `tensor/DDL_lfc|DDL_z.npy` [4735]; `embed/gene_vectors.npy` [4735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4735 or target_col == 4735). Every well: [[IRF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
