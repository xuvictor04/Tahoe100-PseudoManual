---
symbol: "IMMP2L"
type: "gene"
col: 11589
ensembl_id: "ENSG00000184903"
name: "inner mitochondrial membrane peptidase subunit 2"
location: "7q31.1"
module: 200
arm: "+"
pooled_cpm: 687.59
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 35
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# IMMP2L

*inner mitochondrial membrane peptidase subunit 2* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.36× (z +3.8, q 0.048, up in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (C32 3.29×, SK-MEL-2 2.51×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 1.94×; ⚠ cell-cycle shift, explains ~70% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 2.28×).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.245× (z -18.2, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.361× (z -13.2, q 2e-37, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC4]] (+0.72, fdr 7e-06), [[FHIT]] (+0.71, fdr 7e-06), [[TBC1D5]] (+0.67, fdr 7e-06); moves opposite to [[KMT5C]] (-0.57, fdr 1e-05), [[SDHAP1]] (-0.56, fdr 3e-05), [[OSBPL2]] (-0.54, fdr 3e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PRKN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11589.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (C32 3.29×, SK-MEL-2 2.51×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 1.94×; ⚠ cell-cycle shift, explains ~70% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 2.28×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.048 | 34/47 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.048 | 36/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.31× | +3.4 | 0.14 | 30/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.27× | +3.2 | 0.23 | 31/48 (NCI-H1573, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.245×** | -18.2 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.261×** | -16.7 | 0e+00 | 47/47 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.276×** | -16.7 | 0e+00 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.361×** | -13.2 | 2e-37 | 48/48 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.367×** | -13.0 | 2e-36 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.148×** | -12.9 | 3e-36 | 45/49 (NCI-H23, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.390×** | -12.2 | 3e-32 | 46/48 (SNU-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.404×** | -11.7 | 7e-30 | 45/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.418×** | -11.3 | 1e-27 | 46/48 (HCT15, SNU-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.207×** | -10.7 | 9e-25 | 43/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.570×** | -10.3 | 5e-23 | 33/48 (NCI-H23, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.466×** | -9.5 | 1e-19 | 35/48 (A-427, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.489×** | -8.9 | 3e-17 | 40/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -8.1 | 2e-14 | 34/48 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -7.6 | 8e-13 | 35/49 (A549, SW48, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.562×** | -7.4 | 3e-12 | 43/48 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.565×** | -7.4 | 5e-12 | 39/48 (HCT15, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.502×** | -6.6 | 1e-09 | 45/48 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -6.5 | 2e-09 | 42/48 (J82, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.646×** | -5.6 | 4e-07 | 44/48 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Vilanterol (drug)]] 5 µM |  | **0.768×** | -4.8 | 3e-05 | 38/49 (NCI-H2347, A-172, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -4.5 | 1e-04 | 45/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -4.2 | 6e-04 | 37/48 (SW48, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.001 | 35/48 (H4, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.716×** | -4.0 | 0.001 | 38/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 1,377 | 0 | 20 (14 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0713× (z -26.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 728 | 0 | 20 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -23.4) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -17.0) |
| [[PANC-1 (line)]] | alt | 707 | 0 | 20 (14 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -27.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -16.3) |
| [[SNU-423 (line)]] | alt | 843 | 0 | 20 (14 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.231× (z -14.5) |
| [[C-33 A (line)]] | alt | 1,151 | 0 | 19 (13 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0754× (z -14.8) |
| [[A-427 (line)]] | wt | 735 | 0 | 18 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -21.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 1,242 | 0 | 18 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -30.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0499× (z -19.2) |
| [[SNU-1 (line)]] | wt | 1,140 | 0 | 18 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.197× (z -17.4) |
| [[HCT15 (line)]] | alt | 1,214 | 0 | 17 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -23.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.216× (z -17.1) |
| [[LoVo (line)]] | wt | 798 | 0 | 16 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -25.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.307× (z -14.3) |
| [[SW48 (line)]] | wt | 1,373 | 0 | 16 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -17.9) |
| [[AN3 CA (line)]] | alt | 1,532 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -17.7) |
| [[J82 (line)]] | alt | 461 | 0 | 15 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -12.9) |
| [[RKO (line)]] | wt | 1,116 | 0 | 15 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0384× (z -17.0) |
| [[A549 (line)]] | wt | 854 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -29.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -21.8) |
| [[SW480 (line)]] | alt | 580 | 0 | 14 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -22.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 448 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -18.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 641 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -22.1) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -13.4) |
| [[LS 180 (line)]] | wt | 422 | 0 | 12 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -18.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.109× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 701 | 0 | 12 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0841× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 739 | 0 | 11 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -16.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.2) |
| [[H4 (line)]] | wt | 455 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -9.0) |
| [[SW1417 (line)]] | alt | 834 | 0 | 10 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -16.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 432 | 1 | 8 (7 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.28× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -17.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.294× (z -13.8) |
| [[C32 (line)]] | wt | 3,113 | 1 (1 ⚠) | 7 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 3.29× (z +10.4) ⚠ cell-cycle shift, explains ~46% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -15.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -15.6) |
| [[KATO III (line)]] | alt | 458 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -13.9) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.138× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 493 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.128× (z -11.5) |
| [[COLO 205 (line)]] | alt | 303 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -9.8) |
| [[HOP62 (line)]] | alt | 361 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 529 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.246× (z -12.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.225× (z -9.9) |
| [[BT-474 (line)]] | alt | 382 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.323× (z -11.5) |
| [[Hs 766T (line)]] | wt | 326 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -14.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -9.3) |
| [[HT-29 (line)]] | alt | 648 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.5) ⚠ cell-cycle shift, explains ~70% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.237× (z -15.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.119× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 384 | 0 | 6 (5 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.109× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 2,314 | 1 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.51× (z +8.5) ⚠ cell-cycle shift, explains ~46% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -13.7) |
| [[SW 1271 (line)]] | alt | 778 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.232× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 335 | 1 (1 ⚠) | 4 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.23× (z +8.5) ⚠ unreliable plate only | [[Digitoxin (drug)]] 5 µM 0.315× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.185× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 383 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.170× (z -9.9) |
| [[CHP-212 (line)]] | wt | 382 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 367 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.124× (z -9.1) |
| [[SHP-77 (line)]] | alt | 241 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 388 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 309 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 335 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -9.9) |
| [[A498 (line)]] | wt | 540 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -16.7) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.110× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 2,303 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -10.9) |
| [[SW 1088 (line)]] | alt | 507 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2122 (line)]] | alt | 631 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 711 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[FHIT]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 | STRING 497 |
| [[TBC1D5]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[DIAPH2]] | +0.67 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[PHF14]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[UTP20]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SUMF1]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[AFG1L]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[DPH6]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[SUPT3H]] | +0.62 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[DOCK1]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SEMA6A-AS1]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT5C]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[OSBPL2]] | -0.54 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[MYPOP]] | -0.54 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SDHAP1-1]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[GDPD3]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[IL17RC]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[ANO8]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ANG]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[C2CD2L]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ADIPOR1]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SDHAP2]] | -0.52 | -0.60 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKN]] | B | PRKN activity raises IMMP2L's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without PRKN | 0.032 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[WWOX]] | B | WWOX activity raises IMMP2L's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without WWOX | 0.058 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[TENM3]] | B | TENM3 activity raises IMMP2L's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 1.44× lower at baseline in the lines without TENM3 | 0.071 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX |
| [[LINC01203]] | B | LINC01203 activity raises IMMP2L's level | lines that do not express LINC01203 (37) vs lines expressing it (13) | 1.42× lower at baseline in the lines without LINC01203 | 0.093 | ⚠ within organs, on part of the lines; also absent: SIM1, BMP10, LINC02643; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.907). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.6, 30.7); signed map (10.1, -12.6). **Vector** length 106, 52.2% of its response variance represented; |z| ≥ 3 in 1,816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.3 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.3 | -9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.1 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +5.9 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | -1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.0 | -16.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.4 | -6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -5.4 | -7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -13.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.7 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -10.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -3.1 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | inner mitochondrial membrane peptidase subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:110,662,644-111,562,517 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMP2; previously IMMP2L-IT1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T52](https://www.uniprot.org/uniprotkb/Q96T52) (Mitochondrial inner membrane protease subunit 2):

> Catalyzes the removal of transit peptides required for the targeting of proteins from the mitochondrial matrix, across the inner membrane, into the inter-membrane space. Known to process the nuclear encoded protein DIABLO.

**Summary**, from NCBI Gene [83943](https://www.ncbi.nlm.nih.gov/gene/83943):

> This gene encodes a protein involved in processing the signal peptide sequences used to direct mitochondrial proteins to the mitochondria. The encoded protein resides in the mitochondria and is one of the necessary proteins for the catalytic activity of the mitochondrial inner membrane peptidase (IMP) complex. Two variants that encode the same protein have been described for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:14598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14598) · Entrez [83943](https://www.ncbi.nlm.nih.gov/gene/83943) · UniProt [Q96T52](https://www.uniprot.org/uniprotkb/Q96T52) · Ensembl [ENSG00000184903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184903)

## Data

Gene col 11589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11589); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11589]; `tensor/DDL_lfc|DDL_z.npy` [11589]; `embed/gene_vectors.npy` [11589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11589 or target_col == 11589). Every well: [[IMMP2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMMP2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
