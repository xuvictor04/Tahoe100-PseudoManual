---
symbol: "HLCS"
type: "gene"
col: 8241
ensembl_id: "ENSG00000159267"
name: "holocarboxylase synthetase"
location: "21q22.13"
module: 4
arm: "+"
pooled_cpm: 116.8
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HLCS

*holocarboxylase synthetase* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.34× (z +4.8, q 1e-03, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.418× (z -20.0, q 0e+00, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.538× (z -14.2, q 8e-44, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPH6]] (+0.67, fdr 7e-06), [[ENOX2]] (+0.65, fdr 7e-06), [[DOCK1]] (+0.64, fdr 7e-06); moves opposite to [[TSC22D4]] (-0.65, fdr 7e-06), [[BMF]] (-0.62, fdr 1e-05), [[PEX13]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ULK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +4.8 | 1e-03 | 32/48 (HEC-1-A, H4, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.071 | 17/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.072 | 21/48 (LS 180, NCI-H1573, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.22× | +3.2 | 0.16 | 18/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.1 | 0.19 | 5/48 (HOP62, LS 180, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.19 | 17/49 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.21× | +3.0 | 0.19 | 16/48 (NCI-H460, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.418×** | -20.0 | 0e+00 | 45/48 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.346×** | -17.3 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.398×** | -15.0 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -14.2 | 8e-44 | 48/49 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.476×** | -12.1 | 2e-31 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.481×** | -11.9 | 1e-30 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.473×** | -11.7 | 9e-30 | 44/48 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.288×** | -10.6 | 3e-24 | 47/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.600×** | -8.3 | 7e-15 | 39/48 (LoVo, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -7.6 | 1e-12 | 38/48 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.617×** | -7.5 | 2e-12 | 34/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -6.8 | 5e-10 | 39/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.679×** | -6.3 | 1e-08 | 35/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -6.2 | 2e-08 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.686×** | -6.1 | 4e-08 | 30/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -6.1 | 4e-08 | 35/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -4.4 | 4e-04 | 26/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.702×** | -3.0 | 0.056 | 18/49 (LoVo, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.826×** | -2.9 | 0.069 | 19/48 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.785×** | -2.8 | 0.099 | 14/49 (PANC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 168 | 0 | 15 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -24.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -19.7) |
| [[PANC-1 (line)]] | alt | 93.9 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -30.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -14.0) |
| [[SW480 (line)]] | alt | 263 | 0 | 13 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.461× (z -9.7) |
| [[A-172 (line)]] | wt | 199 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -30.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -19.4) |
| [[J82 (line)]] | alt | 82.5 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -20.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -11.5) |
| [[LoVo (line)]] | wt | 227 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -18.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.198× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 86.0 | 0 | 11 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -12.1) |
| [[KATO III (line)]] | alt | 112 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -17.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.220× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 189 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -24.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -18.9) |
| [[RKO (line)]] | wt | 130 | 0 | 8 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.301× (z -11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.3) |
| [[SW48 (line)]] | wt | 190 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.0) |
| [[A-427 (line)]] | wt | 121 | 0 | 7 (7 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -13.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 97.0 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -20.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 93.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -19.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -8.6) |
| [[HT-29 (line)]] | alt | 77.4 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -29.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.408× (z -10.0) |
| [[BT-474 (line)]] | alt | 79.7 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 91.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -23.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.6) |
| [[HOP62 (line)]] | alt | 109 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 116 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 58.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -24.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 173 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.6) |
| [[SNU-1 (line)]] | wt | 123 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.8) |
| [[SW1417 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.1) |
| [[COLO 205 (line)]] | alt | 70.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 57.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 87.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.195× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 84.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 63.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -12.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 82.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 79.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -11.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH6]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 | same gene group |
| [[ENOX2]] | +0.65 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[EEFSEC]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NAA15]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EIF4G3]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[MTHFD1L]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Metabolism of vitamins and cofactors |
| [[TSEN2]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[THADA]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | -0.65 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[BMF]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[PEX13]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ANG]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.53 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[KLC4]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[APAF1]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[APTR]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ATOSA]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ULK2]] | B | ULK2 activity raises HLCS's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.14× lower at baseline in the lines without ULK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[PRMT3]] | C | PRMT3's natural level strengthens HLCS's drug response | PRMT3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.22; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.6, -33.3); signed map (3.2, -51.3). **Vector** length 96.7, 34.0% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.6 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -14.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -6.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -4.0 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -10.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | -3.0 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | holocarboxylase synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:36,748,626-36,990,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCS |
| Gene groups (HGNC) | Ligases |
| Reactome | 7 pathways, smallest: Defective HLCS causes multiple carboxylase deficiency; Defects in biotin (Btn) metabolism; Biotin transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P50747](https://www.uniprot.org/uniprotkb/P50747) (Biotin--protein ligase):

> Biotin--protein ligase catalyzing the biotinylation of the 4 biotin-dependent carboxylases acetyl-CoA-carboxylase, pyruvate carboxylase, propionyl-CoA carboxylase, and methylcrotonyl-CoA carboxylase.

**Summary**, from NCBI Gene [3141](https://www.ncbi.nlm.nih.gov/gene/3141):

> This gene encodes an enzyme that catalyzes the binding of biotin to carboxylases and histones. The protein plays an important role in gluconeogenesis, fatty acid synthesis and branched chain amino acid catabolism. Defects in this gene are the cause of holocarboxylase synthetase deficiency. Multiple alternatively spliced variants, encoding the same protein, have been identified.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:4976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4976) · Entrez [3141](https://www.ncbi.nlm.nih.gov/gene/3141) · UniProt [P50747](https://www.uniprot.org/uniprotkb/P50747) · Ensembl [ENSG00000159267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159267)

## Data

Gene col 8241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8241); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8241]; `tensor/DDL_lfc|DDL_z.npy` [8241]; `embed/gene_vectors.npy` [8241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8241 or target_col == 8241). Every well: [[HLCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
