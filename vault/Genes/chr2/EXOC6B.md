---
symbol: "EXOC6B"
type: "gene"
col: 6837
ensembl_id: "ENSG00000144036"
name: "exocyst complex component 6B"
location: "2p13.2"
module: 211
arm: "+"
pooled_cpm: 288.53
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 18
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# EXOC6B

*exocyst complex component 6B* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.18× (z +14.6, q 1e-45, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.455× (z -14.8, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.726× (z -8.5, q 1e-15, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (A549 0.477×, NCI-H2347 0.435×, HS-578T 0.471×, NCI-H1792 0.504×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.111×, C-33 A 0.216×, SHP-77 0.256×, NCI-H460 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.321×, CFPAC-1 0.353×, A498 0.409×; ⚠ cell-cycle shift, explains ~79% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.488×); [[Auranofin (drug)]] 5 µM in 1 line (SNU-1 0.429×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERC1]] (+0.78, fdr 7e-06), [[SNX29]] (+0.67, fdr 7e-06), [[VPS13D]] (+0.66, fdr 1e-05); moves opposite to [[PAN2]] (-0.59, fdr 3e-05), [[LINC00623]] (-0.57, fdr 3e-05), [[LINC00869-1]] (-0.57, fdr 5e-05).
> It is in [[Module 211]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GARNL3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +14.6 | 1e-45 | 48/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +11.8 | 2e-29 | 47/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +11.7 | 3e-29 | 47/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +8.5 | 2e-15 | 38/48 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.67×** | +8.5 | 3e-15 | 43/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +7.1 | 1e-10 | 36/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +7.0 | 1e-10 | 34/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 8e-07 | 35/48 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.4 | 4e-06 | 28/48 (HT-29, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +5.2 | 9e-06 | 40/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +5.0 | 4e-05 | 34/47 (H4, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 31/47 (SW480, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 28/47 (RKO, A-172, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +3.9 | 0.003 | 30/50 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 33/50 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.006 | 12/48 (SK-MEL-2, AsPC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.006 | 25/47 (C32, Hs 766T, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.010 | 25/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.024 | 10/48 (SW480, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (A549 0.477×, NCI-H2347 0.435×, HS-578T 0.471×, NCI-H1792 0.504×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.111×, C-33 A 0.216×, SHP-77 0.256×, NCI-H460 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.321×, CFPAC-1 0.353×, A498 0.409×; ⚠ cell-cycle shift, explains ~79% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.488×); [[Auranofin (drug)]] 5 µM in 1 line (SNU-1 0.429×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.455×** | -14.8 | 0e+00 | 45/49 (NCI-H23, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.489×** | -12.9 | 7e-36 | 40/44 (SNU-1, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.489×** | -12.4 | 3e-33 | 42/45 (NCI-H1792, A-427, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.544×** | -11.0 | 5e-26 | 43/48 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.664×** | -10.9 | 2e-25 | 34/48 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.553×** | -10.7 | 9e-25 | 46/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.577×** | -10.3 | 4e-23 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.608×** | -9.4 | 6e-19 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -8.5 | 1e-15 | 33/49 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.667×** | -7.6 | 2e-12 | 45/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.690×** | -7.0 | 2e-10 | 36/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.732×** | -5.9 | 2e-07 | 32/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.749×** | -5.4 | 2e-06 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.580×** | -5.3 | 4e-06 | 31/49 (SNU-423, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.754×** | -5.3 | 4e-06 | 29/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -4.5 | 2e-04 | 33/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.844× | -3.2 | 0.042 | 23/48 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.893× | -3.0 | 0.071 | 4/49 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 308 | 3 (1 ⚠) | 17 (15 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.234× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.488× (z -10.6) |
| [[HOP62 (line)]] | alt | 306 | 5 (1 ⚠) | 9 (8 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.26× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.318× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 338 | 2 (1 ⚠) | 12 (12 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.71× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -18.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 253 | 3 | 11 (11 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -19.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[KATO III (line)]] | alt | 299 | 5 (1 ⚠) | 8 (8 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -16.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LOX-IMVI (line)]] | wt | 344 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -17.6) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.2) |
| [[LS 180 (line)]] | wt | 226 | 8 (2 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.75× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -13.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AsPC-1 (line)]] | alt | 214 | 6 (1 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -15.1) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 318 | 1 | 10 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 2.02× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -20.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.532× (z -8.9) |
| [[SNU-423 (line)]] | alt | 265 | 1 | 10 (9 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -22.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -12.8) |
| [[A-172 (line)]] | wt | 384 | 1 | 9 (8 ⚠) | [[Panobinostat (drug)]] 5 µM 1.69× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -10.6) |
| [[A498 (line)]] | wt | 259 | 4 (1 ⚠) | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -18.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[COLO 205 (line)]] | alt | 141 | 6 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[LoVo (line)]] | wt | 276 | 6 (2 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 314 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -16.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -8.8) |
| [[HT-29 (line)]] | alt | 85.8 | 8 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.97× (z +13.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -8.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 496 | 1 (1 ⚠) | 8 (7 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.93× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 461 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -14.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 510 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -27.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.549× (z -8.8) |
| [[SW480 (line)]] | alt | 184 | 6 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +16.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.434× (z -12.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 552 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -16.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 216 | 2 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.330× (z -13.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 240 | 2 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.4) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.18× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -9.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.202× (z -9.4) |
| [[SW 900 (line)]] | alt | 250 | 6 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.469× (z -9.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 298 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 271 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.9) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -13.7) |
| [[SNU-1 (line)]] | wt | 427 | 1 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.429× (z -10.0) |
| [[A549 (line)]] | wt | 438 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 206 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -21.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[H4 (line)]] | wt | 304 | 3 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.37× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 225 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.562× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 233 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 176 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -15.1) |
| [[RKO (line)]] | wt | 286 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -10.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 258 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -13.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 266 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 338 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.3) |
| [[C-33 A (line)]] | alt | 423 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -9.1) |
| [[SHP-77 (line)]] | alt | 232 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 165 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 292 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 385 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.6) |
| [[HCT15 (line)]] | alt | 346 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1271 (line)]] | alt | 298 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 321 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.7) ⚠ cell-cycle shift, explains ~79% of this change |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 337 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERC1]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[SNX29]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[VPS13D]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 | same gene group; STRING 987 |
| [[BTBD9]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[GAB2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PWWP3A]] | +0.63 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[TANGO2]] | +0.63 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[RPS6KC1]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KIF1B]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[VTI1A]] | +0.62 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[RNF216]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAN2]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[LINC00623]] | -0.57 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LINC00869-1]] | -0.57 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[KBTBD2]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[THAP9]] | -0.55 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[LINC00938]] | -0.55 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[DDX39B]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TTC32]] | -0.54 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD18A]] | -0.54 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[COQ9]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ZNF888]] | -0.53 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[LINC01138]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GARNL3]] | C | GARNL3 activity raises EXOC6B's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.0, -23.5); signed map (-28.7, -25.9). **Vector** length 123, 52.9% of its response variance represented; |z| ≥ 3 in 1,669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +13.5 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +13.5 | +7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +12.7 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.7 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +14.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.6 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.8 | -10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -9.7 | -10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.6 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:72,175,984-72,826,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0919; previously SEC15L2, SEC15B |
| Gene groups (HGNC) | Exocyst complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2D4](https://www.uniprot.org/uniprotkb/Q9Y2D4) (Exocyst complex component 6B):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane.

**Summary**, from NCBI Gene [23233](https://www.ncbi.nlm.nih.gov/gene/23233):

> This gene encodes a protein which is a part of the evolutionarily conserved exocyst, a multimeric protein complex necessary for exocytosis, which in turn, is crucial for cell growth, polarity and migration. Disruption of this gene may be associated with phenotypes exhibiting multiple symptoms including intellectual disability and developmental delay (DD). [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:17085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17085) · Entrez [23233](https://www.ncbi.nlm.nih.gov/gene/23233) · UniProt [Q9Y2D4](https://www.uniprot.org/uniprotkb/Q9Y2D4) · Ensembl [ENSG00000144036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144036)

## Data

Gene col 6837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6837); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6837]; `tensor/DDL_lfc|DDL_z.npy` [6837]; `embed/gene_vectors.npy` [6837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6837 or target_col == 6837). Every well: [[EXOC6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
