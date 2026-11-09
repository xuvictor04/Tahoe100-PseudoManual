---
symbol: "BBS9"
type: "gene"
col: 4345
ensembl_id: "ENSG00000122507"
name: "Bardet-Biedl syndrome 9"
location: "7p14.3"
module: 76
arm: "+"
pooled_cpm: 117.97
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 38
n_dd_up_clean: 17
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# BBS9

*Bardet-Biedl syndrome 9* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.69× (z +5.6, q 2e-05, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.268× (z -19.5, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.255× (z -14.3, q 3e-44, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCDC1]] (+0.55, fdr 3e-05), [[RAB2A]] (+0.54, fdr 1e-04), [[LINC02937]] (+0.53, fdr 1e-05); moves opposite to [[DENND4B]] (-0.48, fdr 1e-04), [[LRR1]] (-0.48, fdr 5e-05), [[TEAD4]] (-0.48, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CRIP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UMAD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.6 | 2e-05 | 36/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.4 | 2e-05 | 38/47 (KATO III, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +4.8 | 3e-04 | 36/46 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.002 | 33/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.002 | 38/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.002 | 32/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.004 | 33/46 (C32, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +4.0 | 0.005 | 29/47 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.9 | 0.007 | 29/47 (LS 180, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **2.23×** | +3.8 | 0.009 | 34/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +3.5 | 0.020 | 28/49 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.02×** | +3.3 | 0.044 | 30/48 (A498, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.067 | 29/47 (SW480, C32, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.36×** | +3.0 | 0.093 | 21/47 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.093 | 30/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.093 | 27/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.093 | 24/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.093 | 25/48 (BT-474, C-33 A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.268×** | -19.5 | 0e+00 | 43/47 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.209×** | -16.4 | 0e+00 | 46/47 (H4, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.213×** | -16.2 | 0e+00 | 47/47 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.219×** | -15.3 | 0e+00 | 46/47 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.255×** | -14.3 | 3e-44 | 45/47 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.283×** | -13.2 | 6e-38 | 46/47 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.393×** | -9.4 | 5e-19 | 45/46 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.410×** | -9.3 | 8e-19 | 35/47 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.390×** | -9.3 | 9e-19 | 37/48 (RPMI-7951, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.427×** | -8.6 | 6e-16 | 42/46 (H4, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.453×** | -8.0 | 9e-14 | 32/43 (HepG2/C3A, SNU-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.458×** | -7.7 | 7e-13 | 35/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.485×** | -7.6 | 2e-12 | 42/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.494×** | -7.4 | 7e-12 | 43/47 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.470×** | -7.3 | 1e-11 | 32/44 (Panc 03.27, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.282×** | -5.9 | 1e-07 | 42/47 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -5.3 | 4e-06 | 37/47 (H4, HCT15, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.637×** | -4.4 | 3e-04 | 32/47 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.412×** | -4.1 | 8e-04 | 34/47 (NCI-H1792, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.610×** | -3.7 | 0.005 | 36/47 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.702×** | -3.5 | 0.011 | 29/47 (NCI-H2030, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.708×** | -3.4 | 0.014 | 28/46 (LOX-IMVI, H4, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.496×** | -3.3 | 0.020 | 29/47 (NCI-H23, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.498×** | -3.3 | 0.021 | 29/47 (NCI-H23, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.672×** | -3.0 | 0.052 | 25/47 (COLO 205, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -2.9 | 0.057 | 24/47 (HCT15, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 371 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -24.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.115× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 265 | 0 | 16 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0533× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 255 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -21.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.287× (z -9.5) |
| [[KATO III (line)]] | alt | 71.4 | 8 (1 ⚠) | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.27× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.191× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.268× (z -10.1) |
| [[SW480 (line)]] | alt | 108 | 1 | 13 (9 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.97× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -19.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.133× (z -17.6) |
| [[HEC-1-A (line)]] | alt | 284 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -23.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.270× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 137 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0834× (z -30.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.215× (z -13.3) |
| [[SW 900 (line)]] | alt | 155 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.217× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -27.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 96.3 | 1 (1 ⚠) | 11 (7 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.9) ⚠ cell-cycle shift, explains ~79% of this change | [[Harringtonine (drug)]] 0.5 µM 0.134× (z -15.6) |
| [[HOP62 (line)]] | alt | 171 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -25.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -17.8) |
| [[Hs 766T (line)]] | wt | 115 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0927× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.210× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 1 (1 ⚠) | 10 (6 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.59× (z +10.4) ⚠ position not correctable | [[Digitoxin (drug)]] 0.5 µM 0.130× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 201 | 0 | 11 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -20.5) |
| [[PANC-1 (line)]] | alt | 46.5 | 3 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.227× (z -10.8) |
| [[HCT15 (line)]] | alt | 186 | 0 | 10 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~35% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.190× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 75.3 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -14.2) |
| [[C32 (line)]] | wt | 158 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0870× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.231× (z -11.0) |
| [[HS-578T (line)]] | alt | 238 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.216× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0886× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.187× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.230× (z -11.8) |
| [[A-172 (line)]] | wt | 139 | 1 | 7 (6 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.79× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.212× (z -10.6) |
| [[A498 (line)]] | wt | 157 | 0 | 8 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0854× (z -18.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.152× (z -13.6) |
| [[COLO 205 (line)]] | alt | 135 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -21.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.196× (z -13.7) |
| [[HT-29 (line)]] | alt | 48.7 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.95× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.259× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.286× (z -8.7) |
| [[SNU-1 (line)]] | wt | 156 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.103× (z -16.1) |
| [[SHP-77 (line)]] | alt | 131 | 1 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.255× (z -12.3) |
| [[SNU-423 (line)]] | alt | 113 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -16.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -12.4) |
| [[A549 (line)]] | wt | 103 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -13.1) |
| [[LS 180 (line)]] | wt | 87.6 | 1 (1 ⚠) | 5 (4 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +8.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -12.6) |
| [[SW 1088 (line)]] | alt | 330 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0289× (z -15.7) |
| [[A-427 (line)]] | wt | 105 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LoVo (line)]] | wt | 99.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 160 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HepG2_C3A (line)]] | wt | 64.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0696× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[RKO (line)]] | wt | 51.3 | 1 | 2 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 3.69× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.177× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -9.2) |
| [[SW1417 (line)]] | alt | 54.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[BT-474 (line)]] | alt | 43.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.19× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.219× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -11.2) |
| [[J82 (line)]] | alt | 42.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.200× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0837× (z -11.2) |
| [[CHP-212 (line)]] | wt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.250× (z -8.8) |
| [[SW 1271 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCDC1]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[RAB2A]] | +0.54 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[LINC02937]] | +0.53 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MBD5]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ATG14]] | +0.51 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[RPS6KC1]] | +0.51 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[TNKS]] | +0.51 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[COMMD9]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[C1QTNF3-AMACR]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[GUSBP1-1]] | +0.49 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[FXR1]] | +0.49 | +0.24 / +0.55 | both halves | 5e-04 |  |
| [[CYB5R4]] | +0.49 | +0.35 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND4B]] | -0.48 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[LRR1]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[TEAD4]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PLEKHH1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[NUP188]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SUV39H2]] | -0.47 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[AGAP13P]] | -0.46 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ACTR3B]] | -0.46 | -0.26 / -0.40 | both halves | 3e-04 |  |
| [[PKN3]] | -0.44 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[AGAP9]] | -0.44 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[CTPS1]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CCNJ]] | -0.44 | -0.28 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRIP1]] | B | CRIP1 activity lowers BBS9's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 1.71× higher at baseline in the lines without CRIP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[MAP2K1]] | B | MAP2K1 activity lowers BBS9's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CRIP1]] | C | CRIP1 activity weakens BBS9's drug response | lines that do not express CRIP1 (27) vs lines expressing it (21) | the lines without CRIP1 respond 1.02× as strongly (z diff -0.73); strongest at Dinaciclib 0.5 µM: 0.34x vs 0.51x (z diff -2.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UMAD1]] | C | BBS9's natural level strengthens UMAD1's drug response | BBS9's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.34; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.7, -14.3); signed map (-20.4, 3.2). **Vector** length 85.9, 38.3% of its response variance represented; |z| ≥ 3 in 1,875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.4 | -16.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.2 | -16.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.0 | +3.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.6 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.4 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -4.2 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.7 | -19.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:33,109,557-33,877,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B1, PTHB1 |
| Gene groups (HGNC) | BBSome |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3SYG4](https://www.uniprot.org/uniprotkb/Q3SYG4) (Protein PTHB1):

> The BBSome complex is thought to function as a coat complex required for sorting of specific membrane proteins to the primary cilia. The BBSome complex is required for ciliogenesis but is dispensable for centriolar satellite function. This ciliogenic function is mediated in part by the Rab8 GDP/GTP exchange factor, which localizes to the basal body and contacts the BBSome. Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane. Firstly the BBSome associates with the …

**Summary**, from NCBI Gene [27241](https://www.ncbi.nlm.nih.gov/gene/27241):

> This gene is downregulated by parathyroid hormone in osteoblastic cells, and therefore is thought to be involved in parathyroid hormone action in bones. The exact function of this gene has not yet been determined. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:30000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30000) · Entrez [27241](https://www.ncbi.nlm.nih.gov/gene/27241) · UniProt [Q3SYG4](https://www.uniprot.org/uniprotkb/Q3SYG4) · Ensembl [ENSG00000122507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122507)

## Data

Gene col 4345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4345); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4345]; `tensor/DDL_lfc|DDL_z.npy` [4345]; `embed/gene_vectors.npy` [4345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4345 or target_col == 4345). Every well: [[BBS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
