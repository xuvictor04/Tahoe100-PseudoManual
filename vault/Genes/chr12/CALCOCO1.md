---
symbol: "CALCOCO1"
type: "gene"
col: 261
ensembl_id: "ENSG00000012822"
name: "calcium binding and coiled-coil domain 1"
location: "12q13.13"
module: 76
arm: "+"
pooled_cpm: 30.46
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 28
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# CALCOCO1

*calcium binding and coiled-coil domain 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.05× (z +9.0, q 1e-16, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.206× (z -19.8, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.411× (z -11.2, q 1e-26, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRIPT]] (+0.77, fdr 7e-06), [[CCDC28A]] (+0.71, fdr 7e-06), [[YPEL3]] (+0.71, fdr 7e-06); moves opposite to [[NAA15]] (-0.54, fdr 1e-05), [[NETO2]] (-0.54, fdr 3e-05), [[CEP83]] (-0.53, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +9.0 | 1e-16 | 39/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +8.8 | 5e-16 | 36/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +8.3 | 2e-14 | 36/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +5.6 | 3e-06 | 29/48 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.3 | 1e-05 | 29/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 1e-04 | 28/47 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.49×** | +4.2 | 0.002 | 23/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.06×** | +4.0 | 0.004 | 25/48 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.39×** | +3.9 | 0.005 | 24/48 (PANC-1, HCT15, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.009 | 20/47 (C32, Hs 766T, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +3.6 | 0.018 | 18/47 (A498, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +3.3 | 0.038 | 14/48 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.072 | 15/48 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.41×** | +3.1 | 0.078 | 8/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.084 | 11/48 (RPMI-7951, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.096 | 17/48 (A-427, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.206×** | -19.8 | 0e+00 | 47/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.383×** | -17.0 | 0e+00 | 40/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.411×** | -11.2 | 1e-26 | 35/47 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.391×** | -10.1 | 5e-22 | 40/48 (COLO 205, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.449×** | -10.1 | 9e-22 | 38/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.451×** | -10.0 | 2e-21 | 43/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.465×** | -9.6 | 5e-20 | 41/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.226×** | -8.2 | 1e-14 | 45/47 (NCI-H1792, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.229×** | -8.2 | 2e-14 | 42/47 (NCI-H1792, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.235×** | -8.0 | 5e-14 | 44/47 (SW1417, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.273×** | -7.2 | 3e-11 | 41/48 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.578×** | -6.9 | 3e-10 | 31/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.295×** | -6.8 | 5e-10 | 41/46 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.548×** | -6.5 | 3e-09 | 28/46 (NCI-H1792, H4, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.485×** | -6.5 | 3e-09 | 39/48 (LoVo, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.625×** | -5.6 | 8e-07 | 32/48 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.642×** | -5.6 | 8e-07 | 34/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.552×** | -5.3 | 3e-06 | 38/48 (SW480, COLO 205, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.625×** | -4.2 | 6e-04 | 24/48 (C-33 A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.004 | 21/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.538×** | -3.4 | 0.014 | 22/46 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.772×** | -3.1 | 0.050 | 19/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 93.5 | 0 | 15 (10 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0454× (z -24.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -14.5) |
| [[COLO 205 (line)]] | alt | 45.4 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0103× (z -25.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0927× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 28.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.210× (z -10.9) |
| [[PANC-1 (line)]] | alt | 20.0 | 3 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.08× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -21.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.1) |
| [[SW480 (line)]] | alt | 59.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -17.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.246× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 14.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.51× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 33.6 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.111× (z -17.0) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -16.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -13.6) |
| [[C32 (line)]] | wt | 21.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -13.3) |
| [[H4 (line)]] | wt | 33.1 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0677× (z -13.0) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -11.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -9.5) |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -8.5) |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -19.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 26.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[KATO III (line)]] | alt | 50.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 59.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.8) |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.187× (z -12.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0377× (z -10.8) |
| [[A549 (line)]] | wt | 20.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -10.7) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -11.1) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -12.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0913× (z -14.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -8.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -9.1) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0777× (z -9.2) |
| [[HS-578T (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.207× (z -10.8) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.234× (z -9.3) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.152× (z -12.0) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -9.9) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -10.3) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.147× (z -12.0) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.171× (z -9.7) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.231× (z -9.5) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -10.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRIPT]] | +0.77 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CCDC28A]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[YPEL3]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 | STRING 406 |
| [[FOXO4]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[UBXN6]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[SERINC1]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[CCNDBP1]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ATF6B]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PIK3C3]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NETO2]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CEP83]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SNHG26]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TASOR2]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TCERG1]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PPRC1]] | -0.51 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[NOP56]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TERT]] | -0.51 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[RAD51D]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NOC3L]] | -0.51 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.8, -46.4); signed map (-18.2, 9.5). **Vector** length 111, 34.5% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | -1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.0 | +2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -19.8 |
|  | [[EX229 (drug)]] 5 µM |  | -7.9 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.7 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.5 | -8.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.6 | -6.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.5 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium binding and coiled-coil domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,708,517-53,727,745 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1536, calphoglin, Cocoa |
| Gene groups (HGNC) | Zinc fingers UBZ1 CCHH-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1Z2](https://www.uniprot.org/uniprotkb/Q9P1Z2) (Calcium-binding and coiled-coil domain-containing protein 1):

> Functions as a coactivator for aryl hydrocarbon and nuclear receptors (NR). Recruited to promoters through its contact with the N-terminal basic helix-loop-helix-Per-Arnt-Sim (PAS) domain of transcription factors or coactivators, such as NCOA2. During ER-activation acts synergistically in combination with other NCOA2-binding proteins, such as EP300, CREBBP and CARM1. Involved in the transcriptional activation of target genes in the Wnt/CTNNB1 pathway. Functions as a secondary coactivator in …

**Summary**, from NCBI Gene [57658](https://www.ncbi.nlm.nih.gov/gene/57658):

> Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; beta-catenin binding activity; and transcription coactivator activity. Involved in positive regulation of DNA-templated transcription and positive regulation of gene expression. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29306) · Entrez [57658](https://www.ncbi.nlm.nih.gov/gene/57658) · UniProt [Q9P1Z2](https://www.uniprot.org/uniprotkb/Q9P1Z2) · Ensembl [ENSG00000012822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012822)

## Data

Gene col 261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 261); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 261]; `tensor/DDL_lfc|DDL_z.npy` [261]; `embed/gene_vectors.npy` [261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 261 or target_col == 261). Every well: [[CALCOCO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALCOCO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
