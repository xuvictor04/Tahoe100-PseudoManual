---
symbol: "PIK3C2A"
type: "gene"
col: 238
ensembl_id: "ENSG00000011405"
name: "phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha"
location: "11p15.1"
module: 40
arm: "+"
pooled_cpm: 257.9
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# PIK3C2A

*phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +11.4, q 4e-27, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.575× (z -9.4, q 3e-18, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.674× (z -7.0, q 4e-10, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6A]] (+0.83, fdr 7e-06), [[SRP54-AS1]] (+0.77, fdr 7e-06), [[P4HA1]] (+0.74, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.68, fdr 7e-06), [[CHTOP]] (-0.67, fdr 7e-06), [[COA7]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM83H]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +11.4 | 4e-27 | 39/49 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +9.0 | 1e-16 | 39/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.6 | 2e-15 | 41/50 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.6 | 5e-12 | 41/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +6.1 | 1e-07 | 34/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.0 | 2e-07 | 32/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 33/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.7 | 7e-07 | 32/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.6 | 2e-06 | 37/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 2e-06 | 31/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +5.1 | 2e-05 | 33/48 (SW480, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +4.9 | 4e-05 | 32/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 2e-04 | 36/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.8 | 0.006 | 25/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.014 | 30/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.022 | 26/48 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.040 | 25/49 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.048 | 21/49 (PANC-1, BT-474, …) | rises with dose | plate-row cell shift |
| [[Berbamine (drug)]] 5 µM |  | 1.13× | +2.9 | 0.093 | 6/49 (NCI-H23, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -9.4 | 3e-18 | 38/45 (C32, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.679×** | -7.1 | 4e-10 | 36/49 (SK-MEL-2, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -7.0 | 4e-10 | 40/47 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.674×** | -7.0 | 4e-10 | 41/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -6.5 | 7e-09 | 33/44 (C-33 A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.770×** | -4.8 | 2e-04 | 31/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.779×** | -4.6 | 4e-04 | 29/48 (H4, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.787×** | -4.4 | 8e-04 | 33/48 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.794×** | -4.2 | 0.001 | 31/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.790×** | -4.2 | 0.002 | 34/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -4.0 | 0.004 | 25/48 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.813×** | -3.8 | 0.007 | 27/49 (SW48, A498, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.820×** | -3.6 | 0.012 | 25/48 (A498, H4, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.826×** | -3.5 | 0.019 | 27/49 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.835× | -3.3 | 0.035 | 24/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.840× | -3.2 | 0.051 | 23/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.063 | 19/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.847× | -3.0 | 0.073 | 18/49 (A-172, A498, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.083 | 16/49 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.852× | -2.9 | 0.093 | 16/47 (NCI-H460, HOP62, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.853× | -2.9 | 0.093 | 18/48 (A-172, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 328 | 2 | 5 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 327 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.566× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 313 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 209 | 6 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 348 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.470× (z -11.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 289 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 303 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.432× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 202 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 170 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 303 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 225 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 255 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -10.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 169 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 296 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 256 | 2 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -9.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 225 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 342 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.526× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 296 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -13.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 285 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 454 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.483× (z -8.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 217 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -11.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 214 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 258 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 349 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -9.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 134 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 216 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 218 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.7) | — |
| [[A-427 (line)]] | wt | 228 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 260 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 175 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.8) | — |
| [[J82 (line)]] | alt | 347 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 145 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 111 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.9) | — |
| [[SW48 (line)]] | wt | 259 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[A549 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 320 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 396 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 466 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 292 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 223 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.77 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.69 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MAX]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TMEM50B]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GPR155]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[COPA]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[RARS2]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.68 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[CHTOP]] | -0.67 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[COA7]] | -0.67 | -0.69 / -0.58 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | -0.67 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[RTL6]] | -0.65 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.64 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[CSTF2T]] | -0.64 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[DDX20]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[PUF60]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[CENPBD1P]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[VEZF1]] | -0.62 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ZNF502]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83H]] | B | FAM83H activity raises PIK3C2A's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without FAM83H | 0.079 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN |
| [[TOP2A]] | B | TOP2A activity lowers PIK3C2A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (4.7, -18.9); signed map (-43.0, 13.9). **Vector** length 133, 52.3% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +7.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.7 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -10.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -10.6 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.7 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.5 | -7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.6 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:17,077,730-17,207,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PI3K-C2alpha |
| Gene groups (HGNC) | Phosphatidylinositol 3-kinase family |
| Reactome | 12 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the Golgi membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O00443](https://www.uniprot.org/uniprotkb/O00443) (Phosphatidylinositol 4-phosphate 3-kinase C2 domain-containing subunit alpha):

> Generates phosphatidylinositol 3-phosphate (PtdIns3P) and phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4)P2) that act as second messengers. Has a role in several intracellular trafficking events. Functions in insulin signaling and secretion. Required for translocation of the glucose transporter SLC2A4/GLUT4 to the plasma membrane and glucose uptake in response to insulin-mediated RHOQ activation. Regulates insulin secretion through two different mechanisms: involved in glucose-induced …

**Summary**, from NCBI Gene [5286](https://www.ncbi.nlm.nih.gov/gene/5286):

> The protein encoded by this gene belongs to the phosphoinositide 3-kinase (PI3K) family. PI3-kinases play roles in signaling pathways involved in cell proliferation, oncogenic transformation, cell survival, cell migration, and intracellular protein trafficking. This protein contains a lipid kinase catalytic domain as well as a C-terminal C2 domain, a characteristic of class II PI3-kinases. C2 domains act as calcium-dependent phospholipid binding motifs that mediate translocation of proteins to …

**Accessions** — [HGNC:8971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8971) · Entrez [5286](https://www.ncbi.nlm.nih.gov/gene/5286) · UniProt [O00443](https://www.uniprot.org/uniprotkb/O00443) · Ensembl [ENSG00000011405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011405)

## Data

Gene col 238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 238); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 238]; `tensor/DDL_lfc|DDL_z.npy` [238]; `embed/gene_vectors.npy` [238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 238 or target_col == 238). Every well: [[PIK3C2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3C2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
