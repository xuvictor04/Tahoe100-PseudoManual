---
symbol: "VRK3"
type: "gene"
col: 2542
ensembl_id: "ENSG00000105053"
name: "VRK serine/threonine kinase 3"
location: "19q13.33"
module: 3
arm: "+"
pooled_cpm: 44.38
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# VRK3

*VRK serine/threonine kinase 3* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.45× (z +9.2, q 2e-17, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.473× (z -16.8, q 0e+00, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.613× (z -11.9, q 1e-30, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD4B]] (+0.71, fdr 7e-06), [[MED31]] (+0.70, fdr 7e-06), [[POLR2J4]] (+0.68, fdr 1e-05); moves opposite to [[POGLUT1]] (-0.67, fdr 1e-05), [[OXCT1]] (-0.65, fdr 1e-05), [[SLC12A2-DT]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +9.2 | 2e-17 | 34/48 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +8.6 | 2e-15 | 33/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +8.2 | 4e-14 | 28/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +6.3 | 5e-08 | 29/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +6.3 | 5e-08 | 26/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.9 | 3e-07 | 23/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +5.6 | 2e-06 | 23/47 (NCI-H2030, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +4.6 | 3e-04 | 16/47 (A-172, LoVo, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.09× | +3.1 | 0.11 | 5/48 (SW 900, KATO III, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.12 | 6/48 (A498, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.473×** | -16.8 | 0e+00 | 36/42 (H4, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.530×** | -15.4 | 0e+00 | 37/47 (H4, NCI-H1792, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.656×** | -14.5 | 4e-45 | 34/47 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.555×** | -13.2 | 8e-38 | 33/40 (A-172, LS 180, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -11.9 | 1e-30 | 38/47 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -9.8 | 7e-21 | 32/47 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -8.9 | 6e-17 | 34/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -8.2 | 2e-14 | 32/49 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.702×** | -7.9 | 2e-13 | 27/48 (NCI-H1792, SNU-423, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.745×** | -7.1 | 6e-11 | 32/48 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.780×** | -6.0 | 1e-07 | 24/47 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.840× | -5.9 | 1e-07 | 22/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.664×** | -5.2 | 9e-06 | 23/48 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.677×** | -5.0 | 3e-05 | 18/35 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.802×** | -4.9 | 3e-05 | 23/46 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -4.7 | 8e-05 | 24/48 (SNU-423, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.700×** | -4.5 | 2e-04 | 20/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.705×** | -4.4 | 3e-04 | 20/48 (H4, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.709×** | -4.3 | 4e-04 | 20/48 (LOX-IMVI, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.718×** | -4.2 | 8e-04 | 15/48 (CFPAC-1, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.843× | -4.1 | 0.001 | 16/48 (A-172, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.874× | -3.2 | 0.029 | 12/48 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.033 | 16/48 (NCI-H1573, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Cilostazol (drug)]] 0.05 µM |  | 0.872× | -3.0 | 0.050 | 10/48 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.792×** | -2.9 | 0.064 | 9/48 (SNU-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.878× | -2.9 | 0.078 | 14/48 (HS-578T, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 51.3 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 56.4 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -13.0) |
| [[A549 (line)]] | wt | 70.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.442× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 52.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 54.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -9.2) |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -16.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 58.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0632× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 56.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -12.2) |
| [[SW480 (line)]] | alt | 43.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -14.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 51.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -13.1) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.131× (z -10.3) |
| [[SW 900 (line)]] | alt | 58.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 30.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0969× (z -11.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -12.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 70.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 36.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.154× (z -10.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -9.5) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD4B]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[MED31]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[POLR2J4]] | +0.68 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[CCDC32]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ZCCHC17]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.63 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[SDF2]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DUSP18]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SWI5]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RNF181]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT1]] | -0.67 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[OXCT1]] | -0.65 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[PARD3B]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SEPTIN11]] | -0.63 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TMEM64]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[OTUD4]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MCCC2]] | -0.61 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[NCR3LG1]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SLC16A9]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[DIS3L]] | -0.61 | -0.64 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers VRK3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers VRK3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.0, -5.6); signed map (-24.5, 8.9). **Vector** length 106, 27.4% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +7.7 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.7 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +8.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.6 | -14.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -16.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -9.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.4 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | VRK serine/threonine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,976,468-50,025,946 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | VRK serine/threonine kinase family |
| Reactome | 28 pathways, smallest: ERKs are inactivated; ERK/MAPK targets; MAPK targets/ Nuclear events mediated by MAP kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV63](https://www.uniprot.org/uniprotkb/Q8IV63) (Serine/threonine-protein kinase VRK3):

> Plays a role in the regulation of the cell cycle by phosphorylating the nuclear envelope protein barrier-to-autointegration factor/BAF that is required for disassembly and reassembly, respectively, of the nuclear envelope during mitosis. Under normal physiological conditions, negatively regulates ERK activity along with VHR/DUSP3 phosphatase in the nucleus, causing timely and transient action of ERK. Stress conditions activate CDK5 which phosphorylates VRK3 to increase VHR phosphatase activity …

**Summary**, from NCBI Gene [51231](https://www.ncbi.nlm.nih.gov/gene/51231):

> This gene encodes a member of the vaccinia-related kinase (VRK) family of serine/threonine protein kinases. In both human and mouse, this gene has substitutions at several residues within the ATP binding motifs that in other kinases have been shown to be required for catalysis. In vitro assays indicate the protein lacks phosphorylation activity. The protein, however, likely retains its substrate binding capability. This gene is widely expressed in human tissues and its protein localizes to the …

**Accessions** — [HGNC:18996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18996) · Entrez [51231](https://www.ncbi.nlm.nih.gov/gene/51231) · UniProt [Q8IV63](https://www.uniprot.org/uniprotkb/Q8IV63) · Ensembl [ENSG00000105053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105053)

## Data

Gene col 2542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2542); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2542]; `tensor/DDL_lfc|DDL_z.npy` [2542]; `embed/gene_vectors.npy` [2542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2542 or target_col == 2542). Every well: [[VRK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VRK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
