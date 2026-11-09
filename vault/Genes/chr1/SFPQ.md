---
symbol: "SFPQ"
type: "gene"
col: 3805
ensembl_id: "ENSG00000116560"
name: "splicing factor proline and glutamine rich"
location: "1p34.3"
module: 3
arm: "-"
pooled_cpm: 258.99
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SFPQ

*splicing factor proline and glutamine rich* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.59× (z +41.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.696× (z -9.8, q 5e-20, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF6]] (+0.74, fdr 7e-06), [[SRSF3]] (+0.73, fdr 7e-06), [[EWSR1]] (+0.73, fdr 1e-05); moves opposite to [[MIR4458HG]] (-0.71, fdr 1e-05), [[RNF181]] (-0.71, fdr 4e-05), [[RABAC1]] (-0.69, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.59×** | +41.3 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.75×** | +25.3 | 0e+00 | 48/48 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.46×** | +22.8 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.52×** | +17.7 | 0e+00 | 48/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +17.1 | 0e+00 | 49/49 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +15.8 | 0e+00 | 43/44 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +15.2 | 0e+00 | 45/45 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +14.4 | 4e-45 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +12.5 | 8e-34 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +10.4 | 2e-23 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +8.4 | 2e-15 | 45/49 (NCI-H1573, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +8.2 | 1e-14 | 32/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.9 | 1e-13 | 43/47 (Hs 766T, COLO 205, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +7.8 | 2e-13 | 44/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +7.1 | 5e-11 | 42/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.4 | 2e-06 | 30/48 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.001 | 25/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.002 | 26/48 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.006 | 31/49 (HCT15, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.008 | 24/48 (HEC-1-A, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -9.8 | 5e-20 | 40/49 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -6.8 | 4e-09 | 39/48 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.1 | 7e-05 | 28/50 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -4.8 | 2e-04 | 27/48 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.845× | -4.6 | 5e-04 | 18/48 (J82, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.796×** | -4.4 | 0.001 | 31/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.804×** | -4.2 | 0.002 | 28/48 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.810×** | -4.0 | 0.005 | 34/49 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.825×** | -3.7 | 0.014 | 24/48 (COLO 205, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.726×** | -3.2 | 0.074 | 27/49 (RKO, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.078 | 17/48 (RKO, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.839× | -3.1 | 0.078 | 18/47 (RKO, A498, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.845× | -3.1 | 0.078 | 22/47 (COLO 205, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.846× | -3.1 | 0.078 | 23/48 (BT-474, C32, …) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 0.853× | -3.0 | 0.087 | 10/48 (SW48, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 276 | 14 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +39.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -11.1) |
| [[PANC-1 (line)]] | alt | 248 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +39.5) | — |
| [[SW480 (line)]] | alt | 354 | 10 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +22.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -16.0) |
| [[A-172 (line)]] | wt | 131 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +28.3) | — |
| [[HS-578T (line)]] | alt | 224 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +37.8) | — |
| [[KATO III (line)]] | alt | 194 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +28.5) | — |
| [[NCI-H1573 (line)]] | alt | 257 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +37.2) | — |
| [[AsPC-1 (line)]] | alt | 193 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +37.1) | — |
| [[HEC-1-A (line)]] | alt | 252 | 10 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +31.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 229 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.9) | — |
| [[HOP62 (line)]] | alt | 297 | 9 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +32.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.8) |
| [[LoVo (line)]] | wt | 325 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +35.8) | — |
| [[LS 180 (line)]] | wt | 244 | 10 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +25.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 189 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +34.9) | — |
| [[Hs 766T (line)]] | wt | 184 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +30.2) | — |
| [[hTERT-HPNE (line)]] | wt | 224 | 9 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +38.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 313 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +31.2) | — |
| [[SW 900 (line)]] | alt | 217 | 9 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +26.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.0) |
| [[HT-29 (line)]] | alt | 237 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +29.4) | — |
| [[RPMI-7951 (line)]] | alt | 254 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +28.3) | — |
| [[SNU-1 (line)]] | wt | 275 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +22.6) | — |
| [[HCT15 (line)]] | alt | 370 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 332 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +29.0) | — |
| [[SW1417 (line)]] | alt | 214 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +23.9) | — |
| [[A498 (line)]] | wt | 192 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +37.3) | — |
| [[A549 (line)]] | wt | 171 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +28.6) | — |
| [[BT-474 (line)]] | alt | 253 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.4) | — |
| [[CFPAC-1 (line)]] | alt | 266 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +29.1) | — |
| [[J82 (line)]] | alt | 288 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +25.4) | — |
| [[NCI-H23 (line)]] | alt | 392 | 5 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +26.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 183 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +24.5) | — |
| [[SNU-423 (line)]] | alt | 197 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +32.9) | — |
| [[SW48 (line)]] | wt | 385 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +18.9) | — |
| [[C-33 A (line)]] | alt | 338 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -8.6) |
| [[COLO 205 (line)]] | alt | 179 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +36.1) | — |
| [[H4 (line)]] | wt | 233 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.1) | — |
| [[RKO (line)]] | wt | 357 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.7) |
| [[SHP-77 (line)]] | alt | 280 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 234 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +33.2) | — |
| [[A-427 (line)]] | wt | 284 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.93× (z +12.3) | — |
| [[C32 (line)]] | wt | 234 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +28.8) | — |
| [[NCI-H2030 (line)]] | alt | 352 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +25.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 230 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +21.4) | — |
| [[CHP-212 (line)]] | wt | 177 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 243 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +14.6) | — |
| [[AN3 CA (line)]] | alt | 405 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) | — |
| [[SW 1271 (line)]] | alt | 203 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +13.3) | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 280 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF6]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 694 |
| [[SRSF3]] | +0.73 | +0.67 / +0.79 | both halves | 7e-06 | same gene group; STRING 881 |
| [[EWSR1]] | +0.73 | +0.53 / +0.77 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 883 |
| [[SRSF1]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 872 |
| [[HNRNPM]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | same gene group; STRING 968 |
| [[TRIM44]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[LINC00641]] | +0.68 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[YWHAE]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[DDX3X]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 | STRING 662 |
| [[MAPRE1]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[SDCBP2-AS1]] | +0.66 | +0.44 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4458HG]] | -0.71 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[RNF181]] | -0.71 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[RABAC1]] | -0.69 | -0.50 / -0.73 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.69 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[NUDT22]] | -0.69 | -0.30 / -0.75 | both halves | 2e-04 |  |
| [[COX5B]] | -0.68 | -0.46 / -0.69 | both halves | 2e-05 |  |
| [[CNOT8]] | -0.68 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[VKORC1]] | -0.67 | -0.57 / -0.71 | both halves | 9e-06 |  |
| [[MALSU1]] | -0.67 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.67 | -0.46 / -0.69 | both halves | 2e-05 |  |
| [[MPG]] | -0.67 | -0.46 / -0.75 | both halves | 3e-05 |  |
| [[LAMTOR2]] | -0.67 | -0.46 / -0.70 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SFPQ's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.7, -24.3); signed map (14.6, -38.6). **Vector** length 130, 52.6% of its response variance represented; |z| ≥ 3 in 1,464 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.61 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.62 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.62 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +15.4 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +14.8 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +14.7 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +25.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +41.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.3 | +7.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -6.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -5.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.8 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor proline and glutamine rich |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,176,378-35,193,446 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSF, PPP1R140 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; RNA binding motif containing |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 7 pathways, smallest: PTK6 Regulates Proteins Involved in RNA Processing; Suppression of apoptosis; Response of Mtb to phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P23246](https://www.uniprot.org/uniprotkb/P23246) (Splicing factor, proline- and glutamine-rich):

> DNA- and RNA binding protein, involved in several nuclear processes. Essential pre-mRNA splicing factor required early in spliceosome formation and for splicing catalytic step II, probably as a heteromer with NONO. Binds to pre-mRNA in spliceosome C complex, and specifically binds to intronic polypyrimidine tracts. Involved in regulation of signal-induced alternative splicing. During splicing of PTPRC/CD45, a phosphorylated form is sequestered by THRAP3 from the pre-mRNA in resting T-cells; …

**Summary**, from NCBI Gene [6421](https://www.ncbi.nlm.nih.gov/gene/6421):

> Enables DNA binding activity; histone deacetylase binding activity; and protein homodimerization activity. Involved in several processes, including alternative mRNA splicing, via spliceosome; positive regulation of oxidative stress-induced intrinsic apoptotic signaling pathway; and regulation of transcription by RNA polymerase II. Acts upstream of or within double-strand break repair via homologous recombination. Located in chromatin; nuclear matrix; and paraspeckles. [provided by Alliance of …

**Accessions** — [HGNC:10774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10774) · Entrez [6421](https://www.ncbi.nlm.nih.gov/gene/6421) · UniProt [P23246](https://www.uniprot.org/uniprotkb/P23246) · Ensembl [ENSG00000116560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116560)

## Data

Gene col 3805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3805); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3805]; `tensor/DDL_lfc|DDL_z.npy` [3805]; `embed/gene_vectors.npy` [3805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3805 or target_col == 3805). Every well: [[SFPQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFPQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
