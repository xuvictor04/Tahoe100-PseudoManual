---
symbol: "AGTPBP1"
type: "gene"
col: 5642
ensembl_id: "ENSG00000135049"
name: "ATP/GTP binding carboxypeptidase 1"
location: "9q21.33"
module: 113
arm: "+"
pooled_cpm: 138.94
n_lines_expressing: 47
n_dd_up: 27
n_dd_down: 22
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# AGTPBP1

*ATP/GTP binding carboxypeptidase 1* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +17.4, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.529× (z -14.2, q 8e-43, down in 34 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.723× (z -7.5, q 4e-12, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TANC2]] (+0.66, fdr 7e-06), [[ZDHHC9]] (+0.61, fdr 1e-05), [[CLASP1]] (+0.60, fdr 7e-06); moves opposite to [[SLC13A3]] (-0.53, fdr 0.001, ⚠ not reproduced), [[PPP1R3F]] (-0.53, fdr 8e-05), [[ERCC6L2-AS1]] (-0.51, fdr 2e-04), [[LINC01134]] (-0.51, fdr 1e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[DTNB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 1 with an alert ⚠; shown: the 15 strongest. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +17.4 | 0e+00 | 41/45 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +16.5 | 0e+00 | 42/45 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +15.9 | 0e+00 | 40/45 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +14.7 | 0e+00 | 42/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +11.7 | 2e-29 | 32/45 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +10.8 | 3e-25 | 33/45 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.54×** | +10.8 | 4e-25 | 43/46 (HT-29, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +10.5 | 4e-24 | 36/45 (LS 180, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +10.3 | 3e-23 | 34/45 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +9.9 | 3e-21 | 36/45 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +6.6 | 2e-09 | 31/46 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +6.6 | 2e-09 | 26/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +6.0 | 7e-08 | 30/44 (NCI-H460, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.28×** | +5.6 | 8e-07 | 25/45 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-06 | 25/46 (NCI-H460, H4, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 18 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -14.2 | 8e-43 | 34/42 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -13.9 | 1e-41 | 37/46 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.539×** | -13.8 | 8e-41 | 37/44 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -13.3 | 2e-38 | 33/43 (C-33 A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -12.7 | 5e-35 | 37/44 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.633×** | -10.6 | 3e-24 | 38/45 (C32, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.681×** | -8.9 | 5e-17 | 33/45 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.705×** | -8.1 | 3e-14 | 28/45 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -7.5 | 4e-12 | 29/45 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.730×** | -7.3 | 2e-11 | 32/45 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.730×** | -7.3 | 2e-11 | 32/45 (C32, SNU-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.761×** | -6.3 | 1e-08 | 27/45 (C32, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.839× | -5.8 | 4e-07 | 19/45 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -5.7 | 4e-07 | 24/45 (SW48, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.783×** | -5.5 | 2e-06 | 22/45 (NCI-H2030, C32, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.629×** | -5.4 | 3e-06 | 24/45 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.678×** | -4.5 | 2e-04 | 23/45 (SW1417, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.003 | 17/45 (SW1417, HepG2/C3A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.891× | -3.8 | 0.004 | 5/46 (Panc 03.27, HCT15, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.852× | -3.7 | 0.005 | 16/45 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.730×** | -3.7 | 0.007 | 14/44 (SW 900, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.900× | -3.5 | 0.012 | 8/46 (CFPAC-1, C32, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.780×** | -3.3 | 0.025 | 10/45 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.038 | 17/45 (SW48, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.765×** | -3.1 | 0.039 | 13/45 (SK-MEL-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.913× | -3.0 | 0.048 | 12/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.886× | -2.8 | 0.086 | 16/45 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 483 | 12 | 9 (8 ⚠) | [[Trametinib (drug)]] 5 µM 4.74× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.298× (z -11.1) |
| [[C32 (line)]] | wt | 227 | 0 | 15 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.340× (z -10.3) |
| [[KATO III (line)]] | alt | 97.5 | 8 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.417× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 226 | 0 | 12 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -23.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 132 | 5 | 6 (6 ⚠) | [[Belinostat (drug)]] 5 µM 2.50× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -16.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 115 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 91.2 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +14.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 316 | 1 | 8 (7 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.65× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -16.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 153 | 6 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.94× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 232 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0993× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.319× (z -12.4) |
| [[SNU-1 (line)]] | wt | 141 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.187× (z -18.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 364 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -16.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 145 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 272 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -17.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 138 | 7 | 0 | [[Belinostat (drug)]] 5 µM 2.50× (z +12.5) | — |
| [[SW480 (line)]] | alt | 77.1 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.415× (z -9.8) ⚠ toxic |
| [[A549 (line)]] | wt | 157 | 3 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.15× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 101 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -10.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 37.0 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 57.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 148 | 4 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.73× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.407× (z -11.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 75.6 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.74× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 272 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.6 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.305× (z -12.8) ⚠ cell-cycle shift, explains ~76% of this change |
| [[Panc 03.27 (line)]] | alt | 88.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 115 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 120 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0752× (z -30.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 99.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -18.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -28.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 107 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -12.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 78.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.6) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0907× (z -10.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 98.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 182 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -12.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 64.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 45.8 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.59× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 103 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -8.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 210 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.335× (z -10.3) |
| [[SHP-77 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 27.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANC2]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZDHHC9]] | +0.61 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CLASP1]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SSBP2]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CTNNBL1]] | +0.60 | +0.53 / +0.41 | both halves | 4e-05 | same gene group |
| [[MAPT]] | +0.59 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[SERGEF]] | +0.59 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[RNF130]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[HACE1]] | +0.56 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[EXOC6B]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[TTLL7]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 | pathway: Carboxyterminal post-translational modifications of tubulin; STRING 442 |
| [[RAC3]] | +0.55 | +0.41 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC13A3]] | -0.53 | -0.46 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[PPP1R3F]] | -0.53 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[ERCC6L2-AS1]] | -0.51 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[LINC01134]] | -0.51 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.51 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[ANKRD17-DT]] | -0.51 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[MIRLET7IHG]] | -0.50 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[SOCS2-AS1]] | -0.50 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[THAP2]] | -0.50 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[RFX3-DT]] | -0.50 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[ERMAP]] | -0.49 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[LINC03048]] | -0.49 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[PCF11]] | -0.49 | -0.37 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers AGTPBP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RFX3-DT]] | C | RFX3-DT activity raises AGTPBP1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without RFX3-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTNB]] | C | AGTPBP1 activity raises DTNB's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |
| [[VPS13A]] | C | AGTPBP1 activity raises VPS13A's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |
| [[DNM1L]] | C | AGTPBP1 activity raises DNM1L's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |
| [[TMEM161A]] | C | AGTPBP1 activity raises TMEM161A's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |
| [[FTO]] | C | AGTPBP1 activity raises FTO's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.32× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |
| [[UBE2Q2P2]] | C | AGTPBP1 activity raises UBE2Q2P2's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without AGTPBP1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent |
| [[VPS13D]] | C | AGTPBP1 activity raises VPS13D's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without AGTPBP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.8, -9.1); signed map (-28.4, 24.2). **Vector** length 130, 43.4% of its response variance represented; |z| ≥ 3 in 1,789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.5 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +14.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.0 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +3.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.8 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +10.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.8 | -13.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.5 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.6 | -5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -7.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.9 | -1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | ATP/GTP binding carboxypeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:85,546,539-85,742,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1035, Nna1, CCP1 |
| Gene groups (HGNC) | M14 carboxypeptidases; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPW5](https://www.uniprot.org/uniprotkb/Q9UPW5) (Cytosolic carboxypeptidase 1):

> Metallocarboxypeptidase that mediates protein deglutamylation of tubulin and non-tubulin target proteins. Catalyzes the removal of polyglutamate side chains present on the gamma-carboxyl group of glutamate residues within the C-terminal tail of alpha- and beta-tubulin. Specifically cleaves tubulin long-side-chains, while it is not able to remove the branching point glutamate. Also catalyzes the removal of polyglutamate residues from the carboxy-terminus of alpha-tubulin as well as non-tubulin …

**Summary**, from NCBI Gene [23287](https://www.ncbi.nlm.nih.gov/gene/23287):

> NNA1 is a zinc carboxypeptidase that contains nuclear localization signals and an ATP/GTP-binding motif that was initially cloned from regenerating spinal cord neurons of the mouse.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:17258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17258) · Entrez [23287](https://www.ncbi.nlm.nih.gov/gene/23287) · UniProt [Q9UPW5](https://www.uniprot.org/uniprotkb/Q9UPW5) · Ensembl [ENSG00000135049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135049)

## Data

Gene col 5642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5642); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5642]; `tensor/DDL_lfc|DDL_z.npy` [5642]; `embed/gene_vectors.npy` [5642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5642 or target_col == 5642). Every well: [[AGTPBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGTPBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
