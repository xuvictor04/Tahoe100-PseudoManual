---
symbol: "PUS7L"
type: "gene"
col: 4965
ensembl_id: "ENSG00000129317"
name: "pseudouridine synthase 7 like"
location: "12q12"
module: 215
arm: "+"
pooled_cpm: 44.47
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# PUS7L

*pseudouridine synthase 7 like* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.65× (z +14.5, q 6e-45, up in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.27× (z +3.6, q 0.044, up in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LoVo 4.23×, SW480 4.12×, SNU-423 6.10×, LS 180 4.61×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 3.57×, SNU-423 4.97×, NCI-H2347 4.38×, NCI-H1792 3.92×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-423 4.31×, NCI-H2347 3.84×, HT-29 4.24×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.266× (z -20.5, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.336× (z -16.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H3]] (+0.71, fdr 8e-06), [[UCHL5]] (+0.68, fdr 1e-05), [[RUVBL1]] (+0.66, fdr 7e-06); moves opposite to [[YPEL3]] (-0.68, fdr 1e-05), [[RBM38]] (-0.67, fdr 1e-04), [[RPS19]] (-0.66, fdr 1e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[YPEL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4965.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LoVo 4.23×, SW480 4.12×, SNU-423 6.10×, LS 180 4.61×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 3.57×, SNU-423 4.97×, NCI-H2347 4.38×, NCI-H1792 3.92×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-423 4.31×, NCI-H2347 3.84×, HT-29 4.24×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +14.5 | 6e-45 | 34/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +13.5 | 8e-39 | 44/47 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +9.9 | 7e-21 | 37/44 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.044 | 17/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.044 | 22/48 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.25× | +3.3 | 0.10 | 19/47 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 1.23× | +3.2 | 0.12 | 19/48 (SW480, LS 180, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 13/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 8/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.21× | +3.0 | 0.15 | 14/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.266×** | -20.5 | 0e+00 | 45/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.336×** | -16.9 | 0e+00 | 46/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.364×** | -15.6 | 0e+00 | 43/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.386×** | -14.7 | 0e+00 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.631×** | -10.0 | 1e-21 | 35/47 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.610×** | -7.6 | 2e-12 | 36/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -6.2 | 6e-08 | 35/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.485×** | -5.8 | 3e-07 | 28/47 (NCI-H23, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -5.8 | 3e-07 | 35/48 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.652×** | -4.7 | 1e-04 | 26/48 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.671×** | -4.6 | 2e-04 | 26/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.737×** | -4.5 | 4e-04 | 23/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -4.4 | 5e-04 | 23/47 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.001 | 23/48 (LoVo, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.729×** | -3.6 | 0.010 | 22/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.789×** | -3.4 | 0.020 | 23/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.734×** | -3.4 | 0.023 | 14/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.860× | -3.3 | 0.033 | 10/48 (KATO III, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.1 | 1 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -24.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.274× (z -12.6) |
| [[LoVo (line)]] | wt | 68.8 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.23× (z +14.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.222× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.304× (z -12.3) |
| [[RKO (line)]] | wt | 70.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -17.4) |
| [[Hs 766T (line)]] | wt | 47.9 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.11× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.163× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -10.7) |
| [[J82 (line)]] | alt | 41.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0994× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -13.3) |
| [[PANC-1 (line)]] | alt | 44.2 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -20.1) |
| [[SW480 (line)]] | alt | 65.1 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.12× (z +14.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -15.8) |
| [[A-427 (line)]] | wt | 53.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -13.2) |
| [[HOP62 (line)]] | alt | 35.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.243× (z -11.4) |
| [[HT-29 (line)]] | alt | 33.0 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.05× (z +10.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 49.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 33.5 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.32× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 119 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0737× (z -26.6) |
| [[SNU-423 (line)]] | alt | 43.7 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.10× (z +13.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.302× (z -9.4) |
| [[A549 (line)]] | wt | 31.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.0701× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -10.1) |
| [[H4 (line)]] | wt | 50.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0866× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 44.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.37× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.249× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 60.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.238× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.279× (z -11.1) |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.178× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 24.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 52.1 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.105× (z -14.8) |
| [[A-172 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -11.8) |
| [[BT-474 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.223× (z -11.1) |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.273× (z -8.7) |
| [[C32 (line)]] | wt | 34.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.6) |
| [[COLO 205 (line)]] | alt | 47.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -13.5) |
| [[HCT15 (line)]] | alt | 55.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -10.0) |
| [[HS-578T (line)]] | alt | 38.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -8.8) |
| [[LS 180 (line)]] | wt | 42.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.61× (z +12.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -9.5) |
| [[SW1417 (line)]] | alt | 32.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.16× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.247× (z -11.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.351× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.290× (z -11.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | +0.71 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[UCHL5]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RUVBL1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PDAP1]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[GUF1]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ZNF460]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[FARSB]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CEP41]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL3]] | -0.68 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[RBM38]] | -0.67 | -0.35 / -0.77 | both halves | 1e-04 |  |
| [[RPS19]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[COX4I1]] ⚠ | -0.65 | -0.55 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.65 | -0.50 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC34]] | -0.64 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[ULK1]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[RPS29]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RPL36]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[RPS27]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.63 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.62 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[BRI3]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[NENF]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YPEL3]] | B | YPEL3 activity lowers PUS7L's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without YPEL3 | 0.094 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.7, -25.4); signed map (-5.3, -38.2). **Vector** length 103, 30.6% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +13.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -20.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.2 | -2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.8 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine synthase 7 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:43,718,992-43,758,793 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434G1415 |
| Gene groups (HGNC) | Pseudouridine synthases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0K6](https://www.uniprot.org/uniprotkb/Q9H0K6) (Pseudouridylate synthase PUS7L):

> Pseudouridine synthase that catalyzes pseudouridylation of mRNAs.

**Summary**, from NCBI Gene [83448](https://www.ncbi.nlm.nih.gov/gene/83448):

> Enables pseudouridine synthase activity. Involved in mRNA pseudouridine synthesis. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25276) · Entrez [83448](https://www.ncbi.nlm.nih.gov/gene/83448) · UniProt [Q9H0K6](https://www.uniprot.org/uniprotkb/Q9H0K6) · Ensembl [ENSG00000129317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129317)

## Data

Gene col 4965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4965); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4965]; `tensor/DDL_lfc|DDL_z.npy` [4965]; `embed/gene_vectors.npy` [4965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4965 or target_col == 4965). Every well: [[PUS7L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUS7L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
