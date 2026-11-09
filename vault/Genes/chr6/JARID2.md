---
symbol: "JARID2"
type: "gene"
col: 158
ensembl_id: "ENSG00000008083"
name: "jumonji and AT-rich interaction domain containing 2"
location: "6p22.3"
module: 134
arm: "+"
pooled_cpm: 247.35
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# JARID2

*jumonji and AT-rich interaction domain containing 2* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.88× (z +14.2, q 6e-43, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.371× (z -22.2, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.732× (z -7.0, q 2e-10, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLEC11A]] (+0.59, fdr 1e-05), [[PAG1]] (+0.57, fdr 2e-05), [[FYN]] (+0.56, fdr 1e-05); moves opposite to [[GABPB2]] (-0.48, fdr 3e-04), [[CHMP3]] (-0.47, fdr 1e-04), [[LINC01355]] (-0.47, fdr 1e-04).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL6A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +14.2 | 6e-43 | 40/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +12.9 | 9e-36 | 39/47 (SW480, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +12.4 | 5e-33 | 37/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +11.3 | 2e-27 | 34/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +7.5 | 7e-12 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +6.4 | 1e-08 | 29/48 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +5.9 | 3e-07 | 27/48 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 1e-06 | 28/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.56×** | +5.2 | 1e-05 | 33/47 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.15× | +4.3 | 9e-04 | 21/47 (H4, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.2 | 0.073 | 17/47 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.371×** | -22.2 | 0e+00 | 45/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.357×** | -22.2 | 0e+00 | 42/43 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.440×** | -17.0 | 0e+00 | 40/44 (hTERT-HPNE, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.759×** | -8.7 | 4e-16 | 27/47 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -8.6 | 1e-15 | 34/46 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.732×** | -7.0 | 2e-10 | 34/47 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -7.0 | 2e-10 | 27/47 (RPMI-7951, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.619×** | -5.6 | 1e-06 | 25/37 (LOX-IMVI, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.655×** | -5.0 | 5e-05 | 29/47 (LoVo, C32, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.802×** | -4.9 | 5e-05 | 25/47 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.815×** | -4.6 | 2e-04 | 25/47 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.870× | -4.4 | 5e-04 | 17/48 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.822×** | -4.4 | 5e-04 | 23/46 (C32, NCI-H23, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.823×** | -4.2 | 0.001 | 23/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.831×** | -4.1 | 0.001 | 23/47 (SK-MEL-2, C32, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.716×** | -3.9 | 0.003 | 22/47 (SW 900, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.834× | -3.9 | 0.003 | 21/46 (C32, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.844× | -3.8 | 0.005 | 18/47 (SK-MEL-2, HCT15, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.005 | 22/47 (C32, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.012 | 20/47 (C32, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.789×** | -3.3 | 0.020 | 18/47 (C32, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 0.866× | -3.2 | 0.028 | 16/47 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.036 | 17/47 (NCI-H460, BT-474, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 376 | 3 | 13 (11 ⚠) | [[TAK-901 (drug)]] 5 µM 8.51× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -15.2) |
| [[PANC-1 (line)]] | alt | 80.3 | 6 (1 ⚠) | 9 (8 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +19.5) | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -17.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.489× (z -11.0) |
| [[SW480 (line)]] | alt | 137 | 10 (2 ⚠) | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.00× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -29.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.634× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 1,179 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 167 | 5 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +16.8) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -19.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.422× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 769 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -26.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -20.2) |
| [[KATO III (line)]] | alt | 130 | 7 (2 ⚠) | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.27× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.440× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 424 | 2 (1 ⚠) | 7 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.23× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -12.1) |
| [[SW1417 (line)]] | alt | 186 | 6 (1 ⚠) | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.20× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 161 | 6 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.30× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.555× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 213 | 6 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +18.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.95× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -15.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 170 | 3 | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.32× (z +11.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -12.4) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -10.7) |
| [[RKO (line)]] | wt | 99.0 | 6 (1 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.25× (z +12.4) | [[Harringtonine (drug)]] 0.5 µM 0.426× (z -9.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HEC-1-A (line)]] | alt | 101 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.65× (z +11.0) | — |
| [[J82 (line)]] | alt | 352 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -16.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 304 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.85× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -29.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.313× (z -16.3) |
| [[HOP62 (line)]] | alt | 908 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -20.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -8.9) |
| [[HS-578T (line)]] | alt | 773 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 147 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 276 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -17.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 150 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -18.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 76.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 344 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 186 | 2 (1 ⚠) | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.76× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -14.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 211 | 1 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -18.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 137 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -15.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 134 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.39× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 294 | 2 (1 ⚠) | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.75× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 415 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -25.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 265 | 1 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 290 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -19.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 101 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 192 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -12.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 83.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.22× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 332 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.1) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.189× (z -18.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 143 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.02× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 481 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0594× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -8.6) |
| [[A-427 (line)]] | wt | 201 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -17.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 242 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -12.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 155 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +10.1) | — |
| [[H4 (line)]] | wt | 373 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.23× (z +10.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 154 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.39× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[COLO 205 (line)]] | alt | 97.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +9.0) | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 512 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -10.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 276 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLEC11A]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PAG1]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[FYN]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[LINC03047]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SLC2A3]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[NDRG1]] | +0.54 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[ELL2]] | +0.54 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[WDFY2]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[TCF7L1]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RORA]] | +0.51 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[SMARCD3]] | +0.51 | +0.53 / +0.39 | both halves | 6e-05 | pathway: Epigenetic regulation of gene expression |
| [[RNF122]] | +0.51 | +0.51 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB2]] | -0.48 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[CHMP3]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[LINC01355]] | -0.47 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[KLRA1P]] | -0.47 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[FBXO4]] | -0.47 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[HNF4G]] | -0.47 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[CARD8]] | -0.47 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[CLHC1]] | -0.47 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[ACTR3C]] | -0.47 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[PSMD6-AS1]] | -0.46 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[TXNRD2]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ZXDA]] | -0.46 | -0.40 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL6A1]] | B | COL6A1 activity raises JARID2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 1.65× lower at baseline in the lines without COL6A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[COL6A2]] | B | COL6A2 activity raises JARID2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without COL6A2 | 0.032 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[PAG1]] | B | PAG1 activity raises JARID2's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.77× lower at baseline in the lines without PAG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[COL6A1]] | B | COL6A1 activity weakens JARID2's drug response | lines that do not express COL6A1 (23) vs lines expressing it (25) | the lines without COL6A1 respond 1.30× as strongly (z diff -1.12); strongest at Belinostat 5 µM: 1.98x vs 1.31x (z diff -4.3) | 0.048 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; target measured in part of the lines; artifact flags |
| [[LINC03047]] | B | LINC03047 activity raises JARID2's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without LINC03047 | 0.074 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[IGFBP2]] | B | IGFBP2 activity lowers JARID2's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.67× higher at baseline in the lines without IGFBP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers JARID2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers JARID2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.5, -11.0); signed map (-27.3, 28.6). **Vector** length 126, 41.3% of its response variance represented; |z| ≥ 3 in 1,772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +12.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.4 | +11.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +14.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +7.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -9.5 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.9 | -17.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -22.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | jumonji and AT-rich interaction domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:15,246,069-15,522,042 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously JMJ |
| Gene groups (HGNC) | AT-rich interaction domain containing; Iron (II) and 2-oxoglutarate dependent oxygenases |
| Reactome | 2 pathways, smallest: PRC2 methylates histones and DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92833](https://www.uniprot.org/uniprotkb/Q92833) (Protein Jumonji):

> Histone reader that acts as a regulator of histone methyltransferase complexes, thereby playing an essential role in embryonic development, including heart and liver development, neural tube fusion process and hematopoiesis. Specifically recognizes and binds histone H2A ubiquitinated at 'Lys-119' (H2AK119Ub). Acts as an accessory subunit for the core PRC2 (Polycomb repressive complex 2) complex, which mediates histone H3K27 (H3K27me3) trimethylation on chromatin. Mediates the recruitment of the …

**Summary**, from NCBI Gene [3720](https://www.ncbi.nlm.nih.gov/gene/3720):

> This gene encodes a Jumonji- and AT-rich interaction domain (ARID)-domain-containing protein. The encoded protein is a DNA-binding protein that functions as a transcriptional repressor. This protein interacts with the Polycomb repressive complex 2 (PRC2) which plays an essential role in regulating gene expression during embryonic development. This protein facilitates the recruitment of the PRC2 complex to target genes. Alternate splicing results in multiple transcript variants. Mutations in …

**Accessions** — [HGNC:6196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6196) · Entrez [3720](https://www.ncbi.nlm.nih.gov/gene/3720) · UniProt [Q92833](https://www.uniprot.org/uniprotkb/Q92833) · Ensembl [ENSG00000008083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008083)

## Data

Gene col 158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 158); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 158]; `tensor/DDL_lfc|DDL_z.npy` [158]; `embed/gene_vectors.npy` [158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 158 or target_col == 158). Every well: [[JARID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JARID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
