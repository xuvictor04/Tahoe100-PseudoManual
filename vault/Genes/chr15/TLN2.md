---
symbol: "TLN2"
type: "gene"
col: 10184
ensembl_id: "ENSG00000171914"
name: "talin 2"
location: "15q22.2"
module: 73
arm: "+"
pooled_cpm: 44.73
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 17
n_dd_up_clean: 28
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# TLN2

*talin 2* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.42× (z +23.3, q 0e+00, up in 39 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.369× (z -15.6, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK39]] (+0.59, fdr 3e-05), [[C16orf74]] (+0.58, fdr 3e-05), [[DOCK9]] (+0.57, fdr 5e-05); moves opposite to [[YJU2B]] (-0.48, fdr 1e-04), [[ZSCAN16-AS1]] (-0.47, fdr 2e-04), [[LRRC27]] (-0.46, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ERG]] → it (grade B ⚠); 2 go from it, the strongest it → [[LRRC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.42×** | +23.3 | 0e+00 | 39/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +23.1 | 0e+00 | 36/43 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.90×** | +21.4 | 0e+00 | 37/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.10×** | +17.8 | 0e+00 | 37/43 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +15.2 | 0e+00 | 37/43 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.50×** | +14.4 | 4e-45 | 37/43 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.94×** | +8.8 | 7e-17 | 33/43 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.72×** | +8.2 | 2e-14 | 24/43 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +7.6 | 2e-12 | 32/43 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +6.7 | 1e-09 | 26/43 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +5.8 | 3e-07 | 24/43 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.8 | 4e-07 | 18/43 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.93×** | +5.4 | 3e-06 | 21/42 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +5.1 | 1e-05 | 17/43 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-05 | 20/43 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.9 | 3e-05 | 23/43 (SW480, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 4e-05 | 22/43 (PANC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.369×** | -15.6 | 0e+00 | 41/43 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -14.1 | 1e-42 | 35/42 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.488×** | -11.3 | 4e-27 | 36/43 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -10.3 | 1e-22 | 36/43 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.609×** | -7.5 | 8e-12 | 27/43 (AsPC-1, LoVo, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -7.4 | 1e-11 | 24/43 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.430×** | -6.9 | 3e-10 | 27/43 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.765×** | -6.0 | 2e-07 | 21/43 (KATO III, LoVo, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.508×** | -5.6 | 2e-06 | 21/43 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -5.1 | 2e-05 | 24/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.734×** | -4.9 | 6e-05 | 19/43 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.811×** | -4.7 | 2e-04 | 20/43 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -4.3 | 7e-04 | 19/42 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -4.1 | 0.002 | 19/43 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.619×** | -3.9 | 0.003 | 14/28 (SNU-423, H4, …) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.756×** | -3.1 | 0.057 | 9/43 (H4, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 60.1 | 5 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 4.15× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.128× (z -9.3) |
| [[KATO III (line)]] | alt | 158 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -26.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -14.9) |
| [[HOP62 (line)]] | alt | 45.6 | 5 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.58× (z +16.7) | [[Digitoxin (drug)]] 5 µM 0.201× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -12.7) |
| [[LoVo (line)]] | wt | 254 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -13.0) |
| [[PANC-1 (line)]] | alt | 47.6 | 5 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.93× (z +19.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -16.2) |
| [[A-427 (line)]] | wt | 45.2 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -18.3) |
| [[SW480 (line)]] | alt | 12.9 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +16.4) | — |
| [[A-172 (line)]] | wt | 38.6 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.81× (z +13.8) | — |
| [[H4 (line)]] | wt | 29.5 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.3× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.149× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 27.4 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.39× (z +10.2) | [[Harringtonine (drug)]] 5 µM 0.104× (z -15.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -10.3) |
| [[A498 (line)]] | wt | 23.3 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +17.4) | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +16.0) | — |
| [[A549 (line)]] | wt | 36.5 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 48.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0537× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -9.5) |
| [[HS-578T (line)]] | alt | 42.3 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +15.4) | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 16.3× (z +13.5) | — |
| [[J82 (line)]] | alt | 50.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.42× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.308× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 56.2 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.151× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 3.88× (z +12.1) | — |
| [[C32 (line)]] | wt | 31.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.90× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +16.5) | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.45× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 25.1 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -9.0) |
| [[RKO (line)]] | wt | 38.1 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.3) | [[PH-797804 (drug)]] 5 µM 0.0708× (z -9.8) |
| [[SNU-423 (line)]] | alt | 36.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.52× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.256× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 11.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 16.7× (z +12.1) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0700× (z -11.1) |
| [[C-33 A (line)]] | alt | 53.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -13.1) |
| [[LS 180 (line)]] | wt | 145 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 62.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.91× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 34.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +17.1) | — |
| [[HCT15 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 83.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -9.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.100× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0761× (z -13.0) |
| [[SW1417 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +13.8) | — |
| [[SW48 (line)]] | wt | 65.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK39]] | +0.59 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[C16orf74]] | +0.58 | +0.44 / +0.53 | both halves | 3e-05 | same gene group |
| [[DOCK9]] | +0.57 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[CALB1]] | +0.57 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[TPTEP1-1]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RAP1GAP2]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[MPRIP]] | +0.55 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ANO1]] | +0.55 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[MUC17]] | +0.54 | +0.56 / +0.29 | both halves | 2e-04 |  |
| [[LINC02582]] | +0.54 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[ASAP2]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[DSG4]] | +0.53 | +0.47 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YJU2B]] | -0.48 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[ZSCAN16-AS1]] | -0.47 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[LRRC27]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[OSCP1]] | -0.46 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[ORAI3]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SPATA24]] | -0.45 | -0.29 / -0.39 | both halves | 3e-04 |  |
| [[DNAL4]] | -0.45 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[WBP4]] | -0.44 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[BBS1]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZNF226]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZNF630]] | -0.44 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[CYP27A1]] | -0.43 | -0.41 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERG]] | B | ERG activity raises TLN2's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without ERG | 0.005 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[TPTEP1-1]] | B | TPTEP1-1 activity raises TLN2's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.33× lower at baseline in the lines without TPTEP1-1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[TOP2A]] | B | TOP2A activity lowers TLN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02582]] | B | LINC02582 activity weakens TLN2's drug response | lines that do not express LINC02582 (36) vs lines expressing it (7) | the lines without LINC02582 respond 1.77× as strongly (z diff -3.35); strongest at Belinostat 5 µM: 3.25x vs 1.08x (z diff -7.6) | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[LINC02582]] | B | LINC02582 activity raises TLN2's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.09× lower at baseline in the lines without LINC02582 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[DSG4]] | B | DSG4 activity raises TLN2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.54× lower at baseline in the lines without DSG4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[TPTEP1-1]] | B | TPTEP1-1 activity weakens TLN2's drug response | lines that do not express TPTEP1-1 (36) vs lines expressing it (7) | the lines without TPTEP1-1 respond 1.31× as strongly (z diff -1.67); strongest at Idarubicin (hydrochloride) 5 µM: 2.56x vs 1.15x (z diff -5.3) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC20]] | B | TLN2 activity raises LRRC20's level | lines that do not express TLN2 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without TLN2 | 0.061 | ⚠ within organs, on part of the lines; also absent: FAT3, ENSG00000232732, SLC26A2; maybe low, not absent |
| [[GLI2]] | B | TLN2 activity raises GLI2's level | lines that do not express TLN2 (5) vs lines expressing it (45) | 3.38× lower at baseline in the lines without TLN2 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAT3, ENSG00000232732, SLC26A2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, 50.1); signed map (9.4, 35.6). **Vector** length 84.9, 20.6% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +15.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.6 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +14.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | +4.9 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -1.7 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | talin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:62,390,526-62,844,631 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0320, ILWEQ |
| Gene groups (HGNC) | FERM domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4G6](https://www.uniprot.org/uniprotkb/Q9Y4G6) (Talin-2):

> As a major component of focal adhesion plaques that links integrin to the actin cytoskeleton, may play an important role in cell adhesion. Recruits PIP5K1C to focal adhesion plaques and strongly activates its kinase activity (By similarity).

**Summary**, from NCBI Gene [83660](https://www.ncbi.nlm.nih.gov/gene/83660):

> This gene encodes a protein related to talin 1, a cytoskeletal protein that plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. This protein has a different pattern of expression compared to talin 1 but, like talin 1, is thought to associate with unique transmembrane receptors to form novel linkages between extracellular matrices and the actin cytoskeleton. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15447) · Entrez [83660](https://www.ncbi.nlm.nih.gov/gene/83660) · UniProt [Q9Y4G6](https://www.uniprot.org/uniprotkb/Q9Y4G6) · Ensembl [ENSG00000171914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171914)

## Data

Gene col 10184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10184); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10184]; `tensor/DDL_lfc|DDL_z.npy` [10184]; `embed/gene_vectors.npy` [10184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10184 or target_col == 10184). Every well: [[TLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
