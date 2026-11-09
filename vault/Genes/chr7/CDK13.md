---
symbol: "CDK13"
type: "gene"
col: 808
ensembl_id: "ENSG00000065883"
name: "cyclin dependent kinase 13"
location: "7p14.1"
module: 38
arm: "+"
pooled_cpm: 319.04
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CDK13

*cyclin dependent kinase 13* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.44× (z +4.1, q 0.022, up in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 1.95×; ⚠ cell-cycle shift, explains ~67% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (LoVo 3.53×); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 1.73×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 1.74×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -20.0, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.677× (z -9.2, q 2e-18, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOS1]] (+0.64, fdr 1e-05), [[UBAP1L]] (+0.63, fdr 8e-05), [[KIAA2026]] (+0.62, fdr 1e-05); moves opposite to [[C15orf39]] (-0.54, fdr 1e-04), [[ZBTB17]] (-0.52, fdr 8e-05), [[ZFP1]] (-0.51, fdr 5e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 1.95×; ⚠ cell-cycle shift, explains ~67% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (LoVo 3.53×); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 1.73×; ⚠ cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 1.74×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.022 | 35/49 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.6 | 0.083 | 19/48 (SW480, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.30× | +3.0 | 0.50 | 22/49 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.431×** | -20.0 | 0e+00 | 48/49 (H4, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.419×** | -19.8 | 0e+00 | 42/44 (Hs 766T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.482×** | -16.0 | 0e+00 | 44/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.527×** | -15.2 | 0e+00 | 46/48 (BT-474, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.542×** | -14.5 | 1e-45 | 46/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.558×** | -13.8 | 1e-41 | 47/48 (SW1417, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -9.2 | 2e-18 | 42/48 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.681×** | -8.8 | 1e-16 | 37/48 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -8.7 | 3e-16 | 36/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.805×** | -7.3 | 2e-11 | 28/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.745×** | -7.0 | 2e-10 | 31/48 (SK-MEL-2, LOX-IMVI, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -6.8 | 7e-10 | 34/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.752×** | -6.7 | 7e-10 | 40/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.759×** | -6.5 | 3e-09 | 30/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.762×** | -6.4 | 5e-09 | 36/48 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -5.3 | 4e-06 | 29/49 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.826×** | -4.5 | 2e-04 | 26/48 (SK-MEL-2, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.829×** | -4.4 | 3e-04 | 25/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.860× | -3.4 | 0.017 | 17/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.017 | 28/49 (SNU-423, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.017 | 24/48 (NCI-H1573, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.859× | -3.3 | 0.023 | 16/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.875× | -3.0 | 0.055 | 9/49 (A-172, Hs 766T, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 410 | 0 | 12 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.608× (z -8.5) |
| [[A549 (line)]] | wt | 255 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.560× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 412 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 419 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 451 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.616× (z -8.9) |
| [[A-172 (line)]] | wt | 333 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.459× (z -12.7) |
| [[HOP62 (line)]] | alt | 238 | 1 (1 ⚠) | 7 (7 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.67× (z +8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 421 | 2 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.53× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 426 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.482× (z -11.6) |
| [[BT-474 (line)]] | alt | 346 | 2 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.8) ⚠ cell-cycle shift, explains ~67% of this change | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -20.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 289 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.655× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 274 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 328 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.570× (z -9.5) |
| [[SW 900 (line)]] | alt | 345 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.451× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 359 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 550 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 414 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 241 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 237 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.408× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 338 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 224 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.596× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 304 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.569× (z -10.2) |
| [[A-427 (line)]] | wt | 233 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.478× (z -12.6) |
| [[COLO 205 (line)]] | alt | 229 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.475× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 298 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.491× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 348 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.557× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 191 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.467× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.484× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 280 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 432 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 293 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 496 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 297 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 233 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 260 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 274 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.453× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.504× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 330 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 329 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 305 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 246 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.490× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 284 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.572× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 252 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 285 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOS1]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[UBAP1L]] | +0.63 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[KIAA2026]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SOS2]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LINC02976]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MBTD1]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NBR2]] | +0.59 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[SPAG7]] | +0.58 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[CNPY2]] | +0.58 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ZNF131]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.58 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[AGO3]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf39]] | -0.54 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[ZBTB17]] | -0.52 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[ZFP1]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[DLD]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[OCRL]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TRIM68]] | -0.50 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[MOCS1]] | -0.50 | -0.21 / -0.55 | both halves | 6e-04 |  |
| [[ZMIZ2]] | -0.49 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[HPSE]] | -0.49 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | CDK13's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | CDK13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.482 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.9, 19.6); signed map (5.1, 1.9). **Vector** length 116, 44.4% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | -0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | -0.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.1 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -16.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -9.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:39,950,121-40,099,580 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHED, CDC2L, KIAA1791; previously CDC2L5 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 4 pathways, smallest: TP53 Regulates Transcription of DNA Repair Genes; Transcriptional Regulation by TP53; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14004](https://www.uniprot.org/uniprotkb/Q14004) (Cyclin-dependent kinase 13):

> Cyclin-dependent kinase which displays CTD kinase activity and is required for RNA splicing. Has CTD kinase activity by hyperphosphorylating the C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit RPB1, thereby acting as a key regulator of transcription elongation. Required for RNA splicing, probably by phosphorylating SRSF1/SF2. Required during hematopoiesis. In case of infection by HIV-1 virus, interacts with HIV-1 Tat protein acetylated at 'Lys-50' and …

**Summary**, from NCBI Gene [8621](https://www.ncbi.nlm.nih.gov/gene/8621):

> The protein encoded by this gene is a member of the cyclin-dependent serine/threonine protein kinase family. Members of this family are well known for their essential roles as master switches in cell cycle control. The exact function of this protein has not yet been determined, but it may play a role in mRNA processing and may be involved in regulation of hematopoiesis. Alternatively spliced transcript variants have been described.[provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:1733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1733) · Entrez [8621](https://www.ncbi.nlm.nih.gov/gene/8621) · UniProt [Q14004](https://www.uniprot.org/uniprotkb/Q14004) · Ensembl [ENSG00000065883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065883)

## Data

Gene col 808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 808); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 808]; `tensor/DDL_lfc|DDL_z.npy` [808]; `embed/gene_vectors.npy` [808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 808 or target_col == 808). Every well: [[CDK13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
