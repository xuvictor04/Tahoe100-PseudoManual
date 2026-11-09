---
symbol: "AP2A1"
type: "gene"
col: 12311
ensembl_id: "ENSG00000196961"
name: "adaptor related protein complex 2 subunit alpha 1"
location: "19q13.33"
module: 42
arm: "+"
pooled_cpm: 42.16
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# AP2A1

*adaptor related protein complex 2 subunit alpha 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.99× (z +14.6, q 3e-45, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.550× (z -12.6, q 7e-34, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKACA]] (+0.71, fdr 7e-06), [[P3H1]] (+0.68, fdr 7e-06), [[ADIPOR1]] (+0.67, fdr 1e-05); moves opposite to [[METTL18]] (-0.71, fdr 7e-06), [[RPL7L1]] (-0.67, fdr 9e-06), [[RPP25L]] (-0.66, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +14.6 | 3e-45 | 43/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +14.4 | 1e-44 | 44/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +14.1 | 1e-42 | 43/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +12.9 | 1e-35 | 40/46 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.54×** | +8.7 | 3e-16 | 25/40 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +7.9 | 3e-13 | 31/48 (SW480, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.6 | 2e-12 | 31/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.41×** | +6.7 | 1e-09 | 30/43 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +6.6 | 3e-09 | 31/48 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.6 | 3e-09 | 35/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 26/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 4e-06 | 26/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +4.7 | 1e-04 | 21/48 (A-427, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 19/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.18× | +3.4 | 0.027 | 17/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.055 | 6/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -12.6 | 7e-34 | 41/48 (HS-578T, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -11.7 | 2e-29 | 44/48 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -10.5 | 1e-23 | 42/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -9.1 | 1e-17 | 31/48 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.679×** | -8.2 | 3e-14 | 33/48 (HS-578T, A549, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -7.0 | 2e-10 | 31/48 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sulfisoxazole (drug)]] 5 µM |  | **0.822×** | -5.4 | 5e-06 | 23/48 (A498, HT-29, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.767×** | -5.2 | 2e-05 | 26/47 (HT-29, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.788×** | -5.1 | 3e-05 | 23/48 (RPMI-7951, SW 1271, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.807×** | -4.5 | 3e-04 | 25/48 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.859× | -4.3 | 7e-04 | 19/48 (A498, NCI-H2030, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.808×** | -4.3 | 9e-04 | 20/47 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.866× | -4.1 | 0.002 | 15/48 (A498, AsPC-1, …) | rises with dose | position effect removed |
| [[Nafamostat (mesylate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.075 | 5/48 (NCI-H2030, SW 1088, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.760×** | -3.0 | 0.091 | 13/48 (COLO 205, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 53.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.8) |
| [[KATO III (line)]] | alt | 35.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.29× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 37.6 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.97× (z +11.9) | — |
| [[SW480 (line)]] | alt | 38.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +13.2) | — |
| [[A498 (line)]] | wt | 71.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 33.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -15.3) |
| [[LoVo (line)]] | wt | 22.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 62.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[A-172 (line)]] | wt | 57.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.0) |
| [[HT-29 (line)]] | alt | 55.7 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[J82 (line)]] | alt | 62.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 53.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -12.0) |
| [[LS 180 (line)]] | wt | 32.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 54.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.1) |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.3) |
| [[AN3 CA (line)]] | alt | 50.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -8.9) |
| [[C32 (line)]] | wt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.6) |
| [[H4 (line)]] | wt | 62.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.253× (z -9.5) |
| [[HOP62 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -10.6) |
| [[Hs 766T (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.177× (z -11.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 58.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 36.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.453× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -9.6) |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.3) |
| [[SW48 (line)]] | wt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -9.0) |
| [[A-427 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACA]] | +0.71 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Neuronal System |
| [[P3H1]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.67 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[SAP130]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[GGCX]] | +0.66 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SETD3]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[GNB2]] | +0.65 | +0.71 / +0.44 | both halves | 3e-05 | pathway: Beta-catenin independent WNT signaling |
| [[MLEC]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.64 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[IGSF8]] | +0.63 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | -0.71 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[RPL7L1]] | -0.67 | -0.69 / -0.57 | both halves | 9e-06 |  |
| [[RPP25L]] | -0.66 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.66 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.65 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.65 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[ASNSD1]] | -0.64 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.63 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ZBED9]] | -0.62 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.62 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[SRSF8]] | -0.62 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[KICS2]] | -0.62 | -0.69 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.6, -18.2); signed map (-48.0, -5.6). **Vector** length 118, 31.2% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.1 | +14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +14.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +14.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.0 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.7 | +1.8 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.7 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.3 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.7 | -10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.7 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.8 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 2 subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,767,001-49,807,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CLAPA1, ADTAA |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 2; MicroRNA protein coding host genes |
| Reactome | 43 pathways, smallest: Nef Mediated CD8 Down-regulation; Nef Mediated CD4 Down-regulation; WNT5A-dependent internalization of FZD2, FZD5 and ROR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O95782](https://www.uniprot.org/uniprotkb/O95782) (AP-2 complex subunit alpha-1):

> Component of the adaptor protein complex 2 (AP-2). Adaptor protein complexes function in protein transport via transport vesicles in different membrane traffic pathways. Adaptor protein complexes are vesicle coat components and appear to be involved in cargo selection and vesicle formation. AP-2 is involved in clathrin-dependent endocytosis in which cargo proteins are incorporated into vesicles surrounded by clathrin (clathrin-coated vesicles, CCVs) which are destined for fusion with the early …

**Summary**, from NCBI Gene [160](https://www.ncbi.nlm.nih.gov/gene/160):

> This gene encodes the alpha 1 adaptin subunit of the adaptor protein 2 (AP-2) complex found in clathrin coated vesicles. The AP-2 complex is a heterotetramer consisting of two large adaptins (alpha or beta), a medium adaptin (mu), and a small adaptin (sigma). The complex is part of the protein coat on the cytoplasmic face of coated vesicles which links clathrin to receptors in vesicles. Alternative splicing of this gene results in two transcript variants encoding two different isoforms. A third …

**Accessions** — [HGNC:561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:561) · Entrez [160](https://www.ncbi.nlm.nih.gov/gene/160) · UniProt [O95782](https://www.uniprot.org/uniprotkb/O95782) · Ensembl [ENSG00000196961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196961)

## Data

Gene col 12311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12311); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12311]; `tensor/DDL_lfc|DDL_z.npy` [12311]; `embed/gene_vectors.npy` [12311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12311 or target_col == 12311). Every well: [[AP2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
