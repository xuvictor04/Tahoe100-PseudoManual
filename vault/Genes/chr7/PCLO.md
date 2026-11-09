---
symbol: "PCLO"
type: "gene"
col: 11819
ensembl_id: "ENSG00000186472"
name: "piccolo presynaptic cytomatrix protein"
location: "7q21.11"
module: 94
arm: "+"
pooled_cpm: 111.86
n_lines_expressing: 35
n_dd_up: 56
n_dd_down: 29
n_dd_up_clean: 54
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# PCLO

*piccolo presynaptic cytomatrix protein* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 56 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 5.39× (z +38.2, q 0e+00, up in 32 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.494× (z -11.3, q 6e-27, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDSL]] (+0.72, fdr 7e-06), [[DUSP15]] (+0.69, fdr 7e-06), [[STK32A]] (+0.68, fdr 1e-05); moves opposite to [[MBOAT7]] (-0.62, fdr 1e-05), [[UFD1]] (-0.57, fdr 1e-05), [[DCUN1D2]] (-0.56, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAR2P1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[STK33]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 4 with an alert ⚠; shown: the 15 strongest. 56 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **5.39×** | +38.2 | 0e+00 | 32/33 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **7.78×** | +32.9 | 0e+00 | 34/34 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **6.60×** | +30.3 | 0e+00 | 32/33 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.57×** | +28.9 | 0e+00 | 28/33 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.85×** | +24.4 | 0e+00 | 31/33 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **4.01×** | +20.2 | 0e+00 | 32/33 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.93×** | +16.4 | 0e+00 | 28/33 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +15.7 | 0e+00 | 30/33 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +15.7 | 0e+00 | 30/33 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +14.9 | 0e+00 | 27/33 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.57×** | +13.7 | 7e-41 | 29/33 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +10.8 | 2e-25 | 27/33 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.94×** | +10.6 | 1e-24 | 23/33 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +9.5 | 9e-20 | 29/34 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +9.3 | 3e-19 | 25/33 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -11.3 | 6e-27 | 26/33 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -9.4 | 1e-18 | 27/33 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.538×** | -9.0 | 4e-17 | 27/33 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -8.8 | 2e-16 | 25/33 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.548×** | -8.7 | 2e-16 | 28/33 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -8.3 | 9e-15 | 24/33 (Panc 03.27, A-427, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.574×** | -7.8 | 5e-13 | 27/33 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.585×** | -7.2 | 5e-11 | 23/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.734×** | -7.0 | 1e-10 | 25/34 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.642×** | -5.9 | 2e-07 | 19/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.695×** | -5.8 | 3e-07 | 20/33 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -5.3 | 5e-06 | 22/33 (J82, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.734×** | -5.0 | 3e-05 | 20/33 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -4.6 | 2e-04 | 16/34 (C32, PANC-1, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **0.760×** | -4.2 | 9e-04 | 14/33 (C32, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.770×** | -4.0 | 0.002 | 10/33 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.849× | -3.7 | 0.006 | 6/33 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.006 | 19/33 (SW480, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 283 | 12 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +28.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.254× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 291 | 4 | 13 (6 ⚠) | [[Selinexor (drug)]] 5 µM 2.70× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.289× (z -12.5) |
| [[J82 (line)]] | alt | 255 | 4 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.195× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.260× (z -13.4) |
| [[PANC-1 (line)]] | alt | 46.8 | 7 | 8 (1 ⚠) | [[Selinexor (drug)]] 5 µM 7.30× (z +22.5) | [[Digitoxin (drug)]] 0.5 µM 0.192× (z -13.2) |
| [[LoVo (line)]] | wt | 38.7 | 12 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 20.7× (z +29.3) | [[Digitoxin (drug)]] 0.5 µM 0.219× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 183 | 13 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +20.9) | — |
| [[SK-MEL-2 (line)]] | alt | 257 | 12 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.12× (z +19.1) | — |
| [[A-172 (line)]] | wt | 52.8 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +25.6) | — |
| [[HT-29 (line)]] | alt | 42.3 | 11 | 0 | [[Selinexor (drug)]] 5 µM 17.5× (z +26.9) | — |
| [[Panc 03.27 (line)]] | alt | 385 | 5 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 282 | 7 | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.74× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.0) |
| [[A498 (line)]] | wt | 153 | 9 | 1 | [[Selinexor (drug)]] 5 µM 3.41× (z +16.2) | [[Bortezomib (drug)]] 0.05 µM 0.307× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 70.8 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +25.6) | — |
| [[SW 900 (line)]] | alt | 88.2 | 10 | 0 | [[Selinexor (drug)]] 5 µM 5.59× (z +17.8) | — |
| [[BT-474 (line)]] | alt | 91.2 | 9 | 0 | [[Selinexor (drug)]] 5 µM 7.95× (z +20.4) | — |
| [[H4 (line)]] | wt | 64.3 | 9 | 0 | [[Selinexor (drug)]] 5 µM 14.7× (z +20.5) | — |
| [[HOP62 (line)]] | alt | 47.3 | 9 | 0 | [[Selinexor (drug)]] 5 µM 11.6× (z +24.3) | — |
| [[CFPAC-1 (line)]] | alt | 90.0 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.6) | — |
| [[C32 (line)]] | wt | 178 | 7 | 0 | [[Selinexor (drug)]] 0.05 µM 4.60× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 38.0 | 6 | 0 | [[Selinexor (drug)]] 5 µM 9.70× (z +15.1) | — |
| [[CHP-212 (line)]] | wt | 89.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +17.0) | — |
| [[hTERT-HPNE (line)]] | wt | 59.6 | 6 | 0 | [[Selinexor (drug)]] 5 µM 4.77× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 64.8 | 4 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 8.28× (z +20.5) | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.4) |
| [[SHP-77 (line)]] | alt | 259 | 4 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.91× (z +19.0) | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 157 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +16.8) | — |
| [[A549 (line)]] | wt | 37.7 | 5 | 0 | [[Selinexor (drug)]] 5 µM 9.60× (z +19.4) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 4 | 0 | [[Selinexor (drug)]] 5 µM 11.3× (z +34.1) | — |
| [[NCI-H1573 (line)]] | alt | 95.8 | 4 | 0 | [[Selinexor (drug)]] 5 µM 11.8× (z +26.0) | — |
| [[SW1417 (line)]] | alt | 410 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.54× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.269× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 30.6 | 3 | 0 | [[Selinexor (drug)]] 5 µM 11.4× (z +19.0) | — |
| [[NCI-H2030 (line)]] | alt | 85.2 | 2 | 0 | [[Selinexor (drug)]] 5 µM 4.95× (z +13.5) | — |
| [[NCI-H661 (line)]] | alt | 1,179 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 137 | 1 | 0 | [[Selinexor (drug)]] 5 µM 6.03× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDSL]] | +0.72 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[DUSP15]] | +0.69 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[STK32A]] | +0.68 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[NGFR]] | +0.66 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[ZNF441]] | +0.63 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PNPLA4]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[RNF150]] | +0.60 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[MAPK1IP1L]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ZNF44]] | +0.59 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TIGD2]] | +0.59 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SLC44A2]] | +0.59 | +0.27 / +0.70 | both halves | 3e-04 |  |
| [[CLK4]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[UFD1]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[LIN52]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[FOXK2]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TCF3]] | -0.53 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[RBM14-RBM4]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[STARD3]] | -0.52 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CMC2]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[SAP130]] | -0.51 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[DONSON]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[DGCR8]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR2P1]] | B | FAR2P1 activity raises PCLO's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without FAR2P1 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[NGFR]] | B | NGFR activity raises PCLO's level | lines that do not express NGFR (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without NGFR | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK33]] | B | PCLO activity raises STK33's level | lines that do not express PCLO (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without PCLO | 0.045 | ⚠ within organs, on part of the lines; also absent: POPDC3, WIPF1, WDR17 |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.8, 24.7); signed map (14.4, -16.2). **Vector** length 110, 32.4% of its response variance represented; |z| ≥ 3 in 1,433 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +13.1 | +38.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +10.1 | +30.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.9 | +16.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +24.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.5 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +15.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.9 | +20.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +5.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -4.4 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -11.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -5.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | piccolo presynaptic cytomatrix protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:82,754,012-83,162,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0559, DKFZp779G1236, ACZ |
| Gene groups (HGNC) | C2 domain containing; PDZ domain containing; Zinc fingers PCLO-type |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6V0](https://www.uniprot.org/uniprotkb/Q9Y6V0) (Protein piccolo):

> Scaffold protein of the presynaptic cytomatrix at the active zone (CAZ) which is the place in the synapse where neurotransmitter is released (By similarity). After synthesis, participates in the formation of Golgi-derived membranous organelles termed Piccolo-Bassoon transport vesicles (PTVs) that are transported along axons to sites of nascent synaptic contacts (By similarity). At the presynaptic active zone, regulates the spatial organization of synaptic vesicle cluster, the protein complexes …

**Summary**, from NCBI Gene [27445](https://www.ncbi.nlm.nih.gov/gene/27445):

> The protein encoded by this gene is part of the presynaptic cytoskeletal matrix, which is involved in establishing active synaptic zones and in synaptic vesicle trafficking. Variations in this gene have been associated with bipolar disorder and major depressive disorder. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:13406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13406) · Entrez [27445](https://www.ncbi.nlm.nih.gov/gene/27445) · UniProt [Q9Y6V0](https://www.uniprot.org/uniprotkb/Q9Y6V0) · Ensembl [ENSG00000186472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186472)

## Data

Gene col 11819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11819); `tables/drug_effects.parquet` (98 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11819]; `tensor/DDL_lfc|DDL_z.npy` [11819]; `embed/gene_vectors.npy` [11819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11819 or target_col == 11819). Every well: [[PCLO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCLO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
