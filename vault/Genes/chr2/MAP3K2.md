---
symbol: "MAP3K2"
type: "gene"
col: 9884
ensembl_id: "ENSG00000169967"
name: "mitogen-activated protein kinase kinase kinase 2"
location: "2q14.3"
module: 79
arm: "+"
pooled_cpm: 299.33
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# MAP3K2

*mitogen-activated protein kinase kinase kinase 2* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +9.2, q 3e-17, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.597× (z -11.8, q 3e-29, down in 41 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.781× (z -8.3, q 1e-14, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM3A]] (+0.67, fdr 7e-06), [[ZNF292]] (+0.67, fdr 7e-06), [[CNNM2]] (+0.65, fdr 7e-06); moves opposite to [[MAK16]] (-0.62, fdr 8e-06), [[EMG1]] (-0.60, fdr 1e-05), [[EBNA1BP2]] (-0.59, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +9.2 | 3e-17 | 37/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.8 | 5e-16 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.7 | 8e-16 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.8 | 8e-13 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +6.3 | 2e-08 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +6.0 | 2e-07 | 36/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.005 | 33/48 (CFPAC-1, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.8 | 0.011 | 18/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.6 | 0.016 | 4/48 (A498, SW48, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.016 | 16/48 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.047 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.067 | 10/48 (NCI-H1792, HepG2/C3A, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.2 | 0.071 | 7/48 (RPMI-7951, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.597×** | -11.8 | 3e-29 | 41/44 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.636×** | -10.8 | 1e-24 | 40/49 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -10.4 | 3e-23 | 44/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -8.3 | 1e-14 | 30/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.714×** | -8.0 | 1e-13 | 35/48 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.729×** | -7.5 | 6e-12 | 35/48 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.716×** | -7.3 | 2e-11 | 30/45 (C32, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.755×** | -6.7 | 2e-09 | 33/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.762×** | -6.5 | 7e-09 | 30/48 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.763×** | -6.4 | 8e-09 | 40/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -5.9 | 2e-07 | 31/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.782×** | -5.7 | 6e-07 | 30/48 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.790×** | -5.4 | 3e-06 | 29/50 (C32, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.857× | -5.2 | 8e-06 | 21/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.817×** | -4.6 | 1e-04 | 29/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.841× | -4.1 | 0.001 | 22/48 (HOP62, C32, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.871× | -3.3 | 0.033 | 15/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.042 | 16/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.872× | -3.2 | 0.042 | 14/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.053 | 11/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.880× | -3.0 | 0.061 | 7/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.882× | -3.0 | 0.066 | 10/48 (HOP62, HCT15, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.885× | -2.9 | 0.081 | 9/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.885× | -2.9 | 0.085 | 12/48 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 390 | 3 (1 ⚠) | 11 (11 ⚠) | [[Digitoxin (drug)]] 5 µM 2.01× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -22.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 334 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 358 | 7 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.57× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 262 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.06× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 254 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 325 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.523× (z -9.2) |
| [[HT-29 (line)]] | alt | 376 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.480× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 160 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +18.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.554× (z -8.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 371 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.368× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 278 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.520× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.588× (z -8.9) |
| [[SW48 (line)]] | wt | 312 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 236 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.380× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 294 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.479× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 410 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.599× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 299 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 241 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.94× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 239 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -12.6) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.511× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 390 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.64× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -11.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[PANC-1 (line)]] | alt | 283 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 189 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.30× (z +10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 315 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 278 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[LOX-IMVI (line)]] | wt | 339 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 263 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 294 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.587× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 255 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.557× (z -9.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 319 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.599× (z -11.1) |
| [[A549 (line)]] | wt | 312 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 282 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.520× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 161 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 307 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.12× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 317 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.457× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 268 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 309 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 365 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 404 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.489× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 375 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 305 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 324 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 327 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 364 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 502 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM3A]] | +0.67 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ZNF292]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[MXI1]] | +0.65 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.64 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | +0.62 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[PDK3]] | +0.61 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.61 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[RCOR3]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DPM3]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PXK]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK16]] | -0.62 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[EMG1]] | -0.60 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[WDR4]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[E2F3]] | -0.58 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[DHX37]] | -0.58 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PUS1]] | -0.57 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[REXO1]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.56 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[ELK3]] | -0.56 | -0.37 / -0.56 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity raises MAP3K2's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.23× lower at baseline in the lines without HOXA3 | 0.056 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises MAP3K2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXA5]] | B | HOXA5 activity raises MAP3K2's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.20× lower at baseline in the lines without HOXA5 | 0.083 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -21.2); signed map (-32.7, 23.8). **Vector** length 118, 43.2% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +7.6 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.2 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.2 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.1 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -1.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.3 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,298,668-127,388,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEKK2B; previously MEKK2 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2U5](https://www.uniprot.org/uniprotkb/Q9Y2U5) (Mitogen-activated protein kinase kinase kinase 2):

> Component of a protein kinase signal transduction cascade. Regulates the JNK and ERK5 pathways by phosphorylating and activating MAP2K5 and MAP2K7 (By similarity). Plays a role in caveolae kiss-and-run dynamics.

**Summary**, from NCBI Gene [10746](https://www.ncbi.nlm.nih.gov/gene/10746):

> The protein encoded by this gene is a member of serine/threonine protein kinase family. This kinase preferentially activates other kinases involved in the MAP kinase signaling pathway. This kinase has been shown to directly phosphorylate and activate Ikappa B kinases, and thus plays a role in NF-kappa B signaling pathway. This kinase has also been found to bind and activate protein kinase C-related kinase 2, which suggests its involvement in a regulated signaling process. [provided by RefSeq, …

**Accessions** — [HGNC:6854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6854) · Entrez [10746](https://www.ncbi.nlm.nih.gov/gene/10746) · UniProt [Q9Y2U5](https://www.uniprot.org/uniprotkb/Q9Y2U5) · Ensembl [ENSG00000169967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169967)

## Data

Gene col 9884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9884); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9884]; `tensor/DDL_lfc|DDL_z.npy` [9884]; `embed/gene_vectors.npy` [9884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9884 or target_col == 9884). Every well: [[MAP3K2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
