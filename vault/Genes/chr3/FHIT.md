---
symbol: "FHIT"
type: "gene"
col: 12111
ensembl_id: "ENSG00000189283"
name: "fragile histidine triad diadenosine triphosphatase"
location: "3p14.2"
module: 200
arm: "+"
pooled_cpm: 227.43
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 40
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# FHIT

*fragile histidine triad diadenosine triphosphatase* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.46× (z +4.8, q 9e-04, up in 34 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.170× (z -21.4, q 0e+00, down in 41 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.231× (z -18.4, q 0e+00, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMMP2L]] (+0.71, fdr 7e-06), [[WWOX]] (+0.68, fdr 7e-06), [[BABAM2]] (+0.66, fdr 7e-06); moves opposite to [[MAP3K3]] (-0.49, fdr 5e-05), [[KMT5C]] (-0.48, fdr 7e-05), [[GNRH1]] (-0.47, fdr 7e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[USP40]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +4.8 | 9e-04 | 34/42 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.3 | 0.006 | 31/41 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.33×** | +3.6 | 0.050 | 29/43 (SNU-1, C32, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.087 | 26/43 (HepG2/C3A, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.26× | +3.3 | 0.10 | 22/43 (C-33 A, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.27× | +3.0 | 0.25 | 22/42 (NCI-H2347, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.170×** | -21.4 | 0e+00 | 41/41 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.231×** | -18.4 | 0e+00 | 41/42 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.252×** | -17.3 | 0e+00 | 41/42 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.401×** | -16.2 | 0e+00 | 37/42 (LoVo, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.300×** | -15.1 | 0e+00 | 40/42 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.267×** | -14.0 | 1e-42 | 42/42 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -13.3 | 3e-38 | 38/43 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.366×** | -12.6 | 1e-34 | 41/42 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.159×** | -12.1 | 1e-31 | 42/43 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.182×** | -11.2 | 3e-27 | 40/42 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.444×** | -10.2 | 1e-22 | 40/42 (RKO, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.471×** | -9.4 | 2e-19 | 36/42 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.482×** | -9.1 | 3e-18 | 38/42 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.495×** | -8.8 | 5e-17 | 39/42 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.559×** | -7.3 | 1e-11 | 33/42 (C-33 A, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.697×** | -6.4 | 6e-09 | 39/43 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.610×** | -6.2 | 2e-08 | 26/42 (HCT15, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.596×** | -6.0 | 6e-08 | 39/41 (RKO, KATO III, …) | all doses, stronger at high dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.610×** | -5.9 | 7e-08 | 40/42 (RKO, NCI-H2347, …) | rises with dose | plate-row cell shift |
| [[Irinotecan (drug)]] 5 µM |  | **0.475×** | -4.9 | 2e-05 | 39/44 (RKO, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.767×** | -4.7 | 6e-05 | 33/43 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -4.2 | 5e-04 | 30/42 (CFPAC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 404 | 0 | 24 (16 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0722× (z -26.4) |
| [[SW48 (line)]] | wt | 812 | 0 | 22 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -18.2) |
| [[SNU-423 (line)]] | alt | 215 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -15.4) |
| [[LoVo (line)]] | wt | 332 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -33.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -22.0) |
| [[HCT15 (line)]] | alt | 594 | 0 | 16 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0630× (z -25.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -17.0) |
| [[SW480 (line)]] | alt | 266 | 0 | 16 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -22.4) |
| [[J82 (line)]] | alt | 295 | 0 | 13 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.112× (z -17.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 320 | 0 | 13 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -17.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -13.9) |
| [[LS 180 (line)]] | wt | 502 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -20.0) |
| [[RKO (line)]] | wt | 487 | 0 | 12 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0657× (z -25.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0534× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 513 | 0 | 12 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0906× (z -20.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 811 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.5) |
| [[SW1417 (line)]] | alt | 218 | 0 | 12 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -15.6) |
| [[CHP-212 (line)]] | wt | 340 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0985× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 614 | 0 | 11 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.1000× (z -25.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -19.3) |
| [[NCI-H1792 (line)]] | alt | 164 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -12.9) |
| [[COLO 205 (line)]] | alt | 321 | 0 | 10 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -19.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -18.1) |
| [[KATO III (line)]] | alt | 163 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.183× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0715× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -16.3) |
| [[C-33 A (line)]] | alt | 160 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -15.4) |
| [[HOP62 (line)]] | alt | 159 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -20.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -12.8) |
| [[SHP-77 (line)]] | alt | 360 | 0 | 9 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -23.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -17.9) |
| [[A-427 (line)]] | wt | 279 | 1 (1 ⚠) | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.62× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.187× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.265× (z -9.2) |
| [[A549 (line)]] | wt | 130 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -12.4) |
| [[C32 (line)]] | wt | 374 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -19.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 261 | 1 | 7 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.70× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.209× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.163× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 375 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -14.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.194× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.226× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 99.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -18.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -12.2) |
| [[BT-474 (line)]] | alt | 150 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -13.2) |
| [[HS-578T (line)]] | alt | 86.1 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 76.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.284× (z -10.9) |
| [[H4 (line)]] | wt | 89.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0823× (z -17.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.165× (z -12.5) |
| [[Hs 766T (line)]] | wt | 77.4 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -10.6) |
| [[SW 900 (line)]] | alt | 209 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.156× (z -13.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -11.5) |
| [[A498 (line)]] | wt | 104 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 77.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -10.4) |
| [[SW 1088 (line)]] | alt | 215 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0743× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -8.6) |
| [[A-172 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 259 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.176× (z -10.7) |
| [[AN3 CA (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 53.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 51.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMMP2L]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 | STRING 497 |
| [[WWOX]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 | STRING 938 |
| [[BABAM2]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 | same gene group |
| [[EXOC4]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[RAD51B]] | +0.62 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[SUMF1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[AFG1L]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LINC01473]] | +0.59 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[DIAPH2]] | +0.53 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[ZC3H12B]] | +0.51 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[TRIM16]] | +0.50 | +0.30 / +0.62 | both halves | 2e-04 |  |
| [[MMACHC]] | +0.50 | +0.40 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K3]] | -0.49 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[KMT5C]] | -0.48 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[GNRH1]] | -0.47 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[MXD4]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 | same gene group |
| [[SRGAP2D]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[MAP3K14-AS1]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[TNFRSF25]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[C2CD2L]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[RAB5B]] | -0.45 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[BNIPL]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[METTL21EP-1]] | -0.43 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[CHST7]] | -0.43 | -0.54 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises FHIT's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP40]] | B | FHIT activity raises USP40's level | lines that do not express FHIT (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without FHIT | 0.056 | ⚠ within organs, on part of the lines; also absent: PTGFRN, FBXO16; maybe low, not absent |

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.7, 30.9); signed map (10.0, -12.4). **Vector** length 105, 41.2% of its response variance represented; |z| ≥ 3 in 1,720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.2 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.3 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.5 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.9 | -21.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.9 | -14.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.4 | -6.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | fragile histidine triad diadenosine triphosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.2 — chr3:59,747,277-61,251,459 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FRA3B, AP3Aase |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Histidine triad superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [P49789](https://www.uniprot.org/uniprotkb/P49789) (Bis(5'-adenosyl)-triphosphatase):

> Possesses dinucleoside triphosphate hydrolase activity. Cleaves P(1)-P(3)-bis(5'-adenosyl) triphosphate (Ap3A) to yield AMP and ADP. Can also hydrolyze P(1)-P(4)-bis(5'-adenosyl) tetraphosphate (Ap4A), but has extremely low activity with ATP. Exhibits adenylylsulfatase activity, hydrolyzing adenosine 5'-phosphosulfate to yield AMP and sulfate. Exhibits adenosine 5'-monophosphoramidase activity, hydrolyzing purine nucleotide phosphoramidates with a single phosphate group such as adenosine …

**Summary**, from NCBI Gene [2272](https://www.ncbi.nlm.nih.gov/gene/2272):

> The protein encoded by this gene is a P1-P3-bis(5'-adenosyl) triphosphate hydrolase involved in purine metabolism. This gene encompasses the common fragile site FRA3B on chromosome 3, where carcinogen-induced damage can lead to translocations and aberrant transcripts. In fact, aberrant transcripts from this gene have been found in about half of all esophageal, stomach, and colon carcinomas. The encoded protein is also a tumor suppressor, as loss of its activity results in replication stress and …

**Accessions** — [HGNC:3701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3701) · Entrez [2272](https://www.ncbi.nlm.nih.gov/gene/2272) · UniProt [P49789](https://www.uniprot.org/uniprotkb/P49789) · Ensembl [ENSG00000189283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189283)

## Data

Gene col 12111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12111); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12111]; `tensor/DDL_lfc|DDL_z.npy` [12111]; `embed/gene_vectors.npy` [12111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12111 or target_col == 12111). Every well: [[FHIT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHIT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
