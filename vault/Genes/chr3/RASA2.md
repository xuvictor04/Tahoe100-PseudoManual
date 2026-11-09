---
symbol: "RASA2"
type: "gene"
col: 7929
ensembl_id: "ENSG00000155903"
name: "RAS p21 protein activator 2"
location: "3q23"
module: 193
arm: "+"
pooled_cpm: 290.76
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# RASA2

*RAS p21 protein activator 2* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.24× (z +5.9, q 2e-06, up in 29 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.374× (z -18.8, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.531× (z -17.1, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMURF2]] (+0.71, fdr 7e-06), [[BMP2K]] (+0.64, fdr 1e-05), [[SPTLC2]] (+0.64, fdr 2e-05); moves opposite to [[HNRNPH2]] (-0.66, fdr 1e-05), [[ZSCAN31]] (-0.61, fdr 1e-05), [[ACIN1]] (-0.59, fdr 3e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.9 | 2e-06 | 29/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +5.7 | 4e-06 | 36/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.002 | 24/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.9 | 0.014 | 25/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.8 | 0.014 | 23/48 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.15× | +3.8 | 0.014 | 13/49 (A549, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.024 | 22/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.043 | 23/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.4 | 0.050 | 23/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.15 | 19/49 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.374×** | -18.8 | 0e+00 | 46/49 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.371×** | -18.2 | 0e+00 | 40/44 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.531×** | -17.1 | 0e+00 | 39/48 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.442×** | -15.6 | 0e+00 | 45/48 (SNU-423, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.447×** | -14.2 | 7e-44 | 39/45 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -11.9 | 9e-31 | 39/48 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -11.2 | 5e-27 | 39/49 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -10.2 | 9e-23 | 39/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.604×** | -9.6 | 5e-20 | 42/48 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.620×** | -9.1 | 5e-18 | 40/48 (A549, RKO, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -6.2 | 2e-08 | 34/48 (A-172, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.726×** | -6.1 | 6e-08 | 33/48 (A549, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -5.9 | 2e-07 | 35/48 (A549, RKO, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.736×** | -5.8 | 2e-07 | 33/48 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.735×** | -5.6 | 8e-07 | 34/48 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.747×** | -5.3 | 4e-06 | 30/47 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.793×** | -5.2 | 5e-06 | 31/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.759×** | -5.2 | 8e-06 | 31/49 (RKO, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.754×** | -5.1 | 8e-06 | 29/48 (COLO 205, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.786×** | -5.0 | 1e-05 | 29/50 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.770×** | -4.9 | 2e-05 | 28/49 (HOP62, BT-474, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.806×** | -4.8 | 4e-05 | 29/48 (RKO, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 580 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -24.1) |
| [[NCI-H1573 (line)]] | alt | 407 | 4 (2 ⚠) | 11 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.07× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -24.7) |
| [[A549 (line)]] | wt | 554 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -28.4) |
| [[MIA PaCa-2 (line)]] | alt | 314 | 4 | 10 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.15× (z +12.9) | [[Adagrasib (drug)]] 0.05 µM 0.650× (z -18.0) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.4) |
| [[HOP62 (line)]] | alt | 381 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -25.5) |
| [[A-172 (line)]] | wt | 287 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.293× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 339 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -21.2) |
| [[SW480 (line)]] | alt | 235 | 1 (1 ⚠) | 10 (7 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.78× (z +8.9) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.394× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.591× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 506 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -15.0) |
| [[J82 (line)]] | alt | 303 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 257 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -18.4) |
| [[CFPAC-1 (line)]] | alt | 447 | 1 | 6 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.74× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 400 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.301× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 369 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 495 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.502× (z -13.1) |
| [[HS-578T (line)]] | alt | 536 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.0) |
| [[LS 180 (line)]] | wt | 246 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -12.7) |
| [[PANC-1 (line)]] | alt | 228 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -12.0) |
| [[SW1417 (line)]] | alt | 343 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.641× (z -9.6) |
| [[A-427 (line)]] | wt | 236 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.554× (z -11.8) |
| [[BT-474 (line)]] | alt | 290 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 230 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 274 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.294× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 268 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.277× (z -17.1) |
| [[SNU-423 (line)]] | alt | 240 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.208× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 218 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -13.0) |
| [[SW48 (line)]] | wt | 234 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.0) |
| [[H4 (line)]] | wt | 345 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -10.7) |
| [[HCT15 (line)]] | alt | 178 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 304 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -21.0) |
| [[Hs 766T (line)]] | wt | 218 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 411 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.311× (z -10.0) |
| [[KATO III (line)]] | alt | 183 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -12.2) |
| [[LoVo (line)]] | wt | 174 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -25.2) |
| [[A498 (line)]] | wt | 237 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.359× (z -12.0) |
| [[C32 (line)]] | wt | 126 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.76× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.380× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 188 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.73× (z +14.4) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 151 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.162× (z -19.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 158 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.324× (z -11.4) |
| [[AN3 CA (line)]] | alt | 192 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.329× (z -9.2) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.287× (z -13.7) |
| [[HT-29 (line)]] | alt | 143 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.396× (z -12.2) |
| [[SNU-1 (line)]] | wt | 212 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.452× (z -8.5) |
| [[SW 1271 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 226 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMURF2]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[BMP2K]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SPTLC2]] | +0.64 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[MAPK8]] | +0.61 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[FXYD5]] | +0.61 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 | same gene group |
| [[CSNK1E]] | +0.60 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ARPC1B]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LYPLA1]] | +0.59 | +0.73 / +0.43 | both halves | 3e-05 | pathway: MAPK family signaling cascades |
| [[FMNL2]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH2]] | -0.66 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[ZSCAN31]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ACIN1]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[RBM23]] | -0.59 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[USP16]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TRIM16L]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PEF1]] | -0.57 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[CHD3]] | -0.57 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[TET2]] | -0.57 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[UBQLN2]] | -0.56 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[ARFGAP2]] | -0.56 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[SMCR8]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RASA2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds |
| [[MYO1D]] | B | MYO1D activity raises RASA2's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.17× lower at baseline in the lines without MYO1D | 0.085 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[ELK3]] | C | ELK3's natural level strengthens RASA2's drug response | ELK3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.58; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, 5.7); signed map (-0.8, 51.0). **Vector** length 121, 49.6% of its response variance represented; |z| ≥ 3 in 1,827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.6 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +6.9 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.3 | -9.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.3 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.2 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.0 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | -0.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.7 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -17.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.7 | -5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.7 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.4 | -5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.2 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.0 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | RAS p21 protein activator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:141,487,027-141,615,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAP1M |
| Gene groups (HGNC) | Pleckstrin homology domain containing; C2 and RasGAP domain containing |
| Hallmark sets | UV_RESPONSE_DN, MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: Regulation of RAS by GAPs; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15283](https://www.uniprot.org/uniprotkb/Q15283) (Ras GTPase-activating protein 2):

> Inhibitory regulator of the Ras-cyclic AMP pathway. Binds inositol tetrakisphosphate (IP4).

**Summary**, from NCBI Gene [5922](https://www.ncbi.nlm.nih.gov/gene/5922):

> The protein encoded by this gene is member of the GAP1 family of GTPase-activating proteins. The gene product stimulates the GTPase activity of normal RAS p21 but not its oncogenic counterpart. Acting as a suppressor of RAS function, the protein enhances the weak intrinsic GTPase activity of RAS proteins resulting in the inactive GDP-bound form of RAS, thereby allowing control of cellular proliferation and differentiation. Alternative splicing results in multiple transcript variants. [provided …

**Accessions** — [HGNC:9872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9872) · Entrez [5922](https://www.ncbi.nlm.nih.gov/gene/5922) · UniProt [Q15283](https://www.uniprot.org/uniprotkb/Q15283) · Ensembl [ENSG00000155903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155903)

## Data

Gene col 7929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7929); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7929]; `tensor/DDL_lfc|DDL_z.npy` [7929]; `embed/gene_vectors.npy` [7929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7929 or target_col == 7929). Every well: [[RASA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
