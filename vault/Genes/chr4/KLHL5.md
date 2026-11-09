---
symbol: "KLHL5"
type: "gene"
col: 3082
ensembl_id: "ENSG00000109790"
name: "kelch like family member 5"
location: "4p14"
module: 66
arm: "+"
pooled_cpm: 99.57
n_lines_expressing: 43
n_dd_up: 13
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 11
direction_downstream: 11
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# KLHL5

*kelch like family member 5* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +17.7, q 0e+00, up in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +7.2, q 1e-10, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.564× (z -10.8, q 3e-24, down in 30 of 41 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.697× (z -6.8, q 1e-09, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGAV]] (+0.72, fdr 7e-06), [[CCDC50]] (+0.64, fdr 3e-05), [[SEMA3C]] (+0.61, fdr 1e-05); moves opposite to [[MPG]] (-0.58, fdr 3e-05), [[LSM11]] (-0.56, fdr 1e-05), [[EIF1AD]] (-0.55, fdr 9e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); 11 go from it, the strongest it → [[OGFRL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +17.7 | 0e+00 | 40/42 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +16.8 | 0e+00 | 37/38 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +12.1 | 1e-31 | 35/39 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.2 | 1e-10 | 28/41 (HT-29, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +7.0 | 3e-10 | 29/42 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.4 | 5e-06 | 24/40 (hTERT-HPNE, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 1e-04 | 21/41 (A498, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 5e-04 | 19/42 (SW480, A-172, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +4.4 | 8e-04 | 21/41 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.1 | 0.002 | 14/41 (A498, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.002 | 20/40 (NCI-H23, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.006 | 17/41 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.8 | 0.006 | 12/41 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.016 | 16/41 (Hs 766T, CHP-212, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.026 | 13/41 (A498, A-172, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.031 | 12/42 (Panc 03.27, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.055 | 12/41 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.12× | +3.1 | 0.057 | 5/42 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3082.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.564×** | -10.8 | 3e-24 | 30/41 (PANC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.619×** | -9.0 | 5e-17 | 28/41 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.664×** | -7.7 | 2e-12 | 28/41 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -6.8 | 1e-09 | 25/41 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -6.2 | 5e-08 | 27/41 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -6.2 | 6e-08 | 26/41 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.791×** | -6.1 | 6e-08 | 21/42 (A549, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.726×** | -6.0 | 1e-07 | 26/41 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.727×** | -6.0 | 1e-07 | 25/41 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.744×** | -5.6 | 2e-06 | 23/41 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.557×** | -5.5 | 2e-06 | 27/41 (SW 900, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -5.2 | 9e-06 | 23/41 (HepG2/C3A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.699×** | -4.8 | 6e-05 | 29/41 (SW480, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -4.7 | 1e-04 | 21/41 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.780×** | -4.7 | 1e-04 | 23/41 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.645×** | -4.2 | 0.001 | 16/40 (H4, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.670×** | -3.8 | 0.005 | 18/41 (RPMI-7951, SW 1088, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.689×** | -3.5 | 0.012 | 17/42 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.883× | -3.3 | 0.029 | 6/42 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.710×** | -3.2 | 0.031 | 15/41 (SW480, hTERT-HPNE, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.714×** | -3.2 | 0.034 | 14/41 (SW 900, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.723×** | -3.1 | 0.047 | 12/41 (SW 900, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.799×** | -3.0 | 0.055 | 10/42 (PANC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 221 | 3 (3 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +15.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.384× (z -15.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.532× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 151 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 68.3 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.05× (z +13.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 89.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.91× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.85× (z +9.0) | — |
| [[A549 (line)]] | wt | 157 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.66× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 26.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.65× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 202 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +15.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 36.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +11.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 69.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 194 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.353× (z -8.5) |
| [[HOP62 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +16.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 119 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +15.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 135 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 95.1 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.344× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 151 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +13.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 68.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.50× (z +10.1) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.131× (z -9.0) |
| [[A-427 (line)]] | wt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 98.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 50.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.228× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 28.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.447× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[SW 1088 (line)]] | alt | 81.2 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0724× (z -8.5) |
| [[SW 900 (line)]] | alt | 437 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.5 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGAV]] | +0.72 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CCDC50]] | +0.64 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SEMA3C]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF12]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ACADM]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[RDX]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CDH2]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NALCN]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[RAB31]] | +0.56 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[RIPK2-DT]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.56 | +0.62 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.58 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[LSM11]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[EIF1AD]] | -0.55 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[QPCTL]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[THOC3]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NUDT22]] | -0.53 | -0.24 / -0.55 | both halves | 4e-04 |  |
| [[SLC35E1]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DHDDS]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[POM121]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SPICE1]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HLA-F-AS1]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises KLHL5's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.85× lower at baseline in the lines without HEG1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[MSRB3]] | B | MSRB3 activity raises KLHL5's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without MSRB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[NALCN]] | B | NALCN activity raises KLHL5's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without NALCN | 0.045 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[ZDHHC2]] | B | ZDHHC2 activity raises KLHL5's level | lines that do not express ZDHHC2 (10) vs lines expressing it (40) | 3.76× lower at baseline in the lines without ZDHHC2 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000289145, TGFB1, PGM5P2 |
| [[ZC3H12C]] | B | ZC3H12C activity raises KLHL5's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 3.10× lower at baseline in the lines without ZC3H12C | 0.048 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[MYL9]] | B | MYL9 activity raises KLHL5's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 2.13× lower at baseline in the lines without MYL9 | 0.082 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CACNA2D1]] | B | CACNA2D1 activity raises KLHL5's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without CACNA2D1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[ZNF215]] | B | ZNF215 activity raises KLHL5's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without ZNF215 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[SLC16A2]] | C | SLC16A2 activity raises KLHL5's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 3.20× lower at baseline in the lines without SLC16A2 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405; co-absent with the target |
| [[ENAH]] | C | ENAH activity raises KLHL5's level | lines that do not express ENAH (3) vs lines expressing it (47) | 4.64× lower at baseline in the lines without ENAH | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SSBP2, DIP2C, SOX12; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity raises KLHL5's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 6.22× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OGFRL1]] | B | KLHL5 activity raises OGFRL1's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 4.51× lower at baseline in the lines without KLHL5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | KLHL5 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLHL5 (7) vs lines expressing it (41) | the lines without KLHL5: 0.82× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[ZC3H12C]] | B | KLHL5 activity raises ZC3H12C's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 3.79× lower at baseline in the lines without KLHL5 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[CREBL2]] | B | KLHL5 activity raises CREBL2's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without KLHL5 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[CRIM1]] | B | KLHL5 activity raises CRIM1's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without KLHL5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | KLHL5 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KLHL5 (7) vs lines expressing it (41) | the lines without KLHL5: 1.26× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[RDX]] | B | KLHL5 activity raises RDX's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 3.25× lower at baseline in the lines without KLHL5 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[MYL9]] | B | KLHL5 activity raises MYL9's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without KLHL5 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[HEG1]] | B | KLHL5 activity raises HEG1's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 2.34× lower at baseline in the lines without KLHL5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| cells under [[Tranilast (drug)]] 0.5 µM | B | KLHL5 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express KLHL5 (7) vs lines expressing it (41) | the lines without KLHL5: 0.84× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[SLC16A2]] | C | KLHL5 activity raises SLC16A2's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 6.14× lower at baseline in the lines without KLHL5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.2, 27.5); signed map (47.1, 19.6). **Vector** length 121, 36.4% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +12.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.4 | +4.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.8 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | -10.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -6.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,045,039-39,126,857 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

UniProt [Q96PQ7](https://www.uniprot.org/uniprotkb/Q96PQ7) carries no function annotation.

**Summary**, from NCBI Gene [51088](https://www.ncbi.nlm.nih.gov/gene/51088):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Located in microtubule cytoskeleton. Implicated in cocaine dependence. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6356) · Entrez [51088](https://www.ncbi.nlm.nih.gov/gene/51088) · UniProt [Q96PQ7](https://www.uniprot.org/uniprotkb/Q96PQ7) · Ensembl [ENSG00000109790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109790)

## Data

Gene col 3082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3082); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3082]; `tensor/DDL_lfc|DDL_z.npy` [3082]; `embed/gene_vectors.npy` [3082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3082 or target_col == 3082). Every well: [[KLHL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
