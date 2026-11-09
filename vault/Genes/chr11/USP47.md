---
symbol: "USP47"
type: "gene"
col: 9919
ensembl_id: "ENSG00000170242"
name: "ubiquitin specific peptidase 47"
location: "11p15.3"
module: 64
arm: "+"
pooled_cpm: 244.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# USP47

*ubiquitin specific peptidase 47* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +20.9, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.483× (z -23.1, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.533× (z -19.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF7]] (+0.66, fdr 1e-05), [[ACOT13]] (+0.65, fdr 1e-05), [[ANKRD49]] (+0.63, fdr 1e-05); moves opposite to [[PLCB3]] (-0.58, fdr 2e-05), [[PMPCA]] (-0.56, fdr 3e-05), [[SPATA33]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +20.9 | 0e+00 | 41/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +16.9 | 0e+00 | 47/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +16.8 | 0e+00 | 46/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +16.1 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +16.0 | 0e+00 | 41/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +15.6 | 0e+00 | 46/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +13.2 | 1e-37 | 48/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +12.8 | 1e-35 | 39/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +11.2 | 3e-27 | 39/48 (LoVo, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +8.2 | 1e-14 | 36/45 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +7.2 | 3e-11 | 28/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +6.8 | 4e-10 | 26/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +6.4 | 6e-09 | 38/49 (PANC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +6.1 | 5e-08 | 24/48 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.7 | 4e-07 | 23/48 (LoVo, BT-474, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.15× | +4.6 | 2e-04 | 10/48 (HOP62, BT-474, …) | two highest doses | low cells (technical?); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.030 | 19/49 (A498, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.046 | 17/48 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -23.1 | 0e+00 | 46/49 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -23.0 | 0e+00 | 42/44 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -19.9 | 0e+00 | 48/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.563×** | -18.2 | 0e+00 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -13.7 | 8e-41 | 42/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.789×** | -10.6 | 2e-24 | 28/49 (A549, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.698×** | -10.5 | 4e-24 | 35/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -10.5 | 7e-24 | 35/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.738×** | -9.2 | 2e-18 | 37/47 (RKO, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.786×** | -7.6 | 1e-12 | 31/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.804×** | -6.9 | 3e-10 | 28/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -6.8 | 4e-10 | 17/48 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.838× | -5.4 | 3e-06 | 23/50 (A-172, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.851× | -4.9 | 4e-05 | 22/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.903× | -4.6 | 2e-04 | 12/48 (A-172, HOP62, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | 0.899× | -3.4 | 0.023 | 10/49 (SW1417, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.912× | -2.9 | 0.092 | 3/47 (HT-29, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.912× | -2.9 | 0.092 | 6/48 (NCI-H2347, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 278 | 12 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +26.0) | [[Panobinostat (drug)]] 5 µM 0.563× (z -12.8) |
| [[SW480 (line)]] | alt | 324 | 9 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +23.4) | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -18.1) |
| [[LoVo (line)]] | wt | 221 | 12 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +23.2) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.639× (z -9.4) |
| [[A-172 (line)]] | wt | 302 | 5 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -18.2) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.468× (z -14.7) |
| [[BT-474 (line)]] | alt | 277 | 11 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +18.6) | [[Panobinostat (drug)]] 0.5 µM 0.548× (z -9.5) |
| [[HOP62 (line)]] | alt | 197 | 7 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.84× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.431× (z -15.4) |
| [[LS 180 (line)]] | wt | 268 | 11 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.548× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 224 | 7 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.0) | [[Auranofin (drug)]] 5 µM 0.314× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 264 | 8 | 5 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.50× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.492× (z -13.1) |
| [[PANC-1 (line)]] | alt | 260 | 8 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.589× (z -12.8) |
| [[A498 (line)]] | wt | 289 | 5 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +26.9) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.517× (z -14.2) |
| [[HT-29 (line)]] | alt | 215 | 8 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +22.5) | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 182 | 8 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.06× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.555× (z -11.2) |
| [[C32 (line)]] | wt | 204 | 9 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -12.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 381 | 3 | 7 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.46× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.392× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 251 | 6 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.522× (z -12.2) |
| [[SW48 (line)]] | wt | 257 | 7 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -9.4) |
| [[A-427 (line)]] | wt | 198 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.496× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.539× (z -11.5) |
| [[HS-578T (line)]] | alt | 235 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -12.6) |
| [[KATO III (line)]] | alt | 138 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.8) | — |
| [[NCI-H2347 (line)]] | alt | 191 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +20.4) | [[Panobinostat (drug)]] 0.5 µM 0.551× (z -10.9) |
| [[SNU-423 (line)]] | alt | 329 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -11.9) |
| [[SW1417 (line)]] | alt | 280 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -14.4) |
| [[COLO 205 (line)]] | alt | 174 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -11.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 240 | 4 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.495× (z -11.1) |
| [[A549 (line)]] | wt | 436 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -21.1) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 330 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.93× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 243 | 2 | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 323 | 1 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.91× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.369× (z -15.0) |
| [[SNU-1 (line)]] | wt | 385 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.28× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.549× (z -8.6) |
| [[RKO (line)]] | wt | 315 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.585× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 217 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.02× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.449× (z -13.6) |
| [[C-33 A (line)]] | alt | 262 | 2 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.92× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.536× (z -9.6) |
| [[HCT15 (line)]] | alt | 319 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.548× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 159 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.9) | [[Auranofin (drug)]] 5 µM 0.477× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 298 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.490× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 190 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 187 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.89× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.488× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -9.0) |
| [[SW 900 (line)]] | alt | 133 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -11.7) |
| [[SW 1271 (line)]] | alt | 221 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.284× (z -8.9) |
| [[AN3 CA (line)]] | alt | 318 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.374× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.483× (z -9.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.479× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 186 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.525× (z -9.2) |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 258 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF7]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ACOT13]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[UBE3A]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PSMD7]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 | pathway: Deubiquitination; STRING 408 |
| [[SNW1]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CPLANE1]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CUL5]] | +0.59 | +0.68 / +0.44 | both halves | 3e-05 | STRING 570 |
| [[CCDC43]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[PSMD4]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TACO1]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCB3]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PMPCA]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SPATA33]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TFRC]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PDXP]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[SUN1]] | -0.52 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[PTMAP5]] | -0.50 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[P4HB]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises USP47's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-21.1, 9.4); signed map (6.9, -30.5). **Vector** length 108, 38.2% of its response variance represented; |z| ≥ 3 in 1,647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +13.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.1 | +15.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.6 | +16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +20.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +6.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.1 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -19.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -18.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -13.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -6.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.7 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:11,841,423-11,961,887 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K76](https://www.uniprot.org/uniprotkb/Q96K76) (Ubiquitin carboxyl-terminal hydrolase 47):

> Ubiquitin-specific protease that specifically deubiquitinates monoubiquitinated DNA polymerase beta (POLB), stabilizing POLB thereby playing a role in base-excision repair (BER). Acts as a regulator of cell growth and genome integrity. May also indirectly regulate CDC25A expression at a transcriptional level.

**Summary**, from NCBI Gene [55031](https://www.ncbi.nlm.nih.gov/gene/55031):

> Enables WD40-repeat domain binding activity and cysteine-type deubiquitinase activity. Involved in base-excision repair; monoubiquitinated protein deubiquitination; and positive regulation of canonical Wnt signaling pathway. Located in cytoplasm. Part of SCF ubiquitin ligase complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20076) · Entrez [55031](https://www.ncbi.nlm.nih.gov/gene/55031) · UniProt [Q96K76](https://www.uniprot.org/uniprotkb/Q96K76) · Ensembl [ENSG00000170242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170242)

## Data

Gene col 9919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9919); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9919]; `tensor/DDL_lfc|DDL_z.npy` [9919]; `embed/gene_vectors.npy` [9919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9919 or target_col == 9919). Every well: [[USP47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
