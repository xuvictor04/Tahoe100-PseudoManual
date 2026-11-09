---
symbol: "ADAM17"
type: "gene"
col: 7554
ensembl_id: "ENSG00000151694"
name: "ADAM metallopeptidase domain 17"
location: "2p25.1"
module: 42
arm: "+"
pooled_cpm: 248.49
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# ADAM17

*ADAM metallopeptidase domain 17* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.58× (z +10.7, q 1e-23, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.506× (z -10.9, q 8e-25, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.736× (z -4.9, q 9e-05, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM41B]] (+0.72, fdr 7e-06), [[HSPA5]] (+0.68, fdr 1e-05), [[CSNK2A1]] (+0.64, fdr 2e-05); moves opposite to [[ZNF280D]] (-0.60, fdr 1e-05), [[LATS1]] (-0.60, fdr 1e-05), [[AASDHPPT]] (-0.58, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.58×** | +10.7 | 1e-23 | 48/49 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +10.3 | 2e-22 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +9.0 | 4e-17 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.91×** | +8.9 | 7e-17 | 46/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +7.9 | 2e-13 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +6.9 | 6e-10 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.8 | 7e-10 | 40/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +6.6 | 2e-09 | 40/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.6 | 2e-06 | 34/47 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.3 | 5e-06 | 37/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 8e-04 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +4.2 | 0.001 | 22/48 (SNU-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.9 | 0.004 | 27/45 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.004 | 33/49 (LoVo, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.007 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.008 | 24/48 (A-172, HOP62, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.009 | 36/48 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.018 | 17/49 (KATO III, COLO 205, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.018 | 24/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.506×** | -10.9 | 8e-25 | 42/49 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -8.4 | 1e-14 | 38/44 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -7.0 | 7e-10 | 40/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.652×** | -6.3 | 3e-08 | 37/45 (SHP-77, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.792×** | -5.3 | 1e-05 | 27/49 (A549, NCI-H1792, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.736×** | -4.9 | 9e-05 | 41/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -4.6 | 4e-04 | 29/48 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.825×** | -4.4 | 9e-04 | 25/48 (A-427, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.2 | 0.002 | 25/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.834× | -4.1 | 0.002 | 25/48 (Panc 03.27, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -4.1 | 0.002 | 27/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.781×** | -3.9 | 0.004 | 31/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.792×** | -3.7 | 0.009 | 26/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.800×** | -3.6 | 0.014 | 25/48 (SW 1088, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.819×** | -3.2 | 0.055 | 23/48 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.068 | 25/47 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.825×** | -3.1 | 0.069 | 22/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 226 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.96× (z +21.1) | — |
| [[BT-474 (line)]] | alt | 216 | 8 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.22× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 121 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +14.9) | — |
| [[SW480 (line)]] | alt | 214 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -12.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 472 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.220× (z -15.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 298 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 223 | 1 | 5 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.39× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.425× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 271 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.65× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 325 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.73× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 176 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 180 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 340 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 156 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 244 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 307 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 291 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.38× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 457 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -19.8) ⚠ cell-cycle shift, explains ~14% of this change |
| [[COLO 205 (line)]] | alt | 188 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.44× (z +12.9) | — |
| [[RKO (line)]] | wt | 265 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SHP-77 (line)]] | alt | 302 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.39× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 191 | 2 (1 ⚠) | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.53× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 392 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +18.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -14.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HOP62 (line)]] | alt | 251 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 276 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.24× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[Panc 03.27 (line)]] | alt | 192 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.65× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 323 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 191 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.466× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 83.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 215 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -8.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.22× (z +10.6) ⚠ toxic | — |
| [[HEC-1-A (line)]] | alt | 126 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.19× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 174 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 183 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 363 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 285 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 231 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 327 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 170 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 184 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM41B]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.64 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[HERPUD1]] | +0.60 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[SESN2]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PLD3]] | +0.59 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[ULK1]] | +0.58 | +0.62 / +0.42 | both halves | 4e-05 | pathway: Death Receptor Signaling |
| [[SEC11A]] | +0.57 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[IGSF8]] | +0.57 | +0.54 / +0.44 | both halves | 3e-05 | same gene group; STRING 449 |
| [[DPM1]] | +0.57 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[CORO7]] | +0.57 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[GARS1]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF280D]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[LATS1]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TXNRD2]] | -0.56 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ZC3H7B]] | -0.56 | -0.61 / -0.37 | both halves | 9e-05 |  |
| [[TRMT5]] | -0.56 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[NSD1]] | -0.56 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[ZNF507]] | -0.55 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[ST7L]] | -0.54 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[ZBTB33]] | -0.53 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[UBQLN2]] | -0.53 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[NOL11]] | -0.53 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.435). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, -30.4); signed map (-43.3, 7.7). **Vector** length 97.0, 37.8% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -0.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,488,486-9,556,732 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cSVP, CD156B; previously TACE |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing; CD molecules |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, KRAS_SIGNALING_UP |
| Reactome | 34 pathways, smallest: Release of Hh-Np from the secreting cell; Constitutive Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant |
| Matched by | ensembl_id |

**Function**, from UniProt [P78536](https://www.uniprot.org/uniprotkb/P78536) (Disintegrin and metalloproteinase domain-containing protein 17):

> Transmembrane metalloprotease which mediates the ectodomain shedding of a myriad of transmembrane proteins including adhesion proteins, growth factor precursors and cytokines important for inflammation and immunity. Cleaves the membrane-bound precursor of TNF to its mature soluble form. Responsible for the proteolytical release of soluble JAM3 from endothelial cells surface. Responsible for the proteolytic release of several other cell-surface proteins, including p75 TNF-receptor, interleukin 1 …

**Summary**, from NCBI Gene [6868](https://www.ncbi.nlm.nih.gov/gene/6868):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biologic processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The encoded preproprotein is proteolytically processed to generate the mature protease. The encoded protease functions in the …

**Accessions** — [HGNC:195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:195) · Entrez [6868](https://www.ncbi.nlm.nih.gov/gene/6868) · UniProt [P78536](https://www.uniprot.org/uniprotkb/P78536) · Ensembl [ENSG00000151694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151694)

## Data

Gene col 7554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7554); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7554]; `tensor/DDL_lfc|DDL_z.npy` [7554]; `embed/gene_vectors.npy` [7554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7554 or target_col == 7554). Every well: [[ADAM17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
