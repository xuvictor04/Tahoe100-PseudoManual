---
symbol: "BHLHE40"
type: "gene"
col: 5510
ensembl_id: "ENSG00000134107"
name: "basic helix-loop-helix family member e40"
location: "3p26.1"
module: 14
arm: "+"
pooled_cpm: 256.24
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BHLHE40

*basic helix-loop-helix family member e40* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 17.0× (z +15.1, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.351× (z -15.2, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARRDC3]] (+0.72, fdr 7e-06), [[NR1D1]] (+0.67, fdr 7e-06), [[GEM]] (+0.64, fdr 2e-05); moves opposite to [[LIN52]] (-0.55, fdr 5e-05), [[TMEM11-DT]] (-0.53, fdr 4e-05), [[GPR89A]] (-0.51, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[RRAD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **17.0×** | +15.1 | 0e+00 | 49/49 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.75×** | +10.3 | 3e-22 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +7.8 | 2e-12 | 39/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.03×** | +7.2 | 8e-11 | 40/48 (SW48, H4, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.07×** | +7.1 | 1e-10 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.71×** | +7.0 | 3e-10 | 34/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.7 | 2e-09 | 38/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.49×** | +5.7 | 1e-06 | 30/48 (SW1417, PANC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 2e-06 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +5.4 | 3e-06 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.41×** | +4.7 | 2e-04 | 27/38 (HS-578T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.55×** | +4.1 | 0.002 | 34/47 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.7 | 0.011 | 26/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.021 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.351×** | -15.2 | 0e+00 | 48/49 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -12.9 | 2e-35 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.371×** | -10.2 | 6e-22 | 43/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.450×** | -7.9 | 6e-13 | 44/48 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.490×** | -7.3 | 3e-11 | 39/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -6.2 | 7e-08 | 40/50 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -5.9 | 3e-07 | 29/44 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.588×** | -5.2 | 1e-05 | 35/47 (A-172, COLO 205, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.870× | -5.2 | 1e-05 | 7/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.635×** | -4.7 | 2e-04 | 39/48 (H4, A498, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.637×** | -4.6 | 2e-04 | 40/48 (A498, A-172, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.728×** | -4.6 | 2e-04 | 35/48 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -4.2 | 0.001 | 33/48 (C32, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.668×** | -4.1 | 0.001 | 36/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.753×** | -4.1 | 0.001 | 33/48 (A498, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.006 | 34/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.765×** | -3.8 | 0.006 | 34/49 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.712×** | -3.5 | 0.015 | 34/48 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.719×** | -3.4 | 0.021 | 31/48 (RKO, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 195 | 17 (9 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 11.0× (z +18.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 9.44× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -13.6) |
| [[PANC-1 (line)]] | alt | 134 | 13 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 6.36× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 23.2× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.5) |
| [[SW48 (line)]] | wt | 151 | 10 (5 ⚠) | 2 | [[PH-797804 (drug)]] 5 µM 30.0× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.229× (z -11.8) |
| [[C32 (line)]] | wt | 446 | 3 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 38.2× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -19.2) |
| [[NCI-H1573 (line)]] | alt | 217 | 9 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 7.32× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 29.1× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.287× (z -10.0) |
| [[A-172 (line)]] | wt | 559 | 1 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -25.2) |
| [[Hs 766T (line)]] | wt | 432 | 2 (1 ⚠) | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 20.2× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.3) |
| [[A498 (line)]] | wt | 278 | 1 | 7 | [[TAK-901 (drug)]] 5 µM 7.84× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 277 | 5 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 20.7× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.2) |
| [[HOP62 (line)]] | alt | 398 | 4 (2 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 21.0× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -12.3) |
| [[A-427 (line)]] | wt | 66.1 | 7 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 26.8× (z +14.0) | — |
| [[A549 (line)]] | wt | 389 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.7× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -13.1) |
| [[H4 (line)]] | wt | 184 | 5 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 26.6× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 269 | 2 | 5 | [[TAK-901 (drug)]] 5 µM 18.7× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.175× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 693 | 3 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.1× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.8) |
| [[SW480 (line)]] | alt | 170 | 3 (1 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 18.4× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.247× (z -10.6) |
| [[LoVo (line)]] | wt | 149 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 26.5× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.182× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 178 | 5 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 5.87× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.94× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 331 | 4 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 5.13× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 20.0× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -13.2) |
| [[SNU-423 (line)]] | alt | 204 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +13.4) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.0× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -15.4) |
| [[SW1417 (line)]] | alt | 216 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.1) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.15× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.182× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 251 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -11.3) |
| [[COLO 205 (line)]] | alt | 212 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 25.8× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.5) |
| [[HS-578T (line)]] | alt | 439 | 2 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 22.0× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -21.8) |
| [[HT-29 (line)]] | alt | 121 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 10.5× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -16.6) |
| [[KATO III (line)]] | alt | 176 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.0× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.266× (z -12.4) |
| [[LS 180 (line)]] | wt | 173 | 3 | 2 | [[TAK-901 (drug)]] 5 µM 12.4× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.167× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 274 | 2 (1 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 13.7× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.203× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 428 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 24.5× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -15.6) |
| [[SHP-77 (line)]] | alt | 212 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -13.8) |
| [[J82 (line)]] | alt | 251 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 4.12× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 251 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 27.8× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 104 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.87× (z +12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 36.1× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 103 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.06× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.281× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 257 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 141 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 17.0× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -8.9) |
| [[RKO (line)]] | wt | 321 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.83× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 339 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.7× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 118 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 20.6× (z +12.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.1) |
| [[SW 1271 (line)]] | alt | 363 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 17.4× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -17.0) |
| [[SW 900 (line)]] | alt | 270 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 16.8× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.9) |
| [[BT-474 (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -13.8) |
| [[HCT15 (line)]] | alt | 173 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 251 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.19× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -9.6) |
| [[SW 1088 (line)]] | alt | 331 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -9.0) |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 263 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRDC3]] | +0.72 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[NR1D1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 | pathway: Circadian clock; STRING 929 |
| [[GEM]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIE]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CD83]] | +0.63 | +0.49 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[IER3]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[BCL3]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CSRNP1]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 | STRING 419 |
| [[NOCT]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[NFKBIZ]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[RYBP]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NFKB2]] | +0.56 | +0.39 / +0.61 | both halves | 6e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN52]] | -0.55 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[GPR89A]] | -0.51 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[ARIH2]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[VKORC1L1]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SLC38A9]] | -0.48 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[NR2C2]] | -0.48 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[WDR20]] | -0.48 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[ORC2]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[GLYR1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TM2D1]] | -0.46 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[NUP133]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAD]] | B | RRAD activity raises BHLHE40's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without RRAD | 0.012 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[TOP2A]] | B | TOP2A activity raises BHLHE40's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP10]] | B | DUSP10 activity raises BHLHE40's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without DUSP10 | 0.032 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[HCP5]] | B | HCP5 activity raises BHLHE40's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.44× lower at baseline in the lines without HCP5 | 0.037 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[TNFRSF9]] | B | TNFRSF9 activity raises BHLHE40's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without TNFRSF9 | 0.037 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[NINJ1]] | B | NINJ1 activity raises BHLHE40's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without NINJ1 | 0.078 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[IL1A]] | B | IL1A activity raises BHLHE40's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without IL1A | 0.078 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[LIF]] | B | LIF activity raises BHLHE40's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without LIF | 0.084 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[RND1]] | B | RND1 activity strengthens BHLHE40's drug response | lines that do not express RND1 (9) vs lines expressing it (40) | the lines without RND1 respond 0.87× as strongly (z diff +1.72); strongest at Panobinostat 5 µM: 0.46x vs 0.29x (z diff +3.1) | 0.085 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TRAF1]] | B | TRAF1 activity raises BHLHE40's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without TRAF1 | 0.086 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[CADM1]] | B | CADM1 activity raises BHLHE40's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 1.43× lower at baseline in the lines without CADM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[SMAD7]] | B | SMAD7 activity raises BHLHE40's level | lines that do not express SMAD7 (5) vs lines expressing it (45) | 1.97× lower at baseline in the lines without SMAD7 | 0.091 | ⚠ within organs, on part of the lines; also absent: SFXN3, KIAA2012, PLSCR2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.7, 3.2); signed map (8.9, 28.2). **Vector** length 115, 45.8% of its response variance represented; |z| ≥ 3 in 1,595 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.2 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.1 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.6 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.4 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | -0.5 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.4 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | +5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | basic helix-loop-helix family member e40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:4,979,437-4,985,323 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEC1, SHARP2, Clast5; previously STRA13, BHLHB2 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Hallmark sets | UV_RESPONSE_DN, MYOGENESIS, IL2_STAT5_SIGNALING, HYPOXIA, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; BMAL1:CLOCK,NPAS2 activates circadian expression; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [O14503](https://www.uniprot.org/uniprotkb/O14503) (Class E basic helix-loop-helix protein 40):

> Transcriptional repressor involved in the regulation of the circadian rhythm by negatively regulating the activity of the clock genes and clock-controlled genes. Acts as the negative limb of a novel autoregulatory feedback loop (DEC loop) which differs from the one formed by the PER and CRY transcriptional repressors (PER/CRY loop). Both these loops are interlocked as it represses the expression of PER1/2 and in turn is repressed by PER1/2 and CRY1/2. Represses the activity of the circadian …

**Summary**, from NCBI Gene [8553](https://www.ncbi.nlm.nih.gov/gene/8553):

> This gene encodes a basic helix-loop-helix protein expressed in various tissues. The encoded protein can interact with ARNTL or compete for E-box binding sites in the promoter of PER1 and repress CLOCK/ARNTL's transactivation of PER1. This gene is believed to be involved in the control of circadian rhythm and cell differentiation. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:1046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1046) · Entrez [8553](https://www.ncbi.nlm.nih.gov/gene/8553) · UniProt [O14503](https://www.uniprot.org/uniprotkb/O14503) · Ensembl [ENSG00000134107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134107)

## Data

Gene col 5510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5510); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5510]; `tensor/DDL_lfc|DDL_z.npy` [5510]; `embed/gene_vectors.npy` [5510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5510 or target_col == 5510). Every well: [[BHLHE40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BHLHE40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
