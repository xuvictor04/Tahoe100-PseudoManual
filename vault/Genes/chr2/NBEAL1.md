---
symbol: "NBEAL1"
type: "gene"
col: 6878
ensembl_id: "ENSG00000144426"
name: "neurobeachin like 1"
location: "2q33.2"
module: 5
arm: "-"
pooled_cpm: 261.24
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NBEAL1

*neurobeachin like 1* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.37× (z +7.9, q 2e-12, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -21.3, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPAG9]] (+0.69, fdr 1e-05), [[ARHGEF10]] (+0.61, fdr 2e-05), [[PPARA]] (+0.61, fdr 1e-05); moves opposite to [[KLHL42]] (-0.66, fdr 3e-05), [[PATZ1]] (-0.64, fdr 1e-05), [[ZNF362]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6878.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +7.9 | 2e-12 | 32/48 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +7.4 | 3e-11 | 33/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +6.7 | 3e-09 | 30/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 2e-07 | 25/47 (LS 180, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +5.9 | 4e-07 | 32/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.6 | 3e-04 | 25/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.3 | 0.001 | 20/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.001 | 28/49 (RKO, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 26/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.16× | +3.8 | 0.007 | 18/50 (A-427, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.016 | 9/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.020 | 18/50 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.030 | 21/48 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.062 | 15/49 (A-427, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.09× | +3.1 | 0.086 | 3/48 (MIA PaCa-2, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -21.3 | 0e+00 | 46/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -16.5 | 0e+00 | 47/49 (NCI-H1573, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.537×** | -15.0 | 0e+00 | 42/47 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -14.7 | 0e+00 | 40/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.548×** | -13.9 | 6e-42 | 37/45 (C32, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.591×** | -13.2 | 1e-37 | 39/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.366×** | -13.2 | 1e-37 | 43/48 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.606×** | -12.5 | 3e-34 | 38/49 (H4, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.625×** | -11.3 | 6e-28 | 35/44 (H4, A-172, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.663×** | -10.3 | 5e-23 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -9.2 | 3e-18 | 33/48 (H4, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -8.8 | 5e-17 | 40/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.511×** | -8.8 | 7e-17 | 33/38 (C32, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -8.7 | 1e-16 | 39/50 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.714×** | -8.4 | 1e-15 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -8.3 | 4e-15 | 35/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.754×** | -6.8 | 4e-10 | 32/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -6.5 | 3e-09 | 32/48 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -6.3 | 6e-09 | 25/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -6.3 | 6e-09 | 33/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -5.5 | 8e-07 | 30/48 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -5.4 | 1e-06 | 27/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.695×** | -4.8 | 4e-05 | 30/49 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.835× | -4.2 | 6e-04 | 23/47 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 288 | 0 | 18 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -17.1) |
| [[H4 (line)]] | wt | 337 | 0 | 17 (13 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 323 | 1 | 13 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -14.5) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.224× (z -12.3) |
| [[SW480 (line)]] | alt | 242 | 0 | 14 (7 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.422× (z -16.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -15.1) |
| [[HOP62 (line)]] | alt | 325 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -14.5) |
| [[LS 180 (line)]] | wt | 229 | 0 | 13 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -20.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -17.4) |
| [[PANC-1 (line)]] | alt | 215 | 5 (2 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +12.9) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.85× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -18.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.378× (z -9.8) |
| [[A-172 (line)]] | wt | 350 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -20.1) |
| [[KATO III (line)]] | alt | 245 | 0 | 12 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -23.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -17.2) |
| [[C32 (line)]] | wt | 202 | 2 | 9 (5 ⚠) | [[Belinostat (drug)]] 5 µM 1.83× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 276 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -15.6) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 294 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -22.2) |
| [[RPMI-7951 (line)]] | alt | 337 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -15.9) |
| [[SNU-423 (line)]] | alt | 223 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 454 | 5 (3 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +24.4) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.49× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 346 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -17.0) |
| [[HS-578T (line)]] | alt | 236 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -17.4) |
| [[hTERT-HPNE (line)]] | wt | 414 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 354 | 2 (2 ⚠) | 7 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 4.56× (z +22.8) ⚠ cell-cycle shift, explains ~49% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -17.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.175× (z -14.3) |
| [[A549 (line)]] | wt | 268 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 294 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -14.4) |
| [[Hs 766T (line)]] | wt | 272 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -13.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.223× (z -11.6) |
| [[J82 (line)]] | alt | 254 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 190 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -15.9) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.261× (z -9.7) |
| [[SNU-1 (line)]] | wt | 262 | 6 (5 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.5) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.0) |
| [[HCT15 (line)]] | alt | 315 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -11.1) |
| [[HT-29 (line)]] | alt | 349 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -19.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -14.6) |
| [[SW 900 (line)]] | alt | 208 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -14.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -9.6) |
| [[A-427 (line)]] | wt | 242 | 3 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +10.2) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.65× (z +8.9) | [[PH-797804 (drug)]] 5 µM 0.237× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 182 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.5) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.03× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.347× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.495× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 249 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.389× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.242× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 350 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +16.6) ⚠ cell-cycle shift, explains ~82% of this change | [[TAK-901 (drug)]] 5 µM 0.202× (z -14.1) |
| [[RKO (line)]] | wt | 107 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.297× (z -12.9) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.220× (z -8.7) |
| [[A498 (line)]] | wt | 251 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 1.99× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -15.5) |
| [[BT-474 (line)]] | alt | 166 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.377× (z -10.9) |
| [[LoVo (line)]] | wt | 203 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.78× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 211 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.01× (z +9.1) ⚠ cell-cycle shift, explains ~49% of this change | [[Dinaciclib (drug)]] 5 µM 0.416× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 178 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -10.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 110 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 292 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.462× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 133 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.261× (z -11.7) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 297 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 269 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 280 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | +0.69 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF10]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[PPARA]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[RRAS]] | +0.59 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PTPRH]] | +0.59 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CCNI]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.58 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[DDAH2]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[CAST]] | +0.57 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[KMT2C]] | +0.57 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[GOLGA2]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL42]] | -0.66 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PATZ1]] | -0.64 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ZNF362]] | -0.63 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[SPRYD4]] | -0.62 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[TOR1A]] | -0.62 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[RMDN2]] | -0.61 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[SETMAR]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ANGEL2]] | -0.60 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SMAD1]] | -0.60 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[AKAP7]] | -0.59 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ZNF239]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | -0.58 | -0.52 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.9, 9.8); signed map (-19.1, 24.0). **Vector** length 131, 51.5% of its response variance represented; |z| ≥ 3 in 1,835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.0 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.7 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.0 | +5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.4 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.7 | -21.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -15.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.7 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.2 | -13.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.7 | -3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | neurobeachin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:203,014,608-203,226,378 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC164581; previously ALS2CR17, ALS2CR16 |
| Gene groups (HGNC) | WD repeat domain containing; BEACH domain containing ; Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q6ZS30](https://www.uniprot.org/uniprotkb/Q6ZS30) carries no function annotation.

**Summary**, from NCBI Gene [65065](https://www.ncbi.nlm.nih.gov/gene/65065):

> Predicted to be active in cytosol and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20681) · Entrez [65065](https://www.ncbi.nlm.nih.gov/gene/65065) · UniProt [Q6ZS30](https://www.uniprot.org/uniprotkb/Q6ZS30) · Ensembl [ENSG00000144426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144426)

## Data

Gene col 6878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6878); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6878]; `tensor/DDL_lfc|DDL_z.npy` [6878]; `embed/gene_vectors.npy` [6878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6878 or target_col == 6878). Every well: [[NBEAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBEAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
