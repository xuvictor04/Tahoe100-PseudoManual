---
symbol: "WDPCP"
type: "gene"
col: 6826
ensembl_id: "ENSG00000143951"
name: "WD repeat containing planar cell polarity effector"
location: "2p15"
module: 22
arm: "+"
pooled_cpm: 173.79
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 39
n_dd_up_clean: 8
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# WDPCP

*WD repeat containing planar cell polarity effector* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.94× (z +15.4, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.455× (z -18.3, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.63, fdr 1e-05), [[CDCA2]] (+0.62, fdr 1e-05), [[KIAA1328]] (+0.62, fdr 1e-04); moves opposite to [[YOD1]] (-0.55, fdr 4e-05), [[DNAJA4]] (-0.54, fdr 4e-05), [[AIFM2]] (-0.54, fdr 9e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRKN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +15.4 | 0e+00 | 42/47 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +14.3 | 1e-43 | 41/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +11.4 | 5e-28 | 35/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +9.8 | 1e-20 | 41/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +7.7 | 1e-12 | 40/48 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +7.7 | 1e-12 | 24/47 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +6.3 | 2e-08 | 37/47 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +5.4 | 5e-06 | 29/48 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.0 | 0.003 | 14/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.17× | +3.8 | 0.009 | 17/48 (LoVo, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.012 | 14/47 (KATO III, A-172, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.13× | +3.7 | 0.012 | 4/48 (KATO III, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.012 | 17/46 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.6 | 0.012 | 19/46 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.6 | 0.012 | 16/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.017 | 17/48 (KATO III, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.455×** | -18.3 | 0e+00 | 46/47 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.449×** | -17.9 | 0e+00 | 36/43 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -16.4 | 0e+00 | 37/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -16.2 | 0e+00 | 43/46 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.555×** | -13.6 | 3e-40 | 44/47 (HCT15, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -12.6 | 2e-34 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.590×** | -12.2 | 2e-32 | 36/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.585×** | -11.5 | 1e-28 | 36/44 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -11.0 | 1e-26 | 40/46 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -10.6 | 1e-24 | 38/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.645×** | -10.2 | 2e-22 | 38/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.667×** | -9.4 | 4e-19 | 41/47 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -9.1 | 3e-18 | 36/47 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -8.7 | 1e-16 | 36/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.704×** | -8.1 | 2e-14 | 34/47 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -7.1 | 5e-11 | 28/47 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -7.0 | 8e-11 | 25/47 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.825×** | -6.2 | 1e-08 | 26/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.790×** | -5.4 | 1e-06 | 29/46 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.790×** | -5.2 | 4e-06 | 30/46 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.799×** | -5.2 | 5e-06 | 28/47 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **0.803×** | -5.1 | 9e-06 | 27/47 (SW48, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 331 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.332× (z -15.7) |
| [[HOP62 (line)]] | alt | 254 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -10.8) |
| [[PANC-1 (line)]] | alt | 188 | 2 | 11 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.418× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.433× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 165 | 0 | 12 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.317× (z -13.2) |
| [[C32 (line)]] | wt | 385 | 1 | 10 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 4.20× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 133 | 8 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 2 (1 ⚠) | 9 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.348× (z -12.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 131 | 3 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.346× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.355× (z -13.0) |
| [[SW480 (line)]] | alt | 169 | 1 | 10 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.300× (z -17.5) |
| [[SW 900 (line)]] | alt | 176 | 2 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.372× (z -11.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -10.9) |
| [[A-427 (line)]] | wt | 354 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -17.2) |
| [[A498 (line)]] | wt | 167 | 2 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.409× (z -12.5) |
| [[HT-29 (line)]] | alt | 108 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.27× (z +13.9) | [[Auranofin (drug)]] 5 µM 0.311× (z -13.6) |
| [[J82 (line)]] | alt | 127 | 1 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -13.4) |
| [[KATO III (line)]] | alt | 123 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +13.3) | [[Auranofin (drug)]] 5 µM 0.319× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 198 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 378 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -8.8) |
| [[HCT15 (line)]] | alt | 246 | 0 | 7 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.257× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 183 | 3 | 4 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.44× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.547× (z -8.8) |
| [[SNU-423 (line)]] | alt | 123 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.430× (z -10.9) |
| [[A-172 (line)]] | wt | 158 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.434× (z -9.6) |
| [[C-33 A (line)]] | alt | 293 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.386× (z -10.9) |
| [[HS-578T (line)]] | alt | 226 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.456× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 179 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.314× (z -12.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.435× (z -9.0) |
| [[LoVo (line)]] | wt | 78.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 180 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.457× (z -9.9) |
| [[RKO (line)]] | wt | 102 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.5) | [[Digitoxin (drug)]] 5 µM 0.344× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.397× (z -9.4) |
| [[COLO 205 (line)]] | alt | 109 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -15.7) |
| [[LS 180 (line)]] | wt | 90.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.332× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 446 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0543× (z -45.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 91.2 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.362× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 322 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -16.4) |
| [[A549 (line)]] | wt | 197 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 279 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 117 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 129 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.1) | [[Auranofin (drug)]] 5 µM 0.436× (z -9.5) |
| [[AN3 CA (line)]] | alt | 205 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 52.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +14.0) | — |
| [[SNU-1 (line)]] | wt | 167 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.324× (z -15.4) |
| [[Hs 766T (line)]] | wt | 64.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 55.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 208 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -27.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.455× (z -10.2) |
| [[SW48 (line)]] | wt | 202 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -12.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 205 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 43.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 204 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CDCA2]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[KIAA1328]] | +0.62 | +0.34 / +0.52 | both halves | 1e-04 | STRING 783 |
| [[TOP2A]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[G2E3]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PSRC1]] | +0.61 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TTK]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[GPSM2]] | +0.60 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[DLGAP5]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SAPCD2]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CDKN3]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[GAS2L3]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YOD1]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DNAJA4]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[AIFM2]] | -0.54 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[POU6F1]] | -0.51 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[SEL1L3]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[FAM149A]] | -0.51 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[AHSA2P]] | -0.50 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[DVL3]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.50 | -0.29 / -0.28 | both halves | 3e-04 |  |
| [[PEA15]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[MICALL1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[C1orf54]] | -0.49 | -0.33 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKN]] | B | PRKN activity raises WDPCP's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.35× lower at baseline in the lines without PRKN | 0.011 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[PRKN]] | B | PRKN activity strengthens WDPCP's drug response | lines that do not express PRKN (7) vs lines expressing it (41) | the lines without PRKN respond 0.81× as strongly (z diff +1.63); strongest at Dinaciclib 0.05 µM: 0.88x vs 0.54x (z diff +4.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10; target measured in part of the lines; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers WDPCP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.0, -58.8); signed map (-51.1, -40.6). **Vector** length 120, 43.9% of its response variance represented; |z| ≥ 3 in 1,728 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.50 to 28); *Kinesins* (reactome, mean cos +0.53 to 10); *Phosphorylation of Emi1* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.2 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +15.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +11.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +7.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Berbamine (dihydrochloride) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.2 | -16.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -11.3 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.4 | -18.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.8 | -13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -4.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat containing planar cell polarity effector |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:63,119,559-63,827,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hFrtz, fritz, BBS15, CPLANE5; previously C2orf86 |
| Gene groups (HGNC) | Ciliogenesis and planar polarity effector complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O95876](https://www.uniprot.org/uniprotkb/O95876) (WD repeat-containing and planar cell polarity effector protein fritz homolog):

> Probable effector of the planar cell polarity signaling pathway which regulates the septin cytoskeleton in both ciliogenesis and collective cell movements. Together with FUZ and WDPCP proposed to function as core component of the CPLANE (ciliogenesis and planar polarity effectors) complex involved in the recruitment of peripheral IFT-A proteins to basal bodies (By similarity). Binds phosphatidylinositol 3-phosphate with highest affinity, followed by phosphatidylinositol 4-phosphate and …

**Summary**, from NCBI Gene [51057](https://www.ncbi.nlm.nih.gov/gene/51057):

> This gene encodes a cytoplasmic WD40 repeat protein. A similar gene in frogs encodes a planar cell polarity protein that plays a critical role in collective cell movement and ciliogenesis by mediating septin localization. Mutations in this gene are associated with Bardet-Biedl syndrome 15 and may also play a role in Meckel-Gruber syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:28027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28027) · Entrez [51057](https://www.ncbi.nlm.nih.gov/gene/51057) · UniProt [O95876](https://www.uniprot.org/uniprotkb/O95876) · Ensembl [ENSG00000143951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143951)

## Data

Gene col 6826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6826); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6826]; `tensor/DDL_lfc|DDL_z.npy` [6826]; `embed/gene_vectors.npy` [6826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6826 or target_col == 6826). Every well: [[WDPCP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDPCP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
