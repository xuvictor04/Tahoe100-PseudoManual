---
symbol: "U2AF2"
type: "gene"
col: 725
ensembl_id: "ENSG00000063244"
name: "U2 small nuclear RNA auxiliary factor 2"
location: "19q13.42"
module: 126
arm: "+"
pooled_cpm: 56.94
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# U2AF2

*U2 small nuclear RNA auxiliary factor 2* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +14.0, q 8e-42, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.90× (z +10.9, q 1e-25, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.408× (z -13.8, q 1e-40, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP13A1]] (+0.82, fdr 7e-06), [[MTA2]] (+0.80, fdr 7e-06), [[SRSF1]] (+0.78, fdr 1e-05); moves opposite to [[POLR2J]] (-0.73, fdr 4e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[TMEM191A-1]] (-0.71, fdr 1e-04), [[ATP5MJ]] (-0.70, fdr 5e-05), [[TMEM256]] (-0.70, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +14.0 | 8e-42 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +13.2 | 2e-37 | 41/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +11.1 | 3e-26 | 38/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.90×** | +10.9 | 1e-25 | 46/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +9.3 | 2e-18 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.75×** | +8.1 | 4e-14 | 41/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +7.7 | 1e-12 | 41/48 (SW480, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 3e-06 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.3 | 6e-06 | 30/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 4e-05 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.8 | 8e-05 | 28/36 (A-172, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.7 | 1e-04 | 29/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.34×** | +4.4 | 4e-04 | 29/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.20×** | +4.0 | 0.002 | 21/48 (A498, A549, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.005 | 23/47 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.034 | 21/48 (C32, A-427, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.037 | 23/47 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 725.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -13.8 | 1e-40 | 46/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.406×** | -13.5 | 6e-39 | 47/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.432×** | -12.9 | 5e-36 | 46/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.485×** | -11.1 | 1e-26 | 45/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.446×** | -6.5 | 9e-09 | 41/48 (HT-29, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.755×** | -6.1 | 9e-08 | 39/48 (SW 900, HT-29, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -5.6 | 1e-06 | 30/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.703×** | -5.4 | 4e-06 | 29/48 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -4.0 | 0.004 | 30/48 (HCT15, SW1417, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.015 | 25/47 (NCI-H23, SW480, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.793×** | -3.6 | 0.018 | 24/48 (HEC-1-A, BT-474, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.804×** | -3.3 | 0.050 | 19/48 (A498, HOP62, …) | rises with dose | position effect removed |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.1 | 0.078 | 10/48 (HS-578T, SHP-77, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.820×** | -3.1 | 0.088 | 17/47 (NCI-H23, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.3 | 8 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.51× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.392× (z -11.3) |
| [[PANC-1 (line)]] | alt | 95.1 | 5 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.295× (z -14.9) |
| [[LoVo (line)]] | wt | 46.5 | 6 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.325× (z -12.1) |
| [[A498 (line)]] | wt | 65.9 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.7) ⚠ cell-cycle shift, explains ~57% of this change | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -10.3) |
| [[HT-29 (line)]] | alt | 98.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -10.8) |
| [[J82 (line)]] | alt | 66.7 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -12.4) |
| [[A549 (line)]] | wt | 48.4 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.22× (z +8.5) | — |
| [[KATO III (line)]] | alt | 70.2 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 37.0 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.372× (z -9.8) |
| [[A-172 (line)]] | wt | 42.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.383× (z -8.7) |
| [[HOP62 (line)]] | alt | 36.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +13.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 49.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.365× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.318× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 63.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.4) |
| [[A-427 (line)]] | wt | 51.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.12× (z +11.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.353× (z -8.9) |
| [[C-33 A (line)]] | alt | 112 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -9.9) |
| [[HS-578T (line)]] | alt | 46.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.293× (z -10.6) |
| [[LS 180 (line)]] | wt | 50.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.270× (z -10.8) |
| [[SNU-423 (line)]] | alt | 34.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 64.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.377× (z -10.3) |
| [[Hs 766T (line)]] | wt | 33.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.326× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 38.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.389× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 38.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 68.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.350× (z -9.6) |
| [[SW1417 (line)]] | alt | 72.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.60× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 45.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -10.1) |
| [[BT-474 (line)]] | alt | 63.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -8.8) |
| [[C32 (line)]] | wt | 41.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 10.1× (z +8.9) | — |
| [[H4 (line)]] | wt | 78.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.248× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 46.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP13A1]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[MTA2]] | +0.80 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[SRSF1]] | +0.78 | +0.56 / +0.80 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 998 |
| [[SSU72]] | +0.77 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[VPS52]] | +0.75 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ATN1]] | +0.75 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[HNRNPL]] | +0.74 | +0.63 / +0.69 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 946 |
| [[UBQLN4]] | +0.73 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[EWSR1]] | +0.72 | +0.54 / +0.73 | both halves | 1e-05 | same gene group; STRING 623 |
| [[LY6G5B]] | +0.71 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[DHFR]] | +0.71 | +0.44 / +0.76 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 9 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J]] ⚠ | -0.73 | -0.42 / -0.71 | both halves | 4e-05 | pathway: Dengue Virus-Host Interactions; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM191A-1]] | -0.71 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[ATP5MJ]] | -0.70 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[TMEM256]] | -0.70 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[LAMTOR5]] | -0.70 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[RNF114]] | -0.70 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[C4orf48]] | -0.70 | -0.39 / -0.70 | both halves | 5e-05 |  |
| [[CAMLG]] | -0.68 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[MRPL41]] ⚠ | -0.68 | -0.30 / -0.64 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.67 | -0.43 / -0.70 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PITPNA-AS1]] | -0.67 | -0.33 / -0.69 | both halves | 1e-04 |  |
| [[RPL18]] ⚠ | -0.66 | -0.35 / -0.70 | both halves | 1e-04 | pathway: Dengue Virus-Host Interactions; ⚠ in the vector space only through flagged drug-doses |
| [[LIN7B]] | -0.66 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[RNF181]] | -0.66 | -0.36 / -0.70 | both halves | 9e-05 |  |
| [[CDKN2D]] | -0.66 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[COMMD6]] | -0.66 | -0.42 / -0.70 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.4, -24.8); signed map (-12.5, -34.8). **Vector** length 111, 34.8% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.0 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.9 | -12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -13.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.3 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -13.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -6.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | +0.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | U2 small nuclear RNA auxiliary factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,654,146-55,674,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U2AF65 |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal A complex; Spliceosomal E complex |
| Reactome | 13 pathways, smallest: Protein hydroxylation; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation; Transport of Mature mRNA derived from an Intron-Containing Transcript |
| Matched by | ensembl_id |

**Function**, from UniProt [P26368](https://www.uniprot.org/uniprotkb/P26368) (Splicing factor U2AF 65 kDa subunit):

> Plays a role in pre-mRNA splicing and 3'-end processing. By recruiting PRPF19 and the PRP19C/Prp19 complex/NTC/Nineteen complex to the RNA polymerase II C-terminal domain (CTD), and thereby pre-mRNA, may couple transcription to splicing. Induces cardiac troponin-T (TNNT2) pre-mRNA exon inclusion in muscle. Regulates the TNNT2 exon 5 inclusion through competition with MBNL1. Binds preferentially to a single-stranded structure within the polypyrimidine tract of TNNT2 intron 4 during spliceosome …

**Summary**, from NCBI Gene [11338](https://www.ncbi.nlm.nih.gov/gene/11338):

> U2 auxiliary factor (U2AF), comprised of a large and a small subunit, is a non-snRNP protein required for the binding of U2 snRNP to the pre-mRNA branch site. This gene encodes the U2AF large subunit which contains a sequence-specific RNA-binding region with 3 RNA recognition motifs and an Arg/Ser-rich domain necessary for splicing. The large subunit binds to the polypyrimidine tract of introns early during spliceosome assembly. Multiple transcript variants have been detected for this gene, but …

**Accessions** — [HGNC:23156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23156) · Entrez [11338](https://www.ncbi.nlm.nih.gov/gene/11338) · UniProt [P26368](https://www.uniprot.org/uniprotkb/P26368) · Ensembl [ENSG00000063244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063244)

## Data

Gene col 725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 725); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 725]; `tensor/DDL_lfc|DDL_z.npy` [725]; `embed/gene_vectors.npy` [725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 725 or target_col == 725). Every well: [[U2AF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/U2AF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
