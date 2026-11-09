---
symbol: "UBE2H"
type: "gene"
col: 11834
ensembl_id: "ENSG00000186591"
name: "ubiquitin conjugating enzyme E2 H"
location: "7q32.2"
module: 31
arm: "+"
pooled_cpm: 379.22
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# UBE2H

*ubiquitin conjugating enzyme E2 H* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.85× (z +15.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.621× (z -11.6, q 2e-28, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.779× (z -6.1, q 9e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUP]] (+0.61, fdr 1e-05), [[MXD1]] (+0.61, fdr 1e-05), [[KIAA1522]] (+0.60, fdr 1e-05); moves opposite to [[TERT]] (-0.53, fdr 1e-05), [[DCTD]] (-0.52, fdr 3e-05), [[MSANTD2]] (-0.51, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[PKP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +15.6 | 0e+00 | 45/48 (PANC-1, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +13.2 | 2e-37 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +13.2 | 3e-37 | 30/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +9.2 | 6e-18 | 36/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +7.6 | 3e-12 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.5 | 8e-12 | 35/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +7.3 | 2e-11 | 31/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +6.9 | 5e-10 | 29/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +6.8 | 7e-10 | 25/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +6.6 | 2e-09 | 32/48 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +6.4 | 6e-09 | 21/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +6.2 | 2e-08 | 28/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 2e-07 | 30/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +5.8 | 2e-07 | 32/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 3e-06 | 30/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.8 | 6e-05 | 25/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -11.6 | 2e-28 | 38/44 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.646×** | -11.1 | 3e-26 | 37/49 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.671×** | -9.4 | 1e-18 | 35/45 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.829×** | -6.8 | 2e-09 | 24/49 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.779×** | -6.1 | 9e-08 | 29/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -6.1 | 9e-08 | 30/47 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.854× | -5.7 | 9e-07 | 16/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | 0.844× | -4.3 | 0.001 | 21/48 (SW1417, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.029 | 18/48 (C32, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.787×** | -3.2 | 0.079 | 21/47 (SW 1088, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 163 | 17 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.15× (z +28.3) | — |
| [[NCI-H460 (line)]] | wt | 338 | 10 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.569× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 140 | 9 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.92× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 245 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.1) | — |
| [[HT-29 (line)]] | alt | 301 | 7 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.06× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 496 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.488× (z -10.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 229 | 7 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 768 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -18.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[J82 (line)]] | alt | 205 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +26.9) | — |
| [[Panc 03.27 (line)]] | alt | 957 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -18.6) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW1417 (line)]] | alt | 817 | 2 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 1.82× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -19.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 190 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +20.2) | — |
| [[NCI-H1573 (line)]] | alt | 169 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 598 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -16.4) ⚠ cell-cycle shift, explains ~10% of this change |
| [[BT-474 (line)]] | alt | 510 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.05× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.9) ⚠ cell-cycle shift, explains ~10% of this change |
| [[C32 (line)]] | wt | 955 | 2 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.88× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -22.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 279 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +19.6) | — |
| [[LoVo (line)]] | wt | 611 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.32× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 470 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -16.4) ⚠ cell-cycle shift, explains ~10% of this change |
| [[RKO (line)]] | wt | 205 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.478× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 305 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.9) | — |
| [[A498 (line)]] | wt | 598 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +22.2) | — |
| [[KATO III (line)]] | alt | 563 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.617× (z -9.7) |
| [[SNU-423 (line)]] | alt | 436 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.30× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -12.1) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW 900 (line)]] | alt | 431 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.90× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -15.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 194 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 286 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.7) | — |
| [[HepG2_C3A (line)]] | wt | 254 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -10.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 166 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 484 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -14.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 112 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 200 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.4) | — |
| [[SW48 (line)]] | wt | 273 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 775 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 243 | 2 | 0 | [[Auranofin (drug)]] 5 µM 1.96× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 238 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 254 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +16.6) | — |
| [[A549 (line)]] | wt | 280 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -9.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[COLO 205 (line)]] | alt | 394 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[Hs 766T (line)]] | wt | 479 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -13.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[LOX-IMVI (line)]] | wt | 208 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.93× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 296 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 255 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 488 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 357 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUP]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MXD1]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[KIAA1522]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[CLU]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[NPEPPS]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[FA2H]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[GPRC5A]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CLDN4]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[MKNK1]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NEAT1]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[EPB41L1]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERT]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[DCTD]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.51 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PMS1]] | -0.50 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF202]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[NAF1]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CAD]] | -0.50 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A15]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ADSL]] | -0.49 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[PRIMPOL]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[METTL8]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NUP35]] | -0.48 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKP1]] | B | PKP1 activity raises UBE2H's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without PKP1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[GPRC5A]] | B | GPRC5A activity raises UBE2H's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without GPRC5A | 0.003 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PKP1]] | B | PKP1 activity weakens UBE2H's drug response | lines that do not express PKP1 (33) vs lines expressing it (16) | the lines without PKP1 respond 1.25× as strongly (z diff -0.90); strongest at Homoharringtonine 5 µM: 1.61x vs 1.15x (z diff -5.7) | 0.006 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; target measured in part of the lines; both ways; artifact flags |
| [[TERT]] | B | TERT activity lowers UBE2H's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.90× higher at baseline in the lines without TERT | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[TERT]] | B | TERT activity strengthens UBE2H's drug response | lines that do not express TERT (13) vs lines expressing it (36) | the lines without TERT respond 0.96× as strongly (z diff +0.52); strongest at Homoharringtonine 5 µM: 1.18x vs 1.56x (z diff +3.6) | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS; target measured in part of the lines; both ways; artifact flags |
| [[TMPRSS4]] | B | TMPRSS4 activity raises UBE2H's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 1.65× lower at baseline in the lines without TMPRSS4 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[LIPH]] | B | LIPH activity raises UBE2H's level | lines that do not express LIPH (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without LIPH | 0.018 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[DUOX2]] | B | DUOX2 activity raises UBE2H's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.60× lower at baseline in the lines without DUOX2 | 0.020 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[KPNA7]] | B | KPNA7 activity raises UBE2H's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without KPNA7 | 0.022 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[FA2H]] | B | FA2H activity raises UBE2H's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without FA2H | 0.025 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[DUOX2]] | B | DUOX2 activity weakens UBE2H's drug response | lines that do not express DUOX2 (32) vs lines expressing it (17) | the lines without DUOX2 respond 1.27× as strongly (z diff -0.84); strongest at Ouabain (Octahydrate) 5 µM: 1.87x vs 1.32x (z diff -4.0) | 0.033 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB; target measured in part of the lines; both ways; artifact flags |
| [[PCDH1]] | B | PCDH1 activity raises UBE2H's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without PCDH1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.0, 57.2); signed map (-7.5, 18.2). **Vector** length 127, 46.4% of its response variance represented; |z| ≥ 3 in 1,784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +6.5 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +7.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.2 | +5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.3 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -2.8 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:129,830,732-129,952,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBCH, UBC8, GID3 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62256](https://www.uniprot.org/uniprotkb/P62256) (Ubiquitin-conjugating enzyme E2 H):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. E2 ubiquitin conjugating enzyme that transfers ubiquitin to MAEA, a core component of the CTLH E3 ubiquitin-protein ligase complex. In vitro catalyzes 'Lys-11'- and 'Lys-48'-linked polyubiquitination. Capable, in vitro, to ubiquitinate histone H2A.

**Summary**, from NCBI Gene [7328](https://www.ncbi.nlm.nih.gov/gene/7328):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein sequence is 100% identical to the mouse homolog and 98% identical to the frog and …

**Accessions** — [HGNC:12484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12484) · Entrez [7328](https://www.ncbi.nlm.nih.gov/gene/7328) · UniProt [P62256](https://www.uniprot.org/uniprotkb/P62256) · Ensembl [ENSG00000186591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186591)

## Data

Gene col 11834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11834); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11834]; `tensor/DDL_lfc|DDL_z.npy` [11834]; `embed/gene_vectors.npy` [11834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11834 or target_col == 11834). Every well: [[UBE2H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
