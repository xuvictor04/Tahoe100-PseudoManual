---
symbol: "FBXO25"
type: "gene"
col: 7173
ensembl_id: "ENSG00000147364"
name: "F-box protein 25"
location: "8p23.3"
module: 76
arm: "+"
pooled_cpm: 29.83
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# FBXO25

*F-box protein 25* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.39× (z +19.2, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.210× (z -34.2, q 0e+00, down in 44 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.263× (z -15.3, q 0e+00, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01881]] (+0.84, fdr 7e-06), [[SPSB3]] (+0.69, fdr 1e-05), [[CCDC28A]] (+0.67, fdr 1e-04); moves opposite to [[ZNF629]] (-0.55, fdr 4e-05), [[DNAJC11]] (-0.52, fdr 5e-05), [[DHX37]] (-0.51, fdr 1e-04).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +19.2 | 0e+00 | 40/44 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +18.5 | 0e+00 | 42/44 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +15.3 | 0e+00 | 38/44 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +9.1 | 1e-17 | 33/44 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.6 | 3e-09 | 19/41 (C-33 A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +6.0 | 1e-07 | 22/42 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.0 | 5e-05 | 15/44 (NCI-H2347, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.5 | 4e-04 | 15/44 (HOP62, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.003 | 15/42 (SNU-1, H4, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.032 | 12/36 (HepG2/C3A, SW480, …) | all doses, flat | composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.14× | +3.3 | 0.047 | 5/44 (SHP-77, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.048 | 9/43 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.051 | 11/43 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.063 | 5/43 (HCT15, HEC-1-A, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.067 | 5/44 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.067 | 2/44 (CFPAC-1, LS 180) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.210×** | -34.2 | 0e+00 | 44/44 (A498, HS-578T, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.263×** | -15.3 | 0e+00 | 40/43 (A549, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.273×** | -14.9 | 0e+00 | 40/42 (SNU-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.294×** | -14.0 | 1e-42 | 39/43 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.532×** | -13.8 | 3e-41 | 36/44 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.309×** | -13.5 | 2e-39 | 39/42 (LoVo, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.391×** | -10.8 | 5e-25 | 39/43 (HS-578T, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -10.7 | 5e-25 | 26/43 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.622×** | -9.8 | 7e-21 | 32/43 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.477×** | -9.6 | 4e-20 | 32/44 (A498, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.651×** | -9.4 | 3e-19 | 31/44 (A-172, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -9.2 | 2e-18 | 31/44 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -9.1 | 3e-18 | 29/44 (HS-578T, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.679×** | -8.5 | 1e-15 | 25/44 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -7.5 | 2e-12 | 22/44 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.614×** | -6.3 | 8e-09 | 26/44 (A549, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.732×** | -6.3 | 1e-08 | 23/42 (HS-578T, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 61.6 | 0 | 14 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -19.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.261× (z -13.3) |
| [[A-172 (line)]] | wt | 53.3 | 0 | 13 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -16.7) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -12.1) |
| [[SW480 (line)]] | alt | 29.5 | 7 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.61× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -14.9) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 24.1 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -20.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.128× (z -10.2) |
| [[LoVo (line)]] | wt | 48.8 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -17.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.402× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 35.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.74× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -14.1) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 21.4 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -13.4) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.335× (z -8.6) |
| [[SNU-1 (line)]] | wt | 40.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.0347× (z -11.1) |
| [[A549 (line)]] | wt | 45.9 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -16.0) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0865× (z -12.6) |
| [[SW1417 (line)]] | alt | 26.2 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.07× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -12.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0946× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 48.8 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -18.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.118× (z -12.2) |
| [[KATO III (line)]] | alt | 76.9 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -15.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.397× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 15.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.2) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -12.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.216× (z -13.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.112× (z -9.8) |
| [[A-427 (line)]] | wt | 35.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +15.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 48.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -10.6) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -12.0) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 16.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -16.5) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -12.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0550× (z -11.4) |
| [[SHP-77 (line)]] | alt | 121 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -16.4) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.278× (z -9.7) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.181× (z -12.5) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -11.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.210× (z -9.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -12.4) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -11.2) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -12.1) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -10.7) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0674× (z -15.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01881]] | +0.84 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.69 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.67 | +0.36 / +0.74 | both halves | 1e-04 |  |
| [[REPS2]] | +0.65 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[INPP5K]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[MBTPS1]] | +0.62 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[AUH]] | +0.62 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[ANAPC1P2]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[ABTB1]] | +0.61 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[COQ8A]] | +0.61 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[MARF1]] | +0.61 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[ALDH6A1]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF629]] | -0.55 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DHX37]] | -0.51 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[GPATCH4]] | -0.51 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TAF2]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CUEDC1]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CDK12]] | -0.50 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[DPP3]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PDE12]] | -0.49 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ZNF195]] | -0.49 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[AFG1L]] | -0.49 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[SLC9A8]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FBXO25's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.4, -45.4); signed map (-19.2, 10.3). **Vector** length 116, 30.5% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +19.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +18.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +15.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.4 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.0 | -34.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.8 | -14.9 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -14.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.8 | -13.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.6 | -15.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.6 | -10.8 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:406,428-477,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX25 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCJ0](https://www.uniprot.org/uniprotkb/Q8TCJ0) (F-box only protein 25):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. May play a role in accumulation of expanded polyglutamine (polyQ) protein huntingtin (HTT) (By similarity).

**Summary**, from NCBI Gene [26260](https://www.ncbi.nlm.nih.gov/gene/26260):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13596) · Entrez [26260](https://www.ncbi.nlm.nih.gov/gene/26260) · UniProt [Q8TCJ0](https://www.uniprot.org/uniprotkb/Q8TCJ0) · Ensembl [ENSG00000147364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147364)

## Data

Gene col 7173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7173); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7173]; `tensor/DDL_lfc|DDL_z.npy` [7173]; `embed/gene_vectors.npy` [7173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7173 or target_col == 7173). Every well: [[FBXO25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
