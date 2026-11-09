---
symbol: "CDC42SE2"
type: "gene"
col: 8207
ensembl_id: "ENSG00000158985"
name: "CDC42 small effector 2"
location: "5q31.1"
module: 163
arm: "+"
pooled_cpm: 163.64
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# CDC42SE2

*CDC42 small effector 2* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.15× (z +5.4, q 5e-05, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.587× (z -14.2, q 9e-43, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.622× (z -12.6, q 2e-34, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RANBP9]] (+0.67, fdr 7e-06), [[SLC9A6]] (+0.62, fdr 1e-05), [[TANC1]] (+0.62, fdr 1e-05); moves opposite to [[NEPRO-AS1]] (-0.62, fdr 1e-05), [[KDM6B]] (-0.60, fdr 1e-05), [[MSANTD3-TMEFF1]] (-0.60, fdr 3e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.4 | 5e-05 | 16/48 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +5.2 | 5e-05 | 22/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +4.9 | 1e-04 | 20/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +4.5 | 0.001 | 22/48 (LoVo, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.005 | 21/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.8 | 0.015 | 14/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.021 | 19/48 (A498, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.4 | 0.043 | 18/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.061 | 17/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.099 | 11/49 (A498, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.12× | +3.0 | 0.12 | 11/49 (A498, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.587×** | -14.2 | 9e-43 | 42/49 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.692×** | -13.8 | 6e-41 | 35/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -13.2 | 2e-37 | 39/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.622×** | -12.6 | 2e-34 | 43/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.655×** | -11.2 | 3e-27 | 43/48 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.647×** | -10.7 | 9e-25 | 32/45 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -6.4 | 1e-08 | 27/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.804×** | -5.8 | 5e-07 | 28/48 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.818×** | -5.3 | 7e-06 | 22/48 (NCI-H1573, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.821×** | -5.0 | 3e-05 | 23/48 (A-172, NCI-H1573, …) | rises with dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.780×** | -4.6 | 2e-04 | 25/48 (Hs 766T, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.787×** | -4.5 | 4e-04 | 24/47 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.887× | -4.5 | 4e-04 | 14/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.854× | -4.2 | 0.001 | 21/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.008 | 20/48 (SW 900, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.867× | -3.6 | 0.011 | 14/48 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.068 | 9/48 (HOP62, Panc 03.27, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.891× | -3.0 | 0.073 | 7/47 (CFPAC-1, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 303 | 1 (1 ⚠) | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.227× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.554× (z -9.3) |
| [[LoVo (line)]] | wt | 346 | 1 (1 ⚠) | 7 (5 ⚠) | [[Digitoxin (drug)]] 5 µM 1.78× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.199× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.625× (z -9.8) |
| [[KATO III (line)]] | alt | 176 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 126 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -17.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -17.0) |
| [[SW480 (line)]] | alt | 158 | 2 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.78× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.319× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.509× (z -14.5) |
| [[A549 (line)]] | wt | 201 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -9.4) |
| [[HCT15 (line)]] | alt | 242 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 195 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.574× (z -9.2) |
| [[PANC-1 (line)]] | alt | 215 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.497× (z -10.8) |
| [[SNU-423 (line)]] | alt | 143 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.423× (z -11.7) |
| [[A-172 (line)]] | wt | 106 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.467× (z -11.1) |
| [[A-427 (line)]] | wt | 242 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.571× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 254 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.479× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 282 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -11.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 287 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -12.9) |
| [[Hs 766T (line)]] | wt | 180 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.524× (z -8.6) |
| [[HS-578T (line)]] | alt | 121 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -10.3) |
| [[HT-29 (line)]] | alt | 185 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.509× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 172 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -15.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -15.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -27.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.470× (z -10.2) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.645× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.559× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.517× (z -8.8) |
| [[SW1417 (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -12.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 163 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -12.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.543× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.477× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.525× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.568× (z -9.8) |
| [[SW48 (line)]] | wt | 117 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.28× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -8.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 131 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.55× (z +9.5) | — |
| [[C32 (line)]] | wt | 74.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.438× (z -8.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[HepG2_C3A (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.395× (z -10.7) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 136 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.471× (z -11.5) |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0787× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 113 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.484× (z -8.8) |
| [[AN3 CA (line)]] | alt | 163 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 117 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP9]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.62 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[TANC1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ABHD12]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[STK38]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.61 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[RNF38]] | +0.60 | +0.73 / +0.40 | both halves | 4e-05 |  |
| [[LMTK2]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PPP2R5E]] | +0.59 | +0.71 / +0.43 | both halves | 4e-05 |  |
| [[LPCAT3]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CDS1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.62 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.60 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[MSANTD3-TMEFF1]] | -0.60 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[CYB5D1]] | -0.59 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[CAVIN4]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[EGFR]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ETS1]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SCAF1]] | -0.56 | -0.68 / -0.32 | both halves | 1e-04 |  |
| [[MYSM1]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.56 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ZNF554]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[THOC6]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDS1]] | B | CDS1 activity raises CDC42SE2's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without CDS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[RHPN2]] | C | RHPN2 activity raises CDC42SE2's level | lines that do not express RHPN2 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without RHPN2 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RASSF7, LY6E-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.9, -5.5); signed map (-19.4, 18.8). **Vector** length 116, 33.9% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -10.0 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.9 | -12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.8 | -11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -13.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 small effector 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:131,245,493-131,398,447 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21967, SPEC2 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRR3](https://www.uniprot.org/uniprotkb/Q9NRR3) (CDC42 small effector protein 2):

> Probably involved in the organization of the actin cytoskeleton by acting downstream of CDC42, inducing actin filament assembly. Alters CDC42-induced cell shape changes. In activated T-cells, may play a role in CDC42-mediated F-actin accumulation at the immunological synapse. May play a role in early contractile events in phagocytosis in macrophages.

**Summary**, from NCBI Gene [56990](https://www.ncbi.nlm.nih.gov/gene/56990):

> Enables signaling adaptor activity. Involved in regulation of signal transduction. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18547) · Entrez [56990](https://www.ncbi.nlm.nih.gov/gene/56990) · UniProt [Q9NRR3](https://www.uniprot.org/uniprotkb/Q9NRR3) · Ensembl [ENSG00000158985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158985)

## Data

Gene col 8207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8207); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8207]; `tensor/DDL_lfc|DDL_z.npy` [8207]; `embed/gene_vectors.npy` [8207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8207 or target_col == 8207). Every well: [[CDC42SE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42SE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
