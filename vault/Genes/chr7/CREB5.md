---
symbol: "CREB5"
type: "gene"
col: 7108
ensembl_id: "ENSG00000146592"
name: "cAMP responsive element binding protein 5"
location: "7p15.1-p14.3"
module: 125
arm: "+"
pooled_cpm: 130.2
n_lines_expressing: 35
n_dd_up: 67
n_dd_down: 30
n_dd_up_clean: 49
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# CREB5

*cAMP responsive element binding protein 5* — 7p15.1-p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 67 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 14.1× (z +65.6, q 0e+00, up in 32 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.697× (z -9.0, q 1e-16, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBILA]] (+0.65, fdr 7e-06), [[C3orf52]] (+0.64, fdr 1e-05), [[NAV3]] (+0.63, fdr 7e-06); moves opposite to [[KANSL2]] (-0.59, fdr 2e-05), [[PEX11B]] (-0.51, fdr 3e-05), [[MIRLET7BHG]] (-0.51, fdr 3e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TRAF1]] → it (grade B ⚠); 7 go from it, the strongest it → [[PRECSIT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 81 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 67 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **14.1×** | +65.6 | 0e+00 | 32/33 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.43×** | +35.2 | 0e+00 | 33/33 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **7.94×** | +34.9 | 0e+00 | 32/33 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **4.18×** | +25.1 | 0e+00 | 33/33 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **2.75×** | +25.0 | 0e+00 | 32/34 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.72×** | +24.7 | 0e+00 | 33/33 (KATO III, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **3.57×** | +22.3 | 0e+00 | 30/32 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | **3.51×** | +21.1 | 0e+00 | 31/32 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.12×** | +19.9 | 0e+00 | 29/33 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.74×** | +17.6 | 0e+00 | 30/33 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | **2.71×** | +17.5 | 0e+00 | 29/32 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **2.62×** | +16.8 | 0e+00 | 31/33 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ position correction uncertain | **2.45×** | +15.7 | 0e+00 | 27/33 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +13.7 | 3e-41 | 29/34 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **2.23×** | +13.5 | 4e-40 | 27/32 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.90×** | +11.2 | 1e-27 | 25/33 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +11.0 | 1e-26 | 27/33 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +10.4 | 8e-24 | 23/33 (KATO III, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +10.1 | 1e-22 | 24/33 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.76×** | +9.9 | 1e-21 | 26/32 (HEC-1-A, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **2.90×** | +9.7 | 5e-21 | 27/31 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -9.0 | 1e-16 | 24/34 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.446×** | -7.4 | 3e-11 | 24/32 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.759×** | -6.9 | 1e-09 | 19/33 (RKO, SHP-77, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -6.3 | 3e-08 | 21/33 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.788×** | -6.0 | 3e-07 | 14/33 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.727×** | -5.6 | 2e-06 | 18/33 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.729×** | -5.6 | 2e-06 | 18/33 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.738×** | -5.4 | 5e-06 | 17/33 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.741×** | -5.3 | 7e-06 | 19/33 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.749×** | -5.1 | 2e-05 | 21/33 (CHP-212, HEC-1-A, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.752×** | -5.0 | 2e-05 | 20/33 (A-172, SHP-77, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.753×** | -5.0 | 2e-05 | 18/33 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.0 | 3e-05 | 22/33 (NCI-H23, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.755×** | -5.0 | 3e-05 | 19/33 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.766×** | -4.7 | 9e-05 | 17/33 (HepG2/C3A, HS-578T, …) | all doses, flat |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.839× | -4.4 | 4e-04 | 14/34 (SHP-77, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.780×** | -4.4 | 4e-04 | 16/33 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 534 | 13 | 19 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +33.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -21.5) |
| [[NCI-H1792 (line)]] | alt | 193 | 10 (4 ⚠) | 12 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +33.3) | [[Clobetasol propionate (drug)]] 5 µM 0.277× (z -11.8) |
| [[KATO III (line)]] | alt | 152 | 20 (7 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.16× (z +19.9) | — |
| [[BT-474 (line)]] | alt | 264 | 17 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +17.7) | [[Ponatinib (drug)]] 5 µM 0.236× (z -9.1) |
| [[A-172 (line)]] | wt | 139 | 17 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 47.8× (z +38.1) | — |
| [[NCI-H1573 (line)]] | alt | 120 | 15 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +25.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.4) |
| [[A498 (line)]] | wt | 339 | 11 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +28.9) | [[Triamcinolone (drug)]] 5 µM 0.444× (z -10.1) |
| [[C32 (line)]] | wt | 41.0 | 14 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 51.8× (z +33.3) | — |
| [[LOX-IMVI (line)]] | wt | 184 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +40.5) | — |
| [[SW 900 (line)]] | alt | 89.9 | 13 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +27.2) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.301× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 55.9 | 13 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +26.4) | — |
| [[SHP-77 (line)]] | alt | 180 | 9 (3 ⚠) | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 4.25× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.5) |
| [[H4 (line)]] | wt | 305 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +28.7) | — |
| [[HEC-1-A (line)]] | alt | 510 | 5 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +20.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -22.4) |
| [[RKO (line)]] | wt | 560 | 7 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +24.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -18.2) |
| [[SK-MEL-2 (line)]] | alt | 73.7 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +24.5) | — |
| [[HT-29 (line)]] | alt | 43.0 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +24.7) | — |
| [[J82 (line)]] | alt | 73.3 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.2× (z +35.6) | — |
| [[NCI-H23 (line)]] | alt | 119 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +37.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.4) |
| [[PANC-1 (line)]] | alt | 47.4 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +28.4) | — |
| [[RPMI-7951 (line)]] | alt | 69.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.1× (z +28.9) | — |
| [[HOP62 (line)]] | alt | 65.0 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 65.9× (z +38.0) | — |
| [[HS-578T (line)]] | alt | 87.4 | 7 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +30.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.0) |
| [[SNU-1 (line)]] | wt | 188 | 8 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +33.6) | — |
| [[SNU-423 (line)]] | alt | 159 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +30.5) | — |
| [[A549 (line)]] | wt | 52.6 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +17.9) | — |
| [[SW48 (line)]] | wt | 240 | 5 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 47.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +30.0) | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +13.2) | — |
| [[CHP-212 (line)]] | wt | 74.4 | 4 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 8.90× (z +9.3) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 4.66× (z +9.3) | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.101× (z -10.6) |
| [[SW 1088 (line)]] | alt | 63.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.4× (z +11.2) | — |
| [[SW 1271 (line)]] | alt | 59.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +8.8) | — |
| [[A-427 (line)]] | wt | 9.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 29.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 22.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBILA]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[C3orf52]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[NAV3]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NGF]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CPA4]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[JUN]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 | STRING 971 |
| [[DUSP8]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[CXCL8]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.59 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL2]] | -0.59 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[PEX11B]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MIRLET7BHG]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NUP133]] | -0.50 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[BAG4]] | -0.49 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[UGP2]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RCOR3]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[COPS8]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAF1]] | B | TRAF1 activity raises CREB5's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.80× lower at baseline in the lines without TRAF1 | 0.024 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[KCNQ3]] | B | KCNQ3 activity raises CREB5's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 2.54× lower at baseline in the lines without KCNQ3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[F2RL2]] | B | F2RL2 activity raises CREB5's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without F2RL2 | 0.049 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[NR3C1]] | B | NR3C1 activity lowers CREB5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PLAAT1]] | B | PLAAT1 activity raises CREB5's level | lines that do not express PLAAT1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without PLAAT1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SDK1, PDGFD, SNCA |
| [[PRECSIT]] | B | PRECSIT activity raises CREB5's level | lines that do not express PRECSIT (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without PRECSIT | 0.078 | ⚠ within organs, on part of the lines; also absent: FAM3B, CFAP45, ENSG00000283511; maybe low, not absent |
| [[LINC01828]] | C | LINC01828 activity raises CREB5's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 2.97× lower at baseline in the lines without LINC01828 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRECSIT]] | B | CREB5 activity raises PRECSIT's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without CREB5 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[FHL2]] | B | CREB5 activity raises FHL2's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without CREB5 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[FLNC]] | B | CREB5 activity lowers FLNC's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.12× higher at baseline in the lines without CREB5 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[OSGIN1]] | B | CREB5 activity raises OSGIN1's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.81× lower at baseline in the lines without CREB5 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[PLAAT1]] | B | CREB5 activity raises PLAAT1's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without CREB5 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[TRAF1]] | B | CREB5 activity raises TRAF1's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 2.19× lower at baseline in the lines without CREB5 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[BAG4]] | B | CREB5 activity lowers BAG4's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.35× higher at baseline in the lines without CREB5 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, 17.8); signed map (32.2, 33.3). **Vector** length 127, 38.5% of its response variance represented; |z| ≥ 3 in 1,921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.9 | +24.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | +12.2 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +11.7 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.3 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +10.7 | +5.4 |
|  | [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | +9.6 | +21.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +9.1 | +25.0 |
|  | [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | +7.6 | +17.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +7.2 | +16.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -5.5 | -4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.2 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.9 | -5.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.8 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.1-p14.3 — chr7:28,299,321-28,825,894 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H_GS165L15.1, CRE-BPA |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Activating transcription factor 2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02930](https://www.uniprot.org/uniprotkb/Q02930) (Cyclic AMP-responsive element-binding protein 5):

> Binds to the cAMP response element and activates transcription.

**Summary**, from NCBI Gene [9586](https://www.ncbi.nlm.nih.gov/gene/9586):

> The product of this gene belongs to the CRE (cAMP response element)-binding protein family. Members of this family contain zinc-finger and bZIP DNA-binding domains. The encoded protein specifically binds to CRE as a homodimer or a heterodimer with c-Jun or CRE-BP1, and functions as a CRE-dependent trans-activator. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16844) · Entrez [9586](https://www.ncbi.nlm.nih.gov/gene/9586) · UniProt [Q02930](https://www.uniprot.org/uniprotkb/Q02930) · Ensembl [ENSG00000146592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146592)

## Data

Gene col 7108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7108); `tables/drug_effects.parquet` (119 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7108]; `tensor/DDL_lfc|DDL_z.npy` [7108]; `embed/gene_vectors.npy` [7108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7108 or target_col == 7108). Every well: [[CREB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
