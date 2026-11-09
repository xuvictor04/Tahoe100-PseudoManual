---
symbol: "PTBP2"
type: "gene"
col: 3925
ensembl_id: "ENSG00000117569"
name: "polypyrimidine tract binding protein 2"
location: "1p21.3"
module: 51
arm: "+"
pooled_cpm: 205.47
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# PTBP2

*polypyrimidine tract binding protein 2* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.45× (z +10.5, q 6e-23, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.322× (z -23.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF8]] (+0.66, fdr 7e-06), [[C2CD5]] (+0.64, fdr 7e-06), [[RBM26]] (+0.63, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.55, fdr 4e-04), [[TPRG1L]] (-0.53, fdr 4e-04), [[LRP10]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +10.5 | 6e-23 | 36/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +8.7 | 1e-15 | 42/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +8.3 | 2e-14 | 44/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.5 | 7e-12 | 37/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +7.5 | 8e-12 | 40/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.7 | 1e-06 | 29/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.038 | 20/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.058 | 25/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.13 | 17/48 (NCI-H1573, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.322×** | -23.2 | 0e+00 | 48/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.338×** | -22.2 | 0e+00 | 48/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.362×** | -20.8 | 0e+00 | 48/49 (SNU-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.421×** | -17.7 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -16.7 | 0e+00 | 42/44 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.548×** | -12.3 | 1e-32 | 48/48 (SNU-423, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -11.5 | 1e-28 | 42/49 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -11.2 | 2e-27 | 40/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.614×** | -10.0 | 1e-21 | 45/48 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.641×** | -8.7 | 2e-16 | 41/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -8.1 | 2e-14 | 44/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -7.7 | 8e-13 | 40/48 (A-172, A549, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.691×** | -7.5 | 2e-12 | 39/48 (HS-578T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.703×** | -6.9 | 2e-10 | 42/50 (SW480, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.798×** | -6.4 | 6e-09 | 26/48 (J82, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.018 | 26/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.724×** | -3.3 | 0.029 | 23/46 (SW1417, H4, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.065 | 25/47 (C32, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.070 | 19/48 (SK-MEL-2, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 226 | 3 | 11 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.45× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -17.8) |
| [[HS-578T (line)]] | alt | 279 | 1 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -18.0) |
| [[A-172 (line)]] | wt | 159 | 1 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -17.7) |
| [[A498 (line)]] | wt | 176 | 3 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.290× (z -19.9) |
| [[HOP62 (line)]] | alt | 164 | 3 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -20.1) |
| [[J82 (line)]] | alt | 256 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -18.8) |
| [[SNU-423 (line)]] | alt | 224 | 1 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 289 | 1 | 9 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.06× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.246× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 186 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -20.5) |
| [[A549 (line)]] | wt | 170 | 2 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +19.0) | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -21.2) |
| [[HEC-1-A (line)]] | alt | 306 | 1 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -18.0) |
| [[NCI-H1792 (line)]] | alt | 253 | 2 (1 ⚠) | 7 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.02× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.305× (z -16.5) |
| [[PANC-1 (line)]] | alt | 189 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -19.1) |
| [[RKO (line)]] | wt | 309 | 2 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +17.1) | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -18.4) |
| [[NCI-H2347 (line)]] | alt | 236 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.363× (z -15.0) |
| [[SW48 (line)]] | wt | 309 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 246 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -14.2) |
| [[LoVo (line)]] | wt | 164 | 1 | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.86× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.333× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 277 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 179 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.309× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 123 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 228 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.338× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 260 | 1 | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.22× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.329× (z -13.9) |
| [[SHP-77 (line)]] | alt | 220 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -13.2) |
| [[SW 900 (line)]] | alt | 182 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 134 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -15.6) |
| [[C-33 A (line)]] | alt | 255 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -13.7) |
| [[C32 (line)]] | wt | 246 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -10.8) |
| [[Hs 766T (line)]] | wt | 188 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -14.1) |
| [[HT-29 (line)]] | alt | 109 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.8) | [[Auranofin (drug)]] 5 µM 0.349× (z -12.8) |
| [[KATO III (line)]] | alt | 97.2 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 261 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -14.5) |
| [[SW1417 (line)]] | alt | 149 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -10.8) |
| [[A-427 (line)]] | wt | 140 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 174 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 217 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.456× (z -11.3) |
| [[SNU-1 (line)]] | wt | 379 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -31.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -13.0) |
| [[H4 (line)]] | wt | 142 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -11.1) |
| [[HCT15 (line)]] | alt | 244 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -10.8) |
| [[AN3 CA (line)]] | alt | 275 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -12.8) |
| [[BT-474 (line)]] | alt | 221 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -12.5) |
| [[LS 180 (line)]] | wt | 157 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -10.0) |
| [[COLO 205 (line)]] | alt | 97.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.4) | — |
| [[NCI-H661 (line)]] | alt | 219 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -8.9) |
| [[SW 1271 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -9.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 271 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF8]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[C2CD5]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RBM26]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 | same gene group |
| [[SREK1]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 | same gene group |
| [[DECR2]] | +0.61 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SLC25A12]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.59 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[LSM14A]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[FAM133B]] | +0.59 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[USP24]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[POGZ]] | +0.59 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[COQ2]] | +0.59 | +0.35 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.55 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[TPRG1L]] | -0.53 | -0.25 / -0.65 | both halves | 4e-04 |  |
| [[LRP10]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BAG5]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[MCFD2]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[TMED7-TICAM2]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[TMEM127]] | -0.50 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[RHOC]] | -0.50 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[TICAM2]] | -0.49 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[DPP9]] | -0.49 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[GABRE]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ZNF731P]] | -0.48 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PTBP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.0, 2.4); signed map (7.1, -38.3). **Vector** length 91.7, 34.7% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.2 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | -16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | -20.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.8 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.1 | -12.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -0.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.8 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | polypyrimidine tract binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:96,721,665-96,823,738 (+) |
| Ensembl biotype | protein_coding |
| Also known as | brPTB, nPTB, PTB, PTBLP |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKA9](https://www.uniprot.org/uniprotkb/Q9UKA9) (Polypyrimidine tract-binding protein 2):

> RNA-binding protein which binds to intronic polypyrimidine tracts and mediates negative regulation of exons splicing. May antagonize in a tissue-specific manner the ability of NOVA1 to activate exon selection. In addition to its function in pre-mRNA splicing, plays also a role in the regulation of translation.; [Isoform 5]: Reduced affinity for RNA.

**Summary**, from NCBI Gene [58155](https://www.ncbi.nlm.nih.gov/gene/58155):

> The protein encoded by this gene binds to intronic polypyrimidine clusters in pre-mRNA molecules and is implicated in controlling the assembly of other splicing-regulatory proteins. This protein is very similar to the polypyrimidine tract binding protein (PTB) but most of its isoforms are expressed primarily in the brain. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:17662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17662) · Entrez [58155](https://www.ncbi.nlm.nih.gov/gene/58155) · UniProt [Q9UKA9](https://www.uniprot.org/uniprotkb/Q9UKA9) · Ensembl [ENSG00000117569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117569)

## Data

Gene col 3925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3925); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3925]; `tensor/DDL_lfc|DDL_z.npy` [3925]; `embed/gene_vectors.npy` [3925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3925 or target_col == 3925). Every well: [[PTBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
