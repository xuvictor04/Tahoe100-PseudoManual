---
symbol: "VWA8"
type: "gene"
col: 2269
ensembl_id: "ENSG00000102763"
name: "von Willebrand factor A domain containing 8"
location: "13q14.11"
module: 4
arm: "+"
pooled_cpm: 89.74
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# VWA8

*von Willebrand factor A domain containing 8* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.66× (z +7.1, q 7e-10, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.70× (z +7.0, q 7e-10, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -9.6, q 3e-19, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDIN1]] (+0.80, fdr 7e-06), [[NAA25]] (+0.76, fdr 7e-06), [[CHCHD6]] (+0.72, fdr 7e-06); moves opposite to [[FAM117A]] (-0.65, fdr 1e-05), [[ZFYVE1]] (-0.64, fdr 7e-06), [[AAMDC]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PIR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +7.1 | 7e-10 | 36/48 (AsPC-1, SNU-423, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +7.0 | 7e-10 | 39/48 (COLO 205, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +6.6 | 9e-09 | 35/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +6.4 | 2e-08 | 32/48 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.57×** | +6.2 | 5e-08 | 35/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.52×** | +5.8 | 7e-07 | 33/48 (AsPC-1, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.7 | 1e-06 | 34/48 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 2e-06 | 37/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.1 | 2e-05 | 36/48 (J82, PANC-1, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 4e-04 | 33/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.38×** | +4.5 | 4e-04 | 28/48 (SNU-423, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.5 | 4e-04 | 30/48 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.001 | 29/47 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.003 | 28/49 (J82, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 27/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 27/48 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.022 | 25/49 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.049 | 19/48 (PANC-1, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.079 | 18/48 (CFPAC-1, A549, …) | all doses, flat |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.089 | 17/48 (Panc 03.27, AN3 CA, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -9.6 | 3e-19 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.653×** | -8.4 | 9e-15 | 30/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -7.7 | 3e-12 | 39/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -7.4 | 2e-11 | 32/49 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -6.2 | 7e-08 | 34/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -6.0 | 1e-07 | 33/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.672×** | -5.6 | 2e-06 | 34/48 (NCI-H661, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.750×** | -4.0 | 0.004 | 27/49 (NCI-H23, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.763×** | -3.8 | 0.009 | 23/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.777×** | -3.5 | 0.022 | 25/48 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.838× | -3.5 | 0.022 | 21/49 (C-33 A, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.074 | 24/50 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 111 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -17.3) |
| [[LoVo (line)]] | wt | 160 | 2 (1 ⚠) | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -20.0) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 67.3 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.16× (z +9.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -18.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.2) |
| [[PANC-1 (line)]] | alt | 79.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -16.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -14.4) |
| [[SNU-1 (line)]] | wt | 158 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -12.1) |
| [[SW1417 (line)]] | alt | 93.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -13.5) |
| [[A498 (line)]] | wt | 69.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[COLO 205 (line)]] | alt | 146 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.46× (z +12.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.48× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.1) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.5) |
| [[RKO (line)]] | wt | 162 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -12.1) |
| [[SHP-77 (line)]] | alt | 106 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0818× (z -25.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -10.2) |
| [[A-427 (line)]] | wt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 101 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -10.9) |
| [[KATO III (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 85.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.5) |
| [[SW480 (line)]] | alt | 126 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -12.9) |
| [[HOP62 (line)]] | alt | 39.3 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.04× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.49× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -17.8) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 70.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -15.0) |
| [[SW48 (line)]] | wt | 216 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.359× (z -9.4) |
| [[A549 (line)]] | wt | 71.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.7) ⚠ cell-cycle shift, explains ~64% of this change |
| [[AN3 CA (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.6) ⚠ cell-cycle shift, explains ~64% of this change |
| [[CFPAC-1 (line)]] | alt | 28.9 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.59× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.422× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 62.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.6) ⚠ cell-cycle shift, explains ~64% of this change |
| [[Hs 766T (line)]] | wt | 78.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.7) |
| [[J82 (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[LOX-IMVI (line)]] | wt | 95.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.414× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 95.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.342× (z -9.4) |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -8.8) |
| [[SW 900 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIN1]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[NAA25]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | same gene group |
| [[CHCHD6]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PTPN4]] | +0.71 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[BLMH]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[NAA15]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[POLR3B]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[HERC2]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | same gene group |
| [[MIPOL1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.65 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.64 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.62 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TMEM106A]] | -0.60 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ZNF490]] | -0.59 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[LINC01772]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIR]] | B | PIR activity raises VWA8's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without PIR | 0.008 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |
| [[NFIA]] | B | NFIA activity raises VWA8's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without NFIA | 0.087 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[LRRC8D]] | C | LRRC8D activity raises VWA8's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.2, -34.2); signed map (-12.8, -50.2). **Vector** length 138, 49.2% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *tRNA processing* (reactome, mean cos +0.53 to 10); *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +10.2 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.0 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.3 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -7.3 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | von Willebrand factor A domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,566,835-41,961,120 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P7BP2; previously KIAA0564 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [A3KMH1](https://www.uniprot.org/uniprotkb/A3KMH1) (von Willebrand factor A domain-containing protein 8):

> Exhibits ATPase activity in vitro.

**Summary**, from NCBI Gene [23078](https://www.ncbi.nlm.nih.gov/gene/23078):

> Predicted to enable ATP hydrolysis activity. Located in mitochondrion and peroxisome. Implicated in retinitis pigmentosa 97. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29071) · Entrez [23078](https://www.ncbi.nlm.nih.gov/gene/23078) · UniProt [A3KMH1](https://www.uniprot.org/uniprotkb/A3KMH1) · Ensembl [ENSG00000102763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102763)

## Data

Gene col 2269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2269); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2269]; `tensor/DDL_lfc|DDL_z.npy` [2269]; `embed/gene_vectors.npy` [2269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2269 or target_col == 2269). Every well: [[VWA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VWA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
