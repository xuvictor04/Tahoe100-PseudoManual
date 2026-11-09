---
symbol: "DGLUCY"
type: "gene"
col: 5488
ensembl_id: "ENSG00000133943"
name: "D-glutamate cyclase"
location: "14q32.11"
module: 32
arm: "+"
pooled_cpm: 58.22
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 37
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# DGLUCY

*D-glutamate cyclase* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.40× (z +5.3, q 7e-05, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -21.0, q 0e+00, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.316× (z -18.9, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A6]] (+0.60, fdr 1e-05), [[DNPEP]] (+0.57, fdr 4e-05), [[GPATCH3]] (+0.54, fdr 3e-05); moves opposite to [[CNN2]] (-0.54, fdr 7e-05), [[TMEM170B]] (-0.53, fdr 4e-05), [[FAM3C]] (-0.48, fdr 8e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +5.3 | 7e-05 | 28/45 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.37×** | +4.8 | 4e-04 | 28/47 (A-427, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.003 | 23/46 (KATO III, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.007 | 20/46 (KATO III, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.007 | 21/46 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.013 | 20/46 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.030 | 19/46 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.032 | 17/45 (C32, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.056 | 17/46 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Rifaximin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.069 | 9/46 (RPMI-7951, SW480, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.084 | 11/46 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.092 | 14/47 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.099 | 14/46 (SW480, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.11 | 13/46 (BT-474, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.405×** | -21.0 | 0e+00 | 40/46 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.316×** | -18.9 | 0e+00 | 45/46 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.323×** | -18.5 | 0e+00 | 43/46 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.369×** | -16.3 | 0e+00 | 44/46 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.408×** | -14.1 | 2e-43 | 38/46 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.541×** | -10.1 | 6e-22 | 35/46 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.538×** | -9.8 | 1e-20 | 26/38 (SNU-423, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.558×** | -9.6 | 8e-20 | 38/46 (LoVo, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.534×** | -9.4 | 3e-19 | 32/46 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.564×** | -9.4 | 3e-19 | 35/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -8.9 | 3e-17 | 35/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.601×** | -8.3 | 3e-15 | 39/46 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.581×** | -8.2 | 7e-15 | 28/41 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.627×** | -7.7 | 8e-13 | 29/46 (LoVo, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -7.6 | 1e-12 | 36/46 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.650×** | -7.1 | 6e-11 | 34/46 (SNU-423, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -6.2 | 2e-08 | 30/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.743×** | -4.9 | 3e-05 | 27/46 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -4.5 | 2e-04 | 23/46 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.752×** | -4.3 | 4e-04 | 19/45 (MIA PaCa-2, H4, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -4.3 | 4e-04 | 25/46 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.701×** | -4.2 | 6e-04 | 22/45 (HOP62, J82, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.770×** | -4.1 | 8e-04 | 25/46 (RKO, HS-578T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.006 | 18/46 (MIA PaCa-2, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 179 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -26.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.181× (z -20.3) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 12 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0494× (z -25.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.123× (z -18.6) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -16.6) |
| [[HS-578T (line)]] | alt | 64.7 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -16.8) |
| [[HOP62 (line)]] | alt | 51.0 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -10.2) |
| [[PANC-1 (line)]] | alt | 44.5 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -29.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -11.1) |
| [[A-172 (line)]] | wt | 62.7 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.163× (z -16.5) |
| [[A549 (line)]] | wt | 60.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 97.2 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -17.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.210× (z -14.0) |
| [[SW480 (line)]] | alt | 39.8 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -15.5) |
| [[H4 (line)]] | wt | 114 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.191× (z -12.1) |
| [[LS 180 (line)]] | wt | 102 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 74.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.156× (z -14.3) |
| [[SW48 (line)]] | wt | 144 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.234× (z -10.4) |
| [[Hs 766T (line)]] | wt | 58.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -11.9) |
| [[KATO III (line)]] | alt | 47.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -13.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.311× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 74.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -11.4) |
| [[HT-29 (line)]] | alt | 46.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 68.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 4 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -13.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RKO (line)]] | wt | 43.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 87.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.312× (z -10.7) |
| [[A-427 (line)]] | wt | 68.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -11.1) |
| [[A498 (line)]] | wt | 20.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -16.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 50.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -9.8) |
| [[HCT15 (line)]] | alt | 81.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.301× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 68.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.333× (z -8.5) |
| [[SHP-77 (line)]] | alt | 32.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.276× (z -10.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.320× (z -9.4) |
| [[CHP-212 (line)]] | wt | 81.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 41.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -9.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -8.5) |
| [[SNU-1 (line)]] | wt | 62.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.212× (z -10.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 34.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.329× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[C32 (line)]] | wt | 52.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2347 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -9.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A6]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[DNPEP]] | +0.57 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[GPATCH3]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[COA6]] | +0.54 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[APOL2]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ERAP2]] | +0.52 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[PSMB10]] | +0.51 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[CASP8]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[RCC1L]] | +0.51 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[ZC3HAV1]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GLA]] | +0.50 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[BTN3A3]] | +0.50 | +0.47 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNN2]] | -0.54 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[TMEM170B]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[FAM3C]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MYL12A]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[FRY]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[ITGB5]] | -0.46 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[ACTB]] | -0.44 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[TXNDC17]] | -0.44 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[DOCK4]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[COL4A3]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ACTG1]] | -0.43 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[MMD]] | -0.43 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DGLUCY's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.421). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 54.4); signed map (60.0, 33.5). **Vector** length 88.9, 26.3% of its response variance represented; |z| ≥ 3 in 1,365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -16.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -18.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | D-glutamate cyclase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:91,060,333-91,225,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39975; previously C14orf159 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Carbon-oxygen lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3D6](https://www.uniprot.org/uniprotkb/Q7Z3D6) (D-glutamate cyclase, mitochondrial):

> D-glutamate cyclase that converts D-glutamate to 5-oxo-D-proline.

**Summary**, from NCBI Gene [80017](https://www.ncbi.nlm.nih.gov/gene/80017):

> Predicted to enable D-glutamate cyclase activity. Predicted to be involved in glutamate metabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20498) · Entrez [80017](https://www.ncbi.nlm.nih.gov/gene/80017) · UniProt [Q7Z3D6](https://www.uniprot.org/uniprotkb/Q7Z3D6) · Ensembl [ENSG00000133943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133943)

## Data

Gene col 5488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5488); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5488]; `tensor/DDL_lfc|DDL_z.npy` [5488]; `embed/gene_vectors.npy` [5488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5488 or target_col == 5488). Every well: [[DGLUCY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGLUCY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
