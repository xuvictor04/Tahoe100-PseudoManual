---
symbol: "YPEL5"
type: "gene"
col: 4122
ensembl_id: "ENSG00000119801"
name: "yippee like 5"
location: "2p23.1"
module: 69
arm: "+"
pooled_cpm: 66.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# YPEL5

*yippee like 5* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +23.1, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.449× (z -16.1, q 0e+00, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.377× (z -10.2, q 2e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBP1]] (+0.76, fdr 7e-06), [[GABARAPL1]] (+0.74, fdr 7e-06), [[CREBRF]] (+0.71, fdr 1e-05); moves opposite to [[PDSS1]] (-0.74, fdr 7e-06), [[EIF2B3]] (-0.72, fdr 7e-06), [[SNRPD1]] (-0.70, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STEAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +23.1 | 0e+00 | 46/49 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +11.9 | 4e-30 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 6e-13 | 41/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +7.0 | 3e-10 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +7.0 | 3e-10 | 32/48 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +6.2 | 4e-08 | 29/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.6 | 1e-06 | 26/49 (SHP-77, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 1e-05 | 25/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 24/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.0 | 0.003 | 20/41 (SW480, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.0 | 0.004 | 23/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.004 | 18/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.22×** | +3.9 | 0.004 | 20/47 (SNU-1, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.005 | 21/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.14× | +3.8 | 0.005 | 10/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.010 | 17/50 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.019 | 18/47 (NCI-H2030, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.039 | 13/48 (A-427, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.042 | 7/50 (A-427, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.048 | 16/47 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.449×** | -16.1 | 0e+00 | 46/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.546×** | -12.1 | 2e-31 | 40/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.583×** | -10.8 | 6e-25 | 37/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.377×** | -10.2 | 2e-22 | 41/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.623×** | -9.5 | 2e-19 | 37/48 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.429×** | -8.9 | 6e-17 | 43/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.451×** | -8.3 | 6e-15 | 41/48 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.470×** | -7.9 | 2e-13 | 39/48 (SW1417, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.485×** | -7.6 | 2e-12 | 39/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.740×** | -6.0 | 9e-08 | 29/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.665×** | -5.8 | 3e-07 | 31/48 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.684×** | -5.4 | 3e-06 | 30/48 (HCT15, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.689×** | -5.3 | 4e-06 | 32/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.777×** | -5.0 | 2e-05 | 27/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -5.0 | 2e-05 | 19/48 (A498, SW 900, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.818×** | -3.8 | 0.005 | 25/48 (SNU-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.698×** | -3.8 | 0.005 | 21/47 (Hs 766T, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.009 | 17/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.851× | -3.2 | 0.036 | 11/48 (NCI-H460, H4, …) | inconsistent across doses | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.853× | -3.2 | 0.042 | 8/48 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.0 | 5 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -14.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.237× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 94.7 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -12.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW1417 (line)]] | alt | 77.9 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -14.1) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.238× (z -8.9) |
| [[A498 (line)]] | wt | 101 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.406× (z -10.3) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -14.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.166× (z -9.3) |
| [[SW480 (line)]] | alt | 51.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +17.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.335× (z -12.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 89.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +15.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -10.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 70.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.401× (z -9.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LoVo (line)]] | wt | 37.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -21.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 86.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.428× (z -9.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 93.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 52.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +19.8) | — |
| [[A-172 (line)]] | wt | 85.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.488× (z -8.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 72.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 42.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 81.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 70.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.412× (z -9.3) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 76.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.389× (z -9.1) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 55.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +17.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -10.6) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 69.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -17.6) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 41.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +13.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -8.6) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 63.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 45.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -10.5) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 96.8 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.440× (z -9.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW48 (line)]] | wt | 28.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -9.3) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.176× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 27.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +10.0) | — |
| [[C32 (line)]] | wt | 48.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 99.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0849× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 55.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 34.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 52.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.3) | — |
| [[J82 (line)]] | alt | 43.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +16.5) | — |
| [[LS 180 (line)]] | wt | 41.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 80.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 86.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBP1]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[GABARAPL1]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.71 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.70 | +0.54 / +0.80 | both halves | 1e-05 | STRING 437 |
| [[ATOSA]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[PCMTD1]] | +0.69 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[HECA]] | +0.69 | +0.58 / +0.77 | both halves | 7e-06 | STRING 469 |
| [[TMEM59]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[RB1CC1]] | +0.67 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[TCP11L2]] | +0.67 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[MKRN1]] | +0.65 | +0.56 / +0.76 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDSS1]] | -0.74 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[EIF2B3]] | -0.72 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[SNRPD1]] | -0.70 | -0.67 / -0.67 | both halves | 7e-06 |  |
| [[AGK]] | -0.69 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[MPHOSPH6]] | -0.67 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[RIOK1]] | -0.66 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.66 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[DDX55]] | -0.65 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[TMEM177]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[COA1]] | -0.63 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[NLE1]] | -0.63 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[METTL2A]] | -0.63 | -0.46 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1]] | B | STEAP1 activity raises YPEL5's level | lines that do not express STEAP1 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without STEAP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[ADRA1B]] | B | ADRA1B activity raises YPEL5's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without ADRA1B | 0.099 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.2, -44.0); signed map (-13.4, 10.9). **Vector** length 136, 42.6% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.4 | +23.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.0 | +11.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -13.7 | -16.1 |
|  | [[EX229 (drug)]] 5 µM |  | -9.1 | -8.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.0 | -10.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.8 | -7.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.8 | -8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.6 | -7.6 |

## What is on record

|  |  |
|---|---|
| Name | yippee like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:30,146,941-30,160,533 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-127 |
| Gene groups (HGNC) | Yippee like family; CTLH complex subunits |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P62699](https://www.uniprot.org/uniprotkb/P62699) (Protein yippee-like 5):

> Component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. Required for normal cell proliferation (By similarity).

**Summary**, from NCBI Gene [51646](https://www.ncbi.nlm.nih.gov/gene/51646):

> Predicted to enable metal ion binding activity. Predicted to be involved in cell population proliferation. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18329) · Entrez [51646](https://www.ncbi.nlm.nih.gov/gene/51646) · UniProt [P62699](https://www.uniprot.org/uniprotkb/P62699) · Ensembl [ENSG00000119801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119801)

## Data

Gene col 4122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4122); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4122]; `tensor/DDL_lfc|DDL_z.npy` [4122]; `embed/gene_vectors.npy` [4122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4122 or target_col == 4122). Every well: [[YPEL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YPEL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
