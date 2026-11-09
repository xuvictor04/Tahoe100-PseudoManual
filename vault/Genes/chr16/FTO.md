---
symbol: "FTO"
type: "gene"
col: 6445
ensembl_id: "ENSG00000140718"
name: "FTO alpha-ketoglutarate dependent dioxygenase"
location: "16q12.2"
module: 185
arm: "+"
pooled_cpm: 168.39
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# FTO

*FTO alpha-ketoglutarate dependent dioxygenase* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.95× (z +12.0, q 3e-30, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.507× (z -21.3, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -18.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTNNBL1]] (+0.69, fdr 1e-05), [[CDKAL1]] (+0.68, fdr 7e-06), [[INVS]] (+0.68, fdr 7e-06); moves opposite to [[KRBOX5]] (-0.58, fdr 2e-05), [[XIAP]] (-0.58, fdr 4e-05), [[CREB1]] (-0.58, fdr 1e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +12.0 | 3e-30 | 47/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +7.5 | 1e-11 | 38/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.29×** | +5.2 | 5e-05 | 30/48 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.24×** | +4.7 | 4e-04 | 25/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +4.1 | 0.004 | 13/48 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.015 | 20/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.7 | 0.015 | 17/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.040 | 19/49 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.060 | 20/49 (NCI-H2030, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.064 | 18/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.32× | +3.1 | 0.11 | 18/50 (HEC-1-A, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +3.0 | 0.12 | 8/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.507×** | -21.3 | 0e+00 | 43/48 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.434×** | -18.5 | 0e+00 | 47/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -18.5 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -14.7 | 0e+00 | 38/49 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.505×** | -14.6 | 0e+00 | 46/47 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -13.8 | 1e-41 | 42/44 (CHP-212, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -12.6 | 2e-34 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.540×** | -12.2 | 2e-32 | 46/49 (SNU-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.568×** | -12.1 | 1e-31 | 41/48 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -11.8 | 2e-30 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.656×** | -9.3 | 5e-19 | 38/48 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.675×** | -8.7 | 1e-16 | 40/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -8.4 | 2e-15 | 41/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.691×** | -7.3 | 1e-11 | 43/48 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -7.0 | 1e-10 | 29/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.861× | -4.7 | 9e-05 | 7/49 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.816×** | -4.0 | 0.001 | 27/47 (HT-29, H4, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.831×** | -4.0 | 0.002 | 22/47 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.726×** | -3.5 | 0.009 | 25/48 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.5 | 0.009 | 12/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.838× | -3.5 | 0.010 | 20/48 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.896× | -3.4 | 0.012 | 7/49 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.024 | 20/48 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 233 | 1 (1 ⚠) | 16 (10 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.85× (z +9.7) ⚠ cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -29.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -22.9) |
| [[C32 (line)]] | wt | 268 | 1 | 14 (9 ⚠) | [[PH-797804 (drug)]] 5 µM 4.34× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -33.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 190 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -30.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -27.6) |
| [[J82 (line)]] | alt | 177 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -25.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -19.5) |
| [[PANC-1 (line)]] | alt | 133 | 2 | 11 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -17.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -14.2) |
| [[MIA PaCa-2 (line)]] | alt | 215 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -19.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -16.7) |
| [[SNU-423 (line)]] | alt | 172 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -29.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -18.2) |
| [[SW480 (line)]] | alt | 177 | 2 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.392× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.429× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 128 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -25.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -15.7) |
| [[A498 (line)]] | wt | 301 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -30.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -16.2) |
| [[HS-578T (line)]] | alt | 190 | 1 | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -16.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -12.5) |
| [[A549 (line)]] | wt | 166 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -17.2) |
| [[HepG2_C3A (line)]] | wt | 186 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 184 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -19.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 377 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -21.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.9) |
| [[SW1417 (line)]] | alt | 141 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -19.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -16.2) |
| [[SW 900 (line)]] | alt | 165 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 85.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -18.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -14.9) |
| [[H4 (line)]] | wt | 199 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.8) |
| [[HT-29 (line)]] | alt | 129 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -12.9) |
| [[LoVo (line)]] | wt | 138 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.296× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -17.2) |
| [[CHP-212 (line)]] | wt | 310 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.3) |
| [[COLO 205 (line)]] | alt | 94.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -13.7) |
| [[HCT15 (line)]] | alt | 195 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 179 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.06× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -13.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -11.6) |
| [[KATO III (line)]] | alt | 121 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -15.1) |
| [[LS 180 (line)]] | wt | 103 | 1 (1 ⚠) | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.31× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 67.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.428× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 199 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -14.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 234 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.240× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -14.9) |
| [[BT-474 (line)]] | alt | 117 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 119 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.50× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 184 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -23.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -16.9) |
| [[SW48 (line)]] | wt | 170 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -11.4) |
| [[A-427 (line)]] | wt | 159 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.39× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.1) |
| [[AN3 CA (line)]] | alt | 241 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 122 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.10× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -17.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 178 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.49× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 166 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -8.7) |
| [[RKO (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SHP-77 (line)]] | alt | 186 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.485× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.5) |
| [[SW 1088 (line)]] | alt | 295 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.2) |
| [[Hs 766T (line)]] | wt | 66.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBL1]] | +0.69 | +0.69 / +0.56 | both halves | 1e-05 | STRING 450 |
| [[CDKAL1]] | +0.68 | +0.65 / +0.74 | both halves | 7e-06 | STRING 872 |
| [[INVS]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CDC123]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 | STRING 586 |
| [[TOMM70]] | +0.66 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[MRPS35]] | +0.65 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[VPS50]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[IPO11]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CSTPP1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NOL10]] | +0.63 | +0.58 / +0.63 | both halves | 8e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX5]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[XIAP]] | -0.58 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[CREB1]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 | STRING 481 |
| [[RO60]] | -0.57 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[PKNOX1]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[NPHS1]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[PDE6D]] | -0.54 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[LRCH3]] | -0.53 | -0.59 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises FTO's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers FTO's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AGTPBP1]] | C | AGTPBP1 activity raises FTO's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.32× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.5, -13.3); signed map (-15.4, -49.3). **Vector** length 127, 48.2% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +12.5 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +10.1 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +8.1 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | +7.5 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.0 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.5 | -21.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.8 | -18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | FTO alpha-ketoglutarate dependent dioxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:53,701,692-54,158,512 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1752, MGC5149, ALKBH9, IFEX9 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Reactome | 3 pathways, smallest: Reversal of alkylation damage by DNA dioxygenases; DNA Damage Reversal; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0B1](https://www.uniprot.org/uniprotkb/Q9C0B1) (Alpha-ketoglutarate-dependent dioxygenase FTO):

> RNA demethylase that mediates oxidative demethylation of different RNA species, such as mRNAs, tRNAs and snRNAs, and acts as a regulator of fat mass, adipogenesis and energy homeostasis. Specifically demethylates N(6)-methyladenosine (m6A) RNA, the most prevalent internal modification of messenger RNA (mRNA) in higher eukaryotes. M6A demethylation by FTO affects mRNA expression and stability. Also able to demethylate m6A in U6 small nuclear RNA (snRNA). Mediates demethylation of …

**Summary**, from NCBI Gene [79068](https://www.ncbi.nlm.nih.gov/gene/79068):

> This gene is a nuclear protein of the AlkB related non-haem iron and 2-oxoglutarate-dependent oxygenase superfamily but the exact physiological function of this gene is not known. Other non-heme iron enzymes function to reverse alkylated DNA and RNA damage by oxidative demethylation. Studies in mice and humans indicate a role in nervous and cardiovascular systems and a strong association with body mass index, obesity risk, and type 2 diabetes. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:24678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24678) · Entrez [79068](https://www.ncbi.nlm.nih.gov/gene/79068) · UniProt [Q9C0B1](https://www.uniprot.org/uniprotkb/Q9C0B1) · Ensembl [ENSG00000140718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140718)

## Data

Gene col 6445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6445); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6445]; `tensor/DDL_lfc|DDL_z.npy` [6445]; `embed/gene_vectors.npy` [6445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6445 or target_col == 6445). Every well: [[FTO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
