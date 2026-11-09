---
symbol: "DST"
type: "gene"
col: 7579
ensembl_id: "ENSG00000151914"
name: "dystonin"
location: "6p12.1"
module: 16
arm: "+"
pooled_cpm: 799.96
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DST

*dystonin* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.58× (z +7.8, q 4e-12, up in 30 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[RMC-6236 (drug)]] 5 µM: 1.85× (z +5.7, q 2e-06, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.615× (z -12.2, q 1e-31, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIO]] (+0.71, fdr 7e-06), [[SHTN1]] (+0.69, fdr 7e-06), [[DYNC1H1]] (+0.64, fdr 1e-05); moves opposite to [[TAF5]] (-0.63, fdr 1e-05), [[MGAT1]] (-0.61, fdr 1e-05), [[CRLS1]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.8 | 4e-12 | 30/42 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.0 | 4e-07 | 29/47 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.85×** | +5.7 | 2e-06 | 35/46 (AsPC-1, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 2e-05 | 31/45 (AsPC-1, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +5.2 | 2e-05 | 32/45 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +4.7 | 2e-04 | 31/45 (COLO 205, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 2e-04 | 32/46 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.6 | 3e-04 | 29/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +4.5 | 5e-04 | 30/45 (COLO 205, BT-474, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +4.4 | 7e-04 | 31/46 (COLO 205, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.3 | 7e-04 | 24/43 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.3 | 9e-04 | 21/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.002 | 30/48 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +4.0 | 0.002 | 28/46 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 24/46 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 27/46 (KATO III, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.006 | 27/45 (MIA PaCa-2, LoVo, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.012 | 23/46 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.015 | 23/46 (AsPC-1, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.4 | 0.017 | 17/46 (BT-474, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.017 | 22/47 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.017 | 16/46 (AsPC-1, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -12.2 | 1e-31 | 36/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -11.0 | 1e-25 | 41/45 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.558×** | -10.4 | 6e-23 | 42/46 (SW480, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.623×** | -8.4 | 6e-15 | 38/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.640×** | -7.9 | 2e-13 | 36/46 (SW480, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.697×** | -6.4 | 1e-08 | 36/46 (SW480, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.710×** | -6.1 | 9e-08 | 41/46 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.682×** | -4.9 | 8e-05 | 37/46 (hTERT-HPNE, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.785×** | -4.1 | 0.002 | 29/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.794×** | -4.1 | 0.002 | 26/46 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.793×** | -4.0 | 0.004 | 26/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.807×** | -3.8 | 0.007 | 23/46 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.810×** | -3.7 | 0.008 | 25/46 (BT-474, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.010 | 25/46 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.818×** | -3.6 | 0.014 | 23/46 (BT-474, A-427, …) | all doses, stronger at high dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.028 | 28/46 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.835× | -3.2 | 0.047 | 22/46 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.047 | 23/45 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.886× | -3.0 | 0.073 | 14/46 (SK-MEL-2, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 484 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 5.22× (z +16.1) | — |
| [[BT-474 (line)]] | alt | 271 | 7 (2 ⚠) | 5 (4 ⚠) | [[Peretinoin (drug)]] 5 µM 2.91× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.359× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.3) |
| [[HT-29 (line)]] | alt | 632 | 7 (3 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +24.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.88× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.345× (z -13.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.2) |
| [[LoVo (line)]] | wt | 377 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +14.6) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.94× (z +14.5) | — |
| [[RKO (line)]] | wt | 396 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.2) |
| [[KATO III (line)]] | alt | 306 | 6 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.54× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.429× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 213 | 7 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 470 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +16.3) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 2.03× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.474× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 482 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.73× (z +8.7) | — |
| [[SW480 (line)]] | alt | 778 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -19.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -15.9) |
| [[A-427 (line)]] | wt | 1,432 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.425× (z -12.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 403 | 6 (2 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 2.38× (z +10.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.98× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 2,401 | 1 (1 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +10.1) ⚠ cell-cycle shift, explains ~44% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -24.8) |
| [[A-172 (line)]] | wt | 1,220 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -12.2) |
| [[A498 (line)]] | wt | 464 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.90× (z +8.6) | — |
| [[C32 (line)]] | wt | 1,022 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.4) |
| [[J82 (line)]] | alt | 1,011 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 1,238 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -15.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 872 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -17.6) |
| [[PANC-1 (line)]] | alt | 1,246 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 1,072 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -19.0) |
| [[SW48 (line)]] | wt | 419 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -8.7) |
| [[A549 (line)]] | wt | 545 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +9.2) ⚠ cell-cycle shift, explains ~14% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -14.2) |
| [[C-33 A (line)]] | alt | 975 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.442× (z -11.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 1,043 | 1 (1 ⚠) | 2 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 2.45× (z +9.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 1,388 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 624 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +12.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 1,050 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -11.0) |
| [[HCT15 (line)]] | alt | 299 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 486 | 0 | 2 | — | [[Dexamethasone (drug)]] 5 µM 0.436× (z -9.2) |
| [[SNU-423 (line)]] | alt | 1,487 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.6) |
| [[SW 1271 (line)]] | alt | 975 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.4) |
| [[H4 (line)]] | wt | 1,306 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -9.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 1,159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 880 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 602 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -8.6) |
| [[SHP-77 (line)]] | alt | 536 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.537× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 251 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 769 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.2) |
| [[SW1417 (line)]] | alt | 262 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.69× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 276 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1,041 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 139 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 725 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1,132 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 111 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 608 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 751 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1,383 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 517 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIO]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MITOTIC_SPINDLE |
| [[SHTN1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[DYNC1H1]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 549 |
| [[HSPB8]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SYNE1]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PALLD]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ZNF518B]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MPDZ]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HUWE1]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PTPN11]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | pathway: Cell-Cell communication |
| [[PRECSIT]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SYTL2]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5]] | -0.63 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[MGAT1]] | -0.61 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[CRLS1]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ANKRD13D]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[MHENCR]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[SDF2]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SMYD4]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ELP2]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[KHDC4]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1B]] | B | MAP1B activity raises DST's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without MAP1B | 0.007 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[DSEL]] | B | DSEL activity raises DST's level | lines that do not express DSEL (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without DSEL | 0.026 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: HDX, GLRB, AFAP1L1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers DST's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises DST's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TPM1]] | C | TPM1 activity lowers DST's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 2.80× higher at baseline in the lines without TPM1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.7, -1.8); signed map (11.9, -10.5). **Vector** length 157, 56.9% of its response variance represented; |z| ≥ 3 in 1,754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +11.0 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.7 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.8 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.8 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -11.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.3 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.1 | -7.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.0 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -12.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.8 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.3 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dystonin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:56,457,987-56,954,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BP240, KIAA0728, FLJ21489, FLJ13425, FLJ32235, FLJ30627, CATX-15, BPA; previously BPAG1 |
| Gene groups (HGNC) | EF-hand domain containing; Plakins; Spectrin repeat containing; SH3 domain containing |
| Hallmark sets | PROTEIN_SECRETION, EPITHELIAL_MESENCHYMAL_TRANSITION, MITOTIC_SPINDLE |
| Reactome | 14 pathways, smallest: Type I hemidesmosome assembly; RHOV GTPase cycle; RHOU GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03001](https://www.uniprot.org/uniprotkb/Q03001) (Dystonin):

> Cytoskeletal linker protein. Acts as an integrator of intermediate filaments, actin and microtubule cytoskeleton networks. Required for anchoring either intermediate filaments to the actin cytoskeleton in neural and muscle cells or keratin-containing intermediate filaments to hemidesmosomes in epithelial cells. The proteins may self-aggregate to form filaments or a two-dimensional mesh. Regulates the organization and stability of the microtubule network of sensory neurons to allow axonal …

**Summary**, from NCBI Gene [667](https://www.ncbi.nlm.nih.gov/gene/667):

> This gene encodes a member of the plakin protein family of adhesion junction plaque proteins. Multiple alternatively spliced transcript variants encoding distinct isoforms have been found for this gene, but the full-length nature of some variants has not been defined. It has been reported that some isoforms are expressed in neural and muscle tissue, anchoring neural intermediate filaments to the actin cytoskeleton, and some isoforms are expressed in epithelial tissue, anchoring …

**Accessions** — [HGNC:1090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1090) · Entrez [667](https://www.ncbi.nlm.nih.gov/gene/667) · UniProt [Q03001](https://www.uniprot.org/uniprotkb/Q03001) · Ensembl [ENSG00000151914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151914)

## Data

Gene col 7579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7579); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7579]; `tensor/DDL_lfc|DDL_z.npy` [7579]; `embed/gene_vectors.npy` [7579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7579 or target_col == 7579). Every well: [[DST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
