---
symbol: "LRCH1"
type: "gene"
col: 5817
ensembl_id: "ENSG00000136141"
name: "leucine rich repeats and calponin homology domain containing 1"
location: "13q14.13-q14.2"
module: 141
arm: "+"
pooled_cpm: 177.68
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# LRCH1

*leucine rich repeats and calponin homology domain containing 1* — 13q14.13-q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.24× (z +10.0, q 9e-21, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.387× (z -22.5, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.441× (z -19.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRED1]] (+0.59, fdr 2e-05), [[PDE9A]] (+0.56, fdr 1e-05), [[TNS4]] (+0.55, fdr 1e-05); moves opposite to [[DYNC1LI2]] (-0.49, fdr 7e-05), [[TOM1]] (-0.47, fdr 2e-04), [[HDLBP]] (-0.45, fdr 6e-04).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TNS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +10.0 | 9e-21 | 42/49 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.4 | 4e-11 | 34/48 (AsPC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +7.1 | 2e-10 | 33/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.0 | 4e-10 | 28/48 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.7 | 2e-09 | 32/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.1 | 1e-07 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 2e-05 | 26/48 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.8 | 1e-04 | 22/47 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +4.3 | 1e-03 | 23/49 (SNU-423, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.009 | 18/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.5 | 0.021 | 15/48 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.039 | 17/48 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.061 | 13/48 (NCI-H2347, A-427, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.068 | 6/48 (C32, RKO, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.068 | 13/48 (A498, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -22.5 | 0e+00 | 49/49 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.405×** | -20.6 | 0e+00 | 40/44 (HCT15, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.441×** | -19.4 | 0e+00 | 48/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.461×** | -18.3 | 0e+00 | 47/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.440×** | -17.9 | 0e+00 | 38/45 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -14.2 | 6e-44 | 39/49 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.587×** | -12.6 | 2e-34 | 43/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.700×** | -8.4 | 3e-15 | 36/48 (LoVo, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.719×** | -7.8 | 4e-13 | 39/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -6.8 | 6e-10 | 34/47 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.804×** | -5.6 | 1e-06 | 27/48 (SW480, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.790×** | -5.6 | 1e-06 | 24/48 (LS 180, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.826×** | -4.7 | 1e-04 | 24/50 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.819×** | -4.7 | 1e-04 | 24/47 (SW480, LS 180, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.835× | -4.6 | 2e-04 | 19/49 (LS 180, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.822×** | -4.4 | 3e-04 | 23/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.832×** | -4.3 | 5e-04 | 22/49 (KATO III, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -4.3 | 6e-04 | 16/48 (A-172, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.876× | -3.9 | 0.003 | 17/49 (SW480, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.866× | -3.8 | 0.004 | 16/48 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 414 | 2 | 14 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.26× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.174× (z -24.0) |
| [[LoVo (line)]] | wt | 275 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -17.9) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -14.9) |
| [[LS 180 (line)]] | wt | 483 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -18.9) |
| [[HEC-1-A (line)]] | alt | 236 | 1 | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.84× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 248 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -13.0) |
| [[HOP62 (line)]] | alt | 126 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -12.4) |
| [[Hs 766T (line)]] | wt | 146 | 2 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.03× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -15.2) |
| [[KATO III (line)]] | alt | 286 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -18.5) |
| [[Panc 03.27 (line)]] | alt | 213 | 2 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -11.2) |
| [[A-172 (line)]] | wt | 107 | 2 (1 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.94× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -12.3) |
| [[SNU-423 (line)]] | alt | 126 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.441× (z -10.7) |
| [[SW48 (line)]] | wt | 198 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.46× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.315× (z -12.3) |
| [[A549 (line)]] | wt | 161 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -16.9) |
| [[C32 (line)]] | wt | 150 | 2 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.68× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.434× (z -11.2) |
| [[HS-578T (line)]] | alt | 90.7 | 1 | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.40× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -10.1) |
| [[HT-29 (line)]] | alt | 273 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.297× (z -13.5) |
| [[A498 (line)]] | wt | 164 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.335× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 166 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -14.5) |
| [[COLO 205 (line)]] | alt | 1,224 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -17.2) |
| [[J82 (line)]] | alt | 150 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.419× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 89.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.8) |
| [[SW1417 (line)]] | alt | 191 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -12.8) |
| [[HCT15 (line)]] | alt | 197 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 97.6 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 2.64× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.410× (z -10.9) |
| [[RKO (line)]] | wt | 202 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.446× (z -10.9) |
| [[CHP-212 (line)]] | wt | 186 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -9.8) |
| [[H4 (line)]] | wt | 129 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 155 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 74.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +15.3) ⚠ cell-cycle shift, explains ~6% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 102 | 2 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.14× (z +10.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 2.03× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -11.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.1 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.89× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 119 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.67× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.466× (z -9.5) |
| [[SHP-77 (line)]] | alt | 89.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -11.8) |
| [[SNU-1 (line)]] | wt | 153 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.45× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 77.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 79.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -20.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 148 | 0 | 2 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0684× (z -10.8) |
| [[A-427 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -19.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -11.5) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0668× (z -17.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 93.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRED1]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[PDE9A]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TNS4]] | +0.55 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SOX13]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[OSBPL10]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.53 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ACY1]] | +0.52 | +0.37 / +0.50 | both halves | 9e-05 |  |
| [[ETV4]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.51 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[GJB2]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[ACOT11]] | +0.51 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1LI2]] | -0.49 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[TOM1]] | -0.47 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[HDLBP]] | -0.45 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[CANX]] | -0.44 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[RNF10]] | -0.44 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS4]] | B | TNS4 activity raises LRCH1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.83× lower at baseline in the lines without TNS4 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[B3GNT3]] | B | B3GNT3 activity raises LRCH1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without B3GNT3 | 0.034 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PADI1]] | B | PADI1 activity raises LRCH1's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.90× lower at baseline in the lines without PADI1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[TGFBR2]] | B | TGFBR2 activity raises LRCH1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without TGFBR2 | 0.067 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[MIR4280HG]] | B | MIR4280HG activity raises LRCH1's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without MIR4280HG | 0.086 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[FUT4]] | B | FUT4 activity raises LRCH1's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without FUT4 | 0.098 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[GJB2]] | B | GJB2 activity raises LRCH1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without GJB2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.9, 49.4); signed map (5.7, 37.7). **Vector** length 95.9, 29.7% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +7.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | -0.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and calponin homology domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.13-q14.2 — chr13:46,553,168-46,753,040 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1016; previously CHDC1 |
| Gene groups (HGNC) | Leucine rich repeats and calponin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2L9](https://www.uniprot.org/uniprotkb/Q9Y2L9) (Leucine-rich repeat and calponin homology domain-containing protein 1):

> Acts as a negative regulator of GTPase CDC42 by sequestering CDC42-guanine exchange factor DOCK8. Probably by preventing CDC42 activation, negatively regulates CD4(+) T-cell migration.

**Summary**, from NCBI Gene [23143](https://www.ncbi.nlm.nih.gov/gene/23143):

> This gene encodes a protein with a leucine-rich repeat and a calponin homology domain. Polymorphism in this gene may be associated with susceptibililty to knee osteoarthritis. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:20309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20309) · Entrez [23143](https://www.ncbi.nlm.nih.gov/gene/23143) · UniProt [Q9Y2L9](https://www.uniprot.org/uniprotkb/Q9Y2L9) · Ensembl [ENSG00000136141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136141)

## Data

Gene col 5817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5817); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5817]; `tensor/DDL_lfc|DDL_z.npy` [5817]; `embed/gene_vectors.npy` [5817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5817 or target_col == 5817). Every well: [[LRCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
