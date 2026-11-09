---
symbol: "TANC2"
type: "gene"
col: 10028
ensembl_id: "ENSG00000170921"
name: "tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 2"
location: "17q23.2-q23.3"
module: 113
arm: "+"
pooled_cpm: 358.42
n_lines_expressing: 43
n_dd_up: 24
n_dd_down: 29
n_dd_up_clean: 23
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# TANC2

*tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 2* — 17q23.2-q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +8.3, q 9e-14, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -30.2, q 0e+00, down in 38 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.75, fdr 7e-06), [[ANGPTL4]] (+0.69, fdr 7e-06), [[AGTPBP1]] (+0.66, fdr 7e-06); moves opposite to [[SLC37A1]] (-0.55, fdr 3e-05), [[LINC01134]] (-0.51, fdr 5e-04), [[LYPLAL1-AS1]] (-0.48, fdr 2e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +8.3 | 9e-14 | 31/41 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.41×** | +6.0 | 4e-07 | 28/41 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.0 | 4e-07 | 32/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 4e-07 | 27/41 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 4e-07 | 23/41 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.40×** | +5.9 | 5e-07 | 26/41 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 5e-07 | 26/41 (hTERT-HPNE, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.39×** | +5.6 | 1e-06 | 28/41 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.37×** | +5.4 | 4e-06 | 23/41 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.4 | 4e-06 | 25/41 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 8e-06 | 24/40 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.34×** | +5.0 | 2e-05 | 25/41 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 6e-05 | 26/41 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 2e-04 | 24/41 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 2e-04 | 23/43 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.294×** | -30.2 | 0e+00 | 38/41 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.335×** | -26.9 | 0e+00 | 37/42 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.315×** | -20.1 | 0e+00 | 41/42 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.306×** | -19.9 | 0e+00 | 36/37 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.329×** | -19.4 | 0e+00 | 35/41 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.400×** | -15.4 | 0e+00 | 38/41 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.410×** | -14.4 | 4e-45 | 35/38 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.433×** | -14.0 | 7e-43 | 40/40 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.510×** | -11.3 | 8e-28 | 35/41 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.514×** | -11.2 | 4e-27 | 32/43 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.553×** | -9.9 | 1e-21 | 35/40 (HCT15, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.600×** | -8.9 | 2e-17 | 38/41 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.604×** | -8.8 | 6e-17 | 35/41 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.606×** | -8.8 | 9e-17 | 36/41 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.609×** | -8.7 | 2e-16 | 40/41 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.653×** | -7.4 | 4e-12 | 32/41 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -5.1 | 8e-06 | 27/41 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.7 | 6e-05 | 24/41 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.1 | 0.001 | 23/41 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.775×** | -3.9 | 0.002 | 23/41 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.9 | 0.002 | 25/41 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.791×** | -3.8 | 0.003 | 27/40 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.018 | 20/41 (C32, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 717 | 21 | 15 (8 ⚠) | [[Dexamethasone (drug)]] 0.05 µM 2.59× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -39.7) |
| [[LOX-IMVI (line)]] | wt | 548 | 17 | 17 (10 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 3.08× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -21.3) |
| [[C32 (line)]] | wt | 1,032 | 0 | 26 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -41.9) |
| [[hTERT-HPNE (line)]] | wt | 361 | 18 | 7 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 4.15× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -17.0) |
| [[HOP62 (line)]] | alt | 543 | 9 | 12 (5 ⚠) | [[Budesonide (drug)]] 5 µM 2.57× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -25.9) |
| [[SW 900 (line)]] | alt | 371 | 11 | 10 (4 ⚠) | [[Budesonide (drug)]] 5 µM 2.66× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 220 | 13 (1 ⚠) | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.68× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.394× (z -12.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 1,103 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -37.2) |
| [[J82 (line)]] | alt | 343 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -27.5) |
| [[MIA PaCa-2 (line)]] | alt | 401 | 0 | 14 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -20.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -19.4) |
| [[NCI-H1573 (line)]] | alt | 542 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -31.9) |
| [[Panc 03.27 (line)]] | alt | 317 | 3 | 11 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -22.5) |
| [[A549 (line)]] | wt | 591 | 2 | 11 (4 ⚠) | [[Betamethasone dipropionate (drug)]] 0.5 µM 2.43× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -27.1) |
| [[HEC-1-A (line)]] | alt | 384 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -29.3) |
| [[SK-MEL-2 (line)]] | alt | 251 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -23.7) |
| [[BT-474 (line)]] | alt | 260 | 2 | 10 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -21.7) |
| [[NCI-H2347 (line)]] | alt | 402 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -24.3) |
| [[PANC-1 (line)]] | alt | 403 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -30.1) |
| [[A-172 (line)]] | wt | 426 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -22.2) |
| [[SNU-423 (line)]] | alt | 852 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -25.2) |
| [[NCI-H23 (line)]] | alt | 632 | 0 | 10 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -17.0) |
| [[RKO (line)]] | wt | 135 | 2 | 8 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.85× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -20.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.0) |
| [[SNU-1 (line)]] | wt | 205 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.251× (z -13.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.8) |
| [[A498 (line)]] | wt | 435 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -19.5) |
| [[RPMI-7951 (line)]] | alt | 250 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -16.0) |
| [[CHP-212 (line)]] | wt | 356 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -24.2) |
| [[COLO 205 (line)]] | alt | 145 | 7 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 3.63× (z +13.2) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.38× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 283 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -24.4) |
| [[KATO III (line)]] | alt | 167 | 5 (2 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +14.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.493× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 247 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -28.7) |
| [[LoVo (line)]] | wt | 156 | 2 | 4 | [[Panobinostat (drug)]] 0.05 µM 1.91× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -21.5) |
| [[A-427 (line)]] | wt | 291 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -21.2) |
| [[SW48 (line)]] | wt | 200 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.9) |
| [[SW480 (line)]] | alt | 294 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -11.9) |
| [[SW 1088 (line)]] | alt | 339 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.2) |
| [[C-33 A (line)]] | alt | 371 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 269 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -21.4) |
| [[SHP-77 (line)]] | alt | 403 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -20.8) |
| [[SW 1271 (line)]] | alt | 402 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.1) |
| [[AN3 CA (line)]] | alt | 85.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 71.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 54.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 59.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 52.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 425 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.75 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ANGPTL4]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[AGTPBP1]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[AKAP13]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MT2A]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ABLIM3]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[UBE2E2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TRAM2]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ERRFI1]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[HS3ST3B1]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[NCOA3]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC37A1]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[LINC01134]] | -0.51 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[LYPLAL1-AS1]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[TLR1]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[GALNT7-DT]] | -0.47 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[ATF5]] | -0.47 | -0.45 / -0.23 | both halves | 5e-04 |  |
| [[COL16A1]] | -0.46 | -0.50 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TANC2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity raises TANC2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TOX2]] | B | TOX2 activity raises TANC2's level | lines that do not express TOX2 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without TOX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: TWIST2, OLFM1, PLEKHG4B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 11.4); signed map (14.3, 34.9). **Vector** length 126, 47.9% of its response variance represented; |z| ≥ 3 in 2,060 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.60 to 5); *metallothionein* (control, mean cos +0.60 to 5); *Response to metal ions* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.9 | +4.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.5 | +4.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +6.5 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +6.3 | +5.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +6.3 | +5.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +6.1 | +5.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -26.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.7 | -14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -19.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -20.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.9 | -0.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.6 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2-q23.3 — chr17:62,966,235-63,427,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564D166, FLJ10215, FLJ11824, KIAA1148, KIAA1636, rols, ROLSA |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCD6](https://www.uniprot.org/uniprotkb/Q9HCD6) (Protein TANC2):

> Scaffolding protein in the dendritic spines which acts as immobile postsynaptic posts able to recruit KIF1A-driven dense core vesicles to dendritic spines.

**Summary**, from NCBI Gene [26115](https://www.ncbi.nlm.nih.gov/gene/26115):

> Predicted to be a structural constituent of postsynaptic density. Predicted to be involved in dense core granule cytoskeletal transport; regulation of dendritic spine development; and regulation of dendritic spine morphogenesis. Predicted to act upstream of or within in utero embryonic development. Located in dendritic spine. Implicated in intellectual developmental disorder with autistic features and language delay, with or without seizures. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30212) · Entrez [26115](https://www.ncbi.nlm.nih.gov/gene/26115) · UniProt [Q9HCD6](https://www.uniprot.org/uniprotkb/Q9HCD6) · Ensembl [ENSG00000170921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170921)

## Data

Gene col 10028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10028); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10028]; `tensor/DDL_lfc|DDL_z.npy` [10028]; `embed/gene_vectors.npy` [10028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10028 or target_col == 10028). Every well: [[TANC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TANC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
