---
symbol: "GARS1-DT"
type: "gene"
col: 12173
ensembl_id: "ENSG00000196295"
name: "GARS1 divergent transcript"
location: "7p14.3"
module: 15
arm: "+"
pooled_cpm: 55.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GARS1-DT

*GARS1 divergent transcript* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.59× (z +7.0, q 2e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.344× (z -22.7, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.326× (z -16.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF460-AS1]] (+0.79, fdr 7e-06), [[NBR2]] (+0.75, fdr 7e-06), [[BCL2L2-PABPN1]] (+0.72, fdr 1e-05); moves opposite to [[DHRS2]] (-0.62, fdr 2e-05), [[H3-3B]] (-0.60, fdr 1e-05), [[IER2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +7.0 | 2e-09 | 38/48 (LoVo, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +5.8 | 2e-06 | 34/48 (KATO III, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.6 | 3e-06 | 31/48 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.8 | 2e-04 | 29/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +4.5 | 1e-03 | 28/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.009 | 23/48 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.5 | 0.038 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.073 | 13/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.073 | 17/49 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.093 | 20/48 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.23×** | +3.1 | 0.094 | 19/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.12 | 20/47 (SW480, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.344×** | -22.7 | 0e+00 | 47/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.299×** | -17.5 | 0e+00 | 47/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.326×** | -16.9 | 0e+00 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.469×** | -11.4 | 5e-28 | 42/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.577×** | -8.3 | 1e-14 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -8.1 | 7e-14 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.623×** | -7.1 | 7e-11 | 42/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.465×** | -6.0 | 1e-07 | 33/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.681×** | -5.8 | 4e-07 | 36/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.689×** | -5.6 | 1e-06 | 30/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -5.2 | 1e-05 | 30/48 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -5.1 | 2e-05 | 31/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **0.715×** | -4.9 | 4e-05 | 28/47 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -4.9 | 5e-05 | 27/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.733×** | -4.7 | 1e-04 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.023 | 27/48 (AN3 CA, C32, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.732×** | -3.4 | 0.023 | 23/48 (H4, SW480, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.0 | 0.068 | 19/48 (SW480, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 109 | 1 | 11 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -32.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -19.7) |
| [[SW480 (line)]] | alt | 57.7 | 1 | 10 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -15.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 82.5 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -22.3) |
| [[A549 (line)]] | wt | 33.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -19.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.167× (z -15.5) |
| [[H4 (line)]] | wt | 95.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -16.4) |
| [[LoVo (line)]] | wt | 51.9 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.72× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -21.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 74.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.230× (z -14.6) |
| [[A-172 (line)]] | wt | 93.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -13.0) |
| [[A498 (line)]] | wt | 63.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -26.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -12.7) |
| [[C32 (line)]] | wt | 51.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -14.5) |
| [[HS-578T (line)]] | alt | 51.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 35.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 37.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -10.3) |
| [[RKO (line)]] | wt | 46.7 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.89× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -15.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.275× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 71.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -9.5) |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -9.5) |
| [[A-427 (line)]] | wt | 95.0 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.237× (z -12.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.302× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 57.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.4) |
| [[HOP62 (line)]] | alt | 33.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.4) |
| [[HT-29 (line)]] | alt | 77.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -26.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 42.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -9.0) |
| [[J82 (line)]] | alt | 44.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -10.4) |
| [[KATO III (line)]] | alt | 65.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LOX-IMVI (line)]] | wt | 35.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LS 180 (line)]] | wt | 40.1 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.220× (z -11.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -10.2) |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -10.4) |
| [[AN3 CA (line)]] | alt | 67.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -8.5) |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 74.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -9.7) |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0575× (z -11.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 60.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 82.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW 1271 (line)]] | alt | 84.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -14.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -15.2) |
| [[SW48 (line)]] | wt | 62.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 69.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460-AS1]] | +0.79 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[NBR2]] | +0.75 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[BCL2L2-PABPN1]] | +0.72 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[NRSN2-AS1]] | +0.69 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SLC25A53]] | +0.67 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[METTL4]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.64 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[APTX]] | +0.64 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[KCTD15]] | +0.61 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[CCNY-AS1]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GOT1-DT]] | +0.60 | +0.47 / +0.53 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS2]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[H3-3B]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[IER2]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[STK17A]] | -0.54 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SFR1]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SNAPIN]] | -0.53 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[DNMBP]] | -0.53 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[MRPL57]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[DPF1]] | -0.52 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[LIMA1]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[KRT19]] | -0.51 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[MAP1S]] | -0.51 | -0.43 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers GARS1-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers GARS1-DT's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.5, 22.9); signed map (2.5, 1.4). **Vector** length 104, 31.3% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.1 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +0.2 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.0 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.5 | -17.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.9 | -22.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GARS1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p14.3 — chr7:30,516,309-30,595,286 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC005154.6, AC005154.1; previously GARS-DT |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48951) · Entrez [401320](https://www.ncbi.nlm.nih.gov/gene/401320) · Ensembl [ENSG00000196295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196295)

## Data

Gene col 12173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12173); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12173]; `tensor/DDL_lfc|DDL_z.npy` [12173]; `embed/gene_vectors.npy` [12173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12173 or target_col == 12173). Every well: [[GARS1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GARS1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
