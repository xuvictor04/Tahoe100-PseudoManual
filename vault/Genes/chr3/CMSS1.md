---
symbol: "CMSS1"
type: "gene"
col: 11507
ensembl_id: "ENSG00000184220"
name: "cms1 ribosomal small subunit homolog"
location: "3q12.1"
module: 4
arm: "+"
pooled_cpm: 202.28
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CMSS1

*cms1 ribosomal small subunit homolog* — 3q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.22× (z +17.8, q 0e+00, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.48× (z +8.6, q 5e-16, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.579× (z -17.2, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP83]] (+0.80, fdr 7e-06), [[TSEN2]] (+0.78, fdr 7e-06), [[MDN1]] (+0.77, fdr 7e-06); moves opposite to [[TSC22D4]] (-0.63, fdr 1e-05), [[KLC4]] (-0.63, fdr 1e-05), [[ZNF821]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.22×** | +17.8 | 0e+00 | 39/48 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.06×** | +16.1 | 0e+00 | 40/48 (C32, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.84×** | +13.6 | 1e-39 | 35/48 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +12.6 | 2e-34 | 43/48 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +10.2 | 2e-22 | 37/47 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +8.6 | 5e-16 | 36/48 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.2 | 3e-14 | 34/48 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +8.1 | 3e-14 | 33/48 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +7.6 | 2e-12 | 38/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 2e-11 | 29/48 (Panc 03.27, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.0 | 2e-10 | 32/48 (NCI-H1792, H4, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +6.5 | 3e-09 | 28/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +5.5 | 2e-06 | 34/48 (C32, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.26×** | +5.1 | 1e-05 | 24/48 (NCI-H2030, NCI-H1792, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 23/48 (NCI-H1792, H4, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +4.3 | 6e-04 | 26/48 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.001 | 23/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.001 | 20/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.002 | 20/48 (SW1417, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.003 | 17/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.003 | 21/49 (HT-29, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 18/47 (C32, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -17.2 | 0e+00 | 41/49 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -6.2 | 1e-07 | 29/49 (SNU-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -4.6 | 5e-04 | 24/48 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -4.6 | 5e-04 | 24/48 (RKO, SW48, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.815×** | -4.6 | 5e-04 | 26/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.824×** | -4.3 | 0.001 | 23/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.822×** | -4.2 | 0.002 | 22/47 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.832×** | -4.1 | 0.003 | 19/49 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.832×** | -4.0 | 0.005 | 23/47 (SW1417, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.888× | -3.8 | 0.010 | 8/49 (Panc 03.27, SNU-1, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.848× | -3.6 | 0.019 | 18/49 (C-33 A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.855× | -3.5 | 0.021 | 20/48 (HOP62, A-427, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.021 | 22/47 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.023 | 19/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 0.898× | -3.4 | 0.023 | 6/48 (C-33 A, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.861× | -3.4 | 0.028 | 9/48 (KATO III, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.028 | 18/47 (COLO 205, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.884× | -3.2 | 0.045 | 21/48 (LoVo, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 170 | 7 (4 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.37× (z +16.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 139 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 81.2 | 7 (5 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.18× (z +12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 3.19× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 89.3 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 89.4 | 7 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.3) | — |
| [[SW48 (line)]] | wt | 368 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.48× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -21.6) |
| [[HS-578T (line)]] | alt | 225 | 5 (5 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.95× (z +14.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -13.5) |
| [[A-172 (line)]] | wt | 109 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 79.5 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 223 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -18.9) |
| [[RKO (line)]] | wt | 336 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -21.3) |
| [[SW1417 (line)]] | alt | 241 | 1 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.06× (z +10.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -20.2) |
| [[AsPC-1 (line)]] | alt | 88.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 146 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.11× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 438 | 2 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.84× (z +9.2) ⚠ unreliable plate only · without an alert: [[Belumosudil (drug)]] 5 µM 1.81× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -22.7) |
| [[SK-MEL-2 (line)]] | alt | 263 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 109 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 110 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 289 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -23.2) |
| [[BT-474 (line)]] | alt | 163 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 146 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +13.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[KATO III (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 159 | 0 | 3 | — | [[Cobimetinib (drug)]] 5 µM 0.415× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 280 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.52× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 286 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.53× (z +12.3) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -17.9) |
| [[Panc 03.27 (line)]] | alt | 190 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 342 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.90× (z +9.7) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -20.1) |
| [[SHP-77 (line)]] | alt | 292 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -11.8) |
| [[SNU-1 (line)]] | wt | 277 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.17× (z +8.5) ⚠ toxic | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.506× (z -11.0) |
| [[C-33 A (line)]] | alt | 244 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 289 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +11.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 304 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -15.4) |
| [[LS 180 (line)]] | wt | 92.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 238 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 1.93× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 145 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.82× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 211 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +9.0) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.1) |
| [[A-427 (line)]] | wt | 396 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.641× (z -9.9) |
| [[A549 (line)]] | wt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.7) |
| [[AN3 CA (line)]] | alt | 305 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -11.5) |
| [[CHP-212 (line)]] | wt | 208 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.8) |
| [[COLO 205 (line)]] | alt | 51.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.47× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 236 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | +0.80 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[MDN1]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[DDX10]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[DKC1]] | +0.72 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[URB2]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[LDLRAD3]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[CLYBL]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[NAA15]] | +0.70 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[CAD]] | +0.70 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[DPH6]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[EEFSEC]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[KLC4]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.62 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ZNF490]] | -0.59 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GNAS]] | -0.59 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.59 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[APPBP2]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises CMSS1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without TERT | 0.017 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[FAM78B]] | B | FAM78B activity raises CMSS1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.57× lower at baseline in the lines without FAM78B | 0.022 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[MTHFD1L]], [[USP31]] | C | MTHFD1L, USP31 activity raises CMSS1's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.53× lower at baseline in the lines without MTHFD1L, USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.7, -37.4); signed map (-5.7, -49.9). **Vector** length 160, 60.2% of its response variance represented; |z| ≥ 3 in 1,633 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.4 | +12.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +8.3 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.2 | +10.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.5 | +17.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +5.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.3 | -17.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.8 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cms1 ribosomal small subunit homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.1 — chr3:99,817,837-100,181,732 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4308; previously C3orf26 |
| Matched by | ensembl_id |

UniProt [Q9BQ75](https://www.uniprot.org/uniprotkb/Q9BQ75) carries no function annotation.

**Summary**, from NCBI Gene [84319](https://www.ncbi.nlm.nih.gov/gene/84319):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28666) · Entrez [84319](https://www.ncbi.nlm.nih.gov/gene/84319) · UniProt [Q9BQ75](https://www.uniprot.org/uniprotkb/Q9BQ75) · Ensembl [ENSG00000184220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184220)

## Data

Gene col 11507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11507); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11507]; `tensor/DDL_lfc|DDL_z.npy` [11507]; `embed/gene_vectors.npy` [11507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11507 or target_col == 11507). Every well: [[CMSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
