---
symbol: "HIVEP3"
type: "gene"
col: 4789
ensembl_id: "ENSG00000127124"
name: "HIVEP zinc finger 3"
location: "1p34.2"
module: 162
arm: "+"
pooled_cpm: 208.14
n_lines_expressing: 43
n_dd_up: 13
n_dd_down: 56
n_dd_up_clean: 12
n_dd_down_clean: 43
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# HIVEP3

*HIVEP zinc finger 3* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.78× (z +23.2, q 0e+00, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.519× (z -14.9, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR3]] (+0.72, fdr 7e-06), [[CD82]] (+0.71, fdr 7e-06), [[EGR2]] (+0.68, fdr 7e-06); moves opposite to [[LURAP1L]] (-0.59, fdr 3e-05), [[DHRS4]] (-0.55, fdr 2e-04), [[CSDE1]] (-0.53, fdr 3e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NAV2]] → it (grade B ⚠); 3 go from it, the strongest it → [[MYEOV]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +23.2 | 0e+00 | 32/41 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +14.0 | 2e-42 | 35/41 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +13.5 | 2e-39 | 36/41 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +12.9 | 1e-35 | 31/41 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +11.5 | 1e-28 | 34/41 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +11.2 | 6e-27 | 33/41 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +8.6 | 8e-16 | 34/41 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.4 | 7e-12 | 25/41 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +6.2 | 4e-08 | 31/42 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 3e-07 | 25/42 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.008 | 14/42 (SW1417, NCI-H23, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +3.7 | 0.010 | 17/41 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.031 | 19/41 (SK-MEL-2, PANC-1, …) | all doses, flat | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.077 | 13/41 (NCI-H2347, NCI-H23, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 69 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.519×** | -14.9 | 0e+00 | 37/41 (J82, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -10.3 | 1e-22 | 34/41 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.519×** | -10.1 | 9e-22 | 34/40 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.534×** | -10.1 | 1e-21 | 35/41 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -9.2 | 6e-18 | 30/38 (C32, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.644×** | -7.1 | 2e-10 | 33/42 (C32, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.739×** | -6.8 | 6e-10 | 28/42 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -6.6 | 2e-09 | 25/37 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.664×** | -6.6 | 3e-09 | 32/41 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -6.2 | 4e-08 | 31/40 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -6.0 | 8e-08 | 30/41 (C32, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -6.0 | 8e-08 | 27/41 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.692×** | -5.9 | 2e-07 | 30/40 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -5.8 | 2e-07 | 28/41 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.8 | 3e-07 | 30/43 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.687×** | -5.7 | 5e-07 | 32/41 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -5.7 | 5e-07 | 26/41 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.727×** | -5.4 | 2e-06 | 23/43 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -5.3 | 3e-06 | 26/42 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.719×** | -5.3 | 3e-06 | 26/41 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -5.3 | 4e-06 | 23/42 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -5.3 | 4e-06 | 27/41 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,912 | 0 | 43 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0703× (z -35.1) |
| [[A-172 (line)]] | wt | 466 | 0 | 20 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.246× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 570 | 0 | 20 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.511× (z -21.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -17.0) |
| [[LS 180 (line)]] | wt | 105 | 6 | 11 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.58× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.172× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -16.1) |
| [[LoVo (line)]] | wt | 125 | 0 | 15 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 12 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -11.4) |
| [[A549 (line)]] | wt | 62.9 | 10 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +35.9) | [[Selinexor (drug)]] 5 µM 0.467× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 106 | 8 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +30.6) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 112 | 10 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +39.8) | [[Selinexor (drug)]] 5 µM 0.555× (z -10.0) |
| [[PANC-1 (line)]] | alt | 359 | 3 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +20.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -14.6) |
| [[SW480 (line)]] | alt | 134 | 7 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.30× (z +13.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -11.8) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.549× (z -9.9) |
| [[HS-578T (line)]] | alt | 199 | 7 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +24.0) | [[Selinexor (drug)]] 5 µM 0.519× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 65.7 | 8 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +33.2) | [[Ixazomib citrate (drug)]] 5 µM 0.423× (z -9.3) |
| [[J82 (line)]] | alt | 234 | 4 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +22.7) | [[Selinexor (drug)]] 5 µM 0.299× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 314 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +18.6) | [[Selinexor (drug)]] 5 µM 0.350× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 71.9 | 6 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.94× (z +14.1) | [[Selinexor (drug)]] 5 µM 0.461× (z -11.2) |
| [[HOP62 (line)]] | alt | 233 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +25.7) | [[Selinexor (drug)]] 5 µM 0.437× (z -9.3) |
| [[Hs 766T (line)]] | wt | 541 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.372× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 85.7 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +19.9) | [[Selinexor (drug)]] 5 µM 0.494× (z -9.9) |
| [[BT-474 (line)]] | alt | 131 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 152 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +15.7) | [[Selinexor (drug)]] 5 µM 0.289× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 63.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +32.3) | — |
| [[RPMI-7951 (line)]] | alt | 361 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.4) | [[Ixazomib citrate (drug)]] 5 µM 0.286× (z -10.3) |
| [[SHP-77 (line)]] | alt | 86.8 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.05× (z +13.3) | — |
| [[A-427 (line)]] | wt | 92.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -12.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 115 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.486× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 356 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.99× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 173 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.239× (z -16.2) |
| [[SW 900 (line)]] | alt | 169 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +25.5) | [[Selinexor (drug)]] 5 µM 0.530× (z -8.8) |
| [[SW48 (line)]] | wt | 153 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +19.8) | — |
| [[C-33 A (line)]] | alt | 99.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.30× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 285 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -9.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -9.0) |
| [[H4 (line)]] | wt | 151 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +15.4) | [[Selinexor (drug)]] 5 µM 0.449× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 121 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +24.6) | — |
| [[SW1417 (line)]] | alt | 262 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 282 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +24.8) | [[Selinexor (drug)]] 5 µM 0.425× (z -10.7) |
| [[SW 1088 (line)]] | alt | 363 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[5-Azacytidine (drug)]] 0.5 µM 0.170× (z -9.3) |
| [[AN3 CA (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 35.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 42.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 46.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 49.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR3]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 | same gene group |
| [[CD82]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[EGR2]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 | same gene group |
| [[VDR]] | +0.66 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[EGR1]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[IER2]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[MAP3K14]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SOX13]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ADAM19]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A7]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ECE1]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SH2B3]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LURAP1L]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[DHRS4]] | -0.55 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[CSDE1]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[FAIM]] | -0.51 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[ZNF514]] | -0.51 | -0.35 / -0.43 | both halves | 1e-04 | same gene group |
| [[SETD7]] | -0.51 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.50 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[NAXD]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CLCC1]] | -0.50 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[GARS1-DT]] | -0.50 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[C8orf44-SGK3]] | -0.50 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV2]] | B | NAV2 activity raises HIVEP3's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without NAV2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[MAP2K1]] | B | MAP2K1 activity raises HIVEP3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.4% of all compounds | 0.062 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASA3]] | B | RASA3 activity raises HIVEP3's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.46× lower at baseline in the lines without RASA3 | 0.078 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HIVEP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers HIVEP3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TINAGL1]] | B | TINAGL1 activity raises HIVEP3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.23× lower at baseline in the lines without TINAGL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[CD82]] | C | CD82 activity raises HIVEP3's level | lines that do not express CD82 (11) vs lines expressing it (39) | 3.12× lower at baseline in the lines without CD82 | 0.053 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYEOV]] | B | HIVEP3 activity raises MYEOV's level | lines that do not express HIVEP3 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without HIVEP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CD82; maybe low, not absent |
| [[ARL4C]] | B | HIVEP3 activity raises ARL4C's level | lines that do not express HIVEP3 (7) vs lines expressing it (43) | 5.97× lower at baseline in the lines without HIVEP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: CD82; maybe low, not absent |
| [[CD82]] | C | HIVEP3 activity raises CD82's level | lines that do not express HIVEP3 (7) vs lines expressing it (43) | 3.45× lower at baseline in the lines without HIVEP3 | 0.085 | ⚠ within organs, on part of the lines; also absent: CD82; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -1.2); signed map (0.7, 43.1). **Vector** length 147, 51.5% of its response variance represented; |z| ≥ 3 in 1,994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +23.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.7 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.3 | +11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.3 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -14.6 | -14.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.3 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -8.0 | -6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.7 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.9 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.9 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.6 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | HIVEP zinc finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:41,506,365-42,035,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KRC, KBP1, KBP-1, SHN3, FLJ16752, KIAA1555, ZAS3, Schnurri-3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 2 pathways, smallest: Regulation of RUNX2 expression and activity; Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1R4](https://www.uniprot.org/uniprotkb/Q5T1R4) (Transcription factor HIVEP3):

> Plays a role of transcription factor; binds to recognition signal sequences (Rss heptamer) for somatic recombination of immunoglobulin and T-cell receptor gene segments; Also binds to the kappa-B motif of gene such as S100A4, involved in cell progression and differentiation. Kappa-B motif is a gene regulatory element found in promoters and enhancers of genes involved in immunity, inflammation, and growth and that responds to viral antigens, mitogens, and cytokines. Involvement of HIVEP3 in cell …

**Summary**, from NCBI Gene [59269](https://www.ncbi.nlm.nih.gov/gene/59269):

> This gene encodes a member of the human immunodeficiency virus type 1 enhancer-binding protein family. Members of this protein family contain multiple zinc finger and acid-rich (ZAS) domains and serine-threonine rich regions. This protein acts as a transcription factor and is able to regulate nuclear factor kappaB-mediated transcription by binding the kappaB motif in target genes. This protein also binds the recombination signal sequence that flanks the V, D, and J regions of immunoglobulin and …

**Accessions** — [HGNC:13561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13561) · Entrez [59269](https://www.ncbi.nlm.nih.gov/gene/59269) · UniProt [Q5T1R4](https://www.uniprot.org/uniprotkb/Q5T1R4) · Ensembl [ENSG00000127124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127124)

## Data

Gene col 4789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4789); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4789]; `tensor/DDL_lfc|DDL_z.npy` [4789]; `embed/gene_vectors.npy` [4789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4789 or target_col == 4789). Every well: [[HIVEP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIVEP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
