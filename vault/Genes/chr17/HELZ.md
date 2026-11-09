---
symbol: "HELZ"
type: "gene"
col: 12563
ensembl_id: "ENSG00000198265"
name: "helicase with zinc finger"
location: "17q24.2"
module: 164
arm: "+"
pooled_cpm: 351.94
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# HELZ

*helicase with zinc finger* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.23× (z +10.4, q 1e-22, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.341× (z -14.3, q 8e-44, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.626× (z -6.5, q 9e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBPJ]] (+0.74, fdr 7e-06), [[LNPK]] (+0.71, fdr 7e-06), [[PEX3]] (+0.71, fdr 7e-06); moves opposite to [[POGK]] (-0.62, fdr 1e-05), [[COA7]] (-0.60, fdr 1e-05), [[DNAH14]] (-0.57, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MLLT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.23×** | +10.4 | 1e-22 | 49/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.93×** | +7.8 | 2e-12 | 47/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +5.7 | 2e-06 | 33/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.0 | 0.008 | 28/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.012 | 24/48 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.049 | 26/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.050 | 38/48 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.14 | 32/48 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.26× | +3.0 | 0.16 | 36/48 (A-172, PANC-1, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.341×** | -14.3 | 8e-44 | 43/44 (CFPAC-1, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.374×** | -13.6 | 9e-40 | 49/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.455×** | -10.5 | 2e-23 | 46/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.527×** | -8.2 | 3e-14 | 41/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.626×** | -6.5 | 9e-09 | 36/48 (CFPAC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.649×** | -6.0 | 2e-07 | 45/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.641×** | -5.9 | 2e-07 | 35/47 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.671×** | -5.3 | 8e-06 | 42/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.717×** | -4.6 | 2e-04 | 43/48 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -4.5 | 5e-04 | 29/48 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.743×** | -4.1 | 0.002 | 31/48 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.745×** | -4.1 | 0.002 | 32/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -3.4 | 0.027 | 20/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.785×** | -3.4 | 0.032 | 33/48 (SW 900, RKO, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.845× | -3.3 | 0.035 | 18/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.802×** | -3.1 | 0.077 | 30/48 (CFPAC-1, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 647 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -10.3) |
| [[SW480 (line)]] | alt | 325 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 191 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 208 | 1 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.418× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 605 | 2 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 4.90× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 274 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.06× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 361 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.40× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.409× (z -10.6) |
| [[HT-29 (line)]] | alt | 390 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.11× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -12.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 301 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 235 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.521× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 361 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.62× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 430 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 436 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 413 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 357 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.12× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 279 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.66× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -15.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 149 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.00× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 479 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -13.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 232 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 369 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.08× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 341 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 439 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.29× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 558 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 977 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -18.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 469 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.27× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 273 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.46× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 356 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -10.5) ⚠ toxic |
| [[RKO (line)]] | wt | 285 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.81× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 335 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -12.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 413 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.55× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 460 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 218 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 345 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 432 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 539 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 526 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 278 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 304 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.14× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -13.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 340 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.11× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -17.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 347 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.480× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 338 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.221× (z -13.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 265 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -9.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 267 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.97× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 361 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 356 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPJ]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[LNPK]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[PEX3]] | +0.71 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ZNF395]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZNF654]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[USP37]] | +0.67 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MXI1]] | +0.67 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[HERC3]] | +0.66 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[SMAP2]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[MANBA]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ATF2]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[COA7]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[DNAH14]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PUS1]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.56 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[CUEDC1]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MGA]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.55 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PTPN21]] | -0.53 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[DDX10]] | -0.53 | -0.61 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLLT3]] | B | MLLT3 activity raises HELZ's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without MLLT3 | 0.045 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -18.0); signed map (-37.5, 22.8). **Vector** length 122, 56.8% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.7 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.4 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.3 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +0.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.3 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | -0.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.6 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.8 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -6.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.1 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | helicase with zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:67,070,444-67,245,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0054, HUMORF5, DHRC |
| Gene groups (HGNC) | Zinc fingers CCCH-type; UPF1 like RNA helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [P42694](https://www.uniprot.org/uniprotkb/P42694) (ATP-dependent RNA helicase with zinc finger domain):

> ATP-dependent RNA helicase that promotes degradation of mRNAs via its association with the CCR4-NOT deadenylase complex, leading to deadenylation, decapping, and subsequent degradation of target mRNAs. Can repress translation independently of mRNA decay in a manner dependent on both the CCR4-NOT complex and the helicase DDX6. Involved in promoting cell proliferation, translation initiation, and ribosomal protein S6 (RPS6) phosphorylation.

**Summary**, from NCBI Gene [9931](https://www.ncbi.nlm.nih.gov/gene/9931):

> HELZ is a member of the superfamily I class of RNA helicases. RNA helicases alter the conformation of RNA by unwinding double-stranded regions, thereby altering the biologic activity of the RNA molecule and regulating access to other proteins (Wagner et al., 1999 [PubMed 10471385]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16878) · Entrez [9931](https://www.ncbi.nlm.nih.gov/gene/9931) · UniProt [P42694](https://www.uniprot.org/uniprotkb/P42694) · Ensembl [ENSG00000198265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198265)

## Data

Gene col 12563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12563); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12563]; `tensor/DDL_lfc|DDL_z.npy` [12563]; `embed/gene_vectors.npy` [12563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12563 or target_col == 12563). Every well: [[HELZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HELZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
