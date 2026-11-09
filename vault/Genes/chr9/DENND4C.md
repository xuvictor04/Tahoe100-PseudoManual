---
symbol: "DENND4C"
type: "gene"
col: 5974
ensembl_id: "ENSG00000137145"
name: "DENN domain containing 4C"
location: "9p22.1"
module: 45
arm: "+"
pooled_cpm: 208.6
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# DENND4C

*DENN domain containing 4C* — 9p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.47× (z +8.7, q 3e-15, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.295× (z -27.4, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.670× (z -12.7, q 8e-35, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1A]] (+0.67, fdr 1e-05), [[RCOR3]] (+0.63, fdr 7e-06), [[SNX2]] (+0.58, fdr 3e-05); moves opposite to [[EP400P1]] (-0.61, fdr 1e-05), [[MAEA]] (-0.60, fdr 1e-05), [[BRD9]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGES]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.47×** | +8.7 | 3e-15 | 45/49 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +7.5 | 2e-11 | 36/48 (SW48, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +6.4 | 3e-08 | 33/48 (SW48, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +5.9 | 3e-07 | 33/48 (C-33 A, LOX-IMVI, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.9 | 3e-07 | 25/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.8 | 6e-07 | 29/48 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.18× | +5.3 | 9e-06 | 21/48 (PANC-1, LOX-IMVI, …) | all doses, flat | low cells (technical?) |
| [[Mifepristone (drug)]] 5 µM |  | **1.26×** | +5.0 | 4e-05 | 28/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +5.0 | 4e-05 | 30/48 (hTERT-HPNE, C-33 A, …) | top dose only |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.23×** | +4.7 | 1e-04 | 22/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +4.6 | 2e-04 | 25/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.15× | +4.6 | 2e-04 | 5/48 (A498, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 8e-04 | 25/48 (LS 180, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.009 | 20/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.009 | 22/48 (SW48, NCI-H460, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.013 | 21/49 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Minodronic acid (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.023 | 9/48 (HT-29, LoVo, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.025 | 19/48 (LS 180, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.027 | 23/48 (LoVo, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.075 | 12/48 (HT-29, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.093 | 7/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +2.9 | 0.099 | 17/47 (LoVo, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.295×** | -27.4 | 0e+00 | 48/49 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.316×** | -24.9 | 0e+00 | 44/44 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.377×** | -20.3 | 0e+00 | 43/45 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -12.7 | 8e-35 | 37/49 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.585×** | -12.0 | 3e-31 | 40/48 (HT-29, COLO 205, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -10.8 | 3e-25 | 45/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.632×** | -10.3 | 6e-23 | 39/48 (Panc 03.27, HT-29, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -9.1 | 4e-18 | 42/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.674×** | -8.8 | 6e-17 | 33/48 (HT-29, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -7.1 | 9e-11 | 29/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.747×** | -6.5 | 3e-09 | 38/48 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.785×** | -5.4 | 3e-06 | 35/48 (SW 900, COLO 205, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.690×** | -5.1 | 1e-05 | 39/48 (LS 180, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.667×** | -4.5 | 2e-04 | 34/46 (NCI-H460, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.818×** | -4.5 | 3e-04 | 26/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.869× | -4.4 | 3e-04 | 17/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.833×** | -4.1 | 0.001 | 25/48 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.844× | -3.8 | 0.004 | 18/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.788×** | -3.3 | 0.024 | 16/48 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.903× | -3.2 | 0.028 | 13/49 (NCI-H1573, LS 180, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.876× | -3.0 | 0.060 | 16/49 (HT-29, NCI-H1792, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.812×** | -2.9 | 0.078 | 15/47 (CHP-212, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 274 | 2 | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 182 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -20.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -16.5) |
| [[SW 900 (line)]] | alt | 316 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -10.2) |
| [[A549 (line)]] | wt | 403 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -28.1) |
| [[SW480 (line)]] | alt | 214 | 1 | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.68× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 197 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -10.1) |
| [[LoVo (line)]] | wt | 245 | 1 | 7 (7 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.79× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -14.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H2347 (line)]] | alt | 195 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -19.7) |
| [[Panc 03.27 (line)]] | alt | 299 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -11.6) |
| [[SNU-423 (line)]] | alt | 232 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.8) |
| [[SW1417 (line)]] | alt | 240 | 1 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.8) ⚠ cell-cycle shift, explains ~80% of this change | [[Dinaciclib (drug)]] 5 µM 0.195× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -9.0) |
| [[HT-29 (line)]] | alt | 269 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -17.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 302 | 1 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 171 | 4 (4 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.87× (z +10.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.454× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 178 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.9) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.70× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 200 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 204 | 1 (1 ⚠) | 5 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.55× (z +8.5) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 172 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 225 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -9.1) |
| [[A498 (line)]] | wt | 358 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -13.4) |
| [[COLO 205 (line)]] | alt | 412 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -19.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 290 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -14.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 205 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -12.4) |
| [[CHP-212 (line)]] | wt | 234 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.302× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 238 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.559× (z -8.8) |
| [[HOP62 (line)]] | alt | 171 | 1 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.95× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -9.4) |
| [[PANC-1 (line)]] | alt | 79.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.61× (z +10.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 174 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.355× (z -13.3) |
| [[A-427 (line)]] | wt | 135 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.8) ⚠ cell-cycle shift, explains ~80% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -20.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 299 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.273× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 129 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -19.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 334 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -12.8) |
| [[HS-578T (line)]] | alt | 169 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 261 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 270 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 219 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -12.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -8.9) |
| [[H4 (line)]] | wt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -15.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 168 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.8) ⚠ cell-cycle shift, explains ~80% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -14.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 88.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 76.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.412× (z -9.9) |
| [[SW 1271 (line)]] | alt | 111 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0883× (z -11.8) |
| [[C32 (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1A]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SNX2]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 | STRING 433 |
| [[SCPEP1]] | +0.58 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[RRAGD]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[HSF2]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[USP33]] | +0.56 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[ARL6IP5]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SLC22A18]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[QPRT]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[GALM]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[XPO1]] | +0.54 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EP400P1]] | -0.61 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[MAEA]] | -0.60 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[BRD9]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SLFNL1-AS1]] | -0.56 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[DPP9]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[RNASEH1]] | -0.53 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[REXO1]] | -0.53 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[PUS1]] | -0.53 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[UVSSA]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MSS51]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CRYGS]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GOLGA3]] | -0.52 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGES]] | B | PTGES activity raises DENND4C's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without PTGES | 0.073 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.1, -24.5); signed map (-24.4, -7.2). **Vector** length 118, 42.2% of its response variance represented; |z| ≥ 3 in 1,468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +10.3 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +8.8 | +5.9 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.7 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +6.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.6 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -7.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.9 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:19,230,435-19,374,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20686, bA513M16.3, RAB10GEF; previously C9orf55B, C9orf55 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZ89](https://www.uniprot.org/uniprotkb/Q5VZ89) (DENN domain-containing protein 4C):

> Guanine nucleotide exchange factor (GEF) activating RAB10. Promotes the exchange of GDP to GTP, converting inactive GDP-bound RAB10 into its active GTP-bound form. Thereby, stimulates SLC2A4/GLUT4 glucose transporter-enriched vesicles delivery to the plasma membrane in response to insulin.

**Summary**, from NCBI Gene [55667](https://www.ncbi.nlm.nih.gov/gene/55667):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in cellular response to insulin stimulus; protein localization to plasma membrane; and regulation of Rab protein signal transduction. Located in Golgi apparatus and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26079) · Entrez [55667](https://www.ncbi.nlm.nih.gov/gene/55667) · UniProt [Q5VZ89](https://www.uniprot.org/uniprotkb/Q5VZ89) · Ensembl [ENSG00000137145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137145)

## Data

Gene col 5974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5974); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5974]; `tensor/DDL_lfc|DDL_z.npy` [5974]; `embed/gene_vectors.npy` [5974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5974 or target_col == 5974). Every well: [[DENND4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
