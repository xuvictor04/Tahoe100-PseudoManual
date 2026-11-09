---
symbol: "TCP11L2"
type: "gene"
col: 9231
ensembl_id: "ENSG00000166046"
name: "t-complex 11 like 2"
location: "12q23.3"
module: 69
arm: "+"
pooled_cpm: 40.11
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 61
n_dd_up_clean: 11
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# TCP11L2

*t-complex 11 like 2* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Bimiralisib (drug)]] 5 µM: 2.06× (z +4.6, q 0.002, up in 30 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 61 drug-doses (28 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.139× (z -24.2, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.319× (z -15.1, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.80, fdr 7e-06), [[JMY]] (+0.79, fdr 7e-06), [[UBXN7]] (+0.77, fdr 7e-06); moves opposite to [[NAA15]] (-0.68, fdr 7e-06), [[PDSS1]] (-0.64, fdr 1e-05), [[TCERG1]] (-0.62, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FBXO32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **2.06×** | +4.6 | 0.002 | 30/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 0.006 | 20/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.39×** | +4.1 | 0.008 | 23/49 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.008 | 27/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.008 | 17/48 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.008 | 20/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.21×** | +3.6 | 0.027 | 25/48 (KATO III, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.066 | 19/47 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.066 | 16/48 (SW480, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.070 | 10/47 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.65×** | +3.2 | 0.070 | 17/49 (KATO III, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +3.2 | 0.073 | 8/48 (Panc 03.27, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BI-3406 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.092 | 11/49 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.092 | 12/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 29 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 61 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 28 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.139×** | -24.2 | 0e+00 | 47/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.318×** | -21.4 | 0e+00 | 43/47 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.221×** | -19.9 | 0e+00 | 45/47 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.241×** | -18.1 | 0e+00 | 46/47 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.318×** | -15.1 | 0e+00 | 44/48 (LS 180, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.319×** | -15.1 | 0e+00 | 44/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.327×** | -14.8 | 0e+00 | 43/45 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.313×** | -14.8 | 0e+00 | 34/36 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.362×** | -13.4 | 3e-39 | 45/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.356×** | -13.1 | 2e-37 | 40/46 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.170×** | -11.3 | 9e-28 | 45/47 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.174×** | -11.1 | 4e-27 | 46/47 (HCT15, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.177×** | -11.0 | 1e-26 | 43/46 (SNU-423, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.452×** | -10.5 | 5e-24 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.426×** | -10.4 | 7e-24 | 31/37 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.201×** | -10.2 | 7e-23 | 42/46 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.208×** | -10.0 | 5e-22 | 43/47 (A549, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.488×** | -9.5 | 8e-20 | 38/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.369×** | -9.4 | 1e-19 | 47/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.515×** | -8.8 | 5e-17 | 36/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.508×** | -8.4 | 8e-16 | 44/47 (SW 900, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.515×** | -8.3 | 3e-15 | 37/47 (CFPAC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.325×** | -7.1 | 2e-11 | 40/45 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.476×** | -7.0 | 5e-11 | 42/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.517×** | -6.2 | 9e-09 | 39/48 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.81 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.3 | 0 | 21 (16 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -23.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.175× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 73.3 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0550× (z -32.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -24.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.177× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 33.3 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -19.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -17.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -13.0) |
| [[PANC-1 (line)]] | alt | 19.9 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0878× (z -17.2) |
| [[SNU-423 (line)]] | alt | 85.9 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -10.0) |
| [[HT-29 (line)]] | alt | 54.1 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 11 (10 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0573× (z -18.8) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.0) |
| [[A549 (line)]] | wt | 50.1 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -21.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 34.7 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -9.7) |
| [[C32 (line)]] | wt | 36.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0835× (z -22.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0953× (z -15.1) |
| [[SW480 (line)]] | alt | 30.3 | 0 | 10 (8 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.124× (z -14.9) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.278× (z -9.9) |
| [[A-172 (line)]] | wt | 34.6 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0739× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -12.3) |
| [[Hs 766T (line)]] | wt | 46.2 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -16.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 98.0 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0492× (z -20.4) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 6 (3 ⚠) | — | [[Isocorydine (drug)]] 0.5 µM 0.123× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 47.3 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.0780× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 48.0 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0974× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0368× (z -14.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0996× (z -10.2) |
| [[SW 900 (line)]] | alt | 42.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[EX229 (drug)]] 0.05 µM 0.230× (z -8.9) |
| [[HS-578T (line)]] | alt | 33.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -12.3) |
| [[LoVo (line)]] | wt | 51.4 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.107× (z -14.0) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.181× (z -10.2) |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0743× (z -17.4) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0778× (z -8.9) |
| [[COLO 205 (line)]] | alt | 47.3 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.134× (z -10.5) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 18.4 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0741× (z -15.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 34.3 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.145× (z -13.1) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 64.4 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0645× (z -17.1) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0729× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -12.8) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0805× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.228× (z -8.5) |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.118× (z -12.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0568× (z -8.5) |
| [[H4 (line)]] | wt | 33.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0732× (z -12.4) |
| [[A-427 (line)]] | wt | 22.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0741× (z -9.9) |
| [[J82 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.109× (z -12.3) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -9.9) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -9.5) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[RKO (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -10.0) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.80 | +0.70 / +0.84 | both halves | 7e-06 |  |
| [[JMY]] | +0.79 | +0.60 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[UBXN7]] | +0.77 | +0.69 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RB1CC1]] | +0.75 | +0.59 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[HBP1]] | +0.73 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[SERINC1]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MKRN1]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.70 | +0.58 / +0.79 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.69 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[SLU7]] | +0.69 | +0.39 / +0.75 | both halves | 5e-05 |  |
| [[FBXL20]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[MXI1]] | +0.68 | +0.71 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | -0.68 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[PDSS1]] | -0.64 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[TCERG1]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[UBE2N]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[IPO9]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.59 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[WDR4]] | -0.59 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[EIF2B3]] | -0.57 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[PUS1]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[AGK]] | -0.57 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[NME1]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[NOC3L]] | -0.56 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO32]] | B | FBXO32 activity raises TCP11L2's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without FBXO32 | 0.022 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TCP11L2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[YPEL3]] | B | YPEL3 activity raises TCP11L2's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without YPEL3 | 0.084 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[GALNT14]] | B | GALNT14 activity raises TCP11L2's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.24× lower at baseline in the lines without GALNT14 | 0.088 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.5, -44.6); signed map (-14.1, 9.9). **Vector** length 97.3, 34.5% of its response variance represented; |z| ≥ 3 in 1,855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +3.2 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -4.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | -0.0 |
|  | [[Alpelisib (drug)]] 5 µM |  | +2.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.5 | -24.2 |
|  | [[EX229 (drug)]] 5 µM |  | -9.4 | -11.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.9 | -11.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.3 | -10.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.5 | -10.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.3 | -11.1 |

## What is on record

|  |  |
|---|---|
| Name | t-complex 11 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,301,929-106,347,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40368 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4U5](https://www.uniprot.org/uniprotkb/Q8N4U5) (T-complex protein 11-like protein 2):

> Promotes the migration of muscle-derived satellite cells (MDSCs) during differentiation throught interaction with FMNL2 and therefore may participate in microfilament assembly.

**Summary**, from NCBI Gene [255394](https://www.ncbi.nlm.nih.gov/gene/255394):

> Predicted to be involved in muscle cell migration and signal transduction. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28627) · Entrez [255394](https://www.ncbi.nlm.nih.gov/gene/255394) · UniProt [Q8N4U5](https://www.uniprot.org/uniprotkb/Q8N4U5) · Ensembl [ENSG00000166046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166046)

## Data

Gene col 9231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9231); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9231]; `tensor/DDL_lfc|DDL_z.npy` [9231]; `embed/gene_vectors.npy` [9231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9231 or target_col == 9231). Every well: [[TCP11L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCP11L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
