---
symbol: "KLF6"
type: "gene"
col: 849
ensembl_id: "ENSG00000067082"
name: "KLF transcription factor 6"
location: "10p15.2"
module: 113
arm: "+"
pooled_cpm: 256.61
n_lines_expressing: 49
n_dd_up: 38
n_dd_down: 12
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# KLF6

*KLF transcription factor 6* — 10p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +17.4, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 3.55× (z +15.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.332× (z -13.9, q 3e-41, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.647× (z -5.5, q 3e-06, down in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (PANC-1 0.113×, NCI-H23 0.122×, CFPAC-1 0.164×, HEC-1-A 0.171×, …; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 0.5 µM in 5 lines (PANC-1 0.158×, CFPAC-1 0.213×, HEC-1-A 0.218×, NCI-H23 0.195×, …; ⚠ cell-cycle shift, explains ~36% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (PANC-1 0.169×, NCI-H23 0.197×, CFPAC-1 0.228×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.398×, COLO 205 0.268×, CFPAC-1 0.448×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.261×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOB]] (+0.69, fdr 7e-06), [[ZFP36L1]] (+0.62, fdr 7e-06), [[KLF11]] (+0.60, fdr 1e-05); moves opposite to [[SNRNP40]] (-0.58, fdr 1e-05), [[MLEC]] (-0.58, fdr 1e-05), [[TMEM248]] (-0.57, fdr 1e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.65×** | +17.4 | 0e+00 | 46/47 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.55×** | +15.4 | 0e+00 | 46/47 (SK-MEL-2, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.38×** | +15.4 | 0e+00 | 47/47 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +14.4 | 7e-45 | 42/44 (A549, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.90×** | +13.4 | 4e-39 | 46/47 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +9.6 | 6e-20 | 46/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +8.9 | 5e-17 | 43/47 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.99×** | +8.3 | 6e-15 | 42/46 (NCI-H2030, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.81×** | +7.5 | 5e-12 | 41/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +7.2 | 3e-11 | 40/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.73×** | +6.9 | 3e-10 | 43/46 (SW48, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +6.3 | 1e-08 | 39/47 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.42×** | +6.2 | 2e-08 | 35/48 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.5 | 2e-06 | 35/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.48×** | +4.9 | 3e-05 | 32/47 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +4.7 | 9e-05 | 30/48 (SW48, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +4.6 | 1e-04 | 31/46 (SK-MEL-2, Panc 03.27, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 3e-04 | 31/47 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.002 | 29/46 (SK-MEL-2, COLO 205, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.002 | 26/46 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (PANC-1 0.113×, NCI-H23 0.122×, CFPAC-1 0.164×, HEC-1-A 0.171×, …; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 0.5 µM in 5 lines (PANC-1 0.158×, CFPAC-1 0.213×, HEC-1-A 0.218×, NCI-H23 0.195×, …; ⚠ cell-cycle shift, explains ~36% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (PANC-1 0.169×, NCI-H23 0.197×, CFPAC-1 0.228×; ⚠ cell-cycle shift, explains ~34% of this change); [[Panobinostat (drug)]] 0.05 µM in 3 lines (HEC-1-A 0.398×, COLO 205 0.268×, CFPAC-1 0.448×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.261×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.332×** | -13.9 | 3e-41 | 45/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.415×** | -11.1 | 3e-26 | 43/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.428×** | -10.7 | 2e-24 | 43/47 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.615×** | -8.7 | 5e-16 | 36/48 (A549, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.518×** | -8.0 | 2e-13 | 40/47 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.611×** | -6.0 | 2e-07 | 36/49 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.635×** | -5.7 | 8e-07 | 38/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.647×** | -5.5 | 3e-06 | 33/47 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -4.3 | 0.001 | 27/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.720×** | -4.0 | 0.004 | 25/43 (CFPAC-1, LOX-IMVI, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.581×** | -3.6 | 0.018 | 27/46 (HCT15, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.5 | 0.019 | 0/49 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.758×** | -3.5 | 0.021 | 29/47 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.061 | 21/47 (HEC-1-A, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.842× | -3.1 | 0.079 | 20/47 (RKO, SK-MEL-2, …) | top dose only | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.73 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 401 | 10 (4 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +19.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 7.22× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -16.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 351 | 11 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.215× (z -17.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 129 | 14 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.76× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.69× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 274 | 8 (4 ⚠) | 5 (5 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.29× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.61× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.113× (z -23.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 335 | 12 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 7.11× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.88× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 527 | 8 (3 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.30× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 321 | 7 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.277× (z -11.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 264 | 5 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.26× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.288× (z -12.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-423 (line)]] | alt | 298 | 4 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.36× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.239× (z -13.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 285 | 5 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.68× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.264× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 307 | 2 (1 ⚠) | 8 (7 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.64× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.122× (z -21.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.261× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 491 | 6 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.45× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.235× (z -14.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 622 | 3 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.63× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.164× (z -19.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.448× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 268 | 4 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.35× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.171× (z -19.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.398× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 241 | 6 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +18.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.31× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.266× (z -10.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 334 | 4 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.27× (z +15.8) | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 132 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +17.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.70× (z +15.6) | [[Selinexor (drug)]] 5 µM 0.463× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 251 | 7 (3 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 9.36× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.279× (z -11.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 128 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +14.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.75× (z +11.6) | — |
| [[J82 (line)]] | alt | 185 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +22.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.34× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.369× (z -8.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 325 | 1 | 7 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.42× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.199× (z -15.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 286 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +21.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 8.20× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.308× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 186 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +23.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.70× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 90.8 | 6 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.63× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.340× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 311 | 3 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 6.12× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.152× (z -13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.268× (z -9.4) |
| [[LoVo (line)]] | wt | 281 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.377× (z -9.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 271 | 7 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.62× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 377 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.89× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.317× (z -11.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 228 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.311× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 320 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -9.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 80.5 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 10.8× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.56× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 165 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +18.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.14× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 241 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.286× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 233 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.55× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.355× (z -8.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 91.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.27× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 183 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 214 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 190 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.319× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 98.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.89× (z +9.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.62× (z +10.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 216 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.72× (z +8.8) | — |
| [[SW480 (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.75× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[CHP-212 (line)]] | wt | 275 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.83× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.95× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOB]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ZFP36L1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KLF11]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZFHX3]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 | same gene group; STRING 464 |
| [[DUSP1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 772 |
| [[KLF4]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 690 |
| [[CDV3]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ITSN2]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[IL6R]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[GADD45B]] | +0.56 | +0.63 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 414 |
| [[ARL4A]] | +0.55 | +0.61 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[KLF2]] | +0.55 | +0.63 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP40]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[MLEC]] | -0.58 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[NDC1]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[P3H1]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RPA1]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SEC24C]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SAR1A]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MGAT5]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KLF6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DUSP8]] | C | DUSP8 activity raises KLF6's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without DUSP8 | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.468). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.7, 13.2); signed map (14.7, 27.1). **Vector** length 142, 56.7% of its response variance represented; |z| ≥ 3 in 1,875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.0 | +15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +10.0 | +17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.8 | +13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +15.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.4 | +7.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +7.0 | +6.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.8 | +4.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.5 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +6.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.3 | -8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.9 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.5 | -5.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.1 | -0.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.2 — chr10:3,775,996-3,785,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPBP, GBF, Zf9, PAC1; previously BCD1, ST12, COPEB |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING, HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99612](https://www.uniprot.org/uniprotkb/Q99612) (Krueppel-like factor 6):

> Transcriptional activator (By similarity). Binds a GC box motif. Could play a role in B-cell growth and development.

**Summary**, from NCBI Gene [1316](https://www.ncbi.nlm.nih.gov/gene/1316):

> This gene encodes a member of the Kruppel-like family of transcription factors. The zinc finger protein is a transcriptional activator, and functions as a tumor suppressor. Multiple transcript variants encoding different isoforms have been found for this gene, some of which are implicated in carcinogenesis. [provided by RefSeq, May 2009]

**Accessions** — [HGNC:2235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2235) · Entrez [1316](https://www.ncbi.nlm.nih.gov/gene/1316) · UniProt [Q99612](https://www.uniprot.org/uniprotkb/Q99612) · Ensembl [ENSG00000067082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067082)

## Data

Gene col 849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 849); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 849]; `tensor/DDL_lfc|DDL_z.npy` [849]; `embed/gene_vectors.npy` [849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 849 or target_col == 849). Every well: [[KLF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
