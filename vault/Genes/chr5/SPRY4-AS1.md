---
symbol: "SPRY4-AS1"
type: "gene"
col: 13785
ensembl_id: "ENSG00000231185"
name: "SPRY4 antisense RNA 1"
location: "5q31.3"
module: 92
arm: "+"
pooled_cpm: 120.58
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 61
n_dd_up_clean: 7
n_dd_down_clean: 46
in_vector_space: true
direction_upstream: 5
direction_downstream: 16
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SPRY4-AS1

*SPRY4 antisense RNA 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +12.6, q 1e-33, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 61 drug-doses (15 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.122× (z -23.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01844]] (+0.85, fdr 7e-06, ⚠ same locus), [[SPRY4]] (+0.83, fdr 7e-06, ⚠ same locus), [[ITGB5]] (+0.78, fdr 7e-06), [[SPRED2]] (+0.77, fdr 7e-06), [[HMGA2]] (+0.76, fdr 7e-06); moves opposite to [[GBP2]] (-0.61, fdr 7e-06).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01844]] → it (grade B ⚠); 16 go from it, the strongest it → [[ARHGAP31]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +12.6 | 1e-33 | 35/46 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +8.2 | 9e-14 | 36/45 (HS-578T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.8 | 1e-06 | 28/47 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.016 | 24/45 (H4, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.024 | 29/45 (C32, A549, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.024 | 28/46 (SW1417, HepG2/C3A, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.084 | 22/45 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.36×** | +3.2 | 0.084 | 23/45 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.10 | 24/45 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.51× | +3.1 | 0.12 | 18/45 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.14 | 19/45 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 61 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.122×** | -23.0 | 0e+00 | 47/47 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.153×** | -18.7 | 0e+00 | 44/44 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.280×** | -18.6 | 0e+00 | 42/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.242×** | -18.4 | 0e+00 | 45/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | **0.188×** | -18.3 | 0e+00 | 46/46 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.173×** | -18.1 | 0e+00 | 46/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.210×** | -15.5 | 0e+00 | 44/45 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.254×** | -14.2 | 9e-44 | 44/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.317×** | -13.9 | 2e-42 | 41/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.281×** | -13.1 | 2e-37 | 41/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.266×** | -12.7 | 5e-35 | 43/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; position correction uncertain | **0.304×** | -12.3 | 5e-33 | 44/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.332×** | -11.0 | 3e-26 | 39/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.354×** | -10.7 | 3e-25 | 42/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.345×** | -10.4 | 1e-23 | 41/45 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.155×** | -10.1 | 3e-22 | 44/44 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.388×** | -9.8 | 4e-21 | 37/45 (A-172, HOP62, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.167×** | -9.7 | 1e-20 | 43/45 (HEC-1-A, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.404×** | -9.4 | 2e-19 | 42/45 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 149 | 0 | 39 (10 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0665× (z -25.7) |
| [[HEC-1-A (line)]] | alt | 319 | 0 | 37 (7 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0407× (z -29.3) |
| [[MIA PaCa-2 (line)]] | alt | 929 | 0 | 33 (9 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.223× (z -39.1) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0951× (z -18.9) |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 33 (9 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0381× (z -28.3) |
| [[HepG2_C3A (line)]] | wt | 395 | 0 | 32 (10 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0463× (z -23.5) |
| [[SW480 (line)]] | alt | 128 | 0 | 31 (6 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0845× (z -24.4) ⚠ position correction uncertain · without an alert: [[Trametinib (drug)]] 5 µM 0.0775× (z -23.0) |
| [[RKO (line)]] | wt | 251 | 0 | 27 (8 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0307× (z -27.0) |
| [[HOP62 (line)]] | alt | 190 | 0 | 21 (6 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0469× (z -18.7) |
| [[C32 (line)]] | wt | 191 | 0 | 19 (3 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0659× (z -20.1) ⚠ position correction uncertain · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0587× (z -17.8) |
| [[HCT15 (line)]] | alt | 114 | 0 | 18 (5 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0546× (z -18.8) |
| [[A-172 (line)]] | wt | 202 | 0 | 17 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0437× (z -23.2) |
| [[Hs 766T (line)]] | wt | 67.2 | 1 | 16 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +13.4) | [[Trametinib (drug)]] 5 µM 0.112× (z -13.4) |
| [[LS 180 (line)]] | wt | 49.8 | 2 | 15 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 48.0 | 1 | 15 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +13.3) | [[Trametinib (drug)]] 5 µM 0.0932× (z -18.1) |
| [[A-427 (line)]] | wt | 187 | 0 | 15 (6 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.250× (z -14.6) |
| [[COLO 205 (line)]] | alt | 113 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -21.2) |
| [[H4 (line)]] | wt | 75.6 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0426× (z -16.2) |
| [[HT-29 (line)]] | alt | 60.7 | 1 | 14 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.5) | [[Trametinib (drug)]] 5 µM 0.0874× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 58.2 | 1 | 13 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -17.7) |
| [[A549 (line)]] | wt | 66.4 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -20.5) |
| [[LoVo (line)]] | wt | 44.6 | 1 | 12 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +16.3) | [[Trametinib (drug)]] 5 µM 0.165× (z -16.1) |
| [[SW 1271 (line)]] | alt | 200 | 0 | 12 (3 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0792× (z -12.6) ⚠ position correction uncertain · without an alert: [[Trametinib (drug)]] 5 µM 0.0762× (z -11.3) |
| [[C-33 A (line)]] | alt | 108 | 0 | 11 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0781× (z -15.0) |
| [[HS-578T (line)]] | alt | 51.5 | 2 | 9 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +12.0) | [[Trametinib (drug)]] 5 µM 0.110× (z -12.9) |
| [[J82 (line)]] | alt | 37.0 | 0 | 10 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.152× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 47.0 | 3 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +12.3) | [[Trametinib (drug)]] 0.5 µM 0.180× (z -11.9) |
| [[BT-474 (line)]] | alt | 54.9 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -10.5) ⚠ position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 39.5 | 1 | 8 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +13.1) | [[Binimetinib (drug)]] 5 µM 0.113× (z -13.1) ⚠ position correction uncertain · without an alert: [[Trametinib (drug)]] 5 µM 0.112× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 72.8 | 1 | 8 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.2) | [[Cobimetinib (drug)]] 5 µM 0.0698× (z -17.4) |
| [[Panc 03.27 (line)]] | alt | 37.8 | 1 | 8 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.6) | [[Cobimetinib (drug)]] 0.5 µM 0.0936× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 90.0 | 1 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.5) | [[Trametinib (drug)]] 5 µM 0.0674× (z -18.5) |
| [[A498 (line)]] | wt | 40.5 | 2 | 6 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -13.3) ⚠ toxic · without an alert: [[Trametinib (drug)]] 5 µM 0.179× (z -12.0) |
| [[SNU-1 (line)]] | wt | 178 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.8) |
| [[SW 900 (line)]] | alt | 48.6 | 1 | 7 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.1) | [[Trametinib (drug)]] 5 µM 0.133× (z -12.1) |
| [[SW1417 (line)]] | alt | 91.2 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 42.6 | 2 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +14.7) | [[Ponatinib (drug)]] 5 µM 0.191× (z -9.9) |
| [[SW48 (line)]] | wt | 77.6 | 0 | 7 (3 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.0556× (z -17.1) ⚠ position correction uncertain · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0952× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 38.4 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +11.8) | [[Adagrasib (drug)]] 0.05 µM 0.481× (z -15.7) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.118× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 76.5 | 0 | 5 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.133× (z -11.3) |
| [[AN3 CA (line)]] | alt | 284 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0976× (z -12.7) |
| [[SNU-423 (line)]] | alt | 31.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.4) | [[Trametinib (drug)]] 5 µM 0.177× (z -9.3) |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.170× (z -9.0) |
| [[SW 1088 (line)]] | alt | 90.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0464× (z -11.1) |
| [[KATO III (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01844]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | ⚠ same locus (44.2 kb, same strand: neighbours can correlate without regulation) |
| [[SPRY4]] | +0.83 | +0.82 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ITGB5]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SPRED2]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ETV4]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[SPRED1]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[NPAS2]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[AGO2]] | +0.73 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[PITPNC1]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[NT5E]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.70 | +0.71 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP2]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01844]] | B | LINC01844 activity raises SPRY4-AS1's level | lines that do not express LINC01844 (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without LINC01844 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287712, ADGRG2, ENSG00000291283; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity lowers SPRY4-AS1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.96× higher at baseline in the lines without DUSP4 | 0.058 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[TOP2A]] | B | TOP2A activity lowers SPRY4-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises SPRY4-AS1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.8% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GPRC5B]] | B | GPRC5B activity lowers SPRY4-AS1's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 1.88× higher at baseline in the lines without GPRC5B | 0.060 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP31]] | C | SPRY4-AS1 activity raises ARHGAP31's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 5.32× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[FHOD3]] | C | SPRY4-AS1 activity raises FHOD3's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 4.81× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[ELK3]] | C | SPRY4-AS1 activity raises ELK3's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 3.50× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[NPAS2]] | C | SPRY4-AS1 activity raises NPAS2's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 3.31× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[PHLDA1]] | C | SPRY4-AS1 activity raises PHLDA1's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[SLC25A45]] | C | SPRY4-AS1 activity raises SLC25A45's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.00× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[TRIOBP]] | C | SPRY4-AS1 activity raises TRIOBP's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |
| [[ACTN1]] | C | SPRY4-AS1 activity raises ACTN1's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without SPRY4-AS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |
| [[IVNS1ABP]] | C | SPRY4-AS1 activity lowers IVNS1ABP's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 1.41× higher at baseline in the lines without SPRY4-AS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |
| [[BCAR3]] | C | SPRY4-AS1 activity raises BCAR3's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 3.34× lower at baseline in the lines without SPRY4-AS1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |
| [[OSBPL5]] | C | SPRY4-AS1 activity raises OSBPL5's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without SPRY4-AS1 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent |
| [[COL13A1]] | C | SPRY4-AS1 activity raises COL13A1's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 5.94× lower at baseline in the lines without SPRY4-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.0, 6.8); signed map (8.7, 47.2). **Vector** length 155, 61.8% of its response variance represented; |z| ≥ 3 in 2,418 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.70 to 8); *KRAS signaling up* (hallmark, mean cos +0.55 to 7); *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +12.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.7 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | -0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +4.2 | +2.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | +3.1 | +0.7 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -17.1 | -18.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -17.0 | -23.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -15.3 | -18.7 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | -15.0 | -18.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -14.6 | -15.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -14.4 | -18.1 |

## What is on record

|  |  |
|---|---|
| Name | SPRY4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q31.3 — chr5:142,325,209-142,672,001 (+) |
| Ensembl biotype | lncRNA |
| Also known as | THCAT68, AC005592.2; previously LINC01844 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53465) · Entrez [101926941](https://www.ncbi.nlm.nih.gov/gene/101926941) · Ensembl [ENSG00000231185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231185)

## Data

Gene col 13785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13785); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13785]; `tensor/DDL_lfc|DDL_z.npy` [13785]; `embed/gene_vectors.npy` [13785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13785 or target_col == 13785). Every well: [[SPRY4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRY4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
