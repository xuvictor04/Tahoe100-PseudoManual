---
symbol: "SFI1"
type: "gene"
col: 12528
ensembl_id: "ENSG00000198089"
name: "SFI1 centrin binding protein"
location: "22q12.2"
module: 16
arm: "-"
pooled_cpm: 40.03
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SFI1

*SFI1 centrin binding protein* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.32× (z +5.6, q 2e-05, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -23.5, q 0e+00, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.387× (z -18.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO7]] (+0.66, fdr 1e-05), [[ZMYND19]] (+0.64, fdr 1e-05), [[NPHP4]] (+0.62, fdr 2e-05); moves opposite to [[POLR2M]] (-0.63, fdr 1e-05), [[UBQLN2]] (-0.62, fdr 1e-05), [[HNRNPH2]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +5.6 | 2e-05 | 27/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 0.002 | 19/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | 1.37× | +3.3 | 0.17 | 10/48 (LoVo, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.17× | +3.0 | 0.32 | 13/47 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.440×** | -23.5 | 0e+00 | 44/47 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.387×** | -18.5 | 0e+00 | 45/48 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -14.5 | 3e-45 | 44/48 (SNU-423, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.493×** | -14.3 | 3e-44 | 42/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.321×** | -12.0 | 3e-31 | 45/48 (PANC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.607×** | -10.1 | 4e-22 | 38/48 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -9.7 | 3e-20 | 35/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -8.8 | 7e-17 | 29/47 (SNU-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.653×** | -8.6 | 4e-16 | 35/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -8.5 | 1e-15 | 40/48 (HS-578T, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.677×** | -7.9 | 1e-13 | 34/48 (H4, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.678×** | -7.9 | 2e-13 | 32/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -7.3 | 1e-11 | 33/47 (SNU-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.686×** | -7.2 | 2e-11 | 33/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.694×** | -6.8 | 3e-10 | 29/44 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -6.6 | 1e-09 | 33/48 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -5.5 | 1e-06 | 27/48 (J82, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -4.7 | 8e-05 | 21/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.871× | -3.9 | 0.002 | 17/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.834× | -3.7 | 0.005 | 15/47 (NCI-H23, C32, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.800×** | -3.2 | 0.025 | 15/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.897× | -3.1 | 0.034 | 6/48 (A-427, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.6 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.198× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 72.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.351× (z -12.4) |
| [[HS-578T (line)]] | alt | 55.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 58.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -22.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.207× (z -16.3) |
| [[PANC-1 (line)]] | alt | 41.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -21.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -17.2) |
| [[A-172 (line)]] | wt | 43.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -20.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 52.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -10.5) |
| [[A549 (line)]] | wt | 40.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -24.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 49.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -10.0) |
| [[SW 900 (line)]] | alt | 44.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.291× (z -10.4) |
| [[A498 (line)]] | wt | 45.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.264× (z -12.4) |
| [[J82 (line)]] | alt | 41.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -17.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.293× (z -12.1) |
| [[SNU-423 (line)]] | alt | 45.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -31.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.145× (z -17.8) |
| [[A-427 (line)]] | wt | 39.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.7) |
| [[C32 (line)]] | wt | 41.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.273× (z -10.2) |
| [[COLO 205 (line)]] | alt | 34.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -11.1) |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.269× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -8.7) |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0670× (z -16.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -11.1) |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -8.7) |
| [[SW480 (line)]] | alt | 28.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.381× (z -11.1) |
| [[C-33 A (line)]] | alt | 77.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 33.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.278× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 63.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.227× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0786× (z -8.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 28.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.302× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW 1088 (line)]] | alt | 62.2 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0743× (z -8.6) |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO7]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NPHP4]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[SMYD4]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TELO2]] | +0.60 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[PPP2R3B]] | +0.59 | +0.44 / +0.57 | both halves | 3e-05 | pathway: G2/M Transition |
| [[PBX4]] | +0.58 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[NFATC2IP]] | +0.58 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[MSH2]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.57 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[NUP85]] | +0.57 | +0.64 / +0.42 | both halves | 4e-05 | pathway: Mitotic Prometaphase |
| [[FANCA]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2M]] | -0.63 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[UBQLN2]] | -0.62 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[LIG4]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.58 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ZBED9]] | -0.58 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[ZNF260]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ZXDA]] | -0.57 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[RBM24]] | -0.57 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[RNF6]] | -0.57 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[RBM7]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[FUNDC1]] | -0.56 | -0.62 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises SFI1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without NT5M | 0.036 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.7, 1.7); signed map (-48.5, -16.2). **Vector** length 79.9, 18.3% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.8 | -7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.1 | -23.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.6 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.0 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -9.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | +0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | SFI1 centrin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,488,688-31,618,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0542, PISD, PPP1R139 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A8K8P3](https://www.uniprot.org/uniprotkb/A8K8P3) (Protein SFI1 homolog):

> Plays a role in the dynamic structure of centrosome-associated contractile fibers via its interaction with CETN2.

**Summary**, from NCBI Gene [9814](https://www.ncbi.nlm.nih.gov/gene/9814):

> Enables phosphatase binding activity. Located in centriole; cytosol; and nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29064) · Entrez [9814](https://www.ncbi.nlm.nih.gov/gene/9814) · UniProt [A8K8P3](https://www.uniprot.org/uniprotkb/A8K8P3) · Ensembl [ENSG00000198089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198089)

## Data

Gene col 12528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12528); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12528]; `tensor/DDL_lfc|DDL_z.npy` [12528]; `embed/gene_vectors.npy` [12528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12528 or target_col == 12528). Every well: [[SFI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
