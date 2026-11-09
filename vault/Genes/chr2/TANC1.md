---
symbol: "TANC1"
type: "gene"
col: 3631
ensembl_id: "ENSG00000115183"
name: "tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 1"
location: "2q24.2"
module: 163
arm: "+"
pooled_cpm: 192.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# TANC1

*tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 1* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.33× (z +6.9, q 3e-09, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.452× (z -19.1, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC1]] (+0.64, fdr 9e-06), [[CDC42SE2]] (+0.62, fdr 1e-05), [[RANBP9]] (+0.60, fdr 1e-05); moves opposite to [[PIGL]] (-0.53, fdr 3e-05), [[SLF2]] (-0.52, fdr 3e-05), [[ZNF554]] (-0.52, fdr 3e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +6.9 | 3e-09 | 28/48 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.8 | 3e-09 | 33/48 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +5.9 | 7e-07 | 31/49 (J82, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.8 | 7e-07 | 29/48 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.18× | +5.5 | 4e-06 | 22/49 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.6 | 3e-04 | 15/48 (A-172, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.008 | 20/47 (J82, C-33 A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.17× | +3.8 | 0.012 | 20/49 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.11× | +3.6 | 0.019 | 15/48 (SNU-1, A-427, …) | all doses, flat | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.5 | 0.029 | 2/50 (MIA PaCa-2, NCI-H1792) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.30×** | +3.3 | 0.047 | 19/45 (J82, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.452×** | -19.1 | 0e+00 | 45/48 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -16.5 | 0e+00 | 38/44 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.505×** | -16.4 | 0e+00 | 43/49 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.730×** | -10.7 | 1e-24 | 32/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -10.6 | 3e-24 | 35/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -9.2 | 3e-18 | 34/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.685×** | -9.1 | 8e-18 | 35/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.666×** | -9.0 | 1e-17 | 30/45 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -8.9 | 3e-17 | 32/47 (C32, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.716×** | -8.0 | 7e-14 | 32/48 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.748×** | -7.0 | 2e-10 | 35/48 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.743×** | -6.9 | 3e-10 | 31/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.790×** | -5.7 | 6e-07 | 33/48 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.797×** | -5.5 | 2e-06 | 27/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.806×** | -5.2 | 8e-06 | 28/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.847× | -3.7 | 0.007 | 19/47 (C32, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.858× | -3.7 | 0.007 | 18/48 (SW 900, C32, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.861× | -3.6 | 0.009 | 20/47 (C32, KATO III, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.858× | -3.5 | 0.011 | 19/47 (H4, C32, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.862× | -3.4 | 0.016 | 17/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.872× | -3.3 | 0.024 | 13/48 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.867× | -3.2 | 0.035 | 11/48 (SW 1271, A-172, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.914× | -3.0 | 0.052 | 15/49 (LS 180, C32, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.791×** | -2.9 | 0.067 | 15/48 (C32, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 362 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -18.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -15.4) |
| [[SW480 (line)]] | alt | 200 | 0 | 13 (11 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.275× (z -25.3) |
| [[C32 (line)]] | wt | 655 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.263× (z -19.8) |
| [[SK-MEL-2 (line)]] | alt | 308 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -33.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.226× (z -19.5) |
| [[HT-29 (line)]] | alt | 296 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.230× (z -20.2) |
| [[LoVo (line)]] | wt | 263 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -15.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -13.5) |
| [[LS 180 (line)]] | wt | 383 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.422× (z -11.1) |
| [[A-172 (line)]] | wt | 132 | 3 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.0) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.465× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 194 | 1 | 6 (5 ⚠) | [[Belinostat (drug)]] 5 µM 2.01× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -12.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.536× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 258 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.636× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 158 | 1 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +10.0) ⚠ cell-cycle shift, explains ~3% of this change | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -14.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.539× (z -9.1) |
| [[A-427 (line)]] | wt | 121 | 1 (1 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.59× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.257× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 228 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 249 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -9.1) |
| [[J82 (line)]] | alt | 145 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.05 µM 1.93× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -11.9) |
| [[SW1417 (line)]] | alt | 351 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.430× (z -12.3) |
| [[CHP-212 (line)]] | wt | 303 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.255× (z -10.8) |
| [[HOP62 (line)]] | alt | 91.9 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.6) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 1.84× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.468× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.506× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 131 | 1 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +10.5) ⚠ cell-cycle shift, explains ~80% of this change | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -11.9) |
| [[SW48 (line)]] | wt | 319 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.249× (z -13.3) |
| [[A498 (line)]] | wt | 250 | 1 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.06× (z +10.5) ⚠ cell-cycle shift, explains ~80% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -13.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 303 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.0) ⚠ cell-cycle shift, explains ~58% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 83.7 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.1) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 2.15× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.273× (z -14.8) |
| [[SW 900 (line)]] | alt | 191 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.345× (z -14.0) |
| [[AN3 CA (line)]] | alt | 250 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -17.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.257× (z -11.6) |
| [[COLO 205 (line)]] | alt | 250 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.484× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.515× (z -11.1) |
| [[SNU-423 (line)]] | alt | 84.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -10.3) |
| [[H4 (line)]] | wt | 205 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -10.3) |
| [[HCT15 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -9.8) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.390× (z -10.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.19× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -9.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 151 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -12.3) |
| [[PANC-1 (line)]] | alt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.535× (z -11.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 137 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.9) ⚠ cell-cycle shift, explains ~3% of this change | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A549 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 67.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +14.5) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.445× (z -9.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC1]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CDC42SE2]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RANBP9]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[DLG3]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ANXA11]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CASZ1]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN14]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TGFBR3]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TRIM2]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PIK3C2B]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 | same gene group |
| [[CPOX]] | +0.54 | +0.46 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGL]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 | same gene group |
| [[SLF2]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ZNF554]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RPSAP52]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[IBA57]] | -0.50 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[SLC7A6OS]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[CRYM]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ZNF274]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TMEM132D]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZNF776]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ST3GAL3]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TANC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPINT1]] | B | SPINT1 activity strengthens TANC1's drug response | lines that do not express SPINT1 (25) vs lines expressing it (24) | the lines without SPINT1 respond 0.62× as strongly (z diff +2.39); strongest at Dinaciclib 0.05 µM: 0.76x vs 0.58x (z diff +3.3) | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.8, -5.4); signed map (-19.4, 18.8). **Vector** length 124, 39.8% of its response variance represented; |z| ≥ 3 in 1,526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.8 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.4 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.2 | +0.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.4 | -19.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.0 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.9 | -10.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:158,968,640-159,232,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1728, ROLSB |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Tetratricopeptide repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D5](https://www.uniprot.org/uniprotkb/Q9C0D5) (Protein TANC1):

> May be a scaffold component in the postsynaptic density.

**Summary**, from NCBI Gene [85461](https://www.ncbi.nlm.nih.gov/gene/85461):

> Predicted to be involved in regulation of postsynapse organization. Predicted to act upstream of or within dendritic spine maintenance; myoblast fusion; and visual learning. Predicted to be located in several cellular components, including axon terminus; neuronal cell body; and postsynaptic density. Predicted to be active in glutamatergic synapse and postsynaptic density, intracellular component. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29364) · Entrez [85461](https://www.ncbi.nlm.nih.gov/gene/85461) · UniProt [Q9C0D5](https://www.uniprot.org/uniprotkb/Q9C0D5) · Ensembl [ENSG00000115183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115183)

## Data

Gene col 3631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3631); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3631]; `tensor/DDL_lfc|DDL_z.npy` [3631]; `embed/gene_vectors.npy` [3631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3631 or target_col == 3631). Every well: [[TANC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TANC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
