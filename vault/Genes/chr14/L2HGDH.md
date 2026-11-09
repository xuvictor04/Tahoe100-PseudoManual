---
symbol: "L2HGDH"
type: "gene"
col: 1498
ensembl_id: "ENSG00000087299"
name: "L-2-hydroxyglutarate dehydrogenase"
location: "14q21.3"
module: 10
arm: "-"
pooled_cpm: 44.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# L2HGDH

*L-2-hydroxyglutarate dehydrogenase* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.93× (z +31.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.527× (z -18.1, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HACE1]] (+0.73, fdr 7e-06), [[ATG4C]] (+0.70, fdr 1e-05), [[RPA1]] (+0.69, fdr 1e-05); moves opposite to [[PCNX4-DT]] (-0.74, fdr 1e-05), [[ARRDC3-AS1]] (-0.73, fdr 2e-05), [[PPP3CB-AS1]] (-0.72, fdr 1e-05).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02257]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.93×** | +31.7 | 0e+00 | 48/48 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.90×** | +31.4 | 0e+00 | 48/48 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.51×** | +27.2 | 0e+00 | 47/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +17.9 | 0e+00 | 45/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +14.4 | 4e-45 | 40/47 (Panc 03.27, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.29×** | +11.8 | 5e-30 | 42/48 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +10.4 | 3e-23 | 30/48 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.27×** | +7.0 | 2e-10 | 24/47 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +6.7 | 1e-09 | 22/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.003 | 11/48 (COLO 205, J82, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.004 | 6/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.007 | 4/48 (HT-29, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.012 | 9/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.6 | 0.012 | 11/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.023 | 6/47 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.062 | 4/48 (SW 900, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.11× | +3.1 | 0.062 | 12/48 (HOP62, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.527×** | -18.1 | 0e+00 | 39/48 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.649×** | -18.0 | 0e+00 | 34/47 (RKO, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.601×** | -15.0 | 0e+00 | 36/47 (A-427, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.623×** | -13.9 | 6e-42 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -12.4 | 4e-33 | 34/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.697×** | -10.6 | 2e-24 | 32/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -10.3 | 3e-23 | 4/49 (RPMI-7951, C32, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -8.9 | 4e-17 | 30/49 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.763×** | -8.0 | 1e-13 | 23/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.747×** | -7.9 | 1e-13 | 25/42 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.772×** | -7.6 | 1e-12 | 22/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.775×** | -7.5 | 3e-12 | 25/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -6.6 | 2e-09 | 26/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.807×** | -6.3 | 1e-08 | 22/47 (A-172, A498, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.813×** | -6.1 | 5e-08 | 19/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.808×** | -6.0 | 6e-08 | 22/47 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.866× | -6.0 | 8e-08 | 13/48 (LS 180, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.657×** | -6.0 | 8e-08 | 19/48 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.833×** | -5.4 | 2e-06 | 17/47 (LS 180, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.822×** | -5.3 | 3e-06 | 15/47 (RKO, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.839× | -5.1 | 6e-06 | 16/47 (SK-MEL-2, LoVo, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.9 | 3 | 7 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.04× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.355× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.394× (z -11.5) |
| [[A549 (line)]] | wt | 46.9 | 3 | 5 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.66× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0772× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.288× (z -12.8) |
| [[RKO (line)]] | wt | 51.3 | 2 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.249× (z -11.3) |
| [[PANC-1 (line)]] | alt | 44.8 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.423× (z -11.1) |
| [[A498 (line)]] | wt | 20.6 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.255× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 53.8 | 2 | 4 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.34× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -13.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 111 | 2 | 4 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.26× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.8 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +9.6) | [[Harringtonine (drug)]] 0.5 µM 0.116× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 28.0 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 4.32× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 62.3 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.55× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 61.8 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.360× (z -9.4) |
| [[SW1417 (line)]] | alt | 57.2 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -14.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 69.8 | 2 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.85× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.527× (z -9.6) |
| [[HOP62 (line)]] | alt | 25.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 40.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 47.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +12.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 53.8 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.44× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.8) | [[vincristine (drug)]] 0.5 µM 0.231× (z -8.5) |
| [[A-427 (line)]] | wt | 52.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.0878× (z -26.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 27.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +12.6) | — |
| [[J82 (line)]] | alt | 41.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +10.9) | — |
| [[KATO III (line)]] | alt | 41.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 45.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 75.6 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.200× (z -14.2) |
| [[HCT15 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 25.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.69× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 49.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 65.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RPMI-7951 (line)]] | alt | 23.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.25× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.215× (z -8.7) |
| [[SHP-77 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 39.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0963× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 31.4 | 1 | 1 | [[Belinostat (drug)]] 5 µM 2.98× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.236× (z -11.1) |
| [[SW48 (line)]] | wt | 66.6 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.267× (z -9.3) |
| [[BT-474 (line)]] | alt | 57.6 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 2.77× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 50.0 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.91× (z +8.9) | — |
| [[H4 (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.91× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | +0.73 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.70 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[RPA1]] | +0.69 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CHEK2]] | +0.69 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.68 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CKLF]] | +0.67 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PHKA2]] | +0.67 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SCAI]] | +0.66 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SHQ1]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SMYD4]] | +0.66 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PPAT]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[RADX]] | +0.65 | +0.40 / +0.60 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*69 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | -0.74 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | -0.73 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[PPP3CB-AS1]] | -0.72 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[DNAH12]] | -0.72 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | -0.71 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[TMEM202-AS1]] | -0.71 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NEB]] | -0.71 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | -0.70 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.70 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[KRCC1]] | -0.70 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[CFAP70]] | -0.70 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[LINC00571]] | -0.69 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02257]] | B | LINC02257 activity strengthens L2HGDH's drug response | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257 respond 1.05× as strongly (z diff -0.21); strongest at Panobinostat 0.5 µM: 2.00x vs 2.81x (z diff +1.5) | 0.039 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SMCO2]] | B | SMCO2 activity lowers L2HGDH's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.17× higher at baseline in the lines without SMCO2 | 0.048 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[RGS20]] | B | RGS20 activity lowers L2HGDH's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.41× higher at baseline in the lines without RGS20 | 0.073 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[DSCC1]] | C | DSCC1 activity raises L2HGDH's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without DSCC1 | 0.016 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.8, 12.6); signed map (-39.8, -12.3). **Vector** length 108, 29.2% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.1 | +31.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +14.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +17.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +27.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +31.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +11.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -8.8 | -15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -8.2 | -18.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.5 | -12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | L-2-hydroxyglutarate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:50,237,563-50,312,229 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12618; previously C14orf160 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Flavoproteins |
| Reactome | 2 pathways, smallest: Interconversion of 2-oxoglutarate and 2-hydroxyglutarate; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9P8](https://www.uniprot.org/uniprotkb/Q9H9P8) (L-2-hydroxyglutarate dehydrogenase, mitochondrial):

> Catalyzes the oxidation of L-2-hydroxyglutarate to 2-oxoglutarate in the mitochondrial matrix. L-2-hydroxyglutarate is a physiological metabolite produced in presence of an elevated NADH/NAD(+) ratio in the mitochondrial matrix: it competes with 2-oxoglutarate and inhibits the activity of some 2-oxoglutarate-dependent dioxygenases, such as KDM4A, KDM4B and KDM4C histone demethylases, thereby acting as an epigenetic regulator. Acts as a negative regulator of macrophage activation by mediating …

**Summary**, from NCBI Gene [79944](https://www.ncbi.nlm.nih.gov/gene/79944):

> This gene encodes L-2-hydroxyglutarate dehydrogenase, a FAD-dependent enzyme that oxidizes L-2-hydroxyglutarate to alpha-ketoglutarate in a variety of mammalian tissues. Mutations in this gene cause L-2-hydroxyglutaric aciduria, a rare autosomal recessive neurometabolic disorder resulting in moderate to severe cognitive disability. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20499) · Entrez [79944](https://www.ncbi.nlm.nih.gov/gene/79944) · UniProt [Q9H9P8](https://www.uniprot.org/uniprotkb/Q9H9P8) · Ensembl [ENSG00000087299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087299)

## Data

Gene col 1498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1498); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1498]; `tensor/DDL_lfc|DDL_z.npy` [1498]; `embed/gene_vectors.npy` [1498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1498 or target_col == 1498). Every well: [[L2HGDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L2HGDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
