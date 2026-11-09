---
symbol: "EXOC4"
type: "gene"
col: 5223
ensembl_id: "ENSG00000131558"
name: "exocyst complex component 4"
location: "7q33"
module: 200
arm: "+"
pooled_cpm: 381.39
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 39
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# EXOC4

*exocyst complex component 4* — 7q33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (22 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.259× (z -19.1, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.372× (z -13.9, q 4e-42, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMMP2L]] (+0.72, fdr 7e-06), [[SUMF1]] (+0.72, fdr 7e-06), [[FARS2]] (+0.71, fdr 7e-06); moves opposite to [[FOXO6]] (-0.58, fdr 2e-05), [[ATP2A3]] (-0.56, fdr 2e-05), [[RGS9]] (-0.55, fdr 1e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADGRB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.30× | +3.6 | 0.10 | 37/47 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.62× | +3.6 | 0.10 | 37/50 (NCI-H2347, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.4 | 0.11 | 19/48 (NCI-H2347, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.259×** | -19.1 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.289×** | -17.5 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.303×** | -16.2 | 0e+00 | 47/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.473×** | -14.9 | 0e+00 | 46/48 (C32, A498, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.372×** | -13.9 | 4e-42 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.383×** | -13.0 | 1e-36 | 48/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.411×** | -12.6 | 3e-34 | 47/48 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.520×** | -8.9 | 6e-17 | 39/44 (HCT15, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -8.6 | 4e-16 | 47/49 (C32, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.561×** | -8.1 | 2e-14 | 45/48 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.569×** | -7.3 | 1e-11 | 41/45 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.611×** | -6.9 | 2e-10 | 38/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -6.9 | 3e-10 | 41/48 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.624×** | -6.6 | 1e-09 | 41/48 (HCT15, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.626×** | -6.6 | 2e-09 | 43/48 (SNU-423, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.488×** | -6.6 | 2e-09 | 47/48 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -5.6 | 8e-07 | 39/48 (SNU-423, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -5.1 | 8e-06 | 34/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -4.6 | 8e-05 | 42/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Vilanterol (drug)]] 5 µM |  | **0.803×** | -4.4 | 3e-04 | 32/49 (HOP62, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.734×** | -4.0 | 0.001 | 39/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -3.9 | 0.002 | 28/48 (HCT15, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.005 | 25/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.007 | 34/49 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.730×** | -3.1 | 0.027 | 29/48 (C-33 A, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.731×** | -3.1 | 0.027 | 31/48 (LoVo, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 623 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -22.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -11.6) |
| [[KATO III (line)]] | alt | 514 | 0 | 16 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -27.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.349× (z -14.0) |
| [[C32 (line)]] | wt | 920 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -34.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.181× (z -10.5) |
| [[SW480 (line)]] | alt | 496 | 0 | 15 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -27.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -22.9) |
| [[NCI-H460 (line)]] | wt | 363 | 0 | 14 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -20.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.222× (z -18.5) |
| [[HCT15 (line)]] | alt | 456 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.332× (z -12.3) |
| [[SNU-423 (line)]] | alt | 355 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -23.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.413× (z -11.1) |
| [[A-427 (line)]] | wt | 414 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -15.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.196× (z -11.3) |
| [[LoVo (line)]] | wt | 475 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -21.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.375× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 447 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -20.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.478× (z -9.0) |
| [[PANC-1 (line)]] | alt | 367 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -22.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.228× (z -17.7) |
| [[SW1417 (line)]] | alt | 424 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -22.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.369× (z -10.6) |
| [[COLO 205 (line)]] | alt | 399 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.319× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 307 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.309× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 826 | 0 | 10 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.180× (z -20.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.383× (z -11.7) |
| [[HT-29 (line)]] | alt | 490 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.359× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 473 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.242× (z -16.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.232× (z -9.1) |
| [[HOP62 (line)]] | alt | 268 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.341× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 280 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -14.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 282 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.264× (z -12.7) |
| [[LS 180 (line)]] | wt | 313 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -20.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.269× (z -15.3) |
| [[RKO (line)]] | wt | 533 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.350× (z -11.2) |
| [[SW 900 (line)]] | alt | 292 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -19.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.350× (z -10.7) |
| [[A549 (line)]] | wt | 303 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 377 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.276× (z -14.8) |
| [[C-33 A (line)]] | alt | 320 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.298× (z -12.7) |
| [[H4 (line)]] | wt | 317 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 371 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -18.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 228 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.230× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 245 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.530× (z -8.6) |
| [[SNU-1 (line)]] | wt | 335 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -18.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -17.6) |
| [[SW48 (line)]] | wt | 476 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.191× (z -13.6) |
| [[AN3 CA (line)]] | alt | 565 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.157× (z -15.5) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 208 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.383× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 282 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -20.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 292 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -13.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.343× (z -11.1) |
| [[SHP-77 (line)]] | alt | 303 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.381× (z -12.4) |
| [[A498 (line)]] | wt | 433 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -23.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[CHP-212 (line)]] | wt | 356 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -13.2) |
| [[Hs 766T (line)]] | wt | 367 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -12.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 370 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.257× (z -13.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 282 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -11.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 290 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -13.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -10.4) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 493 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 317 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMMP2L]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[SUMF1]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[FARS2]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[VPS13B]] | +0.71 | +0.49 / +0.81 | both halves | 1e-05 |  |
| [[TBC1D5]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | STRING 538 |
| [[TBCK]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 | STRING 435 |
| [[FTX]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[AFG1L]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FHIT]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[ENOX2]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ARID1B]] | +0.59 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[ZRANB2-DT]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO6]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ATP2A3]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[RGS9]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[EML2]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 | same gene group |
| [[ANO8]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CDC42BPG]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GDPD5]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CAMSAP3]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 | same gene group |
| [[CCDC88B]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SLC17A7]] | -0.51 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ADGRB2]] | -0.51 | -0.31 / -0.57 | both halves | 2e-04 | same gene group |
| [[KLHL26]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB2]] | B | ADGRB2 activity raises EXOC4's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without ADGRB2 | 0.044 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.0, 29.8); signed map (10.2, -12.9). **Vector** length 99.8, 52.5% of its response variance represented; |z| ≥ 3 in 1,591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.8 | -16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.5 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.6 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.6 | -6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -6.5 | -8.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.4 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.1 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:133,253,073-134,066,589 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1699, MGC27170, SEC8, Sec8p; previously SEC8L1 |
| Gene groups (HGNC) | Exocyst complex; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A65](https://www.uniprot.org/uniprotkb/Q96A65) (Exocyst complex component 4):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane. Couples NMDA receptor (NMDAR) cargo to the exocyst by binding the scaffold protein DLG3, delivering NMDARs to the synaptic plasma membrane.

**Summary**, from NCBI Gene [60412](https://www.ncbi.nlm.nih.gov/gene/60412):

> The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex, including this protein, are found to interact with the actin cytoskeletal remodeling and vesicle …

**Accessions** — [HGNC:30389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30389) · Entrez [60412](https://www.ncbi.nlm.nih.gov/gene/60412) · UniProt [Q96A65](https://www.uniprot.org/uniprotkb/Q96A65) · Ensembl [ENSG00000131558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131558)

## Data

Gene col 5223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5223); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5223]; `tensor/DDL_lfc|DDL_z.npy` [5223]; `embed/gene_vectors.npy` [5223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5223 or target_col == 5223). Every well: [[EXOC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
