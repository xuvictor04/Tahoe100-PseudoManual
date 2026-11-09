---
symbol: "VDR"
type: "gene"
col: 3232
ensembl_id: "ENSG00000111424"
name: "vitamin D receptor"
location: "12q13.11"
module: 162
arm: "+"
pooled_cpm: 22.73
n_lines_expressing: 42
n_dd_up: 37
n_dd_down: 21
n_dd_up_clean: 20
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 17
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# VDR

*vitamin D receptor* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.24× (z +34.9, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.760× (z -6.6, q 3e-08, down in 22 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP3]] (+0.66, fdr 8e-06), [[CD82]] (+0.65, fdr 1e-05), [[NFKBIE]] (+0.63, fdr 7e-06); moves opposite to [[GPN1]] (-0.52, fdr 2e-05), [[UBQLN1]] (-0.51, fdr 3e-05), [[BABAM1]] (-0.50, fdr 1e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CD82]] → it (grade B ⚠); 17 go from it, the strongest it → [[SHB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.24×** | +34.9 | 0e+00 | 37/40 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +28.3 | 0e+00 | 35/39 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.79×** | +22.7 | 0e+00 | 38/40 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.45×** | +21.1 | 0e+00 | 36/39 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.26×** | +20.2 | 0e+00 | 36/39 (SW1417, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.24×** | +19.3 | 0e+00 | 35/39 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +14.7 | 0e+00 | 32/40 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +12.3 | 5e-33 | 35/40 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +10.5 | 5e-24 | 27/39 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +10.3 | 4e-23 | 28/40 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.78×** | +9.5 | 1e-19 | 23/38 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.71×** | +9.1 | 3e-18 | 25/39 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +8.6 | 4e-16 | 26/40 (BT-474, KATO III, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +6.6 | 2e-09 | 24/39 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.44×** | +6.0 | 9e-08 | 19/39 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 2e-05 | 17/39 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +4.7 | 9e-05 | 9/40 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.001 | 8/38 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.002 | 11/40 (NCI-H460, J82, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.008 | 8/40 (SW1417, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.014 | 4/39 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.016 | 5/40 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.019 | 8/39 (SW1417, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.760×** | -6.6 | 3e-08 | 22/40 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.695×** | -6.2 | 2e-07 | 17/39 (LS 180, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -5.3 | 3e-05 | 20/40 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -4.7 | 3e-04 | 17/39 (LS 180, A498, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.756×** | -4.4 | 0.001 | 13/39 (SK-MEL-2, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.768×** | -4.3 | 0.002 | 15/39 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.760×** | -4.1 | 0.004 | 15/40 (SK-MEL-2, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.782×** | -4.0 | 0.004 | 14/39 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.846× | -4.0 | 0.004 | 13/40 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.783×** | -4.0 | 0.004 | 13/39 (J82, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.850× | -3.9 | 0.005 | 19/40 (SK-MEL-2, J82, …) | top dose only | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.006 | 13/39 (LS 180, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.798×** | -3.8 | 0.006 | 15/39 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.736×** | -3.7 | 0.008 | 11/38 (Panc 03.27, SW48, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.805×** | -3.7 | 0.009 | 10/39 (LS 180, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.010 | 17/39 (LS 180, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.578×** | -3.6 | 0.010 | 12/37 (HCT15, J82, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.010 | 14/39 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.010 | 16/40 (RPMI-7951, LS 180, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.814×** | -3.5 | 0.014 | 17/39 (LS 180, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 156 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.202× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 10.9 | 9 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +22.6) | — |
| [[A498 (line)]] | wt | 39.8 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +16.3) | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0662× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 20.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +16.3) | — |
| [[SW1417 (line)]] | alt | 41.5 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 27.2 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +20.9) | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 28.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +17.7) | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.325× (z -9.4) |
| [[SW480 (line)]] | alt | 24.3 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +14.6) | — |
| [[BT-474 (line)]] | alt | 73.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +22.3) | — |
| [[HS-578T (line)]] | alt | 8.57 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +19.4) | — |
| [[KATO III (line)]] | alt | 56.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +20.7) | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +13.5) | — |
| [[C32 (line)]] | wt | 23.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +14.4) | — |
| [[J82 (line)]] | alt | 19.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.1) | [[Cobimetinib (drug)]] 5 µM 0.170× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 18.4 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 6.07× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 6.56 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 7.91 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.72× (z +10.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 8.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 37.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.2) | [[Bortezomib (drug)]] 0.05 µM 0.242× (z -9.6) |
| [[SNU-423 (line)]] | alt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +16.0) | — |
| [[A549 (line)]] | wt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 5 µM 0.272× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 7.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +9.6) | — |
| [[A-172 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP3]] | +0.66 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[CD82]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[NFKBIE]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[IRAK2]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[EGR2]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PER2]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ADGRE5]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TNFRSF1B]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TLE3]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EGR3]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP26]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ECE1]] | +0.53 | +0.37 / +0.57 | both halves | 7e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN1]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[UBQLN1]] | -0.51 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[BABAM1]] | -0.50 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[GTF3C3]] | -0.49 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ANAPC10]] | -0.49 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[VTI1B]] | -0.48 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[VTI1A]] | -0.48 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TSN]] | -0.48 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[HMBOX1]] | -0.47 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[GFM2]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[VPS50]] | -0.47 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[GLB1]] | -0.47 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD82]] | B | CD82 activity raises VDR's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without CD82 | 0.020 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[ITGA1]] | B | ITGA1 activity raises VDR's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without ITGA1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[SERTAD4]] | B | SERTAD4 activity raises VDR's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without SERTAD4 | 0.037 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[SOX9]] | B | SOX9 activity raises VDR's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without SOX9 | 0.046 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[ARHGAP26]] | B | ARHGAP26 activity raises VDR's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[IER3]] | B | IER3 activity raises VDR's level | lines that do not express IER3 (5) vs lines expressing it (45) | 4.07× lower at baseline in the lines without IER3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[IL1A]] | B | IL1A activity raises VDR's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without IL1A | 0.097 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[LONRF3]] | C | LONRF3 activity raises VDR's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 3.38× lower at baseline in the lines without LONRF3 | 0.016 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64; co-absent with the target |
| [[SMOX]] | C | SMOX activity raises VDR's level | lines that do not express SMOX (6) vs lines expressing it (44) | 4.37× lower at baseline in the lines without SMOX | 0.019 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHB]] | B | VDR activity raises SHB's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without VDR | 0.005 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[IER3]] | B | VDR activity raises IER3's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.64× lower at baseline in the lines without VDR | 0.016 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[IL7]] | B | VDR activity raises IL7's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.83× lower at baseline in the lines without VDR | 0.017 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[PMEPA1]] | B | VDR activity raises PMEPA1's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without VDR | 0.024 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[CD82]] | B | VDR activity raises CD82's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without VDR | 0.055 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[DUSP5]] | B | VDR activity raises DUSP5's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.12× lower at baseline in the lines without VDR | 0.067 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[ICAM1]] | B | VDR activity raises ICAM1's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.89× lower at baseline in the lines without VDR | 0.081 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[BCL3]] | B | VDR activity raises BCL3's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.00× lower at baseline in the lines without VDR | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[MMD]] | B | VDR activity raises MMD's level | lines that do not express VDR (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without VDR | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[IL1A]] | B | VDR activity raises IL1A's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without VDR | 0.090 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | VDR activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express VDR (8) vs lines expressing it (40) | the lines without VDR: 0.74× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| cells under [[vincristine (drug)]] 0.5 µM | B | VDR activity lowers the cells' numbers under vincristine 0.5 µM (makes them more sensitive) | lines that do not express VDR (8) vs lines expressing it (40) | the lines without VDR: 1.34× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.7, 0.5); signed map (0.9, 43.2). **Vector** length 93.4, 21.8% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +34.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +19.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +28.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | vitamin D receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:47,841,537-47,943,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NR1I1, PPP1R163 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Nuclear receptor subfamily 1 group I |
| Hallmark sets | PANCREAS_BETA_CELLS, P53_PATHWAY |
| Reactome | 7 pathways, smallest: Vitamin D (calciferol) metabolism; SUMOylation of intracellular receptors; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P11473](https://www.uniprot.org/uniprotkb/P11473) (Vitamin D3 receptor):

> Nuclear receptor for calcitriol, the active form of vitamin D3 which mediates the action of this vitamin on cells. Enters the nucleus upon vitamin D3 binding where it forms heterodimers with the retinoid X receptor/RXR. The VDR-RXR heterodimers bind to specific response elements on DNA and activate the transcription of vitamin D3-responsive target genes. Plays a central role in calcium homeostasis (By similarity). Also functions as a receptor for the secondary bile acid lithocholic acid (LCA) …

**Summary**, from NCBI Gene [7421](https://www.ncbi.nlm.nih.gov/gene/7421):

> This gene encodes vitamin D3 receptor, which is a member of the nuclear hormone receptor superfamily of ligand-inducible transcription factors. This receptor also functions as a receptor for the secondary bile acid, lithocholic acid. Downstream targets of vitamin D3 receptor are principally involved in mineral metabolism, though this receptor regulates a variety of other metabolic pathways, such as those involved in immune response and cancer. Mutations in this gene are associated with type II …

**Accessions** — [HGNC:12679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12679) · Entrez [7421](https://www.ncbi.nlm.nih.gov/gene/7421) · UniProt [P11473](https://www.uniprot.org/uniprotkb/P11473) · Ensembl [ENSG00000111424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111424)

## Data

Gene col 3232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3232); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3232]; `tensor/DDL_lfc|DDL_z.npy` [3232]; `embed/gene_vectors.npy` [3232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3232 or target_col == 3232). Every well: [[VDR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VDR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
