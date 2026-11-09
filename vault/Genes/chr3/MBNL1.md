---
symbol: "MBNL1"
type: "gene"
col: 7645
ensembl_id: "ENSG00000152601"
name: "muscleblind like splicing regulator 1"
location: "3q25.1-q25.2"
module: 217
arm: "+"
pooled_cpm: 470.61
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# MBNL1

*muscleblind like splicing regulator 1* — 3q25.1-q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.43× (z +9.4, q 3e-18, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.586× (z -14.0, q 7e-42, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTRN]] (+0.71, fdr 7e-06), [[NFIB]] (+0.64, fdr 1e-05), [[ALCAM]] (+0.63, fdr 1e-05); moves opposite to [[PEX16]] (-0.58, fdr 2e-05), [[MYO9B]] (-0.58, fdr 3e-05), [[RBCK1]] (-0.57, fdr 1e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PDLIM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +9.4 | 3e-18 | 35/48 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +8.5 | 8e-15 | 37/48 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +7.9 | 7e-13 | 33/47 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +7.4 | 2e-11 | 35/48 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.8 | 1e-09 | 31/48 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.8 | 5e-07 | 28/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +5.3 | 9e-06 | 24/48 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +5.0 | 4e-05 | 13/48 (LoVo, RPMI-7951, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +4.2 | 0.002 | 15/48 (HOP62, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.006 | 21/44 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.033 | 25/48 (C32, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.13× | +3.3 | 0.041 | 18/48 (H4, A498, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.041 | 5/48 (CFPAC-1, SHP-77, …) | all doses, flat | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.042 | 16/48 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.12× | +3.1 | 0.075 | 15/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -14.0 | 7e-42 | 46/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.649×** | -11.3 | 3e-27 | 43/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.686×** | -9.9 | 1e-20 | 35/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -8.7 | 5e-16 | 39/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.721×** | -8.6 | 1e-15 | 39/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.841× | -6.4 | 1e-08 | 24/49 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.802×** | -5.5 | 4e-06 | 27/48 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.864× | -5.4 | 5e-06 | 15/49 (A498, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.828×** | -4.9 | 5e-05 | 26/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.840× | -4.6 | 3e-04 | 21/48 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.843× | -4.5 | 4e-04 | 23/48 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.850× | -4.2 | 0.001 | 17/48 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.862× | -3.9 | 0.005 | 12/48 (LoVo, J82, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.828×** | -3.5 | 0.017 | 25/48 (HT-29, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.028 | 18/48 (MIA PaCa-2, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 474 | 6 (3 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.00× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.609× (z -10.1) |
| [[C32 (line)]] | wt | 385 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +11.7) | — |
| [[KATO III (line)]] | alt | 688 | 3 | 5 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.87× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 470 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -13.8) |
| [[HOP62 (line)]] | alt | 351 | 5 (4 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.36× (z +13.4) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.51× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.512× (z -10.8) |
| [[J82 (line)]] | alt | 599 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.620× (z -9.8) |
| [[HT-29 (line)]] | alt | 825 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -12.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.553× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 489 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -13.4) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.580× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 563 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +13.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.533× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 699 | 0 | 5 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.209× (z -16.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -14.9) |
| [[SW 900 (line)]] | alt | 588 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.426× (z -12.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.484× (z -11.2) |
| [[SW48 (line)]] | wt | 668 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -12.4) |
| [[SW480 (line)]] | alt | 423 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -24.4) |
| [[HEC-1-A (line)]] | alt | 426 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -18.6) |
| [[Hs 766T (line)]] | wt | 882 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 377 | 3 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.1) |
| [[LS 180 (line)]] | wt | 595 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 377 | 1 (1 ⚠) | 3 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.83× (z +11.0) ⚠ toxic | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.492× (z -13.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.557× (z -11.2) |
| [[A-427 (line)]] | wt | 471 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 1.65× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.628× (z -8.8) |
| [[A498 (line)]] | wt | 472 | 3 | 0 | [[Budesonide (drug)]] 5 µM 1.69× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 587 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -13.0) |
| [[HS-578T (line)]] | alt | 603 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.434× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 484 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.574× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 339 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.516× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 294 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.07× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.623× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 219 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 466 | 2 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.03× (z +10.5) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.551× (z -9.2) |
| [[BT-474 (line)]] | alt | 288 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.73× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 270 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.28× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 370 | 1 | 1 | [[Digitoxin (drug)]] 0.5 µM 1.79× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.567× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 526 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -15.1) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW1417 (line)]] | alt | 492 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.603× (z -10.8) |
| [[A549 (line)]] | wt | 341 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -11.2) ⚠ cell-cycle shift, explains ~10% of this change |
| [[CFPAC-1 (line)]] | alt | 468 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.584× (z -8.5) |
| [[HCT15 (line)]] | alt | 331 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 437 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.608× (z -11.7) |
| [[RKO (line)]] | wt | 339 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 549 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.545× (z -10.2) |
| [[SNU-1 (line)]] | wt | 510 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.484× (z -10.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 454 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 326 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 450 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 536 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 387 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 373 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 635 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTRN]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[NFIB]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ADGRG6]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DPYD]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ITGAV]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[RHOBTB3]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[PON2]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[NFIA]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SLC44A1]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LPP]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CAV1]] | +0.56 | +0.38 / +0.62 | both halves | 7e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX16]] | -0.58 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MYO9B]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RBCK1]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GPSM1]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF778]] | -0.56 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[C19orf25]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FAM131A]] | -0.55 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NAT9]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF251]] | -0.54 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ZBTB49]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[PPP2R5B]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ADPRM]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDLIM1]] | B | PDLIM1 activity raises MBNL1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without PDLIM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[EPS8]] | B | EPS8 activity raises MBNL1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without EPS8 | 0.045 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[SHANK1]] | B | SHANK1 activity lowers MBNL1's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 1.28× higher at baseline in the lines without SHANK1 | 0.064 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[KITLG]] | B | KITLG activity raises MBNL1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without KITLG | 0.080 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MBNL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLSCR4]] | B | PLSCR4 activity raises MBNL1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.24× lower at baseline in the lines without PLSCR4 | 0.099 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[ANKRD28]] | C | ANKRD28's natural level strengthens MBNL1's drug response | ANKRD28's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.35; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ATF7IP]] | C | ATF7IP's natural level strengthens MBNL1's drug response | ATF7IP's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.03; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, 15.6); signed map (47.4, 18.7). **Vector** length 152, 52.7% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +9.9 | +8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +9.4 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.1 | +7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.6 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | +6.0 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +5.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +5.0 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +4.9 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -8.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | -6.8 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -14.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.4 | -5.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -5.2 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | muscleblind like splicing regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1-q25.2 — chr3:152,243,828-152,465,780 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0428, EXP42, EXP40, EXP35, EXP; previously MBNL |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Muscleblind like splicing regulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR56](https://www.uniprot.org/uniprotkb/Q9NR56) (Muscleblind-like protein 1):

> Mediates pre-mRNA alternative splicing regulation. Acts either as activator or repressor of splicing on specific pre-mRNA targets. Inhibits cardiac troponin-T (TNNT2) pre-mRNA exon inclusion but induces insulin receptor (IR) pre-mRNA exon inclusion in muscle. Antagonizes the alternative splicing activity pattern of CELF proteins. Regulates the TNNT2 exon 5 skipping through competition with U2AF2. Inhibits the formation of the spliceosome A complex on intron 4 of TNNT2 pre-mRNA. Binds to the …

**Summary**, from NCBI Gene [4154](https://www.ncbi.nlm.nih.gov/gene/4154):

> This gene encodes a member of the muscleblind protein family which was initially described in Drosophila melanogaster. The encoded protein is a C3H-type zinc finger protein that modulates alternative splicing of pre-mRNAs. Muscleblind proteins bind specifically to expanded dsCUG RNA but not to normal size CUG repeats and may thereby play a role in the pathophysiology of myotonic dystrophy. Mice lacking this gene exhibited muscle abnormalities and cataracts. Several alternatively spliced …

**Accessions** — [HGNC:6923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6923) · Entrez [4154](https://www.ncbi.nlm.nih.gov/gene/4154) · UniProt [Q9NR56](https://www.uniprot.org/uniprotkb/Q9NR56) · Ensembl [ENSG00000152601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152601)

## Data

Gene col 7645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7645); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7645]; `tensor/DDL_lfc|DDL_z.npy` [7645]; `embed/gene_vectors.npy` [7645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7645 or target_col == 7645). Every well: [[MBNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
