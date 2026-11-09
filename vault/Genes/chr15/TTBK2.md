---
symbol: "TTBK2"
type: "gene"
col: 4927
ensembl_id: "ENSG00000128881"
name: "tau tubulin kinase 2"
location: "15q15.2"
module: 17
arm: "+"
pooled_cpm: 93.24
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 20
n_dd_up_clean: 19
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TTBK2

*tau tubulin kinase 2* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +19.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.445× (z -19.0, q 0e+00, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.604× (z -16.5, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GKAP1]] (+0.64, fdr 7e-06), [[TBC1D19]] (+0.63, fdr 1e-05), [[TIPRL]] (+0.62, fdr 1e-05); moves opposite to [[TRNT1]] (-0.64, fdr 1e-05), [[GTF3C2-AS2]] (-0.64, fdr 9e-05), [[DPY19L3-DT]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PKIG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 2 with an alert ⚠; shown: the 15 strongest. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +19.0 | 0e+00 | 44/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +15.0 | 0e+00 | 48/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +14.9 | 0e+00 | 43/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +14.4 | 4e-45 | 46/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +11.1 | 9e-27 | 43/48 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +9.7 | 3e-20 | 31/48 (A-172, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.4 | 5e-15 | 32/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +8.2 | 2e-14 | 38/48 (HOP62, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +7.0 | 1e-10 | 36/47 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +6.9 | 2e-10 | 28/49 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 5e-09 | 27/48 (COLO 205, HOP62, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +6.1 | 4e-08 | 29/48 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +6.1 | 5e-08 | 32/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 6e-07 | 23/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +5.5 | 1e-06 | 23/48 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -19.0 | 0e+00 | 37/44 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.459×** | -17.6 | 0e+00 | 38/45 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -16.5 | 0e+00 | 42/49 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.516×** | -16.1 | 0e+00 | 36/49 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -13.4 | 5e-39 | 45/48 (hTERT-HPNE, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -11.9 | 1e-30 | 41/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -11.8 | 3e-30 | 43/50 (SW 1271, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -9.4 | 3e-19 | 37/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -9.1 | 8e-18 | 37/47 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.731×** | -7.6 | 1e-12 | 28/48 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.749×** | -7.0 | 1e-10 | 32/48 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.835× | -4.4 | 6e-04 | 22/48 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.833×** | -4.3 | 9e-04 | 20/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.795×** | -4.0 | 0.003 | 17/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.612×** | -3.9 | 0.003 | 18/37 (SNU-423, C32, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.005 | 15/48 (NCI-H1792, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.623×** | -3.8 | 0.005 | 16/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.635×** | -3.6 | 0.008 | 14/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.866× | -3.5 | 0.013 | 13/48 (C32, SNU-423, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.824×** | -3.4 | 0.020 | 14/49 (PANC-1, LOX-IMVI, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.030 | 13/48 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.683×** | -3.0 | 0.053 | 9/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -2.8 | 0.096 | 11/48 (PANC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.2 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -28.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 154 | 0 | 9 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -17.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.1) |
| [[A-172 (line)]] | wt | 134 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +29.1) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 89.5 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.9) | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 56.8 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.89× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.132× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 30.9 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.3) | — |
| [[SW480 (line)]] | alt | 128 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -12.9) |
| [[A498 (line)]] | wt | 109 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 91.1 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.6) |
| [[HT-29 (line)]] | alt | 85.0 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -11.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 93.9 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -17.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.1) |
| [[PANC-1 (line)]] | alt | 149 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 78.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.293× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 87.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.6) | — |
| [[COLO 205 (line)]] | alt | 57.5 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 89.8 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.5) |
| [[Hs 766T (line)]] | wt | 95.5 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.324× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -10.2) |
| [[KATO III (line)]] | alt | 68.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -10.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 82.5 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.391× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.8) |
| [[LS 180 (line)]] | wt | 36.4 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 78.5 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.0) |
| [[SNU-423 (line)]] | alt | 106 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.2) |
| [[A-427 (line)]] | wt | 72.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.0) |
| [[C-33 A (line)]] | alt | 133 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.390× (z -9.5) |
| [[C32 (line)]] | wt | 105 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -11.9) |
| [[H4 (line)]] | wt | 115 | 1 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.48× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 129 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0627× (z -33.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.3) |
| [[SW 900 (line)]] | alt | 105 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.0) |
| [[HS-578T (line)]] | alt | 75.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 74.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -18.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 86.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.5) |
| [[A549 (line)]] | wt | 71.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.6) |
| [[HCT15 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 86.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 85.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -13.0) |
| [[RKO (line)]] | wt | 83.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.5) |
| [[AN3 CA (line)]] | alt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0876× (z -15.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.87× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.7) | — |
| [[J82 (line)]] | alt | 84.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.432× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 128 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0926× (z -11.6) |
| [[CHP-212 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GKAP1]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TBC1D19]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 | STRING 493 |
| [[TIPRL]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SSNA1]] | +0.61 | +0.47 / +0.48 | both halves | 2e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[HPF1]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | +0.60 | +0.49 / +0.47 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance; ⚠ in the vector space only through flagged drug-doses |
| [[SNAPIN]] | +0.59 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[RP9]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D17]] | +0.57 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[NBEA]] | +0.57 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[TRIM37]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ISCA2]] | +0.56 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[KMT2A]] | +0.55 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | -0.64 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | -0.64 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[DPY19L3-DT]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[DIDO1]] | -0.61 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[DCTN5]] | -0.61 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[LENG8-AS1]] | -0.61 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.61 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PIGW]] | -0.60 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[EXOSC3]] | -0.59 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ERVK13-1]] | -0.59 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[NIPBL-DT]] | -0.58 | -0.30 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIG]] | B | PKIG activity raises TTBK2's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without PKIG | 0.011 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[PRKD1]] | B | PRKD1 activity raises TTBK2's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without PRKD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[TPST1]] | B | TPST1 activity raises TTBK2's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without TPST1 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-6.2, 20.6); signed map (-18.0, -9.1). **Vector** length 119, 38.6% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +19.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +5.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -15.8 | -16.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.6 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.9 | -17.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -11.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | tau tubulin kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:42,738,730-42,920,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0847; previously SCA11 |
| Gene groups (HGNC) | Tau tubulin kinase family |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ55](https://www.uniprot.org/uniprotkb/Q6IQ55) (Tau-tubulin kinase 2):

> Serine/threonine kinase that acts as a key regulator of ciliogenesis: controls the initiation of ciliogenesis by binding to the distal end of the basal body and promoting the removal of CCP110, which caps the mother centriole, leading to the recruitment of IFT proteins, which build the ciliary axoneme. Has some substrate preference for proteins that are already phosphorylated on a Tyr residue at the +2 position relative to the phosphorylation site. Able to phosphorylate tau on serines in vitro. …

**Summary**, from NCBI Gene [146057](https://www.ncbi.nlm.nih.gov/gene/146057):

> This gene encodes a serine-threonine kinase that putatively phosphorylates tau and tubulin proteins. Mutations in this gene cause spinocerebellar ataxia type 11 (SCA11); a neurodegenerative disease characterized by progressive ataxia and atrophy of the cerebellum and brainstem. [provided by RefSeq, Aug 2009]

**Accessions** — [HGNC:19141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19141) · Entrez [146057](https://www.ncbi.nlm.nih.gov/gene/146057) · UniProt [Q6IQ55](https://www.uniprot.org/uniprotkb/Q6IQ55) · Ensembl [ENSG00000128881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128881)

## Data

Gene col 4927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4927); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4927]; `tensor/DDL_lfc|DDL_z.npy` [4927]; `embed/gene_vectors.npy` [4927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4927 or target_col == 4927). Every well: [[TTBK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTBK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
