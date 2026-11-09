---
symbol: "PCM1"
type: "gene"
col: 1228
ensembl_id: "ENSG00000078674"
name: "pericentriolar material 1"
location: "8p22"
module: 22
arm: "+"
pooled_cpm: 265.06
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PCM1

*pericentriolar material 1* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +14.1, q 4e-42, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AsPC-1 3.16×, NCI-H23 2.01×, NCI-H460 1.79×, NCI-H1573 2.05×, …; ⚠ cell-cycle shift, explains ~49% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (LS 180 2.18×, LoVo 1.94×, KATO III 1.92×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 2.01×, SK-MEL-2 2.10×; ⚠ toxic; transcription drop); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 1.78×); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 1.69×); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 1.78×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -14.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAG2]] (+0.69, fdr 7e-06), [[HP1BP3]] (+0.67, fdr 7e-06), [[NUCKS1]] (+0.66, fdr 1e-05); moves opposite to [[ADCY7]] (-0.59, fdr 1e-05), [[SLC35C1]] (-0.58, fdr 1e-05), [[MPP3]] (-0.57, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ST3GAL1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AsPC-1 3.16×, NCI-H23 2.01×, NCI-H460 1.79×, NCI-H1573 2.05×, …; ⚠ cell-cycle shift, explains ~49% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (LS 180 2.18×, LoVo 1.94×, KATO III 1.92×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 2.01×, SK-MEL-2 2.10×; ⚠ toxic; transcription drop); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 1.78×); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 1.69×); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 1.78×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.35×** | +14.1 | 4e-42 | 35/48 (AsPC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +9.7 | 1e-19 | 30/44 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +9.0 | 5e-17 | 35/49 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +8.9 | 1e-16 | 33/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.42×** | +6.2 | 8e-08 | 38/47 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +6.0 | 2e-07 | 26/48 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +5.1 | 2e-05 | 19/48 (KATO III, NCI-H460, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | 1.12× | +3.8 | 0.011 | 15/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.039 | 12/45 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.3 | 0.057 | 4/49 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.1 | 0.086 | 6/50 (AsPC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | 1.19× | +3.1 | 0.10 | 16/49 (AsPC-1, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -14.7 | 0e+00 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.702×** | -11.8 | 2e-29 | 38/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.718×** | -10.6 | 5e-24 | 32/47 (SW480, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.757×** | -9.3 | 3e-18 | 33/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.803×** | -7.3 | 3e-11 | 27/48 (SW480, HCT15, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.819×** | -6.6 | 3e-09 | 27/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.831×** | -6.1 | 6e-08 | 25/48 (SW480, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -5.9 | 3e-07 | 12/48 (SW480, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.837× | -5.6 | 2e-06 | 21/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.838× | -5.1 | 2e-05 | 20/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -5.0 | 4e-05 | 18/49 (SW480, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.864× | -4.6 | 2e-04 | 13/47 (AN3 CA, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.775×** | -4.4 | 4e-04 | 26/45 (SW48, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.910× | -4.4 | 4e-04 | 9/48 (A-427, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.861× | -4.3 | 5e-04 | 16/48 (A-427, CFPAC-1, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.833×** | -4.3 | 5e-04 | 23/48 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.05 µM |  | 0.870× | -4.3 | 6e-04 | 13/47 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.881× | -3.7 | 0.007 | 12/48 (Hs 766T, HCT15, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.811×** | -3.6 | 0.008 | 24/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.925× | -3.6 | 0.008 | 6/49 (MIA PaCa-2, SK-MEL-2, …) | two highest doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 0.893× | -3.5 | 0.013 | 7/47 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Monocrotaline (drug)]] 0.05 µM |  | 0.901× | -3.2 | 0.029 | 5/47 (AsPC-1, CHP-212, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.031 | 15/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 193 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +24.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.78× (z +10.3) | — |
| [[KATO III (line)]] | alt | 337 | 7 (7 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +16.0) ⚠ cell-cycle shift, explains ~49% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 450 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -20.6) |
| [[MIA PaCa-2 (line)]] | alt | 303 | 2 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +10.7) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -15.6) |
| [[AN3 CA (line)]] | alt | 720 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -16.2) ⚠ cell-cycle shift, explains ~74% of this change |
| [[LoVo (line)]] | wt | 212 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +16.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 206 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +17.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[HCT15 (line)]] | alt | 523 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.8) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.576× (z -8.7) |
| [[HOP62 (line)]] | alt | 217 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.560× (z -11.0) |
| [[HS-578T (line)]] | alt | 326 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 320 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +15.1) ⚠ cell-cycle shift, explains ~22% of this change | [[Panobinostat (drug)]] 0.5 µM 0.618× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 328 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.623× (z -10.3) |
| [[PANC-1 (line)]] | alt | 156 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.615× (z -10.0) |
| [[A-427 (line)]] | wt | 441 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.567× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 274 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +14.5) ⚠ cell-cycle shift, explains ~49% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.638× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 212 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.63× (z +8.8) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.387× (z -8.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.620× (z -8.6) |
| [[A498 (line)]] | wt | 157 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +11.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 363 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -15.7) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.602× (z -10.4) |
| [[COLO 205 (line)]] | alt | 189 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 313 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 145 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H23 (line)]] | alt | 307 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +17.8) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 0.5 µM 0.568× (z -10.1) |
| [[RKO (line)]] | wt | 292 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +15.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 224 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.557× (z -9.8) |
| [[SW 900 (line)]] | alt | 285 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 322 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.61× (z +10.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 219 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[Hs 766T (line)]] | wt | 256 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.582× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 267 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.545× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 239 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.67× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 229 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.71× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 628 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +12.4) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 286 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +12.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 490 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 400 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 235 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 304 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 332 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG2]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[HP1BP3]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NUCKS1]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[RAD21]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[ATRX]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SYNE2]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CEP57]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[HSD17B11]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PMPCB]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[HMGN2]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[IFT81]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 646 |
| [[LSM14A]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY7]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SLC35C1]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[MPP3]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[HMOX2]] | -0.56 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[RABIF]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[MON1A]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BAK1]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CSNK1E]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 | pathway: AURKA Activation by TPX2 |
| [[SFN]] | -0.53 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[RABEPK]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[PLEKHG5]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ABCC10]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | ST3GAL1 activity lowers PCM1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.47× higher at baseline in the lines without ST3GAL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | PCM1's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | PCM1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.395). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.5, -53.3); signed map (11.4, -15.4). **Vector** length 147, 48.1% of its response variance represented; |z| ≥ 3 in 1,314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +8.7 | +14.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.6 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.6 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.8 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +3.4 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -9.5 | -10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.0 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.3 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.1 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | pericentriolar material 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,922,842-18,029,948 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTC4 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15154](https://www.uniprot.org/uniprotkb/Q15154) (Pericentriolar material 1 protein):

> Required for centrosome assembly and function. Essential for the correct localization of several centrosomal proteins including CEP250, CETN3, PCNT and NEK2. Required to anchor microtubules to the centrosome. Also involved in cilium biogenesis by recruiting the BBSome, a ciliary protein complex involved in cilium biogenesis, to the centriolar satellites. Recruits the tubulin polyglutamylase complex (TPGC) to centriolar satellites.

**Summary**, from NCBI Gene [5108](https://www.ncbi.nlm.nih.gov/gene/5108):

> The protein encoded by this gene is a component of centriolar satellites, which are electron dense granules scattered around centrosomes. Inhibition studies show that this protein is essential for the correct localization of several centrosomal proteins, and for anchoring microtubules to the centrosome. Chromosomal aberrations involving this gene are associated with papillary thyroid carcinomas and a variety of hematological malignancies, including atypical chronic myeloid leukemia and T-cell …

**Accessions** — [HGNC:8727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8727) · Entrez [5108](https://www.ncbi.nlm.nih.gov/gene/5108) · UniProt [Q15154](https://www.uniprot.org/uniprotkb/Q15154) · Ensembl [ENSG00000078674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078674)

## Data

Gene col 1228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1228); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1228]; `tensor/DDL_lfc|DDL_z.npy` [1228]; `embed/gene_vectors.npy` [1228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1228 or target_col == 1228). Every well: [[PCM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
