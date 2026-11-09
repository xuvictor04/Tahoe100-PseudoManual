---
symbol: "KDSR"
type: "gene"
col: 4077
ensembl_id: "ENSG00000119537"
name: "3-ketodihydrosphingosine reductase"
location: "18q21.33"
module: 30
arm: "-"
pooled_cpm: 86.55
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# KDSR

*3-ketodihydrosphingosine reductase* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +18.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.504× (z -14.9, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNG12-AS1]] (+0.69, fdr 9e-06), [[MAFF]] (+0.67, fdr 1e-05), [[MSRA]] (+0.66, fdr 1e-05); moves opposite to [[HBS1L]] (-0.65, fdr 7e-06), [[SLC9A6]] (-0.63, fdr 3e-05), [[USP35]] (-0.63, fdr 3e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +18.5 | 0e+00 | 44/48 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +15.8 | 0e+00 | 44/49 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +10.1 | 6e-22 | 38/48 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +8.4 | 7e-15 | 34/48 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.9 | 8e-10 | 29/49 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 7e-08 | 32/48 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +5.2 | 1e-05 | 28/48 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.2 | 1e-05 | 26/44 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +5.1 | 2e-05 | 27/48 (LOX-IMVI, HT-29, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 25/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.9 | 5e-05 | 27/50 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.20× | +4.0 | 0.003 | 24/48 (LOX-IMVI, A-172, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | **1.22×** | +3.6 | 0.014 | 21/45 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.021 | 9/48 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 1.17× | +3.4 | 0.024 | 20/48 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.053 | 5/48 (H4, KATO III, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 5 µM |  | 1.15× | +2.9 | 0.099 | 10/48 (SW1417, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.504×** | -14.9 | 0e+00 | 43/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -11.1 | 4e-26 | 37/48 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.624×** | -10.3 | 2e-22 | 39/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -7.8 | 7e-13 | 34/48 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -7.5 | 5e-12 | 39/48 (LoVo, SNU-1, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.749×** | -6.0 | 2e-07 | 33/49 (SW 1088, A-172, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.586×** | -5.9 | 4e-07 | 30/48 (Hs 766T, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.758×** | -5.8 | 5e-07 | 27/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -5.4 | 3e-06 | 29/48 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.786×** | -5.2 | 1e-05 | 30/49 (LOX-IMVI, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.849× | -4.9 | 4e-05 | 22/48 (HEC-1-A, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.762×** | -4.9 | 5e-05 | 30/48 (C32, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.794×** | -4.8 | 7e-05 | 26/48 (LOX-IMVI, C32, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.797×** | -4.7 | 1e-04 | 26/48 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.809×** | -4.6 | 2e-04 | 24/48 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.658×** | -4.6 | 2e-04 | 27/48 (MIA PaCa-2, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.829×** | -4.6 | 2e-04 | 22/49 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 150 | 5 (3 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.3) | [[Cobimetinib (drug)]] 5 µM 0.390× (z -11.2) |
| [[HS-578T (line)]] | alt | 101 | 6 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.410× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.355× (z -14.2) |
| [[A-172 (line)]] | wt | 101 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.2) | [[Belinostat (drug)]] 5 µM 0.419× (z -10.9) |
| [[A549 (line)]] | wt | 93.1 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.397× (z -11.9) |
| [[H4 (line)]] | wt | 138 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.8) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0634× (z -14.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.408× (z -9.2) |
| [[HOP62 (line)]] | alt | 42.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.428× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 162 | 2 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.354× (z -12.5) |
| [[RKO (line)]] | wt | 178 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -14.8) |
| [[C32 (line)]] | wt | 117 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.450× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 104 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +17.4) | — |
| [[J82 (line)]] | alt | 108 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.483× (z -9.6) |
| [[LoVo (line)]] | wt | 129 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.431× (z -11.2) |
| [[SNU-423 (line)]] | alt | 85.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 87.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.291× (z -11.6) |
| [[LS 180 (line)]] | wt | 81.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 52.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.456× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 41.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 70.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.6) | — |
| [[SNU-1 (line)]] | wt | 122 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -9.1) |
| [[SW480 (line)]] | alt | 53.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.419× (z -11.8) |
| [[BT-474 (line)]] | alt | 100 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -11.2) |
| [[C-33 A (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.403× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 54.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 68.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 58.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 90.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.426× (z -9.3) |
| [[A498 (line)]] | wt | 72.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 117 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 98.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.470× (z -9.1) |
| [[KATO III (line)]] | alt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 73.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.6) | — |
| [[NCI-H596 (line)]] | alt | 79.1 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.153× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 88.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 98.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -9.5) |
| [[SW48 (line)]] | wt | 82.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.5) | — |
| [[A-427 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 91.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12-AS1]] | +0.69 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[MAFF]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[MSRA]] | +0.66 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[HELQ]] | +0.64 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ANGPT2]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ZC3H12C]] | +0.62 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[LINC01138]] | +0.61 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ADGRL4]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[DGKH]] | +0.59 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[ERCC6L2]] | +0.59 | +0.60 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBS1L]] | -0.65 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.63 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[USP35]] | -0.63 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[STAM]] | -0.61 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[MKRN2]] | -0.61 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[HTT]] | -0.61 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[VDAC3]] | -0.60 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[NDRG3]] | -0.60 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[CTNNBL1]] | -0.60 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[RIMS3]] | -0.59 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ATP5F1C]] | -0.59 | -0.59 / -0.43 | both halves | 4e-05 |  |
| [[ELP1]] | -0.59 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KDSR's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.009 | ⚠ off-target possible; 4 compounds |
| [[ZNF702P]] | B | ZNF702P activity lowers KDSR's level | lines that do not express ZNF702P (24) vs lines expressing it (26) | 1.31× higher at baseline in the lines without ZNF702P | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33 |
| [[TOP2A]] | B | TOP2A activity lowers KDSR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (28.6, -4.1); signed map (15.1, -3.0). **Vector** length 139, 43.0% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.6 | +10.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +0.9 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.7 | -14.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.0 | -11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.3 | -10.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.0 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.7 | -7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.6 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | 3-ketodihydrosphingosine reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,327,726-63,367,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHSR, SDR35C1; previously FVT1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06136](https://www.uniprot.org/uniprotkb/Q06136) (3-ketodihydrosphingosine reductase):

> Catalyzes the reduction of 3'-oxosphinganine (3-ketodihydrosphingosine/KDS) to sphinganine (dihydrosphingosine/DHS), the second step of de novo sphingolipid biosynthesis.

**Summary**, from NCBI Gene [2531](https://www.ncbi.nlm.nih.gov/gene/2531):

> The protein encoded by this gene catalyzes the reduction of 3-ketodihydrosphingosine to dihydrosphingosine. The putative active site residues of the encoded protein are found on the cytosolic side of the endoplasmic reticulum membrane. A chromosomal rearrangement involving this gene is a cause of follicular lymphoma, also known as type II chronic lymphatic leukemia. The mutation of a conserved residue in the bovine ortholog causes spinal muscular atrophy. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4021) · Entrez [2531](https://www.ncbi.nlm.nih.gov/gene/2531) · UniProt [Q06136](https://www.uniprot.org/uniprotkb/Q06136) · Ensembl [ENSG00000119537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119537)

## Data

Gene col 4077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4077); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4077]; `tensor/DDL_lfc|DDL_z.npy` [4077]; `embed/gene_vectors.npy` [4077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4077 or target_col == 4077). Every well: [[KDSR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDSR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
