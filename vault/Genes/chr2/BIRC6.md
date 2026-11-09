---
symbol: "BIRC6"
type: "gene"
col: 3717
ensembl_id: "ENSG00000115760"
name: "baculoviral IAP repeat containing 6"
location: "2p22.3"
module: 40
arm: "+"
pooled_cpm: 570.21
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# BIRC6

*baculoviral IAP repeat containing 6* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.43× (z +14.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.405× (z -20.9, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.679× (z -12.7, q 1e-34, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBAS]] (+0.65, fdr 7e-06), [[VPS53]] (+0.59, fdr 1e-05), [[COP1]] (+0.59, fdr 7e-06); moves opposite to [[CDC42EP1]] (-0.59, fdr 1e-05), [[PNRC2]] (-0.56, fdr 1e-05), [[TAF9]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.43×** | +14.9 | 0e+00 | 48/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +11.2 | 2e-26 | 48/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +9.2 | 5e-18 | 48/48 (NCI-H23, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.6 | 8e-16 | 44/48 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +8.4 | 6e-15 | 40/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 7e-09 | 37/48 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +6.2 | 3e-08 | 32/48 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.9 | 3e-07 | 35/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.7 | 9e-07 | 38/48 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.43×** | +4.3 | 8e-04 | 39/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.059 | 28/49 (AN3 CA, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.059 | 29/49 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.059 | 28/48 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.088 | 15/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.405×** | -20.9 | 0e+00 | 49/49 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.396×** | -20.6 | 0e+00 | 44/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.484×** | -15.5 | 0e+00 | 41/45 (RPMI-7951, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.509×** | -15.0 | 0e+00 | 46/47 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -12.7 | 1e-34 | 37/49 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -9.8 | 7e-21 | 41/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.658×** | -9.7 | 3e-20 | 47/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.685×** | -8.8 | 2e-16 | 41/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -7.4 | 8e-12 | 46/48 (SW 1271, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.784×** | -5.6 | 1e-06 | 30/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.787×** | -5.6 | 1e-06 | 34/48 (AsPC-1, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.786×** | -5.4 | 4e-06 | 27/48 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.792×** | -5.2 | 1e-05 | 28/50 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -4.8 | 6e-05 | 29/48 (NCI-H1573, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.814×** | -4.8 | 7e-05 | 28/48 (KATO III, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.830×** | -4.3 | 5e-04 | 24/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.860× | -3.5 | 0.015 | 19/48 (C32, LoVo, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.854× | -3.5 | 0.016 | 16/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.866× | -3.3 | 0.024 | 11/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.871× | -3.2 | 0.037 | 14/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.909× | -3.2 | 0.041 | 6/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.873× | -2.9 | 0.086 | 17/47 (H4, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.916× | -2.9 | 0.087 | 4/48 (A549, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 598 | 4 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.32× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.301× (z -18.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.499× (z -11.4) |
| [[SW480 (line)]] | alt | 591 | 3 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.478× (z -14.1) |
| [[A-172 (line)]] | wt | 461 | 4 | 7 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.98× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -15.9) |
| [[HOP62 (line)]] | alt | 495 | 6 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.16× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -15.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 583 | 2 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -15.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -15.2) |
| [[LS 180 (line)]] | wt | 606 | 3 | 8 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 4.46× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 557 | 4 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.404× (z -17.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 675 | 1 | 9 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 2.79× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 526 | 1 | 9 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.576× (z -9.6) |
| [[SW1417 (line)]] | alt | 646 | 3 | 7 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.93× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -19.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -12.0) |
| [[LoVo (line)]] | wt | 605 | 2 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.31× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -11.2) |
| [[C32 (line)]] | wt | 549 | 2 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.478× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 677 | 2 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.51× (z +12.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.310× (z -18.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.433× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 472 | 3 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -18.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 712 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.527× (z -9.9) |
| [[A549 (line)]] | wt | 752 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -26.8) |
| [[HepG2_C3A (line)]] | wt | 581 | 4 | 3 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.85× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 388 | 3 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.590× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 496 | 1 | 6 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.90× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.2) |
| [[J82 (line)]] | alt | 378 | 1 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -17.9) |
| [[NCI-H1573 (line)]] | alt | 663 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 498 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.87× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 616 | 5 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.27× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -23.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 646 | 3 (1 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.06× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -15.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 771 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -14.0) |
| [[COLO 205 (line)]] | alt | 457 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.07× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 710 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.604× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 339 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.43× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.636× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 650 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.10× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.584× (z -9.2) |
| [[PANC-1 (line)]] | alt | 581 | 4 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.29× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -14.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 661 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 2.73× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -19.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 574 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.70× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 358 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.51× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 517 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.52× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.477× (z -9.6) |
| [[A-427 (line)]] | wt | 853 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 2.82× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -30.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 683 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -17.3) |
| [[BT-474 (line)]] | alt | 362 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.89× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 475 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.72× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -16.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 601 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.8) |
| [[HCT15 (line)]] | alt | 669 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -8.7) |
| [[AN3 CA (line)]] | alt | 463 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.43× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 470 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -18.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 459 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.50× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 413 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -15.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 426 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.24× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 757 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.349× (z -10.0) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 520 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.355× (z -9.1) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 580 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 601 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 481 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBAS]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[VPS53]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[COP1]] | +0.59 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TBC1D22A]] | +0.59 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[RNF216]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 | same gene group |
| [[GLG1]] | +0.57 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[UBE4B]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 | STRING 448 |
| [[GAPVD1]] | +0.55 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[EIF3K]] | +0.54 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[AGAP4]] | +0.54 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[POMP]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SPATC1L]] | +0.53 | +0.50 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP1]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.56 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[TAF9]] | -0.52 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[ZSCAN9]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[APOBEC3B]] | -0.49 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[ZNF627]] | -0.48 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DHRS12]] | -0.48 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[TRIM21]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[OGFRL1]] | -0.47 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[BPHL]] | -0.47 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[RNF207]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[CGGBP1]] | -0.47 | -0.65 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BIRC6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDC42EP1]] | B | CDC42EP1 activity raises BIRC6's level | lines that do not express CDC42EP1 (5) vs lines expressing it (45) | 1.19× lower at baseline in the lines without CDC42EP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZFP36, IQCN, SLC22A20P |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (1.6, -22.7); signed map (-46.6, 3.4). **Vector** length 87.1, 38.7% of its response variance represented; |z| ≥ 3 in 1,576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +0.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -15.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -5.6 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | baculoviral IAP repeat containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:32,357,023-32,619,571 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRUCE |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2; Baculoviral IAP repeat containing; MicroRNA protein coding host genes; Atypical E3 ubiquitin ligases |
| Reactome | 4 pathways, smallest: ALK mutants bind TKIs; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR09](https://www.uniprot.org/uniprotkb/Q9NR09) (Dual E2 ubiquitin-conjugating enzyme/E3 ubiquitin-protein ligase BIRC6):

> Anti-apoptotic protein known as inhibitor of apoptosis (IAP) which can regulate cell death by controlling caspases and by acting as an E3 ubiquitin-protein ligase. Unlike most IAPs, does not contain a RING domain and it is not a RING-type E3 ligase. Instead acts as a dual E2/E3 enzyme that combines ubiquitin conjugating (E2) and ubiquitin ligase (E3) activities in a single polypeptide. Ubiquitination is mediated by a non-canonical E1 ubiquitin activating enzyme UBA6. Ubiquitinates CASP3, CASP7 …

**Summary**, from NCBI Gene [57448](https://www.ncbi.nlm.nih.gov/gene/57448):

> This gene encodes a protein with a BIR (baculoviral inhibition of apoptosis protein repeat) domain and a UBCc (ubiquitin-conjugating enzyme E2, catalytic) domain. This protein inhibits apoptosis by facilitating the degradation of apoptotic proteins by ubiquitination. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13516) · Entrez [57448](https://www.ncbi.nlm.nih.gov/gene/57448) · UniProt [Q9NR09](https://www.uniprot.org/uniprotkb/Q9NR09) · Ensembl [ENSG00000115760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115760)

## Data

Gene col 3717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3717); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3717]; `tensor/DDL_lfc|DDL_z.npy` [3717]; `embed/gene_vectors.npy` [3717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3717 or target_col == 3717). Every well: [[BIRC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIRC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
