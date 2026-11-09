---
symbol: "XPO1"
type: "gene"
col: 1357
ensembl_id: "ENSG00000082898"
name: "exportin 1"
location: "2p15"
module: 94
arm: "+"
pooled_cpm: 324.57
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# XPO1

*exportin 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.12× (z +21.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.566× (z -11.4, q 3e-27, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF138]] (+0.65, fdr 7e-06), [[SLC44A2]] (+0.64, fdr 7e-06), [[SLC16A14]] (+0.63, fdr 1e-05); moves opposite to [[MAPKAPK2]] (-0.58, fdr 2e-05), [[WNT2B]] (-0.57, fdr 1e-05), [[UCHL3]] (-0.55, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MARCHF3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.12×** | +21.2 | 0e+00 | 47/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +16.0 | 0e+00 | 43/48 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **2.19×** | +15.7 | 0e+00 | 48/49 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.14×** | +15.2 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.85×** | +12.3 | 1e-32 | 48/48 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +11.9 | 2e-30 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +11.4 | 2e-28 | 46/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.97×** | +11.4 | 5e-28 | 45/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +8.4 | 4e-15 | 38/48 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.3 | 1e-11 | 33/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +7.3 | 2e-11 | 36/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.7 | 1e-09 | 33/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +6.4 | 5e-09 | 38/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +5.4 | 3e-06 | 32/48 (RKO, SW48, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 31/48 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.003 | 38/48 (LoVo, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.004 | 30/47 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 27/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -11.4 | 3e-27 | 46/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -10.4 | 5e-23 | 45/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.625×** | -9.4 | 1e-18 | 46/48 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -7.1 | 1e-10 | 36/45 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.779×** | -5.0 | 7e-05 | 29/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.781×** | -4.7 | 2e-04 | 29/47 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.785×** | -4.6 | 3e-04 | 26/44 (SW48, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.808×** | -4.2 | 0.002 | 25/49 (AsPC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.8 | 0.009 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | **0.830×** | -3.7 | 0.011 | 24/48 (SW 1088, AsPC-1, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.029 | 31/48 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.041 | 28/48 (RPMI-7951, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.063 | 16/48 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.808× | -3.0 | 0.11 | 25/48 (RPMI-7951, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 277 | 16 (8 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.29× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.492× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 388 | 7 | 8 (4 ⚠) | [[Selinexor (drug)]] 5 µM 2.24× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.295× (z -22.1) |
| [[SW48 (line)]] | wt | 335 | 10 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.441× (z -9.7) |
| [[LS 180 (line)]] | wt | 278 | 13 (4 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.70× (z +20.0) | — |
| [[SW1417 (line)]] | alt | 506 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +22.0) | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.9) |
| [[A549 (line)]] | wt | 279 | 11 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +24.3) | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 295 | 7 (1 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.11× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.361× (z -13.7) |
| [[KATO III (line)]] | alt | 329 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.31× (z +20.9) | — |
| [[PANC-1 (line)]] | alt | 373 | 9 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.450× (z -14.2) |
| [[LoVo (line)]] | wt | 236 | 11 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.46× (z +16.7) | — |
| [[SW480 (line)]] | alt | 363 | 10 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.22× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.628× (z -8.7) |
| [[HT-29 (line)]] | alt | 302 | 10 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.65× (z +19.7) | — |
| [[HOP62 (line)]] | alt | 280 | 7 | 2 | [[Selinexor (drug)]] 5 µM 2.37× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.437× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 310 | 5 | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.85× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -13.1) |
| [[A-172 (line)]] | wt | 332 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.418× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 524 | 3 | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.65× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.394× (z -13.9) |
| [[A-427 (line)]] | wt | 563 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.390× (z -15.3) |
| [[C-33 A (line)]] | alt | 404 | 4 | 3 | [[Selinexor (drug)]] 5 µM 2.33× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.399× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 264 | 7 | 0 | [[Selinexor (drug)]] 5 µM 2.85× (z +21.4) | — |
| [[NCI-H2347 (line)]] | alt | 294 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +22.9) | [[Panobinostat (drug)]] 5 µM 0.582× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 391 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.445× (z -11.6) |
| [[C32 (line)]] | wt | 347 | 3 | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.03× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 214 | 6 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.26× (z +13.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 2.11× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 342 | 6 | 0 | [[Selinexor (drug)]] 5 µM 2.50× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 525 | 3 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 3.85× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.368× (z -18.4) |
| [[H4 (line)]] | wt | 271 | 5 | 0 | [[Selinexor (drug)]] 5 µM 2.63× (z +14.1) | — |
| [[J82 (line)]] | alt | 286 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.510× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 202 | 5 | 0 | [[Selinexor (drug)]] 5 µM 3.11× (z +19.8) | — |
| [[NCI-H1792 (line)]] | alt | 265 | 5 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.76× (z +22.6) | — |
| [[NCI-H2030 (line)]] | alt | 265 | 3 | 2 | [[Selinexor (drug)]] 5 µM 2.57× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.470× (z -11.5) |
| [[RKO (line)]] | wt | 292 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +26.2) | — |
| [[SNU-423 (line)]] | alt | 248 | 5 | 0 | [[Selinexor (drug)]] 5 µM 1.93× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 303 | 5 | 0 | [[Selinexor (drug)]] 5 µM 2.30× (z +14.0) | — |
| [[HepG2_C3A (line)]] | wt | 187 | 4 | 0 | [[Selinexor (drug)]] 5 µM 3.03× (z +15.7) | — |
| [[Hs 766T (line)]] | wt | 305 | 3 | 1 | [[Selinexor (drug)]] 5 µM 1.89× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.507× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 230 | 4 | 0 | [[Selinexor (drug)]] 5 µM 2.51× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 418 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[BT-474 (line)]] | alt | 215 | 2 | 1 | [[Selinexor (drug)]] 5 µM 1.96× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 257 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 234 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 408 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.36× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 336 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.59× (z +14.5) | — |
| [[A498 (line)]] | wt | 352 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 525 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[CHP-212 (line)]] | wt | 346 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.9) | — |
| [[NCI-H661 (line)]] | alt | 561 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -10.1) |
| [[NCI-H2122 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 303 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF138]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SLC44A2]] | +0.64 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[SLC16A14]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PHYH]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[HSPA4L]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[USP24]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CHST3]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[EPDR1]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.55 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[ZNF442]] | +0.54 | +0.30 / +0.60 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 | pathway: Regulation of mRNA stability by proteins that bind AU-rich elements |
| [[WNT2B]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 | pathway: Signaling by WNT |
| [[UCHL3]] | -0.55 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PLEKHM1P1]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MARCHF3]] | -0.54 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.54 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[WIPI1]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ENTPD7]] | -0.53 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[BET1L]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[FRMD8]] | -0.52 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ATG101]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[DAP]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCHF3]] | B | MARCHF3 activity lowers XPO1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 1.66× higher at baseline in the lines without MARCHF3 | 0.006 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[ZSCAN12]] | B | ZSCAN12 activity raises XPO1's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.07× lower at baseline in the lines without ZSCAN12 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises XPO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF618]] | B | ZNF618 activity raises XPO1's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without ZNF618 | 0.085 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.8, 23.6); signed map (8.2, -33.6). **Vector** length 139, 55.3% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +21.9 | +21.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +14.8 | +15.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +10.2 | +15.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +7.8 | +12.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.0 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.0 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +1.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +4.5 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.8 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.1 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.3 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | exportin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,476,032-61,538,741 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRM1, CRM-1, emb |
| Gene groups (HGNC) | Exportins |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 59 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; Maturation of hRSV A proteins; NPAS4 regulates expression of target genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O14980](https://www.uniprot.org/uniprotkb/O14980) (Exportin-1):

> Mediates the nuclear export of cellular proteins (cargos) bearing a leucine-rich nuclear export signal (NES) and of RNAs. In the nucleus, in association with RANBP3, binds cooperatively to the NES on its target protein and to the GTPase RAN in its active GTP-bound form (Ran-GTP). Docking of this complex to the nuclear pore complex (NPC) is mediated through binding to nucleoporins. Upon transit of a nuclear export complex into the cytoplasm, disassembling of the complex and hydrolysis of Ran-GTP …

**Summary**, from NCBI Gene [7514](https://www.ncbi.nlm.nih.gov/gene/7514):

> This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:12825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12825) · Entrez [7514](https://www.ncbi.nlm.nih.gov/gene/7514) · UniProt [O14980](https://www.uniprot.org/uniprotkb/O14980) · Ensembl [ENSG00000082898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082898)

## Data

Gene col 1357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1357); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1357]; `tensor/DDL_lfc|DDL_z.npy` [1357]; `embed/gene_vectors.npy` [1357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1357 or target_col == 1357). Every well: [[XPO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
