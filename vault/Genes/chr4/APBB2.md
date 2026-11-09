---
symbol: "APBB2"
type: "gene"
col: 8757
ensembl_id: "ENSG00000163697"
name: "amyloid beta precursor protein binding family B member 2"
location: "4p14-p13"
module: 84
arm: "+"
pooled_cpm: 263.83
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# APBB2

*amyloid beta precursor protein binding family B member 2* — 4p14-p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.34× (z +6.8, q 4e-09, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.421× (z -19.7, q 0e+00, down in 39 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.642× (z -13.8, q 3e-41, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABTB3]] (+0.63, fdr 1e-05), [[WDFY2]] (+0.62, fdr 1e-05), [[PLEK2]] (+0.58, fdr 4e-05); moves opposite to [[MLLT6]] (-0.51, fdr 4e-05), [[AEBP2]] (-0.49, fdr 3e-04), [[GTF2IRD2]] (-0.49, fdr 3e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NLRP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +6.8 | 4e-09 | 32/48 (NCI-H460, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +6.8 | 4e-09 | 28/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +6.1 | 2e-07 | 27/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.7 | 2e-06 | 23/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +4.7 | 3e-04 | 24/48 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.15× | +4.2 | 0.002 | 14/48 (HEC-1-A, SW 900, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.1 | 0.004 | 15/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.022 | 22/49 (NCI-H460, J82, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.062 | 16/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.062 | 15/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.15× | +3.2 | 0.075 | 18/48 (COLO 205, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8757.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.421×** | -19.7 | 0e+00 | 39/49 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -16.1 | 0e+00 | 36/44 (LS 180, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -13.8 | 3e-41 | 34/49 (LOX-IMVI, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -13.2 | 1e-37 | 40/47 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -13.0 | 2e-36 | 37/45 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -10.5 | 9e-24 | 37/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.645×** | -10.0 | 1e-21 | 35/48 (NCI-H460, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.701×** | -8.1 | 4e-14 | 34/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.702×** | -8.1 | 4e-14 | 36/48 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.781×** | -7.7 | 6e-13 | 26/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.707×** | -7.6 | 1e-12 | 32/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.744×** | -6.7 | 7e-10 | 28/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -6.0 | 6e-08 | 31/48 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.571×** | -5.8 | 3e-07 | 29/49 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -5.6 | 6e-07 | 30/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -5.6 | 9e-07 | 26/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -5.5 | 1e-06 | 28/48 (RPMI-7951, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -4.9 | 3e-05 | 26/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -4.8 | 5e-05 | 23/48 (NCI-H2347, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -4.4 | 4e-04 | 26/48 (HCT15, SW1417, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.829×** | -4.1 | 0.001 | 23/49 (H4, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.834× | -3.8 | 0.003 | 23/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.806×** | -3.1 | 0.041 | 15/47 (C32, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.877× | -3.0 | 0.055 | 10/48 (A498, LoVo, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.880× | -2.9 | 0.065 | 10/48 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 583 | 0 | 17 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 626 | 0 | 16 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -22.3) |
| [[NCI-H1792 (line)]] | alt | 692 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -20.7) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 108 | 5 (1 ⚠) | 8 (7 ⚠) | [[Belinostat (drug)]] 5 µM 2.41× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -14.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.440× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 414 | 0 | 12 (4 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.327× (z -11.9) |
| [[PANC-1 (line)]] | alt | 229 | 1 (1 ⚠) | 8 (7 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.08× (z +11.2) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.318× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.4) |
| [[C-33 A (line)]] | alt | 1,289 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -18.5) |
| [[LoVo (line)]] | wt | 299 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -14.9) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.421× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 217 | 1 (1 ⚠) | 7 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.02× (z +8.8) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.350× (z -13.0) |
| [[H4 (line)]] | wt | 281 | 2 (1 ⚠) | 5 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.29× (z +11.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.60× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.319× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.355× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 192 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -11.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.451× (z -9.7) |
| [[KATO III (line)]] | alt | 253 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 177 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -21.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 269 | 1 | 5 (3 ⚠) | [[Trametinib (drug)]] 0.05 µM 1.56× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.448× (z -11.5) |
| [[A498 (line)]] | wt | 284 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.0) |
| [[HCT15 (line)]] | alt | 539 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.267× (z -16.6) |
| [[Hs 766T (line)]] | wt | 221 | 1 (1 ⚠) | 4 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.37× (z +9.0) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -10.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 569 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 228 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -18.2) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 255 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.3) |
| [[C32 (line)]] | wt | 114 | 4 (1 ⚠) | 0 | [[Ponatinib (drug)]] 5 µM 2.83× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 122 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.32× (z +12.0) | — |
| [[RKO (line)]] | wt | 126 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.82× (z +8.7) | [[Digitoxin (drug)]] 0.5 µM 0.297× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 209 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 384 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 110 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.30× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 167 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.456× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.1) |
| [[J82 (line)]] | alt | 246 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -13.7) |
| [[SW 900 (line)]] | alt | 395 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 266 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 280 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -18.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -10.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 95.8 | 1 | 1 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 3.75× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -8.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0713× (z -23.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 275 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.377× (z -11.6) |
| [[A549 (line)]] | wt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.3) |
| [[COLO 205 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +13.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.428× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 71.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -12.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 427 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -8.6) |
| [[SW48 (line)]] | wt | 298 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 202 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB3]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[WDFY2]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.58 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[OSBPL6]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CDYL2]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[BMP2K]] | +0.55 | +0.49 / +0.56 | both halves | 2e-05 |  |
| [[RAC2]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[KIF21B]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[LYPLA1]] | +0.52 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[NLRP3]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[KHDRBS3]] | +0.51 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[TMEM158]] | +0.51 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLLT6]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[AEBP2]] | -0.49 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[GTF2IRD2]] | -0.49 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[RBKS]] | -0.48 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[LINC02889]] | -0.47 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[RBM48]] | -0.47 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[CFH]] | -0.47 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[MAIP1]] | -0.47 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.47 | -0.45 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[C11orf58]] | -0.47 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[KDM3B]] | -0.46 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[BTN3A3]] | -0.46 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[GTF2IRD2B]] | -0.46 | -0.45 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLRP3]] | B | NLRP3 activity raises APBB2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without NLRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[CDYL2]] | B | CDYL2 activity raises APBB2's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without CDYL2 | 0.041 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers APBB2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers APBB2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[OSBPL6]] | B | OSBPL6 activity raises APBB2's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without OSBPL6 | 0.078 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[PKIA]] | B | PKIA activity raises APBB2's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without PKIA | 0.086 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[SEMA7A]] | B | SEMA7A activity raises APBB2's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without SEMA7A | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.9, 6.4); signed map (-1.8, 50.9). **Vector** length 121, 38.4% of its response variance represented; |z| ≥ 3 in 1,765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | +6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -16.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.2 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | +0.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -3.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14-p13 — chr4:40,810,027-41,216,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FE65L, FE65L1, MGC35575 |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92870](https://www.uniprot.org/uniprotkb/Q92870) (Amyloid beta precursor protein binding family B member 2):

> Plays a role in the maintenance of lens transparency, and may also play a role in muscle cell strength (By similarity). Involved in hippocampal neurite branching and neuromuscular junction formation, as a result plays a role in spatial memory functioning (By similarity). Activates transcription of APP.

**Summary**, from NCBI Gene [323](https://www.ncbi.nlm.nih.gov/gene/323):

> The protein encoded by this gene interacts with the cytoplasmic domains of amyloid beta (A4) precursor protein and amyloid beta (A4) precursor-like protein 2. This protein contains two phosphotyrosine binding (PTB) domains, which are thought to function in signal transduction. Polymorphisms in this gene have been associated with Alzheimer's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:582) · Entrez [323](https://www.ncbi.nlm.nih.gov/gene/323) · UniProt [Q92870](https://www.uniprot.org/uniprotkb/Q92870) · Ensembl [ENSG00000163697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163697)

## Data

Gene col 8757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8757); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8757]; `tensor/DDL_lfc|DDL_z.npy` [8757]; `embed/gene_vectors.npy` [8757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8757 or target_col == 8757). Every well: [[APBB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
