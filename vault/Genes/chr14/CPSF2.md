---
symbol: "CPSF2"
type: "gene"
col: 9211
ensembl_id: "ENSG00000165934"
name: "cleavage and polyadenylation specific factor 2"
location: "14q32.12"
module: 194
arm: "+"
pooled_cpm: 64.8
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# CPSF2

*cleavage and polyadenylation specific factor 2* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.58× (z +20.8, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.06× (z +15.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.623× (z -10.4, q 1e-22, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND11]] (+0.75, fdr 7e-06), [[ST7L]] (+0.75, fdr 1e-05), [[ANAPC7]] (+0.74, fdr 7e-06); moves opposite to [[SDHAP1]] (-0.72, fdr 1e-05), [[MOSPD3]] (-0.72, fdr 1e-05), [[SDHAP2]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.58×** | +20.8 | 0e+00 | 45/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +20.6 | 0e+00 | 43/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.78×** | +18.0 | 0e+00 | 43/48 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +15.9 | 0e+00 | 44/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +14.6 | 0e+00 | 44/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +14.4 | 4e-45 | 42/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.84×** | +12.4 | 4e-33 | 39/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +11.5 | 1e-28 | 35/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.3 | 4e-23 | 37/48 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +10.3 | 4e-23 | 47/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +8.0 | 7e-14 | 28/48 (HEC-1-A, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +7.9 | 1e-13 | 34/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +7.5 | 2e-12 | 30/48 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.37×** | +7.0 | 1e-10 | 29/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.34×** | +6.5 | 3e-09 | 28/48 (H4, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.3 | 3e-06 | 28/48 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 8e-06 | 23/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +4.7 | 7e-05 | 20/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.7 | 7e-05 | 22/48 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.13× | +3.7 | 0.005 | 11/48 (NCI-H460, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -10.4 | 1e-22 | 31/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.657×** | -9.3 | 6e-18 | 30/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -6.9 | 1e-09 | 26/48 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.744×** | -6.5 | 9e-09 | 27/48 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.772×** | -5.7 | 1e-06 | 29/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.796×** | -5.0 | 4e-05 | 26/48 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.656×** | -4.9 | 9e-05 | 26/49 (A498, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 0.863× | -4.6 | 3e-04 | 19/48 (A-427, CHP-212, …) | all doses, flat | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM |  | **0.811×** | -4.5 | 5e-04 | 17/48 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.779×** | -3.9 | 0.005 | 20/48 (HEC-1-A, SW48, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.6 | 0.017 | 20/48 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.028 | 17/47 (MIA PaCa-2, J82, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.857× | -3.4 | 0.028 | 16/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.868× | -3.0 | 0.10 | 11/47 (AsPC-1, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 84.5 | 7 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.30× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.522× (z -9.9) |
| [[PANC-1 (line)]] | alt | 71.1 | 6 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +17.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.46× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.510× (z -10.4) |
| [[HOP62 (line)]] | alt | 40.1 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.7 | 6 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 56.1 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +14.8) | — |
| [[A-172 (line)]] | wt | 43.3 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.46× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 55.4 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 45.4 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 159 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 74.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.490× (z -10.0) |
| [[SNU-423 (line)]] | alt | 30.6 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.0) | — |
| [[A498 (line)]] | wt | 52.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +9.8) | — |
| [[A549 (line)]] | wt | 56.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.24× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 40.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 58.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.24× (z +8.6) | — |
| [[A-427 (line)]] | wt | 93.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 64.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 80.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -12.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.416× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 85.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.59× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 76.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 28.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 47.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.33× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 49.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 52.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.0) | — |
| [[LoVo (line)]] | wt | 59.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 58.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 75.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 62.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Belinostat (drug)]] 5 µM 0.385× (z -10.7) |
| [[H4 (line)]] | wt | 42.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 52.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H661 (line)]] | alt | 81.7 | 0 | 1 | — | [[LJI308 (drug)]] 0.5 µM 0.0597× (z -9.5) |
| [[RKO (line)]] | wt | 96.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.432× (z -9.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 82.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -12.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 59.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +12.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | +0.75 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ST7L]] | +0.75 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.74 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.74 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ERCC6L2]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NSD1]] | +0.70 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZFP91]] | +0.70 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MED1]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CYREN]] | +0.69 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[TASOR]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PRDM5]] | +0.67 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.72 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.72 | -0.74 / -0.55 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.71 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[PLCD1]] | -0.71 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[DOK4]] | -0.70 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[CARHSP1]] | -0.70 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.70 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SEMA6C]] | -0.69 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[DPM1]] | -0.69 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[PLD3]] | -0.68 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[SLC27A1]] | -0.68 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[LMBR1L]] | -0.68 | -0.66 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPSF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CPSF2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CPSF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ATG9B]] | B | ATG9B activity lowers CPSF2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.18× higher at baseline in the lines without ATG9B | 0.089 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.884). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.4, 3.0); signed map (17.5, -28.3). **Vector** length 131, 42.6% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.9 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +15.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.6 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +7.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +7.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.4 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.2 | -10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.5 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.8 | -5.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | cleavage and polyadenylation specific factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:92,121,969-92,172,145 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1367, CPSF100 |
| Gene groups (HGNC) | Cleavage and polyadenylation specific factor subunits; MBL fold containing DNA/RNA interacting subfamily |
| Reactome | 13 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2I0](https://www.uniprot.org/uniprotkb/Q9P2I0) (Cleavage and polyadenylation specificity factor subunit 2):

> Component of the cleavage and polyadenylation specificity factor (CPSF) complex that play a key role in pre-mRNA 3'-end formation, recognizing the AAUAAA signal sequence and interacting with poly(A) polymerase and other factors to bring about cleavage and poly(A) addition. Involved in the histone 3' end pre-mRNA processing.

**Summary**, from NCBI Gene [53981](https://www.ncbi.nlm.nih.gov/gene/53981):

> Predicted to enable RNA binding activity. Involved in mRNA 3'-end processing by stem-loop binding activity and cleavage. Located in membrane. Part of mRNA cleavage and polyadenylation specificity factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2325) · Entrez [53981](https://www.ncbi.nlm.nih.gov/gene/53981) · UniProt [Q9P2I0](https://www.uniprot.org/uniprotkb/Q9P2I0) · Ensembl [ENSG00000165934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165934)

## Data

Gene col 9211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9211); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9211]; `tensor/DDL_lfc|DDL_z.npy` [9211]; `embed/gene_vectors.npy` [9211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9211 or target_col == 9211). Every well: [[CPSF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPSF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
