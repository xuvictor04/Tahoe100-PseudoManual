---
symbol: "AP5Z1"
type: "gene"
col: 14330
ensembl_id: "ENSG00000242802"
name: "adaptor related protein complex 5 subunit zeta 1"
location: "7p22.1"
module: 122
arm: "+"
pooled_cpm: 20.45
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 26
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# AP5Z1

*adaptor related protein complex 5 subunit zeta 1* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.55× (z +25.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.654× (z -5.9, q 2e-06, down in 22 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.774× (z -5.2, q 5e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A11]] (+0.72, fdr 7e-06), [[HEXA]] (+0.68, fdr 1e-05), [[SLC38A7]] (+0.65, fdr 7e-06); moves opposite to [[ACTL6A]] (-0.63, fdr 7e-06), [[LSM4]] (-0.60, fdr 1e-05), [[ECT2]] (-0.56, fdr 1e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.55×** | +25.6 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.70×** | +18.7 | 0e+00 | 47/47 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.22×** | +11.4 | 1e-27 | 42/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +10.0 | 2e-21 | 36/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.98×** | +9.2 | 3e-18 | 38/48 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.29×** | +8.9 | 5e-17 | 38/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.9 | 5e-17 | 35/47 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +8.9 | 5e-17 | 32/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +8.8 | 1e-16 | 36/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +8.0 | 5e-14 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +7.9 | 2e-13 | 36/48 (PANC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.1 | 5e-11 | 29/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +6.5 | 3e-09 | 21/36 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +6.4 | 7e-09 | 34/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.86×** | +6.3 | 1e-08 | 32/48 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.2 | 8e-06 | 27/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +5.2 | 8e-06 | 21/48 (NCI-H23, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -5.9 | 2e-06 | 22/30 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -5.2 | 5e-05 | 24/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.724×** | -4.7 | 6e-04 | 28/48 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.735×** | -4.1 | 0.006 | 17/46 (NCI-H661, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.9 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +27.3) | — |
| [[PANC-1 (line)]] | alt | 19.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +21.2) | — |
| [[A-172 (line)]] | wt | 16.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 19.6 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.86× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -18.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +19.0) | — |
| [[H4 (line)]] | wt | 27.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 35.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.43× (z +12.2) | — |
| [[LoVo (line)]] | wt | 20.8 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.70× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 8.99 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.17× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 8.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 34.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.0924× (z -15.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 21.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.27× (z +12.8) | — |
| [[J82 (line)]] | alt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +19.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 9.82 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +15.3) | [[Belumosudil (drug)]] 5 µM 0.155× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.8) | — |
| [[RKO (line)]] | wt | 14.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +19.1) | — |
| [[SW 900 (line)]] | alt | 19.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 9.97 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0838× (z -9.3) |
| [[HS-578T (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +15.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 9.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 38.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +8.8) | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0902× (z -11.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A11]] | +0.72 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[HEXA]] | +0.68 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[SLC38A7]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[WASHC2A]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[WDR81]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 | same gene group |
| [[ATP6V1G1]] | +0.64 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[CELF6]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SPNS1]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[GPATCH3]] | +0.63 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[CLN3]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RNF185]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[LSM4]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ECT2]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SSX2IP]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TTC13]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MAD2L1]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CDC7]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CALM2]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RANBP1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[R3HDM1]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[AKAP11]] | -0.49 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TUBG1]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.6, 14.1); signed map (-9.3, -19.3). **Vector** length 95.4, 22.9% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +18.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +25.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +8.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +6.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 5 subunit zeta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:4,775,615-4,794,397 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPG48, zeta; previously KIAA0415 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Adaptor related protein complex 5 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43299](https://www.uniprot.org/uniprotkb/O43299) (AP-5 complex subunit zeta-1):

> As part of AP-5, a probable fifth adaptor protein complex it may be involved in endosomal transport. According to PubMed:20613862 it is a putative helicase required for efficient homologous recombination DNA double-strand break repair.

**Summary**, from NCBI Gene [9907](https://www.ncbi.nlm.nih.gov/gene/9907):

> This gene was identified by genome-wide screen for genes involved in homologous recombination DNA double-strand break repair (HR-DSBR). The encoded protein was found in a complex with other proteins that have a role in HR-DSBR. Knockdown of this gene reduced homologous recombination, and mutations in this gene were found in patients with spastic paraplegia. It was concluded that this gene likely encodes a helicase (PMID:20613862). [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:22197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22197) · Entrez [9907](https://www.ncbi.nlm.nih.gov/gene/9907) · UniProt [O43299](https://www.uniprot.org/uniprotkb/O43299) · Ensembl [ENSG00000242802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242802)

## Data

Gene col 14330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14330); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14330]; `tensor/DDL_lfc|DDL_z.npy` [14330]; `embed/gene_vectors.npy` [14330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14330 or target_col == 14330). Every well: [[AP5Z1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP5Z1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
