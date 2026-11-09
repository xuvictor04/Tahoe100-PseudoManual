---
symbol: "STAT2"
type: "gene"
col: 9978
ensembl_id: "ENSG00000170581"
name: "signal transducer and activator of transcription 2"
location: "12q13.3"
module: 32
arm: "+"
pooled_cpm: 75.59
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 50
n_dd_up_clean: 6
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 16
direction_downstream: 11
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# STAT2

*signal transducer and activator of transcription 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.31× (z +4.2, q 0.013, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -17.3, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -15.3, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2L6]] (+0.77, fdr 7e-06), [[PML]] (+0.76, fdr 7e-06), [[USP18]] (+0.75, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 11 go from it, the strongest it → [[PML]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.013 | 26/47 (SK-MEL-2, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.015 | 24/49 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.042 | 22/49 (SK-MEL-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.042 | 19/48 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.042 | 20/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.053 | 18/48 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.055 | 19/48 (SK-MEL-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.20× | +3.3 | 0.080 | 19/50 (SK-MEL-2, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.16 | 12/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.464×** | -17.3 | 0e+00 | 43/47 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -15.3 | 0e+00 | 44/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -15.3 | 0e+00 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.410×** | -14.2 | 2e-43 | 45/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -12.7 | 5e-35 | 44/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -10.8 | 4e-25 | 36/47 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.512×** | -10.2 | 1e-22 | 36/48 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.530×** | -10.1 | 5e-22 | 35/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.533×** | -9.6 | 5e-20 | 29/42 (AsPC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -9.5 | 1e-19 | 34/47 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.656×** | -9.4 | 2e-19 | 35/49 (LoVo, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.695×** | -8.1 | 2e-14 | 32/49 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -7.9 | 1e-13 | 35/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.607×** | -7.3 | 1e-11 | 27/44 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -7.0 | 8e-11 | 36/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.660×** | -6.6 | 2e-09 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.751×** | -6.4 | 5e-09 | 35/48 (RPMI-7951, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -6.4 | 5e-09 | 35/49 (CFPAC-1, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.689×** | -5.9 | 1e-07 | 29/48 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.699×** | -5.7 | 4e-07 | 29/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -5.3 | 3e-06 | 31/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.688×** | -5.2 | 3e-06 | 26/48 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.721×** | -5.2 | 5e-06 | 30/49 (LoVo, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 123 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -24.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.143× (z -15.1) |
| [[LoVo (line)]] | wt | 117 | 0 | 15 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 108 | 0 | 12 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -20.4) |
| [[COLO 205 (line)]] | alt | 168 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.319× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 122 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0730× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.370× (z -11.6) |
| [[A498 (line)]] | wt | 95.6 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -18.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.390× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 92.0 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0426× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -16.1) |
| [[BT-474 (line)]] | alt | 74.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.228× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 68.8 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 8 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0844× (z -14.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 97.0 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.326× (z -11.6) |
| [[KATO III (line)]] | alt | 71.8 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.229× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 26.9 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.220× (z -13.5) |
| [[SNU-423 (line)]] | alt | 128 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.479× (z -9.1) |
| [[SW 900 (line)]] | alt | 88.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -12.0) |
| [[SW480 (line)]] | alt | 52.4 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.293× (z -13.9) |
| [[SW1417 (line)]] | alt | 84.2 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -11.5) |
| [[PANC-1 (line)]] | alt | 45.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -10.4) |
| [[RKO (line)]] | wt | 96.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.388× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.475× (z -10.1) |
| [[A-172 (line)]] | wt | 101 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 110 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0950× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -10.1) |
| [[H4 (line)]] | wt | 82.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0483× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.186× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -11.7) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.555× (z -10.4) |
| [[HS-578T (line)]] | alt | 91.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 71.5 | 0 | 3 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.418× (z -9.0) |
| [[C-33 A (line)]] | alt | 80.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.346× (z -9.3) |
| [[HCT15 (line)]] | alt | 70.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 54.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -8.7) |
| [[HOP62 (line)]] | alt | 32.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.360× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -9.1) |
| [[HT-29 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.329× (z -8.5) |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -8.5) |
| [[SW 1271 (line)]] | alt | 48.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0796× (z -8.7) |
| [[SW48 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2L6]] | +0.77 | +0.70 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 544 |
| [[PML]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 588 |
| [[USP18]] | +0.75 | +0.68 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 957 |
| [[IFI6]] | +0.75 | +0.63 / +0.81 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 899 |
| [[MX1]] | +0.74 | +0.66 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 939 |
| [[CMPK2]] | +0.74 | +0.67 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 674 |
| [[OAS1]] | +0.74 | +0.67 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 880 |
| [[IRF9]] | +0.74 | +0.65 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 999 |
| [[SHFL]] | +0.73 | +0.67 / +0.77 | both halves | 7e-06 | STRING 425 |
| [[LAP3]] | +0.73 | +0.62 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI44]] | +0.73 | +0.68 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 717 |
| [[HERC5]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 722 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises STAT2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[MX1]] | B | MX1 activity strengthens STAT2's drug response | lines that do not express MX1 (19) vs lines expressing it (30) | the lines without MX1 respond 0.66× as strongly (z diff +2.10); strongest at Dinaciclib 0.5 µM: 0.85x vs 0.41x (z diff +4.2) | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity raises STAT2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without IFI6 | 0.016 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers STAT2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[TYMP]] | B | TYMP activity strengthens STAT2's drug response | lines that do not express TYMP (20) vs lines expressing it (29) | the lines without TYMP respond 0.63× as strongly (z diff +1.99); strongest at Homoharringtonine 0.5 µM: 0.74x vs 0.46x (z diff +3.6) | 0.020 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20; target measured in part of the lines; artifact flags |
| [[TRIM22]] | B | TRIM22 activity raises STAT2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without TRIM22 | 0.048 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CCDC194]] | B | CCDC194 activity raises STAT2's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without CCDC194 | 0.048 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[IFI44L]] | B | IFI44L activity raises STAT2's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without IFI44L | 0.051 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[BATF2]] | B | BATF2 activity raises STAT2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.53× lower at baseline in the lines without BATF2 | 0.057 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises STAT2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without PLSCR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises STAT2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without OAS2 | 0.066 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[MAP2K2]] | B | MAP2K2 activity lowers STAT2's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PML]] | C | STAT2's natural level strengthens PML's drug response | STAT2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.61; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | STAT2's natural level strengthens ADAR's drug response | STAT2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.52; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | STAT2's natural level strengthens TDRD7's drug response | STAT2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.37; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | STAT2's natural level strengthens IRF9's drug response | STAT2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.45; direction not clear | 0.018 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | STAT2's natural level strengthens IFIT1's drug response | STAT2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.24; direction not clear | 0.020 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | STAT2's natural level strengthens TRANK1's drug response | STAT2's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.38; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | STAT2's natural level strengthens USP18's drug response | STAT2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.32; direction not clear | 0.030 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | STAT2's natural level strengthens IFI35's drug response | STAT2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.43; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | STAT2's natural level strengthens PSMB9's drug response | STAT2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.36; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[PNPT1]] | C | STAT2's natural level strengthens PNPT1's drug response | STAT2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.62; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[REC8]] | C | STAT2's natural level strengthens REC8's drug response | STAT2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.45; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 54.2); signed map (66.8, 32.4). **Vector** length 131, 48.5% of its response variance represented; |z| ≥ 3 in 1,594 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.68 to 23); *Interferon gamma signaling* (reactome, mean cos +0.62 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.65 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.7 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -3.5 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.1 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.7 | -6.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.9 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.8 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,341,597-56,360,203 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STAT113 |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, PI3K_AKT_MTOR_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 18 pathways, smallest: Regulation of IFNA/IFNB signaling; Interleukin-20 family signaling; Evasion by RSV of host interferon responses |
| Matched by | ensembl_id |

**Function**, from UniProt [P52630](https://www.uniprot.org/uniprotkb/P52630) (Signal transducer and activator of transcription 2):

> Signal transducer and activator of transcription that mediates signaling by type I interferons (IFN-alpha and IFN-beta). Following type I IFN binding to cell surface receptors, Jak kinases (TYK2 and JAK1) are activated, leading to tyrosine phosphorylation of STAT1 and STAT2. The phosphorylated STATs dimerize, associate with IRF9/ISGF3G to form a complex termed ISGF3 transcription factor, that enters the nucleus. ISGF3 binds to the IFN stimulated response element (ISRE) to activate the …

**Summary**, from NCBI Gene [6773](https://www.ncbi.nlm.nih.gov/gene/6773):

> The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. In response to interferon (IFN), this protein forms a complex with STAT1 and IFN regulatory factor family protein p48 (ISGF3G), in which this protein acts as a transactivator, but lacks the …

**Accessions** — [HGNC:11363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11363) · Entrez [6773](https://www.ncbi.nlm.nih.gov/gene/6773) · UniProt [P52630](https://www.uniprot.org/uniprotkb/P52630) · Ensembl [ENSG00000170581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170581)

## Data

Gene col 9978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9978); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9978]; `tensor/DDL_lfc|DDL_z.npy` [9978]; `embed/gene_vectors.npy` [9978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9978 or target_col == 9978). Every well: [[STAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
