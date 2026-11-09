---
symbol: "RB1CC1"
type: "gene"
col: 342
ensembl_id: "ENSG00000023287"
name: "RB1 inducible coiled-coil 1"
location: "8q11.23"
module: 69
arm: "+"
pooled_cpm: 349.78
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# RB1CC1

*RB1 inducible coiled-coil 1* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +16.0, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.297× (z -29.7, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.268× (z -16.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.80, fdr 7e-06), [[TBC1D15]] (+0.79, fdr 7e-06), [[SLU7]] (+0.77, fdr 9e-06); moves opposite to [[PDSS1]] (-0.62, fdr 1e-05), [[C19orf48]] (-0.59, fdr 1e-05), [[NME1]] (-0.58, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +16.0 | 0e+00 | 40/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +15.5 | 0e+00 | 46/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +10.8 | 8e-25 | 42/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +10.5 | 2e-23 | 44/48 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +10.0 | 2e-21 | 41/48 (H4, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +9.3 | 1e-18 | 37/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.9 | 6e-17 | 40/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +8.7 | 2e-16 | 40/48 (HEC-1-A, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +7.4 | 6e-12 | 28/49 (AsPC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +6.7 | 1e-09 | 38/49 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.5 | 3e-09 | 33/48 (C32, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +5.9 | 2e-07 | 30/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +5.7 | 7e-07 | 28/48 (HS-578T, AsPC-1, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +5.4 | 3e-06 | 20/49 (CHP-212, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +4.8 | 6e-05 | 27/48 (C32, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 5e-04 | 29/49 (MIA PaCa-2, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +4.3 | 5e-04 | 21/48 (Hs 766T, NCI-H2030, …) | all doses, flat |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.12× | +4.0 | 0.002 | 3/48 (RPMI-7951, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.297×** | -29.7 | 0e+00 | 48/48 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.268×** | -16.9 | 0e+00 | 48/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.303×** | -15.3 | 0e+00 | 48/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.324×** | -14.4 | 4e-45 | 48/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.342×** | -13.7 | 9e-41 | 47/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.372×** | -12.7 | 9e-35 | 48/48 (HS-578T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.626×** | -11.0 | 2e-26 | 44/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.543×** | -10.7 | 1e-24 | 48/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.650×** | -10.5 | 4e-24 | 36/49 (NCI-H23, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.667×** | -9.5 | 1e-19 | 33/44 (HT-29, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.643×** | -7.7 | 6e-13 | 46/49 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.719×** | -7.6 | 1e-12 | 36/48 (RKO, SW48, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.658×** | -7.3 | 1e-11 | 46/48 (SW480, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.725×** | -7.3 | 1e-11 | 34/45 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.567×** | -7.3 | 2e-11 | 46/47 (AsPC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -4.3 | 7e-04 | 23/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.838× | -4.1 | 0.001 | 23/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.849× | -4.0 | 0.002 | 18/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.852× | -3.9 | 0.002 | 18/49 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.874× | -3.3 | 0.024 | 14/48 (HT-29, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 290 | 12 (3 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -16.5) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.250× (z -9.1) |
| [[HS-578T (line)]] | alt | 439 | 8 (4 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +22.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -26.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.199× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 364 | 7 (2 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +17.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -25.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.201× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 222 | 9 (3 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +19.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -22.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.272× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 461 | 2 | 12 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.264× (z -22.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.133× (z -18.1) |
| [[PANC-1 (line)]] | alt | 373 | 6 (1 ⚠) | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +14.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.297× (z -19.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.282× (z -10.8) |
| [[A549 (line)]] | wt | 492 | 1 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -19.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.8) |
| [[HT-29 (line)]] | alt | 333 | 5 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -20.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.259× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 440 | 6 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +16.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.429× (z -15.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.298× (z -11.6) |
| [[C32 (line)]] | wt | 315 | 10 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +20.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -16.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.301× (z -9.6) |
| [[SW 900 (line)]] | alt | 467 | 1 | 11 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -19.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.213× (z -11.9) |
| [[A498 (line)]] | wt | 458 | 5 (3 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +20.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -18.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.156× (z -12.7) |
| [[LoVo (line)]] | wt | 248 | 6 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.228× (z -20.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.445× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 422 | 2 | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -26.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.183× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 195 | 4 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -30.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.198× (z -14.7) |
| [[SW480 (line)]] | alt | 287 | 2 (1 ⚠) | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.363× (z -23.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.335× (z -13.0) |
| [[BT-474 (line)]] | alt | 267 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +17.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.351× (z -13.4) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 530 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -20.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.416× (z -11.1) |
| [[A-172 (line)]] | wt | 273 | 6 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +21.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -13.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.304× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 330 | 4 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -15.1) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 401 | 2 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.358× (z -15.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.299× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 338 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -26.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.189× (z -15.5) |
| [[SW1417 (line)]] | alt | 239 | 2 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -22.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.251× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 289 | 0 | 7 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.367× (z -14.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.258× (z -10.3) |
| [[COLO 205 (line)]] | alt | 270 | 5 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.370× (z -12.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.205× (z -10.7) |
| [[Hs 766T (line)]] | wt | 346 | 2 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.360× (z -15.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.208× (z -12.2) |
| [[KATO III (line)]] | alt | 330 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.220× (z -18.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.216× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 443 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -22.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.293× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 355 | 0 | 7 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -18.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.278× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 409 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -15.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.244× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 418 | 4 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.11× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.407× (z -13.9) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 273 | 0 | 7 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.129× (z -25.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.107× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 203 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.392× (z -12.6) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 287 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -19.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.229× (z -9.5) |
| [[SNU-423 (line)]] | alt | 695 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.315× (z -8.7) |
| [[A-427 (line)]] | wt | 339 | 1 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.74× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 281 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.338× (z -15.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.190× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 442 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.455× (z -11.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.318× (z -9.0) |
| [[J82 (line)]] | alt | 316 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.423× (z -12.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.264× (z -9.8) |
| [[SHP-77 (line)]] | alt | 425 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -17.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.306× (z -9.5) |
| [[CHP-212 (line)]] | wt | 336 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -15.3) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 255 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -13.4) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 262 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.370× (z -13.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.295× (z -8.8) |
| [[HOP62 (line)]] | alt | 404 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -15.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 341 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -10.5) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 419 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -13.9) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 436 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.80 | +0.64 / +0.86 | both halves | 7e-06 |  |
| [[TBC1D15]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 | STRING 491 |
| [[SLU7]] | +0.77 | +0.57 / +0.82 | both halves | 9e-06 |  |
| [[UBXN7]] | +0.76 | +0.53 / +0.80 | both halves | 1e-05 |  |
| [[TCP11L2]] | +0.75 | +0.59 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[WDR48]] | +0.74 | +0.58 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SYF2]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.73 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[JMY]] | +0.72 | +0.46 / +0.80 | both halves | 2e-05 | **novel candidate** |
| [[BSDC1]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[GABARAPL1]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | same gene group; pathway: Autophagy; STRING 967 |
| [[SERINC1]] | +0.68 | +0.45 / +0.76 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDSS1]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[C19orf48]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[NME1]] | -0.58 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[VARS1]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CAD]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.56 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.54 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[EMC1]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[AGK]] | -0.54 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[RANBP1]] | -0.53 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[UBE2N]] | -0.53 | -0.56 / -0.52 | both halves | 1e-05 | pathway: Autophagy |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -45.1); signed map (-14.2, 9.8). **Vector** length 151, 62.1% of its response variance represented; |z| ≥ 3 in 1,982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +6.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +5.4 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +5.3 | +2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.7 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -24.6 | -29.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -15.9 | -16.9 |
|  | [[EX229 (drug)]] 5 µM |  | -15.2 | -14.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -14.5 | -12.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -13.8 | -13.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -13.8 | -15.3 |

## What is on record

|  |  |
|---|---|
| Name | RB1 inducible coiled-coil 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:52,622,458-52,745,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0203, Cc1, DRAGOU14, FIP200, ATG17, PPP1R131 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Autophagy related |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDY2](https://www.uniprot.org/uniprotkb/Q8TDY2) (RB1-inducible coiled-coil protein 1):

> Involved in autophagy. Regulates early events but also late events of autophagosome formation through direct interaction with Atg16L1. Required for the formation of the autophagosome-like double-membrane structure that surrounds the Salmonella-containing vacuole (SCV) during S.typhimurium infection and subsequent xenophagy (By similarity). Involved in repair of DNA damage caused by ionizing radiation, which subsequently improves cell survival by decreasing apoptosis (By similarity). Inhibits …

**Summary**, from NCBI Gene [9821](https://www.ncbi.nlm.nih.gov/gene/9821):

> The protein encoded by this gene interacts with signaling pathways to coordinately regulate cell growth, cell proliferation, apoptosis, autophagy, and cell migration. This tumor suppressor also enhances retinoblastoma 1 gene expression in cancer cells. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:15574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15574) · Entrez [9821](https://www.ncbi.nlm.nih.gov/gene/9821) · UniProt [Q8TDY2](https://www.uniprot.org/uniprotkb/Q8TDY2) · Ensembl [ENSG00000023287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023287)

## Data

Gene col 342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 342); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 342]; `tensor/DDL_lfc|DDL_z.npy` [342]; `embed/gene_vectors.npy` [342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 342 or target_col == 342). Every well: [[RB1CC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RB1CC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
