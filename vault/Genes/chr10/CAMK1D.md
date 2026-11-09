---
symbol: "CAMK1D"
type: "gene"
col: 11363
ensembl_id: "ENSG00000183049"
name: "calcium/calmodulin dependent protein kinase ID"
location: "10p13"
module: 228
arm: "+"
pooled_cpm: 150.88
n_lines_expressing: 41
n_dd_up: 2
n_dd_down: 44
n_dd_up_clean: 2
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# CAMK1D

*calcium/calmodulin dependent protein kinase ID* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +5.9, q 2e-06, up in 19 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 6 lines (J82 8.19×, HS-578T 4.74×, PANC-1 3.23×, A498 4.74×, …; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A498 5.14×, A-172 2.56×, J82 2.10×, hTERT-HPNE 4.77×); [[Tucidinostat (drug)]] 5 µM in 3 lines (SW480 2.74×, LoVo 2.08×, NCI-H460 1.99×); [[Tucidinostat (drug)]] 0.5 µM in 3 lines (SW480 2.49×, NCI-H460 2.79×, LoVo 2.17×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.443× (z -17.2, q 0e+00, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGBD5]] (+0.58, fdr 3e-05), [[SOX9]] (+0.55, fdr 1e-05), [[DPF3]] (+0.54, fdr 2e-04); moves opposite to [[CLCC1]] (-0.45, fdr 3e-05), [[PSMF1]] (-0.45, fdr 1e-04), [[ANAPC10]] (-0.44, fdr 2e-04).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DTX4]] → it (grade B ⚠); 2 go from it, the strongest it → [[TSPAN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11363.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 6 lines (J82 8.19×, HS-578T 4.74×, PANC-1 3.23×, A498 4.74×, …; ⚠ cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A498 5.14×, A-172 2.56×, J82 2.10×, hTERT-HPNE 4.77×); [[Tucidinostat (drug)]] 5 µM in 3 lines (SW480 2.74×, LoVo 2.08×, NCI-H460 1.99×); [[Tucidinostat (drug)]] 0.5 µM in 3 lines (SW480 2.49×, NCI-H460 2.79×, LoVo 2.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.9 | 2e-06 | 19/39 (SW480, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 2e-05 | 19/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +3.5 | 0.097 | 14/39 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.14 | 8/39 (SNU-423, A549, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.34× | +3.2 | 0.14 | 14/39 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.25 | 6/40 (SW480, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -17.2 | 0e+00 | 29/39 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.577×** | -16.5 | 0e+00 | 25/39 (NCI-H1792, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -15.6 | 0e+00 | 25/34 (NCI-H1792, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -15.3 | 0e+00 | 30/40 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.465×** | -15.0 | 0e+00 | 28/36 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -14.4 | 7e-45 | 28/40 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -14.1 | 2e-43 | 30/39 (NCI-H1792, C-33 A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -12.1 | 9e-32 | 27/39 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -11.5 | 8e-29 | 28/39 (NCI-H1792, SNU-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -11.2 | 2e-27 | 25/39 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -10.3 | 3e-23 | 28/38 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -10.0 | 1e-21 | 25/39 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -9.7 | 2e-20 | 27/38 (CFPAC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.642×** | -9.4 | 2e-19 | 23/39 (SHP-77, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -9.3 | 7e-19 | 29/39 (SW 900, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -8.0 | 6e-14 | 31/39 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -7.8 | 2e-13 | 23/39 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -7.8 | 2e-13 | 30/39 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -7.2 | 2e-11 | 22/39 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -7.2 | 2e-11 | 24/39 (HT-29, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -7.1 | 4e-11 | 24/39 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -6.8 | 3e-10 | 23/41 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 353 | 0 | 26 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -22.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -22.3) |
| [[CFPAC-1 (line)]] | alt | 403 | 0 | 21 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -18.9) |
| [[MIA PaCa-2 (line)]] | alt | 142 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -19.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -18.1) |
| [[RKO (line)]] | wt | 256 | 0 | 16 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0431× (z -40.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -29.2) |
| [[NCI-H1792 (line)]] | alt | 1,351 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -33.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -22.1) |
| [[HT-29 (line)]] | alt | 136 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -14.1) |
| [[LoVo (line)]] | wt | 82.5 | 5 (2 ⚠) | 9 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -14.8) |
| [[C-33 A (line)]] | alt | 174 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -16.2) |
| [[HOP62 (line)]] | alt | 146 | 1 (1 ⚠) | 12 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.91× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 183 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -26.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -16.1) |
| [[SHP-77 (line)]] | alt | 618 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -16.3) |
| [[SW 900 (line)]] | alt | 316 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -13.7) |
| [[SNU-423 (line)]] | alt | 241 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -11.7) |
| [[SW48 (line)]] | wt | 338 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -22.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -14.9) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.240× (z -11.0) |
| [[HS-578T (line)]] | alt | 170 | 2 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.74× (z +17.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.51× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.2) |
| [[J82 (line)]] | alt | 140 | 3 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +33.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.460× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.0) |
| [[SW480 (line)]] | alt | 49.7 | 3 (1 ⚠) | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.74× (z +16.6) | [[Harringtonine (drug)]] 5 µM 0.238× (z -16.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -12.7) |
| [[A-172 (line)]] | wt | 186 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.402× (z -9.3) |
| [[A-427 (line)]] | wt | 117 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0934× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.393× (z -10.4) |
| [[Hs 766T (line)]] | wt | 200 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -11.8) |
| [[A549 (line)]] | wt | 179 | 1 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.77× (z +10.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.255× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.296× (z -12.6) |
| [[LS 180 (line)]] | wt | 116 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -15.1) |
| [[A498 (line)]] | wt | 131 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.14× (z +13.5) | — |
| [[HCT15 (line)]] | alt | 184 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 49.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 57.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 49.2 | 2 | 1 | [[Tucidinostat (drug)]] 0.5 µM 2.79× (z +9.1) | [[Homoharringtonine (drug)]] 0.05 µM 0.349× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.59× (z +10.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.77× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 77.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -12.7) |
| [[PANC-1 (line)]] | alt | 87.4 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.23× (z +13.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -15.5) |
| [[BT-474 (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 253 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 56.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -9.0) |
| [[SW 1088 (line)]] | alt | 87.6 | 0 | 1 | — | [[Bestatin (drug)]] 5 µM 0.0674× (z -8.6) |
| [[AN3 CA (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGBD5]] | +0.58 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[SOX9]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[DPF3]] | +0.54 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[BMP2]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CA8]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ROR1-AS1]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[KCNN3]] | +0.52 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[PKIA]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CYB5R2]] | +0.52 | +0.37 / +0.61 | both halves | 7e-05 |  |
| [[WNT7B]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TMCC2]] | +0.52 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[IL1A]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCC1]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PSMF1]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ANAPC10]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTX4]] | B | DTX4 activity lowers CAMK1D's level | lines that do not express DTX4 (7) vs lines expressing it (43) | 2.85× higher at baseline in the lines without DTX4 | 0.039 | ⚠ within organs, on part of the lines; also absent: NEO1, WNK4, STPG2 |
| [[PIM1]] | C | PIM1 activity raises CAMK1D's level | lines that do not express PIM1 (4) vs lines expressing it (46) | 3.85× lower at baseline in the lines without PIM1 | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: CLSTN3, HFE, HACD1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN5]] | B | CAMK1D activity raises TSPAN5's level | lines that do not express CAMK1D (9) vs lines expressing it (41) | 2.79× lower at baseline in the lines without CAMK1D | 0.032 | ⚠ within organs, on part of the lines; also absent: OBSCN |
| [[PKIA]] | B | CAMK1D activity raises PKIA's level | lines that do not express CAMK1D (9) vs lines expressing it (41) | 2.77× lower at baseline in the lines without CAMK1D | 0.090 | ⚠ within organs, on part of the lines; also absent: OBSCN |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 2.7); signed map (45.0, 12.8). **Vector** length 118, 36.3% of its response variance represented; |z| ≥ 3 in 1,714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +8.2 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.2 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.5 | -6.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.5 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.5 | -0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.5 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase ID |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:12,349,547-12,835,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CKLiK |
| Gene groups (HGNC) | MicroRNA protein coding host genes; CAMK1 family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IU85](https://www.uniprot.org/uniprotkb/Q8IU85) (Calcium/calmodulin-dependent protein kinase type 1D):

> Calcium/calmodulin-dependent protein kinase that operates in the calcium-triggered CaMKK-CaMK1 signaling cascade and, upon calcium influx, activates CREB-dependent gene transcription, regulates calcium-mediated granulocyte function and respiratory burst and promotes basal dendritic growth of hippocampal neurons. In neutrophil cells, required for cytokine-induced proliferative responses and activation of the respiratory burst. Activates the transcription factor CREB1 in hippocampal neuron …

**Summary**, from NCBI Gene [57118](https://www.ncbi.nlm.nih.gov/gene/57118):

> This gene is a member of the calcium/calmodulin-dependent protein kinase 1 family, a subfamily of the serine/threonine kinases. The encoded protein is a component of the calcium-regulated calmodulin-dependent protein kinase cascade. It has been associated with multiple processes including regulation of granulocyte function, activation of CREB-dependent gene transcription, aldosterone synthesis, differentiation and activation of neutrophil cells, and apoptosis of erythroleukemia cells. …

**Accessions** — [HGNC:19341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19341) · Entrez [57118](https://www.ncbi.nlm.nih.gov/gene/57118) · UniProt [Q8IU85](https://www.uniprot.org/uniprotkb/Q8IU85) · Ensembl [ENSG00000183049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183049)

## Data

Gene col 11363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11363); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11363]; `tensor/DDL_lfc|DDL_z.npy` [11363]; `embed/gene_vectors.npy` [11363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11363 or target_col == 11363). Every well: [[CAMK1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
