---
symbol: "PPM1H"
type: "gene"
col: 3193
ensembl_id: "ENSG00000111110"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1H"
location: "12q14.1-q14.2"
module: 27
arm: "+"
pooled_cpm: 38.9
n_lines_expressing: 39
n_dd_up: 44
n_dd_down: 18
n_dd_up_clean: 39
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PPM1H

*protein phosphatase, Mg2+/Mn2+ dependent 1H* — 12q14.1-q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.89× (z +16.0, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.658× (z -7.5, q 3e-11, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPFIBP2]] (+0.62, fdr 1e-05), [[DCDC2]] (+0.58, fdr 1e-05), [[CACHD1]] (+0.54, fdr 1e-05); moves opposite to [[PPP4R1L]] (-0.48, fdr 3e-05), [[CRYGS]] (-0.48, fdr 3e-04), [[HGS]] (-0.45, fdr 6e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MPP7]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC27A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +16.0 | 0e+00 | 33/37 (LoVo, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +14.8 | 0e+00 | 32/37 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +11.8 | 7e-30 | 25/36 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +11.5 | 1e-28 | 25/37 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +11.2 | 4e-27 | 24/37 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.82×** | +10.3 | 8e-23 | 29/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +9.8 | 1e-20 | 30/37 (J82, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +9.5 | 2e-19 | 29/36 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +8.6 | 5e-16 | 17/37 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +7.8 | 5e-13 | 19/36 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.36×** | +7.7 | 9e-13 | 25/37 (A-427, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.9 | 2e-10 | 16/37 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.78×** | +6.8 | 4e-10 | 26/37 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.29×** | +6.5 | 4e-09 | 22/37 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +6.3 | 1e-08 | 22/36 (SW480, SW 900, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +6.1 | 3e-08 | 21/36 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -7.5 | 3e-11 | 20/36 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -6.6 | 1e-08 | 20/36 (A498, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.699×** | -6.4 | 2e-08 | 20/33 (A-427, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.736×** | -5.5 | 4e-06 | 18/37 (SW480, NCI-H2030, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -5.1 | 4e-05 | 17/37 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.757×** | -4.8 | 1e-04 | 11/36 (A-427, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.701×** | -4.6 | 4e-04 | 18/36 (A498, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.792×** | -4.2 | 0.002 | 22/36 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.796×** | -4.1 | 0.002 | 15/36 (SW480, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.798×** | -4.1 | 0.002 | 19/35 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.784×** | -4.1 | 0.002 | 18/33 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.013 | 13/36 (CFPAC-1, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.013 | 15/36 (A-427, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.816×** | -3.5 | 0.016 | 10/37 (SW480, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.029 | 16/37 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.829×** | -3.1 | 0.050 | 11/36 (SNU-423, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.050 | 11/36 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.637×** | -3.0 | 0.066 | 5/35 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 90.0 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.395× (z -9.7) |
| [[HT-29 (line)]] | alt | 97.0 | 1 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -9.2) |
| [[SW480 (line)]] | alt | 58.7 | 4 | 2 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.93× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.357× (z -10.9) |
| [[LoVo (line)]] | wt | 42.6 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.55× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.312× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -9.2) |
| [[SW1417 (line)]] | alt | 202 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.1) |
| [[J82 (line)]] | alt | 47.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +19.2) | — |
| [[PANC-1 (line)]] | alt | 20.1 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.53× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0568× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 52.9 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.379× (z -10.0) |
| [[A-172 (line)]] | wt | 20.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +15.1) | — |
| [[KATO III (line)]] | alt | 84.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.81× (z +8.6) | — |
| [[RKO (line)]] | wt | 18.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.36× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 24.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 80.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.4) |
| [[LS 180 (line)]] | wt | 41.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +8.9) | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.01× (z +14.4) | — |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.363× (z -8.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIBP2]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DCDC2]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CACHD1]] | +0.54 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MTUS1]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SAMD12]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TRERF1]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[KSR2]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PPARGC1A]] | +0.52 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CXADR]] | +0.51 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[STK33]] | +0.51 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ADAM22]] | +0.51 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[POU3F2]] | +0.50 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R1L]] | -0.48 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CRYGS]] | -0.48 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[HGS]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[EFCAB13]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[KLC1]] | -0.44 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[SZT2]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[TBCCD1]] | -0.44 | -0.31 / -0.23 | both halves | 5e-04 |  |
| [[ZNF778]] | -0.43 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[C11orf91]] | -0.42 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[TRIOBP]] | -0.42 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[FOXL1]] | -0.42 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[GPATCH2L]] | -0.42 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP7]] | B | MPP7 activity raises PPM1H's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.54× lower at baseline in the lines without MPP7 | 0.006 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[SLC27A2]] | B | SLC27A2 activity raises PPM1H's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without SLC27A2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[KSR2]] | B | KSR2 activity raises PPM1H's level | lines that do not express KSR2 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without KSR2 | 0.035 | ⚠ within organs, on part of the lines; also absent: SPTB, MYT1, YBX2; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises PPM1H's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without ATP8B1 | 0.040 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[SAMD12]] | B | SAMD12 activity raises PPM1H's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without SAMD12 | 0.044 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[ACOXL]] | B | ACOXL activity raises PPM1H's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.51× lower at baseline in the lines without ACOXL | 0.058 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises PPM1H's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without SORL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[NR3C2]] | B | NR3C2 activity raises PPM1H's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without NR3C2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[KLHL13]] | B | KLHL13 activity raises PPM1H's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 1.15× lower at baseline in the lines without KLHL13 | 0.089 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[RNF43]] | B | RNF43 activity raises PPM1H's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without RNF43 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[MTUS1]] | B | MTUS1 activity raises PPM1H's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.34× lower at baseline in the lines without MTUS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC27A2]] | B | PPM1H activity raises SLC27A2's level | lines that do not express PPM1H (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without PPM1H | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent |
| [[RAB29]] | B | PPM1H activity raises RAB29's level | lines that do not express PPM1H (11) vs lines expressing it (39) | 1.17× lower at baseline in the lines without PPM1H | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent |
| [[SLC2A12]] | B | PPM1H activity raises SLC2A12's level | lines that do not express PPM1H (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without PPM1H | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent |
| [[NUAK1]] | B | PPM1H activity strengthens NUAK1's drug response | lines that do not express PPM1H (11) vs lines expressing it (32) | the lines without PPM1H respond 0.49× as strongly (z diff +1.55); strongest at Panobinostat 5 µM: 0.60x vs 0.37x (z diff +3.3) | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.2, 46.0); signed map (52.1, 2.4). **Vector** length 101, 26.2% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +16.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.3 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +10.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +4.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.7 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1-q14.2 — chr12:62,643,994-62,935,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1157, FLJ13253, NERPP-2C; previously ARHCL1 |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULR3](https://www.uniprot.org/uniprotkb/Q9ULR3) (Protein phosphatase 1H):

> Dephosphorylates CDKN1B at 'Thr-187', thus removing a signal for proteasomal degradation.

**Summary**, from NCBI Gene [57460](https://www.ncbi.nlm.nih.gov/gene/57460):

> Enables identical protein binding activity and phosphoprotein phosphatase activity. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18583) · Entrez [57460](https://www.ncbi.nlm.nih.gov/gene/57460) · UniProt [Q9ULR3](https://www.uniprot.org/uniprotkb/Q9ULR3) · Ensembl [ENSG00000111110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111110)

## Data

Gene col 3193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3193); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3193]; `tensor/DDL_lfc|DDL_z.npy` [3193]; `embed/gene_vectors.npy` [3193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3193 or target_col == 3193). Every well: [[PPM1H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
