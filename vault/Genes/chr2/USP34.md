---
symbol: "USP34"
type: "gene"
col: 3680
ensembl_id: "ENSG00000115464"
name: "ubiquitin specific peptidase 34"
location: "2p15"
module: 65
arm: "-"
pooled_cpm: 575.98
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# USP34

*ubiquitin specific peptidase 34* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.43× (z +8.9, q 5e-16, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -21.6, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRH1]] (+0.62, fdr 5e-05), [[TAS2R14]] (+0.59, fdr 1e-05), [[RALGAPA1]] (+0.59, fdr 5e-05); moves opposite to [[DUSP11]] (-0.54, fdr 5e-04), [[MIR29B2CHG]] (-0.53, fdr 1e-04), [[VPS33B]] (-0.52, fdr 5e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +8.9 | 5e-16 | 40/48 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +7.9 | 1e-12 | 39/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +7.6 | 6e-12 | 43/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 9e-09 | 32/48 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +5.8 | 7e-07 | 40/48 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.2 | 2e-05 | 23/48 (COLO 205, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.9 | 8e-05 | 26/47 (NCI-H460, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +4.8 | 1e-04 | 43/49 (A498, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.9 | 0.006 | 17/48 (HEC-1-A, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.8 | 0.007 | 17/48 (COLO 205, AsPC-1, …) | top dose only | composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.007 | 32/48 (AsPC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.023 | 28/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.11 | 11/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -21.6 | 0e+00 | 45/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.497×** | -16.8 | 0e+00 | 47/47 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.511×** | -16.8 | 0e+00 | 47/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.516×** | -16.5 | 0e+00 | 46/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.516×** | -15.9 | 0e+00 | 40/44 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.537×** | -15.5 | 0e+00 | 48/49 (NCI-H460, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.518×** | -15.2 | 0e+00 | 43/45 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.564×** | -14.3 | 1e-44 | 47/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.611×** | -11.9 | 1e-30 | 42/48 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -11.4 | 3e-28 | 40/50 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -9.6 | 3e-20 | 42/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.722×** | -8.1 | 2e-14 | 41/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.753×** | -7.1 | 6e-11 | 39/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.823×** | -6.9 | 2e-10 | 27/48 (C32, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.767×** | -6.6 | 1e-09 | 35/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -6.3 | 8e-09 | 31/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -4.9 | 3e-05 | 15/48 (A549, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.721×** | -4.2 | 8e-04 | 40/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.894× | -4.0 | 0.002 | 7/48 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.858× | -3.8 | 0.004 | 17/48 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.898× | -3.8 | 0.004 | 9/48 (NCI-H23, A549, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.872× | -3.4 | 0.015 | 16/48 (CFPAC-1, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.867× | -3.3 | 0.023 | 13/47 (MIA PaCa-2, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 661 | 4 (1 ⚠) | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.90× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -21.2) |
| [[J82 (line)]] | alt | 317 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -18.6) |
| [[LoVo (line)]] | wt | 516 | 5 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -15.8) |
| [[COLO 205 (line)]] | alt | 383 | 8 (4 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +20.6) | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 760 | 1 (1 ⚠) | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -17.2) |
| [[PANC-1 (line)]] | alt | 650 | 0 | 12 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -24.8) |
| [[SW480 (line)]] | alt | 606 | 2 | 10 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 3.22× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -18.0) |
| [[A549 (line)]] | wt | 750 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -35.3) |
| [[C32 (line)]] | wt | 516 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -19.3) |
| [[HT-29 (line)]] | alt | 531 | 1 | 10 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.346× (z -18.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -15.3) |
| [[LS 180 (line)]] | wt | 484 | 2 (1 ⚠) | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 860 | 1 | 10 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -21.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -13.5) |
| [[SW 900 (line)]] | alt | 518 | 0 | 11 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.404× (z -14.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -12.4) |
| [[A-427 (line)]] | wt | 1,108 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -16.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 397 | 2 | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -15.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 474 | 1 | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.54× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -22.7) |
| [[HOP62 (line)]] | alt | 643 | 0 | 10 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -14.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -11.4) |
| [[HS-578T (line)]] | alt | 431 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 806 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 750 | 0 | 10 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -20.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.411× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 1,591 | 1 | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -29.2) |
| [[NCI-H23 (line)]] | alt | 865 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -20.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -15.4) |
| [[RKO (line)]] | wt | 620 | 1 | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 534 | 4 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.446× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 457 | 0 | 8 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -15.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -12.4) |
| [[A-172 (line)]] | wt | 540 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -19.2) |
| [[HCT15 (line)]] | alt | 642 | 1 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -14.6) |
| [[KATO III (line)]] | alt | 444 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -14.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -11.4) |
| [[SNU-1 (line)]] | wt | 567 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -17.9) |
| [[SNU-423 (line)]] | alt | 373 | 1 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.68× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -13.2) |
| [[SW48 (line)]] | wt | 503 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.0) |
| [[BT-474 (line)]] | alt | 347 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.566× (z -10.0) |
| [[CHP-212 (line)]] | wt | 529 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.1) |
| [[H4 (line)]] | wt | 525 | 0 | 6 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 673 | 1 | 5 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.71× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -17.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -12.3) |
| [[A498 (line)]] | wt | 435 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -17.1) |
| [[C-33 A (line)]] | alt | 679 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -19.2) |
| [[Hs 766T (line)]] | wt | 297 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.524× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 459 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 276 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 421 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -14.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 381 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.76× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -14.3) |
| [[AN3 CA (line)]] | alt | 419 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 500 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -12.3) |
| [[SW 1271 (line)]] | alt | 548 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.5) |
| [[NCI-H2122 (line)]] | alt | 598 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 568 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 437 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRH1]] | +0.62 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[TAS2R14]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RALGAPA1]] | +0.59 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[PRR4]] | +0.55 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[SFSWAP]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ZNF638]] | +0.54 | +0.32 / +0.55 | both halves | 1e-04 | STRING 543 |
| [[TAF1]] | +0.53 | +0.26 / +0.63 | both halves | 4e-04 |  |
| [[NF1]] | +0.53 | +0.59 / +0.44 | both halves | 3e-05 | same gene group |
| [[COMMD10]] | +0.52 | +0.32 / +0.54 | both halves | 1e-04 |  |
| [[ASXL2]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 | pathway: Deubiquitination |
| [[BPTF]] | +0.51 | +0.25 / +0.51 | both halves | 4e-04 | STRING 615 |
| [[CUX1]] | +0.51 | +0.35 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP11]] | -0.54 | -0.23 / -0.57 | both halves | 5e-04 |  |
| [[MIR29B2CHG]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[VPS33B]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ZNF738]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ZNF836]] | -0.50 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[ALG9]] | -0.48 | -0.21 / -0.52 | both halves | 6e-04 |  |
| [[CAPN5]] | -0.47 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[MINDY3]] | -0.46 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SNX33]] | -0.46 | -0.21 / -0.33 | both halves | 6e-04 |  |
| [[IL22RA1]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[SNX11]] | -0.45 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[LINC00674]] | -0.44 | -0.22 / -0.46 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises USP34's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PRKN]] | B | PRKN activity raises USP34's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.48× lower at baseline in the lines without PRKN | 0.073 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.6, 14.8); signed map (7.8, -11.1). **Vector** length 93.1, 40.9% of its response variance represented; |z| ≥ 3 in 1,500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.7 | -15.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.4 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.3 | -15.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | -0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.5 | -16.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -9.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -2.3 | +0.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,187,463-61,471,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0570, KIAA0729 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; Armadillo like helical domain containing; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: TCF dependent signaling in response to WNT; Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70CQ2](https://www.uniprot.org/uniprotkb/Q70CQ2) (Ubiquitin carboxyl-terminal hydrolase 34):

> Ubiquitin hydrolase that can remove conjugated ubiquitin from AXIN1 and AXIN2, thereby acting as a regulator of Wnt signaling pathway. Acts as an activator of the Wnt signaling pathway downstream of the beta-catenin destruction complex by deubiquitinating and stabilizing AXIN1 and AXIN2, leading to promote nuclear accumulation of AXIN1 and AXIN2 and positively regulate beta-catenin (CTNBB1)-mediated transcription. Recognizes and hydrolyzes the peptide bond at the C-terminal Gly of ubiquitin. …

**Summary**, from NCBI Gene [9736](https://www.ncbi.nlm.nih.gov/gene/9736):

> Enables cysteine-type deubiquitinase activity and cysteine-type endopeptidase activity. Involved in positive regulation of canonical Wnt signaling pathway and protein K48-linked deubiquitination. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20066) · Entrez [9736](https://www.ncbi.nlm.nih.gov/gene/9736) · UniProt [Q70CQ2](https://www.uniprot.org/uniprotkb/Q70CQ2) · Ensembl [ENSG00000115464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115464)

## Data

Gene col 3680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3680); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3680]; `tensor/DDL_lfc|DDL_z.npy` [3680]; `embed/gene_vectors.npy` [3680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3680 or target_col == 3680). Every well: [[USP34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
