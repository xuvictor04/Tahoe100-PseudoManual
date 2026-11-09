---
symbol: "TRIM16"
type: "gene"
col: 13319
ensembl_id: "ENSG00000221926"
name: "tripartite motif containing 16"
location: "17p12"
module: 117
arm: "+"
pooled_cpm: 46.73
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TRIM16

*tripartite motif containing 16* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.57× (z +8.2, q 1e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.337× (z -19.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM16L-1]] (+0.80, fdr 7e-06), [[TRIM16L]] (+0.72, fdr 7e-06), [[ME1]] (+0.64, fdr 7e-06); moves opposite to [[RCN2]] (-0.56, fdr 1e-05), [[NARF]] (-0.56, fdr 1e-05), [[FCHO2]] (-0.55, fdr 1e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CYP4F11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +8.2 | 1e-13 | 31/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.8 | 2e-06 | 28/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.73×** | +5.2 | 5e-05 | 25/47 (LoVo, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +4.8 | 3e-04 | 19/47 (NCI-H1573, A-172, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +4.7 | 3e-04 | 20/47 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 4e-04 | 23/47 (A549, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.011 | 16/48 (A549, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.011 | 21/48 (A-172, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.011 | 17/49 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.031 | 16/47 (LoVo, J82, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.20×** | +3.4 | 0.039 | 16/48 (A-172, Hs 766T, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.042 | 18/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.051 | 13/47 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.053 | 17/48 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.064 | 18/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.069 | 16/48 (NCI-H1573, J82, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.072 | 4/48 (SW1417, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.337×** | -19.7 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -18.3 | 0e+00 | 43/48 (HT-29, SW48, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -16.9 | 0e+00 | 46/47 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -14.6 | 1e-45 | 40/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.527×** | -11.6 | 3e-29 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -11.4 | 5e-28 | 41/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -9.7 | 3e-20 | 37/49 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -8.1 | 5e-14 | 34/45 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.682×** | -6.9 | 2e-10 | 25/48 (COLO 205, LS 180, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.703×** | -6.4 | 9e-09 | 27/48 (HT-29, KATO III, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.696×** | -6.3 | 1e-08 | 21/39 (KATO III, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.720×** | -6.0 | 1e-07 | 25/47 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.806×** | -5.5 | 1e-06 | 25/47 (PANC-1, SW480, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.786×** | -4.4 | 5e-04 | 21/48 (HT-29, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.781×** | -3.7 | 0.009 | 17/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.040 | 13/48 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.726×** | -3.0 | 0.071 | 15/47 (SW48, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.729×** | -3.0 | 0.074 | 11/47 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 102 | 0 | 9 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -13.1) |
| [[HT-29 (line)]] | alt | 64.3 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -20.9) |
| [[PANC-1 (line)]] | alt | 39.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0840× (z -28.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -21.0) |
| [[HEC-1-A (line)]] | alt | 60.5 | 2 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.19× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 49.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -10.8) |
| [[A-427 (line)]] | wt | 33.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -10.6) |
| [[A549 (line)]] | wt | 67.1 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.16× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -13.2) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -11.9) |
| [[SW1417 (line)]] | alt | 59.1 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -16.7) |
| [[COLO 205 (line)]] | alt | 73.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -9.4) |
| [[H4 (line)]] | wt | 48.8 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.54× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.173× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.198× (z -10.0) |
| [[LoVo (line)]] | wt | 53.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 53.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.7) |
| [[SHP-77 (line)]] | alt | 113 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.0) |
| [[SW48 (line)]] | wt | 114 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -20.7) |
| [[SW480 (line)]] | alt | 39.3 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -18.8) |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.228× (z -10.3) |
| [[HS-578T (line)]] | alt | 38.1 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -9.5) |
| [[KATO III (line)]] | alt | 100 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0878× (z -16.4) |
| [[A-172 (line)]] | wt | 36.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.85× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.323× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 90.9 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -15.6) |
| [[HOP62 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -11.0) |
| [[RKO (line)]] | wt | 26.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0388× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 57.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.6) |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[C32 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -13.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 66.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.139× (z -8.6) |
| [[J82 (line)]] | alt | 34.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 20.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 53.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -8.5) |
| [[SNU-1 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0629× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -8.9) |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0673× (z -9.8) |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16L-1]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[TRIM16L]] | +0.72 | +0.71 / +0.76 | both halves | 7e-06 | STRING 740 |
| [[ME1]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ANKEF1]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FBXW10B]] | +0.61 | +0.59 / +0.67 | both halves | 7e-06 | ⚠ same locus (8.3 kb, same strand: neighbours can correlate without regulation) |
| [[WDR18]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GCLM]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[IFRD2]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CYP4F11]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DNTTIP2]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[XKR6]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NARF]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[FCHO2]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TMEM50A]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MAP3K3]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ATP6AP2]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[YPEL1]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[IKBIP]] | -0.53 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[TGFBR1]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FBXL20]] | -0.51 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZNF710-AS1]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP4F11]] | B | CYP4F11 activity raises TRIM16's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without CYP4F11 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[PIR]] | B | PIR activity raises TRIM16's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PIR | 0.042 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[FBXW10B]] | B | FBXW10B activity raises TRIM16's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without FBXW10B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises TRIM16's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.31× lower at baseline in the lines without ALOX12P2-1 | 0.047 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[TRIM16L]] | B | TRIM16L activity raises TRIM16's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without TRIM16L | 0.070 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[ME1]] | B | ME1 activity raises TRIM16's level | lines that do not express ME1 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without ME1 | 0.098 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.9, 49.0); signed map (50.2, -10.1). **Vector** length 117, 32.6% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.50 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.50 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.2 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.9 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -18.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -14.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.3 | -19.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -16.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.0 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.8 | -0.6 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | -1.7 | -0.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,627,960-15,684,311 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EBBP |
| Gene groups (HGNC) | Tripartite motif family |
| Matched by | ensembl_id |

**Function**, from UniProt [O95361](https://www.uniprot.org/uniprotkb/O95361) (E3 ubiquitin-protein ligase TRIM16):

> E3 ubiquitin-protein ligase that plays an essential role in the organization of autophagic response and ubiquitination upon lysosomal and phagosomal damages. Plays a role in the stress-induced biogenesis and degradation of protein aggresomes by regulating the p62-KEAP1-NRF2 signaling and particularly by modulating the ubiquitination levels and thus stability of NRF2. Acts as a scaffold protein and facilitates autophagic degradation of protein aggregates by interacting with p62/SQSTM, ATG16L1 …

**Summary**, from NCBI Gene [10626](https://www.ncbi.nlm.nih.gov/gene/10626):

> The protein encoded by this gene is a tripartite motif (TRIM) family member that contains two B box domains and a coiled-coiled region that are characteristic of the B box zinc finger protein family. While it lacks a RING domain found in other TRIM proteins, the encoded protein can homodimerize or heterodimerize with other TRIM proteins and has E3 ubiquitin ligase activity. This gene is also a tumor suppressor and is involved in secretory autophagy. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:17241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17241) · Entrez [10626](https://www.ncbi.nlm.nih.gov/gene/10626) · UniProt [O95361](https://www.uniprot.org/uniprotkb/O95361) · Ensembl [ENSG00000221926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221926)

## Data

Gene col 13319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13319); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13319]; `tensor/DDL_lfc|DDL_z.npy` [13319]; `embed/gene_vectors.npy` [13319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13319 or target_col == 13319). Every well: [[TRIM16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
