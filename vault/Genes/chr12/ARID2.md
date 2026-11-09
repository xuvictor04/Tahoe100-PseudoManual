---
symbol: "ARID2"
type: "gene"
col: 12088
ensembl_id: "ENSG00000189079"
name: "AT-rich interaction domain 2"
location: "12q12"
module: 2
arm: "-"
pooled_cpm: 232.85
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ARID2

*AT-rich interaction domain 2* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.96× (z +15.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.265× (z -31.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID1B]] (+0.70, fdr 1e-05), [[TCF12]] (+0.65, fdr 3e-05), [[ATAD2B]] (+0.65, fdr 8e-05); moves opposite to [[TPD52L2]] (-0.62, fdr 7e-05), [[FCHSD1]] (-0.59, fdr 0.001, ⚠ one half only (not replicated)), [[AP1M1]] (-0.58, fdr 1e-04), [[WDR55]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); 2 go from it, the strongest it → [[TULP4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +15.9 | 0e+00 | 45/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +12.0 | 2e-30 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +11.5 | 3e-28 | 36/48 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +10.5 | 2e-23 | 42/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +9.9 | 7e-21 | 43/49 (SNU-423, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +9.7 | 3e-20 | 41/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +6.5 | 7e-09 | 38/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.002 | 21/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.015 | 20/48 (NCI-H23, A-172, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.021 | 10/48 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.028 | 21/47 (PANC-1, A-172, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.042 | 13/49 (A-172, A498, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.10× | +3.2 | 0.059 | 0/48 | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.10 | 7/48 (HEC-1-A, SNU-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.265×** | -31.3 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.269×** | -31.0 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.383×** | -22.6 | 0e+00 | 48/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -17.6 | 0e+00 | 42/44 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.476×** | -17.5 | 0e+00 | 46/49 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -11.9 | 8e-31 | 39/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -9.2 | 2e-18 | 37/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.688×** | -8.8 | 9e-17 | 37/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -8.3 | 9e-15 | 37/47 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.708×** | -8.1 | 2e-14 | 40/48 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.720×** | -7.7 | 5e-13 | 31/48 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.736×** | -6.7 | 1e-09 | 30/45 (NCI-H2030, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -4.6 | 2e-04 | 29/49 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.830×** | -4.4 | 5e-04 | 23/48 (A549, BT-474, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.844× | -4.0 | 0.002 | 21/48 (HepG2/C3A, AN3 CA, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.760×** | -3.0 | 0.084 | 19/47 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.915× | -3.0 | 0.097 | 7/48 (AN3 CA, NCI-H2030, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.765×** | -2.9 | 0.097 | 16/48 (MIA PaCa-2, NCI-H661, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 290 | 8 (3 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +22.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -24.5) |
| [[C32 (line)]] | wt | 458 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -20.1) |
| [[SW480 (line)]] | alt | 279 | 5 (1 ⚠) | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.189× (z -32.3) |
| [[A549 (line)]] | wt | 235 | 6 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.68× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -25.4) |
| [[NCI-H2347 (line)]] | alt | 156 | 5 (2 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +23.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.03× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -20.2) |
| [[KATO III (line)]] | alt | 189 | 6 (2 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 435 | 1 | 10 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.17× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -26.4) |
| [[NCI-H460 (line)]] | wt | 242 | 5 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.86× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.267× (z -23.3) |
| [[HepG2_C3A (line)]] | wt | 288 | 2 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -23.1) |
| [[LoVo (line)]] | wt | 209 | 5 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.307× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 386 | 4 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -23.0) |
| [[SNU-423 (line)]] | alt | 168 | 3 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.49× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -16.4) |
| [[SW1417 (line)]] | alt | 204 | 3 (2 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -21.1) |
| [[HEC-1-A (line)]] | alt | 225 | 2 (1 ⚠) | 7 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.85× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.312× (z -17.9) |
| [[LS 180 (line)]] | wt | 229 | 4 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.250× (z -19.3) |
| [[NCI-H1573 (line)]] | alt | 443 | 2 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -19.5) |
| [[Panc 03.27 (line)]] | alt | 207 | 2 | 7 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.07× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -21.0) |
| [[SW 900 (line)]] | alt | 247 | 1 | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.190× (z -22.9) |
| [[AsPC-1 (line)]] | alt | 175 | 3 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.255× (z -17.0) |
| [[HOP62 (line)]] | alt | 139 | 3 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -19.1) |
| [[NCI-H2030 (line)]] | alt | 320 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -20.7) |
| [[AN3 CA (line)]] | alt | 439 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -13.2) |
| [[BT-474 (line)]] | alt | 213 | 3 | 4 | [[TAK-901 (drug)]] 0.05 µM 2.04× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -17.0) |
| [[C-33 A (line)]] | alt | 570 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -18.4) |
| [[HT-29 (line)]] | alt | 166 | 2 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -21.9) |
| [[SK-MEL-2 (line)]] | alt | 235 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.315× (z -16.1) |
| [[SNU-1 (line)]] | wt | 368 | 3 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -14.9) |
| [[A498 (line)]] | wt | 120 | 2 (1 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 3.02× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -20.1) |
| [[COLO 205 (line)]] | alt | 145 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -12.2) |
| [[H4 (line)]] | wt | 153 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 154 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.37× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -14.1) |
| [[J82 (line)]] | alt | 146 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.00× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 183 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.01× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.192× (z -23.1) |
| [[RKO (line)]] | wt | 349 | 3 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -20.0) |
| [[SW48 (line)]] | wt | 259 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -19.1) |
| [[A-172 (line)]] | wt | 124 | 2 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.35× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -12.4) |
| [[A-427 (line)]] | wt | 290 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -22.7) |
| [[CHP-212 (line)]] | wt | 269 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -14.7) |
| [[HS-578T (line)]] | alt | 161 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -18.1) |
| [[HCT15 (line)]] | alt | 221 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.364× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 170 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -24.5) |
| [[NCI-H661 (line)]] | alt | 410 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 158 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 2.49× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -13.2) |
| [[SHP-77 (line)]] | alt | 208 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 140 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -10.4) |
| [[Hs 766T (line)]] | wt | 132 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.333× (z -13.3) |
| [[SW 1271 (line)]] | alt | 301 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -9.5) |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID1B]] | +0.70 | +0.49 / +0.72 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 997 |
| [[TCF12]] | +0.65 | +0.45 / +0.64 | both halves | 3e-05 | pathway: ATP-dependent chromatin remodelers |
| [[ATAD2B]] | +0.65 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[FBXL17]] | +0.64 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ARID1A]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 998 |
| [[ARHGEF11]] | +0.63 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[ZNF827]] | +0.61 | +0.32 / +0.58 | both halves | 2e-04 | pathway: ATP-dependent chromatin remodelers |
| [[DPY19L1P1]] | +0.60 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[POU2F1]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[RAF1]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TDRD3]] | +0.56 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[SIK3]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.62 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[FCHSD1]] | -0.59 | -0.16 / -0.63 | ⚠ one half (not replicated) | 0.001 |  |
| [[AP1M1]] | -0.58 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[WDR55]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[MIER2]] | -0.58 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[KCTD21]] | -0.57 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[TMEM92-AS1]] | -0.57 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[PLXNA3]] | -0.57 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[RNF216P1]] | -0.57 | -0.12 / -0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[YKT6]] | -0.57 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[TPCN2]] | -0.56 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[MKNK1]] | -0.54 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[MSTO2P]] | -0.54 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[ZNF417]] | -0.54 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises ARID2's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without SOBP | 0.023 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity lowers ARID2's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.47× higher at baseline in the lines without TMEM92-AS1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TULP4]] | C | ARID2's natural level weakens TULP4's drug response | ARID2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.00; direction clear | 0.048 | ⚠ tissue can mimic it; precision caveat |
| [[TLK1]] | C | ARID2's natural level strengthens TLK1's drug response | ARID2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.00; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.3, 13.5); signed map (26.5, -23.2). **Vector** length 102, 37.4% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.1 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +12.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -31.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -31.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:45,729,706-45,908,040 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1557, DKFZp686G052, FLJ30619, BAF200, SMARCF3, ZIPZAP, p200 |
| Gene groups (HGNC) | AT-rich interaction domain containing; Armadillo like helical domain containing; PBAF complex subunits |
| Reactome | 8 pathways, smallest: Formation of the polybromo-BAF (pBAF) complex; SWI/SNF chromatin remodelers; RMTs methylate histone arginines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CP9](https://www.uniprot.org/uniprotkb/Q68CP9) (AT-rich interactive domain-containing protein 2):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Required for the stability of the SWI/SNF chromatin remodeling complex SWI/SNF-B (PBAF). May be involved in targeting the complex to different genes. May be involved in regulating transcriptional activation of cardiac genes.

**Summary**, from NCBI Gene [196528](https://www.ncbi.nlm.nih.gov/gene/196528):

> This gene encodes a member of the AT-rich interactive domain (ARID)-containing family of DNA-binding proteins. Members of the ARID family have roles in embryonic patterning, cell lineage gene regulation, cell cycle control, transcriptional regulation and chromatin structure modification. This protein functions as a subunit of the polybromo- and BRG1-associated factor or PBAF (SWI/SNF-B) chromatin remodeling complex which facilitates ligand-dependent transcriptional activation by nuclear …

**Accessions** — [HGNC:18037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18037) · Entrez [196528](https://www.ncbi.nlm.nih.gov/gene/196528) · UniProt [Q68CP9](https://www.uniprot.org/uniprotkb/Q68CP9) · Ensembl [ENSG00000189079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189079)

## Data

Gene col 12088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12088); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12088]; `tensor/DDL_lfc|DDL_z.npy` [12088]; `embed/gene_vectors.npy` [12088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12088 or target_col == 12088). Every well: [[ARID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
