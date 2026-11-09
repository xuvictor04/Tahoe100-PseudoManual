---
symbol: "PLEKHA5"
type: "gene"
col: 583
ensembl_id: "ENSG00000052126"
name: "pleckstrin homology domain containing A5"
location: "12p12.3"
module: 222
arm: "+"
pooled_cpm: 257.02
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# PLEKHA5

*pleckstrin homology domain containing A5* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +11.0, q 2e-25, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -17.0, q 0e+00, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND5B]] (+0.72, fdr 7e-06), [[DENND1B]] (+0.59, fdr 1e-05), [[RAPGEF2]] (+0.56, fdr 1e-05); moves opposite to [[SNAPC4]] (-0.54, fdr 5e-05), [[ARHGAP1]] (-0.53, fdr 3e-05), [[WDR37]] (-0.52, fdr 4e-05).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RALGPS2]] → it (grade B ⚠); 8 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +11.0 | 2e-25 | 34/44 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +9.5 | 4e-19 | 35/45 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +5.8 | 2e-06 | 30/43 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.20× | +4.0 | 0.008 | 18/46 (NCI-H1792, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +3.9 | 0.011 | 20/44 (NCI-H1792, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.011 | 13/45 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.011 | 19/43 (NCI-H1792, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.011 | 16/44 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.011 | 18/44 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.013 | 13/44 (NCI-H1792, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.6 | 0.017 | 11/44 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.5 | 0.018 | 11/44 (NCI-H1792, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.023 | 16/44 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.028 | 17/46 (NCI-H1792, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.16× | +3.3 | 0.031 | 15/43 (HOP62, KATO III, …) | rises with dose |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.15× | +3.1 | 0.081 | 7/43 (A498, HepG2/C3A, …) | top dose only |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.087 | 10/45 (NCI-H1792, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.087 | 5/45 (NCI-H2347, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -17.0 | 0e+00 | 37/44 (Panc 03.27, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.522×** | -15.1 | 0e+00 | 37/44 (Panc 03.27, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.508×** | -14.5 | 1e-45 | 35/41 (Panc 03.27, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.534×** | -14.2 | 8e-44 | 38/45 (NCI-H23, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.559×** | -13.0 | 2e-36 | 32/40 (LOX-IMVI, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.672×** | -12.7 | 7e-35 | 28/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.352×** | -12.6 | 9e-35 | 41/45 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -11.7 | 1e-29 | 29/45 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.614×** | -11.3 | 1e-27 | 33/44 (SW480, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -7.5 | 3e-12 | 29/44 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.737×** | -7.1 | 8e-11 | 32/44 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.744×** | -6.8 | 4e-10 | 27/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -5.8 | 3e-07 | 23/44 (LoVo, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.787×** | -5.5 | 1e-06 | 29/44 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.781×** | -5.5 | 1e-06 | 25/46 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.655×** | -5.1 | 1e-05 | 28/44 (NCI-H460, H4, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.670×** | -4.9 | 4e-05 | 26/44 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.772×** | -4.3 | 6e-04 | 25/44 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.711×** | -4.1 | 0.001 | 23/44 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.004 | 19/44 (LOX-IMVI, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.740×** | -3.6 | 0.007 | 19/43 (RPMI-7951, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.855× | -3.6 | 0.007 | 18/45 (Panc 03.27, KATO III, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.850× | -3.5 | 0.009 | 14/44 (LoVo, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 1,203 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -25.4) |
| [[NCI-H1573 (line)]] | alt | 172 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -24.4) |
| [[Panc 03.27 (line)]] | alt | 568 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -22.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.254× (z -21.3) |
| [[HEC-1-A (line)]] | alt | 302 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -15.7) |
| [[LoVo (line)]] | wt | 327 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -28.5) |
| [[NCI-H1792 (line)]] | alt | 285 | 4 (2 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.59× (z +17.1) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 2.15× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -29.3) |
| [[KATO III (line)]] | alt | 343 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -18.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.270× (z -16.8) |
| [[CHP-212 (line)]] | wt | 512 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -13.6) |
| [[HOP62 (line)]] | alt | 303 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.6) |
| [[LS 180 (line)]] | wt | 202 | 2 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.97× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.517× (z -9.6) |
| [[SW480 (line)]] | alt | 218 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -19.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.389× (z -17.4) |
| [[A498 (line)]] | wt | 237 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -13.7) |
| [[COLO 205 (line)]] | alt | 270 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.1) |
| [[J82 (line)]] | alt | 171 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.59× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 207 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.498× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 859 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -17.0) |
| [[RKO (line)]] | wt | 131 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.20× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 186 | 3 (1 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -14.2) |
| [[A-172 (line)]] | wt | 95.7 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 1.84× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.8) |
| [[HT-29 (line)]] | alt | 229 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 337 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 293 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 149 | 3 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 203 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.51× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -13.4) |
| [[A-427 (line)]] | wt | 311 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 67.3 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.52× (z +14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.60× (z +12.0) | — |
| [[SW48 (line)]] | wt | 174 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -9.4) |
| [[A549 (line)]] | wt | 137 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.1) |
| [[BT-474 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.385× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.430× (z -10.0) |
| [[SNU-423 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -10.5) |
| [[SW 900 (line)]] | alt | 619 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -12.7) |
| [[C-33 A (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -9.9) |
| [[HS-578T (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -8.9) |
| [[NCI-H596 (line)]] | alt | 299 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.199× (z -10.1) |
| [[PANC-1 (line)]] | alt | 65.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.636× (z -8.6) |
| [[SHP-77 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.487× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 46.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5B]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[DENND1B]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RAPGEF2]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[RUFY3]] | +0.55 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[SCN8A]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MARK1]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MAGI3]] | +0.54 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[SIK3]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[PDE5A]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NEO1]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[BEND7]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[GKAP1]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC4]] | -0.54 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ARHGAP1]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[WDR37]] | -0.52 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[TRMT44]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RUSF1]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ZNF17]] | -0.50 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[B4GALT7]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DDX41]] | -0.49 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ZNF550]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[DDX49]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[FOXRED1]] | -0.48 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[MAN1B1]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity raises PLEKHA5's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 3.12× lower at baseline in the lines without RALGPS2 | 0.086 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | PLEKHA5 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express PLEKHA5 (4) vs lines expressing it (44) | the lines without PLEKHA5: 0.56× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| [[ARAP2]] | C | PLEKHA5 activity raises ARAP2's level | lines that do not express PLEKHA5 (4) vs lines expressing it (46) | 6.34× lower at baseline in the lines without PLEKHA5 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| [[RALGPS2]] | C | PLEKHA5 activity raises RALGPS2's level | lines that do not express PLEKHA5 (4) vs lines expressing it (46) | 3.93× lower at baseline in the lines without PLEKHA5 | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | PLEKHA5 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express PLEKHA5 (4) vs lines expressing it (44) | the lines without PLEKHA5: 0.76× the cells of the other lines | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | PLEKHA5 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express PLEKHA5 (4) vs lines expressing it (44) | the lines without PLEKHA5: 0.29× the cells of the other lines | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| cells under [[Harringtonine (drug)]] 0.5 µM | C | PLEKHA5 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express PLEKHA5 (4) vs lines expressing it (44) | the lines without PLEKHA5: 0.43× the cells of the other lines | 0.067 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| [[GNAI1]] | C | PLEKHA5 activity raises GNAI1's level | lines that do not express PLEKHA5 (4) vs lines expressing it (46) | 4.53× lower at baseline in the lines without PLEKHA5 | 0.070 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| cells under [[Allantoin (drug)]] 0.5 µM | C | PLEKHA5 activity raises the cells' numbers under Allantoin 0.5 µM (protects the cells) | lines that do not express PLEKHA5 (4) vs lines expressing it (44) | the lines without PLEKHA5: 0.82× the cells of the other lines | 0.097 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 13.5); signed map (10.7, -5.2). **Vector** length 117, 36.8% of its response variance represented; |z| ≥ 3 in 1,472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.1 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.1 | +9.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | -0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +3.9 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -12.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -15.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -17.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -7.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:19,129,669-19,376,400 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEPP2, KIAA1686, FLJ10667 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

UniProt [Q9HAU0](https://www.uniprot.org/uniprotkb/Q9HAU0) carries no function annotation.

**Summary**, from NCBI Gene [54477](https://www.ncbi.nlm.nih.gov/gene/54477):

> Predicted to enable phosphatidylinositol phosphate binding activity. Predicted to act upstream of or within reproductive system development. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30036) · Entrez [54477](https://www.ncbi.nlm.nih.gov/gene/54477) · UniProt [Q9HAU0](https://www.uniprot.org/uniprotkb/Q9HAU0) · Ensembl [ENSG00000052126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052126)

## Data

Gene col 583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 583); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 583]; `tensor/DDL_lfc|DDL_z.npy` [583]; `embed/gene_vectors.npy` [583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 583 or target_col == 583). Every well: [[PLEKHA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
